# v16.0.2 → v16.0.3 · 最優先の変更候補 (90)

[一覧の目次](README.md)

<a id="compare-48735a9cb1c887375812042d1cef2146"></a>

### [`00c377f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c377f8.md) → [`00c387ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c387ec.md) __cxa_guard_abort

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58060.md) · 呼出先 4件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md) [`00c5e290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e290.md)
- 新版 呼出元 1件 [`00c59030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59030.md) · 呼出先 4件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c5c740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c740.md) [`00c5c750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c750.md) [`00c5f260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38804",
      "incomplete_value": false,
      "site": "00c38808",
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
            "const:ac8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37810",
      "incomplete_value": false,
      "site": "00c37814",
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
            "const:b08:8"
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
      "definition_site": "00c38820",
      "incomplete_value": false,
      "site": "00c38824",
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
            "const:ac8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3782c",
      "incomplete_value": false,
      "site": "00c37830",
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
            "const:b08:8"
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
      "definition_site": "00c38834",
      "incomplete_value": false,
      "site": "00c38838",
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
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37840",
      "incomplete_value": false,
      "site": "00c37844",
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
            "const:b30:8"
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
      "00c38804",
      "PARAM",
      [
        "storage",
        "01128b08",
        null,
        null
      ]
    ],
    [
      "00c38820",
      "PARAM",
      [
        "storage",
        "01128b08",
        null,
        null
      ]
    ],
    [
      "00c38834",
      "PARAM",
      [
        "storage",
        "01128b30",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c38804",
      "PARAM",
      [
        "storage",
        "01129ac8",
        null,
        null
      ]
    ],
    [
      "00c38820",
      "PARAM",
      [
        "storage",
        "01129ac8",
        null,
        null
      ]
    ],
    [
      "00c38834",
      "PARAM",
      [
        "storage",
        "01129af0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c377f8.md#insn-00c37814) · [`00c37830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c377f8.md#insn-00c37830) · [`00c37844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c377f8.md#insn-00c37844)
- 新版 [`00c38808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c387ec.md#insn-00c38808) · [`00c38824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c387ec.md#insn-00c38824) · [`00c38838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c387ec.md#insn-00c38838)

~~~diff
- 00c37814 ["INT_ADD", "register:40f0:8", ["const:c37814:8", "const:4:8"]]
- 00c37814 ["CALL", null, ["callee:00c5c740:8"]]
+ 00c38808 ["INT_ADD", "register:40f0:8", ["const:c38808:8", "const:4:8"]]
+ 00c38808 ["CALL", null, ["callee:00c5c740:8"]]
- 00c37814 bytes d78f0094
+ 00c38808 bytes ce8f0094
- 00c37830 ["INT_ADD", "register:40f0:8", ["const:c37830:8", "const:4:8"]]
- 00c37830 ["CALL", null, ["callee:00c5c750:8"]]
+ 00c38824 ["INT_ADD", "register:40f0:8", ["const:c38824:8", "const:4:8"]]
+ 00c38824 ["CALL", null, ["callee:00c5c750:8"]]
- 00c37830 bytes d48f0094
+ 00c38824 bytes cb8f0094
- 00c37844 ["INT_ADD", "register:40f0:8", ["const:c37844:8", "const:4:8"]]
- 00c37844 ["CALL", null, ["callee:00c5f260:8"]]
+ 00c38838 ["INT_ADD", "register:40f0:8", ["const:c38838:8", "const:4:8"]]
+ 00c38838 ["CALL", null, ["callee:00c5f260:8"]]
- 00c37844 bytes 939a0094
+ 00c38838 bytes 8a9a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e876f818f2e79819af894562d050c18"></a>

### [`00c37894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37894.md) → [`00c38888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38888.md) FUN_00c38888

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c5c750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c750.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c388a0",
      "incomplete_value": false,
      "site": "00c388a4",
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
            "const:ac8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c378ac",
      "incomplete_value": false,
      "site": "00c378b0",
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
            "const:b08:8"
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
      "definition_site": "00c388c4",
      "incomplete_value": true,
      "site": "00c388c8",
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
            "const:eba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c378d0",
      "incomplete_value": true,
      "site": "00c378d4",
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
            "const:e7a:8"
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
      "00c388a0",
      "PARAM",
      [
        "storage",
        "01128b08",
        null,
        null
      ]
    ],
    [
      "00c388c4",
      "PARAM",
      [
        "storage",
        "002a0e7a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c388a0",
      "PARAM",
      [
        "storage",
        "01129ac8",
        null,
        null
      ]
    ],
    [
      "00c388c4",
      "PARAM",
      [
        "storage",
        "002a0eba",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c378b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37894.md#insn-00c378b0) · [`00c378d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37894.md#insn-00c378d4) · [`00c378a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37894.md#insn-00c378a8)
- 新版 [`00c388a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38888.md#insn-00c388a4) · [`00c388c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38888.md#insn-00c388c8) · [`00c3889c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38888.md#insn-00c3889c)

~~~diff
- 00c378b0 ["INT_ADD", "register:40f0:8", ["const:c378b0:8", "const:4:8"]]
- 00c378b0 ["CALL", null, ["callee:00c5c750:8"]]
+ 00c388a4 ["INT_ADD", "register:40f0:8", ["const:c388a4:8", "const:4:8"]]
+ 00c388a4 ["CALL", null, ["callee:00c5c750:8"]]
- 00c378b0 bytes b48f0094
+ 00c388a4 bytes ab8f0094
- 00c378d4 ["INT_ADD", "register:40f0:8", ["const:c378d4:8", "const:4:8"]]
- 00c378d4 ["CALL", null, ["callee:00c3909c:8"]]
+ 00c388c8 ["INT_ADD", "register:40f0:8", ["const:c388c8:8", "const:4:8"]]
+ 00c388c8 ["CALL", null, ["callee:00c3909c:8"]]
- 00c378d4 bytes f5010094
+ 00c388c8 bytes f5010094
- 00c378a8 ["COPY", "register:4000:8", ["const:1128000:8"]]
+ 00c3889c ["COPY", "register:4000:8", ["const:1129000:8"]]
- 00c378a8 bytes 802700b0
+ 00c3889c bytes 802700b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca6060d5f0e6b3df71baf78a472398e0"></a>

### [`00c37930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37930.md) → [`00c38924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38924.md) FUN_00c38924

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c3794c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3794c.md) [`00c52f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52f80.md) · 呼出先 1件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md)
- 新版 呼出元 2件 [`00c38940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38940.md) [`00c53f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53f74.md) · 呼出先 1件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38938",
      "incomplete_value": true,
      "site": "00c3893c",
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
            "const:f45:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37944",
      "incomplete_value": true,
      "site": "00c37948",
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
            "const:e7a:8"
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
      "00c38938",
      "PARAM",
      [
        "storage",
        "002a2e7a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c38938",
      "PARAM",
      [
        "storage",
        "002a2f45",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37930.md#insn-00c37948) · [`00c3793c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37930.md#insn-00c3793c) · [`00c37944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37930.md#insn-00c37944)
- 新版 [`00c3893c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38924.md#insn-00c3893c) · [`00c38930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38924.md#insn-00c38930) · [`00c38938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38924.md#insn-00c38938)

~~~diff
- 00c37948 ["INT_ADD", "register:40f0:8", ["const:c37948:8", "const:4:8"]]
- 00c37948 ["CALL", null, ["callee:00c3909c:8"]]
+ 00c3893c ["INT_ADD", "register:40f0:8", ["const:c3893c:8", "const:4:8"]]
+ 00c3893c ["CALL", null, ["callee:00c3909c:8"]]
- 00c37948 bytes d8010094
+ 00c3893c bytes d8010094
- 00c3793c ["COPY", "register:0:8", ["register:4000:8"]]
- 00c3793c ["INT_ADD", "register:40f0:8", ["const:c3793c:8", "const:4:8"]]
- 00c3793c ["CALLIND", null, ["register:0:8"]]
+ 00c38930 ["COPY", "register:0:8", ["register:4000:8"]]
+ 00c38930 ["INT_ADD", "register:40f0:8", ["const:c38930:8", "const:4:8"]]
+ 00c38930 ["CALLIND", null, ["register:0:8"]]
- 00c3793c bytes 00003fd6
+ 00c38930 bytes 00003fd6
- 00c37944 ["COPY", "tmp:0:8", ["const:e7a:8"]]
- 00c37944 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c37944 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c37944 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c38938 ["COPY", "tmp:0:8", ["const:f45:8"]]
+ 00c38938 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c38938 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c38938 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c37944 bytes 00e83991
+ 00c38938 bytes 00143d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8df771db2ddc2b27e84aa08f0bde8b18"></a>

### [`00c3797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3797c.md) → [`00c38970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38970.md) FUN_00c38970

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`00c378f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c378f0.md) [`00c52094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52094.md) [`00c5219c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5219c.md) [`00c52364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52364.md) [`00c52614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52614.md) · 呼出先 1件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md)
- 新版 呼出元 8件 [`00c388e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c388e4.md) [`00c53088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53088.md) [`00c53190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53190.md) [`00c53358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53358.md) [`00c53608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c53/00c53608.md) · 呼出先 1件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38984",
      "incomplete_value": false,
      "site": "00c38988",
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
            "const:a4b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37990",
      "incomplete_value": false,
      "site": "00c37994",
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
            "const:8f3:8"
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
      "00c38984",
      "PARAM",
      [
        "storage",
        "002a88f3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c38984",
      "PARAM",
      [
        "storage",
        "002a8a4b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3797c.md#insn-00c37994) · [`00c37988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3797c.md#insn-00c37988) · [`00c37990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3797c.md#insn-00c37990)
- 新版 [`00c38988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38970.md#insn-00c38988) · [`00c3897c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38970.md#insn-00c3897c) · [`00c38984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38970.md#insn-00c38984)

~~~diff
- 00c37994 ["INT_ADD", "register:40f0:8", ["const:c37994:8", "const:4:8"]]
- 00c37994 ["CALL", null, ["callee:00c3909c:8"]]
+ 00c38988 ["INT_ADD", "register:40f0:8", ["const:c38988:8", "const:4:8"]]
+ 00c38988 ["CALL", null, ["callee:00c3909c:8"]]
- 00c37994 bytes c5010094
+ 00c38988 bytes c5010094
- 00c37988 ["COPY", "register:0:8", ["register:4000:8"]]
- 00c37988 ["INT_ADD", "register:40f0:8", ["const:c37988:8", "const:4:8"]]
- 00c37988 ["CALLIND", null, ["register:0:8"]]
+ 00c3897c ["COPY", "register:0:8", ["register:4000:8"]]
+ 00c3897c ["INT_ADD", "register:40f0:8", ["const:c3897c:8", "const:4:8"]]
+ 00c3897c ["CALLIND", null, ["register:0:8"]]
- 00c37988 bytes 00003fd6
+ 00c3897c bytes 00003fd6
- 00c37990 ["COPY", "tmp:0:8", ["const:8f3:8"]]
- 00c37990 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c37990 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c37990 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c38984 ["COPY", "tmp:0:8", ["const:a4b:8"]]
+ 00c38984 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c38984 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c38984 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c37990 bytes 00cc2391
+ 00c38984 bytes 002c2991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26083f121bbf4a45add0bc2d64afe340"></a>

### [`00c379c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c379c0.md) → [`00c389b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c389b4.md) FUN_00c389b4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00c378f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c378f0.md) [`00c37968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37968.md) [`00c37b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37b60.md) · 呼出先 6件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c383cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c383cc.md) [`00c51ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ee4.md) [`00c51ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ef0.md) [`00c5ee70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee70.md)
- 新版 呼出元 3件 [`00c388e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c388e4.md) [`00c3895c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c3895c.md) [`00c38b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38b54.md) · 呼出先 6件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c393c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c393c0.md) [`00c52ed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52ed8.md) [`00c52ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52ee4.md) [`00c5fe40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fe40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.78% / 新版 91.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c389dc",
      "incomplete_value": false,
      "site": "00c389e0",
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
            "const:ff4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c379e8",
      "incomplete_value": false,
      "site": "00c379ec",
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
            "const:faa:8"
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
      "definition_site": "00c38a20",
      "incomplete_value": false,
      "site": "00c38a28",
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
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37a2c",
      "incomplete_value": false,
      "site": "00c37a34",
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
            "const:861:8"
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
      "definition_site": "00c38a24",
      "incomplete_value": true,
      "site": "00c38a28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37a30",
      "incomplete_value": true,
      "site": "00c37a34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:950:8"
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
      "00c389dc",
      "PARAM",
      [
        "storage",
        "002c1faa",
        null,
        "string"
      ]
    ],
    [
      "00c38a20",
      "PARAM",
      [
        "storage",
        "002b0861",
        null,
        "string"
      ]
    ],
    [
      "00c38a24",
      "READ",
      [
        "storage",
        "00ca4950",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c389dc",
      "PARAM",
      [
        "storage",
        "002c1ff4",
        null,
        "string"
      ]
    ],
    [
      "00c38a20",
      "PARAM",
      [
        "storage",
        "002b0938",
        null,
        "string"
      ]
    ],
    [
      "00c38a24",
      "READ",
      [
        "storage",
        "00ca5920",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c379ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c379c0.md#insn-00c379ec) · [`00c37a34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c379c0.md#insn-00c37a34) · [`00c37ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c379c0.md#insn-00c37ac8)
- 新版 [`00c389e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c389b4.md#insn-00c389e0) · [`00c38a28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c389b4.md#insn-00c38a28) · [`00c38abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c389b4.md#insn-00c38abc)

~~~diff
- 00c379ec ["INT_ADD", "register:40f0:8", ["const:c379ec:8", "const:4:8"]]
- 00c379ec ["CALL", null, ["callee:00c3909c:8"]]
+ 00c389e0 ["INT_ADD", "register:40f0:8", ["const:c389e0:8", "const:4:8"]]
+ 00c389e0 ["CALL", null, ["callee:00c3909c:8"]]
- 00c379ec bytes af010094
+ 00c389e0 bytes af010094
- 00c37a34 ["INT_ADD", "register:40f0:8", ["const:c37a34:8", "const:4:8"]]
- 00c37a34 ["CALL", null, ["callee:00c3909c:8"]]
+ 00c38a28 ["INT_ADD", "register:40f0:8", ["const:c38a28:8", "const:4:8"]]
+ 00c38a28 ["CALL", null, ["callee:00c3909c:8"]]
- 00c37a34 bytes 9d010094
+ 00c38a28 bytes 9d010094
- 00c37ac8 ["INT_ADD", "register:40f0:8", ["const:c37ac8:8", "const:4:8"]]
- 00c37ac8 ["CALL", null, ["callee:00c3909c:8"]]
+ 00c38abc ["INT_ADD", "register:40f0:8", ["const:c38abc:8", "const:4:8"]]
+ 00c38abc ["CALL", null, ["callee:00c3909c:8"]]
- 00c37ac8 bytes 78010094
+ 00c38abc bytes 78010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4cdee421346a0dc7f546e6a273e4bc5"></a>

### [`00c37b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37b0c.md) → [`00c38b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38b00.md) FUN_00c38b00

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`00c378dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c378dc.md) [`00c3794c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3794c.md) [`00c37b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37b2c.md) · 呼出先 1件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)
- 新版 呼出元 3件 [`00c388d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c388d0.md) [`00c38940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38940.md) [`00c38b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38b20.md) · 呼出先 1件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c38b18",
      "incomplete_value": false,
      "site": "00c38b18",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37b24",
      "incomplete_value": false,
      "site": "00c37b24",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c38b14",
      "incomplete_value": false,
      "site": "00c38b18",
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
            "const:941:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37b20",
      "incomplete_value": false,
      "site": "00c37b24",
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
            "const:86a:8"
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
      "00c38b18",
      "WRITE",
      [
        "storage",
        "00ca4950",
        null,
        "pointer"
      ]
    ],
    [
      "00c38b18",
      "DATA",
      [
        "storage",
        "002b186a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c38b18",
      "WRITE",
      [
        "storage",
        "00ca5920",
        null,
        "pointer"
      ]
    ],
    [
      "00c38b18",
      "DATA",
      [
        "storage",
        "002b1941",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37b0c.md#insn-00c37b24) · [`00c37b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37b0c.md#insn-00c37b18) · [`00c37b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37b0c.md#insn-00c37b20)
- 新版 [`00c38b18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38b00.md#insn-00c38b18) · [`00c38b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38b00.md#insn-00c38b0c) · [`00c38b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38b00.md#insn-00c38b14)

~~~diff
- 00c37b24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
- 00c37b24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c38b18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:920:8"]]
+ 00c38b18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00c37b24 bytes 09a904f9
+ 00c38b18 bytes 099104f9
- 00c37b18 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 00c38b0c ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 00c37b18 bytes 680300b0
+ 00c38b0c bytes 680300b0
- 00c37b20 ["COPY", "tmp:0:8", ["const:86a:8"]]
- 00c37b20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c37b20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c37b20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c38b14 ["COPY", "tmp:0:8", ["const:941:8"]]
+ 00c38b14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c38b14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c38b14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c37b20 bytes 29a92191
+ 00c38b14 bytes 29052591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8a5a4fd15eb8810a151fbd8608e95c2"></a>

### [`00c37c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c28.md) → [`00c38c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c1c.md) __cxa_deleted_virtual

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c38c2c",
      "incomplete_value": false,
      "site": "00c38c30",
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
            "const:eb7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37c38",
      "incomplete_value": false,
      "site": "00c37c3c",
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
            "const:de8:8"
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
      "00c38c2c",
      "PARAM",
      [
        "storage",
        "002b5de8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c38c2c",
      "PARAM",
      [
        "storage",
        "002b5eb7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c28.md#insn-00c37c3c) · [`00c37c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c28.md#insn-00c37c38)
- 新版 [`00c38c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c1c.md#insn-00c38c30) · [`00c38c2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c1c.md#insn-00c38c2c)

~~~diff
- 00c37c3c ["INT_ADD", "register:40f0:8", ["const:c37c3c:8", "const:4:8"]]
- 00c37c3c ["CALL", null, ["callee:00c3909c:8"]]
+ 00c38c30 ["INT_ADD", "register:40f0:8", ["const:c38c30:8", "const:4:8"]]
+ 00c38c30 ["CALL", null, ["callee:00c3909c:8"]]
- 00c37c3c bytes 1b010094
+ 00c38c30 bytes 1b010094
- 00c37c38 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 00c37c38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c37c38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c37c38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c38c2c ["COPY", "tmp:0:8", ["const:eb7:8"]]
+ 00c38c2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c38c2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c38c2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c37c38 bytes 00a03791
+ 00c38c2c bytes 00dc3a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eeac738a718a8053af49536607099435"></a>

### [`00c37c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c74.md) → [`00c38c68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c68.md) _ZNKSt9exception4whatEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c38c70",
      "incomplete_value": false,
      "site": "00c38c74",
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
            "const:eca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37c7c",
      "incomplete_value": false,
      "site": "00c37c80",
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
            "const:dff:8"
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
      "00c38c70",
      "DATA",
      [
        "storage",
        "002a3dff",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c38c70",
      "DATA",
      [
        "storage",
        "002a3eca",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c74.md#insn-00c37c7c)
- 新版 [`00c38c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38c68.md#insn-00c38c70)

~~~diff
- 00c37c7c ["COPY", "tmp:0:8", ["const:dff:8"]]
- 00c37c7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c37c7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c37c7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c38c70 ["COPY", "tmp:0:8", ["const:eca:8"]]
+ 00c38c70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c38c70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c38c70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c37c7c bytes 00fc3791
+ 00c38c70 bytes 00283b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2479eab0ca60820347d6d404490d3bf7"></a>

### [`00c37cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37cb0.md) → [`00c38ca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38ca4.md) _ZNKSt13bad_exception4whatEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c38cac",
      "incomplete_value": false,
      "site": "00c38cb0",
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
            "const:5ea:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37cb8",
      "incomplete_value": false,
      "site": "00c37cbc",
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
            "const:51d:8"
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
      "00c38cac",
      "DATA",
      [
        "storage",
        "002ae51d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c38cac",
      "DATA",
      [
        "storage",
        "002ae5ea",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37cb0.md#insn-00c37cb8)
- 新版 [`00c38cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38ca4.md#insn-00c38cac)

~~~diff
- 00c37cb8 ["COPY", "tmp:0:8", ["const:51d:8"]]
- 00c37cb8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c37cb8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c37cb8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c38cac ["COPY", "tmp:0:8", ["const:5ea:8"]]
+ 00c38cac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c38cac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c38cac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c37cb8 bytes 00741491
+ 00c38cac bytes 00a81791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-192fe17331da4b74f98b562536abacb7"></a>

### [`00c37d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37d04.md) → [`00c38cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38cf8.md) _ZNKSt9bad_alloc4whatEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c38d00",
      "incomplete_value": false,
      "site": "00c38d04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:bd1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37d0c",
      "incomplete_value": false,
      "site": "00c37d10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:b04:8"
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
      "00c38d00",
      "DATA",
      [
        "storage",
        "002aab04",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c38d00",
      "DATA",
      [
        "storage",
        "002aabd1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37d04.md#insn-00c37d0c)
- 新版 [`00c38d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38cf8.md#insn-00c38d00)

~~~diff
- 00c37d0c ["COPY", "tmp:0:8", ["const:b04:8"]]
- 00c37d0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c37d0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c37d0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c38d00 ["COPY", "tmp:0:8", ["const:bd1:8"]]
+ 00c38d00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c38d00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c38d00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c37d0c bytes 00102c91
+ 00c38d00 bytes 00442f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc205e6d60a835d626f5ad53c48dbf76"></a>

### [`00c37d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37d58.md) → [`00c38d4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38d4c.md) _ZNKSt20bad_array_new_length4whatEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c38d54",
      "incomplete_value": false,
      "site": "00c38d58",
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
            "const:28a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c37d60",
      "incomplete_value": false,
      "site": "00c37d64",
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
            "const:1bf:8"
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
      "00c38d54",
      "DATA",
      [
        "storage",
        "002a51bf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c38d54",
      "DATA",
      [
        "storage",
        "002a528a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37d58.md#insn-00c37d60)
- 新版 [`00c38d54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38d4c.md#insn-00c38d54)

~~~diff
- 00c37d60 ["COPY", "tmp:0:8", ["const:1bf:8"]]
- 00c37d60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c37d60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c37d60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c38d54 ["COPY", "tmp:0:8", ["const:28a:8"]]
+ 00c38d54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c38d54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c38d54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c37d60 bytes 00fc0691
+ 00c38d54 bytes 00280a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7149f58feeb7418903ece7f9113ad1a2"></a>

### [`00c37d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37d68.md) → [`00c38d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38d5c.md) _ZNSt12out_of_rangeD1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md) [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00bf8268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf8/00bf8268.md) [`00c57fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fd0.md) · 呼出先 3件 [`00c53d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)
- 新版 呼出元 10件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md) [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00b41350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41350.md) [`00bf925c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf9/00bf925c.md) [`00c58fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fa0.md) · 呼出先 3件 [`00c54d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59380.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c38d7c",
      "incomplete_value": true,
      "site": "00c38d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00c37d88",
      "incomplete_value": true,
      "site": "00c37d90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00c38d74",
      "READ",
      [
        "storage",
        "00c9bb60",
        null,
        "pointer"
      ]
    ],
    [
      "00c38d84",
      "DATA",
      [
        "storage",
        "00c967a8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00c38d74",
      "READ",
      [
        "storage",
        "00c9cb30",
        null,
        "pointer"
      ]
    ],
    [
      "00c38d84",
      "DATA",
      [
        "storage",
        "00c97778",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37d68.md#insn-00c37d78) · [`00c37d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37d68.md#insn-00c37d80) · [`00c37d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37d68.md#insn-00c37d98)
- 新版 [`00c38d6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38d5c.md#insn-00c38d6c) · [`00c38d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38d5c.md#insn-00c38d74) · [`00c38d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38d5c.md#insn-00c38d8c)

~~~diff
- 00c37d78 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c38d6c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c37d78 bytes 28030090
+ 00c38d6c bytes 28030090
- 00c37d80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b60:8"]]
- 00c37d80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c38d74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b30:8"]]
+ 00c38d74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c37d80 bytes 08b145f9
+ 00c38d74 bytes 089945f9
- 00c37d98 ["INT_ADD", "register:40f0:8", ["const:c37d98:8", "const:4:8"]]
- 00c37d98 ["CALL", null, ["callee:00c54d30:8"]]
+ 00c38d8c ["INT_ADD", "register:40f0:8", ["const:c38d8c:8", "const:4:8"]]
+ 00c38d8c ["CALL", null, ["callee:00c54d30:8"]]
- 00c37d98 bytes ea6f0094
+ 00c38d8c bytes e96f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e114f4c47ff02abac888bb37aad8536d"></a>

### [`00c37df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37df8.md) → [`00c38dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38dec.md) _ZNSt13runtime_errorD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`006d76a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76a8.md) [`00bf03e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf03e4.md) [`00bf0b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0b4c.md) [`00c5a990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a990.md) [`00c5e040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e040.md) · 呼出先 3件 [`00c53d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c583b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583b0.md)
- 新版 呼出元 8件 [`006d7a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7a58.md) [`00bf13d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf13d8.md) [`00bf1b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1b40.md) [`00c5b960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b960.md) [`00c5f010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f010.md) · 呼出先 3件 [`00c54d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59380.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c38e0c",
      "incomplete_value": true,
      "site": "00c38e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00c37e18",
      "incomplete_value": true,
      "site": "00c37e20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00c38e04",
      "READ",
      [
        "storage",
        "00c9bb68",
        null,
        "pointer"
      ]
    ],
    [
      "00c38e14",
      "DATA",
      [
        "storage",
        "00c967d0",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00c38e04",
      "READ",
      [
        "storage",
        "00c9cb38",
        null,
        "pointer"
      ]
    ],
    [
      "00c38e14",
      "DATA",
      [
        "storage",
        "00c977a0",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c37e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37df8.md#insn-00c37e08) · [`00c37e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37df8.md#insn-00c37e10) · [`00c37e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37df8.md#insn-00c37e28)
- 新版 [`00c38dfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38dec.md#insn-00c38dfc) · [`00c38e04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38dec.md#insn-00c38e04) · [`00c38e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38dec.md#insn-00c38e1c)

~~~diff
- 00c37e08 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c38dfc ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c37e08 bytes 28030090
+ 00c38dfc bytes 28030090
- 00c37e10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b68:8"]]
- 00c37e10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c38e04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
+ 00c38e04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c37e10 bytes 08b545f9
+ 00c38e04 bytes 089d45f9
- 00c37e28 ["INT_ADD", "register:40f0:8", ["const:c37e28:8", "const:4:8"]]
- 00c37e28 ["CALL", null, ["callee:00c54d30:8"]]
+ 00c38e1c ["INT_ADD", "register:40f0:8", ["const:c38e1c:8", "const:4:8"]]
+ 00c38e1c ["CALL", null, ["callee:00c54d30:8"]]
- 00c37e28 bytes c66f0094
+ 00c38e1c bytes c56f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da13d0eeebdc2eb2e8ca5b4cc90615d9"></a>

### [`00c38098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38098.md) → [`00c3908c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3908c.md) _ZNKSt10bad_typeid4whatEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c39094",
      "incomplete_value": false,
      "site": "00c39098",
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
            "const:b65:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c380a0",
      "incomplete_value": false,
      "site": "00c380a4",
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
            "const:a87:8"
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
      "00c39094",
      "DATA",
      [
        "storage",
        "002bea87",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c39094",
      "DATA",
      [
        "storage",
        "002beb65",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c380a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38098.md#insn-00c380a0)
- 新版 [`00c39094`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3908c.md#insn-00c39094)

~~~diff
- 00c380a0 ["COPY", "tmp:0:8", ["const:a87:8"]]
- 00c380a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c380a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c380a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c39094 ["COPY", "tmp:0:8", ["const:b65:8"]]
+ 00c39094 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c39094 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c39094 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c380a0 bytes 001c2a91
+ 00c39094 bytes 00942d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bea9160d2a5ee34bb4dc31dc1a72698"></a>

### [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) → [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) FUN_00c3909c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 22件 [`00c3760c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3760c.md) [`00c37750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37750.md) [`00c377f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c377f8.md) [`00c37894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37894.md) [`00c37930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37930.md) · 呼出先 10件 [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md) [`00c5a350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a350.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5e7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e7d0.md) [`00c5ef40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef40.md)
- 新版 呼出元 22件 [`00c38600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38600.md) [`00c38744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38744.md) [`00c387ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c387ec.md) [`00c38888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38888.md) [`00c38924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38924.md) · 呼出先 10件 [`00c5b2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b2c0.md) [`00c5b320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b320.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5f7a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f7a0.md) [`00c5ff10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5ff10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c390d0",
      "incomplete_value": false,
      "site": "00c390fc",
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
            "const:e92:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c380dc",
      "incomplete_value": false,
      "site": "00c38108",
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
            "const:e48:8"
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
      "definition_site": "00c390f8",
      "incomplete_value": true,
      "site": "00c390fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00c38104",
      "incomplete_value": true,
      "site": "00c38108",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c39174",
      "incomplete_value": false,
      "site": "00c39180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:bc6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38180",
      "incomplete_value": false,
      "site": "00c3818c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "00c390d0",
      "PARAM",
      [
        "storage",
        "002c0e48",
        null,
        "string"
      ]
    ],
    [
      "00c390f4",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c390f8",
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
      "00c390d0",
      "PARAM",
      [
        "storage",
        "002c0e92",
        null,
        "string"
      ]
    ],
    [
      "00c390f4",
      "READ",
      [
        "storage",
        "00c9cc18",
        null,
        "pointer"
      ]
    ],
    [
      "00c390f8",
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

- 旧版 [`00c38108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md#insn-00c38108) · [`00c3818c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md#insn-00c3818c) · [`00c381a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md#insn-00c381a0)
- 新版 [`00c390fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md#insn-00c390fc) · [`00c39180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md#insn-00c39180) · [`00c39194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md#insn-00c39194)

~~~diff
- 00c38108 ["INT_ADD", "register:40f0:8", ["const:c38108:8", "const:4:8"]]
- 00c38108 ["CALL", null, ["callee:00c5b2c0:8"]]
+ 00c390fc ["INT_ADD", "register:40f0:8", ["const:c390fc:8", "const:4:8"]]
+ 00c390fc ["CALL", null, ["callee:00c5b2c0:8"]]
- 00c38108 bytes 7a880094
+ 00c390fc bytes 71880094
- 00c3818c ["INT_ADD", "register:40f0:8", ["const:c3818c:8", "const:4:8"]]
- 00c3818c ["CALL", null, ["callee:00c5ff30:8"]]
+ 00c39180 ["INT_ADD", "register:40f0:8", ["const:c39180:8", "const:4:8"]]
+ 00c39180 ["CALL", null, ["callee:00c5ff30:8"]]
- 00c3818c bytes 759b0094
+ 00c39180 bytes 6c9b0094
- 00c381a0 ["INT_ADD", "register:40f0:8", ["const:c381a0:8", "const:4:8"]]
- 00c381a0 ["CALL", null, ["callee:00c5ff40:8"]]
+ 00c39194 ["INT_ADD", "register:40f0:8", ["const:c39194:8", "const:4:8"]]
+ 00c39194 ["CALL", null, ["callee:00c5ff40:8"]]
- 00c381a0 bytes 749b0094
+ 00c39194 bytes 6b9b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46777b327769f3e0f0e037aad0949af9"></a>

### [`00c383cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c383cc.md) → [`00c393c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c393c0.md) FUN_00c393c0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c379c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c379c0.md) · 呼出先 2件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md)
- 新版 呼出元 1件 [`00c389b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c389b4.md) · 呼出先 2件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c596b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c39404",
      "incomplete_value": true,
      "site": "00c39408",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38410",
      "incomplete_value": true,
      "site": "00c38414",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f48:8"
              ]
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c393f4",
      "incomplete_value": true,
      "site": "00c39408",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38400",
      "incomplete_value": true,
      "site": "00c38414",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f50:8"
              ]
            ]
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
      "00c393f0",
      "READ",
      [
        "storage",
        "00c9bf48",
        null,
        "pointer"
      ]
    ],
    [
      "00c393f4",
      "READ",
      [
        "storage",
        "00c9bf50",
        null,
        "pointer"
      ]
    ],
    [
      "00c393f4",
      "PARAM",
      [
        "storage",
        "00c96aa0",
        "_ZTIN10__cxxabiv117__class_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c393f0",
      "READ",
      [
        "storage",
        "00c9cf18",
        null,
        "pointer"
      ]
    ],
    [
      "00c393f4",
      "READ",
      [
        "storage",
        "00c9cf20",
        null,
        "pointer"
      ]
    ],
    [
      "00c393f4",
      "PARAM",
      [
        "storage",
        "00c97a70",
        "_ZTIN10__cxxabiv117__class_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c38414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c383cc.md#insn-00c38414) · [`00c383f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c383cc.md#insn-00c383f0) · [`00c383f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c383cc.md#insn-00c383f8)
- 新版 [`00c39408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c393c0.md#insn-00c39408) · [`00c393e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c393c0.md#insn-00c393e4) · [`00c393ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c393c0.md#insn-00c393ec)

~~~diff
- 00c38414 ["INT_ADD", "register:40f0:8", ["const:c38414:8", "const:4:8"]]
- 00c38414 ["CALL", null, ["callee:00c596b0:8"]]
+ 00c39408 ["INT_ADD", "register:40f0:8", ["const:c39408:8", "const:4:8"]]
+ 00c39408 ["CALL", null, ["callee:00c596b0:8"]]
- 00c38414 bytes b3800094
+ 00c39408 bytes aa800094
- 00c383f0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c393e4 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c383f0 bytes 080300f0
+ 00c393e4 bytes 080300f0
- 00c383f8 ["COPY", "register:4010:8", ["const:c9b000:8"]]
+ 00c393ec ["COPY", "register:4010:8", ["const:c9c000:8"]]
- 00c383f8 bytes 020300f0
+ 00c393ec bytes 020300f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acca3fa521454ef3169e389051edd708"></a>

### [`00c389b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c389b0.md) → [`00c399a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c399a4.md) FUN_00c399a4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md) [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c596b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596b0.md) [`00c5c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c39a04",
      "incomplete_value": true,
      "site": "00c39a08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38a10",
      "incomplete_value": true,
      "site": "00c38a14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f48:8"
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
      "definition_site": "00c399f4",
      "incomplete_value": true,
      "site": "00c39a08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38a00",
      "incomplete_value": true,
      "site": "00c38a14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
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
      "00c399f0",
      "READ",
      [
        "storage",
        "00c9bf48",
        null,
        "pointer"
      ]
    ],
    [
      "00c399f4",
      "READ",
      [
        "storage",
        "00c9bf58",
        null,
        "pointer"
      ]
    ],
    [
      "00c399f4",
      "PARAM",
      [
        "storage",
        "00c96ab8",
        "_ZTIN10__cxxabiv117__pbase_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c399f0",
      "READ",
      [
        "storage",
        "00c9cf18",
        null,
        "pointer"
      ]
    ],
    [
      "00c399f4",
      "READ",
      [
        "storage",
        "00c9cf28",
        null,
        "pointer"
      ]
    ],
    [
      "00c399f4",
      "PARAM",
      [
        "storage",
        "00c97a88",
        "_ZTIN10__cxxabiv117__pbase_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c38a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c389b0.md#insn-00c38a14) · [`00c389dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c389b0.md#insn-00c389dc) · [`00c389f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c389b0.md#insn-00c389f0)
- 新版 [`00c39a08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c399a4.md#insn-00c39a08) · [`00c399d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c399a4.md#insn-00c399d0) · [`00c399e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c399a4.md#insn-00c399e4)

~~~diff
- 00c38a14 ["INT_ADD", "register:40f0:8", ["const:c38a14:8", "const:4:8"]]
- 00c38a14 ["CALL", null, ["callee:00c596b0:8"]]
+ 00c39a08 ["INT_ADD", "register:40f0:8", ["const:c39a08:8", "const:4:8"]]
+ 00c39a08 ["CALL", null, ["callee:00c596b0:8"]]
- 00c38a14 bytes 337f0094
+ 00c39a08 bytes 2a7f0094
- 00c389dc ["INT_ADD", "register:40f0:8", ["const:c389dc:8", "const:4:8"]]
- 00c389dc ["CALL", null, ["callee:00c5c8f0:8"]]
+ 00c399d0 ["INT_ADD", "register:40f0:8", ["const:c399d0:8", "const:4:8"]]
+ 00c399d0 ["CALL", null, ["callee:00c5c8f0:8"]]
- 00c389dc bytes d18b0094
+ 00c399d0 bytes c88b0094
- 00c389f0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c399e4 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00c389f0 bytes 080300f0
+ 00c399e4 bytes 080300f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd2cfcc46b3beefc9574c632cc79cfa6"></a>

### [`00c38a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38a5c.md) → [`00c39a50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39a50.md) FUN_00c39a50

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c38d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38d18.md) [`00c38e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38e0c.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md) [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c39d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39d0c.md) [`00c39e00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39e00.md) [`00c596b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596b0.md) [`00c5c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8f0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 89.14% / 新版 89.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 11件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c39a7c",
      "incomplete_value": true,
      "site": "00c39a80",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00c38a88",
      "incomplete_value": true,
      "site": "00c38a8c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c39b90",
      "incomplete_value": true,
      "site": "00c39b94",
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
                "register:4040:8"
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
      "definition_site": "00c38b9c",
      "incomplete_value": true,
      "site": "00c38ba0",
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
                "register:4040:8"
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
    "ordinal": 13,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c39ae0",
      "incomplete_value": true,
      "site": "00c39aec",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4008:8"
              ],
              [
                "leaf",
                "const:f18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38aec",
      "incomplete_value": true,
      "site": "00c38af8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4008:8"
              ],
              [
                "leaf",
                "const:f48:8"
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
      "00c39a78",
      "READ",
      [
        "storage",
        "00c9bf60",
        null,
        "pointer"
      ]
    ],
    [
      "00c39ae0",
      "READ",
      [
        "storage",
        "00c9bf48",
        null,
        "pointer"
      ]
    ],
    [
      "00c39ae0",
      "PARAM",
      [
        "storage",
        "00c96a88",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c39a78",
      "READ",
      [
        "storage",
        "00c9cf30",
        null,
        "pointer"
      ]
    ],
    [
      "00c39ae0",
      "READ",
      [
        "storage",
        "00c9cf18",
        null,
        "pointer"
      ]
    ],
    [
      "00c39ae0",
      "PARAM",
      [
        "storage",
        "00c97a58",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c38af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38a5c.md#insn-00c38af8) · [`00c38b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38a5c.md#insn-00c38b30) · [`00c38bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38a5c.md#insn-00c38bb4)
- 新版 [`00c39aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39a50.md#insn-00c39aec) · [`00c39b24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39a50.md#insn-00c39b24) · [`00c39ba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39a50.md#insn-00c39ba8)

~~~diff
- 00c38af8 ["INT_ADD", "register:40f0:8", ["const:c38af8:8", "const:4:8"]]
- 00c38af8 ["CALL", null, ["callee:00c596b0:8"]]
+ 00c39aec ["INT_ADD", "register:40f0:8", ["const:c39aec:8", "const:4:8"]]
+ 00c39aec ["CALL", null, ["callee:00c596b0:8"]]
- 00c38af8 bytes fa7e0094
+ 00c39aec bytes f17e0094
- 00c38b30 ["INT_ADD", "register:40f0:8", ["const:c38b30:8", "const:4:8"]]
- 00c38b30 ["CALL", null, ["callee:00c596b0:8"]]
+ 00c39b24 ["INT_ADD", "register:40f0:8", ["const:c39b24:8", "const:4:8"]]
+ 00c39b24 ["CALL", null, ["callee:00c596b0:8"]]
- 00c38b30 bytes ec7e0094
+ 00c39b24 bytes e37e0094
- 00c38bb4 ["INT_ADD", "register:40f0:8", ["const:c38bb4:8", "const:4:8"]]
- 00c38bb4 ["CALL", null, ["callee:00c596b0:8"]]
+ 00c39ba8 ["INT_ADD", "register:40f0:8", ["const:c39ba8:8", "const:4:8"]]
+ 00c39ba8 ["CALL", null, ["callee:00c596b0:8"]]
- 00c38bb4 bytes cb7e0094
+ 00c39ba8 bytes c27e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3584315cb7caf72af564e278fb0603a"></a>

### [`00c38eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38eac.md) → [`00c39ea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39ea0.md) FUN_00c39ea0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md) [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c596b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596b0.md) [`00c5c8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8f0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.81% / 新版 86.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c39ec4",
      "incomplete_value": true,
      "site": "00c39ec8",
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
                "register:40a8:8"
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
      "definition_site": "00c38ed0",
      "incomplete_value": true,
      "site": "00c38ed4",
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
                "register:40a8:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c39f10",
      "incomplete_value": true,
      "site": "00c39f20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38f1c",
      "incomplete_value": true,
      "site": "00c38f2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f48:8"
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
      "definition_site": "00c39f1c",
      "incomplete_value": true,
      "site": "00c39f20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c38f28",
      "incomplete_value": true,
      "site": "00c38f2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f78:8"
              ]
            ]
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
      "00c39ec0",
      "READ",
      [
        "storage",
        "00c9bf60",
        null,
        "pointer"
      ]
    ],
    [
      "00c39f10",
      "READ",
      [
        "storage",
        "00c9bf48",
        null,
        "pointer"
      ]
    ],
    [
      "00c39f10",
      "PARAM",
      [
        "storage",
        "00c96a88",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c39ec0",
      "READ",
      [
        "storage",
        "00c9cf30",
        null,
        "pointer"
      ]
    ],
    [
      "00c39f10",
      "READ",
      [
        "storage",
        "00c9cf18",
        null,
        "pointer"
      ]
    ],
    [
      "00c39f10",
      "PARAM",
      [
        "storage",
        "00c97a58",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c38f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38eac.md#insn-00c38f2c) · [`00c38f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38eac.md#insn-00c38f5c) · [`00c38f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c38eac.md#insn-00c38f94)
- 新版 [`00c39f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39ea0.md#insn-00c39f20) · [`00c39f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39ea0.md#insn-00c39f50) · [`00c39f88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c39ea0.md#insn-00c39f88)

~~~diff
- 00c38f2c ["INT_ADD", "register:40f0:8", ["const:c38f2c:8", "const:4:8"]]
- 00c38f2c ["CALL", null, ["callee:00c596b0:8"]]
+ 00c39f20 ["INT_ADD", "register:40f0:8", ["const:c39f20:8", "const:4:8"]]
+ 00c39f20 ["CALL", null, ["callee:00c596b0:8"]]
- 00c38f2c bytes ed7d0094
+ 00c39f20 bytes e47d0094
- 00c38f5c ["INT_ADD", "register:40f0:8", ["const:c38f5c:8", "const:4:8"]]
- 00c38f5c ["CALL", null, ["callee:00c596b0:8"]]
+ 00c39f50 ["INT_ADD", "register:40f0:8", ["const:c39f50:8", "const:4:8"]]
+ 00c39f50 ["CALL", null, ["callee:00c596b0:8"]]
- 00c38f5c bytes e17d0094
+ 00c39f50 bytes d87d0094
- 00c38f94 ["INT_ADD", "register:40f0:8", ["const:c38f94:8", "const:4:8"]]
- 00c38f94 ["CALL", null, ["callee:00c596b0:8"]]
+ 00c39f88 ["INT_ADD", "register:40f0:8", ["const:c39f88:8", "const:4:8"]]
+ 00c39f88 ["CALL", null, ["callee:00c596b0:8"]]
- 00c38f94 bytes d37d0094
+ 00c39f88 bytes ca7d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0707c3055a0c80e0f08da51991bdb94"></a>

### [`00c39b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39b1c.md) → [`00c3ab10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3ab10.md) __cxa_demangle

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5eec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eec0.md) · 呼出先 10件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3acb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3acb4.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 1件 [`00c5fe90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fe90.md) · 呼出先 10件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) [`00c3bca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bca8.md) [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.35% / 新版 98.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3ae58",
      "incomplete_value": false,
      "site": "00c3ae58",
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
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c39e64",
      "incomplete_value": false,
      "site": "00c39e64",
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
            "const:8b0:8"
          ]
        ]
      ]
    },
    "ordinal": 90,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3afb0",
      "incomplete_value": false,
      "site": "00c3afbc",
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
            "const:edd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c39fbc",
      "incomplete_value": false,
      "site": "00c39fc8",
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
            "const:dff:8"
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
      "definition_site": "00c3b098",
      "incomplete_value": false,
      "site": "00c3b0b0",
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
      "definition_site": "00c3a0a4",
      "incomplete_value": false,
      "site": "00c3a0bc",
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
      "00c3ae58",
      "DATA",
      [
        "storage",
        "00c998b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3afb0",
      "PARAM",
      [
        "storage",
        "002b9dff",
        null,
        "string"
      ]
    ],
    [
      "00c3b098",
      "PARAM",
      [
        "storage",
        "002a0e95",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3ae58",
      "DATA",
      [
        "storage",
        "00c9a880",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3afb0",
      "PARAM",
      [
        "storage",
        "002b9edd",
        null,
        "string"
      ]
    ],
    [
      "00c3b098",
      "PARAM",
      [
        "storage",
        "002a0ed5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c39fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39b1c.md#insn-00c39fc8) · [`00c3a0bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39b1c.md#insn-00c3a0bc) · [`00c39b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39b1c.md#insn-00c39b78)
- 新版 [`00c3afbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3ab10.md#insn-00c3afbc) · [`00c3b0b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3ab10.md#insn-00c3b0b0) · [`00c3ab6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3ab10.md#insn-00c3ab6c)

~~~diff
- 00c39fc8 ["INT_ADD", "register:40f0:8", ["const:c39fc8:8", "const:4:8"]]
- 00c39fc8 ["CALL", null, ["callee:00c3bca8:8"]]
+ 00c3afbc ["INT_ADD", "register:40f0:8", ["const:c3afbc:8", "const:4:8"]]
+ 00c3afbc ["CALL", null, ["callee:00c3bca8:8"]]
- 00c39fc8 bytes 3b030094
+ 00c3afbc bytes 3b030094
- 00c3a0bc ["INT_ADD", "register:40f0:8", ["const:c3a0bc:8", "const:4:8"]]
- 00c3a0bc ["CALL", null, ["callee:00c3909c:8"]]
+ 00c3b0b0 ["INT_ADD", "register:40f0:8", ["const:c3b0b0:8", "const:4:8"]]
+ 00c3b0b0 ["CALL", null, ["callee:00c3909c:8"]]
- 00c3a0bc bytes fbf7ff97
+ 00c3b0b0 bytes fbf7ff97
- 00c39b78 ["INT_ADD", "register:40f0:8", ["const:c39b78:8", "const:4:8"]]
- 00c39b78 ["CALL", null, ["callee:00c59080:8"]]
+ 00c3ab6c ["INT_ADD", "register:40f0:8", ["const:c3ab6c:8", "const:4:8"]]
+ 00c3ab6c ["CALL", null, ["callee:00c59080:8"]]
- 00c39b78 bytes 4e790094
+ 00c3ab6c bytes 45790094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34f4bc8f59074e22a02175314164ffe3"></a>

### [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) → [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) FUN_00c3b208

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00c39b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39b1c.md) [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 31件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3ac28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ac28.md) [`00c3acb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3acb4.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md)
- 新版 呼出元 5件 [`00c3ab10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3ab10.md) [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c3d9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md) [`00c427e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md) · 呼出先 31件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) [`00c3bc1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bc1c.md) [`00c3bca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bca8.md) [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.26% / 新版 98.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3b430",
      "incomplete_value": false,
      "site": "00c3b430",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3a43c",
      "incomplete_value": false,
      "site": "00c3a43c",
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
            "const:620:8"
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
      "definition_site": "00c3b874",
      "incomplete_value": false,
      "site": "00c3b874",
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
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3a880",
      "incomplete_value": false,
      "site": "00c3a880",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "ordinal": 67,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3ba78",
      "incomplete_value": false,
      "site": "00c3ba84",
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
            "const:12e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3aa84",
      "incomplete_value": false,
      "site": "00c3aa90",
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
            "const:5f:8"
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
      "00c3b430",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3b6d4",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3b6f8",
      "DATA",
      [
        "storage",
        "002b08b2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3b430",
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3b6d4",
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3b6f8",
      "DATA",
      [
        "storage",
        "002b0989",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3aa90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md#insn-00c3aa90) · [`00c3abd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md#insn-00c3abd8) · [`00c3a244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md#insn-00c3a244)
- 新版 [`00c3ba84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md#insn-00c3ba84) · [`00c3bbcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md#insn-00c3bbcc) · [`00c3b238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md#insn-00c3b238)

~~~diff
- 00c3aa90 ["INT_ADD", "register:40f0:8", ["const:c3aa90:8", "const:4:8"]]
- 00c3aa90 ["CALL", null, ["callee:00c3bca8:8"]]
+ 00c3ba84 ["INT_ADD", "register:40f0:8", ["const:c3ba84:8", "const:4:8"]]
+ 00c3ba84 ["CALL", null, ["callee:00c3bca8:8"]]
- 00c3aa90 bytes 89000094
+ 00c3ba84 bytes 89000094
- 00c3abd8 ["INT_ADD", "register:40f0:8", ["const:c3abd8:8", "const:4:8"]]
- 00c3abd8 ["CALL", null, ["callee:00c3909c:8"]]
+ 00c3bbcc ["INT_ADD", "register:40f0:8", ["const:c3bbcc:8", "const:4:8"]]
+ 00c3bbcc ["CALL", null, ["callee:00c3909c:8"]]
- 00c3abd8 bytes 34f5ff97
+ 00c3bbcc bytes 34f5ff97
- 00c3a244 ["INT_ADD", "register:40f0:8", ["const:c3a244:8", "const:4:8"]]
- 00c3a244 ["CALL", null, ["callee:00c3d0f4:8"]]
+ 00c3b238 ["INT_ADD", "register:40f0:8", ["const:c3b238:8", "const:4:8"]]
+ 00c3b238 ["CALL", null, ["callee:00c3d0f4:8"]]
- 00c3a244 bytes af070094
+ 00c3b238 bytes af070094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab9f505283ee599c178b3b0e8a2f1db6"></a>

### [`00c3acb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3acb4.md) → [`00c3bca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bca8.md) FUN_00c3bca8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c39b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39b1c.md) [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 3件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 2件 [`00c3ab10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3ab10.md) [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 3件 [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c3bd18",
      "incomplete_value": false,
      "site": "00c3bd18",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3ad24",
      "incomplete_value": false,
      "site": "00c3ad24",
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
            "const:620:8"
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
      "00c3bd18",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3bd18",
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3acec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3acb4.md#insn-00c3acec) · [`00c3ad14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3acb4.md#insn-00c3ad14) · [`00c3ad18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3acb4.md#insn-00c3ad18)
- 新版 [`00c3bce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bca8.md#insn-00c3bce0) · [`00c3bd08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bca8.md#insn-00c3bd08) · [`00c3bd0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bca8.md#insn-00c3bd0c)

~~~diff
- 00c3acec ["INT_ADD", "register:40f0:8", ["const:c3acec:8", "const:4:8"]]
- 00c3acec ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3bce0 ["INT_ADD", "register:40f0:8", ["const:c3bce0:8", "const:4:8"]]
+ 00c3bce0 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3acec bytes 017d0094
+ 00c3bce0 bytes f87c0094
- 00c3ad14 ["INT_ADD", "register:40f0:8", ["const:c3ad14:8", "const:4:8"]]
- 00c3ad14 ["CALL", null, ["callee:00c59080:8"]]
+ 00c3bd08 ["INT_ADD", "register:40f0:8", ["const:c3bd08:8", "const:4:8"]]
+ 00c3bd08 ["CALL", null, ["callee:00c59080:8"]]
- 00c3ad14 bytes e7740094
+ 00c3bd08 bytes de740094
- 00c3ad18 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c3bd0c ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c3ad18 bytes e80200b0
+ 00c3bd0c bytes e80200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adaaae9fcb6a6117312c3e4e940d1066"></a>

### [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) → [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) FUN_00c3bd5c

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 15件 [`00c39b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c39/00c39b1c.md) [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 38件 [`00c3ac28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ac28.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3cd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cd04.md) [`00c3e278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e278.md)
- 新版 呼出元 15件 [`00c3ab10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3a/00c3ab10.md) [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md) [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 38件 [`00c3bc1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bc1c.md) [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c3dcf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3dcf8.md) [`00c3f26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f26c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.14% / 新版 93.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 21件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3bf40",
      "incomplete_value": false,
      "site": "00c3bf40",
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
      "definition_site": "00c3af4c",
      "incomplete_value": false,
      "site": "00c3af4c",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3bfb0",
      "incomplete_value": false,
      "site": "00c3bfb0",
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
      "definition_site": "00c3afbc",
      "incomplete_value": false,
      "site": "00c3afbc",
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
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3c020",
      "incomplete_value": false,
      "site": "00c3c020",
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
      "definition_site": "00c3b02c",
      "incomplete_value": false,
      "site": "00c3b02c",
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
      "00c3bda8",
      "DATA",
      [
        "storage",
        "00312a20",
        "switchD_00c3adbc::switchdataD_00312a20",
        "ushort"
      ]
    ],
    [
      "00c3bec0",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3bf40",
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
      "00c3bda8",
      "DATA",
      [
        "storage",
        "00312a60",
        "switchD_00c3bdb0::switchdataD_00312a60",
        "ushort"
      ]
    ],
    [
      "00c3bec0",
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3bf40",
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

- 旧版 [`00c3adac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md#insn-00c3adac) · [`00c3adb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md#insn-00c3adb0) · [`00c3ae6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md#insn-00c3ae6c)
- 新版 [`00c3bda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md#insn-00c3bda0) · [`00c3be60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md#insn-00c3be60)

~~~diff
- 00c3adac ["COPY", "tmp:0:8", ["const:a20:8"]]
- 00c3adac ["INT_CARRY", "register:105:1", ["register:4068:8", "tmp:0:8"]]
- 00c3adac ["INT_SCARRY", "register:106:1", ["register:4068:8", "tmp:0:8"]]
- 00c3adac ["INT_ADD", "tmp:1:8", ["register:4068:8", "tmp:0:8"]]
+ 00c3bda0 ["COPY", "tmp:0:8", ["const:a60:8"]]
+ 00c3bda0 ["INT_CARRY", "register:105:1", ["register:4068:8", "tmp:0:8"]]
+ 00c3bda0 ["INT_SCARRY", "register:106:1", ["register:4068:8", "tmp:0:8"]]
+ 00c3bda0 ["INT_ADD", "tmp:1:8", ["register:4068:8", "tmp:0:8"]]
- 00c3adac bytes ad812891
+ 00c3bda0 bytes ad812991
- 00c3adb0 ["COPY", "register:4070:8", ["const:c3adc0:8"]]
- 00c3adb0 bytes 8e000010
- 00c3ae6c ["INT_ADD", "register:40f0:8", ["const:c3ae6c:8", "const:4:8"]]
- 00c3ae6c ["CALL", null, ["callee:00c4f678:8"]]
+ 00c3be60 ["INT_ADD", "register:40f0:8", ["const:c3be60:8", "const:4:8"]]
+ 00c3be60 ["CALL", null, ["callee:00c4f678:8"]]
- 00c3ae6c bytes 064e0094
+ 00c3be60 bytes 064e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0024dfe04bf015fff31ac7e39816b1e4"></a>

### [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) → [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) FUN_00c3d29c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3f3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c42a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42a5c.md) · 呼出先 19件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3ac28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ac28.md) [`00c3c100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c100.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3d0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d0cc.md)
- 新版 呼出元 7件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c403a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c403a0.md) [`00c43a50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43a50.md) · 呼出先 19件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) [`00c3bc1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bc1c.md) [`00c3d0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d0f4.md) [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c3e0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.24% / 新版 98.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d698",
      "incomplete_value": false,
      "site": "00c3d698",
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
      "definition_site": "00c3c6a4",
      "incomplete_value": false,
      "site": "00c3c6a4",
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
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d6bc",
      "incomplete_value": false,
      "site": "00c3d6bc",
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
            "const:dff:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3c6c8",
      "incomplete_value": false,
      "site": "00c3c6c8",
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
            "const:d30:8"
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d984",
      "incomplete_value": false,
      "site": "00c3d984",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3c990",
      "incomplete_value": false,
      "site": "00c3c990",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "ordinal": 74,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3d3fc",
      "PARAM",
      [
        "storage",
        "002b189e",
        null,
        "string"
      ]
    ],
    [
      "00c3d57c",
      "DATA",
      [
        "storage",
        "00c99610",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d698",
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
      "00c3d3fc",
      "PARAM",
      [
        "storage",
        "002b1975",
        null,
        "string"
      ]
    ],
    [
      "00c3d57c",
      "DATA",
      [
        "storage",
        "00c9a5e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3d698",
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

- 旧版 [`00c3c410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md#insn-00c3c410) · [`00c3c338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md#insn-00c3c338) · [`00c3c388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md#insn-00c3c388)
- 新版 [`00c3d404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md#insn-00c3d404) · [`00c3d32c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md#insn-00c3d32c) · [`00c3d37c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md#insn-00c3d37c)

~~~diff
- 00c3c410 ["INT_ADD", "register:40f0:8", ["const:c3c410:8", "const:4:8"]]
- 00c3c410 ["CALL", null, ["callee:00c4e180:8"]]
+ 00c3d404 ["INT_ADD", "register:40f0:8", ["const:c3d404:8", "const:4:8"]]
+ 00c3d404 ["CALL", null, ["callee:00c4e180:8"]]
- 00c3c410 bytes 5f430094
+ 00c3d404 bytes 5f430094
- 00c3c338 ["INT_ADD", "register:40f0:8", ["const:c3c338:8", "const:4:8"]]
- 00c3c338 ["CALL", null, ["callee:00c3f4e4:8"]]
+ 00c3d32c ["INT_ADD", "register:40f0:8", ["const:c3d32c:8", "const:4:8"]]
+ 00c3d32c ["CALL", null, ["callee:00c3f4e4:8"]]
- 00c3c338 bytes 6e080094
+ 00c3d32c bytes 6e080094
- 00c3c388 ["INT_ADD", "register:40f0:8", ["const:c3c388:8", "const:4:8"]]
- 00c3c388 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c3d37c ["INT_ADD", "register:40f0:8", ["const:c3d37c:8", "const:4:8"]]
+ 00c3d37c ["CALL", null, ["callee:00c5b140:8"]]
- 00c3c388 bytes 7a770094
+ 00c3d37c bytes 71770094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d0225424c87645c8aca329f31a2f0af"></a>

### [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) → [`00c3d9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md) FUN_00c3d9d0

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 13件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3ce7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md)
- 新版 呼出元 4件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) [`00c3d9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md) [`00c3f654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f654.md) [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 13件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md) [`00c3de70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md) [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3dc48",
      "incomplete_value": false,
      "site": "00c3dc4c",
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
            "const:2fd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3cc54",
      "incomplete_value": false,
      "site": "00c3cc58",
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
            "const:232:8"
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
      "00c3dc00",
      "DATA",
      [
        "storage",
        "00c99680",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3dc00",
      "DATA",
      [
        "storage",
        "00c996f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3dc48",
      "PARAM",
      [
        "storage",
        "002a5232",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3dc00",
      "DATA",
      [
        "storage",
        "00c9a650",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3dc00",
      "DATA",
      [
        "storage",
        "00c9a6c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3dc48",
      "PARAM",
      [
        "storage",
        "002a52fd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3cc58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md#insn-00c3cc58) · [`00c3ca4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md#insn-00c3ca4c) · [`00c3ca74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md#insn-00c3ca74)
- 新版 [`00c3dc4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md#insn-00c3dc4c) · [`00c3da40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md#insn-00c3da40) · [`00c3da68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md#insn-00c3da68)

~~~diff
- 00c3cc58 ["INT_ADD", "register:40f0:8", ["const:c3cc58:8", "const:4:8"]]
- 00c3cc58 ["CALL", null, ["callee:00c59070:8"]]
+ 00c3dc4c ["INT_ADD", "register:40f0:8", ["const:c3dc4c:8", "const:4:8"]]
+ 00c3dc4c ["CALL", null, ["callee:00c59070:8"]]
- 00c3cc58 bytes 126d0094
+ 00c3dc4c bytes 096d0094
- 00c3ca4c ["INT_ADD", "register:40f0:8", ["const:c3ca4c:8", "const:4:8"]]
- 00c3ca4c ["CALL", null, ["callee:00c3b208:8"]]
+ 00c3da40 ["INT_ADD", "register:40f0:8", ["const:c3da40:8", "const:4:8"]]
+ 00c3da40 ["CALL", null, ["callee:00c3b208:8"]]
- 00c3ca4c bytes f2f5ff97
+ 00c3da40 bytes f2f5ff97
- 00c3ca74 ["INT_ADD", "register:40f0:8", ["const:c3ca74:8", "const:4:8"]]
- 00c3ca74 ["CALL", null, ["callee:00c40e0c:8"]]
+ 00c3da68 ["INT_ADD", "register:40f0:8", ["const:c3da68:8", "const:4:8"]]
+ 00c3da68 ["CALL", null, ["callee:00c40e0c:8"]]
- 00c3ca74 bytes e90c0094
+ 00c3da68 bytes e90c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4a036e29545fc0cf65bc3263b7aa2b8"></a>

### [`00c3cddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cddc.md) → [`00c3ddd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3ddd0.md) FUN_00c3ddd0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c3de34",
      "incomplete_value": false,
      "site": "00c3de34",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3ce40",
      "incomplete_value": false,
      "site": "00c3ce40",
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
            "const:760:8"
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
      "00c3de34",
      "DATA",
      [
        "storage",
        "00c99760",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3de34",
      "DATA",
      [
        "storage",
        "00c9a730",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3ce10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cddc.md#insn-00c3ce10) · [`00c3ce30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cddc.md#insn-00c3ce30) · [`00c3ce34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cddc.md#insn-00c3ce34)
- 新版 [`00c3de04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3ddd0.md#insn-00c3de04) · [`00c3de24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3ddd0.md#insn-00c3de24) · [`00c3de28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3ddd0.md#insn-00c3de28)

~~~diff
- 00c3ce10 ["INT_ADD", "register:40f0:8", ["const:c3ce10:8", "const:4:8"]]
- 00c3ce10 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3de04 ["INT_ADD", "register:40f0:8", ["const:c3de04:8", "const:4:8"]]
+ 00c3de04 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3ce10 bytes b8740094
+ 00c3de04 bytes af740094
- 00c3ce30 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c3de24 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c3ce30 bytes e80200b0
+ 00c3de24 bytes e80200b0
- 00c3ce34 ["COPY", "tmp:0:8", ["const:760:8"]]
- 00c3ce34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3ce34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3ce34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3de28 ["COPY", "tmp:0:8", ["const:730:8"]]
+ 00c3de28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3de28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3de28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3ce34 bytes 08811d91
+ 00c3de28 bytes 08c11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2da8e81e9625ac84862e9319ec63fd85"></a>

### [`00c3ce7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) → [`00c3de70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md) FUN_00c3de70

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c3f3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 4件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 10件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) [`00c3d9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md) [`00c3f654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f654.md) [`00c403a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c403a0.md) [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 4件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3df8c",
      "incomplete_value": false,
      "site": "00c3dfa4",
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
      "definition_site": "00c3cf98",
      "incomplete_value": false,
      "site": "00c3cfb0",
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
      "definition_site": "00c3df94",
      "incomplete_value": false,
      "site": "00c3dfa4",
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
      "definition_site": "00c3cfa0",
      "incomplete_value": false,
      "site": "00c3cfb0",
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
      "definition_site": "00c3df9c",
      "incomplete_value": false,
      "site": "00c3dfa4",
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
      "definition_site": "00c3cfa8",
      "incomplete_value": false,
      "site": "00c3cfb0",
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
      "00c3df8c",
      "PARAM",
      [
        "storage",
        "002a0e95",
        null,
        "string"
      ]
    ],
    [
      "00c3df94",
      "PARAM",
      [
        "storage",
        "002b28c7",
        null,
        "string"
      ]
    ],
    [
      "00c3df9c",
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
      "00c3df8c",
      "PARAM",
      [
        "storage",
        "002a0ed5",
        null,
        "string"
      ]
    ],
    [
      "00c3df94",
      "PARAM",
      [
        "storage",
        "002b2911",
        null,
        "string"
      ]
    ],
    [
      "00c3df9c",
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

- 旧版 [`00c3cfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md#insn-00c3cfb0) · [`00c3cfd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md#insn-00c3cfd0) · [`00c3cee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md#insn-00c3cee8)
- 新版 [`00c3dfa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md#insn-00c3dfa4) · [`00c3dfc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md#insn-00c3dfc4) · [`00c3dedc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md#insn-00c3dedc)

~~~diff
- 00c3cfb0 ["INT_ADD", "register:40f0:8", ["const:c3cfb0:8", "const:4:8"]]
- 00c3cfb0 ["CALL", null, ["callee:00c3909c:8"]]
+ 00c3dfa4 ["INT_ADD", "register:40f0:8", ["const:c3dfa4:8", "const:4:8"]]
+ 00c3dfa4 ["CALL", null, ["callee:00c3909c:8"]]
- 00c3cfb0 bytes 3eecff97
+ 00c3dfa4 bytes 3eecff97
- 00c3cfd0 ["INT_ADD", "register:40f0:8", ["const:c3cfd0:8", "const:4:8"]]
- 00c3cfd0 ["CALL", null, ["callee:00c3909c:8"]]
+ 00c3dfc4 ["INT_ADD", "register:40f0:8", ["const:c3dfc4:8", "const:4:8"]]
+ 00c3dfc4 ["CALL", null, ["callee:00c3909c:8"]]
- 00c3cfd0 bytes 36ecff97
+ 00c3dfc4 bytes 36ecff97
- 00c3cee8 ["INT_ADD", "register:40f0:8", ["const:c3cee8:8", "const:4:8"]]
- 00c3cee8 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3dedc ["INT_ADD", "register:40f0:8", ["const:c3dedc:8", "const:4:8"]]
+ 00c3dedc ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3cee8 bytes 82740094
+ 00c3dedc bytes 79740094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16735aa47d222e72a55c5f3c6d063687"></a>

### [`00c3cfd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cfd8.md) → [`00c3dfcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3dfcc.md) FUN_00c3dfcc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c3e054",
      "incomplete_value": false,
      "site": "00c3e054",
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
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d060",
      "incomplete_value": false,
      "site": "00c3d060",
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
            "const:840:8"
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
      "00c3e054",
      "DATA",
      [
        "storage",
        "00c99840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3e054",
      "DATA",
      [
        "storage",
        "00c9a810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cfd8.md#insn-00c3d030) · [`00c3d050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cfd8.md#insn-00c3d050) · [`00c3d054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cfd8.md#insn-00c3d054)
- 新版 [`00c3e024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3dfcc.md#insn-00c3e024) · [`00c3e044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3dfcc.md#insn-00c3e044) · [`00c3e048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3dfcc.md#insn-00c3e048)

~~~diff
- 00c3d030 ["INT_ADD", "register:40f0:8", ["const:c3d030:8", "const:4:8"]]
- 00c3d030 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3e024 ["INT_ADD", "register:40f0:8", ["const:c3e024:8", "const:4:8"]]
+ 00c3e024 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3d030 bytes 30740094
+ 00c3e024 bytes 27740094
- 00c3d050 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c3e044 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c3d050 bytes e8020090
+ 00c3e044 bytes e8020090
- 00c3d054 ["COPY", "tmp:0:8", ["const:840:8"]]
- 00c3d054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3e048 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 00c3e048 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e048 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e048 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d054 bytes 08012191
+ 00c3e048 bytes 08412091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53f38922a12a7ac089f03c95346bd68c"></a>

### [`00c3d2ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d2ac.md) → [`00c3e2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e2a0.md) FUN_00c3e2a0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c3e304",
      "incomplete_value": false,
      "site": "00c3e304",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d310",
      "incomplete_value": false,
      "site": "00c3d310",
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
            "const:620:8"
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
      "definition_site": "00c3e328",
      "incomplete_value": false,
      "site": "00c3e328",
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
            "const:1c7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d334",
      "incomplete_value": false,
      "site": "00c3d334",
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
            "const:e9:8"
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
      "00c3e304",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e328",
      "DATA",
      [
        "storage",
        "002bb0e9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3e304",
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e328",
      "DATA",
      [
        "storage",
        "002bb1c7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d2ac.md#insn-00c3d2e0) · [`00c3d300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d2ac.md#insn-00c3d300) · [`00c3d304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d2ac.md#insn-00c3d304)
- 新版 [`00c3e2d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e2a0.md#insn-00c3e2d4) · [`00c3e2f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e2a0.md#insn-00c3e2f4) · [`00c3e2f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e2a0.md#insn-00c3e2f8)

~~~diff
- 00c3d2e0 ["INT_ADD", "register:40f0:8", ["const:c3d2e0:8", "const:4:8"]]
- 00c3d2e0 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3e2d4 ["INT_ADD", "register:40f0:8", ["const:c3e2d4:8", "const:4:8"]]
+ 00c3e2d4 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3d2e0 bytes 84730094
+ 00c3e2d4 bytes 7b730094
- 00c3d300 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c3e2f4 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c3d300 bytes c80200d0
+ 00c3e2f4 bytes c80200d0
- 00c3d304 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3d304 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d304 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d304 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3e2f8 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 00c3e2f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e2f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e2f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d304 bytes 08811891
+ 00c3e2f8 bytes 08c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc61e359cf4cdbff41b8a13fb9c41c3d"></a>

### [`00c3d35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d35c.md) → [`00c3e350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e350.md) FUN_00c3e350

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c3e3b4",
      "incomplete_value": false,
      "site": "00c3e3b4",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d3c0",
      "incomplete_value": false,
      "site": "00c3d3c0",
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
            "const:620:8"
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
      "definition_site": "00c3e3d8",
      "incomplete_value": false,
      "site": "00c3e3d8",
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
            "const:94c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d3e4",
      "incomplete_value": false,
      "site": "00c3d3e4",
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
            "const:875:8"
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
      "00c3e3b4",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e3d8",
      "DATA",
      [
        "storage",
        "002b1875",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3e3b4",
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e3d8",
      "DATA",
      [
        "storage",
        "002b194c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d35c.md#insn-00c3d390) · [`00c3d3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d35c.md#insn-00c3d3b0) · [`00c3d3b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d35c.md#insn-00c3d3b4)
- 新版 [`00c3e384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e350.md#insn-00c3e384) · [`00c3e3a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e350.md#insn-00c3e3a4) · [`00c3e3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e350.md#insn-00c3e3a8)

~~~diff
- 00c3d390 ["INT_ADD", "register:40f0:8", ["const:c3d390:8", "const:4:8"]]
- 00c3d390 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3e384 ["INT_ADD", "register:40f0:8", ["const:c3e384:8", "const:4:8"]]
+ 00c3e384 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3d390 bytes 58730094
+ 00c3e384 bytes 4f730094
- 00c3d3b0 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c3e3a4 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c3d3b0 bytes c80200d0
+ 00c3e3a4 bytes c80200d0
- 00c3d3b4 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3d3b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d3b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d3b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3e3a8 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 00c3e3a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e3a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e3a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d3b4 bytes 08811891
+ 00c3e3a8 bytes 08c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a100c7f2b0f3f66469f603bf20ab81a"></a>

### [`00c3d40c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d40c.md) → [`00c3e400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e400.md) FUN_00c3e400

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c3e464",
      "incomplete_value": false,
      "site": "00c3e464",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d470",
      "incomplete_value": false,
      "site": "00c3d470",
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
            "const:620:8"
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
      "definition_site": "00c3e488",
      "incomplete_value": false,
      "site": "00c3e488",
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
            "const:e5e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d494",
      "incomplete_value": false,
      "site": "00c3d494",
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
            "const:e1e:8"
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
      "00c3e464",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e488",
      "DATA",
      [
        "storage",
        "0029fe1e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3e464",
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e488",
      "DATA",
      [
        "storage",
        "0029fe5e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d40c.md#insn-00c3d440) · [`00c3d460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d40c.md#insn-00c3d460) · [`00c3d464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d40c.md#insn-00c3d464)
- 新版 [`00c3e434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e400.md#insn-00c3e434) · [`00c3e454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e400.md#insn-00c3e454) · [`00c3e458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e400.md#insn-00c3e458)

~~~diff
- 00c3d440 ["INT_ADD", "register:40f0:8", ["const:c3d440:8", "const:4:8"]]
- 00c3d440 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3e434 ["INT_ADD", "register:40f0:8", ["const:c3e434:8", "const:4:8"]]
+ 00c3e434 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3d440 bytes 2c730094
+ 00c3e434 bytes 23730094
- 00c3d460 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c3e454 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c3d460 bytes c80200d0
+ 00c3e454 bytes c80200d0
- 00c3d464 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3d464 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d464 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d464 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3e458 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 00c3e458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d464 bytes 08811891
+ 00c3e458 bytes 08c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3541b929a0a09ae03d83dd3af2bcbdd6"></a>

### [`00c3d4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d4bc.md) → [`00c3e4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e4b0.md) FUN_00c3e4b0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c3e514",
      "incomplete_value": false,
      "site": "00c3e514",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d520",
      "incomplete_value": false,
      "site": "00c3d520",
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
            "const:620:8"
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
      "definition_site": "00c3e538",
      "incomplete_value": false,
      "site": "00c3e538",
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
            "const:903:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d544",
      "incomplete_value": false,
      "site": "00c3d544",
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
            "const:8b9:8"
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
      "00c3e514",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e538",
      "DATA",
      [
        "storage",
        "002b28b9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3e514",
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e538",
      "DATA",
      [
        "storage",
        "002b2903",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d4bc.md#insn-00c3d4f0) · [`00c3d510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d4bc.md#insn-00c3d510) · [`00c3d514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d4bc.md#insn-00c3d514)
- 新版 [`00c3e4e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e4b0.md#insn-00c3e4e4) · [`00c3e504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e4b0.md#insn-00c3e504) · [`00c3e508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e4b0.md#insn-00c3e508)

~~~diff
- 00c3d4f0 ["INT_ADD", "register:40f0:8", ["const:c3d4f0:8", "const:4:8"]]
- 00c3d4f0 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3e4e4 ["INT_ADD", "register:40f0:8", ["const:c3e4e4:8", "const:4:8"]]
+ 00c3e4e4 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3d4f0 bytes 00730094
+ 00c3e4e4 bytes f7720094
- 00c3d510 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c3e504 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c3d510 bytes c80200d0
+ 00c3e504 bytes c80200d0
- 00c3d514 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3d514 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d514 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d514 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3e508 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 00c3e508 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e508 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e508 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d514 bytes 08811891
+ 00c3e508 bytes 08c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-292ea66f44c056da6615464f3c17287f"></a>

### [`00c3d56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d56c.md) → [`00c3e560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e560.md) FUN_00c3e560

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c3e5c4",
      "incomplete_value": false,
      "site": "00c3e5c4",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d5d0",
      "incomplete_value": false,
      "site": "00c3d5d0",
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
            "const:620:8"
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
      "definition_site": "00c3e5e8",
      "incomplete_value": false,
      "site": "00c3e5e8",
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
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d5f4",
      "incomplete_value": false,
      "site": "00c3d5f4",
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
            "const:9db:8"
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
      "00c3e5c4",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e5e8",
      "DATA",
      [
        "storage",
        "002a99db",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3e5c4",
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e5e8",
      "DATA",
      [
        "storage",
        "002a9aa8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d56c.md#insn-00c3d5a0) · [`00c3d5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d56c.md#insn-00c3d5c0) · [`00c3d5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d56c.md#insn-00c3d5c4)
- 新版 [`00c3e594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e560.md#insn-00c3e594) · [`00c3e5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e560.md#insn-00c3e5b4) · [`00c3e5b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e560.md#insn-00c3e5b8)

~~~diff
- 00c3d5a0 ["INT_ADD", "register:40f0:8", ["const:c3d5a0:8", "const:4:8"]]
- 00c3d5a0 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3e594 ["INT_ADD", "register:40f0:8", ["const:c3e594:8", "const:4:8"]]
+ 00c3e594 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3d5a0 bytes d4720094
+ 00c3e594 bytes cb720094
- 00c3d5c0 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c3e5b4 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c3d5c0 bytes c80200d0
+ 00c3e5b4 bytes c80200d0
- 00c3d5c4 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3d5c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d5c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d5c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3e5b8 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 00c3e5b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e5b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e5b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d5c4 bytes 08811891
+ 00c3e5b8 bytes 08c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bd9aa3df8d36e7410a903d0ed185441"></a>

### [`00c3d7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d7cc.md) → [`00c3e7c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e7c0.md) FUN_00c3e7c0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c3e824",
      "incomplete_value": false,
      "site": "00c3e824",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d830",
      "incomplete_value": false,
      "site": "00c3d830",
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
            "const:620:8"
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
      "definition_site": "00c3e848",
      "incomplete_value": false,
      "site": "00c3e848",
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
            "const:eff:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d854",
      "incomplete_value": false,
      "site": "00c3d854",
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
            "const:e21:8"
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
      "00c3e824",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e848",
      "DATA",
      [
        "storage",
        "002b9e21",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3e824",
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e848",
      "DATA",
      [
        "storage",
        "002b9eff",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d7cc.md#insn-00c3d800) · [`00c3d820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d7cc.md#insn-00c3d820) · [`00c3d824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d7cc.md#insn-00c3d824)
- 新版 [`00c3e7f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e7c0.md#insn-00c3e7f4) · [`00c3e814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e7c0.md#insn-00c3e814) · [`00c3e818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e7c0.md#insn-00c3e818)

~~~diff
- 00c3d800 ["INT_ADD", "register:40f0:8", ["const:c3d800:8", "const:4:8"]]
- 00c3d800 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3e7f4 ["INT_ADD", "register:40f0:8", ["const:c3e7f4:8", "const:4:8"]]
+ 00c3e7f4 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3d800 bytes 3c720094
+ 00c3e7f4 bytes 33720094
- 00c3d820 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c3e814 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c3d820 bytes c80200d0
+ 00c3e814 bytes c80200d0
- 00c3d824 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3d824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3e818 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 00c3e818 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e818 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e818 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d824 bytes 08811891
+ 00c3e818 bytes 08c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd115a839a6f9521d2656c8d868a94a9"></a>

### [`00c3d87c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d87c.md) → [`00c3e870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e870.md) FUN_00c3e870

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c3e8d8",
      "incomplete_value": false,
      "site": "00c3e8d8",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d8e4",
      "incomplete_value": false,
      "site": "00c3d8e4",
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
            "const:6a0:8"
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
      "00c3e8d8",
      "DATA",
      [
        "storage",
        "00c976a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3e8d8",
      "DATA",
      [
        "storage",
        "00c98670",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d87c.md#insn-00c3d8b4) · [`00c3d8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d87c.md#insn-00c3d8d4) · [`00c3d8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d87c.md#insn-00c3d8d8)
- 新版 [`00c3e8a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e870.md#insn-00c3e8a8) · [`00c3e8c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e870.md#insn-00c3e8c8) · [`00c3e8cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e870.md#insn-00c3e8cc)

~~~diff
- 00c3d8b4 ["INT_ADD", "register:40f0:8", ["const:c3d8b4:8", "const:4:8"]]
- 00c3d8b4 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3e8a8 ["INT_ADD", "register:40f0:8", ["const:c3e8a8:8", "const:4:8"]]
+ 00c3e8a8 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3d8b4 bytes 0f720094
+ 00c3e8a8 bytes 06720094
- 00c3d8d4 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c3e8c8 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c3d8d4 bytes c80200d0
+ 00c3e8c8 bytes c80200d0
- 00c3d8d8 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 00c3d8d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d8d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d8d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3e8cc ["COPY", "tmp:0:8", ["const:670:8"]]
+ 00c3e8cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e8cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e8cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d8d8 bytes 08811a91
+ 00c3e8cc bytes 08c11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a50e686a96df5b857dea89cb6751ce15"></a>

### [`00c3d924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d924.md) → [`00c3e918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e918.md) FUN_00c3e918

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c3e97c",
      "incomplete_value": false,
      "site": "00c3e97c",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d988",
      "incomplete_value": false,
      "site": "00c3d988",
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
            "const:620:8"
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
      "definition_site": "00c3e9a0",
      "incomplete_value": false,
      "site": "00c3e9a0",
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
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d9ac",
      "incomplete_value": false,
      "site": "00c3d9ac",
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
            "const:889:8"
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
      "00c3e97c",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e9a0",
      "DATA",
      [
        "storage",
        "002b0889",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3e97c",
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3e9a0",
      "DATA",
      [
        "storage",
        "002b0960",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3d958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d924.md#insn-00c3d958) · [`00c3d978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d924.md#insn-00c3d978) · [`00c3d97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d924.md#insn-00c3d97c)
- 新版 [`00c3e94c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e918.md#insn-00c3e94c) · [`00c3e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e918.md#insn-00c3e96c) · [`00c3e970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e918.md#insn-00c3e970)

~~~diff
- 00c3d958 ["INT_ADD", "register:40f0:8", ["const:c3d958:8", "const:4:8"]]
- 00c3d958 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3e94c ["INT_ADD", "register:40f0:8", ["const:c3e94c:8", "const:4:8"]]
+ 00c3e94c ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3d958 bytes e6710094
+ 00c3e94c bytes dd710094
- 00c3d978 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c3e96c ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c3d978 bytes c80200d0
+ 00c3e96c bytes c80200d0
- 00c3d97c ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3d97c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d97c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3d97c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3e970 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 00c3e970 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e970 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3e970 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3d97c bytes 08811891
+ 00c3e970 bytes 08c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-670975eb6c350595887fac6494986367"></a>

### [`00c3d9d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d9d4.md) → [`00c3e9c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e9c8.md) FUN_00c3e9c8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c3ea2c",
      "incomplete_value": false,
      "site": "00c3ea2c",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3da38",
      "incomplete_value": false,
      "site": "00c3da38",
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
            "const:620:8"
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
      "definition_site": "00c3ea50",
      "incomplete_value": false,
      "site": "00c3ea50",
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
            "const:e9e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3da5c",
      "incomplete_value": false,
      "site": "00c3da5c",
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
            "const:e54:8"
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
      "00c3ea2c",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3ea50",
      "DATA",
      [
        "storage",
        "002c0e54",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3ea2c",
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3ea50",
      "DATA",
      [
        "storage",
        "002c0e9e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3da08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d9d4.md#insn-00c3da08) · [`00c3da28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d9d4.md#insn-00c3da28) · [`00c3da2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d9d4.md#insn-00c3da2c)
- 新版 [`00c3e9fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e9c8.md#insn-00c3e9fc) · [`00c3ea1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e9c8.md#insn-00c3ea1c) · [`00c3ea20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e9c8.md#insn-00c3ea20)

~~~diff
- 00c3da08 ["INT_ADD", "register:40f0:8", ["const:c3da08:8", "const:4:8"]]
- 00c3da08 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3e9fc ["INT_ADD", "register:40f0:8", ["const:c3e9fc:8", "const:4:8"]]
+ 00c3e9fc ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3da08 bytes ba710094
+ 00c3e9fc bytes b1710094
- 00c3da28 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c3ea1c ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c3da28 bytes c80200d0
+ 00c3ea1c bytes c80200d0
- 00c3da2c ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3da2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3da2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3da2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3ea20 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 00c3ea20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3ea20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3ea20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3da2c bytes 08811891
+ 00c3ea20 bytes 08c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cad8d1d89c7f869af17a5e77bbd175e"></a>

### [`00c3da84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3da84.md) → [`00c3ea78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3ea78.md) FUN_00c3ea78

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3eadc",
      "incomplete_value": false,
      "site": "00c3eadc",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3dae8",
      "incomplete_value": false,
      "site": "00c3dae8",
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
            "const:620:8"
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
      "definition_site": "00c3eb00",
      "incomplete_value": false,
      "site": "00c3eb00",
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
            "const:a97:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3db0c",
      "incomplete_value": false,
      "site": "00c3db0c",
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
            "const:93f:8"
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
      "00c3eadc",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3eb00",
      "DATA",
      [
        "storage",
        "002a893f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3eadc",
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3eb00",
      "DATA",
      [
        "storage",
        "002a8a97",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3dab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3da84.md#insn-00c3dab8) · [`00c3dad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3da84.md#insn-00c3dad8) · [`00c3dadc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3da84.md#insn-00c3dadc)
- 新版 [`00c3eaac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3ea78.md#insn-00c3eaac) · [`00c3eacc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3ea78.md#insn-00c3eacc) · [`00c3ead0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3ea78.md#insn-00c3ead0)

~~~diff
- 00c3dab8 ["INT_ADD", "register:40f0:8", ["const:c3dab8:8", "const:4:8"]]
- 00c3dab8 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3eaac ["INT_ADD", "register:40f0:8", ["const:c3eaac:8", "const:4:8"]]
+ 00c3eaac ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3dab8 bytes 8e710094
+ 00c3eaac bytes 85710094
- 00c3dad8 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c3eacc ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c3dad8 bytes c80200d0
+ 00c3eacc bytes c80200d0
- 00c3dadc ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3dadc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3dadc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3dadc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3ead0 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 00c3ead0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3ead0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3ead0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3dadc bytes 08811891
+ 00c3ead0 bytes 08c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b06db7e205b57a6fb748e1a8568371f"></a>

### [`00c3db30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3db30.md) → [`00c3eb24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3eb24.md) FUN_00c3eb24

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c3eb88",
      "incomplete_value": false,
      "site": "00c3eb88",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3db94",
      "incomplete_value": false,
      "site": "00c3db94",
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
            "const:620:8"
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
      "definition_site": "00c3ebac",
      "incomplete_value": false,
      "site": "00c3ebac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c2000:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3dbb8",
      "incomplete_value": false,
      "site": "00c3dbb8",
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
            "const:fe6:8"
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
      "00c3eb88",
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3ebac",
      "DATA",
      [
        "storage",
        "002c1fe6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3eb88",
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3ebac",
      "DATA",
      [
        "storage",
        "002c2030",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3db64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3db30.md#insn-00c3db64) · [`00c3db84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3db30.md#insn-00c3db84) · [`00c3db88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3db30.md#insn-00c3db88)
- 新版 [`00c3eb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3eb24.md#insn-00c3eb58) · [`00c3eb78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3eb24.md#insn-00c3eb78) · [`00c3eb7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3eb24.md#insn-00c3eb7c)

~~~diff
- 00c3db64 ["INT_ADD", "register:40f0:8", ["const:c3db64:8", "const:4:8"]]
- 00c3db64 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3eb58 ["INT_ADD", "register:40f0:8", ["const:c3eb58:8", "const:4:8"]]
+ 00c3eb58 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3db64 bytes 63710094
+ 00c3eb58 bytes 5a710094
- 00c3db84 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c3eb78 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c3db84 bytes c80200d0
+ 00c3eb78 bytes c80200d0
- 00c3db88 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3db88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3db88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3db88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3eb7c ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 00c3eb7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3eb7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3eb7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3db88 bytes 08811891
+ 00c3eb7c bytes 08c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f11857ebc8b6f747474280bc0cc78aec"></a>

### [`00c3decc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3decc.md) → [`00c3eec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3eec0.md) FUN_00c3eec0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

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
      "definition_site": "00c3ef28",
      "incomplete_value": true,
      "site": "00c3ef34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1e6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3df34",
      "incomplete_value": true,
      "site": "00c3df40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:108:8"
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
      "definition_site": "00c3ef2c",
      "incomplete_value": true,
      "site": "00c3ef38",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00c3df38",
      "incomplete_value": true,
      "site": "00c3df44",
      "value": [
        "LOAD",
        "8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3ef28",
      "READ",
      [
        "storage",
        "002bb108",
        null,
        "string"
      ]
    ],
    [
      "00c3ef2c",
      "READ",
      [
        "storage",
        "002bb118",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3ef28",
      "READ",
      [
        "storage",
        "002bb1e6",
        null,
        "string"
      ]
    ],
    [
      "00c3ef2c",
      "READ",
      [
        "storage",
        "002bb1f6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3df14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3decc.md#insn-00c3df14) · [`00c3df2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3decc.md#insn-00c3df2c) · [`00c3df64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3decc.md#insn-00c3df64)
- 新版 [`00c3ef08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3eec0.md#insn-00c3ef08) · [`00c3ef20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3eec0.md#insn-00c3ef20) · [`00c3ef58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3eec0.md#insn-00c3ef58)

~~~diff
- 00c3df14 ["INT_ADD", "register:40f0:8", ["const:c3df14:8", "const:4:8"]]
- 00c3df14 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c3ef08 ["INT_ADD", "register:40f0:8", ["const:c3ef08:8", "const:4:8"]]
+ 00c3ef08 ["CALL", null, ["callee:00c5b140:8"]]
- 00c3df14 bytes 97700094
+ 00c3ef08 bytes 8e700094
- 00c3df2c ["COPY", "tmp:0:8", ["const:108:8"]]
- 00c3df2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c3df2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c3df2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c3ef20 ["COPY", "tmp:0:8", ["const:1e6:8"]]
+ 00c3ef20 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c3ef20 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c3ef20 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c3df2c bytes 4a210491
+ 00c3ef20 bytes 4a990791
- 00c3df64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c3df64 ["INT_ADD", "register:40f0:8", ["const:c3df64:8", "const:4:8"]]
- 00c3df64 ["CALLIND", null, ["register:0:8"]]
+ 00c3ef58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3ef58 ["INT_ADD", "register:40f0:8", ["const:c3ef58:8", "const:4:8"]]
+ 00c3ef58 ["CALLIND", null, ["register:0:8"]]
- 00c3df64 bytes 00013fd6
+ 00c3ef58 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb75e44ee028c5357ee155ebe67f5a1a"></a>

### [`00c3e04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) → [`00c3f040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f040.md) FUN_00c3f040

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 7件 [`00c3dbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3dbe0.md) [`00c3f3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c42528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md) [`00c43708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 7件 [`00c3ebd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3ebd4.md) [`00c403a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c403a0.md) [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c4351c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c4351c.md) [`00c446fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c446fc.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.26% / 新版 96.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3f160",
      "incomplete_value": false,
      "site": "00c3f160",
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
      "definition_site": "00c3e16c",
      "incomplete_value": false,
      "site": "00c3e16c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c3f160",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3f16c",
      "DATA",
      [
        "storage",
        "002af708",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3f160",
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3f16c",
      "DATA",
      [
        "storage",
        "002af7df",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3e13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md#insn-00c3e13c) · [`00c3e15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md#insn-00c3e15c) · [`00c3e160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md#insn-00c3e160)
- 新版 [`00c3f130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f040.md#insn-00c3f130) · [`00c3f150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f040.md#insn-00c3f150) · [`00c3f154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f040.md#insn-00c3f154)

~~~diff
- 00c3e13c ["INT_ADD", "register:40f0:8", ["const:c3e13c:8", "const:4:8"]]
- 00c3e13c ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3f130 ["INT_ADD", "register:40f0:8", ["const:c3f130:8", "const:4:8"]]
+ 00c3f130 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3e13c bytes ed6f0094
+ 00c3f130 bytes e46f0094
- 00c3e15c ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c3f150 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c3e15c bytes c80200b0
+ 00c3f150 bytes c80200b0
- 00c3e160 ["COPY", "tmp:0:8", ["const:710:8"]]
- 00c3e160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3e160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3e160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3f154 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 00c3f154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3f154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3f154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3e160 bytes 08411c91
+ 00c3f154 bytes 08811b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e88ad5122e0cab4b398ac187215b300b"></a>

### [`00c3e278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e278.md) → [`00c3f26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f26c.md) FUN_00c3f26c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00c3f2d0",
      "incomplete_value": false,
      "site": "00c3f2d0",
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
      "definition_site": "00c3e2dc",
      "incomplete_value": false,
      "site": "00c3e2dc",
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
      "00c3f2d0",
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
      "00c3f2d0",
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

- 旧版 [`00c3e2ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e278.md#insn-00c3e2ac) · [`00c3e2cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e278.md#insn-00c3e2cc) · [`00c3e2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e278.md#insn-00c3e2d0)
- 新版 [`00c3f2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f26c.md#insn-00c3f2a0) · [`00c3f2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f26c.md#insn-00c3f2c0) · [`00c3f2c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f26c.md#insn-00c3f2c4)

~~~diff
- 00c3e2ac ["INT_ADD", "register:40f0:8", ["const:c3e2ac:8", "const:4:8"]]
- 00c3e2ac ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3f2a0 ["INT_ADD", "register:40f0:8", ["const:c3f2a0:8", "const:4:8"]]
+ 00c3f2a0 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3e2ac bytes 916f0094
+ 00c3f2a0 bytes 886f0094
- 00c3e2cc ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c3f2c0 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c3e2cc bytes c80200b0
+ 00c3f2c0 bytes c80200b0
- 00c3e2d0 ["COPY", "tmp:0:8", ["const:710:8"]]
- 00c3e2d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3e2d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3e2d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3f2c4 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 00c3f2c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3f2c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3f2c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3e2d0 bytes 08411c91
+ 00c3f2c4 bytes 08811b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce7d7adebc5843ebb90222bb9e903c2c"></a>

### [`00c3e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e4f0.md) → [`00c3f4e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f4e4.md) FUN_00c3f4e4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) · 呼出先 4件 [`00c3f0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f0d0.md) [`00c3f3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 2件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) · 呼出先 4件 [`00c400c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c400c4.md) [`00c403a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c403a0.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.74% / 新版 96.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3f5e8",
      "incomplete_value": false,
      "site": "00c3f5f4",
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
            "const:dff:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3e5f4",
      "incomplete_value": false,
      "site": "00c3e600",
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
            "const:d30:8"
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
      "00c3f5cc",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3f5f4",
      "DATA",
      [
        "storage",
        "002b8d30",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c3f5cc",
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3f5f4",
      "DATA",
      [
        "storage",
        "002b8dff",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3e548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e4f0.md#insn-00c3e548) · [`00c3e598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e4f0.md#insn-00c3e598) · [`00c3e5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e4f0.md#insn-00c3e5c8)
- 新版 [`00c3f53c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f4e4.md#insn-00c3f53c) · [`00c3f58c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f4e4.md#insn-00c3f58c) · [`00c3f5bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f4e4.md#insn-00c3f5bc)

~~~diff
- 00c3e548 ["INT_ADD", "register:40f0:8", ["const:c3e548:8", "const:4:8"]]
- 00c3e548 ["CALL", null, ["callee:00c400c4:8"]]
+ 00c3f53c ["INT_ADD", "register:40f0:8", ["const:c3f53c:8", "const:4:8"]]
+ 00c3f53c ["CALL", null, ["callee:00c400c4:8"]]
- 00c3e548 bytes e2020094
+ 00c3f53c bytes e2020094
- 00c3e598 ["INT_ADD", "register:40f0:8", ["const:c3e598:8", "const:4:8"]]
- 00c3e598 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3f58c ["INT_ADD", "register:40f0:8", ["const:c3f58c:8", "const:4:8"]]
+ 00c3f58c ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3e598 bytes d66e0094
+ 00c3f58c bytes cd6e0094
- 00c3e5c8 ["COPY", "register:4048:8", ["const:c97000:8"]]
+ 00c3f5bc ["COPY", "register:4048:8", ["const:c98000:8"]]
- 00c3e5c8 bytes c90200b0
+ 00c3f5bc bytes c90200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1afa0fd1e87c8156c499871200c3d251"></a>

### [`00c3e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) → [`00c3f654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f654.md) FUN_00c3f654

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c43708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) [`00c4b848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md) [`00c4e684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md) · 呼出先 8件 [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3ce7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)
- 新版 呼出元 5件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c446fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c446fc.md) [`00c4c83c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c83c.md) [`00c4f678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4f678.md) · 呼出先 8件 [`00c3d9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md) [`00c3de70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md) [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.02% / 新版 99.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3fad4",
      "incomplete_value": false,
      "site": "00c3fad4",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3eae0",
      "incomplete_value": false,
      "site": "00c3eae0",
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
            "const:5a0:8"
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
      "00c3f868",
      "DATA",
      [
        "storage",
        "00c99530",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3fad4",
      "DATA",
      [
        "storage",
        "00c995a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3f868",
      "DATA",
      [
        "storage",
        "00c9a500",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3fad4",
      "DATA",
      [
        "storage",
        "00c9a570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3e6d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md#insn-00c3e6d4) · [`00c3e6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md#insn-00c3e6e0) · [`00c3e6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md#insn-00c3e6e8)
- 新版 [`00c3f6c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f654.md#insn-00c3f6c8) · [`00c3f6d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f654.md#insn-00c3f6d4) · [`00c3f6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f654.md#insn-00c3f6dc)

~~~diff
- 00c3e6d4 ["INT_ADD", "register:40f0:8", ["const:c3e6d4:8", "const:4:8"]]
- 00c3e6d4 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c3f6c8 ["INT_ADD", "register:40f0:8", ["const:c3f6c8:8", "const:4:8"]]
+ 00c3f6c8 ["CALL", null, ["callee:00c5b140:8"]]
- 00c3e6d4 bytes a76e0094
+ 00c3f6c8 bytes 9e6e0094
- 00c3e6e0 ["INT_ADD", "register:40f0:8", ["const:c3e6e0:8", "const:4:8"]]
- 00c3e6e0 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00c3f6d4 ["INT_ADD", "register:40f0:8", ["const:c3f6d4:8", "const:4:8"]]
+ 00c3f6d4 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00c3e6e0 bytes cc720094
+ 00c3f6d4 bytes c3720094
- 00c3e6e8 ["INT_ADD", "register:40f0:8", ["const:c3e6e8:8", "const:4:8"]]
- 00c3e6e8 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3f6dc ["INT_ADD", "register:40f0:8", ["const:c3f6dc:8", "const:4:8"]]
+ 00c3f6dc ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3e6e8 bytes 826e0094
+ 00c3f6dc bytes 796e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19d2d3ae31e3a4b77c036b4133e48f13"></a>

### [`00c3eb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3eb30.md) → [`00c3fb24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3fb24.md) FUN_00c3fb24

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c43708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 2件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c446fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c446fc.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c3fb8c",
      "incomplete_value": false,
      "site": "00c3fb8c",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3eb98",
      "incomplete_value": false,
      "site": "00c3eb98",
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
            "const:610:8"
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
      "00c3fb8c",
      "DATA",
      [
        "storage",
        "00c99610",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c3fb8c",
      "DATA",
      [
        "storage",
        "00c9a5e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3eb68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3eb30.md#insn-00c3eb68) · [`00c3eb88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3eb30.md#insn-00c3eb88) · [`00c3eb8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3eb30.md#insn-00c3eb8c)
- 新版 [`00c3fb5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3fb24.md#insn-00c3fb5c) · [`00c3fb7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3fb24.md#insn-00c3fb7c) · [`00c3fb80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3fb24.md#insn-00c3fb80)

~~~diff
- 00c3eb68 ["INT_ADD", "register:40f0:8", ["const:c3eb68:8", "const:4:8"]]
- 00c3eb68 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3fb5c ["INT_ADD", "register:40f0:8", ["const:c3fb5c:8", "const:4:8"]]
+ 00c3fb5c ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3eb68 bytes 626d0094
+ 00c3fb5c bytes 596d0094
- 00c3eb88 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c3fb7c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c3eb88 bytes c80200f0
+ 00c3fb7c bytes c80200f0
- 00c3eb8c ["COPY", "tmp:0:8", ["const:610:8"]]
- 00c3eb8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3eb8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3eb8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3fb80 ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 00c3fb80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3fb80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3fb80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3eb8c bytes 08411891
+ 00c3fb80 bytes 08811791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec26f416c108181455f73046559dd2a6"></a>

### [`00c3ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ebd8.md) → [`00c3fbcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3fbcc.md) FUN_00c3fbcc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 4件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c4b6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) · 呼出先 7件 [`00c3fa0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fa0c.md) [`00c3fae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fae4.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 4件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c4c6b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c6b8.md) · 呼出先 7件 [`00c40a00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40a00.md) [`00c40ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40ad8.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.34% / 新版 98.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3fe38",
      "incomplete_value": false,
      "site": "00c3fe38",
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
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3ee44",
      "incomplete_value": false,
      "site": "00c3ee44",
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
            "const:7f0:8"
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
      "00c3fd20",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3fe38",
      "DATA",
      [
        "storage",
        "00c977f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3ff18",
      "PARAM",
      [
        "storage",
        "002a1d4c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c3fd20",
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3fe38",
      "DATA",
      [
        "storage",
        "00c987c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c3ff18",
      "PARAM",
      [
        "storage",
        "002a1d8c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3ecfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ebd8.md#insn-00c3ecfc) · [`00c3ed1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ebd8.md#insn-00c3ed1c) · [`00c3ed20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ebd8.md#insn-00c3ed20)
- 新版 [`00c3fcf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3fbcc.md#insn-00c3fcf0) · [`00c3fd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3fbcc.md#insn-00c3fd10) · [`00c3fd14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3fbcc.md#insn-00c3fd14)

~~~diff
- 00c3ecfc ["INT_ADD", "register:40f0:8", ["const:c3ecfc:8", "const:4:8"]]
- 00c3ecfc ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c3fcf0 ["INT_ADD", "register:40f0:8", ["const:c3fcf0:8", "const:4:8"]]
+ 00c3fcf0 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3ecfc bytes fd6c0094
+ 00c3fcf0 bytes f46c0094
- 00c3ed1c ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c3fd10 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c3ed1c bytes c80200b0
+ 00c3fd10 bytes c80200b0
- 00c3ed20 ["COPY", "tmp:0:8", ["const:710:8"]]
- 00c3ed20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3ed20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3ed20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c3fd14 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 00c3fd14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3fd14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c3fd14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3ed20 bytes 08411c91
+ 00c3fd14 bytes 08811b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82e859fbb9c12fcdc262588dbcd77343"></a>

### [`00c3ef9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ef9c.md) → [`00c3ff90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3ff90.md) FUN_00c3ff90

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c4b6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) · 呼出先 3件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 3件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c4c6b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c6b8.md) · 呼出先 3件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4006c",
      "incomplete_value": false,
      "site": "00c4006c",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f078",
      "incomplete_value": false,
      "site": "00c3f078",
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
            "const:110:8"
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
      "definition_site": "00c4008c",
      "incomplete_value": false,
      "site": "00c4008c",
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
            "const:5fd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f098",
      "incomplete_value": false,
      "site": "00c3f098",
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
            "const:530:8"
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
      "00c4006c",
      "DATA",
      [
        "storage",
        "00c98110",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4008c",
      "DATA",
      [
        "storage",
        "002ae530",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4006c",
      "DATA",
      [
        "storage",
        "00c990e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4008c",
      "DATA",
      [
        "storage",
        "002ae5fd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3effc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ef9c.md#insn-00c3effc) · [`00c3f044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ef9c.md#insn-00c3f044) · [`00c3f068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ef9c.md#insn-00c3f068)
- 新版 [`00c3fff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3ff90.md#insn-00c3fff0) · [`00c40038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3ff90.md#insn-00c40038) · [`00c4005c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3ff90.md#insn-00c4005c)

~~~diff
- 00c3effc ["INT_ADD", "register:40f0:8", ["const:c3effc:8", "const:4:8"]]
- 00c3effc ["CALL", null, ["callee:00c40e0c:8"]]
+ 00c3fff0 ["INT_ADD", "register:40f0:8", ["const:c3fff0:8", "const:4:8"]]
+ 00c3fff0 ["CALL", null, ["callee:00c40e0c:8"]]
- 00c3effc bytes 87030094
+ 00c3fff0 bytes 87030094
- 00c3f044 ["INT_ADD", "register:40f0:8", ["const:c3f044:8", "const:4:8"]]
- 00c3f044 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c40038 ["INT_ADD", "register:40f0:8", ["const:c40038:8", "const:4:8"]]
+ 00c40038 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3f044 bytes 2b6c0094
+ 00c40038 bytes 226c0094
- 00c3f068 ["COPY", "register:4050:8", ["const:c98000:8"]]
+ 00c4005c ["COPY", "register:4050:8", ["const:c99000:8"]]
- 00c3f068 bytes ca0200b0
+ 00c4005c bytes ca0200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ac1d7fdbe224111ec4d459b51d4a38a"></a>

### [`00c3f0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f0d0.md) → [`00c400c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c400c4.md) FUN_00c400c4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e4f0.md) [`00c4b6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) · 呼出先 6件 [`00c4c2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c2c4.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md)
- 新版 呼出元 3件 [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c3f4e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f4e4.md) [`00c4c6b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c6b8.md) · 呼出先 6件 [`00c4d2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d2b8.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c402e8",
      "incomplete_value": false,
      "site": "00c402ec",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f2f4",
      "incomplete_value": false,
      "site": "00c3f2f8",
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
            "const:140:8"
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
      "00c402ec",
      "DATA",
      [
        "storage",
        "00c99140",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c402ec",
      "DATA",
      [
        "storage",
        "00c9a110",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3f29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f0d0.md#insn-00c3f29c) · [`00c3f2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f0d0.md#insn-00c3f2f0) · [`00c3f2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f0d0.md#insn-00c3f2f4)
- 新版 [`00c40290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c400c4.md#insn-00c40290) · [`00c402e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c400c4.md#insn-00c402e4) · [`00c402e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c400c4.md#insn-00c402e8)

~~~diff
- 00c3f29c ["INT_ADD", "register:40f0:8", ["const:c3f29c:8", "const:4:8"]]
- 00c3f29c ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c40290 ["INT_ADD", "register:40f0:8", ["const:c40290:8", "const:4:8"]]
+ 00c40290 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3f29c bytes 956b0094
+ 00c40290 bytes 8c6b0094
- 00c3f2f0 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c402e4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c3f2f0 bytes c80200d0
+ 00c402e4 bytes c80200d0
- 00c3f2f4 ["COPY", "tmp:0:8", ["const:140:8"]]
- 00c3f2f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3f2f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3f2f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c402e8 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 00c402e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c402e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c402e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3f2f4 bytes 08010591
+ 00c402e8 bytes 08410491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9aeeb91e2e1fa5838c5d8e50c830873c"></a>

### [`00c3f3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) → [`00c403a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c403a0.md) FUN_00c403a0

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3e4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e4f0.md) · 呼出先 13件 [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3ce7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3dbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3dbe0.md) [`00c3e04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c465bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md)
- 新版 呼出元 2件 [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c3f4e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f4e4.md) · 呼出先 13件 [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c3de70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md) [`00c3ebd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3ebd4.md) [`00c3f040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f040.md) [`00c475b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c475b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.10% / 新版 98.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c405e8",
      "incomplete_value": false,
      "site": "00c405e8",
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
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f5f4",
      "incomplete_value": false,
      "site": "00c3f5f4",
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
            "const:370:8"
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
      "definition_site": "00c40850",
      "incomplete_value": false,
      "site": "00c40850",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f85c",
      "incomplete_value": false,
      "site": "00c3f85c",
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
            "const:290:8"
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4052c",
      "DATA",
      [
        "storage",
        "00c991c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00c405e8",
      "DATA",
      [
        "storage",
        "00c99370",
        null,
        "undefined *"
      ]
    ],
    [
      "00c406d8",
      "DATA",
      [
        "storage",
        "00c99450",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4052c",
      "DATA",
      [
        "storage",
        "00c9a198",
        null,
        "undefined *"
      ]
    ],
    [
      "00c405e8",
      "DATA",
      [
        "storage",
        "00c9a340",
        null,
        "undefined *"
      ]
    ],
    [
      "00c406d8",
      "DATA",
      [
        "storage",
        "00c9a420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c3f3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md#insn-00c3f3e0) · [`00c3f464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md#insn-00c3f464) · [`00c3f484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md#insn-00c3f484)
- 新版 [`00c403d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c403a0.md#insn-00c403d4) · [`00c40458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c403a0.md#insn-00c40458) · [`00c40478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c403a0.md#insn-00c40478)

~~~diff
- 00c3f3e0 ["INT_ADD", "register:40f0:8", ["const:c3f3e0:8", "const:4:8"]]
- 00c3f3e0 ["CALL", null, ["callee:00c3ebd4:8"]]
+ 00c403d4 ["INT_ADD", "register:40f0:8", ["const:c403d4:8", "const:4:8"]]
+ 00c403d4 ["CALL", null, ["callee:00c3ebd4:8"]]
- 00c3f3e0 bytes 00faff97
+ 00c403d4 bytes 00faff97
- 00c3f464 ["INT_ADD", "register:40f0:8", ["const:c3f464:8", "const:4:8"]]
- 00c3f464 ["CALL", null, ["callee:00c3f040:8"]]
+ 00c40458 ["INT_ADD", "register:40f0:8", ["const:c40458:8", "const:4:8"]]
+ 00c40458 ["CALL", null, ["callee:00c3f040:8"]]
- 00c3f464 bytes fafaff97
+ 00c40458 bytes fafaff97
- 00c3f484 ["INT_ADD", "register:40f0:8", ["const:c3f484:8", "const:4:8"]]
- 00c3f484 ["CALL", null, ["callee:00c475b0:8"]]
+ 00c40478 ["INT_ADD", "register:40f0:8", ["const:c40478:8", "const:4:8"]]
+ 00c40478 ["CALL", null, ["callee:00c475b0:8"]]
- 00c3f484 bytes 4e1c0094
+ 00c40478 bytes 4e1c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f318a3d6f117c396adbb6208de74ac47"></a>

### [`00c3f96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f96c.md) → [`00c40960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40960.md) FUN_00c40960

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00c409c4",
      "incomplete_value": false,
      "site": "00c409c4",
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
      "definition_site": "00c3f9d0",
      "incomplete_value": false,
      "site": "00c3f9d0",
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
      "00c409c4",
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
      "00c409c4",
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

- 旧版 [`00c3f9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f96c.md#insn-00c3f9a0) · [`00c3f9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f96c.md#insn-00c3f9c0) · [`00c3f9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f96c.md#insn-00c3f9c4)
- 新版 [`00c40994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40960.md#insn-00c40994) · [`00c409b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40960.md#insn-00c409b4) · [`00c409b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40960.md#insn-00c409b8)

~~~diff
- 00c3f9a0 ["INT_ADD", "register:40f0:8", ["const:c3f9a0:8", "const:4:8"]]
- 00c3f9a0 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c40994 ["INT_ADD", "register:40f0:8", ["const:c40994:8", "const:4:8"]]
+ 00c40994 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3f9a0 bytes d4690094
+ 00c40994 bytes cb690094
- 00c3f9c0 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c409b4 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c3f9c0 bytes c8020090
+ 00c409b4 bytes c8020090
- 00c3f9c4 ["COPY", "tmp:0:8", ["const:710:8"]]
- 00c3f9c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c3f9c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c3f9c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c409b8 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 00c409b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c409b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c409b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c3f9c4 bytes 08411c91
+ 00c409b8 bytes 08811b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86d74f6749eed9cf5780d82bcb7a89fc"></a>

### [`00c3fae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fae4.md) → [`00c40ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40ad8.md) FUN_00c40ad8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ebd8.md) · 呼出先 3件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 2件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3fbcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3fbcc.md) · 呼出先 3件 [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c40b44",
      "incomplete_value": false,
      "site": "00c40b44",
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
      "definition_site": "00c3fb50",
      "incomplete_value": false,
      "site": "00c3fb50",
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
      "00c40b44",
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
      "00c40b44",
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

- 旧版 [`00c3fb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fae4.md#insn-00c3fb18) · [`00c3fb40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fae4.md#insn-00c3fb40) · [`00c3fb44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fae4.md#insn-00c3fb44)
- 新版 [`00c40b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40ad8.md#insn-00c40b0c) · [`00c40b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40ad8.md#insn-00c40b34) · [`00c40b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40ad8.md#insn-00c40b38)

~~~diff
- 00c3fb18 ["INT_ADD", "register:40f0:8", ["const:c3fb18:8", "const:4:8"]]
- 00c3fb18 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c40b0c ["INT_ADD", "register:40f0:8", ["const:c40b0c:8", "const:4:8"]]
+ 00c40b0c ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c3fb18 bytes 76690094
+ 00c40b0c bytes 6d690094
- 00c3fb40 ["INT_ADD", "register:40f0:8", ["const:c3fb40:8", "const:4:8"]]
- 00c3fb40 ["CALL", null, ["callee:00c59080:8"]]
+ 00c40b34 ["INT_ADD", "register:40f0:8", ["const:c40b34:8", "const:4:8"]]
+ 00c40b34 ["CALL", null, ["callee:00c59080:8"]]
- 00c3fb40 bytes 5c610094
+ 00c40b34 bytes 53610094
- 00c3fb44 ["COPY", "register:4048:8", ["const:c97000:8"]]
+ 00c40b38 ["COPY", "register:4048:8", ["const:c98000:8"]]
- 00c3fb44 bytes c9020090
+ 00c40b38 bytes c9020090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b96cb32dae086a1862855ae16f3d7bb0"></a>

### [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) → [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) FUN_00c40e0c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 14件 [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c3ef9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ef9c.md) · 呼出先 42件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c3a1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a1b4.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3cd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cd04.md)
- 新版 呼出元 14件 [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md) [`00c3f654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f654.md) [`00c3ff90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3ff90.md) · 呼出先 42件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c3b1a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b1a8.md) [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md) [`00c3dcf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3dcf8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.24% / 新版 98.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c415a0",
      "incomplete_value": false,
      "site": "00c415a0",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c405ac",
      "incomplete_value": false,
      "site": "00c405ac",
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
            "const:ee0:8"
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c419e0",
      "incomplete_value": false,
      "site": "00c419e0",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c409ec",
      "incomplete_value": false,
      "site": "00c409ec",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "ordinal": 105,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4208c",
      "incomplete_value": false,
      "site": "00c4208c",
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
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41098",
      "incomplete_value": false,
      "site": "00c41098",
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
            "const:8f0:8"
          ]
        ]
      ]
    },
    "ordinal": 164,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c40ee0",
      "READ",
      [
        "storage",
        "00c97a30",
        null,
        "undefined1"
      ]
    ],
    [
      "00c40ef0",
      "READ",
      [
        "storage",
        "00c97a31",
        null,
        "undefined1"
      ]
    ],
    [
      "00c40f1c",
      "READ",
      [
        "storage",
        "00c97a40",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c40ee0",
      "READ",
      [
        "storage",
        "00c98a00",
        null,
        "undefined1"
      ]
    ],
    [
      "00c40ef0",
      "READ",
      [
        "storage",
        "00c98a01",
        null,
        "undefined1"
      ]
    ],
    [
      "00c40f1c",
      "READ",
      [
        "storage",
        "00c98a10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c402d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md#insn-00c402d0) · [`00c40330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md#insn-00c40330) · [`00c408d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md#insn-00c408d4)
- 新版 [`00c412c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md#insn-00c412c4) · [`00c41324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md#insn-00c41324) · [`00c418c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md#insn-00c418c8)

~~~diff
- 00c402d0 ["INT_ADD", "register:40f0:8", ["const:c402d0:8", "const:4:8"]]
- 00c402d0 ["CALL", null, ["callee:00c3b1a8:8"]]
+ 00c412c4 ["INT_ADD", "register:40f0:8", ["const:c412c4:8", "const:4:8"]]
+ 00c412c4 ["CALL", null, ["callee:00c3b1a8:8"]]
- 00c402d0 bytes b9e7ff97
+ 00c412c4 bytes b9e7ff97
- 00c40330 ["INT_ADD", "register:40f0:8", ["const:c40330:8", "const:4:8"]]
- 00c40330 ["CALL", null, ["callee:00c3b1a8:8"]]
+ 00c41324 ["INT_ADD", "register:40f0:8", ["const:c41324:8", "const:4:8"]]
+ 00c41324 ["CALL", null, ["callee:00c3b1a8:8"]]
- 00c40330 bytes a1e7ff97
+ 00c41324 bytes a1e7ff97
- 00c408d4 ["INT_ADD", "register:40f0:8", ["const:c408d4:8", "const:4:8"]]
- 00c408d4 ["CALL", null, ["callee:00c3b1a8:8"]]
+ 00c418c8 ["INT_ADD", "register:40f0:8", ["const:c418c8:8", "const:4:8"]]
+ 00c418c8 ["CALL", null, ["callee:00c3b1a8:8"]]
- 00c408d4 bytes 38e6ff97
+ 00c418c8 bytes 38e6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-824752597eee2fe0002f3da45a285ca4"></a>

### [`00c411a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c411a8.md) → [`00c4219c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c4219c.md) FUN_00c4219c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c4220c",
      "incomplete_value": false,
      "site": "00c4220c",
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
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41218",
      "incomplete_value": false,
      "site": "00c41218",
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
            "const:d20:8"
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
      "00c4220c",
      "DATA",
      [
        "storage",
        "00c97d20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4220c",
      "DATA",
      [
        "storage",
        "00c98cf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c411e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c411a8.md#insn-00c411e8) · [`00c41208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c411a8.md#insn-00c41208) · [`00c4120c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c411a8.md#insn-00c4120c)
- 新版 [`00c421dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c4219c.md#insn-00c421dc) · [`00c421fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c4219c.md#insn-00c421fc) · [`00c42200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c4219c.md#insn-00c42200)

~~~diff
- 00c411e8 ["INT_ADD", "register:40f0:8", ["const:c411e8:8", "const:4:8"]]
- 00c411e8 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c421dc ["INT_ADD", "register:40f0:8", ["const:c421dc:8", "const:4:8"]]
+ 00c421dc ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c411e8 bytes c2630094
+ 00c421dc bytes b9630094
- 00c41208 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c421fc ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c41208 bytes a80200d0
+ 00c421fc bytes a80200d0
- 00c4120c ["COPY", "tmp:0:8", ["const:d20:8"]]
- 00c4120c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4120c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4120c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c42200 ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 00c42200 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c42200 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c42200 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4120c bytes 08813491
+ 00c42200 bytes 08c13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80a2f927fd3d21fe857a0dd4bb5e883a"></a>

### [`00c41268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41268.md) → [`00c4225c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c4225c.md) FUN_00c4225c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c422cc",
      "incomplete_value": false,
      "site": "00c422cc",
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
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c412d8",
      "incomplete_value": false,
      "site": "00c412d8",
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
            "const:d90:8"
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
      "00c422cc",
      "DATA",
      [
        "storage",
        "00c97d90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c422cc",
      "DATA",
      [
        "storage",
        "00c98d60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c412a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41268.md#insn-00c412a8) · [`00c412c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41268.md#insn-00c412c8) · [`00c412cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41268.md#insn-00c412cc)
- 新版 [`00c4229c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c4225c.md#insn-00c4229c) · [`00c422bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c4225c.md#insn-00c422bc) · [`00c422c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c4225c.md#insn-00c422c0)

~~~diff
- 00c412a8 ["INT_ADD", "register:40f0:8", ["const:c412a8:8", "const:4:8"]]
- 00c412a8 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4229c ["INT_ADD", "register:40f0:8", ["const:c4229c:8", "const:4:8"]]
+ 00c4229c ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c412a8 bytes 92630094
+ 00c4229c bytes 89630094
- 00c412c8 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c422bc ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c412c8 bytes a80200d0
+ 00c422bc bytes a80200d0
- 00c412cc ["COPY", "tmp:0:8", ["const:d90:8"]]
- 00c412cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c412cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c412cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c422c0 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 00c422c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c422c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c422c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c412cc bytes 08413691
+ 00c422c0 bytes 08813591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4f61682422da9c512c7224d2af0d0e0"></a>

### [`00c41324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41324.md) → [`00c42318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42318.md) FUN_00c42318

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4238c",
      "incomplete_value": false,
      "site": "00c4238c",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41398",
      "incomplete_value": false,
      "site": "00c41398",
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
            "const:e00:8"
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
      "00c4238c",
      "DATA",
      [
        "storage",
        "00c97e00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4238c",
      "DATA",
      [
        "storage",
        "00c98dd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c41368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41324.md#insn-00c41368) · [`00c41388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41324.md#insn-00c41388) · [`00c4138c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41324.md#insn-00c4138c)
- 新版 [`00c4235c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42318.md#insn-00c4235c) · [`00c4237c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42318.md#insn-00c4237c) · [`00c42380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42318.md#insn-00c42380)

~~~diff
- 00c41368 ["INT_ADD", "register:40f0:8", ["const:c41368:8", "const:4:8"]]
- 00c41368 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4235c ["INT_ADD", "register:40f0:8", ["const:c4235c:8", "const:4:8"]]
+ 00c4235c ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c41368 bytes 62630094
+ 00c4235c bytes 59630094
- 00c41388 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c4237c ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c41388 bytes a80200d0
+ 00c4237c bytes a80200d0
- 00c4138c ["COPY", "tmp:0:8", ["const:e00:8"]]
- 00c4138c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4138c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4138c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c42380 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 00c42380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c42380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c42380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4138c bytes 08013891
+ 00c42380 bytes 08413791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-244137bb69a260a969b81fb26b9407e8"></a>

### [`00c413f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c413f0.md) → [`00c423e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c423e4.md) FUN_00c423e4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c42464",
      "incomplete_value": false,
      "site": "00c42464",
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
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41470",
      "incomplete_value": false,
      "site": "00c41470",
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
            "const:e70:8"
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
      "00c42464",
      "DATA",
      [
        "storage",
        "00c97e70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c42464",
      "DATA",
      [
        "storage",
        "00c98e40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c41440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c413f0.md#insn-00c41440) · [`00c41460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c413f0.md#insn-00c41460) · [`00c41464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c413f0.md#insn-00c41464)
- 新版 [`00c42434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c423e4.md#insn-00c42434) · [`00c42454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c423e4.md#insn-00c42454) · [`00c42458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c423e4.md#insn-00c42458)

~~~diff
- 00c41440 ["INT_ADD", "register:40f0:8", ["const:c41440:8", "const:4:8"]]
- 00c41440 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c42434 ["INT_ADD", "register:40f0:8", ["const:c42434:8", "const:4:8"]]
+ 00c42434 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c41440 bytes 2c630094
+ 00c42434 bytes 23630094
- 00c41460 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c42454 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c41460 bytes a80200d0
+ 00c42454 bytes a80200d0
- 00c41464 ["COPY", "tmp:0:8", ["const:e70:8"]]
- 00c41464 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c41464 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c41464 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c42458 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 00c42458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c42458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c42458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c41464 bytes 08c13991
+ 00c42458 bytes 08013991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-213c0fef1a6f861d26d88013c938dc53"></a>

### [`00c414dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c414dc.md) → [`00c424d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c424d0.md) FUN_00c424d0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c42540",
      "incomplete_value": false,
      "site": "00c42540",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4154c",
      "incomplete_value": false,
      "site": "00c4154c",
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
            "const:f50:8"
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
      "00c42540",
      "DATA",
      [
        "storage",
        "00c97f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c42540",
      "DATA",
      [
        "storage",
        "00c98f20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4151c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c414dc.md#insn-00c4151c) · [`00c4153c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c414dc.md#insn-00c4153c) · [`00c41540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c414dc.md#insn-00c41540)
- 新版 [`00c42510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c424d0.md#insn-00c42510) · [`00c42530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c424d0.md#insn-00c42530) · [`00c42534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c424d0.md#insn-00c42534)

~~~diff
- 00c4151c ["INT_ADD", "register:40f0:8", ["const:c4151c:8", "const:4:8"]]
- 00c4151c ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c42510 ["INT_ADD", "register:40f0:8", ["const:c42510:8", "const:4:8"]]
+ 00c42510 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4151c bytes f5620094
+ 00c42510 bytes ec620094
- 00c4153c ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c42530 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c4153c bytes a80200d0
+ 00c42530 bytes a80200d0
- 00c41540 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 00c41540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c41540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c41540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c42534 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 00c42534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c42534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c42534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c41540 bytes 08413d91
+ 00c42534 bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51cad1742ee379e004d5c32d666ab166"></a>

### [`00c4159c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c4159c.md) → [`00c42590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42590.md) FUN_00c42590

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c42600",
      "incomplete_value": false,
      "site": "00c42600",
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
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4160c",
      "incomplete_value": false,
      "site": "00c4160c",
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
            "const:fc0:8"
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
      "00c42600",
      "DATA",
      [
        "storage",
        "00c97fc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c42600",
      "DATA",
      [
        "storage",
        "00c98f90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c415dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c4159c.md#insn-00c415dc) · [`00c415fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c4159c.md#insn-00c415fc) · [`00c41600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c4159c.md#insn-00c41600)
- 新版 [`00c425d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42590.md#insn-00c425d0) · [`00c425f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42590.md#insn-00c425f0) · [`00c425f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42590.md#insn-00c425f4)

~~~diff
- 00c415dc ["INT_ADD", "register:40f0:8", ["const:c415dc:8", "const:4:8"]]
- 00c415dc ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c425d0 ["INT_ADD", "register:40f0:8", ["const:c425d0:8", "const:4:8"]]
+ 00c425d0 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c415dc bytes c5620094
+ 00c425d0 bytes bc620094
- 00c415fc ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c425f0 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c415fc bytes a80200d0
+ 00c425f0 bytes a80200d0
- 00c41600 ["COPY", "tmp:0:8", ["const:fc0:8"]]
- 00c41600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c41600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c41600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c425f4 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 00c425f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c425f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c425f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c41600 bytes 08013f91
+ 00c425f4 bytes 08413e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cae833759b91821cf775a958f04ff6f9"></a>

### [`00c4165c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c4165c.md) → [`00c42650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42650.md) FUN_00c42650

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c426c4",
      "incomplete_value": false,
      "site": "00c426c4",
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
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c416d0",
      "incomplete_value": false,
      "site": "00c416d0",
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
            "const:30:8"
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
      "00c426c4",
      "DATA",
      [
        "storage",
        "00c98030",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c426c4",
      "DATA",
      [
        "storage",
        "00c99000",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c416a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c4165c.md#insn-00c416a0) · [`00c416c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c4165c.md#insn-00c416c0) · [`00c416c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c4165c.md#insn-00c416c4)
- 新版 [`00c42694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42650.md#insn-00c42694) · [`00c426b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42650.md#insn-00c426b4) · [`00c426b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42650.md#insn-00c426b8)

~~~diff
- 00c416a0 ["INT_ADD", "register:40f0:8", ["const:c416a0:8", "const:4:8"]]
- 00c416a0 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c42694 ["INT_ADD", "register:40f0:8", ["const:c42694:8", "const:4:8"]]
+ 00c42694 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c416a0 bytes 94620094
+ 00c42694 bytes 8b620094
- 00c416c0 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c426b4 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c416c0 bytes a80200f0
+ 00c426b4 bytes a80200f0
- 00c416c4 ["COPY", "tmp:0:8", ["const:30:8"]]
- 00c416c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c416c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c416c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c426b8 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 00c426b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c426b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c426b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c416c4 bytes 08c10091
+ 00c426b8 bytes 08010091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6fb8d9c7df78568cbe34c3af68a138b"></a>

### [`00c41724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41724.md) → [`00c42718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42718.md) FUN_00c42718

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c4278c",
      "incomplete_value": false,
      "site": "00c4278c",
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
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41798",
      "incomplete_value": false,
      "site": "00c41798",
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
            "const:a0:8"
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
      "00c4278c",
      "DATA",
      [
        "storage",
        "00c980a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4278c",
      "DATA",
      [
        "storage",
        "00c99070",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c41768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41724.md#insn-00c41768) · [`00c41788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41724.md#insn-00c41788) · [`00c4178c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41724.md#insn-00c4178c)
- 新版 [`00c4275c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42718.md#insn-00c4275c) · [`00c4277c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42718.md#insn-00c4277c) · [`00c42780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42718.md#insn-00c42780)

~~~diff
- 00c41768 ["INT_ADD", "register:40f0:8", ["const:c41768:8", "const:4:8"]]
- 00c41768 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4275c ["INT_ADD", "register:40f0:8", ["const:c4275c:8", "const:4:8"]]
+ 00c4275c ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c41768 bytes 62620094
+ 00c4275c bytes 59620094
- 00c41788 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c4277c ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c41788 bytes a80200f0
+ 00c4277c bytes a80200f0
- 00c4178c ["COPY", "tmp:0:8", ["const:a0:8"]]
- 00c4178c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4178c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4178c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c42780 ["COPY", "tmp:0:8", ["const:70:8"]]
+ 00c42780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c42780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c42780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4178c bytes 08810291
+ 00c42780 bytes 08c10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87035e6ec6a47f625e4b2ed18157222e"></a>

### [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) → [`00c427e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md) FUN_00c427e0

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 12件 [`00c3a1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a1b4.md) [`00c3a214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c462d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c462d4.md) [`00c463c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c463c8.md)
- 新版 呼出元 2件 [`00c3d9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md) [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 12件 [`00c3b1a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b1a8.md) [`00c3b208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c472c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c472c8.md) [`00c473bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c473bc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.72% / 新版 95.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c42b24",
      "incomplete_value": false,
      "site": "00c42b24",
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
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41b30",
      "incomplete_value": false,
      "site": "00c41b30",
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
            "const:260:8"
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
      "definition_site": "00c42e40",
      "incomplete_value": false,
      "site": "00c42e40",
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
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41e4c",
      "incomplete_value": false,
      "site": "00c41e4c",
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
            "const:340:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c430bc",
      "incomplete_value": false,
      "site": "00c430bc",
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
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c420c8",
      "incomplete_value": false,
      "site": "00c420c8",
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
            "const:2d0:8"
          ]
        ]
      ]
    },
    "ordinal": 53,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c42840",
      "DATA",
      [
        "storage",
        "00312b1c",
        "switchD_00c41854::switchdataD_00312b1c",
        "ushort"
      ]
    ],
    [
      "00c42978",
      "PARAM",
      [
        "storage",
        "002ad191",
        null,
        "string"
      ]
    ],
    [
      "00c42990",
      "PARAM",
      [
        "storage",
        "002ac46c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c42840",
      "DATA",
      [
        "storage",
        "00312b5c",
        "switchD_00c42848::switchdataD_00312b5c",
        "ushort"
      ]
    ],
    [
      "00c42978",
      "PARAM",
      [
        "storage",
        "002ad25e",
        null,
        "string"
      ]
    ],
    [
      "00c42990",
      "PARAM",
      [
        "storage",
        "002ac539",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c41d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md#insn-00c41d38) · [`00c41840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md#insn-00c41840) · [`00c41848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md#insn-00c41848)
- 新版 [`00c42d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md#insn-00c42d2c) · [`00c42834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md#insn-00c42834)

~~~diff
- 00c41d38 ["INT_ADD", "register:40f0:8", ["const:c41d38:8", "const:4:8"]]
- 00c41d38 ["CALL", null, ["callee:00c3b1a8:8"]]
+ 00c42d2c ["INT_ADD", "register:40f0:8", ["const:c42d2c:8", "const:4:8"]]
+ 00c42d2c ["CALL", null, ["callee:00c3b1a8:8"]]
- 00c41d38 bytes 1fe1ff97
+ 00c42d2c bytes 1fe1ff97
- 00c41840 ["COPY", "tmp:0:8", ["const:b1c:8"]]
- 00c41840 ["INT_CARRY", "register:105:1", ["register:4070:8", "tmp:0:8"]]
- 00c41840 ["INT_SCARRY", "register:106:1", ["register:4070:8", "tmp:0:8"]]
- 00c41840 ["INT_ADD", "tmp:1:8", ["register:4070:8", "tmp:0:8"]]
+ 00c42834 ["COPY", "tmp:0:8", ["const:b5c:8"]]
+ 00c42834 ["INT_CARRY", "register:105:1", ["register:4070:8", "tmp:0:8"]]
+ 00c42834 ["INT_SCARRY", "register:106:1", ["register:4070:8", "tmp:0:8"]]
+ 00c42834 ["INT_ADD", "tmp:1:8", ["register:4070:8", "tmp:0:8"]]
- 00c41840 bytes ce712c91
+ 00c42834 bytes ce712d91
- 00c41848 ["COPY", "register:4078:8", ["const:c41858:8"]]
- 00c41848 bytes 8f000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-094b98cc3e001d981d6a9dc4ea0e97c0"></a>

### [`00c4216c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c4216c.md) → [`00c43160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43160.md) FUN_00c43160

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 3件 [`00c495f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c495f8.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 3件 [`00c4a5ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a5ec.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.49% / 新版 97.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4338c",
      "incomplete_value": false,
      "site": "00c4338c",
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
      "definition_site": "00c42398",
      "incomplete_value": false,
      "site": "00c42398",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c433b4",
      "incomplete_value": false,
      "site": "00c433b4",
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
            "const:ee5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c423c0",
      "incomplete_value": false,
      "site": "00c423c0",
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
            "const:e9b:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c43464",
      "incomplete_value": false,
      "site": "00c43464",
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
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42470",
      "incomplete_value": false,
      "site": "00c42470",
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
            "const:880:8"
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
      "00c4338c",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      "00c433b4",
      "DATA",
      [
        "storage",
        "002c0e9b",
        null,
        null
      ]
    ],
    [
      "00c43464",
      "DATA",
      [
        "storage",
        "00c98880",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4338c",
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c433b4",
      "DATA",
      [
        "storage",
        "002c0ee5",
        null,
        null
      ]
    ],
    [
      "00c43464",
      "DATA",
      [
        "storage",
        "00c99850",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c42368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c4216c.md#insn-00c42368) · [`00c42388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c4216c.md#insn-00c42388) · [`00c4238c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c4216c.md#insn-00c4238c)
- 新版 [`00c4335c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43160.md#insn-00c4335c) · [`00c4337c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43160.md#insn-00c4337c) · [`00c43380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43160.md#insn-00c43380)

~~~diff
- 00c42368 ["INT_ADD", "register:40f0:8", ["const:c42368:8", "const:4:8"]]
- 00c42368 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4335c ["INT_ADD", "register:40f0:8", ["const:c4335c:8", "const:4:8"]]
+ 00c4335c ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c42368 bytes 625f0094
+ 00c4335c bytes 595f0094
- 00c42388 ["COPY", "register:4050:8", ["const:c97000:8"]]
+ 00c4337c ["COPY", "register:4050:8", ["const:c98000:8"]]
- 00c42388 bytes aa0200b0
+ 00c4337c bytes aa0200b0
- 00c4238c ["COPY", "tmp:0:8", ["const:710:8"]]
- 00c4238c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4238c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4238c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c43380 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 00c43380 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c43380 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c43380 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4238c bytes 4a411c91
+ 00c43380 bytes 4a811b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e03a68fb21fe4072b16679bbbc14ccca"></a>

### [`00c42528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md) → [`00c4351c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c4351c.md) FUN_00c4351c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c42528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md) · 呼出先 5件 [`00c3e04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c42528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 2件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c4351c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c4351c.md) · 呼出先 5件 [`00c3f040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f040.md) [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c4351c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c4351c.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c435e4",
      "incomplete_value": false,
      "site": "00c435e4",
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
            "const:9a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c425f0",
      "incomplete_value": false,
      "site": "00c425f0",
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
            "const:9d0:8"
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
      "00c435e4",
      "DATA",
      [
        "storage",
        "00c989d0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43694",
      "DATA",
      [
        "storage",
        "00c989d0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43744",
      "DATA",
      [
        "storage",
        "00c98a40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c435e4",
      "DATA",
      [
        "storage",
        "00c999a0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43694",
      "DATA",
      [
        "storage",
        "00c999a0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43744",
      "DATA",
      [
        "storage",
        "00c99a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c42588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md#insn-00c42588) · [`00c42598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md#insn-00c42598) · [`00c425c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md#insn-00c425c0)
- 新版 [`00c4357c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c4351c.md#insn-00c4357c) · [`00c4358c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c4351c.md#insn-00c4358c) · [`00c435b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c4351c.md#insn-00c435b4)

~~~diff
- 00c42588 ["INT_ADD", "register:40f0:8", ["const:c42588:8", "const:4:8"]]
- 00c42588 ["CALL", null, ["callee:00c3f040:8"]]
+ 00c4357c ["INT_ADD", "register:40f0:8", ["const:c4357c:8", "const:4:8"]]
+ 00c4357c ["CALL", null, ["callee:00c3f040:8"]]
- 00c42588 bytes b1eeff97
+ 00c4357c bytes b1eeff97
- 00c42598 ["INT_ADD", "register:40f0:8", ["const:c42598:8", "const:4:8"]]
- 00c42598 ["CALL", null, ["local:b0:8"]]
+ 00c4358c ["INT_ADD", "register:40f0:8", ["const:c4358c:8", "const:4:8"]]
+ 00c4358c ["CALL", null, ["local:b0:8"]]
- 00c42598 bytes e4ffff97
+ 00c4358c bytes e4ffff97
- 00c425c0 ["INT_ADD", "register:40f0:8", ["const:c425c0:8", "const:4:8"]]
- 00c425c0 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c435b4 ["INT_ADD", "register:40f0:8", ["const:c435b4:8", "const:4:8"]]
+ 00c435b4 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c425c0 bytes cc5e0094
+ 00c435b4 bytes c35e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c96369bf703d108fce12add36f72f8af"></a>

### [`00c42790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42790.md) → [`00c43784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43784.md) FUN_00c43784

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c437e8",
      "incomplete_value": true,
      "site": "00c437e8",
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
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c427f4",
      "incomplete_value": true,
      "site": "00c427f4",
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
            "const:ab0:8"
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
      "00c437e8",
      "DATA",
      [
        "storage",
        "00c98ab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c437e8",
      "DATA",
      [
        "storage",
        "00c99a80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c427c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42790.md#insn-00c427c4) · [`00c427e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42790.md#insn-00c427e4) · [`00c427e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42790.md#insn-00c427e8)
- 新版 [`00c437b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43784.md#insn-00c437b8) · [`00c437d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43784.md#insn-00c437d8) · [`00c437dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43784.md#insn-00c437dc)

~~~diff
- 00c427c4 ["INT_ADD", "register:40f0:8", ["const:c427c4:8", "const:4:8"]]
- 00c427c4 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c437b8 ["INT_ADD", "register:40f0:8", ["const:c437b8:8", "const:4:8"]]
+ 00c437b8 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c427c4 bytes 4b5e0094
+ 00c437b8 bytes 425e0094
- 00c427e4 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c437d8 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c427e4 bytes a80200d0
+ 00c437d8 bytes a80200d0
- 00c427e8 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 00c427e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c427e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c427e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c437dc ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 00c437dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c437dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c437dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c427e8 bytes 08c12a91
+ 00c437dc bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a846032f04f7df54f63061aa6f741de6"></a>

### [`00c42834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42834.md) → [`00c43828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43828.md) FUN_00c43828

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 4件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 4件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.78% / 新版 97.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c43944",
      "incomplete_value": false,
      "site": "00c43944",
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
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42950",
      "incomplete_value": false,
      "site": "00c42950",
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
            "const:b20:8"
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
      "00c43944",
      "DATA",
      [
        "storage",
        "00c98b20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c43944",
      "DATA",
      [
        "storage",
        "00c99af0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c42850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42834.md#insn-00c42850) · [`00c42860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42834.md#insn-00c42860) · [`00c4291c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42834.md#insn-00c4291c)
- 新版 [`00c43844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43828.md#insn-00c43844) · [`00c43854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43828.md#insn-00c43854) · [`00c43910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43828.md#insn-00c43910)

~~~diff
- 00c42850 ["INT_ADD", "register:40f0:8", ["const:c42850:8", "const:4:8"]]
- 00c42850 ["CALL", null, ["callee:00c3bd5c:8"]]
+ 00c43844 ["INT_ADD", "register:40f0:8", ["const:c43844:8", "const:4:8"]]
+ 00c43844 ["CALL", null, ["callee:00c3bd5c:8"]]
- 00c42850 bytes 46e1ff97
+ 00c43844 bytes 46e1ff97
- 00c42860 ["INT_ADD", "register:40f0:8", ["const:c42860:8", "const:4:8"]]
- 00c42860 ["CALL", null, ["callee:00c40e0c:8"]]
+ 00c43854 ["INT_ADD", "register:40f0:8", ["const:c43854:8", "const:4:8"]]
+ 00c43854 ["CALL", null, ["callee:00c40e0c:8"]]
- 00c42860 bytes 6ef5ff97
+ 00c43854 bytes 6ef5ff97
- 00c4291c ["INT_ADD", "register:40f0:8", ["const:c4291c:8", "const:4:8"]]
- 00c4291c ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c43910 ["INT_ADD", "register:40f0:8", ["const:c43910:8", "const:4:8"]]
+ 00c43910 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4291c bytes f55d0094
+ 00c43910 bytes ec5d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06c2ff1d43de863a045062b05c20246e"></a>

### [`00c4299c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c4299c.md) → [`00c43990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43990.md) FUN_00c43990

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c439f8",
      "incomplete_value": false,
      "site": "00c439f8",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42a04",
      "incomplete_value": false,
      "site": "00c42a04",
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
            "const:110:8"
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
      "definition_site": "00c43a24",
      "incomplete_value": false,
      "site": "00c43a24",
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
            "const:f99:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42a30",
      "incomplete_value": false,
      "site": "00c42a30",
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
            "const:eca:8"
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
      "00c439f8",
      "DATA",
      [
        "storage",
        "00c98110",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43a24",
      "DATA",
      [
        "storage",
        "002b7eca",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c439f8",
      "DATA",
      [
        "storage",
        "00c990e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43a24",
      "DATA",
      [
        "storage",
        "002b7f99",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c429d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c4299c.md#insn-00c429d4) · [`00c429f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c4299c.md#insn-00c429f4) · [`00c429f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c4299c.md#insn-00c429f8)
- 新版 [`00c439c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43990.md#insn-00c439c8) · [`00c439e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43990.md#insn-00c439e8) · [`00c439ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43990.md#insn-00c439ec)

~~~diff
- 00c429d4 ["INT_ADD", "register:40f0:8", ["const:c429d4:8", "const:4:8"]]
- 00c429d4 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c439c8 ["INT_ADD", "register:40f0:8", ["const:c439c8:8", "const:4:8"]]
+ 00c439c8 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c429d4 bytes c75d0094
+ 00c439c8 bytes be5d0094
- 00c429f4 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c439e8 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c429f4 bytes a80200d0
+ 00c439e8 bytes a80200d0
- 00c429f8 ["COPY", "tmp:0:8", ["const:110:8"]]
- 00c429f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c429f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c429f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c439ec ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 00c439ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c439ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c439ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c429f8 bytes 08410491
+ 00c439ec bytes 08810391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-922862648007bde113a0d700031c6c93"></a>

### [`00c42a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42a5c.md) → [`00c43a50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43a50.md) FUN_00c43a50

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 9件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3ce7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 9件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c3de70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md) [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.38% / 新版 98.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c43ee0",
      "incomplete_value": false,
      "site": "00c43ee0",
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
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42eec",
      "incomplete_value": false,
      "site": "00c42eec",
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
            "const:ce0:8"
          ]
        ]
      ]
    },
    "ordinal": 60,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c43d3c",
      "DATA",
      [
        "storage",
        "00c98b90",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43dd0",
      "DATA",
      [
        "storage",
        "00c98c00",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43dd0",
      "DATA",
      [
        "storage",
        "00c98c70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c43d3c",
      "DATA",
      [
        "storage",
        "00c99b60",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43dd0",
      "DATA",
      [
        "storage",
        "00c99bd0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c43dd0",
      "DATA",
      [
        "storage",
        "00c99c40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c42af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42a5c.md#insn-00c42af8) · [`00c42b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42a5c.md#insn-00c42b40) · [`00c42b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42a5c.md#insn-00c42b70)
- 新版 [`00c43aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43a50.md#insn-00c43aec) · [`00c43b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43a50.md#insn-00c43b34) · [`00c43b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43a50.md#insn-00c43b64)

~~~diff
- 00c42af8 ["INT_ADD", "register:40f0:8", ["const:c42af8:8", "const:4:8"]]
- 00c42af8 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c43aec ["INT_ADD", "register:40f0:8", ["const:c43aec:8", "const:4:8"]]
+ 00c43aec ["CALL", null, ["callee:00c5b140:8"]]
- 00c42af8 bytes 9e5d0094
+ 00c43aec bytes 955d0094
- 00c42b40 ["INT_ADD", "register:40f0:8", ["const:c42b40:8", "const:4:8"]]
- 00c42b40 ["CALL", null, ["callee:00c3bd5c:8"]]
+ 00c43b34 ["INT_ADD", "register:40f0:8", ["const:c43b34:8", "const:4:8"]]
+ 00c43b34 ["CALL", null, ["callee:00c3bd5c:8"]]
- 00c42b40 bytes 8ae0ff97
+ 00c43b34 bytes 8ae0ff97
- 00c42b70 ["INT_ADD", "register:40f0:8", ["const:c42b70:8", "const:4:8"]]
- 00c42b70 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c43b64 ["INT_ADD", "register:40f0:8", ["const:c43b64:8", "const:4:8"]]
+ 00c43b64 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c42b70 bytes 605d0094
+ 00c43b64 bytes 575d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30e72f57798c494888212927d810bcff"></a>

### [`00c42f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42f2c.md) → [`00c43f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43f20.md) FUN_00c43f20

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 8件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3ce7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 8件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3de70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md) [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c44204",
      "incomplete_value": true,
      "site": "00c44204",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43210",
      "incomplete_value": true,
      "site": "00c43210",
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
            "const:d50:8"
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
      "00c4402c",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      "00c44204",
      "DATA",
      [
        "storage",
        "00c98d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4402c",
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c44204",
      "DATA",
      [
        "storage",
        "00c99d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c42f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42f2c.md#insn-00c42f54) · [`00c42f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42f2c.md#insn-00c42f64) · [`00c42ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42f2c.md#insn-00c42ff8)
- 新版 [`00c43f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43f20.md#insn-00c43f48) · [`00c43f58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43f20.md#insn-00c43f58) · [`00c43fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43f20.md#insn-00c43fec)

~~~diff
- 00c42f54 ["INT_ADD", "register:40f0:8", ["const:c42f54:8", "const:4:8"]]
- 00c42f54 ["CALL", null, ["callee:00c3bd5c:8"]]
+ 00c43f48 ["INT_ADD", "register:40f0:8", ["const:c43f48:8", "const:4:8"]]
+ 00c43f48 ["CALL", null, ["callee:00c3bd5c:8"]]
- 00c42f54 bytes 85dfff97
+ 00c43f48 bytes 85dfff97
- 00c42f64 ["INT_ADD", "register:40f0:8", ["const:c42f64:8", "const:4:8"]]
- 00c42f64 ["CALL", null, ["callee:00c40e0c:8"]]
+ 00c43f58 ["INT_ADD", "register:40f0:8", ["const:c43f58:8", "const:4:8"]]
+ 00c43f58 ["CALL", null, ["callee:00c40e0c:8"]]
- 00c42f64 bytes adf3ff97
+ 00c43f58 bytes adf3ff97
- 00c42ff8 ["COPY", "register:40e0:8", ["const:c97000:8"]]
+ 00c43fec ["COPY", "register:40e0:8", ["const:c98000:8"]]
- 00c42ff8 bytes bc0200b0
+ 00c43fec bytes bc0200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7c5c8eda3ebcc696992a5fb2441940b"></a>

### [`00c43474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43474.md) → [`00c44468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44468.md) FUN_00c44468

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c444cc",
      "incomplete_value": false,
      "site": "00c444cc",
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
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c434d8",
      "incomplete_value": false,
      "site": "00c434d8",
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
            "const:e30:8"
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
      "00c444cc",
      "DATA",
      [
        "storage",
        "00c98e30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c444cc",
      "DATA",
      [
        "storage",
        "00c99e00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c434a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43474.md#insn-00c434a8) · [`00c434c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43474.md#insn-00c434c8) · [`00c434cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43474.md#insn-00c434cc)
- 新版 [`00c4449c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44468.md#insn-00c4449c) · [`00c444bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44468.md#insn-00c444bc) · [`00c444c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44468.md#insn-00c444c0)

~~~diff
- 00c434a8 ["INT_ADD", "register:40f0:8", ["const:c434a8:8", "const:4:8"]]
- 00c434a8 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4449c ["INT_ADD", "register:40f0:8", ["const:c4449c:8", "const:4:8"]]
+ 00c4449c ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c434a8 bytes 125b0094
+ 00c4449c bytes 095b0094
- 00c434c8 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c444bc ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c434c8 bytes a80200b0
+ 00c444bc bytes a80200b0
- 00c434cc ["COPY", "tmp:0:8", ["const:e30:8"]]
- 00c434cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c434cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c434cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c444c0 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 00c444c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c444c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c444c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c434cc bytes 08c13891
+ 00c444c0 bytes 08013891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82f218d8ca4dd3b45e3bad6fa35a988b"></a>

### [`00c43510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43510.md) → [`00c44504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44504.md) FUN_00c44504

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c4456c",
      "incomplete_value": false,
      "site": "00c4456c",
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
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43578",
      "incomplete_value": false,
      "site": "00c43578",
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
            "const:ab0:8"
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
      "00c4456c",
      "DATA",
      [
        "storage",
        "00c98ab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4456c",
      "DATA",
      [
        "storage",
        "00c99a80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c43548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43510.md#insn-00c43548) · [`00c43568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43510.md#insn-00c43568) · [`00c4356c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43510.md#insn-00c4356c)
- 新版 [`00c4453c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44504.md#insn-00c4453c) · [`00c4455c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44504.md#insn-00c4455c) · [`00c44560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44504.md#insn-00c44560)

~~~diff
- 00c43548 ["INT_ADD", "register:40f0:8", ["const:c43548:8", "const:4:8"]]
- 00c43548 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4453c ["INT_ADD", "register:40f0:8", ["const:c4453c:8", "const:4:8"]]
+ 00c4453c ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c43548 bytes ea5a0094
+ 00c4453c bytes e15a0094
- 00c43568 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c4455c ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c43568 bytes a80200b0
+ 00c4455c bytes a80200b0
- 00c4356c ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 00c4356c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4356c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4356c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c44560 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 00c44560 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c44560 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c44560 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4356c bytes 08c12a91
+ 00c44560 bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7aa5080cd51d410ebecf2b919ccfe17f"></a>

### [`00c43668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43668.md) → [`00c4465c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c4465c.md) FUN_00c4465c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c446c0",
      "incomplete_value": true,
      "site": "00c446c0",
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
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c436cc",
      "incomplete_value": true,
      "site": "00c436cc",
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
      "00c446c0",
      "DATA",
      [
        "storage",
        "00c98ea0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c446c0",
      "DATA",
      [
        "storage",
        "00c99e70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4369c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43668.md#insn-00c4369c) · [`00c436bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43668.md#insn-00c436bc) · [`00c436c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43668.md#insn-00c436c0)
- 新版 [`00c44690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c4465c.md#insn-00c44690) · [`00c446b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c4465c.md#insn-00c446b0) · [`00c446b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c4465c.md#insn-00c446b4)

~~~diff
- 00c4369c ["INT_ADD", "register:40f0:8", ["const:c4369c:8", "const:4:8"]]
- 00c4369c ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c44690 ["INT_ADD", "register:40f0:8", ["const:c44690:8", "const:4:8"]]
+ 00c44690 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4369c bytes 955a0094
+ 00c44690 bytes 8c5a0094
- 00c436bc ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c446b0 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c436bc bytes a80200b0
+ 00c446b0 bytes a80200b0
- 00c436c0 ["COPY", "tmp:0:8", ["const:ea0:8"]]
- 00c436c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c436c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c436c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c446b4 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 00c446b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c446b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c446b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c436c0 bytes 08813a91
+ 00c446b4 bytes 08c13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0d1a5687ec16f317122c74e863a9ef4"></a>

### [`00c43708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) → [`00c446fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c446fc.md) FUN_00c446fc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 7件 [`00c3e04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c3e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c3eb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3eb30.md) [`00c4b6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) [`00c4b848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 7件 [`00c3f040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f040.md) [`00c3f654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f654.md) [`00c3fb24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3fb24.md) [`00c4c6b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c6b8.md) [`00c4c83c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c83c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.34% / 新版 97.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c447d0",
      "incomplete_value": false,
      "site": "00c447d0",
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
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c437dc",
      "incomplete_value": false,
      "site": "00c437dc",
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
            "const:d0:8"
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
      "definition_site": "00c44ad0",
      "incomplete_value": false,
      "site": "00c44ad0",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43adc",
      "incomplete_value": false,
      "site": "00c43adc",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c44ba0",
      "incomplete_value": false,
      "site": "00c44ba0",
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
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43bac",
      "incomplete_value": false,
      "site": "00c43bac",
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
            "const:d0:8"
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
      "00c447d0",
      "DATA",
      [
        "storage",
        "00c990d0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c44904",
      "DATA",
      [
        "storage",
        "00c99610",
        null,
        "undefined *"
      ]
    ],
    [
      "00c44948",
      "DATA",
      [
        "storage",
        "00c98f10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c447d0",
      "DATA",
      [
        "storage",
        "00c9a0a0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c44904",
      "DATA",
      [
        "storage",
        "00c9a5e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c44948",
      "DATA",
      [
        "storage",
        "00c99ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c43780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md#insn-00c43780) · [`00c437a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md#insn-00c437a8) · [`00c437cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md#insn-00c437cc)
- 新版 [`00c44774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c446fc.md#insn-00c44774) · [`00c4479c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c446fc.md#insn-00c4479c) · [`00c447c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c446fc.md#insn-00c447c0)

~~~diff
- 00c43780 ["INT_ADD", "register:40f0:8", ["const:c43780:8", "const:4:8"]]
- 00c43780 ["CALL", null, ["callee:00c4c83c:8"]]
+ 00c44774 ["INT_ADD", "register:40f0:8", ["const:c44774:8", "const:4:8"]]
+ 00c44774 ["CALL", null, ["callee:00c4c83c:8"]]
- 00c43780 bytes 32200094
+ 00c44774 bytes 32200094
- 00c437a8 ["INT_ADD", "register:40f0:8", ["const:c437a8:8", "const:4:8"]]
- 00c437a8 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4479c ["INT_ADD", "register:40f0:8", ["const:c4479c:8", "const:4:8"]]
+ 00c4479c ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c437a8 bytes 525a0094
+ 00c4479c bytes 495a0094
- 00c437cc ["COPY", "register:4050:8", ["const:c99000:8"]]
+ 00c447c0 ["COPY", "register:4050:8", ["const:c9a000:8"]]
- 00c437cc bytes aa0200d0
+ 00c447c0 bytes aa0200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea493fa82fa428cbd94fe43c3a95a28c"></a>

### [`00c43d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43d7c.md) → [`00c44d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44d70.md) FUN_00c44d70

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c44de4",
      "incomplete_value": false,
      "site": "00c44de4",
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
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43df0",
      "incomplete_value": false,
      "site": "00c43df0",
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
            "const:c40:8"
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
      "00c44de4",
      "DATA",
      [
        "storage",
        "00c97c40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c44de4",
      "DATA",
      [
        "storage",
        "00c98c10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c43dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43d7c.md#insn-00c43dc0) · [`00c43de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43d7c.md#insn-00c43de0) · [`00c43de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43d7c.md#insn-00c43de4)
- 新版 [`00c44db4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44d70.md#insn-00c44db4) · [`00c44dd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44d70.md#insn-00c44dd4) · [`00c44dd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44d70.md#insn-00c44dd8)

~~~diff
- 00c43dc0 ["INT_ADD", "register:40f0:8", ["const:c43dc0:8", "const:4:8"]]
- 00c43dc0 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c44db4 ["INT_ADD", "register:40f0:8", ["const:c44db4:8", "const:4:8"]]
+ 00c44db4 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c43dc0 bytes cc580094
+ 00c44db4 bytes c3580094
- 00c43de0 ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c44dd4 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c43de0 bytes a8020090
+ 00c44dd4 bytes a8020090
- 00c43de4 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 00c43de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c43de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c43de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c44dd8 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 00c44dd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c44dd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c44dd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c43de4 bytes 08013191
+ 00c44dd8 bytes 08413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-217ea61c6db4badb1e114c338fa06a46"></a>

### [`00c4435c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c4435c.md) → [`00c45350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c45350.md) FUN_00c45350

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c453c0",
      "incomplete_value": false,
      "site": "00c453c0",
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
            "const:c80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c443cc",
      "incomplete_value": false,
      "site": "00c443cc",
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
            "const:cb0:8"
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
      "00c453c0",
      "DATA",
      [
        "storage",
        "00c97cb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c453c0",
      "DATA",
      [
        "storage",
        "00c98c80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4439c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c4435c.md#insn-00c4439c) · [`00c443bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c4435c.md#insn-00c443bc) · [`00c443c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c4435c.md#insn-00c443c0)
- 新版 [`00c45390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c45350.md#insn-00c45390) · [`00c453b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c45350.md#insn-00c453b0) · [`00c453b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c45350.md#insn-00c453b4)

~~~diff
- 00c4439c ["INT_ADD", "register:40f0:8", ["const:c4439c:8", "const:4:8"]]
- 00c4439c ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c45390 ["INT_ADD", "register:40f0:8", ["const:c45390:8", "const:4:8"]]
+ 00c45390 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4439c bytes 55570094
+ 00c45390 bytes 4c570094
- 00c443bc ["COPY", "register:4040:8", ["const:c97000:8"]]
+ 00c453b0 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c443bc bytes 880200f0
+ 00c453b0 bytes 880200f0
- 00c443c0 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 00c443c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c443c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c443c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c453b4 ["COPY", "tmp:0:8", ["const:c80:8"]]
+ 00c453b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c453b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c453b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c443c0 bytes 08c13291
+ 00c453b4 bytes 08013291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-568f0f84f91272f7593d5cc0ed29a0f2"></a>

### [`00c462d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c462d4.md) → [`00c472c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c472c8.md) FUN_00c472c8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 3件 [`00c3ac28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ac28.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c427e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md) · 呼出先 3件 [`00c3bc1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bc1c.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c47370",
      "incomplete_value": false,
      "site": "00c47370",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4637c",
      "incomplete_value": false,
      "site": "00c4637c",
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
            "const:180:8"
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
      "00c47370",
      "DATA",
      [
        "storage",
        "00c98180",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c47370",
      "DATA",
      [
        "storage",
        "00c99150",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c462fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c462d4.md#insn-00c462fc) · [`00c46344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c462d4.md#insn-00c46344) · [`00c46374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c462d4.md#insn-00c46374)
- 新版 [`00c472f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c472c8.md#insn-00c472f0) · [`00c47338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c472c8.md#insn-00c47338) · [`00c47368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c472c8.md#insn-00c47368)

~~~diff
- 00c462fc ["INT_ADD", "register:40f0:8", ["const:c462fc:8", "const:4:8"]]
- 00c462fc ["CALL", null, ["callee:00c3bc1c:8"]]
+ 00c472f0 ["INT_ADD", "register:40f0:8", ["const:c472f0:8", "const:4:8"]]
+ 00c472f0 ["CALL", null, ["callee:00c3bc1c:8"]]
- 00c462fc bytes 4bd2ff97
+ 00c472f0 bytes 4bd2ff97
- 00c46344 ["INT_ADD", "register:40f0:8", ["const:c46344:8", "const:4:8"]]
- 00c46344 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c47338 ["INT_ADD", "register:40f0:8", ["const:c47338:8", "const:4:8"]]
+ 00c47338 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c46344 bytes 6b4f0094
+ 00c47338 bytes 624f0094
- 00c46374 ["COPY", "register:4048:8", ["const:c98000:8"]]
+ 00c47368 ["COPY", "register:4048:8", ["const:c99000:8"]]
- 00c46374 bytes 890200d0
+ 00c47368 bytes 890200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9a6d80742b9544f30ceb3dd1b4abeeb"></a>

### [`00c463c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c463c8.md) → [`00c473bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c473bc.md) FUN_00c473bc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c427e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c4742c",
      "incomplete_value": false,
      "site": "00c47438",
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
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46438",
      "incomplete_value": false,
      "site": "00c46444",
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
            "const:1f0:8"
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
      "00c47438",
      "DATA",
      [
        "storage",
        "00c981f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c47438",
      "DATA",
      [
        "storage",
        "00c991c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c463fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c463c8.md#insn-00c463fc) · [`00c46434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c463c8.md#insn-00c46434) · [`00c46438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c463c8.md#insn-00c46438)
- 新版 [`00c473f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c473bc.md#insn-00c473f0) · [`00c47428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c473bc.md#insn-00c47428) · [`00c4742c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c473bc.md#insn-00c4742c)

~~~diff
- 00c463fc ["INT_ADD", "register:40f0:8", ["const:c463fc:8", "const:4:8"]]
- 00c463fc ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c473f0 ["INT_ADD", "register:40f0:8", ["const:c473f0:8", "const:4:8"]]
+ 00c473f0 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c463fc bytes 3d4f0094
+ 00c473f0 bytes 344f0094
- 00c46434 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c47428 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c46434 bytes 880200d0
+ 00c47428 bytes 880200d0
- 00c46438 ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 00c46438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c46438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c46438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4742c ["COPY", "tmp:0:8", ["const:1c0:8"]]
+ 00c4742c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4742c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4742c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c46438 bytes 08c10791
+ 00c4742c bytes 08010791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d99511bb1f750e803d75acf70e4fe7d3"></a>

### [`00c46470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46470.md) → [`00c47464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47464.md) FUN_00c47464

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c427e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c474c8",
      "incomplete_value": false,
      "site": "00c474c8",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c464d4",
      "incomplete_value": false,
      "site": "00c464d4",
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
            "const:3b0:8"
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
      "00c474c8",
      "DATA",
      [
        "storage",
        "00c983b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c474c8",
      "DATA",
      [
        "storage",
        "00c99380",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c464a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46470.md#insn-00c464a4) · [`00c464c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46470.md#insn-00c464c4) · [`00c464c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46470.md#insn-00c464c8)
- 新版 [`00c47498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47464.md#insn-00c47498) · [`00c474b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47464.md#insn-00c474b8) · [`00c474bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47464.md#insn-00c474bc)

~~~diff
- 00c464a4 ["INT_ADD", "register:40f0:8", ["const:c464a4:8", "const:4:8"]]
- 00c464a4 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c47498 ["INT_ADD", "register:40f0:8", ["const:c47498:8", "const:4:8"]]
+ 00c47498 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c464a4 bytes 134f0094
+ 00c47498 bytes 0a4f0094
- 00c464c4 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c474b8 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c464c4 bytes 880200d0
+ 00c474b8 bytes 880200d0
- 00c464c8 ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 00c464c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c464c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c464c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c474bc ["COPY", "tmp:0:8", ["const:380:8"]]
+ 00c474bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c474bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c474bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c464c8 bytes 08c10e91
+ 00c474bc bytes 08010e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-250aca8bf48fa43a8359b3634136ede1"></a>

### [`00c46510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46510.md) → [`00c47504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47504.md) FUN_00c47504

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 3件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 2件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c427e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md) · 呼出先 3件 [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c47570",
      "incomplete_value": false,
      "site": "00c47570",
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
      "definition_site": "00c4657c",
      "incomplete_value": false,
      "site": "00c4657c",
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
      "00c47570",
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
      "00c47570",
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

- 旧版 [`00c46544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46510.md#insn-00c46544) · [`00c4656c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46510.md#insn-00c4656c) · [`00c46570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46510.md#insn-00c46570)
- 新版 [`00c47538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47504.md#insn-00c47538) · [`00c47560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47504.md#insn-00c47560) · [`00c47564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47504.md#insn-00c47564)

~~~diff
- 00c46544 ["INT_ADD", "register:40f0:8", ["const:c46544:8", "const:4:8"]]
- 00c46544 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c47538 ["INT_ADD", "register:40f0:8", ["const:c47538:8", "const:4:8"]]
+ 00c47538 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c46544 bytes eb4e0094
+ 00c47538 bytes e24e0094
- 00c4656c ["INT_ADD", "register:40f0:8", ["const:c4656c:8", "const:4:8"]]
- 00c4656c ["CALL", null, ["callee:00c59080:8"]]
+ 00c47560 ["INT_ADD", "register:40f0:8", ["const:c47560:8", "const:4:8"]]
+ 00c47560 ["CALL", null, ["callee:00c59080:8"]]
- 00c4656c bytes d1460094
+ 00c47560 bytes c8460094
- 00c46570 ["COPY", "register:4048:8", ["const:c97000:8"]]
+ 00c47564 ["COPY", "register:4048:8", ["const:c98000:8"]]
- 00c46570 bytes 890200b0
+ 00c47564 bytes 890200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6747a7a8ae3755dbf3e02aa39fb1dd89"></a>

### [`00c465bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md) → [`00c475b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c475b0.md) FUN_00c475b0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3f3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 14件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3ce7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c478d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md)
- 新版 呼出元 2件 [`00c403a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c403a0.md) [`00c427e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md) · 呼出先 14件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3de70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md) [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c488c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c488c4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.20% / 新版 97.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c476d0",
      "incomplete_value": false,
      "site": "00c476d0",
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
      "definition_site": "00c466dc",
      "incomplete_value": false,
      "site": "00c466dc",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c476f8",
      "incomplete_value": false,
      "site": "00c476f8",
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
            "const:e03:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46704",
      "incomplete_value": false,
      "site": "00c46704",
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
            "const:d34:8"
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
      "definition_site": "00c47884",
      "incomplete_value": false,
      "site": "00c47884",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46890",
      "incomplete_value": false,
      "site": "00c46890",
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
            "const:420:8"
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
      "00c476d0",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      "00c476f8",
      "DATA",
      [
        "storage",
        "002b8d34",
        null,
        "string"
      ]
    ],
    [
      "00c47884",
      "DATA",
      [
        "storage",
        "00c98420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c476d0",
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c476f8",
      "DATA",
      [
        "storage",
        "002b8e03",
        null,
        "string"
      ]
    ],
    [
      "00c47884",
      "DATA",
      [
        "storage",
        "00c993f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c46cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md#insn-00c46cd0) · [`00c46cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md#insn-00c46cf4) · [`00c466ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md#insn-00c466ac)
- 新版 [`00c47cc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c475b0.md#insn-00c47cc4) · [`00c47ce8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c475b0.md#insn-00c47ce8) · [`00c476a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c475b0.md#insn-00c476a0)

~~~diff
- 00c46cd0 ["INT_ADD", "register:40f0:8", ["const:c46cd0:8", "const:4:8"]]
- 00c46cd0 ["CALL", null, ["callee:00c3909c:8"]]
+ 00c47cc4 ["INT_ADD", "register:40f0:8", ["const:c47cc4:8", "const:4:8"]]
+ 00c47cc4 ["CALL", null, ["callee:00c3909c:8"]]
- 00c46cd0 bytes f6c4ff97
+ 00c47cc4 bytes f6c4ff97
- 00c46cf4 ["INT_ADD", "register:40f0:8", ["const:c46cf4:8", "const:4:8"]]
- 00c46cf4 ["CALL", null, ["callee:00c3909c:8"]]
+ 00c47ce8 ["INT_ADD", "register:40f0:8", ["const:c47ce8:8", "const:4:8"]]
+ 00c47ce8 ["CALL", null, ["callee:00c3909c:8"]]
- 00c46cf4 bytes edc4ff97
+ 00c47ce8 bytes edc4ff97
- 00c466ac ["INT_ADD", "register:40f0:8", ["const:c466ac:8", "const:4:8"]]
- 00c466ac ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c476a0 ["INT_ADD", "register:40f0:8", ["const:c476a0:8", "const:4:8"]]
+ 00c476a0 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c466ac bytes 914e0094
+ 00c476a0 bytes 884e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dbbd5b2424cf9b0365693d67c0f2ce1"></a>

### [`00c46d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46d3c.md) → [`00c47d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47d30.md) FUN_00c47d30

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c427e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c47d94",
      "incomplete_value": false,
      "site": "00c47d94",
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
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46da0",
      "incomplete_value": false,
      "site": "00c46da0",
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
            "const:7a0:8"
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
      "00c47d94",
      "DATA",
      [
        "storage",
        "00c987a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c47d94",
      "DATA",
      [
        "storage",
        "00c99770",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c46d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46d3c.md#insn-00c46d70) · [`00c46d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46d3c.md#insn-00c46d90) · [`00c46d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46d3c.md#insn-00c46d94)
- 新版 [`00c47d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47d30.md#insn-00c47d64) · [`00c47d84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47d30.md#insn-00c47d84) · [`00c47d88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47d30.md#insn-00c47d88)

~~~diff
- 00c46d70 ["INT_ADD", "register:40f0:8", ["const:c46d70:8", "const:4:8"]]
- 00c46d70 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c47d64 ["INT_ADD", "register:40f0:8", ["const:c47d64:8", "const:4:8"]]
+ 00c47d64 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c46d70 bytes e04c0094
+ 00c47d64 bytes d74c0094
- 00c46d90 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c47d84 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c46d90 bytes 880200d0
+ 00c47d84 bytes 880200d0
- 00c46d94 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 00c46d94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c46d94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c46d94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c47d88 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 00c47d88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c47d88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c47d88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c46d94 bytes 08811e91
+ 00c47d88 bytes 08c11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b887d060cc292bf120c0761a8c423e03"></a>

### [`00c46ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46ddc.md) → [`00c47dd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47dd0.md) FUN_00c47dd0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c417ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c427e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c47e38",
      "incomplete_value": false,
      "site": "00c47e38",
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
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46e44",
      "incomplete_value": false,
      "site": "00c46e44",
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
            "const:810:8"
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
      "00c47e38",
      "DATA",
      [
        "storage",
        "00c98810",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c47e38",
      "DATA",
      [
        "storage",
        "00c997e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c46e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46ddc.md#insn-00c46e14) · [`00c46e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46ddc.md#insn-00c46e34) · [`00c46e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46ddc.md#insn-00c46e38)
- 新版 [`00c47e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47dd0.md#insn-00c47e08) · [`00c47e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47dd0.md#insn-00c47e28) · [`00c47e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47dd0.md#insn-00c47e2c)

~~~diff
- 00c46e14 ["INT_ADD", "register:40f0:8", ["const:c46e14:8", "const:4:8"]]
- 00c46e14 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c47e08 ["INT_ADD", "register:40f0:8", ["const:c47e08:8", "const:4:8"]]
+ 00c47e08 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c46e14 bytes b74c0094
+ 00c47e08 bytes ae4c0094
- 00c46e34 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c47e28 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c46e34 bytes 880200d0
+ 00c47e28 bytes 880200d0
- 00c46e38 ["COPY", "tmp:0:8", ["const:810:8"]]
- 00c46e38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c46e38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c46e38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c47e2c ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 00c47e2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c47e2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c47e2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c46e38 bytes 08412091
+ 00c47e2c bytes 08811f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5337ca5c996262a46f193d70c489ef38"></a>

### [`00c4722c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c4722c.md) → [`00c48220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c48220.md) FUN_00c48220

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5e1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5f1a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f1a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.08% / 新版 99.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c48344",
      "incomplete_value": false,
      "site": "00c4835c",
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
            "const:dfb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47350",
      "incomplete_value": false,
      "site": "00c47368",
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
            "const:d2c:8"
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
      "00c48344",
      "PARAM",
      [
        "storage",
        "002b8d2c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c48344",
      "PARAM",
      [
        "storage",
        "002b8dfb",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c47368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c4722c.md#insn-00c47368) · [`00c47350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c4722c.md#insn-00c47350) · [`00c4739c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c4722c.md#insn-00c4739c)
- 新版 [`00c4835c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c48220.md#insn-00c4835c) · [`00c48344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c48220.md#insn-00c48344) · [`00c48390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c48220.md#insn-00c48390)

~~~diff
- 00c47368 ["INT_ADD", "register:40f0:8", ["const:c47368:8", "const:4:8"]]
- 00c47368 ["CALL", null, ["callee:00c5f1a0:8"]]
+ 00c4835c ["INT_ADD", "register:40f0:8", ["const:c4835c:8", "const:4:8"]]
+ 00c4835c ["CALL", null, ["callee:00c5f1a0:8"]]
- 00c47368 bytes 9a5b0094
+ 00c4835c bytes 915b0094
- 00c47350 ["COPY", "tmp:0:8", ["const:d2c:8"]]
- 00c47350 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00c47350 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00c47350 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00c48344 ["COPY", "tmp:0:8", ["const:dfb:8"]]
+ 00c48344 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00c48344 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00c48344 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00c47350 bytes 42b03491
+ 00c48344 bytes 42ec3791
- 00c4739c ["INT_ADD", "register:40f0:8", ["const:c4739c:8", "const:4:8"]]
- 00c4739c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c48390 ["INT_ADD", "register:40f0:8", ["const:c48390:8", "const:4:8"]]
+ 00c48390 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4739c bytes 754b0094
+ 00c48390 bytes 6c4b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ba1ccb8442f94227f3a4cbb7fe8e6d2"></a>

### [`00c473e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c473e8.md) → [`00c483dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c483dc.md) FUN_00c483dc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5e1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5f1a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f1a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.12% / 新版 99.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c48518",
      "incomplete_value": false,
      "site": "00c48528",
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
            "const:58e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47524",
      "incomplete_value": false,
      "site": "00c47534",
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
            "const:4c1:8"
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
      "00c48518",
      "PARAM",
      [
        "storage",
        "002ac4c1",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c48518",
      "PARAM",
      [
        "storage",
        "002ac58e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c47534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c473e8.md#insn-00c47534) · [`00c47524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c473e8.md#insn-00c47524) · [`00c47568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c473e8.md#insn-00c47568)
- 新版 [`00c48528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c483dc.md#insn-00c48528) · [`00c48518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c483dc.md#insn-00c48518) · [`00c4855c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c483dc.md#insn-00c4855c)

~~~diff
- 00c47534 ["INT_ADD", "register:40f0:8", ["const:c47534:8", "const:4:8"]]
- 00c47534 ["CALL", null, ["callee:00c5f1a0:8"]]
+ 00c48528 ["INT_ADD", "register:40f0:8", ["const:c48528:8", "const:4:8"]]
+ 00c48528 ["CALL", null, ["callee:00c5f1a0:8"]]
- 00c47534 bytes 275b0094
+ 00c48528 bytes 1e5b0094
- 00c47524 ["COPY", "tmp:0:8", ["const:4c1:8"]]
- 00c47524 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00c47524 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00c47524 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00c48518 ["COPY", "tmp:0:8", ["const:58e:8"]]
+ 00c48518 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00c48518 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00c48518 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00c47524 bytes 42041391
+ 00c48518 bytes 42381691
- 00c47568 ["INT_ADD", "register:40f0:8", ["const:c47568:8", "const:4:8"]]
- 00c47568 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4855c ["INT_ADD", "register:40f0:8", ["const:c4855c:8", "const:4:8"]]
+ 00c4855c ["CALL", null, ["callee:00c5b140:8"]]
- 00c47568 bytes 024b0094
+ 00c4855c bytes f94a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f671988032619881deb92c8127779632"></a>

### [`00c475b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c475b4.md) → [`00c485a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c485a8.md) FUN_00c485a8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5e1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5f1a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f1a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.22% / 新版 99.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c4871c",
      "incomplete_value": false,
      "site": "00c48730",
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
            "const:ed8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47728",
      "incomplete_value": false,
      "site": "00c4773c",
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
            "const:dfa:8"
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
      "00c4871c",
      "PARAM",
      [
        "storage",
        "002b9dfa",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c4871c",
      "PARAM",
      [
        "storage",
        "002b9ed8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4773c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c475b4.md#insn-00c4773c) · [`00c47728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c475b4.md#insn-00c47728) · [`00c47770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c475b4.md#insn-00c47770)
- 新版 [`00c48730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c485a8.md#insn-00c48730) · [`00c4871c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c485a8.md#insn-00c4871c) · [`00c48764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c485a8.md#insn-00c48764)

~~~diff
- 00c4773c ["INT_ADD", "register:40f0:8", ["const:c4773c:8", "const:4:8"]]
- 00c4773c ["CALL", null, ["callee:00c5f1a0:8"]]
+ 00c48730 ["INT_ADD", "register:40f0:8", ["const:c48730:8", "const:4:8"]]
+ 00c48730 ["CALL", null, ["callee:00c5f1a0:8"]]
- 00c4773c bytes a55a0094
+ 00c48730 bytes 9c5a0094
- 00c47728 ["COPY", "tmp:0:8", ["const:dfa:8"]]
- 00c47728 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00c47728 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00c47728 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00c4871c ["COPY", "tmp:0:8", ["const:ed8:8"]]
+ 00c4871c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00c4871c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00c4871c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00c47728 bytes 42e83791
+ 00c4871c bytes 42603b91
- 00c47770 ["INT_ADD", "register:40f0:8", ["const:c47770:8", "const:4:8"]]
- 00c47770 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c48764 ["INT_ADD", "register:40f0:8", ["const:c48764:8", "const:4:8"]]
+ 00c48764 ["CALL", null, ["callee:00c5b140:8"]]
- 00c47770 bytes 804a0094
+ 00c48764 bytes 774a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32e9b9a8ca068da57f10f2359b428128"></a>

### [`00c478d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md) → [`00c488c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c488c4.md) FUN_00c488c4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00c3c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c465bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md) [`00c478d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md) · 呼出先 14件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3ce7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md)
- 新版 呼出元 3件 [`00c3d9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md) [`00c475b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c475b0.md) [`00c488c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c488c4.md) · 呼出先 14件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d29c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c3de70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md) [`00c40e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.80% / 新版 96.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c489e0",
      "incomplete_value": false,
      "site": "00c489e0",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c479ec",
      "incomplete_value": false,
      "site": "00c479ec",
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
            "const:490:8"
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
      "definition_site": "00c48ab8",
      "incomplete_value": false,
      "site": "00c48ab8",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47ac4",
      "incomplete_value": false,
      "site": "00c47ac4",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c48b78",
      "incomplete_value": false,
      "site": "00c48b78",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47b84",
      "incomplete_value": false,
      "site": "00c47b84",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c489e0",
      "DATA",
      [
        "storage",
        "00c98490",
        null,
        "undefined *"
      ]
    ],
    [
      "00c48ab8",
      "DATA",
      [
        "storage",
        "00c98490",
        null,
        "undefined *"
      ]
    ],
    [
      "00c48b78",
      "DATA",
      [
        "storage",
        "00c98490",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c489e0",
      "DATA",
      [
        "storage",
        "00c99460",
        null,
        "undefined *"
      ]
    ],
    [
      "00c48ab8",
      "DATA",
      [
        "storage",
        "00c99460",
        null,
        "undefined *"
      ]
    ],
    [
      "00c48b78",
      "DATA",
      [
        "storage",
        "00c99460",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c481fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md#insn-00c481fc) · [`00c4796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md#insn-00c4796c) · [`00c47980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md#insn-00c47980)
- 新版 [`00c491f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c488c4.md#insn-00c491f0) · [`00c48960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c488c4.md#insn-00c48960) · [`00c48974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c488c4.md#insn-00c48974)

~~~diff
- 00c481fc ["INT_ADD", "register:40f0:8", ["const:c481fc:8", "const:4:8"]]
- 00c481fc ["CALL", null, ["callee:00c3909c:8"]]
+ 00c491f0 ["INT_ADD", "register:40f0:8", ["const:c491f0:8", "const:4:8"]]
+ 00c491f0 ["CALL", null, ["callee:00c3909c:8"]]
- 00c481fc bytes abbfff97
+ 00c491f0 bytes abbfff97
- 00c4796c ["INT_ADD", "register:40f0:8", ["const:c4796c:8", "const:4:8"]]
- 00c4796c ["CALL", null, ["local:b0:8"]]
+ 00c48960 ["INT_ADD", "register:40f0:8", ["const:c48960:8", "const:4:8"]]
+ 00c48960 ["CALL", null, ["local:b0:8"]]
- 00c4796c bytes d9ffff97
+ 00c48960 bytes d9ffff97
- 00c47980 ["INT_ADD", "register:40f0:8", ["const:c47980:8", "const:4:8"]]
- 00c47980 ["CALL", null, ["callee:00c494dc:8"]]
+ 00c48974 ["INT_ADD", "register:40f0:8", ["const:c48974:8", "const:4:8"]]
+ 00c48974 ["CALL", null, ["callee:00c494dc:8"]]
- 00c47980 bytes da020094
+ 00c48974 bytes da020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fcade6ab81e612390b4144a1fb3b995"></a>

### [`00c4823c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c4823c.md) → [`00c49230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49230.md) FUN_00c49230

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c465bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c475b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c475b0.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c492ac",
      "incomplete_value": false,
      "site": "00c492ac",
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
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c482b8",
      "incomplete_value": false,
      "site": "00c482b8",
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
            "const:730:8"
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
      "00c492ac",
      "DATA",
      [
        "storage",
        "00c98730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c492ac",
      "DATA",
      [
        "storage",
        "00c99700",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c48288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c4823c.md#insn-00c48288) · [`00c482a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c4823c.md#insn-00c482a8) · [`00c482ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c4823c.md#insn-00c482ac)
- 新版 [`00c4927c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49230.md#insn-00c4927c) · [`00c4929c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49230.md#insn-00c4929c) · [`00c492a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49230.md#insn-00c492a0)

~~~diff
- 00c48288 ["INT_ADD", "register:40f0:8", ["const:c48288:8", "const:4:8"]]
- 00c48288 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4927c ["INT_ADD", "register:40f0:8", ["const:c4927c:8", "const:4:8"]]
+ 00c4927c ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c48288 bytes 9a470094
+ 00c4927c bytes 91470094
- 00c482a8 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c4929c ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c482a8 bytes 88020090
+ 00c4929c bytes 88020090
- 00c482ac ["COPY", "tmp:0:8", ["const:730:8"]]
- 00c482ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c482ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c482ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c492a0 ["COPY", "tmp:0:8", ["const:700:8"]]
+ 00c492a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c492a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c492a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c482ac bytes 08c11c91
+ 00c492a0 bytes 08011c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e09436b645115d393b9c7dbb82033a7e"></a>

### [`00c4831c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c4831c.md) → [`00c49310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49310.md) FUN_00c49310

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c3909c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c4936c",
      "incomplete_value": false,
      "site": "00c49384",
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
      "definition_site": "00c48378",
      "incomplete_value": false,
      "site": "00c48390",
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
      "definition_site": "00c49374",
      "incomplete_value": false,
      "site": "00c49384",
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
      "definition_site": "00c48380",
      "incomplete_value": false,
      "site": "00c48390",
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
      "definition_site": "00c4937c",
      "incomplete_value": false,
      "site": "00c49384",
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
      "definition_site": "00c48388",
      "incomplete_value": false,
      "site": "00c48390",
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
      "00c4936c",
      "PARAM",
      [
        "storage",
        "002a0e95",
        null,
        "string"
      ]
    ],
    [
      "00c49374",
      "PARAM",
      [
        "storage",
        "002b28c7",
        null,
        "string"
      ]
    ],
    [
      "00c4937c",
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
      "00c4936c",
      "PARAM",
      [
        "storage",
        "002a0ed5",
        null,
        "string"
      ]
    ],
    [
      "00c49374",
      "PARAM",
      [
        "storage",
        "002b2911",
        null,
        "string"
      ]
    ],
    [
      "00c4937c",
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

- 旧版 [`00c48390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c4831c.md#insn-00c48390) · [`00c48378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c4831c.md#insn-00c48378) · [`00c48380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c4831c.md#insn-00c48380)
- 新版 [`00c49384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49310.md#insn-00c49384) · [`00c4936c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49310.md#insn-00c4936c) · [`00c49374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49310.md#insn-00c49374)

~~~diff
- 00c48390 ["INT_ADD", "register:40f0:8", ["const:c48390:8", "const:4:8"]]
- 00c48390 ["CALL", null, ["callee:00c3909c:8"]]
+ 00c49384 ["INT_ADD", "register:40f0:8", ["const:c49384:8", "const:4:8"]]
+ 00c49384 ["CALL", null, ["callee:00c3909c:8"]]
- 00c48390 bytes 46bfff97
+ 00c49384 bytes 46bfff97
- 00c48378 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00c48378 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c48378 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c48378 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c4936c ["COPY", "tmp:0:8", ["const:ed5:8"]]
+ 00c4936c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c4936c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c4936c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c48378 bytes 00543a91
+ 00c4936c bytes 00543b91
- 00c48380 ["COPY", "tmp:0:8", ["const:8c7:8"]]
- 00c48380 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c48380 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c48380 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c49374 ["COPY", "tmp:0:8", ["const:911:8"]]
+ 00c49374 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c49374 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c49374 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c48380 bytes 211c2391
+ 00c49374 bytes 21442491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd65bc74971b9a9cb5842660c15caa7f"></a>

### [`00c484e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c484e8.md) → [`00c494dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c494dc.md) FUN_00c494dc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c478d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c488c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c488c4.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c49540",
      "incomplete_value": false,
      "site": "00c49540",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4854c",
      "incomplete_value": false,
      "site": "00c4854c",
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
            "const:6c0:8"
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
      "00c49540",
      "DATA",
      [
        "storage",
        "00c986c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c49540",
      "DATA",
      [
        "storage",
        "00c99690",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4851c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c484e8.md#insn-00c4851c) · [`00c4853c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c484e8.md#insn-00c4853c) · [`00c48540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c484e8.md#insn-00c48540)
- 新版 [`00c49510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c494dc.md#insn-00c49510) · [`00c49530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c494dc.md#insn-00c49530) · [`00c49534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c494dc.md#insn-00c49534)

~~~diff
- 00c4851c ["INT_ADD", "register:40f0:8", ["const:c4851c:8", "const:4:8"]]
- 00c4851c ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c49510 ["INT_ADD", "register:40f0:8", ["const:c49510:8", "const:4:8"]]
+ 00c49510 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4851c bytes f5460094
+ 00c49510 bytes ec460094
- 00c4853c ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c49530 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c4853c bytes 88020090
+ 00c49530 bytes 88020090
- 00c48540 ["COPY", "tmp:0:8", ["const:6c0:8"]]
- 00c48540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c48540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c48540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c49534 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 00c49534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c49534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c49534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c48540 bytes 08011b91
+ 00c49534 bytes 08411a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a04bae85a7f0ba010d4619a6f128b96a"></a>

### [`00c487bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c487bc.md) → [`00c497b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c497b0.md) FUN_00c497b0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

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
      "definition_site": "00c49808",
      "incomplete_value": true,
      "site": "00c49814",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d91:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c48814",
      "incomplete_value": true,
      "site": "00c48820",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d51:8"
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
      "00c49808",
      "READ",
      [
        "storage",
        "002a1d51",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c49808",
      "READ",
      [
        "storage",
        "002a1d91",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c487f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c487bc.md#insn-00c487f8) · [`00c4880c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c487bc.md#insn-00c4880c) · [`00c48840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c487bc.md#insn-00c48840)
- 新版 [`00c497ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c497b0.md#insn-00c497ec) · [`00c49800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c497b0.md#insn-00c49800) · [`00c49834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c497b0.md#insn-00c49834)

~~~diff
- 00c487f8 ["INT_ADD", "register:40f0:8", ["const:c487f8:8", "const:4:8"]]
- 00c487f8 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c497ec ["INT_ADD", "register:40f0:8", ["const:c497ec:8", "const:4:8"]]
+ 00c497ec ["CALL", null, ["callee:00c5b140:8"]]
- 00c487f8 bytes 5e460094
+ 00c497ec bytes 55460094
- 00c4880c ["COPY", "tmp:0:8", ["const:d51:8"]]
- 00c4880c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4880c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4880c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c49800 ["COPY", "tmp:0:8", ["const:d91:8"]]
+ 00c49800 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c49800 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c49800 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4880c bytes 29453591
+ 00c49800 bytes 29453691
- 00c48840 ["INT_ADD", "register:40f0:8", ["const:c48840:8", "const:4:8"]]
- 00c48840 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00c49834 ["INT_ADD", "register:40f0:8", ["const:c49834:8", "const:4:8"]]
+ 00c49834 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00c48840 bytes 744a0094
+ 00c49834 bytes 6b4a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eefb80961b778399704da0014c9b2654"></a>

### [`00c48b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48b0c.md) → [`00c49b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49b00.md) FUN_00c49b00

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c461d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c49b68",
      "incomplete_value": true,
      "site": "00c49b74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bda:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c48b74",
      "incomplete_value": true,
      "site": "00c48b80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:afc:8"
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
      "definition_site": "00c49bd4",
      "incomplete_value": true,
      "site": "00c49be0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9be:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c48be0",
      "incomplete_value": true,
      "site": "00c48bec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00c49b68",
      "READ",
      [
        "storage",
        "002bfafc",
        null,
        "string"
      ]
    ],
    [
      "00c49bd4",
      "READ",
      [
        "storage",
        "002b08e7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c49b68",
      "READ",
      [
        "storage",
        "002bfbda",
        null,
        "string"
      ]
    ],
    [
      "00c49bd4",
      "READ",
      [
        "storage",
        "002b09be",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c48b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48b0c.md#insn-00c48b58) · [`00c48b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48b0c.md#insn-00c48b6c) · [`00c48b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48b0c.md#insn-00c48b98)
- 新版 [`00c49b4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49b00.md#insn-00c49b4c) · [`00c49b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49b00.md#insn-00c49b60) · [`00c49b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49b00.md#insn-00c49b8c)

~~~diff
- 00c48b58 ["INT_ADD", "register:40f0:8", ["const:c48b58:8", "const:4:8"]]
- 00c48b58 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c49b4c ["INT_ADD", "register:40f0:8", ["const:c49b4c:8", "const:4:8"]]
+ 00c49b4c ["CALL", null, ["callee:00c5b140:8"]]
- 00c48b58 bytes 86450094
+ 00c49b4c bytes 7d450094
- 00c48b6c ["COPY", "tmp:0:8", ["const:afc:8"]]
- 00c48b6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c48b6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c48b6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c49b60 ["COPY", "tmp:0:8", ["const:bda:8"]]
+ 00c49b60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c49b60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c49b60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c48b6c bytes 29f12b91
+ 00c49b60 bytes 29692f91
- 00c48b98 ["INT_ADD", "register:40f0:8", ["const:c48b98:8", "const:4:8"]]
- 00c48b98 ["CALL", null, ["callee:00c461d4:8"]]
+ 00c49b8c ["INT_ADD", "register:40f0:8", ["const:c49b8c:8", "const:4:8"]]
+ 00c49b8c ["CALL", null, ["callee:00c461d4:8"]]
- 00c48b98 bytes 92f1ff97
+ 00c49b8c bytes 92f1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecea371e23a30ed05254afb9b9583db9"></a>

### [`00c48c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48c28.md) → [`00c49c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49c1c.md) FUN_00c49c1c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c49cbc",
      "incomplete_value": true,
      "site": "00c49ccc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c48cc8",
      "incomplete_value": true,
      "site": "00c48cd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00c49cbc",
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
      "00c49cbc",
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

- 旧版 [`00c48c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48c28.md#insn-00c48c54) · [`00c48c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48c28.md#insn-00c48c78) · [`00c48cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48c28.md#insn-00c48cac)
- 新版 [`00c49c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49c1c.md#insn-00c49c48) · [`00c49c6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49c1c.md#insn-00c49c6c) · [`00c49ca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49c1c.md#insn-00c49ca0)

~~~diff
- 00c48c54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48c54 ["INT_ADD", "register:40f0:8", ["const:c48c54:8", "const:4:8"]]
- 00c48c54 ["CALLIND", null, ["register:0:8"]]
+ 00c49c48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c49c48 ["INT_ADD", "register:40f0:8", ["const:c49c48:8", "const:4:8"]]
+ 00c49c48 ["CALLIND", null, ["register:0:8"]]
- 00c48c54 bytes 00013fd6
+ 00c49c48 bytes 00013fd6
- 00c48c78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c48c78 ["INT_ADD", "register:40f0:8", ["const:c48c78:8", "const:4:8"]]
- 00c48c78 ["CALLIND", null, ["register:0:8"]]
+ 00c49c6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c49c6c ["INT_ADD", "register:40f0:8", ["const:c49c6c:8", "const:4:8"]]
+ 00c49c6c ["CALLIND", null, ["register:0:8"]]
- 00c48c78 bytes 00013fd6
+ 00c49c6c bytes 00013fd6
- 00c48cac ["INT_ADD", "register:40f0:8", ["const:c48cac:8", "const:4:8"]]
- 00c48cac ["CALL", null, ["callee:00c5b140:8"]]
+ 00c49ca0 ["INT_ADD", "register:40f0:8", ["const:c49ca0:8", "const:4:8"]]
+ 00c49ca0 ["CALL", null, ["callee:00c5b140:8"]]
- 00c48cac bytes 31450094
+ 00c49ca0 bytes 28450094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ac35314cbf65afa6b5749248dd93aad"></a>

### [`00c495f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c495f8.md) → [`00c4a5ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a5ec.md) FUN_00c4a5ec

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c4216c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c4216c.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c43160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43160.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

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
      "definition_site": "00c4a650",
      "incomplete_value": false,
      "site": "00c4a650",
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
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4965c",
      "incomplete_value": false,
      "site": "00c4965c",
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
            "const:880:8"
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
      "00c4a650",
      "DATA",
      [
        "storage",
        "00c98880",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4a650",
      "DATA",
      [
        "storage",
        "00c99850",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4962c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c495f8.md#insn-00c4962c) · [`00c4964c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c495f8.md#insn-00c4964c) · [`00c49650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c495f8.md#insn-00c49650)
- 新版 [`00c4a620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a5ec.md#insn-00c4a620) · [`00c4a640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a5ec.md#insn-00c4a640) · [`00c4a644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a5ec.md#insn-00c4a644)

~~~diff
- 00c4962c ["INT_ADD", "register:40f0:8", ["const:c4962c:8", "const:4:8"]]
- 00c4962c ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4a620 ["INT_ADD", "register:40f0:8", ["const:c4a620:8", "const:4:8"]]
+ 00c4a620 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4962c bytes b1420094
+ 00c4a620 bytes a8420094
- 00c4964c ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c4a640 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c4964c bytes 680200f0
+ 00c4a640 bytes 680200f0
- 00c49650 ["COPY", "tmp:0:8", ["const:880:8"]]
- 00c49650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c49650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c49650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4a644 ["COPY", "tmp:0:8", ["const:850:8"]]
+ 00c4a644 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4a644 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4a644 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c49650 bytes 08012291
+ 00c4a644 bytes 08412191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0db93eba80304b1835d9018221799fd2"></a>

### [`00c4978c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c4978c.md) → [`00c4a780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a780.md) FUN_00c4a780

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c49f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49f10.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c4af04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4af04.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.16% / 新版 99.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4a960",
      "incomplete_value": false,
      "site": "00c4a964",
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
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4996c",
      "incomplete_value": false,
      "site": "00c49970",
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
            "const:960:8"
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
      "definition_site": "00c4ac98",
      "incomplete_value": false,
      "site": "00c4ac9c",
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
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c49ca4",
      "incomplete_value": false,
      "site": "00c49ca8",
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
            "const:960:8"
          ]
        ]
      ]
    },
    "ordinal": 67,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4a964",
      "DATA",
      [
        "storage",
        "00c98960",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4ac9c",
      "DATA",
      [
        "storage",
        "00c98960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4a964",
      "DATA",
      [
        "storage",
        "00c99930",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4ac9c",
      "DATA",
      [
        "storage",
        "00c99930",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c497e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c4978c.md#insn-00c497e0) · [`00c4985c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c4978c.md#insn-00c4985c) · [`00c4988c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c4978c.md#insn-00c4988c)
- 新版 [`00c4a7d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a780.md#insn-00c4a7d4) · [`00c4a850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a780.md#insn-00c4a850) · [`00c4a880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a780.md#insn-00c4a880)

~~~diff
- 00c497e0 ["INT_ADD", "register:40f0:8", ["const:c497e0:8", "const:4:8"]]
- 00c497e0 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4a7d4 ["INT_ADD", "register:40f0:8", ["const:c4a7d4:8", "const:4:8"]]
+ 00c4a7d4 ["CALL", null, ["callee:00c5b140:8"]]
- 00c497e0 bytes 64420094
+ 00c4a7d4 bytes 5b420094
- 00c4985c ["INT_ADD", "register:40f0:8", ["const:c4985c:8", "const:4:8"]]
- 00c4985c ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4a850 ["INT_ADD", "register:40f0:8", ["const:c4a850:8", "const:4:8"]]
+ 00c4a850 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4985c bytes 45420094
+ 00c4a850 bytes 3c420094
- 00c4988c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4988c ["INT_ADD", "register:40f0:8", ["const:c4988c:8", "const:4:8"]]
- 00c4988c ["CALLIND", null, ["register:0:8"]]
+ 00c4a880 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4a880 ["INT_ADD", "register:40f0:8", ["const:c4a880:8", "const:4:8"]]
+ 00c4a880 ["CALLIND", null, ["register:0:8"]]
- 00c4988c bytes 00013fd6
+ 00c4a880 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1905a736083a5274abd9a2d50f30851c"></a>

### [`00c4a8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a8b4.md) → [`00c4b8a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b8a8.md) FUN_00c4b8a8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.38% / 新版 98.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ba68",
      "incomplete_value": true,
      "site": "00c4ba74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:96b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4aa74",
      "incomplete_value": true,
      "site": "00c4aa80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:894:8"
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
      "00c4ba68",
      "READ",
      [
        "storage",
        "002b1894",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4ba68",
      "READ",
      [
        "storage",
        "002b196b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4a8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a8b4.md#insn-00c4a8fc) · [`00c4a968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a8b4.md#insn-00c4a968) · [`00c4a99c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a8b4.md#insn-00c4a99c)
- 新版 [`00c4b8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b8a8.md#insn-00c4b8f0) · [`00c4b95c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b8a8.md#insn-00c4b95c) · [`00c4b990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b8a8.md#insn-00c4b990)

~~~diff
- 00c4a8fc ["INT_ADD", "register:40f0:8", ["const:c4a8fc:8", "const:4:8"]]
- 00c4a8fc ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4b8f0 ["INT_ADD", "register:40f0:8", ["const:c4b8f0:8", "const:4:8"]]
+ 00c4b8f0 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4a8fc bytes 1d3e0094
+ 00c4b8f0 bytes 143e0094
- 00c4a968 ["INT_ADD", "register:40f0:8", ["const:c4a968:8", "const:4:8"]]
- 00c4a968 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4b95c ["INT_ADD", "register:40f0:8", ["const:c4b95c:8", "const:4:8"]]
+ 00c4b95c ["CALL", null, ["callee:00c5b140:8"]]
- 00c4a968 bytes 023e0094
+ 00c4b95c bytes f93d0094
- 00c4a99c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4a99c ["INT_ADD", "register:40f0:8", ["const:c4a99c:8", "const:4:8"]]
- 00c4a99c ["CALLIND", null, ["register:0:8"]]
+ 00c4b990 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4b990 ["INT_ADD", "register:40f0:8", ["const:c4b990:8", "const:4:8"]]
+ 00c4b990 ["CALLIND", null, ["register:0:8"]]
- 00c4a99c bytes 00013fd6
+ 00c4b990 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee83600c6e2c65ee635674ded354b549"></a>

### [`00c4aba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4aba0.md) → [`00c4bb94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4bb94.md) FUN_00c4bb94

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4bbf8",
      "incomplete_value": true,
      "site": "00c4bc08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:38c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ac04",
      "incomplete_value": true,
      "site": "00c4ac14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2ae:8"
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
      "00c4bbf8",
      "READ",
      [
        "storage",
        "002bc2ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4bbf8",
      "READ",
      [
        "storage",
        "002bc38c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4abe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4aba0.md#insn-00c4abe4) · [`00c4abfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4aba0.md#insn-00c4abfc) · [`00c4ac34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4aba0.md#insn-00c4ac34)
- 新版 [`00c4bbd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4bb94.md#insn-00c4bbd8) · [`00c4bbf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4bb94.md#insn-00c4bbf0) · [`00c4bc28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4bb94.md#insn-00c4bc28)

~~~diff
- 00c4abe4 ["INT_ADD", "register:40f0:8", ["const:c4abe4:8", "const:4:8"]]
- 00c4abe4 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4bbd8 ["INT_ADD", "register:40f0:8", ["const:c4bbd8:8", "const:4:8"]]
+ 00c4bbd8 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4abe4 bytes 633d0094
+ 00c4bbd8 bytes 5a3d0094
- 00c4abfc ["COPY", "tmp:0:8", ["const:2ae:8"]]
- 00c4abfc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4abfc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4abfc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4bbf0 ["COPY", "tmp:0:8", ["const:38c:8"]]
+ 00c4bbf0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4bbf0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4bbf0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4abfc bytes 4ab90a91
+ 00c4bbf0 bytes 4a310e91
- 00c4ac34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4ac34 ["INT_ADD", "register:40f0:8", ["const:c4ac34:8", "const:4:8"]]
- 00c4ac34 ["CALLIND", null, ["register:0:8"]]
+ 00c4bc28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4bc28 ["INT_ADD", "register:40f0:8", ["const:c4bc28:8", "const:4:8"]]
+ 00c4bc28 ["CALLIND", null, ["register:0:8"]]
- 00c4ac34 bytes 00013fd6
+ 00c4bc28 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eeeb38f08f4bb90bea50c4d214857d61"></a>

### [`00c4acc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4acc4.md) → [`00c4bcb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4bcb8.md) FUN_00c4bcb8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4bd1c",
      "incomplete_value": true,
      "site": "00c4bd2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c4ad28",
      "incomplete_value": true,
      "site": "00c4ad38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00c4bd1c",
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
      "00c4bd1c",
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

- 旧版 [`00c4ad08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4acc4.md#insn-00c4ad08) · [`00c4ad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4acc4.md#insn-00c4ad20) · [`00c4ad58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4acc4.md#insn-00c4ad58)
- 新版 [`00c4bcfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4bcb8.md#insn-00c4bcfc) · [`00c4bd14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4bcb8.md#insn-00c4bd14) · [`00c4bd4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4bcb8.md#insn-00c4bd4c)

~~~diff
- 00c4ad08 ["INT_ADD", "register:40f0:8", ["const:c4ad08:8", "const:4:8"]]
- 00c4ad08 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4bcfc ["INT_ADD", "register:40f0:8", ["const:c4bcfc:8", "const:4:8"]]
+ 00c4bcfc ["CALL", null, ["callee:00c5b140:8"]]
- 00c4ad08 bytes 1a3d0094
+ 00c4bcfc bytes 113d0094
- 00c4ad20 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 00c4ad20 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4ad20 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4ad20 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4bd14 ["COPY", "tmp:0:8", ["const:eda:8"]]
+ 00c4bd14 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4bd14 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4bd14 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4ad20 bytes 4a413a91
+ 00c4bd14 bytes 4a693b91
- 00c4ad58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4ad58 ["INT_ADD", "register:40f0:8", ["const:c4ad58:8", "const:4:8"]]
- 00c4ad58 ["CALLIND", null, ["register:0:8"]]
+ 00c4bd4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4bd4c ["INT_ADD", "register:40f0:8", ["const:c4bd4c:8", "const:4:8"]]
+ 00c4bd4c ["CALLIND", null, ["register:0:8"]]
- 00c4ad58 bytes 00013fd6
+ 00c4bd4c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-894df3daceda86dd4d84f047b889b449"></a>

### [`00c4b140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b140.md) → [`00c4c134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c134.md) FUN_00c4c134

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.45% / 新版 98.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4c254",
      "incomplete_value": true,
      "site": "00c4c260",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b260",
      "incomplete_value": true,
      "site": "00c4b26c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee4:8"
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
      "00c4c254",
      "READ",
      [
        "storage",
        "002b7ee4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4c254",
      "READ",
      [
        "storage",
        "002b7fb3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4b16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b140.md#insn-00c4b16c) · [`00c4b190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b140.md#insn-00c4b190) · [`00c4b1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b140.md#insn-00c4b1bc)
- 新版 [`00c4c160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c134.md#insn-00c4c160) · [`00c4c184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c134.md#insn-00c4c184) · [`00c4c1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c134.md#insn-00c4c1b0)

~~~diff
- 00c4b16c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4b16c ["INT_ADD", "register:40f0:8", ["const:c4b16c:8", "const:4:8"]]
- 00c4b16c ["CALLIND", null, ["register:0:8"]]
+ 00c4c160 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4c160 ["INT_ADD", "register:40f0:8", ["const:c4c160:8", "const:4:8"]]
+ 00c4c160 ["CALLIND", null, ["register:0:8"]]
- 00c4b16c bytes 00013fd6
+ 00c4c160 bytes 00013fd6
- 00c4b190 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c4b190 ["INT_ADD", "register:40f0:8", ["const:c4b190:8", "const:4:8"]]
- 00c4b190 ["CALLIND", null, ["register:0:8"]]
+ 00c4c184 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4c184 ["INT_ADD", "register:40f0:8", ["const:c4c184:8", "const:4:8"]]
+ 00c4c184 ["CALLIND", null, ["register:0:8"]]
- 00c4b190 bytes 00013fd6
+ 00c4c184 bytes 00013fd6
- 00c4b1bc ["INT_ADD", "register:40f0:8", ["const:c4b1bc:8", "const:4:8"]]
- 00c4b1bc ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4c1b0 ["INT_ADD", "register:40f0:8", ["const:c4c1b0:8", "const:4:8"]]
+ 00c4c1b0 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4b1bc bytes ed3b0094
+ 00c4c1b0 bytes e43b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-353d86c0cb32cbf591cc2a95a01f046e"></a>

### [`00c4b450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b450.md) → [`00c4c444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c444.md) FUN_00c4c444

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c49f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49f10.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c4af04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4af04.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

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
      "definition_site": "00c4c4ac",
      "incomplete_value": true,
      "site": "00c4c4b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5f1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b4b8",
      "incomplete_value": true,
      "site": "00c4b4c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:524:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00c4c538",
      "incomplete_value": false,
      "site": "00c4c53c",
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
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b544",
      "incomplete_value": false,
      "site": "00c4b548",
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
            "const:960:8"
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
      "00c4c4ac",
      "READ",
      [
        "storage",
        "002ac524",
        null,
        "string"
      ]
    ],
    [
      "00c4c53c",
      "DATA",
      [
        "storage",
        "00c98960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4c4ac",
      "READ",
      [
        "storage",
        "002ac5f1",
        null,
        "string"
      ]
    ],
    [
      "00c4c53c",
      "DATA",
      [
        "storage",
        "00c99930",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4b498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b450.md#insn-00c4b498) · [`00c4b4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b450.md#insn-00c4b4b0) · [`00c4b504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b450.md#insn-00c4b504)
- 新版 [`00c4c48c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c444.md#insn-00c4c48c) · [`00c4c4a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c444.md#insn-00c4c4a4) · [`00c4c4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c444.md#insn-00c4c4f8)

~~~diff
- 00c4b498 ["INT_ADD", "register:40f0:8", ["const:c4b498:8", "const:4:8"]]
- 00c4b498 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4c48c ["INT_ADD", "register:40f0:8", ["const:c4c48c:8", "const:4:8"]]
+ 00c4c48c ["CALL", null, ["callee:00c5b140:8"]]
- 00c4b498 bytes 363b0094
+ 00c4c48c bytes 2d3b0094
- 00c4b4b0 ["COPY", "tmp:0:8", ["const:524:8"]]
- 00c4b4b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4b4b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4b4b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4c4a4 ["COPY", "tmp:0:8", ["const:5f1:8"]]
+ 00c4c4a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4c4a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4c4a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4b4b0 bytes 4a911491
+ 00c4c4a4 bytes 4ac51791
- 00c4b504 ["INT_ADD", "register:40f0:8", ["const:c4b504:8", "const:4:8"]]
- 00c4b504 ["CALL", null, ["callee:00c5b140:8"]]
+ 00c4c4f8 ["INT_ADD", "register:40f0:8", ["const:c4c4f8:8", "const:4:8"]]
+ 00c4c4f8 ["CALL", null, ["callee:00c5b140:8"]]
- 00c4b504 bytes 1b3b0094
+ 00c4c4f8 bytes 123b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-497a997f774646a6736e23f36b089752"></a>

### [`00c4b848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md) → [`00c4c83c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c83c.md) FUN_00c4c83c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c43708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) · 呼出先 6件 [`00c3e04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c3e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c4b6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) [`00c4bbf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bbf8.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)
- 新版 呼出元 1件 [`00c446fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c446fc.md) · 呼出先 6件 [`00c3f040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f040.md) [`00c3f654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f654.md) [`00c4c6b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c6b8.md) [`00c4cbec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4cbec.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.34% / 新版 96.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4c93c",
      "incomplete_value": false,
      "site": "00c4c93c",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b948",
      "incomplete_value": false,
      "site": "00c4b948",
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
            "const:610:8"
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
      "definition_site": "00c4c9e4",
      "incomplete_value": false,
      "site": "00c4c9e4",
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
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b9f0",
      "incomplete_value": false,
      "site": "00c4b9f0",
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
            "const:f80:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4caa4",
      "incomplete_value": false,
      "site": "00c4caa4",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4bab0",
      "incomplete_value": false,
      "site": "00c4bab0",
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
            "const:610:8"
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
      "00c4c93c",
      "DATA",
      [
        "storage",
        "00c99610",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4c9e4",
      "DATA",
      [
        "storage",
        "00c98f80",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4caa4",
      "DATA",
      [
        "storage",
        "00c99610",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4c93c",
      "DATA",
      [
        "storage",
        "00c9a5e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4c9e4",
      "DATA",
      [
        "storage",
        "00c99f50",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4caa4",
      "DATA",
      [
        "storage",
        "00c9a5e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4b8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md#insn-00c4b8b4) · [`00c4b8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md#insn-00c4b8c4) · [`00c4b8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md#insn-00c4b8f0)
- 新版 [`00c4c8a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c83c.md#insn-00c4c8a8) · [`00c4c8b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c83c.md#insn-00c4c8b8) · [`00c4c8e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c83c.md#insn-00c4c8e4)

~~~diff
- 00c4b8b4 ["INT_ADD", "register:40f0:8", ["const:c4b8b4:8", "const:4:8"]]
- 00c4b8b4 ["CALL", null, ["callee:00c4cbec:8"]]
+ 00c4c8a8 ["INT_ADD", "register:40f0:8", ["const:c4c8a8:8", "const:4:8"]]
+ 00c4c8a8 ["CALL", null, ["callee:00c4cbec:8"]]
- 00c4b8b4 bytes d1000094
+ 00c4c8a8 bytes d1000094
- 00c4b8c4 ["INT_ADD", "register:40f0:8", ["const:c4b8c4:8", "const:4:8"]]
- 00c4b8c4 ["CALL", null, ["callee:00c3f040:8"]]
+ 00c4c8b8 ["INT_ADD", "register:40f0:8", ["const:c4c8b8:8", "const:4:8"]]
+ 00c4c8b8 ["CALL", null, ["callee:00c3f040:8"]]
- 00c4b8c4 bytes e2c9ff97
+ 00c4c8b8 bytes e2c9ff97
- 00c4b8f0 ["INT_ADD", "register:40f0:8", ["const:c4b8f0:8", "const:4:8"]]
- 00c4b8f0 ["CALL", null, ["callee:00c3f654:8"]]
+ 00c4c8e4 ["INT_ADD", "register:40f0:8", ["const:c4c8e4:8", "const:4:8"]]
+ 00c4c8e4 ["CALL", null, ["callee:00c3f654:8"]]
- 00c4b8f0 bytes 5ccbff97
+ 00c4c8e4 bytes 5ccbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cd810341acd88217fe0efd20bd65710"></a>

### [`00c4bbf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bbf8.md) → [`00c4cbec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4cbec.md) FUN_00c4cbec

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3f3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c4b848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md) · 呼出先 5件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3e04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 2件 [`00c403a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c403a0.md) [`00c4c83c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c83c.md) · 呼出先 5件 [`00c3bd5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3f040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f040.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.29% / 新版 97.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4cd38",
      "incomplete_value": false,
      "site": "00c4cd38",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4bd44",
      "incomplete_value": false,
      "site": "00c4bd44",
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
            "const:ff0:8"
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
      "definition_site": "00c4cf24",
      "incomplete_value": false,
      "site": "00c4cf24",
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
      "definition_site": "00c4bf30",
      "incomplete_value": false,
      "site": "00c4bf30",
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
      "00c4cc44",
      "READ",
      [
        "storage",
        "00c97a30",
        null,
        "undefined1"
      ]
    ],
    [
      "00c4cc54",
      "READ",
      [
        "storage",
        "00c97a31",
        null,
        "undefined1"
      ]
    ],
    [
      "00c4cc80",
      "READ",
      [
        "storage",
        "00c97a40",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c4cc44",
      "READ",
      [
        "storage",
        "00c98a00",
        null,
        "undefined1"
      ]
    ],
    [
      "00c4cc54",
      "READ",
      [
        "storage",
        "00c98a01",
        null,
        "undefined1"
      ]
    ],
    [
      "00c4cc80",
      "READ",
      [
        "storage",
        "00c98a10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4bc30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bbf8.md#insn-00c4bc30) · [`00c4bcdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bbf8.md#insn-00c4bcdc) · [`00c4bd10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bbf8.md#insn-00c4bd10)
- 新版 [`00c4cc24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4cbec.md#insn-00c4cc24) · [`00c4ccd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4cbec.md#insn-00c4ccd0) · [`00c4cd04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4cbec.md#insn-00c4cd04)

~~~diff
- 00c4bc30 ["COPY", "register:4060:8", ["const:c97850:8"]]
+ 00c4cc24 ["COPY", "register:4060:8", ["const:c98820:8"]]
- 00c4bc30 bytes 0ce12510
+ 00c4cc24 bytes ecdf2510
- 00c4bcdc ["INT_ADD", "register:40f0:8", ["const:c4bcdc:8", "const:4:8"]]
- 00c4bcdc ["CALL", null, ["callee:00c3bd5c:8"]]
+ 00c4ccd0 ["INT_ADD", "register:40f0:8", ["const:c4ccd0:8", "const:4:8"]]
+ 00c4ccd0 ["CALL", null, ["callee:00c3bd5c:8"]]
- 00c4bcdc bytes 23bcff97
+ 00c4ccd0 bytes 23bcff97
- 00c4bd10 ["INT_ADD", "register:40f0:8", ["const:c4bd10:8", "const:4:8"]]
- 00c4bd10 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00c4cd04 ["INT_ADD", "register:40f0:8", ["const:c4cd04:8", "const:4:8"]]
+ 00c4cd04 ["CALL", null, ["callee:00c5b0c0:8"]]
- 00c4bd10 bytes f8380094
+ 00c4cd04 bytes ef380094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

