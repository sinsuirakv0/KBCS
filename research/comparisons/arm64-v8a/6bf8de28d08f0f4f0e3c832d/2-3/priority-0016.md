# v16.0.2 → v16.0.3 · 最優先の変更候補 (16)

[一覧の目次](README.md)

<a id="compare-9b0b5b0692c13317c31a38e16b1c07ea"></a>

### [`00560c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560c5c.md) → [`00560f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00560/00560f7c.md) FUN_00560f7c

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
      "definition_site": "00560f8c",
      "incomplete_value": false,
      "site": "00560f94",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560c6c",
      "incomplete_value": false,
      "site": "00560c74",
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
            "const:3a0:8"
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
      "00560f94",
      "DATA",
      [
        "storage",
        "00c6b3a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560f94",
      "DATA",
      [
        "storage",
        "00c6c370",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560c5c.md#insn-00560c68) · [`00560c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560c5c.md#insn-00560c6c) · [`00560c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560c5c.md#insn-00560c78)
- 新版 [`00560f88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00560/00560f7c.md#insn-00560f88) · [`00560f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00560/00560f7c.md#insn-00560f8c) · [`00560f98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00560/00560f7c.md#insn-00560f98)

~~~diff
- 00560c68 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00560f88 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00560c68 bytes 483800f0
+ 00560f88 bytes 68380090
- 00560c6c ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 00560c6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560c6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560c6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560f8c ["COPY", "tmp:0:8", ["const:370:8"]]
+ 00560f8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560f8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560f8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560c6c bytes 08810e91
+ 00560f8c bytes 08c10d91
- 00560c78 ["INT_ADD", "register:40f0:8", ["const:560c78:8", "const:4:8"]]
- 00560c78 ["CALL", null, ["callee:00c58f40:8"]]
+ 00560f98 ["INT_ADD", "register:40f0:8", ["const:560f98:8", "const:4:8"]]
+ 00560f98 ["CALL", null, ["callee:00c58f40:8"]]
- 00560c78 bytes bedc1b94
+ 00560f98 bytes eadf1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fec1dd5a262a7731b65dd05b9642426"></a>

### [`00560cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560cf8.md) → [`00561018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561018.md) FUN_00561018

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
      "definition_site": "00561030",
      "incomplete_value": false,
      "site": "0056103c",
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
            "const:410:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560d10",
      "incomplete_value": false,
      "site": "00560d1c",
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
            "const:440:8"
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
      "0056103c",
      "DATA",
      [
        "storage",
        "00c6b440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056103c",
      "DATA",
      [
        "storage",
        "00c6c410",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560cf8.md#insn-00560d0c) · [`00560d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560cf8.md#insn-00560d10) · [`00560d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560cf8.md#insn-00560d40)
- 新版 [`0056102c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561018.md#insn-0056102c) · [`00561030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561018.md#insn-00561030) · [`00561060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561018.md#insn-00561060)

~~~diff
- 00560d0c ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0056102c ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00560d0c bytes 483800f0
+ 0056102c bytes 483800f0
- 00560d10 ["COPY", "tmp:0:8", ["const:440:8"]]
- 00560d10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560d10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560d10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00561030 ["COPY", "tmp:0:8", ["const:410:8"]]
+ 00561030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00561030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00561030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560d10 bytes 08011191
+ 00561030 bytes 08411091
- 00560d40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00560d40 ["INT_ADD", "register:40f0:8", ["const:560d40:8", "const:4:8"]]
- 00560d40 ["CALLIND", null, ["register:0:8"]]
+ 00561060 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00561060 ["INT_ADD", "register:40f0:8", ["const:561060:8", "const:4:8"]]
+ 00561060 ["CALLIND", null, ["register:0:8"]]
- 00560d40 bytes 00013fd6
+ 00561060 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c998f56faa8d46d7625032e25e7ad5d0"></a>

### [`00560d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560d54.md) → [`00561074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561074.md) FUN_00561074

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "005610a0",
      "incomplete_value": false,
      "site": "005610a0",
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
            "const:410:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560d80",
      "incomplete_value": false,
      "site": "00560d80",
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
            "const:440:8"
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
      "005610a0",
      "DATA",
      [
        "storage",
        "00c6b440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005610a0",
      "DATA",
      [
        "storage",
        "00c6c410",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560d54.md#insn-00560d68) · [`00560d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560d54.md#insn-00560d74) · [`00560d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560d54.md#insn-00560d78)
- 新版 [`00561088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561074.md#insn-00561088) · [`00561094`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561074.md#insn-00561094) · [`00561098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561074.md#insn-00561098)

~~~diff
- 00560d68 ["INT_ADD", "register:40f0:8", ["const:560d68:8", "const:4:8"]]
- 00560d68 ["CALL", null, ["callee:00c58f30:8"]]
+ 00561088 ["INT_ADD", "register:40f0:8", ["const:561088:8", "const:4:8"]]
+ 00561088 ["CALL", null, ["callee:00c58f30:8"]]
- 00560d68 bytes 7edc1b94
+ 00561088 bytes aadf1b94
- 00560d74 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00561094 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00560d74 bytes 483800f0
+ 00561094 bytes 483800f0
- 00560d78 ["COPY", "tmp:0:8", ["const:440:8"]]
- 00560d78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560d78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560d78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00561098 ["COPY", "tmp:0:8", ["const:410:8"]]
+ 00561098 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00561098 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00561098 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560d78 bytes 08011191
+ 00561098 bytes 08411091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e040622dffabb5ce13b193b10ccc75d"></a>

### [`00560ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560ddc.md) → [`005610fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/005610fc.md) FUN_005610fc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00561118",
      "incomplete_value": true,
      "site": "00561118",
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
            "const:410:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560df8",
      "incomplete_value": true,
      "site": "00560df8",
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
            "const:440:8"
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
      "00561118",
      "DATA",
      [
        "storage",
        "00c6b440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00561118",
      "DATA",
      [
        "storage",
        "00c6c410",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560ddc.md#insn-00560df0) · [`00560df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560ddc.md#insn-00560df4) · [`00560e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560ddc.md#insn-00560e18)
- 新版 [`00561110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/005610fc.md#insn-00561110) · [`00561114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/005610fc.md#insn-00561114) · [`00561138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/005610fc.md#insn-00561138)

~~~diff
- 00560df0 ["COPY", "register:4048:8", ["const:c6b000:8"]]
+ 00561110 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 00560df0 bytes 493800f0
+ 00561110 bytes 493800f0
- 00560df4 ["COPY", "tmp:0:8", ["const:440:8"]]
- 00560df4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00560df4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00560df4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00561114 ["COPY", "tmp:0:8", ["const:410:8"]]
+ 00561114 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00561114 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00561114 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00560df4 bytes 29011191
+ 00561114 bytes 29411091
- 00560e18 ["COPY", "register:0:8", ["register:4048:8"]]
- 00560e18 ["INT_ADD", "register:40f0:8", ["const:560e18:8", "const:4:8"]]
- 00560e18 ["CALLIND", null, ["register:0:8"]]
+ 00561138 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00561138 ["INT_ADD", "register:40f0:8", ["const:561138:8", "const:4:8"]]
+ 00561138 ["CALLIND", null, ["register:0:8"]]
- 00560e18 bytes 20013fd6
+ 00561138 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c442f2327ee6687b38a115a3a66a1010"></a>

### [`00560f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560f20.md) → [`00561240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561240.md) FUN_00561240

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00560b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560b48.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)
- 新版 呼出元 1件 [`00560e68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00560/00560e68.md) · 呼出先 1件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.29% / 新版 85.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00561258",
      "incomplete_value": false,
      "site": "00561258",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560f38",
      "incomplete_value": false,
      "site": "00560f38",
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
            "const:4c0:8"
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
      "definition_site": "00561264",
      "incomplete_value": false,
      "site": "00561264",
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
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560f44",
      "incomplete_value": false,
      "site": "00560f44",
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
            "const:340:8"
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
      "00561258",
      "DATA",
      [
        "storage",
        "00c6b4c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00561264",
      "DATA",
      [
        "storage",
        "00c6b340",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00561258",
      "DATA",
      [
        "storage",
        "00c6c490",
        null,
        "undefined *"
      ]
    ],
    [
      "00561264",
      "DATA",
      [
        "storage",
        "00c6c310",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560f20.md#insn-00560f2c) · [`00560f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560f20.md#insn-00560f30) · [`00560f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560f20.md#insn-00560f3c)
- 新版 [`0056124c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561240.md#insn-0056124c) · [`00561250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561240.md#insn-00561250)

~~~diff
- 00560f2c ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 0056124c ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00560f2c bytes 483800f0
+ 0056124c bytes 483800f0
- 00560f30 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 00560f30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560f30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560f30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00561250 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 00561250 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00561250 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00561250 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560f30 bytes 08011391
+ 00561250 bytes 08411291
- 00560f3c ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00560f3c bytes 483800f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20b2b79e28c3fb27e2accdf8fc2b0e13"></a>

### [`00560fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560fd4.md) → [`005612f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/005612f4.md) FUN_005612f4

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
      "definition_site": "005612f8",
      "incomplete_value": false,
      "site": "005612fc",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560fd8",
      "incomplete_value": false,
      "site": "00560fdc",
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
            "const:4c0:8"
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
      "005612fc",
      "DATA",
      [
        "storage",
        "00c6b4c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005612fc",
      "DATA",
      [
        "storage",
        "00c6c490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560fd4.md#insn-00560fd4) · [`00560fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560fd4.md#insn-00560fd8)
- 新版 [`005612f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/005612f4.md#insn-005612f4) · [`005612f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/005612f4.md#insn-005612f8)

~~~diff
- 00560fd4 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 005612f4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00560fd4 bytes 483800f0
+ 005612f4 bytes 483800f0
- 00560fd8 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 00560fd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560fd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560fd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005612f8 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 005612f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005612f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005612f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560fd8 bytes 08011391
+ 005612f8 bytes 08411291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-613bb3e8f8b3e474c24383fcb1acb88e"></a>

### [`00560fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560fe4.md) → [`00561304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561304.md) FUN_00561304

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
      "definition_site": "00561314",
      "incomplete_value": false,
      "site": "0056131c",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560ff4",
      "incomplete_value": false,
      "site": "00560ffc",
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
            "const:4c0:8"
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
      "0056131c",
      "DATA",
      [
        "storage",
        "00c6b4c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056131c",
      "DATA",
      [
        "storage",
        "00c6c490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560fe4.md#insn-00560ff0) · [`00560ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560fe4.md#insn-00560ff4) · [`00561000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560fe4.md#insn-00561000)
- 新版 [`00561310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561304.md#insn-00561310) · [`00561314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561304.md#insn-00561314) · [`00561320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561304.md#insn-00561320)

~~~diff
- 00560ff0 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00561310 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00560ff0 bytes 483800f0
+ 00561310 bytes 483800f0
- 00560ff4 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 00560ff4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560ff4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560ff4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00561314 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 00561314 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00561314 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00561314 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560ff4 bytes 08011391
+ 00561314 bytes 08411291
- 00561000 ["INT_ADD", "register:40f0:8", ["const:561000:8", "const:4:8"]]
- 00561000 ["CALL", null, ["callee:00c58f40:8"]]
+ 00561320 ["INT_ADD", "register:40f0:8", ["const:561320:8", "const:4:8"]]
+ 00561320 ["CALL", null, ["callee:00c58f40:8"]]
- 00561000 bytes dcdb1b94
+ 00561320 bytes 08df1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80e9a4b0d26582d09463a8494451b8e0"></a>

### [`005610f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005610f4.md) → [`00561414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561414.md) FUN_00561414

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0045444c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/0045444c.md) [`00456848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456848.md) · 呼出先 14件 [`0055f5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f5b8.md) [`00597650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597650.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 2件 [`0045476c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00454/0045476c.md) [`00456b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00456/00456b68.md) · 呼出先 14件 [`0055f8d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055f/0055f8d8.md) [`00597970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597970.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.39% / 新版 96.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0056146c",
      "incomplete_value": false,
      "site": "00561478",
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
            "const:53b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056114c",
      "incomplete_value": false,
      "site": "00561158",
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
            "const:46c:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005616fc",
      "incomplete_value": false,
      "site": "00561704",
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
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005613dc",
      "incomplete_value": false,
      "site": "005613e4",
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
            "const:ce9:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0056179c",
      "incomplete_value": false,
      "site": "005617a0",
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
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056147c",
      "incomplete_value": false,
      "site": "00561480",
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
            "const:209:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0056146c",
      "PARAM",
      [
        "storage",
        "002b746c",
        null,
        "string"
      ]
    ],
    [
      "00561534",
      "PARAM",
      [
        "storage",
        "002bb46e",
        null,
        "string"
      ]
    ],
    [
      "00561550",
      "READ",
      [
        "storage",
        "002b393f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056146c",
      "PARAM",
      [
        "storage",
        "002b753b",
        null,
        "string"
      ]
    ],
    [
      "00561534",
      "PARAM",
      [
        "storage",
        "002bb54c",
        null,
        "string"
      ]
    ],
    [
      "00561550",
      "READ",
      [
        "storage",
        "002b3989",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005610f4.md#insn-00561158) · [`005613e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005610f4.md#insn-005613e4) · [`00561480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005610f4.md#insn-00561480)
- 新版 [`00561478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561414.md#insn-00561478) · [`00561704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561414.md#insn-00561704) · [`005617a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561414.md#insn-005617a0)

~~~diff
- 00561158 ["INT_ADD", "register:40f0:8", ["const:561158:8", "const:4:8"]]
- 00561158 ["CALL", null, ["callee:00c59000:8"]]
+ 00561478 ["INT_ADD", "register:40f0:8", ["const:561478:8", "const:4:8"]]
+ 00561478 ["CALL", null, ["callee:00c59000:8"]]
- 00561158 bytes b6db1b94
+ 00561478 bytes e2de1b94
- 005613e4 ["INT_ADD", "register:40f0:8", ["const:5613e4:8", "const:4:8"]]
- 005613e4 ["CALL", null, ["callee:00c59150:8"]]
+ 00561704 ["INT_ADD", "register:40f0:8", ["const:561704:8", "const:4:8"]]
+ 00561704 ["CALL", null, ["callee:00c59150:8"]]
- 005613e4 bytes 67db1b94
+ 00561704 bytes 93de1b94
- 00561480 ["INT_ADD", "register:40f0:8", ["const:561480:8", "const:4:8"]]
- 00561480 ["CALL", null, ["callee:00c59150:8"]]
+ 005617a0 ["INT_ADD", "register:40f0:8", ["const:5617a0:8", "const:4:8"]]
+ 005617a0 ["CALL", null, ["callee:00c59150:8"]]
- 00561480 bytes 40db1b94
+ 005617a0 bytes 6cde1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9f6b1a2e951296bba01cb9d93c108d0"></a>

### [`005618e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005618e8.md) → [`00561c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561c08.md) FUN_00561c08

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`0045444c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/0045444c.md) [`00456848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456848.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`0045476c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00454/0045476c.md) [`00456b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00456/00456b68.md) · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00561c24",
      "incomplete_value": false,
      "site": "00561c2c",
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
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561904",
      "incomplete_value": false,
      "site": "0056190c",
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
            "const:510:8"
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
      "00561c2c",
      "DATA",
      [
        "storage",
        "00c6b510",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00561c2c",
      "DATA",
      [
        "storage",
        "00c6c4e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005618fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005618e8.md#insn-005618fc) · [`00561900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005618e8.md#insn-00561900) · [`00561904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005618e8.md#insn-00561904)
- 新版 [`00561c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561c08.md#insn-00561c1c) · [`00561c20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561c08.md#insn-00561c20) · [`00561c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561c08.md#insn-00561c24)

~~~diff
- 005618fc ["INT_ADD", "register:40f0:8", ["const:5618fc:8", "const:4:8"]]
- 005618fc ["CALL", null, ["callee:00c58f30:8"]]
+ 00561c1c ["INT_ADD", "register:40f0:8", ["const:561c1c:8", "const:4:8"]]
+ 00561c1c ["CALL", null, ["callee:00c58f30:8"]]
- 005618fc bytes 99d91b94
+ 00561c1c bytes c5dc1b94
- 00561900 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00561c20 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00561900 bytes 483800d0
+ 00561c20 bytes 483800f0
- 00561904 ["COPY", "tmp:0:8", ["const:510:8"]]
- 00561904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00561904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00561904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00561c24 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 00561c24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00561c24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00561c24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00561904 bytes 08411491
+ 00561c24 bytes 08811391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db94fa99531261a2e15089a5515738cc"></a>

### [`0056192c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/0056192c.md) → [`00561c4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561c4c.md) FUN_00561c4c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008d54e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d54e0.md) [`008d6d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6d34.md) · 呼出先 5件 [`005604a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/005604a0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`008d648c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d6/008d648c.md) [`008d7ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d7/008d7ce0.md) · 呼出先 5件 [`005607c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00560/005607c0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59010.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00561cc8",
      "incomplete_value": false,
      "site": "00561cd0",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005619a8",
      "incomplete_value": false,
      "site": "005619b0",
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
            "const:f3a:8"
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
      "00561cac",
      "PARAM",
      [
        "storage",
        "002a8a7d",
        null,
        null
      ]
    ],
    [
      "00561cc8",
      "PARAM",
      [
        "storage",
        "002b4f3a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00561cac",
      "PARAM",
      [
        "storage",
        "002a8bd5",
        null,
        null
      ]
    ],
    [
      "00561cc8",
      "PARAM",
      [
        "storage",
        "002b5018",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005619b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/0056192c.md#insn-005619b0) · [`0056198c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/0056192c.md#insn-0056198c) · [`00561994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/0056192c.md#insn-00561994)
- 新版 [`00561cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561c4c.md#insn-00561cd0) · [`00561cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561c4c.md#insn-00561cac) · [`00561cb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561c4c.md#insn-00561cb4)

~~~diff
- 005619b0 ["INT_ADD", "register:40f0:8", ["const:5619b0:8", "const:4:8"]]
- 005619b0 ["CALL", null, ["callee:00c59010:8"]]
+ 00561cd0 ["INT_ADD", "register:40f0:8", ["const:561cd0:8", "const:4:8"]]
+ 00561cd0 ["CALL", null, ["callee:00c59010:8"]]
- 005619b0 bytes a4d91b94
+ 00561cd0 bytes d0dc1b94
- 0056198c ["COPY", "tmp:0:8", ["const:a7d:8"]]
- 0056198c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056198c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056198c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00561cac ["COPY", "tmp:0:8", ["const:bd5:8"]]
+ 00561cac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00561cac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00561cac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056198c bytes 21f42991
+ 00561cac bytes 21542f91
- 00561994 ["INT_ADD", "register:40f0:8", ["const:561994:8", "const:4:8"]]
- 00561994 ["CALL", null, ["callee:00c59010:8"]]
+ 00561cb4 ["INT_ADD", "register:40f0:8", ["const:561cb4:8", "const:4:8"]]
+ 00561cb4 ["CALL", null, ["callee:00c59010:8"]]
- 00561994 bytes abd91b94
+ 00561cb4 bytes d7dc1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4efffac47ccf8d63a17af7886a46570"></a>

### [`00561b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561b64.md) → [`00561e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561e84.md) FUN_00561e84

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008d54e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d54e0.md) [`008d6d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6d34.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58230.md)
- 新版 呼出元 2件 [`008d648c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d6/008d648c.md) [`008d7ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d7/008d7ce0.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59200.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.37% / 新版 87.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00561ed0",
      "incomplete_value": true,
      "site": "00561ed0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:989:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561bb0",
      "incomplete_value": true,
      "site": "00561bb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:93f:8"
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
      "definition_site": "00561ef0",
      "incomplete_value": true,
      "site": "00561f00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:720:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561bd0",
      "incomplete_value": true,
      "site": "00561be0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6d0:8"
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
      "definition_site": "00561eec",
      "incomplete_value": true,
      "site": "00561f04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:eef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561bcc",
      "incomplete_value": true,
      "site": "00561be4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e11:8"
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
      "00561ea8",
      "READ",
      [
        "storage",
        "002b393f",
        null,
        "string"
      ]
    ],
    [
      "00561eec",
      "READ",
      [
        "storage",
        "002bee11",
        null,
        "string"
      ]
    ],
    [
      "00561eec",
      "READ",
      [
        "storage",
        "002bee21",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00561ea8",
      "READ",
      [
        "storage",
        "002b3989",
        null,
        "string"
      ]
    ],
    [
      "00561eec",
      "READ",
      [
        "storage",
        "002beeef",
        null,
        "string"
      ]
    ],
    [
      "00561eec",
      "READ",
      [
        "storage",
        "002beeff",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561b64.md#insn-00561b80) · [`00561bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561b64.md#insn-00561bbc) · [`00561bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561b64.md#insn-00561bc4)
- 新版 [`00561ea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561e84.md#insn-00561ea0) · [`00561edc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561e84.md#insn-00561edc) · [`00561ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561e84.md#insn-00561ee4)

~~~diff
- 00561b80 ["COPY", "tmp:0:8", ["const:93f:8"]]
- 00561b80 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00561b80 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00561b80 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00561ea0 ["COPY", "tmp:0:8", ["const:989:8"]]
+ 00561ea0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00561ea0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00561ea0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00561b80 bytes 4afd2491
+ 00561ea0 bytes 4a252691
- 00561bbc ["INT_ADD", "register:40f0:8", ["const:561bbc:8", "const:4:8"]]
- 00561bbc ["CALL", null, ["callee:00c58f30:8"]]
+ 00561edc ["INT_ADD", "register:40f0:8", ["const:561edc:8", "const:4:8"]]
+ 00561edc ["CALL", null, ["callee:00c58f30:8"]]
- 00561bbc bytes e9d81b94
+ 00561edc bytes 15dc1b94
- 00561bc4 ["COPY", "tmp:0:8", ["const:e11:8"]]
- 00561bc4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00561bc4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00561bc4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00561ee4 ["COPY", "tmp:0:8", ["const:eef:8"]]
+ 00561ee4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00561ee4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00561ee4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00561bc4 bytes 4a453891
+ 00561ee4 bytes 4abd3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3449706667923bfa58b0e56d65eee78"></a>

### [`00561d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d2c.md) → [`0056204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/0056204c.md) FUN_0056204c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`008d54e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d54e0.md) [`008d6d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6d34.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`008d648c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d6/008d648c.md) [`008d7ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d7/008d7ce0.md) · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00562068",
      "incomplete_value": false,
      "site": "00562070",
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
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561d48",
      "incomplete_value": false,
      "site": "00561d50",
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
            "const:560:8"
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
      "00562070",
      "DATA",
      [
        "storage",
        "00c6b560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00562070",
      "DATA",
      [
        "storage",
        "00c6c530",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d2c.md#insn-00561d40) · [`00561d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d2c.md#insn-00561d44) · [`00561d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d2c.md#insn-00561d48)
- 新版 [`00562060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/0056204c.md#insn-00562060) · [`00562064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/0056204c.md#insn-00562064) · [`00562068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/0056204c.md#insn-00562068)

~~~diff
- 00561d40 ["INT_ADD", "register:40f0:8", ["const:561d40:8", "const:4:8"]]
- 00561d40 ["CALL", null, ["callee:00c58f30:8"]]
+ 00562060 ["INT_ADD", "register:40f0:8", ["const:562060:8", "const:4:8"]]
+ 00562060 ["CALL", null, ["callee:00c58f30:8"]]
- 00561d40 bytes 88d81b94
+ 00562060 bytes b4db1b94
- 00561d44 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00562064 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00561d44 bytes 483800d0
+ 00562064 bytes 483800d0
- 00561d48 ["COPY", "tmp:0:8", ["const:560:8"]]
- 00561d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00561d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00561d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00562068 ["COPY", "tmp:0:8", ["const:530:8"]]
+ 00562068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00562068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00562068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00561d48 bytes 08811591
+ 00562068 bytes 08c11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26b7cd9c168fd02209c6307ee10976c4"></a>

### [`00561d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d74.md) → [`00562094`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/00562094.md) FUN_00562094

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 21件 [`0043dff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dff0.md) [`0043e5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e5b8.md) [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) [`0044f988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f988.md) [`0044fd4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fd4c.md) · 呼出先 7件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00563790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563790.md) [`00585364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585364.md) [`00597684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597684.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 21件 [`0043e310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e310.md) [`0043e8d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e8d8.md) [`00445180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00445/00445180.md) [`0044fca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044f/0044fca8.md) [`0045006c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00450/0045006c.md) · 呼出先 7件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00563ab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563ab0.md) [`00585684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00585/00585684.md) [`005979a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005979a4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00562154",
      "incomplete_value": false,
      "site": "00562154",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561e34",
      "incomplete_value": false,
      "site": "00561e34",
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
            "const:5b0:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005620d8",
      "incomplete_value": true,
      "site": "005620d8",
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
      "definition_site": "00561db8",
      "incomplete_value": true,
      "site": "00561db8",
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
      "005620d4",
      "READ",
      [
        "storage",
        "00ca5dc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00562154",
      "DATA",
      [
        "storage",
        "00c6b5b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005621e0",
      "READ",
      [
        "storage",
        "00c6b5d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005620d4",
      "READ",
      [
        "storage",
        "00ca6d80",
        null,
        "undefined8"
      ]
    ],
    [
      "00562154",
      "DATA",
      [
        "storage",
        "00c6c580",
        null,
        "undefined *"
      ]
    ],
    [
      "005621e0",
      "READ",
      [
        "storage",
        "00c6c5a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d74.md#insn-00561db0) · [`00561db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d74.md#insn-00561db4) · [`00561de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d74.md#insn-00561de0)
- 新版 [`005620d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/00562094.md#insn-005620d0) · [`005620d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/00562094.md#insn-005620d4) · [`00562100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/00562094.md#insn-00562100)

~~~diff
- 00561db0 ["COPY", "register:4048:8", ["const:ca5000:8"]]
+ 005620d0 ["COPY", "register:4048:8", ["const:ca6000:8"]]
- 00561db0 bytes 293a0090
+ 005620d0 bytes 293a0090
- 00561db4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dc0:8"]]
- 00561db4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005620d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d80:8"]]
+ 005620d4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00561db4 bytes 29e146f9
+ 005620d4 bytes 29c146f9
- 00561de0 ["INT_ADD", "register:40f0:8", ["const:561de0:8", "const:4:8"]]
- 00561de0 ["CALL", null, ["callee:0043be80:8"]]
+ 00562100 ["INT_ADD", "register:40f0:8", ["const:562100:8", "const:4:8"]]
+ 00562100 ["CALL", null, ["callee:0043be80:8"]]
- 00561de0 bytes 6067fb97
+ 00562100 bytes 6067fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-883f2a4d2777b979c7b835cbf03317cf"></a>

### [`00562010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562010.md) → [`00562330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/00562330.md) FUN_00562330

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0043dff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dff0.md) [`00458b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458b30.md) [`0097f8e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0097f/0097f8e8.md) · 呼出先 10件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00562734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562734.md) [`00564820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564820.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 3件 [`0043e310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e310.md) [`00458e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00458/00458e50.md) [`00980894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00980/00980894.md) · 呼出先 10件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00562a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/00562a54.md) [`00564b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00564/00564b40.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.46% / 新版 99.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00562748",
      "incomplete_value": false,
      "site": "00562754",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00562428",
      "incomplete_value": false,
      "site": "00562434",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00562754",
      "DATA",
      [
        "storage",
        "00c6b6f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00562754",
      "DATA",
      [
        "storage",
        "00c6c6c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056207c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562010.md#insn-0056207c) · [`0056208c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562010.md#insn-0056208c) · [`005620b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562010.md#insn-005620b8)
- 新版 [`0056239c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/00562330.md#insn-0056239c) · [`005623ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/00562330.md#insn-005623ac) · [`005623d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/00562330.md#insn-005623d8)

~~~diff
- 0056207c ["INT_ADD", "register:40f0:8", ["const:56207c:8", "const:4:8"]]
- 0056207c ["CALL", null, ["callee:00562a54:8"]]
+ 0056239c ["INT_ADD", "register:40f0:8", ["const:56239c:8", "const:4:8"]]
+ 0056239c ["CALL", null, ["callee:00562a54:8"]]
- 0056207c bytes ae010094
+ 0056239c bytes ae010094
- 0056208c ["INT_ADD", "register:40f0:8", ["const:56208c:8", "const:4:8"]]
- 0056208c ["CALL", null, ["callee:00c58f50:8"]]
+ 005623ac ["INT_ADD", "register:40f0:8", ["const:5623ac:8", "const:4:8"]]
+ 005623ac ["CALL", null, ["callee:00c58f50:8"]]
- 0056208c bytes bdd71b94
+ 005623ac bytes e9da1b94
- 005620b8 ["INT_ADD", "register:40f0:8", ["const:5620b8:8", "const:4:8"]]
- 005620b8 ["CALL", null, ["callee:00c594d0:8"]]
+ 005623d8 ["INT_ADD", "register:40f0:8", ["const:5623d8:8", "const:4:8"]]
+ 005623d8 ["CALL", null, ["callee:00c594d0:8"]]
- 005620b8 bytes 12d91b94
+ 005623d8 bytes 3edc1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80e462246e0ef197dba18a9cdb663fd7"></a>

### [`00562d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562d1c.md) → [`0056303c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/0056303c.md) FUN_0056303c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00562dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562dd0.md) [`005630d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005630d8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`005630f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/005630f0.md) [`005633f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/005633f8.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00563048",
      "incomplete_value": false,
      "site": "0056304c",
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
      "definition_site": "00562d28",
      "incomplete_value": false,
      "site": "00562d2c",
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
      "00563048",
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
      "00563048",
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

- 旧版 [`00562d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562d1c.md#insn-00562d2c) · [`00562d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562d1c.md#insn-00562d24) · [`00562d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562d1c.md#insn-00562d28)
- 新版 [`0056304c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/0056303c.md#insn-0056304c) · [`00563044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/0056303c.md#insn-00563044) · [`00563048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/0056303c.md#insn-00563048)

~~~diff
- 00562d2c ["INT_ADD", "register:40f0:8", ["const:562d2c:8", "const:4:8"]]
- 00562d2c ["CALL", null, ["callee:0043bad8:8"]]
+ 0056304c ["INT_ADD", "register:40f0:8", ["const:56304c:8", "const:4:8"]]
+ 0056304c ["CALL", null, ["callee:0043bad8:8"]]
- 00562d2c bytes a362fb97
+ 0056304c bytes a362fb97
- 00562d24 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00563044 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00562d24 bytes a0eaffb0
+ 00563044 bytes a0eaffb0
- 00562d28 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00562d28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00562d28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00562d28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00563048 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00563048 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00563048 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00563048 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00562d28 bytes 00303e91
+ 00563048 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e214fcf7baf19182ad67fbd18e0b542c"></a>

### [`00563424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563424.md) → [`00563744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563744.md) FUN_00563744

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
      "definition_site": "00563748",
      "incomplete_value": false,
      "site": "0056374c",
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
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563428",
      "incomplete_value": false,
      "site": "0056342c",
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
            "const:510:8"
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
      "0056374c",
      "DATA",
      [
        "storage",
        "00c6b510",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056374c",
      "DATA",
      [
        "storage",
        "00c6c4e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563424.md#insn-00563424) · [`00563428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563424.md#insn-00563428)
- 新版 [`00563744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563744.md#insn-00563744) · [`00563748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563744.md#insn-00563748)

~~~diff
- 00563424 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00563744 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00563424 bytes 48380090
+ 00563744 bytes 483800b0
- 00563428 ["COPY", "tmp:0:8", ["const:510:8"]]
- 00563428 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00563428 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00563428 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00563748 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 00563748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00563748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00563748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00563428 bytes 08411491
+ 00563748 bytes 08811391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-922886b1c6b712bc8e0e82b71520f989"></a>

### [`00563434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563434.md) → [`00563754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563754.md) FUN_00563754

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
      "definition_site": "00563764",
      "incomplete_value": false,
      "site": "0056376c",
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
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563444",
      "incomplete_value": false,
      "site": "0056344c",
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
            "const:510:8"
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
      "0056376c",
      "DATA",
      [
        "storage",
        "00c6b510",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056376c",
      "DATA",
      [
        "storage",
        "00c6c4e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563434.md#insn-00563440) · [`00563444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563434.md#insn-00563444) · [`00563450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563434.md#insn-00563450)
- 新版 [`00563760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563754.md#insn-00563760) · [`00563764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563754.md#insn-00563764) · [`00563770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563754.md#insn-00563770)

~~~diff
- 00563440 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00563760 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00563440 bytes 48380090
+ 00563760 bytes 483800b0
- 00563444 ["COPY", "tmp:0:8", ["const:510:8"]]
- 00563444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00563444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00563444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00563764 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 00563764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00563764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00563764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00563444 bytes 08411491
+ 00563764 bytes 08811391
- 00563450 ["INT_ADD", "register:40f0:8", ["const:563450:8", "const:4:8"]]
- 00563450 ["CALL", null, ["callee:00c58f40:8"]]
+ 00563770 ["INT_ADD", "register:40f0:8", ["const:563770:8", "const:4:8"]]
+ 00563770 ["CALL", null, ["callee:00c58f40:8"]]
- 00563450 bytes c8d21b94
+ 00563770 bytes f4d51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b7dbc64d0cae4fea803eb05f45c2d57"></a>

### [`005634d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005634d4.md) → [`005637f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/005637f4.md) FUN_005637f4

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
      "definition_site": "005637f8",
      "incomplete_value": false,
      "site": "005637fc",
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
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005634d8",
      "incomplete_value": false,
      "site": "005634dc",
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
            "const:560:8"
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
      "005637fc",
      "DATA",
      [
        "storage",
        "00c6b560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005637fc",
      "DATA",
      [
        "storage",
        "00c6c530",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005634d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005634d4.md#insn-005634d4) · [`005634d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005634d4.md#insn-005634d8)
- 新版 [`005637f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/005637f4.md#insn-005637f4) · [`005637f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/005637f4.md#insn-005637f8)

~~~diff
- 005634d4 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 005637f4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 005634d4 bytes 48380090
+ 005637f4 bytes 483800b0
- 005634d8 ["COPY", "tmp:0:8", ["const:560:8"]]
- 005634d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005634d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005634d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005637f8 ["COPY", "tmp:0:8", ["const:530:8"]]
+ 005637f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005637f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005637f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005634d8 bytes 08811591
+ 005637f8 bytes 08c11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-893b6392a6a158ceebc4bfaa9310b4f2"></a>

### [`005634e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005634e4.md) → [`00563804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563804.md) FUN_00563804

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
      "definition_site": "00563814",
      "incomplete_value": false,
      "site": "0056381c",
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
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005634f4",
      "incomplete_value": false,
      "site": "005634fc",
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
            "const:560:8"
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
      "0056381c",
      "DATA",
      [
        "storage",
        "00c6b560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056381c",
      "DATA",
      [
        "storage",
        "00c6c530",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005634f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005634e4.md#insn-005634f0) · [`005634f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005634e4.md#insn-005634f4) · [`00563500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005634e4.md#insn-00563500)
- 新版 [`00563810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563804.md#insn-00563810) · [`00563814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563804.md#insn-00563814) · [`00563820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563804.md#insn-00563820)

~~~diff
- 005634f0 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00563810 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 005634f0 bytes 48380090
+ 00563810 bytes 483800b0
- 005634f4 ["COPY", "tmp:0:8", ["const:560:8"]]
- 005634f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005634f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005634f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00563814 ["COPY", "tmp:0:8", ["const:530:8"]]
+ 00563814 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00563814 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00563814 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005634f4 bytes 08811591
+ 00563814 bytes 08c11491
- 00563500 ["INT_ADD", "register:40f0:8", ["const:563500:8", "const:4:8"]]
- 00563500 ["CALL", null, ["callee:00c58f40:8"]]
+ 00563820 ["INT_ADD", "register:40f0:8", ["const:563820:8", "const:4:8"]]
+ 00563820 ["CALL", null, ["callee:00c58f40:8"]]
- 00563500 bytes 9cd21b94
+ 00563820 bytes c8d51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07c037a1758f6bb91c7a917fa3c67cb5"></a>

### [`0056352c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056352c.md) → [`0056384c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/0056384c.md) FUN_0056384c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00563864",
      "incomplete_value": false,
      "site": "00563868",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563544",
      "incomplete_value": false,
      "site": "00563548",
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
            "const:5b0:8"
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
      "00563868",
      "DATA",
      [
        "storage",
        "00c6b5b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00563868",
      "DATA",
      [
        "storage",
        "00c6c580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056352c.md#insn-00563540) · [`00563544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056352c.md#insn-00563544) · [`00563554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056352c.md#insn-00563554)
- 新版 [`00563860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/0056384c.md#insn-00563860) · [`00563864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/0056384c.md#insn-00563864) · [`00563874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/0056384c.md#insn-00563874)

~~~diff
- 00563540 ["COPY", "register:4048:8", ["const:c6b000:8"]]
+ 00563860 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 00563540 bytes 49380090
+ 00563860 bytes 493800b0
- 00563544 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 00563544 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00563544 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00563544 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00563864 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 00563864 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00563864 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00563864 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00563544 bytes 29c11691
+ 00563864 bytes 29011691
- 00563554 ["INT_ADD", "register:40f0:8", ["const:563554:8", "const:4:8"]]
- 00563554 ["CALL", null, ["callee:00c58f50:8"]]
+ 00563874 ["INT_ADD", "register:40f0:8", ["const:563874:8", "const:4:8"]]
+ 00563874 ["CALL", null, ["callee:00c58f50:8"]]
- 00563554 bytes 8bd21b94
+ 00563874 bytes b7d51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e69f0cc1e4e56413fdf9310d9e09574f"></a>

### [`0056357c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056357c.md) → [`0056389c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/0056389c.md) FUN_0056389c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005638b4",
      "incomplete_value": false,
      "site": "005638b8",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563594",
      "incomplete_value": false,
      "site": "00563598",
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
            "const:5b0:8"
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
      "005638b8",
      "DATA",
      [
        "storage",
        "00c6b5b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005638b8",
      "DATA",
      [
        "storage",
        "00c6c580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056357c.md#insn-00563590) · [`00563594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056357c.md#insn-00563594) · [`005635a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056357c.md#insn-005635a4)
- 新版 [`005638b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/0056389c.md#insn-005638b0) · [`005638b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/0056389c.md#insn-005638b4) · [`005638c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/0056389c.md#insn-005638c4)

~~~diff
- 00563590 ["COPY", "register:4048:8", ["const:c6b000:8"]]
+ 005638b0 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 00563590 bytes 49380090
+ 005638b0 bytes 493800b0
- 00563594 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 00563594 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00563594 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00563594 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005638b4 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 005638b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005638b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005638b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00563594 bytes 29c11691
+ 005638b4 bytes 29011691
- 005635a4 ["INT_ADD", "register:40f0:8", ["const:5635a4:8", "const:4:8"]]
- 005635a4 ["CALL", null, ["callee:00c58f50:8"]]
+ 005638c4 ["INT_ADD", "register:40f0:8", ["const:5638c4:8", "const:4:8"]]
+ 005638c4 ["CALL", null, ["callee:00c58f50:8"]]
- 005635a4 bytes 77d21b94
+ 005638c4 bytes a3d51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7012dddde55a8d70b87ae3cb000a59a3"></a>

### [`005635c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005635c8.md) → [`005638e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/005638e8.md) FUN_005638e8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056391c",
      "incomplete_value": false,
      "site": "0056391c",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005635fc",
      "incomplete_value": false,
      "site": "005635fc",
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
            "const:5b0:8"
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
      "0056391c",
      "DATA",
      [
        "storage",
        "00c6b5b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056391c",
      "DATA",
      [
        "storage",
        "00c6c580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005635e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005635c8.md#insn-005635e0) · [`005635ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005635c8.md#insn-005635ec) · [`005635f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005635c8.md#insn-005635f0)
- 新版 [`00563900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/005638e8.md#insn-00563900) · [`0056390c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/005638e8.md#insn-0056390c) · [`00563910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/005638e8.md#insn-00563910)

~~~diff
- 005635e0 ["INT_ADD", "register:40f0:8", ["const:5635e0:8", "const:4:8"]]
- 005635e0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00563900 ["INT_ADD", "register:40f0:8", ["const:563900:8", "const:4:8"]]
+ 00563900 ["CALL", null, ["callee:00c58f30:8"]]
- 005635e0 bytes 60d21b94
+ 00563900 bytes 8cd51b94
- 005635ec ["COPY", "register:4050:8", ["const:c6b000:8"]]
+ 0056390c ["COPY", "register:4050:8", ["const:c6c000:8"]]
- 005635ec bytes 4a380090
+ 0056390c bytes 4a3800b0
- 005635f0 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 005635f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005635f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005635f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00563910 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 00563910 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00563910 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00563910 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005635f0 bytes 4ac11691
+ 00563910 bytes 4a011691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78fa0fb18849b0208a77a48dc175d8c0"></a>

### [`005637d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005637d0.md) → [`00563af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563af0.md) FUN_00563af0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00563b1c",
      "incomplete_value": true,
      "site": "00563b1c",
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
      "definition_site": "005637fc",
      "incomplete_value": true,
      "site": "005637fc",
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
      "00563b14",
      "READ",
      [
        "storage",
        "00ca5dc0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00563b14",
      "READ",
      [
        "storage",
        "00ca6d80",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005637ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005637d0.md#insn-005637ec) · [`005637f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005637d0.md#insn-005637f4) · [`00563818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005637d0.md#insn-00563818)
- 新版 [`00563b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563af0.md#insn-00563b0c) · [`00563b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563af0.md#insn-00563b14) · [`00563b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563af0.md#insn-00563b38)

~~~diff
- 005637ec ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 00563b0c ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 005637ec bytes 083a00d0
+ 00563b0c bytes 083a00f0
- 005637f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
- 005637f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00563b14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
+ 00563b14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005637f4 bytes 08e146f9
+ 00563b14 bytes 08c146f9
- 00563818 ["COPY", "register:0:8", ["register:4048:8"]]
- 00563818 ["INT_ADD", "register:40f0:8", ["const:563818:8", "const:4:8"]]
- 00563818 ["CALLIND", null, ["register:0:8"]]
+ 00563b38 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00563b38 ["INT_ADD", "register:40f0:8", ["const:563b38:8", "const:4:8"]]
+ 00563b38 ["CALLIND", null, ["register:0:8"]]
- 00563818 bytes 20013fd6
+ 00563b38 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c42f6cb557648e061cd5f27545fe4c20"></a>

### [`0056387c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056387c.md) → [`00563b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563b9c.md) FUN_00563b9c

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
      "definition_site": "00563ba0",
      "incomplete_value": false,
      "site": "00563ba4",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563880",
      "incomplete_value": false,
      "site": "00563884",
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
      "00563ba4",
      "DATA",
      [
        "storage",
        "00c6b630",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00563ba4",
      "DATA",
      [
        "storage",
        "00c6c600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056387c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056387c.md#insn-0056387c) · [`00563880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056387c.md#insn-00563880)
- 新版 [`00563b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563b9c.md#insn-00563b9c) · [`00563ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563b9c.md#insn-00563ba0)

~~~diff
- 0056387c ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00563b9c ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 0056387c bytes 48380090
+ 00563b9c bytes 483800b0
- 00563880 ["COPY", "tmp:0:8", ["const:630:8"]]
- 00563880 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00563880 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00563880 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00563ba0 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 00563ba0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00563ba0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00563ba0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00563880 bytes 08c11891
+ 00563ba0 bytes 08011891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-874f16f741e7d4d4db977f3445281735"></a>

### [`0056388c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056388c.md) → [`00563bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563bac.md) FUN_00563bac

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
      "definition_site": "00563bbc",
      "incomplete_value": false,
      "site": "00563bc4",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056389c",
      "incomplete_value": false,
      "site": "005638a4",
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
      "00563bc4",
      "DATA",
      [
        "storage",
        "00c6b630",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00563bc4",
      "DATA",
      [
        "storage",
        "00c6c600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056388c.md#insn-00563898) · [`0056389c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056388c.md#insn-0056389c) · [`005638a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/0056388c.md#insn-005638a8)
- 新版 [`00563bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563bac.md#insn-00563bb8) · [`00563bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563bac.md#insn-00563bbc) · [`00563bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563bac.md#insn-00563bc8)

~~~diff
- 00563898 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00563bb8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00563898 bytes 48380090
+ 00563bb8 bytes 483800b0
- 0056389c ["COPY", "tmp:0:8", ["const:630:8"]]
- 0056389c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056389c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056389c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00563bbc ["COPY", "tmp:0:8", ["const:600:8"]]
+ 00563bbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00563bbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00563bbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056389c bytes 08c11891
+ 00563bbc bytes 08011891
- 005638a8 ["INT_ADD", "register:40f0:8", ["const:5638a8:8", "const:4:8"]]
- 005638a8 ["CALL", null, ["callee:00c58f40:8"]]
+ 00563bc8 ["INT_ADD", "register:40f0:8", ["const:563bc8:8", "const:4:8"]]
+ 00563bc8 ["CALL", null, ["callee:00c58f40:8"]]
- 005638a8 bytes b2d11b94
+ 00563bc8 bytes ded41b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d61586e1446c84c0656598d021179a0"></a>

### [`005638bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005638bc.md) → [`00563bdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563bdc.md) FUN_00563bdc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00563bec",
      "incomplete_value": false,
      "site": "00563bf0",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005638cc",
      "incomplete_value": false,
      "site": "005638d0",
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
            "const:680:8"
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
      "00563bf0",
      "DATA",
      [
        "storage",
        "00c6b680",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00563bf0",
      "DATA",
      [
        "storage",
        "00c6c650",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005638c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005638bc.md#insn-005638c8) · [`005638cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005638bc.md#insn-005638cc)
- 新版 [`00563be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563bdc.md#insn-00563be8) · [`00563bec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563bdc.md#insn-00563bec)

~~~diff
- 005638c8 ["COPY", "register:4048:8", ["const:c6b000:8"]]
+ 00563be8 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 005638c8 bytes 49380090
+ 00563be8 bytes 493800b0
- 005638cc ["COPY", "tmp:0:8", ["const:680:8"]]
- 005638cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005638cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005638cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00563bec ["COPY", "tmp:0:8", ["const:650:8"]]
+ 00563bec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00563bec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00563bec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005638cc bytes 29011a91
+ 00563bec bytes 29411991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fd8721f76eb12f91b9faef20ef93a17"></a>

### [`005638dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005638dc.md) → [`00563bfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563bfc.md) FUN_00563bfc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00565354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565354.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00562734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562734.md) [`00563b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563b44.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00565674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/00565674.md) · 呼出先 5件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00562a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/00562a54.md) [`00563e64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563e64.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

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
      "definition_site": "00563c28",
      "incomplete_value": false,
      "site": "00563c44",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563908",
      "incomplete_value": false,
      "site": "00563924",
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
            "const:680:8"
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
      "00563c44",
      "DATA",
      [
        "storage",
        "00c6b680",
        null,
        "undefined *"
      ]
    ],
    [
      "00563cf4",
      "READ",
      [
        "storage",
        "00c6b680",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00563c44",
      "DATA",
      [
        "storage",
        "00c6c650",
        null,
        "undefined *"
      ]
    ],
    [
      "00563cf4",
      "READ",
      [
        "storage",
        "00c6c650",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005638dc.md#insn-00563904) · [`00563908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005638dc.md#insn-00563908) · [`00563948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/005638dc.md#insn-00563948)
- 新版 [`00563c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563bfc.md#insn-00563c24) · [`00563c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563bfc.md#insn-00563c28) · [`00563c68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00563/00563bfc.md#insn-00563c68)

~~~diff
- 00563904 ["COPY", "register:4050:8", ["const:c6b000:8"]]
+ 00563c24 ["COPY", "register:4050:8", ["const:c6c000:8"]]
- 00563904 bytes 4a380090
+ 00563c24 bytes 4a3800b0
- 00563908 ["COPY", "tmp:0:8", ["const:680:8"]]
- 00563908 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00563908 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00563908 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00563c28 ["COPY", "tmp:0:8", ["const:650:8"]]
+ 00563c28 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00563c28 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00563c28 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00563908 bytes 4a011a91
+ 00563c28 bytes 4a411991
- 00563948 ["INT_ADD", "register:40f0:8", ["const:563948:8", "const:4:8"]]
- 00563948 ["CALL", null, ["callee:00562a54:8"]]
+ 00563c68 ["INT_ADD", "register:40f0:8", ["const:563c68:8", "const:4:8"]]
+ 00563c68 ["CALL", null, ["callee:00562a54:8"]]
- 00563948 bytes 7bfbff97
+ 00563c68 bytes 7bfbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a096551caf241e1f0c0f4699a7ef111"></a>

### [`005645c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005645c8.md) → [`005648e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00564/005648e8.md) FUN_005648e8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00563e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00563/00563e70.md) [`00864d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/00864d38.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) [`0091a2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0091a/0091a2e8.md) [`00a4318c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a43/00a4318c.md) · 呼出先 9件 [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md) [`00c58080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58080.md)
- 新版 呼出元 5件 [`00564190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00564/00564190.md) [`00865ce4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00865/00865ce4.md) [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) [`0091b294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0091b/0091b294.md) [`00a44180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a44/00a44180.md) · 呼出先 9件 [`00459830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459830.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59040.md) [`00c59050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59050.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00564930",
      "incomplete_value": true,
      "site": "00564940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00564610",
      "incomplete_value": true,
      "site": "00564620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00564938",
      "incomplete_value": true,
      "site": "00564944",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00564618",
      "incomplete_value": true,
      "site": "00564624",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00564998",
      "incomplete_value": true,
      "site": "0056499c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00564678",
      "incomplete_value": true,
      "site": "0056467c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0056491c",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00564920",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "00564938",
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
      "0056491c",
      "READ",
      [
        "storage",
        "00c9bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00564920",
      "READ",
      [
        "storage",
        "00c9bc58",
        null,
        "pointer"
      ]
    ],
    [
      "00564938",
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

- 旧版 [`005645ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005645c8.md#insn-005645ec) · [`005645f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005645c8.md#insn-005645f0) · [`005645fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005645c8.md#insn-005645fc)
- 新版 [`0056490c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00564/005648e8.md#insn-0056490c) · [`00564910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00564/005648e8.md#insn-00564910) · [`0056491c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00564/005648e8.md#insn-0056491c)

~~~diff
- 005645ec ["COPY", "register:40d0:8", ["const:c9a000:8"]]
+ 0056490c ["COPY", "register:40d0:8", ["const:c9b000:8"]]
- 005645ec bytes ba3900d0
+ 0056490c bytes ba3900f0
- 005645f0 ["COPY", "register:40c8:8", ["const:c9a000:8"]]
+ 00564910 ["COPY", "register:40c8:8", ["const:c9b000:8"]]
- 005645f0 bytes b93900d0
+ 00564910 bytes b93900f0
- 005645fc ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:d58:8"]]
- 005645fc ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0056491c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:d28:8"]]
+ 0056491c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 005645fc bytes 5aaf46f9
+ 0056491c bytes 5a9746f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2824633b2e0120ba25e8b3a0e3b19a9f"></a>

### [`005647d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005647d4.md) → [`00564af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00564/00564af4.md) FUN_00564af4

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
      "definition_site": "00564af8",
      "incomplete_value": false,
      "site": "00564afc",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005647d8",
      "incomplete_value": false,
      "site": "005647dc",
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
            "const:6f0:8"
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
      "00564afc",
      "DATA",
      [
        "storage",
        "00c6b6f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00564afc",
      "DATA",
      [
        "storage",
        "00c6c6c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005647d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005647d4.md#insn-005647d4) · [`005647d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005647d4.md#insn-005647d8)
- 新版 [`00564af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00564/00564af4.md#insn-00564af4) · [`00564af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00564/00564af4.md#insn-00564af8)

~~~diff
- 005647d4 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00564af4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 005647d4 bytes 283800f0
+ 00564af4 bytes 48380090
- 005647d8 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 005647d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005647d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005647d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00564af8 ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 00564af8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00564af8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00564af8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005647d8 bytes 08c11b91
+ 00564af8 bytes 08011b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d190e756b21ee84ee1910637ec5706f"></a>

### [`005647e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005647e4.md) → [`00564b04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00564/00564b04.md) FUN_00564b04

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
      "definition_site": "00564b14",
      "incomplete_value": false,
      "site": "00564b1c",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005647f4",
      "incomplete_value": false,
      "site": "005647fc",
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
            "const:6f0:8"
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
      "00564b1c",
      "DATA",
      [
        "storage",
        "00c6b6f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00564b1c",
      "DATA",
      [
        "storage",
        "00c6c6c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005647f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005647e4.md#insn-005647f0) · [`005647f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005647e4.md#insn-005647f4) · [`00564800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005647e4.md#insn-00564800)
- 新版 [`00564b10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00564/00564b04.md#insn-00564b10) · [`00564b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00564/00564b04.md#insn-00564b14) · [`00564b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00564/00564b04.md#insn-00564b20)

~~~diff
- 005647f0 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00564b10 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 005647f0 bytes 283800f0
+ 00564b10 bytes 48380090
- 005647f4 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 005647f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005647f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005647f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00564b14 ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 00564b14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00564b14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00564b14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005647f4 bytes 08c11b91
+ 00564b14 bytes 08011b91
- 00564800 ["INT_ADD", "register:40f0:8", ["const:564800:8", "const:4:8"]]
- 00564800 ["CALL", null, ["callee:00c58f40:8"]]
+ 00564b20 ["INT_ADD", "register:40f0:8", ["const:564b20:8", "const:4:8"]]
+ 00564b20 ["CALL", null, ["callee:00c58f40:8"]]
- 00564800 bytes dccd1b94
+ 00564b20 bytes 08d11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0c4efe48cee2cfb2d3b1ed338d2aa3e"></a>

### [`00564820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564820.md) → [`00564b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00564/00564b40.md) FUN_00564b40

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00562010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562010.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)
- 新版 呼出元 1件 [`00562330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/00562330.md) · 呼出先 1件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

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
      "definition_site": "00564b64",
      "incomplete_value": false,
      "site": "00564b64",
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
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564844",
      "incomplete_value": false,
      "site": "00564844",
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
            "const:740:8"
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
      "00564b64",
      "DATA",
      [
        "storage",
        "00c6b740",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00564b64",
      "DATA",
      [
        "storage",
        "00c6c710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564820.md#insn-00564838) · [`0056483c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564820.md#insn-0056483c) · [`00564840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564820.md#insn-00564840)
- 新版 [`00564b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00564/00564b40.md#insn-00564b58) · [`00564b5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00564/00564b40.md#insn-00564b5c)

~~~diff
- 00564838 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00564b58 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00564838 bytes 283800f0
+ 00564b58 bytes 48380090
- 0056483c ["COPY", "tmp:0:8", ["const:740:8"]]
- 0056483c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056483c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056483c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00564b5c ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00564b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00564b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00564b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056483c bytes 08011d91
+ 00564b5c bytes 08411c91
- 00564840 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00564840 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50f38289d071d83d3577db85430b2507"></a>

### [`00564d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564d8c.md) → [`005650ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/005650ac.md) FUN_005650ac

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59000.md) [`00c59010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59010.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0056512c",
      "incomplete_value": false,
      "site": "00565134",
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
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564e0c",
      "incomplete_value": false,
      "site": "00564e14",
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
            "const:cfe:8"
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
      "definition_site": "00565304",
      "incomplete_value": false,
      "site": "00565310",
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
            "const:a46:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564fe4",
      "incomplete_value": false,
      "site": "00564ff0",
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
            "const:8ee:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0056512c",
      "PARAM",
      [
        "storage",
        "002b2cfe",
        null,
        null
      ]
    ],
    [
      "00565268",
      "PARAM",
      [
        "storage",
        "002a2080",
        null,
        null
      ]
    ],
    [
      "00565304",
      "PARAM",
      [
        "storage",
        "002a78ee",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0056512c",
      "PARAM",
      [
        "storage",
        "002b2d48",
        null,
        null
      ]
    ],
    [
      "00565268",
      "PARAM",
      [
        "storage",
        "002a214b",
        null,
        null
      ]
    ],
    [
      "00565304",
      "PARAM",
      [
        "storage",
        "002a7a46",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564d8c.md#insn-00564e14) · [`00564ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564d8c.md#insn-00564ff0) · [`00564dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564d8c.md#insn-00564dcc)
- 新版 [`00565134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/005650ac.md#insn-00565134) · [`00565310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/005650ac.md#insn-00565310) · [`005650ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/005650ac.md#insn-005650ec)

~~~diff
- 00564e14 ["INT_ADD", "register:40f0:8", ["const:564e14:8", "const:4:8"]]
- 00564e14 ["CALL", null, ["callee:00c59010:8"]]
+ 00565134 ["INT_ADD", "register:40f0:8", ["const:565134:8", "const:4:8"]]
+ 00565134 ["CALL", null, ["callee:00c59010:8"]]
- 00564e14 bytes 8bcc1b94
+ 00565134 bytes b7cf1b94
- 00564ff0 ["INT_ADD", "register:40f0:8", ["const:564ff0:8", "const:4:8"]]
- 00564ff0 ["CALL", null, ["callee:00c59000:8"]]
+ 00565310 ["INT_ADD", "register:40f0:8", ["const:565310:8", "const:4:8"]]
+ 00565310 ["CALL", null, ["callee:00c59000:8"]]
- 00564ff0 bytes 10cc1b94
+ 00565310 bytes 3ccf1b94
- 00564dcc ["COPY", "register:0:8", ["register:4048:8"]]
- 00564dcc ["INT_ADD", "register:40f0:8", ["const:564dcc:8", "const:4:8"]]
- 00564dcc ["CALLIND", null, ["register:0:8"]]
+ 005650ec ["COPY", "register:0:8", ["register:4048:8"]]
+ 005650ec ["INT_ADD", "register:40f0:8", ["const:5650ec:8", "const:4:8"]]
+ 005650ec ["CALLIND", null, ["register:0:8"]]
- 00564dcc bytes 20013fd6
+ 005650ec bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-327f0f0c768e884296194793204dc8a0"></a>

### [`00565424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565424.md) → [`00565744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/00565744.md) FUN_00565744

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00564814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564814.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00564b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00564/00564b34.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056575c",
      "incomplete_value": false,
      "site": "00565760",
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
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056543c",
      "incomplete_value": false,
      "site": "00565440",
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
            "const:740:8"
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
      "00565760",
      "DATA",
      [
        "storage",
        "00c6b740",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00565760",
      "DATA",
      [
        "storage",
        "00c6c710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565424.md#insn-00565438) · [`0056543c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565424.md#insn-0056543c) · [`00565450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565424.md#insn-00565450)
- 新版 [`00565758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/00565744.md#insn-00565758) · [`0056575c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/00565744.md#insn-0056575c) · [`00565770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/00565744.md#insn-00565770)

~~~diff
- 00565438 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00565758 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00565438 bytes 283800d0
+ 00565758 bytes 283800f0
- 0056543c ["COPY", "tmp:0:8", ["const:740:8"]]
- 0056543c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056543c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056543c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056575c ["COPY", "tmp:0:8", ["const:710:8"]]
+ 0056575c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056575c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056575c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056543c bytes 08011d91
+ 0056575c bytes 08411c91
- 00565450 ["INT_ADD", "register:40f0:8", ["const:565450:8", "const:4:8"]]
- 00565450 ["CALL", null, ["callee:00c54d90:8"]]
+ 00565770 ["INT_ADD", "register:40f0:8", ["const:565770:8", "const:4:8"]]
+ 00565770 ["CALL", null, ["callee:00c54d90:8"]]
- 00565450 bytes 54ba1b94
+ 00565770 bytes 88bd1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebfd73f3d2f1e7220b1af43a898d8d8c"></a>

### [`005654fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/005654fc.md) → [`0056581c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/0056581c.md) _INIT_27

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00561024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561024.md) [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00561344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00561/00561344.md) [`00bc5880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5880.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 52.00% / 新版 52.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 10件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00565844",
      "incomplete_value": false,
      "site": "00565844",
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
                "const:d60:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565524",
      "incomplete_value": false,
      "site": "00565524",
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
                "const:da0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
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
      "definition_site": "00565864",
      "incomplete_value": false,
      "site": "00565864",
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
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565544",
      "incomplete_value": false,
      "site": "00565544",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056586c",
      "incomplete_value": false,
      "site": "0056586c",
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
                "const:d90:8"
              ]
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
      "definition_site": "0056554c",
      "incomplete_value": false,
      "site": "0056554c",
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
                "const:dd0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:1:8"
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
      "00565834",
      "PARAM",
      [
        "storage",
        "00ca5da0",
        null,
        null
      ]
    ],
    [
      "0056583c",
      "PARAM",
      [
        "storage",
        "00561024",
        null,
        null
      ]
    ],
    [
      "00565840",
      "PARAM",
      [
        "storage",
        "00c63060",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00565834",
      "PARAM",
      [
        "storage",
        "00ca6d60",
        null,
        null
      ]
    ],
    [
      "0056583c",
      "PARAM",
      [
        "storage",
        "00561344",
        null,
        null
      ]
    ],
    [
      "00565840",
      "PARAM",
      [
        "storage",
        "00c64030",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/005654fc.md#insn-00565528) · [`00565558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/005654fc.md#insn-00565558) · [`00565584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/005654fc.md#insn-00565584)
- 新版 [`00565848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/0056581c.md#insn-00565848) · [`00565878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/0056581c.md#insn-00565878)

~~~diff
- 00565528 ["INT_ADD", "register:40f0:8", ["const:565528:8", "const:4:8"]]
- 00565528 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00565848 ["INT_ADD", "register:40f0:8", ["const:565848:8", "const:4:8"]]
+ 00565848 ["CALL", null, ["callee:00c58ed0:8"]]
- 00565528 bytes 76ca1b94
+ 00565848 bytes a2cd1b94
- 00565558 ["INT_ADD", "register:40f0:8", ["const:565558:8", "const:4:8"]]
- 00565558 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00565878 ["INT_ADD", "register:40f0:8", ["const:565878:8", "const:4:8"]]
+ 00565878 ["CALL", null, ["callee:00c58ed0:8"]]
- 00565558 bytes 6aca1b94
+ 00565878 bytes 96cd1b94
- 00565584 ["INT_ADD", "register:40f0:8", ["const:565584:8", "const:4:8"]]
- 00565584 ["CALL", null, ["callee:00c58ed0:8"]]
- 00565584 bytes 5fca1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-760bb6a2ad2f5a1fd9ae7942346bc081"></a>

### [`00565a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565a98.md) → [`00565db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/00565db8.md) FUN_00565db8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`005689bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00568/005689bc.md) [`005692fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/005692fc.md) [`00569520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569520.md) [`0056a1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a1b4.md) [`0056a954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a954.md) · 呼出先 9件 [`0056caa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056caa0.md) [`0056ce8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056ce8c.md) [`0056d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d0ac.md) [`0056d814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d814.md) [`0056d9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d9bc.md)
- 新版 呼出元 5件 [`00568cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00568/00568cdc.md) [`0056961c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00569/0056961c.md) [`00569840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00569/00569840.md) [`0056a4d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056a/0056a4d4.md) [`0056ac74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056a/0056ac74.md) · 呼出先 9件 [`0056cdc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056c/0056cdc0.md) [`0056d1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d1ac.md) [`0056d3cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d3cc.md) [`0056db34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056db34.md) [`0056dcdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056dcdc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 99.05% / 新版 99.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00565f9c",
      "incomplete_value": true,
      "site": "00565f9c",
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
      "definition_site": "00565c7c",
      "incomplete_value": true,
      "site": "00565c7c",
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
      "00565f8c",
      "DATA",
      [
        "storage",
        "002c21ec",
        null,
        null
      ]
    ],
    [
      "00565fa4",
      "DATA",
      [
        "storage",
        "002c3120",
        null,
        "string"
      ]
    ],
    [
      "005669b4",
      "DATA",
      [
        "storage",
        "002d1568",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00565f8c",
      "DATA",
      [
        "storage",
        "002c223c",
        null,
        null
      ]
    ],
    [
      "00565fa4",
      "DATA",
      [
        "storage",
        "002c3170",
        null,
        "string"
      ]
    ],
    [
      "005669b4",
      "DATA",
      [
        "storage",
        "002d15a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565a98.md#insn-00565ae4) · [`00565bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565a98.md#insn-00565bf4) · [`00565c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/00565a98.md#insn-00565c54)
- 新版 [`00565e04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/00565db8.md#insn-00565e04) · [`00565f14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/00565db8.md#insn-00565f14) · [`00565f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/00565db8.md#insn-00565f74)

~~~diff
- 00565ae4 ["INT_ADD", "register:40f0:8", ["const:565ae4:8", "const:4:8"]]
- 00565ae4 ["CALL", null, ["callee:0056cdc0:8"]]
+ 00565e04 ["INT_ADD", "register:40f0:8", ["const:565e04:8", "const:4:8"]]
+ 00565e04 ["CALL", null, ["callee:0056cdc0:8"]]
- 00565ae4 bytes ef1b0094
+ 00565e04 bytes ef1b0094
- 00565bf4 ["INT_ADD", "register:40f0:8", ["const:565bf4:8", "const:4:8"]]
- 00565bf4 ["CALL", null, ["callee:0056d3cc:8"]]
+ 00565f14 ["INT_ADD", "register:40f0:8", ["const:565f14:8", "const:4:8"]]
+ 00565f14 ["CALL", null, ["callee:0056d3cc:8"]]
- 00565bf4 bytes 2e1d0094
+ 00565f14 bytes 2e1d0094
- 00565c54 ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 00565c54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00565c54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00565c54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00565f74 ["COPY", "tmp:0:8", ["const:240:8"]]
+ 00565f74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00565f74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00565f74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00565c54 bytes 29c10791
+ 00565f74 bytes 29010991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66accc9317fa9e95abb4c25fbb96824d"></a>

### [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) → [`00566f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00566/00566f60.md) FUN_00566f60

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056a1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a1b4.md) · 呼出先 28件 [`0056595c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/0056595c.md) [`00568968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00568/00568968.md) [`00569fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569fb4.md) [`0056a050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a050.md) [`0056ce8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056ce8c.md)
- 新版 呼出元 1件 [`0056a4d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056a/0056a4d4.md) · 呼出先 28件 [`00565c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/00565c7c.md) [`00568c88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00568/00568c88.md) [`0056a2d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056a/0056a2d4.md) [`0056a370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056a/0056a370.md) [`0056d1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d1ac.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.73% / 新版 99.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00567e18",
      "incomplete_value": true,
      "site": "00567e28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:790:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567af8",
      "incomplete_value": true,
      "site": "00567b08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 113,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005673cc",
      "value": [
        "leaf",
        "ram:56fa10:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005670ac",
      "value": [
        "leaf",
        "ram:56f6f0:8"
      ]
    },
    "ordinal": 39,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005679a0",
      "value": [
        "leaf",
        "ram:56fad4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00567680",
      "value": [
        "leaf",
        "ram:56f7b4:8"
      ]
    },
    "ordinal": 75,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00567084",
      "READ",
      [
        "storage",
        "00ca3ec4",
        null,
        "string"
      ]
    ],
    [
      "0056708c",
      "READ",
      [
        "storage",
        "00ca3ec8",
        null,
        "string"
      ]
    ],
    [
      "00567230",
      "READ",
      [
        "storage",
        "00ca3ec4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00567084",
      "READ",
      [
        "storage",
        "00ca4e94",
        null,
        "string"
      ]
    ],
    [
      "0056708c",
      "READ",
      [
        "storage",
        "00ca4e98",
        null,
        "string"
      ]
    ],
    [
      "00567230",
      "READ",
      [
        "storage",
        "00ca4e94",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005670ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md#insn-005670ac) · [`005673cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md#insn-005673cc) · [`00567680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md#insn-00567680)
- 新版 [`005673cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00566/00566f60.md#insn-005673cc) · [`005676ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00566/00566f60.md#insn-005676ec) · [`005679a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00566/00566f60.md#insn-005679a0)

~~~diff
- 005670ac ["INT_ADD", "register:40f0:8", ["const:5670ac:8", "const:4:8"]]
- 005670ac ["CALL", null, ["ram:56f6f0:8"]]
+ 005673cc ["INT_ADD", "register:40f0:8", ["const:5673cc:8", "const:4:8"]]
+ 005673cc ["CALL", null, ["ram:56fa10:8"]]
- 005670ac bytes 91210094
+ 005673cc bytes 91210094
- 005673cc ["INT_ADD", "register:40f0:8", ["const:5673cc:8", "const:4:8"]]
- 005673cc ["CALL", null, ["callee:0056f950:8"]]
+ 005676ec ["INT_ADD", "register:40f0:8", ["const:5676ec:8", "const:4:8"]]
+ 005676ec ["CALL", null, ["callee:0056f950:8"]]
- 005673cc bytes 99200094
+ 005676ec bytes 99200094
- 00567680 ["INT_ADD", "register:40f0:8", ["const:567680:8", "const:4:8"]]
- 00567680 ["CALL", null, ["ram:56f7b4:8"]]
+ 005679a0 ["INT_ADD", "register:40f0:8", ["const:5679a0:8", "const:4:8"]]
+ 005679a0 ["CALL", null, ["ram:56fad4:8"]]
- 00567680 bytes 4d200094
+ 005679a0 bytes 4d200094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7ff6aa266992eca3c096cda1f0854d6"></a>

### [`0056aba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056aba8.md) → [`0056aec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056a/0056aec8.md) FUN_0056aec8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043af6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043af6c.md) · 呼出先 11件 [`0056afac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056afac.md) [`0056b01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b01c.md) [`0056b334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b334.md) [`00570e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e78.md) [`00570e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e84.md)
- 新版 呼出元 1件 [`0043b28c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b28c.md) · 呼出先 11件 [`0056b2cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056b/0056b2cc.md) [`0056b33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056b/0056b33c.md) [`0056b654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056b/0056b654.md) [`00571198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571198.md) [`005711a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005711a4.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 82.63% / 新版 82.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 12件, `call_target` 4件, `store_condition` 5件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `store_destination` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056b010",
      "incomplete_value": false,
      "site": "0056b01c",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056acf0",
      "incomplete_value": false,
      "site": "0056acfc",
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
            "const:908:8"
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
      "definition_site": "0056b08c",
      "incomplete_value": false,
      "site": "0056b08c",
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
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ad6c",
      "incomplete_value": false,
      "site": "0056ad6c",
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
            "const:e38:8"
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
      "definition_site": "0056b140",
      "incomplete_value": false,
      "site": "0056b140",
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
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ae20",
      "incomplete_value": false,
      "site": "0056ae20",
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
            "const:e38:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0056aef8",
      "READ",
      [
        "storage",
        "00ca5e48",
        null,
        "undefined8"
      ]
    ],
    [
      "0056af10",
      "PARAM",
      [
        "storage",
        "00ca5e48",
        null,
        "undefined8"
      ]
    ],
    [
      "0056af34",
      "READ",
      [
        "storage",
        "00ca5e48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0056aef8",
      "READ",
      [
        "storage",
        "00ca6e08",
        null,
        "undefined8"
      ]
    ],
    [
      "0056af10",
      "PARAM",
      [
        "storage",
        "00ca6e08",
        null,
        "undefined8"
      ]
    ],
    [
      "0056af34",
      "READ",
      [
        "storage",
        "00ca6e08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056ac0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056aba8.md#insn-0056ac0c) · [`0056ac24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056aba8.md#insn-0056ac24) · [`0056ac2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056aba8.md#insn-0056ac2c)
- 新版 [`0056af2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056a/0056aec8.md#insn-0056af2c) · [`0056af44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056a/0056aec8.md#insn-0056af44) · [`0056af4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056a/0056aec8.md#insn-0056af4c)

~~~diff
- 0056ac0c ["INT_ADD", "register:40f0:8", ["const:56ac0c:8", "const:4:8"]]
- 0056ac0c ["CALL", null, ["callee:00c5b150:8"]]
+ 0056af2c ["INT_ADD", "register:40f0:8", ["const:56af2c:8", "const:4:8"]]
+ 0056af2c ["CALL", null, ["callee:00c5b150:8"]]
- 0056ac0c bytes 5dbd1b94
+ 0056af2c bytes 89c01b94
- 0056ac24 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056ac24 ["INT_ADD", "register:40f0:8", ["const:56ac24:8", "const:4:8"]]
- 0056ac24 ["CALLIND", null, ["register:0:8"]]
+ 0056af44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056af44 ["INT_ADD", "register:40f0:8", ["const:56af44:8", "const:4:8"]]
+ 0056af44 ["CALLIND", null, ["register:0:8"]]
- 0056ac24 bytes 00013fd6
+ 0056af44 bytes 00013fd6
- 0056ac2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
- 0056ac2c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0056af4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e08:8"]]
+ 0056af4c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0056ac2c bytes 602647f9
+ 0056af4c bytes 600647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8248cfdb009af8ed9c7a07fe47d65178"></a>

### [`0056b27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b27c.md) → [`0056b59c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056b/0056b59c.md) FUN_0056b59c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047be20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047be20.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0047c140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047c/0047c140.md) · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0056b5b8",
      "incomplete_value": true,
      "site": "0056b5bc",
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
      "definition_site": "0056b298",
      "incomplete_value": true,
      "site": "0056b29c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0056b5b4",
      "READ",
      [
        "storage",
        "00ca5e18",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b5b4",
      "READ",
      [
        "storage",
        "00ca5e20",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b600",
      "READ",
      [
        "storage",
        "00ca5e30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0056b5b4",
      "READ",
      [
        "storage",
        "00ca6dd8",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b5b4",
      "READ",
      [
        "storage",
        "00ca6de0",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b600",
      "READ",
      [
        "storage",
        "00ca6df0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b28c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b27c.md#insn-0056b28c) · [`0056b290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b27c.md#insn-0056b290) · [`0056b2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b27c.md#insn-0056b2c4)
- 新版 [`0056b5ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056b/0056b59c.md#insn-0056b5ac) · [`0056b5b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056b/0056b59c.md#insn-0056b5b0) · [`0056b5e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056b/0056b59c.md#insn-0056b5e4)

~~~diff
- 0056b28c ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 0056b5ac ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 0056b28c bytes c83900d0
+ 0056b5ac bytes c83900f0
- 0056b290 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 0056b290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056b290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056b290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056b5b0 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 0056b5b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b5b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b5b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056b290 bytes 08613891
+ 0056b5b0 bytes 08613791
- 0056b2c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056b2c4 ["INT_ADD", "register:40f0:8", ["const:56b2c4:8", "const:4:8"]]
- 0056b2c4 ["CALLIND", null, ["register:0:8"]]
+ 0056b5e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b5e4 ["INT_ADD", "register:40f0:8", ["const:56b5e4:8", "const:4:8"]]
+ 0056b5e4 ["CALLIND", null, ["register:0:8"]]
- 0056b2c4 bytes 00013fd6
+ 0056b5e4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5a528b15c68641fe1831064032d5f95"></a>

### [`0056b334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b334.md) → [`0056b654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056b/0056b654.md) FUN_0056b654

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0056aba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056aba8.md) · 呼出先 3件 [`0056b654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b654.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a190.md)
- 新版 呼出元 1件 [`0056aec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056a/0056aec8.md) · 呼出先 3件 [`0056b974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056b/0056b974.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b160.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.78% / 新版 82.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 10件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056b690",
      "incomplete_value": false,
      "site": "0056b694",
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
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b370",
      "incomplete_value": false,
      "site": "0056b374",
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
            "const:7c0:8"
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
      "definition_site": "0056b70c",
      "incomplete_value": true,
      "site": "0056b714",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2d1000:8"
              ],
              [
                "leaf",
                "const:54c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b3ec",
      "incomplete_value": true,
      "site": "0056b3f4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2d1000:8"
              ],
              [
                "leaf",
                "const:50c:8"
              ]
            ]
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
      "definition_site": "0056b718",
      "incomplete_value": true,
      "site": "0056b730",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0056b3f8",
      "incomplete_value": true,
      "site": "0056b410",
      "value": [
        "LOAD",
        "16",
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
      "0056b694",
      "DATA",
      [
        "storage",
        "00c6b7c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0056b6c0",
      "READ",
      [
        "storage",
        "00ca5e58",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b70c",
      "READ",
      [
        "storage",
        "002d150c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0056b694",
      "DATA",
      [
        "storage",
        "00c6c790",
        null,
        "undefined *"
      ]
    ],
    [
      "0056b6c0",
      "READ",
      [
        "storage",
        "00ca6e18",
        null,
        "undefined8"
      ]
    ],
    [
      "0056b70c",
      "READ",
      [
        "storage",
        "002d154c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b334.md#insn-0056b4bc) · [`0056b50c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b334.md#insn-0056b50c) · [`0056b5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b334.md#insn-0056b5e8)
- 新版 [`0056b7dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056b/0056b654.md#insn-0056b7dc) · [`0056b82c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056b/0056b654.md#insn-0056b82c) · [`0056b908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056b/0056b654.md#insn-0056b908)

~~~diff
- 0056b4bc ["COPY", "register:0:8", ["register:4040:8"]]
- 0056b4bc ["INT_ADD", "register:40f0:8", ["const:56b4bc:8", "const:4:8"]]
- 0056b4bc ["CALLIND", null, ["register:0:8"]]
+ 0056b7dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b7dc ["INT_ADD", "register:40f0:8", ["const:56b7dc:8", "const:4:8"]]
+ 0056b7dc ["CALLIND", null, ["register:0:8"]]
- 0056b4bc bytes 00013fd6
+ 0056b7dc bytes 00013fd6
- 0056b50c ["COPY", "register:0:8", ["register:4040:8"]]
- 0056b50c ["INT_ADD", "register:40f0:8", ["const:56b50c:8", "const:4:8"]]
- 0056b50c ["CALLIND", null, ["register:0:8"]]
+ 0056b82c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b82c ["INT_ADD", "register:40f0:8", ["const:56b82c:8", "const:4:8"]]
+ 0056b82c ["CALLIND", null, ["register:0:8"]]
- 0056b50c bytes 00013fd6
+ 0056b82c bytes 00013fd6
- 0056b5e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0056b5e8 ["INT_ADD", "register:40f0:8", ["const:56b5e8:8", "const:4:8"]]
- 0056b5e8 ["CALLIND", null, ["register:0:8"]]
+ 0056b908 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0056b908 ["INT_ADD", "register:40f0:8", ["const:56b908:8", "const:4:8"]]
+ 0056b908 ["CALLIND", null, ["register:0:8"]]
- 0056b5e8 bytes 00013fd6
+ 0056b908 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0240d75f71dc00967b71487b5f7d7f2b"></a>

### [`0056b7dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b7dc.md) → [`0056bafc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056b/0056bafc.md) FUN_0056bafc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00570e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e78.md) · 呼出先 8件 [`005655c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00565/005655c4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 1件 [`00571198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571198.md) · 呼出先 8件 [`005658e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00565/005658e4.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f00.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056bb14",
      "incomplete_value": false,
      "site": "0056bb18",
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
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b7f4",
      "incomplete_value": false,
      "site": "0056b7f8",
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
            "const:7c0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056bb68",
      "incomplete_value": false,
      "site": "0056bb68",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b848",
      "incomplete_value": false,
      "site": "0056b848",
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
            "const:e60:8"
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
      "0056bb18",
      "DATA",
      [
        "storage",
        "00c6b7c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0056bb60",
      "READ",
      [
        "storage",
        "00ca5e60",
        null,
        "undefined4"
      ]
    ],
    [
      "0056bb68",
      "WRITE",
      [
        "storage",
        "00ca5e60",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0056bb18",
      "DATA",
      [
        "storage",
        "00c6c790",
        null,
        "undefined *"
      ]
    ],
    [
      "0056bb60",
      "READ",
      [
        "storage",
        "00ca6e20",
        null,
        "undefined4"
      ]
    ],
    [
      "0056bb68",
      "WRITE",
      [
        "storage",
        "00ca6e20",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b7dc.md#insn-0056b848) · [`0056b7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b7dc.md#insn-0056b7f0) · [`0056b7f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b7dc.md#insn-0056b7f4)
- 新版 [`0056bb68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056b/0056bafc.md#insn-0056bb68) · [`0056bb10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056b/0056bafc.md#insn-0056bb10) · [`0056bb14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056b/0056bafc.md#insn-0056bb14)

~~~diff
- 0056b848 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e60:8"]]
- 0056b848 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 0056bb68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e20:8"]]
+ 0056bb68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 0056b848 bytes 09610eb9
+ 0056bb68 bytes 09210eb9
- 0056b7f0 ["COPY", "register:4048:8", ["const:c6b000:8"]]
+ 0056bb10 ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 0056b7f0 bytes 09380090
+ 0056bb10 bytes 093800b0
- 0056b7f4 ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 0056b7f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056b7f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056b7f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056bb14 ["COPY", "tmp:0:8", ["const:790:8"]]
+ 0056bb14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056bb14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056bb14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056b7f4 bytes 29011f91
+ 0056bb14 bytes 29411e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b49dc81cde39310bf6d0eef8e58dc92"></a>

### [`0056c53c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c53c.md) → [`0056c85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056c/0056c85c.md) FUN_0056c85c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0056c77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c77c.md) [`0056c780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c780.md) · 呼出先 8件 [`0056bd34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056bd34.md) [`00c53890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53890.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 2件 [`0056ca9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056c/0056ca9c.md) [`0056caa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056c/0056caa0.md) · 呼出先 8件 [`0056c054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056c/0056c054.md) [`00c54880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54880.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.08% / 新版 92.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056c9cc",
      "incomplete_value": false,
      "site": "0056c9cc",
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
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056c6ac",
      "incomplete_value": false,
      "site": "0056c6ac",
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
            "const:970:8"
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
      "definition_site": "0056c898",
      "incomplete_value": true,
      "site": "0056c89c",
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
      "definition_site": "0056c578",
      "incomplete_value": true,
      "site": "0056c57c",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0056c900",
      "incomplete_value": false,
      "site": "0056c90c",
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
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056c5e0",
      "incomplete_value": false,
      "site": "0056c5ec",
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
            "const:948:8"
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
      "0056c894",
      "READ",
      [
        "storage",
        "00ca5e18",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c894",
      "READ",
      [
        "storage",
        "00ca5e20",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c900",
      "PARAM",
      [
        "storage",
        "00c6b948",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0056c894",
      "READ",
      [
        "storage",
        "00ca6dd8",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c894",
      "READ",
      [
        "storage",
        "00ca6de0",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c900",
      "PARAM",
      [
        "storage",
        "00c6c918",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056c5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c53c.md#insn-0056c5ec) · [`0056c56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c53c.md#insn-0056c56c) · [`0056c570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056c53c.md#insn-0056c570)
- 新版 [`0056c90c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056c/0056c85c.md#insn-0056c90c) · [`0056c88c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056c/0056c85c.md#insn-0056c88c) · [`0056c890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056c/0056c85c.md#insn-0056c890)

~~~diff
- 0056c5ec ["INT_ADD", "register:40f0:8", ["const:56c5ec:8", "const:4:8"]]
- 0056c5ec ["CALL", null, ["callee:00c596b0:8"]]
+ 0056c90c ["INT_ADD", "register:40f0:8", ["const:56c90c:8", "const:4:8"]]
+ 0056c90c ["CALL", null, ["callee:00c596b0:8"]]
- 0056c5ec bytes 3db01b94
+ 0056c90c bytes 69b31b94
- 0056c56c ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 0056c88c ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 0056c56c bytes c83900b0
+ 0056c88c bytes c83900d0
- 0056c570 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 0056c570 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056c570 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056c570 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056c890 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 0056c890 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056c890 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056c890 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056c570 bytes 08613891
+ 0056c890 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39784a0ef0fcb1d66f09b1106083826d"></a>

### [`0056cfb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056cfb8.md) → [`0056d2d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d2d8.md) FUN_0056d2d8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00566f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00566/00566f60.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 77.05% / 新版 77.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0056d2f4",
      "incomplete_value": true,
      "site": "0056d2f8",
      "value": [
        "INT_SEXT",
        "8",
        [
          [
            "LOAD",
            "1",
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
      "definition_site": "0056cfd4",
      "incomplete_value": true,
      "site": "0056cfd8",
      "value": [
        "INT_SEXT",
        "8",
        [
          [
            "LOAD",
            "1",
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
      "0056d2f4",
      "DATA",
      [
        "storage",
        "002c3120",
        null,
        "string"
      ]
    ],
    [
      "0056d324",
      "DATA",
      [
        "storage",
        "002c3120",
        null,
        "string"
      ]
    ],
    [
      "0056d348",
      "DATA",
      [
        "storage",
        "002c3120",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056d2f4",
      "DATA",
      [
        "storage",
        "002c3170",
        null,
        "string"
      ]
    ],
    [
      "0056d324",
      "DATA",
      [
        "storage",
        "002c3170",
        null,
        "string"
      ]
    ],
    [
      "0056d348",
      "DATA",
      [
        "storage",
        "002c3170",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056cfd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056cfb8.md#insn-0056cfd0) · [`0056cffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056cfb8.md#insn-0056cffc) · [`0056d020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056c/0056cfb8.md#insn-0056d020)
- 新版 [`0056d2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d2d8.md#insn-0056d2f0) · [`0056d31c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d2d8.md#insn-0056d31c) · [`0056d340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d2d8.md#insn-0056d340)

~~~diff
- 0056cfd0 ["COPY", "tmp:0:8", ["const:120:8"]]
- 0056cfd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056cfd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056cfd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056d2f0 ["COPY", "tmp:0:8", ["const:170:8"]]
+ 0056d2f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056d2f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056d2f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056cfd0 bytes 08810491
+ 0056d2f0 bytes 08c10591
- 0056cffc ["COPY", "tmp:0:8", ["const:120:8"]]
- 0056cffc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056cffc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056cffc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056d31c ["COPY", "tmp:0:8", ["const:170:8"]]
+ 0056d31c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056d31c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056d31c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056cffc bytes 29810491
+ 0056d31c bytes 29c10591
- 0056d020 ["COPY", "tmp:0:8", ["const:120:8"]]
- 0056d020 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056d020 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056d020 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056d340 ["COPY", "tmp:0:8", ["const:170:8"]]
+ 0056d340 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056d340 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056d340 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056d020 bytes 29810491
+ 0056d340 bytes 29c10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d49e999d8c30db6d40c41eeee0192547"></a>

### [`0056d478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d478.md) → [`0056d798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d798.md) FUN_0056d798

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00569374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00569/00569374.md) [`0056d320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d320.md) · 呼出先 5件 [`0056a050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056a050.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a120.md) [`00c5a140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a140.md) [`00c5a150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a150.md)
- 新版 呼出元 2件 [`00569694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00569/00569694.md) [`0056d640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d640.md) · 呼出先 5件 [`0056a370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056a/0056a370.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0f0.md) [`00c5b110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b110.md) [`00c5b120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b120.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.13% / 新版 99.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056d9dc",
      "incomplete_value": true,
      "site": "0056d9e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056d6bc",
      "incomplete_value": true,
      "site": "0056d6c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:58:8"
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
      "0056d9dc",
      "READ",
      [
        "storage",
        "002c4058",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0056d9dc",
      "READ",
      [
        "storage",
        "002c40a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056d500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d478.md#insn-0056d500) · [`0056d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d478.md#insn-0056d520) · [`0056d558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056d/0056d478.md#insn-0056d558)
- 新版 [`0056d820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d798.md#insn-0056d820) · [`0056d840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d798.md#insn-0056d840) · [`0056d878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056d/0056d798.md#insn-0056d878)

~~~diff
- 0056d500 ["INT_ADD", "register:40f0:8", ["const:56d500:8", "const:4:8"]]
- 0056d500 ["CALL", null, ["callee:00c5b0f0:8"]]
+ 0056d820 ["INT_ADD", "register:40f0:8", ["const:56d820:8", "const:4:8"]]
+ 0056d820 ["CALL", null, ["callee:00c5b0f0:8"]]
- 0056d500 bytes 08b31b94
+ 0056d820 bytes 34b61b94
- 0056d520 ["INT_ADD", "register:40f0:8", ["const:56d520:8", "const:4:8"]]
- 0056d520 ["CALL", null, ["callee:00c5b110:8"]]
+ 0056d840 ["INT_ADD", "register:40f0:8", ["const:56d840:8", "const:4:8"]]
+ 0056d840 ["CALL", null, ["callee:00c5b110:8"]]
- 0056d520 bytes 08b31b94
+ 0056d840 bytes 34b61b94
- 0056d558 ["INT_ADD", "register:40f0:8", ["const:56d558:8", "const:4:8"]]
- 0056d558 ["CALL", null, ["callee:00c5b110:8"]]
+ 0056d878 ["INT_ADD", "register:40f0:8", ["const:56d878:8", "const:4:8"]]
+ 0056d878 ["CALL", null, ["callee:00c5b110:8"]]
- 0056d558 bytes fab21b94
+ 0056d878 bytes 26b61b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0777e7393f9319911c6f62a7833d36b5"></a>

### [`0056fde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056fde0.md) → [`00570100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00570/00570100.md) FUN_00570100

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00566c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00566/00566c40.md) · 呼出先 3件 [`00c584b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c584b0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5a1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a1f0.md)
- 新版 呼出元 1件 [`00566f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00566/00566f60.md) · 呼出先 3件 [`00c59480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59480.md) [`00c5b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md) [`00c5b1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b1c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005703e0",
      "incomplete_value": true,
      "site": "005703e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:420:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005700c0",
      "incomplete_value": true,
      "site": "005700c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005703e8",
      "incomplete_value": true,
      "site": "005703ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:200:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005700c8",
      "incomplete_value": true,
      "site": "005700cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1b0:8"
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
      "definition_site": "0057062c",
      "incomplete_value": true,
      "site": "00570630",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:420:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057030c",
      "incomplete_value": true,
      "site": "00570310",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3d0:8"
              ]
            ]
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
      "005702e0",
      "READ",
      [
        "storage",
        "002c4430",
        null,
        "undefined8"
      ]
    ],
    [
      "005703e0",
      "READ",
      [
        "storage",
        "002c23d0",
        null,
        null
      ]
    ],
    [
      "005703e8",
      "READ",
      [
        "storage",
        "002c31b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005702e0",
      "READ",
      [
        "storage",
        "002c4480",
        null,
        "undefined8"
      ]
    ],
    [
      "005703e0",
      "READ",
      [
        "storage",
        "002c2420",
        null,
        null
      ]
    ],
    [
      "005703e8",
      "READ",
      [
        "storage",
        "002c3200",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00570638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056fde0.md#insn-00570638) · [`0056fe64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056fde0.md#insn-0056fe64) · [`0056fe80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056f/0056fde0.md#insn-0056fe80)
- 新版 [`00570958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00570/00570100.md#insn-00570958) · [`00570184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00570/00570100.md#insn-00570184) · [`005701a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00570/00570100.md#insn-005701a0)

~~~diff
- 00570638 ["INT_ADD", "register:40f0:8", ["const:570638:8", "const:4:8"]]
- 00570638 ["CALL", null, ["callee:00c59480:8"]]
+ 00570958 ["INT_ADD", "register:40f0:8", ["const:570958:8", "const:4:8"]]
+ 00570958 ["CALL", null, ["callee:00c59480:8"]]
- 00570638 bytes 9e9f1b94
+ 00570958 bytes caa21b94
- 0056fe64 ["INT_ADD", "register:40f0:8", ["const:56fe64:8", "const:4:8"]]
- 0056fe64 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00570184 ["INT_ADD", "register:40f0:8", ["const:570184:8", "const:4:8"]]
+ 00570184 ["CALL", null, ["callee:00c5b0c0:8"]]
- 0056fe64 bytes a3a81b94
+ 00570184 bytes cfab1b94
- 0056fe80 ["INT_ADD", "register:40f0:8", ["const:56fe80:8", "const:4:8"]]
- 0056fe80 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 005701a0 ["INT_ADD", "register:40f0:8", ["const:5701a0:8", "const:4:8"]]
+ 005701a0 ["CALL", null, ["callee:00c5b0c0:8"]]
- 0056fe80 bytes 9ca81b94
+ 005701a0 bytes c8ab1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-480998e2b5587d23616d120b2af57b36"></a>

### [`00570e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e38.md) → [`00571158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571158.md) FUN_00571158

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
      "definition_site": "0057115c",
      "incomplete_value": false,
      "site": "00571160",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570e3c",
      "incomplete_value": false,
      "site": "00570e40",
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
            "const:908:8"
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
      "00571160",
      "DATA",
      [
        "storage",
        "00c6b908",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00571160",
      "DATA",
      [
        "storage",
        "00c6c8d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00570e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e38.md#insn-00570e38) · [`00570e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e38.md#insn-00570e3c)
- 新版 [`00571158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571158.md#insn-00571158) · [`0057115c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571158.md#insn-0057115c)

~~~diff
- 00570e38 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00571158 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00570e38 bytes c83700f0
+ 00571158 bytes c83700f0
- 00570e3c ["COPY", "tmp:0:8", ["const:908:8"]]
- 00570e3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00570e3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00570e3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057115c ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 0057115c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057115c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057115c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00570e3c bytes 08212491
+ 0057115c bytes 08612391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19b4ef1f5a05a82e3ccff1a890b05797"></a>

### [`00570e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e48.md) → [`00571168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571168.md) FUN_00571168

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
      "definition_site": "00571178",
      "incomplete_value": false,
      "site": "00571180",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570e58",
      "incomplete_value": false,
      "site": "00570e60",
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
            "const:908:8"
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
      "00571180",
      "DATA",
      [
        "storage",
        "00c6b908",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00571180",
      "DATA",
      [
        "storage",
        "00c6c8d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00570e54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e48.md#insn-00570e54) · [`00570e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e48.md#insn-00570e58) · [`00570e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e48.md#insn-00570e64)
- 新版 [`00571174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571168.md#insn-00571174) · [`00571178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571168.md#insn-00571178) · [`00571184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571168.md#insn-00571184)

~~~diff
- 00570e54 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00571174 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00570e54 bytes c83700f0
+ 00571174 bytes c83700f0
- 00570e58 ["COPY", "tmp:0:8", ["const:908:8"]]
- 00570e58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00570e58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00570e58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00571178 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 00571178 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00571178 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00571178 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00570e58 bytes 08212491
+ 00571178 bytes 08612391
- 00570e64 ["INT_ADD", "register:40f0:8", ["const:570e64:8", "const:4:8"]]
- 00570e64 ["CALL", null, ["callee:00c58f40:8"]]
+ 00571184 ["INT_ADD", "register:40f0:8", ["const:571184:8", "const:4:8"]]
+ 00571184 ["CALL", null, ["callee:00c58f40:8"]]
- 00570e64 bytes 439c1b94
+ 00571184 bytes 6f9f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7a6764f789aabcb001be805b46c7d3f"></a>

### [`00570fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570fe0.md) → [`00571300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571300.md) FUN_00571300

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00570e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570e84.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`005711a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005711a4.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0057130c",
      "incomplete_value": true,
      "site": "00571310",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00570fec",
      "incomplete_value": true,
      "site": "00570ff0",
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
      "0057130c",
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
      "0057130c",
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

- 旧版 [`00570ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570fe0.md#insn-00570ff0) · [`00570fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570fe0.md#insn-00570fe8) · [`00570fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570fe0.md#insn-00570fec)
- 新版 [`00571310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571300.md#insn-00571310) · [`00571308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571300.md#insn-00571308) · [`0057130c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571300.md#insn-0057130c)

~~~diff
- 00570ff0 ["INT_ADD", "register:40f0:8", ["const:570ff0:8", "const:4:8"]]
- 00570ff0 ["CALL", null, ["callee:0043bad8:8"]]
+ 00571310 ["INT_ADD", "register:40f0:8", ["const:571310:8", "const:4:8"]]
+ 00571310 ["CALL", null, ["callee:0043bad8:8"]]
- 00570ff0 bytes f229fb97
+ 00571310 bytes f229fb97
- 00570fe8 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00571308 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00570fe8 bytes 20eafff0
+ 00571308 bytes 20eafff0
- 00570fec ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00570fec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00570fec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00570fec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0057130c ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0057130c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0057130c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0057130c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00570fec bytes 00303e91
+ 0057130c bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43517026c260ce18c0fb7ca81b3244c3"></a>

### [`00570ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570ff4.md) → [`00571314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571314.md) FUN_00571314

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md)

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
      "definition_site": "0057132c",
      "incomplete_value": false,
      "site": "00571330",
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
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057100c",
      "incomplete_value": false,
      "site": "00571010",
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
            "const:970:8"
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
      "00571330",
      "DATA",
      [
        "storage",
        "00c6b970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00571330",
      "DATA",
      [
        "storage",
        "00c6c940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570ff4.md#insn-00571008) · [`0057100c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570ff4.md#insn-0057100c) · [`00571020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00570/00570ff4.md#insn-00571020)
- 新版 [`00571328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571314.md#insn-00571328) · [`0057132c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571314.md#insn-0057132c) · [`00571340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571314.md#insn-00571340)

~~~diff
- 00571008 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00571328 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00571008 bytes c83700d0
+ 00571328 bytes c83700f0
- 0057100c ["COPY", "tmp:0:8", ["const:970:8"]]
- 0057100c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057100c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057100c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057132c ["COPY", "tmp:0:8", ["const:940:8"]]
+ 0057132c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057132c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057132c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057100c bytes 08c12591
+ 0057132c bytes 08012591
- 00571020 ["INT_ADD", "register:40f0:8", ["const:571020:8", "const:4:8"]]
- 00571020 ["CALL", null, ["callee:00c54d90:8"]]
+ 00571340 ["INT_ADD", "register:40f0:8", ["const:571340:8", "const:4:8"]]
+ 00571340 ["CALL", null, ["callee:00c54d90:8"]]
- 00571020 bytes 608b1b94
+ 00571340 bytes 948e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c408696b8641afb107501a083d9b6ecf"></a>

### [`00571050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571050.md) → [`00571370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571370.md) FUN_00571370

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00571388",
      "incomplete_value": false,
      "site": "0057138c",
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
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571068",
      "incomplete_value": false,
      "site": "0057106c",
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
            "const:970:8"
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
      "0057138c",
      "DATA",
      [
        "storage",
        "00c6b970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057138c",
      "DATA",
      [
        "storage",
        "00c6c940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571050.md#insn-00571064) · [`00571068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571050.md#insn-00571068) · [`0057107c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571050.md#insn-0057107c)
- 新版 [`00571384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571370.md#insn-00571384) · [`00571388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571370.md#insn-00571388) · [`0057139c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571370.md#insn-0057139c)

~~~diff
- 00571064 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00571384 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00571064 bytes c83700d0
+ 00571384 bytes c83700f0
- 00571068 ["COPY", "tmp:0:8", ["const:970:8"]]
- 00571068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00571068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00571068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00571388 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 00571388 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00571388 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00571388 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00571068 bytes 08c12591
+ 00571388 bytes 08012591
- 0057107c ["INT_ADD", "register:40f0:8", ["const:57107c:8", "const:4:8"]]
- 0057107c ["CALL", null, ["callee:00c54d90:8"]]
+ 0057139c ["INT_ADD", "register:40f0:8", ["const:57139c:8", "const:4:8"]]
+ 0057139c ["CALL", null, ["callee:00c54d90:8"]]
- 0057107c bytes 498b1b94
+ 0057139c bytes 7d8e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cfc340d4e993a4bb41b2669f0320c19"></a>

### [`00571134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571134.md) → [`00571454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571454.md) FUN_00571454

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md)

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
      "definition_site": "0057146c",
      "incomplete_value": false,
      "site": "00571470",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057114c",
      "incomplete_value": false,
      "site": "00571150",
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
            "const:9c0:8"
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
      "00571470",
      "DATA",
      [
        "storage",
        "00c6b9c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00571470",
      "DATA",
      [
        "storage",
        "00c6c990",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571134.md#insn-00571148) · [`0057114c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571134.md#insn-0057114c) · [`00571160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571134.md#insn-00571160)
- 新版 [`00571468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571454.md#insn-00571468) · [`0057146c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571454.md#insn-0057146c) · [`00571480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571454.md#insn-00571480)

~~~diff
- 00571148 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00571468 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00571148 bytes c83700d0
+ 00571468 bytes c83700f0
- 0057114c ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 0057114c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057114c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057114c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0057146c ["COPY", "tmp:0:8", ["const:990:8"]]
+ 0057146c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0057146c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0057146c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057114c bytes 08012791
+ 0057146c bytes 08412691
- 00571160 ["INT_ADD", "register:40f0:8", ["const:571160:8", "const:4:8"]]
- 00571160 ["CALL", null, ["callee:00c54d90:8"]]
+ 00571480 ["INT_ADD", "register:40f0:8", ["const:571480:8", "const:4:8"]]
+ 00571480 ["CALL", null, ["callee:00c54d90:8"]]
- 00571160 bytes 108b1b94
+ 00571480 bytes 448e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34296e839e372279714ad12a5ca2fd79"></a>

### [`00571190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571190.md) → [`005714b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005714b0.md) FUN_005714b0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005714c8",
      "incomplete_value": false,
      "site": "005714cc",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005711a8",
      "incomplete_value": false,
      "site": "005711ac",
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
            "const:9c0:8"
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
      "005714cc",
      "DATA",
      [
        "storage",
        "00c6b9c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005714cc",
      "DATA",
      [
        "storage",
        "00c6c990",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005711a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571190.md#insn-005711a4) · [`005711a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571190.md#insn-005711a8) · [`005711bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571190.md#insn-005711bc)
- 新版 [`005714c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005714b0.md#insn-005714c4) · [`005714c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005714b0.md#insn-005714c8) · [`005714dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005714b0.md#insn-005714dc)

~~~diff
- 005711a4 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 005714c4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 005711a4 bytes c83700d0
+ 005714c4 bytes c83700f0
- 005711a8 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 005711a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005711a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005711a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005714c8 ["COPY", "tmp:0:8", ["const:990:8"]]
+ 005714c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005714c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005714c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005711a8 bytes 08012791
+ 005714c8 bytes 08412691
- 005711bc ["INT_ADD", "register:40f0:8", ["const:5711bc:8", "const:4:8"]]
- 005711bc ["CALL", null, ["callee:00c54d90:8"]]
+ 005714dc ["INT_ADD", "register:40f0:8", ["const:5714dc:8", "const:4:8"]]
+ 005714dc ["CALL", null, ["callee:00c54d90:8"]]
- 005711bc bytes f98a1b94
+ 005714dc bytes 2d8e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b06916b2836e75e3763a76b6a2935067"></a>

### [`00571274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571274.md) → [`00571594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571594.md) FUN_00571594

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
      "definition_site": "00571598",
      "incomplete_value": false,
      "site": "0057159c",
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
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571278",
      "incomplete_value": false,
      "site": "0057127c",
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
            "const:a10:8"
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
      "0057159c",
      "DATA",
      [
        "storage",
        "00c6ba10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057159c",
      "DATA",
      [
        "storage",
        "00c6c9e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571274.md#insn-00571274) · [`00571278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571274.md#insn-00571278)
- 新版 [`00571594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571594.md#insn-00571594) · [`00571598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571594.md#insn-00571598)

~~~diff
- 00571274 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00571594 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00571274 bytes c83700d0
+ 00571594 bytes c83700f0
- 00571278 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 00571278 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00571278 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00571278 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00571598 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 00571598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00571598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00571598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00571278 bytes 08412891
+ 00571598 bytes 08812791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-180c3da4b263043014d25458d90ab733"></a>

### [`00571284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571284.md) → [`005715a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005715a4.md) FUN_005715a4

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
      "definition_site": "005715b4",
      "incomplete_value": false,
      "site": "005715bc",
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
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571294",
      "incomplete_value": false,
      "site": "0057129c",
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
            "const:a10:8"
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
      "005715bc",
      "DATA",
      [
        "storage",
        "00c6ba10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005715bc",
      "DATA",
      [
        "storage",
        "00c6c9e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00571290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571284.md#insn-00571290) · [`00571294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571284.md#insn-00571294) · [`005712a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571284.md#insn-005712a0)
- 新版 [`005715b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005715a4.md#insn-005715b0) · [`005715b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005715a4.md#insn-005715b4) · [`005715c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005715a4.md#insn-005715c0)

~~~diff
- 00571290 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 005715b0 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00571290 bytes c83700d0
+ 005715b0 bytes c83700f0
- 00571294 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 00571294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00571294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00571294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005715b4 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 005715b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005715b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005715b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00571294 bytes 08412891
+ 005715b4 bytes 08812791
- 005712a0 ["INT_ADD", "register:40f0:8", ["const:5712a0:8", "const:4:8"]]
- 005712a0 ["CALL", null, ["callee:00c58f40:8"]]
+ 005715c0 ["INT_ADD", "register:40f0:8", ["const:5715c0:8", "const:4:8"]]
+ 005715c0 ["CALL", null, ["callee:00c58f40:8"]]
- 005712a0 bytes 349b1b94
+ 005715c0 bytes 609e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9de8b73f90ac614ff00a705cf38b2451"></a>

### [`005712c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005712c4.md) → [`005715e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005715e4.md) _INIT_28

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`0056ab10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056a/0056ab10.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0056ae30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0056a/0056ae30.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 56.52% / 新版 56.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00571610",
      "incomplete_value": false,
      "site": "00571610",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005712f0",
      "incomplete_value": false,
      "site": "005712f0",
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
            "const:e18:8"
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
      "definition_site": "00571610",
      "incomplete_value": false,
      "site": "00571610",
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
                "const:dd8:8"
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
      "definition_site": "005712f0",
      "incomplete_value": false,
      "site": "005712f0",
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
                "const:e18:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00571614",
      "incomplete_value": false,
      "site": "00571614",
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
                "const:dd8:8"
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
      "definition_site": "005712f4",
      "incomplete_value": false,
      "site": "005712f4",
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
                "const:e18:8"
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
      "00571604",
      "PARAM",
      [
        "storage",
        "00ca5e18",
        null,
        "undefined8"
      ]
    ],
    [
      "00571608",
      "PARAM",
      [
        "storage",
        "0056ab10",
        null,
        null
      ]
    ],
    [
      "0057160c",
      "PARAM",
      [
        "storage",
        "00c63060",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00571604",
      "PARAM",
      [
        "storage",
        "00ca6dd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00571608",
      "PARAM",
      [
        "storage",
        "0056ae30",
        null,
        null
      ]
    ],
    [
      "0057160c",
      "PARAM",
      [
        "storage",
        "00c64030",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005712f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005712c4.md#insn-005712f8) · [`005712d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005712c4.md#insn-005712d4) · [`005712d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005712c4.md#insn-005712d8)
- 新版 [`00571618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005715e4.md#insn-00571618) · [`005715f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005715e4.md#insn-005715f4) · [`005715f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/005715e4.md#insn-005715f8)

~~~diff
- 005712f8 ["INT_ADD", "register:40f0:8", ["const:5712f8:8", "const:4:8"]]
- 005712f8 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00571618 ["INT_ADD", "register:40f0:8", ["const:571618:8", "const:4:8"]]
+ 00571618 ["CALL", null, ["callee:00c58ed0:8"]]
- 005712f8 bytes 029b1b94
+ 00571618 bytes 2e9e1b94
- 005712d4 ["COPY", "register:4098:8", ["const:56ab10:8"]]
+ 005715f4 ["COPY", "register:4098:8", ["const:56ae30:8"]]
- 005712d4 bytes f3c1fc10
+ 005715f4 bytes f3c1fc10
- 005712d8 ["COPY", "register:40a0:8", ["const:c63000:8"]]
+ 005715f8 ["COPY", "register:40a0:8", ["const:c64000:8"]]
- 005712d8 bytes 943700d0
+ 005715f8 bytes 943700f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-580dfcdcfb3b63e1cbe650d0a871aa27"></a>

### [`00571320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571320.md) → [`00571640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571640.md) FUN_00571640

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00573ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00573/00573ba0.md) [`00573ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00573/00573ec0.md) [`00574120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574120.md) · 呼出先 10件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`0057489c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/0057489c.md) [`00596f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596f6c.md) [`00597648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597648.md) [`00597728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597728.md)
- 新版 呼出元 3件 [`00573ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00573/00573ec0.md) [`005741e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/005741e0.md) [`00574440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574440.md) · 呼出先 10件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`00574bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574bbc.md) [`0059728c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059728c.md) [`00597968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597968.md) [`00597a48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597a48.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.21% / 新版 94.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005716c8",
      "incomplete_value": true,
      "site": "005716c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:31b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005713a8",
      "incomplete_value": true,
      "site": "005713a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:250:8"
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
      "definition_site": "00571730",
      "incomplete_value": true,
      "site": "00571730",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d4c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00571410",
      "incomplete_value": true,
      "site": "00571410",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d02:8"
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
      "definition_site": "005717fc",
      "incomplete_value": true,
      "site": "005717fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e65:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005714dc",
      "incomplete_value": true,
      "site": "005714dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e1b:8"
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
      "005716b8",
      "READ",
      [
        "storage",
        "002a3250",
        null,
        "string"
      ]
    ],
    [
      "00571718",
      "READ",
      [
        "storage",
        "002b2d02",
        null,
        "string"
      ]
    ],
    [
      "005717ec",
      "READ",
      [
        "storage",
        "002b1e1b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005716b8",
      "READ",
      [
        "storage",
        "002a331b",
        null,
        "string"
      ]
    ],
    [
      "00571718",
      "READ",
      [
        "storage",
        "002b2d4c",
        null,
        "string"
      ]
    ],
    [
      "005717ec",
      "READ",
      [
        "storage",
        "002b1e65",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005716c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571320.md#insn-005716c8) · [`0057135c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571320.md#insn-0057135c) · [`00571368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571320.md#insn-00571368)
- 新版 [`005719e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571640.md#insn-005719e8) · [`0057167c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571640.md#insn-0057167c) · [`00571688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571640.md#insn-00571688)

~~~diff
- 005716c8 ["INT_ADD", "register:40f0:8", ["const:5716c8:8", "const:4:8"]]
- 005716c8 ["CALL", null, ["callee:00c58f50:8"]]
+ 005719e8 ["INT_ADD", "register:40f0:8", ["const:5719e8:8", "const:4:8"]]
+ 005719e8 ["CALL", null, ["callee:00c58f50:8"]]
- 005716c8 bytes 2e9a1b94
+ 005719e8 bytes 5a9d1b94
- 0057135c ["INT_ADD", "register:40f0:8", ["const:57135c:8", "const:4:8"]]
- 0057135c ["CALL", null, ["callee:00597968:8"]]
+ 0057167c ["INT_ADD", "register:40f0:8", ["const:57167c:8", "const:4:8"]]
+ 0057167c ["CALL", null, ["callee:00597968:8"]]
- 0057135c bytes bb980094
+ 0057167c bytes bb980094
- 00571368 ["INT_ADD", "register:40f0:8", ["const:571368:8", "const:4:8"]]
- 00571368 ["CALL", null, ["callee:0059728c:8"]]
+ 00571688 ["INT_ADD", "register:40f0:8", ["const:571688:8", "const:4:8"]]
+ 00571688 ["CALL", null, ["callee:0059728c:8"]]
- 00571368 bytes 01970094
+ 00571688 bytes 01970094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05fabc78870129e91c5679c93dfc78ce"></a>

### [`00572138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572138.md) → [`00572458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572458.md) FUN_00572458

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005509d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509d8.md) · 呼出先 11件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`00550cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550cf8.md) · 呼出先 11件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005724bc",
      "incomplete_value": true,
      "site": "005724cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:16a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057219c",
      "incomplete_value": true,
      "site": "005721ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9f:8"
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
      "definition_site": "005724d0",
      "incomplete_value": true,
      "site": "005724d0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005721b0",
      "incomplete_value": true,
      "site": "005721b0",
      "value": [
        "LOAD",
        "8",
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
      "0057249c",
      "READ",
      [
        "storage",
        "002bff23",
        null,
        "string"
      ]
    ],
    [
      "005724bc",
      "READ",
      [
        "storage",
        "002a209f",
        null,
        "string"
      ]
    ],
    [
      "005724c4",
      "READ",
      [
        "storage",
        "002a20ad",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0057249c",
      "READ",
      [
        "storage",
        "002bff6d",
        null,
        "string"
      ]
    ],
    [
      "005724bc",
      "READ",
      [
        "storage",
        "002a216a",
        null,
        "string"
      ]
    ],
    [
      "005724c4",
      "READ",
      [
        "storage",
        "002a2178",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00572164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572138.md#insn-00572164) · [`0057216c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572138.md#insn-0057216c) · [`00572174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572138.md#insn-00572174)
- 新版 [`00572484`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572458.md#insn-00572484) · [`0057248c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572458.md#insn-0057248c) · [`00572494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572458.md#insn-00572494)

~~~diff
- 00572164 ["INT_ADD", "register:40f0:8", ["const:572164:8", "const:4:8"]]
- 00572164 ["CALL", null, ["callee:005891cc:8"]]
+ 00572484 ["INT_ADD", "register:40f0:8", ["const:572484:8", "const:4:8"]]
+ 00572484 ["CALL", null, ["callee:005891cc:8"]]
- 00572164 bytes 525b0094
+ 00572484 bytes 525b0094
- 0057216c ["INT_ADD", "register:40f0:8", ["const:57216c:8", "const:4:8"]]
- 0057216c ["CALL", null, ["callee:005894bc:8"]]
+ 0057248c ["INT_ADD", "register:40f0:8", ["const:57248c:8", "const:4:8"]]
+ 0057248c ["CALL", null, ["callee:005894bc:8"]]
- 0057216c bytes 0c5c0094
+ 0057248c bytes 0c5c0094
- 00572174 ["COPY", "tmp:0:8", ["const:f23:8"]]
- 00572174 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00572174 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00572174 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00572494 ["COPY", "tmp:0:8", ["const:f6d:8"]]
+ 00572494 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00572494 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00572494 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00572174 bytes 298d3c91
+ 00572494 bytes 29b53d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51883f531423e029323bced4776ad38f"></a>

### [`005722ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005722ec.md) → [`0057260c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/0057260c.md) FUN_0057260c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005509dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509dc.md) · 呼出先 11件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`00550cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550cfc.md) · 呼出先 11件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00572664",
      "incomplete_value": true,
      "site": "00572664",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f6d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572344",
      "incomplete_value": true,
      "site": "00572344",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f23:8"
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
      "definition_site": "00572670",
      "incomplete_value": true,
      "site": "00572680",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:16a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572350",
      "incomplete_value": true,
      "site": "00572360",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9f:8"
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
      "definition_site": "00572684",
      "incomplete_value": true,
      "site": "00572684",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00572364",
      "incomplete_value": true,
      "site": "00572364",
      "value": [
        "LOAD",
        "8",
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
      "00572650",
      "READ",
      [
        "storage",
        "002bff23",
        null,
        "string"
      ]
    ],
    [
      "00572670",
      "READ",
      [
        "storage",
        "002a209f",
        null,
        "string"
      ]
    ],
    [
      "00572678",
      "READ",
      [
        "storage",
        "002a20ad",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00572650",
      "READ",
      [
        "storage",
        "002bff6d",
        null,
        "string"
      ]
    ],
    [
      "00572670",
      "READ",
      [
        "storage",
        "002a216a",
        null,
        "string"
      ]
    ],
    [
      "00572678",
      "READ",
      [
        "storage",
        "002a2178",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00572318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005722ec.md#insn-00572318) · [`00572320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005722ec.md#insn-00572320) · [`00572328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005722ec.md#insn-00572328)
- 新版 [`00572638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/0057260c.md#insn-00572638) · [`00572640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/0057260c.md#insn-00572640) · [`00572648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/0057260c.md#insn-00572648)

~~~diff
- 00572318 ["INT_ADD", "register:40f0:8", ["const:572318:8", "const:4:8"]]
- 00572318 ["CALL", null, ["callee:005891cc:8"]]
+ 00572638 ["INT_ADD", "register:40f0:8", ["const:572638:8", "const:4:8"]]
+ 00572638 ["CALL", null, ["callee:005891cc:8"]]
- 00572318 bytes e55a0094
+ 00572638 bytes e55a0094
- 00572320 ["INT_ADD", "register:40f0:8", ["const:572320:8", "const:4:8"]]
- 00572320 ["CALL", null, ["callee:005894bc:8"]]
+ 00572640 ["INT_ADD", "register:40f0:8", ["const:572640:8", "const:4:8"]]
+ 00572640 ["CALL", null, ["callee:005894bc:8"]]
- 00572320 bytes 9f5b0094
+ 00572640 bytes 9f5b0094
- 00572328 ["COPY", "tmp:0:8", ["const:f23:8"]]
- 00572328 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00572328 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00572328 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00572648 ["COPY", "tmp:0:8", ["const:f6d:8"]]
+ 00572648 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00572648 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00572648 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00572328 bytes 298d3c91
+ 00572648 bytes 29b53d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8f5b9ed499d930515bd150076b60b99"></a>

### [`005724a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005724a0.md) → [`005727c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/005727c0.md) FUN_005727c0

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005509e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509e0.md) · 呼出先 19件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00574dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574dc8.md)
- 新版 呼出元 1件 [`00550d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d00.md) · 呼出先 19件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005750e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005750e8.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 92.44% / 新版 92.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0057283c",
      "incomplete_value": true,
      "site": "0057284c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:105:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057251c",
      "incomplete_value": true,
      "site": "0057252c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:36:8"
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
      "definition_site": "00572850",
      "incomplete_value": true,
      "site": "00572850",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00572530",
      "incomplete_value": true,
      "site": "00572530",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00572844",
      "incomplete_value": true,
      "site": "00572854",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00572524",
      "incomplete_value": true,
      "site": "00572534",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0057283c",
      "READ",
      [
        "storage",
        "002b9036",
        null,
        "string"
      ]
    ],
    [
      "00572840",
      "READ",
      [
        "storage",
        "002b9045",
        null,
        "string"
      ]
    ],
    [
      "00572844",
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
      "0057283c",
      "READ",
      [
        "storage",
        "002b9105",
        null,
        "string"
      ]
    ],
    [
      "00572840",
      "READ",
      [
        "storage",
        "002b9114",
        null,
        "string"
      ]
    ],
    [
      "00572844",
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

- 旧版 [`00572598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005724a0.md#insn-00572598) · [`00572614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005724a0.md#insn-00572614) · [`005724d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005724a0.md#insn-005724d4)
- 新版 [`005728b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/005727c0.md#insn-005728b8) · [`00572934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/005727c0.md#insn-00572934) · [`005727f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/005727c0.md#insn-005727f4)

~~~diff
- 00572598 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:2b8:8"]]
- 00572598 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
+ 005728b8 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:278:8"]]
+ 005728b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
- 00572598 bytes 54b902b9
+ 005728b8 bytes 547902b9
- 00572614 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
- 00572614 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00572934 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:260:8"]]
+ 00572934 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00572614 bytes 095101f9
+ 00572934 bytes 093101f9
- 005724d4 ["INT_ADD", "register:40f0:8", ["const:5724d4:8", "const:4:8"]]
- 005724d4 ["CALL", null, ["callee:005891cc:8"]]
+ 005727f4 ["INT_ADD", "register:40f0:8", ["const:5727f4:8", "const:4:8"]]
+ 005727f4 ["CALL", null, ["callee:005891cc:8"]]
- 005724d4 bytes 765a0094
+ 005727f4 bytes 765a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e60a763e5fd1bf669cfd0017ddcfde9d"></a>

### [`005728f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005728f4.md) → [`00572c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572c14.md) FUN_00572c14

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005509e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509e4.md) · 呼出先 8件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`00550d04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d04.md) · 呼出先 8件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00572c60",
      "incomplete_value": true,
      "site": "00572c60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dda:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572940",
      "incomplete_value": true,
      "site": "00572940",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d0d:8"
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
      "00572c50",
      "READ",
      [
        "storage",
        "002a9d0d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00572c50",
      "READ",
      [
        "storage",
        "002a9dda",
        null,
        "string"
      ]
    ],
    [
      "00572c78",
      "DATA",
      [
        "storage",
        "00562928",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00572914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005728f4.md#insn-00572914) · [`0057291c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005728f4.md#insn-0057291c) · [`00572928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005728f4.md#insn-00572928)
- 新版 [`00572c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572c14.md#insn-00572c34) · [`00572c3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572c14.md#insn-00572c3c) · [`00572c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572c14.md#insn-00572c48)

~~~diff
- 00572914 ["INT_ADD", "register:40f0:8", ["const:572914:8", "const:4:8"]]
- 00572914 ["CALL", null, ["callee:005891cc:8"]]
+ 00572c34 ["INT_ADD", "register:40f0:8", ["const:572c34:8", "const:4:8"]]
+ 00572c34 ["CALL", null, ["callee:005891cc:8"]]
- 00572914 bytes 66590094
+ 00572c34 bytes 66590094
- 0057291c ["INT_ADD", "register:40f0:8", ["const:57291c:8", "const:4:8"]]
- 0057291c ["CALL", null, ["callee:005894bc:8"]]
+ 00572c3c ["INT_ADD", "register:40f0:8", ["const:572c3c:8", "const:4:8"]]
+ 00572c3c ["CALL", null, ["callee:005894bc:8"]]
- 0057291c bytes 205a0094
+ 00572c3c bytes 205a0094
- 00572928 ["COPY", "tmp:0:8", ["const:d0d:8"]]
- 00572928 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00572928 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00572928 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00572c48 ["COPY", "tmp:0:8", ["const:dda:8"]]
+ 00572c48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00572c48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00572c48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00572928 bytes 29353491
+ 00572c48 bytes 29693791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27504e99dee4b9fcec7f01abb06cd127"></a>

### [`00572a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572a24.md) → [`00572d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572d44.md) FUN_00572d44

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005509e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509e8.md) · 呼出先 11件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`00550d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d08.md) · 呼出先 11件 [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00572d80",
      "incomplete_value": true,
      "site": "00572d98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f77:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572a60",
      "incomplete_value": true,
      "site": "00572a78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f2d:8"
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
      "definition_site": "00572d9c",
      "incomplete_value": true,
      "site": "00572da8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572a7c",
      "incomplete_value": true,
      "site": "00572a88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cc5:8"
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
      "definition_site": "00572dac",
      "incomplete_value": true,
      "site": "00572dac",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00572a8c",
      "incomplete_value": true,
      "site": "00572a8c",
      "value": [
        "LOAD",
        "8",
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
      "00572d80",
      "READ",
      [
        "storage",
        "002bff2d",
        null,
        "string"
      ]
    ],
    [
      "00572d9c",
      "READ",
      [
        "storage",
        "002b3cc5",
        null,
        "string"
      ]
    ],
    [
      "00572da0",
      "READ",
      [
        "storage",
        "002b3cd2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00572d80",
      "READ",
      [
        "storage",
        "002bff77",
        null,
        "string"
      ]
    ],
    [
      "00572d9c",
      "READ",
      [
        "storage",
        "002b3da3",
        null,
        "string"
      ]
    ],
    [
      "00572da0",
      "READ",
      [
        "storage",
        "002b3db0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00572a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572a24.md#insn-00572a48) · [`00572a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572a24.md#insn-00572a50) · [`00572a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572a24.md#insn-00572a5c)
- 新版 [`00572d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572d44.md#insn-00572d68) · [`00572d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572d44.md#insn-00572d70) · [`00572d7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572d44.md#insn-00572d7c)

~~~diff
- 00572a48 ["INT_ADD", "register:40f0:8", ["const:572a48:8", "const:4:8"]]
- 00572a48 ["CALL", null, ["callee:005891cc:8"]]
+ 00572d68 ["INT_ADD", "register:40f0:8", ["const:572d68:8", "const:4:8"]]
+ 00572d68 ["CALL", null, ["callee:005891cc:8"]]
- 00572a48 bytes 19590094
+ 00572d68 bytes 19590094
- 00572a50 ["INT_ADD", "register:40f0:8", ["const:572a50:8", "const:4:8"]]
- 00572a50 ["CALL", null, ["callee:005894bc:8"]]
+ 00572d70 ["INT_ADD", "register:40f0:8", ["const:572d70:8", "const:4:8"]]
+ 00572d70 ["CALL", null, ["callee:005894bc:8"]]
- 00572a50 bytes d3590094
+ 00572d70 bytes d3590094
- 00572a5c ["COPY", "tmp:0:8", ["const:f2d:8"]]
- 00572a5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00572a5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00572a5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00572d7c ["COPY", "tmp:0:8", ["const:f77:8"]]
+ 00572d7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00572d7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00572d7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00572a5c bytes 29b53c91
+ 00572d7c bytes 29dd3d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fd8028618dad9bf34ac3d52608897e2"></a>

### [`00572be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572be0.md) → [`00572f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572f00.md) FUN_00572f00

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005509ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509ec.md) · 呼出先 2件 [`00574f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574f30.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00550d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d0c.md) · 呼出先 2件 [`00575250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575250.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00572f68",
      "incomplete_value": false,
      "site": "00572f74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca7000:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572c48",
      "incomplete_value": false,
      "site": "00572c54",
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
      "00572f68",
      "PARAM",
      [
        "storage",
        "00ca6270",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00572f68",
      "PARAM",
      [
        "storage",
        "00ca7230",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00572c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572be0.md#insn-00572c54) · [`00572c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572be0.md#insn-00572c18) · [`00572c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572be0.md#insn-00572c40)
- 新版 [`00572f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572f00.md#insn-00572f74) · [`00572f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572f00.md#insn-00572f38) · [`00572f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572f00.md#insn-00572f60)

~~~diff
- 00572c54 ["INT_ADD", "register:40f0:8", ["const:572c54:8", "const:4:8"]]
- 00572c54 ["CALL", null, ["callee:00575250:8"]]
+ 00572f74 ["INT_ADD", "register:40f0:8", ["const:572f74:8", "const:4:8"]]
+ 00572f74 ["CALL", null, ["callee:00575250:8"]]
- 00572c54 bytes b7080094
+ 00572f74 bytes b7080094
- 00572c18 ["COPY", "register:0:8", ["register:4048:8"]]
- 00572c18 ["INT_ADD", "register:40f0:8", ["const:572c18:8", "const:4:8"]]
- 00572c18 ["CALLIND", null, ["register:0:8"]]
+ 00572f38 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00572f38 ["INT_ADD", "register:40f0:8", ["const:572f38:8", "const:4:8"]]
+ 00572f38 ["CALLIND", null, ["register:0:8"]]
- 00572c18 bytes 20013fd6
+ 00572f38 bytes 20013fd6
- 00572c40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00572c40 ["INT_ADD", "register:40f0:8", ["const:572c40:8", "const:4:8"]]
- 00572c40 ["CALLIND", null, ["register:0:8"]]
+ 00572f60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00572f60 ["INT_ADD", "register:40f0:8", ["const:572f60:8", "const:4:8"]]
+ 00572f60 ["CALLIND", null, ["register:0:8"]]
- 00572c40 bytes 00013fd6
+ 00572f60 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-814b9d8bd2dc3a39a3f4f7c5404e9f9d"></a>

### [`00572ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572ca8.md) → [`00572fc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572fc8.md) Java_jp_co_ponos_battlecats_MyActivity_onIapList

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`005719ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005719ac.md) [`005744b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/005744b8.md) [`00575164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575164.md)
- 新版 呼出元 0件  · 呼出先 18件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00571ccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571ccc.md) [`005747d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/005747d8.md) [`00575484`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575484.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.32% / 新版 95.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_value` 10件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0057309c",
      "incomplete_value": false,
      "site": "0057309c",
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
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572d7c",
      "incomplete_value": false,
      "site": "00572d7c",
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
            "const:be0:8"
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
      "definition_site": "00573148",
      "incomplete_value": true,
      "site": "0057314c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00572e28",
      "incomplete_value": true,
      "site": "00572e2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005731d8",
      "incomplete_value": true,
      "site": "005731e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:31b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00572eb8",
      "incomplete_value": true,
      "site": "00572ec4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:250:8"
              ]
            ]
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
      "00573004",
      "READ",
      [
        "storage",
        "00ca62a8",
        null,
        "undefined8"
      ]
    ],
    [
      "0057309c",
      "DATA",
      [
        "storage",
        "00c6bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00573148",
      "READ",
      [
        "storage",
        "002c2a40",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00573004",
      "READ",
      [
        "storage",
        "00ca7268",
        null,
        "undefined8"
      ]
    ],
    [
      "0057309c",
      "DATA",
      [
        "storage",
        "00c6cbb0",
        null,
        "pointer"
      ]
    ],
    [
      "00573148",
      "READ",
      [
        "storage",
        "002c2a90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00572ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572ca8.md#insn-00572ce0) · [`0057314c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572ca8.md#insn-0057314c) · [`005731a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572ca8.md#insn-005731a4)
- 新版 [`00573000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572fc8.md#insn-00573000) · [`0057346c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572fc8.md#insn-0057346c) · [`005734c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572fc8.md#insn-005734c4)

~~~diff
- 00572ce0 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 00572ce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00572ce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00572ce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00573000 ["COPY", "tmp:0:8", ["const:268:8"]]
+ 00573000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00573000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00573000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00572ce0 bytes 08a10a91
+ 00573000 bytes 08a10991
- 0057314c ["INT_ADD", "register:40f0:8", ["const:57314c:8", "const:4:8"]]
- 0057314c ["CALL", null, ["callee:004413ec:8"]]
+ 0057346c ["INT_ADD", "register:40f0:8", ["const:57346c:8", "const:4:8"]]
+ 0057346c ["CALL", null, ["callee:004413ec:8"]]
- 0057314c bytes e037fb97
+ 0057346c bytes e037fb97
- 005731a4 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 005731a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005731a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005731a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005734c4 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 005734c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005734c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005734c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005731a4 bytes 08812991
+ 005734c4 bytes 08c12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e185f37913495ef4e87dfaeba43f0d7"></a>

### [`00573ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00573/00573ec0.md) → [`005741e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/005741e0.md) Java_jp_co_ponos_battlecats_MyActivity_onIapPurchases

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00571320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571320.md) [`0058a664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a664.md) [`0058a760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a760.md) [`0058a818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a818.md) [`0058a8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8fc.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00571640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571640.md) [`0058a984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a984.md) [`0058aa80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058aa80.md) [`0058ab38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ab38.md) [`0058ac1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ac1c.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 98.37% / 新版 98.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0057431c",
      "incomplete_value": true,
      "site": "0057431c",
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
      "definition_site": "00573ffc",
      "incomplete_value": true,
      "site": "00573ffc",
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
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00573ffc"
      ],
      [
        "FALL_THROUGH",
        "0057431c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "0057431c",
      "incomplete_value": true,
      "site": "00574320",
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
      "definition_site": "00573ffc",
      "incomplete_value": true,
      "site": "00574000",
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
    "ordinal": 15,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00574318",
      "READ",
      [
        "storage",
        "00ca6290",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00574318",
      "READ",
      [
        "storage",
        "00ca7250",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00573f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00573/00573ec0.md#insn-00573f00) · [`00573f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00573/00573ec0.md#insn-00573f0c) · [`00573f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00573/00573ec0.md#insn-00573f1c)
- 新版 [`00574220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/005741e0.md#insn-00574220) · [`0057422c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/005741e0.md#insn-0057422c) · [`0057423c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/005741e0.md#insn-0057423c)

~~~diff
- 00573f00 ["INT_ADD", "register:40f0:8", ["const:573f00:8", "const:4:8"]]
- 00573f00 ["CALL", null, ["callee:0058a984:8"]]
+ 00574220 ["INT_ADD", "register:40f0:8", ["const:574220:8", "const:4:8"]]
+ 00574220 ["CALL", null, ["callee:0058a984:8"]]
- 00573f00 bytes d9590094
+ 00574220 bytes d9590094
- 00573f0c ["INT_ADD", "register:40f0:8", ["const:573f0c:8", "const:4:8"]]
- 00573f0c ["CALL", null, ["callee:0058a984:8"]]
+ 0057422c ["INT_ADD", "register:40f0:8", ["const:57422c:8", "const:4:8"]]
+ 0057422c ["CALL", null, ["callee:0058a984:8"]]
- 00573f0c bytes d6590094
+ 0057422c bytes d6590094
- 00573f1c ["INT_ADD", "register:40f0:8", ["const:573f1c:8", "const:4:8"]]
- 00573f1c ["CALL", null, ["callee:0058ab38:8"]]
+ 0057423c ["INT_ADD", "register:40f0:8", ["const:57423c:8", "const:4:8"]]
+ 0057423c ["CALL", null, ["callee:0058ab38:8"]]
- 00573f1c bytes 3f5a0094
+ 0057423c bytes 3f5a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73679a6d114ecb37c5bb77babc3d5b3f"></a>

### [`00574120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574120.md) → [`00574440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574440.md) Java_jp_co_ponos_battlecats_MyActivity_onIapPurchases2

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00571320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571320.md) [`0058a664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a664.md) [`0058a760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a760.md) [`0058a818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a818.md) [`0058a8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8fc.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00571640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571640.md) [`0058a984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058a984.md) [`0058aa80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058aa80.md) [`0058ab38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ab38.md) [`0058ac1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ac1c.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 98.74% / 新版 98.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005745d8",
      "incomplete_value": true,
      "site": "005745d8",
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
      "definition_site": "005742b8",
      "incomplete_value": true,
      "site": "005742b8",
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "005742b8"
      ],
      [
        "FALL_THROUGH",
        "005745d8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "005745d8",
      "incomplete_value": true,
      "site": "005745dc",
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
      "definition_site": "005742b8",
      "incomplete_value": true,
      "site": "005742bc",
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
      "005745d4",
      "READ",
      [
        "storage",
        "00ca6290",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005745d4",
      "READ",
      [
        "storage",
        "00ca7250",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574120.md#insn-00574168) · [`00574174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574120.md#insn-00574174) · [`0057418c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574120.md#insn-0057418c)
- 新版 [`00574488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574440.md#insn-00574488) · [`00574494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574440.md#insn-00574494) · [`005744ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574440.md#insn-005744ac)

~~~diff
- 00574168 ["INT_ADD", "register:40f0:8", ["const:574168:8", "const:4:8"]]
- 00574168 ["CALL", null, ["callee:0058a984:8"]]
+ 00574488 ["INT_ADD", "register:40f0:8", ["const:574488:8", "const:4:8"]]
+ 00574488 ["CALL", null, ["callee:0058a984:8"]]
- 00574168 bytes 3f590094
+ 00574488 bytes 3f590094
- 00574174 ["INT_ADD", "register:40f0:8", ["const:574174:8", "const:4:8"]]
- 00574174 ["CALL", null, ["callee:0058a984:8"]]
+ 00574494 ["INT_ADD", "register:40f0:8", ["const:574494:8", "const:4:8"]]
+ 00574494 ["CALL", null, ["callee:0058a984:8"]]
- 00574174 bytes 3c590094
+ 00574494 bytes 3c590094
- 0057418c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057418c ["INT_ADD", "register:40f0:8", ["const:57418c:8", "const:4:8"]]
- 0057418c ["CALLIND", null, ["register:0:8"]]
+ 005744ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 005744ac ["INT_ADD", "register:40f0:8", ["const:5744ac:8", "const:4:8"]]
+ 005744ac ["CALLIND", null, ["register:0:8"]]
- 0057418c bytes 00013fd6
+ 005744ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf94928df01d547fd67963e4c151f1c1"></a>

### [`00574424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574424.md) → [`00574744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574744.md) FUN_00574744

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
      "definition_site": "00574748",
      "incomplete_value": false,
      "site": "0057474c",
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
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574428",
      "incomplete_value": false,
      "site": "0057442c",
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
            "const:a60:8"
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
      "0057474c",
      "DATA",
      [
        "storage",
        "00c6ba60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057474c",
      "DATA",
      [
        "storage",
        "00c6ca30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574424.md#insn-00574424) · [`00574428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574424.md#insn-00574428)
- 新版 [`00574744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574744.md#insn-00574744) · [`00574748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574744.md#insn-00574748)

~~~diff
- 00574424 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00574744 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00574424 bytes a83700f0
+ 00574744 bytes c8370090
- 00574428 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 00574428 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00574428 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00574428 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574748 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 00574748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00574428 bytes 08812991
+ 00574748 bytes 08c12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d046c09afd08f273a3d7383da1e41ca"></a>

### [`00574434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574434.md) → [`00574754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574754.md) FUN_00574754

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
      "definition_site": "00574764",
      "incomplete_value": false,
      "site": "0057476c",
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
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574444",
      "incomplete_value": false,
      "site": "0057444c",
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
            "const:a60:8"
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
      "0057476c",
      "DATA",
      [
        "storage",
        "00c6ba60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057476c",
      "DATA",
      [
        "storage",
        "00c6ca30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574434.md#insn-00574440) · [`00574444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574434.md#insn-00574444) · [`00574450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574434.md#insn-00574450)
- 新版 [`00574760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574754.md#insn-00574760) · [`00574764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574754.md#insn-00574764) · [`00574770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574754.md#insn-00574770)

~~~diff
- 00574440 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00574760 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00574440 bytes a83700f0
+ 00574760 bytes c8370090
- 00574444 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 00574444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00574444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00574444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574764 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 00574764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00574444 bytes 08812991
+ 00574764 bytes 08c12891
- 00574450 ["INT_ADD", "register:40f0:8", ["const:574450:8", "const:4:8"]]
- 00574450 ["CALL", null, ["callee:00c58f40:8"]]
+ 00574770 ["INT_ADD", "register:40f0:8", ["const:574770:8", "const:4:8"]]
+ 00574770 ["CALL", null, ["callee:00c58f40:8"]]
- 00574450 bytes c88e1b94
+ 00574770 bytes f4911b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0ff45efbeeb39b419f11183487031e3"></a>

### [`005744b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/005744b8.md) → [`005747d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/005747d8.md) FUN_005747d8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00572ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572ca8.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)
- 新版 呼出元 1件 [`00572fc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572fc8.md) · 呼出先 1件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00574808",
      "incomplete_value": true,
      "site": "00574808",
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
      "definition_site": "005744e8",
      "incomplete_value": true,
      "site": "005744e8",
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
      "00574808",
      "DATA",
      [
        "storage",
        "00c6bab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574808",
      "DATA",
      [
        "storage",
        "00c6ca80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005744d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/005744b8.md#insn-005744d4) · [`005744d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/005744b8.md#insn-005744d8) · [`00574520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/005744b8.md#insn-00574520)
- 新版 [`005747f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/005747d8.md#insn-005747f4) · [`005747f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/005747d8.md#insn-005747f8) · [`00574840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/005747d8.md#insn-00574840)

~~~diff
- 005744d4 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 005747f4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 005744d4 bytes a83700f0
+ 005747f4 bytes c8370090
- 005744d8 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 005744d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005744d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005744d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005747f8 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 005747f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005747f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005747f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005744d8 bytes 08c12a91
+ 005747f8 bytes 08012a91
- 00574520 ["INT_ADD", "register:40f0:8", ["const:574520:8", "const:4:8"]]
- 00574520 ["CALL", null, ["callee:0043be80:8"]]
+ 00574840 ["INT_ADD", "register:40f0:8", ["const:574840:8", "const:4:8"]]
+ 00574840 ["CALL", null, ["callee:0043be80:8"]]
- 00574520 bytes 901dfb97
+ 00574840 bytes 901dfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4cd4805d18bf40d9aef1c63745647d2"></a>

### [`00574768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574768.md) → [`00574a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574a88.md) FUN_00574a88

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00574464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574464.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00574784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574784.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00574aa0",
      "incomplete_value": false,
      "site": "00574aa4",
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
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574780",
      "incomplete_value": false,
      "site": "00574784",
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
            "const:ab0:8"
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
      "00574aa4",
      "DATA",
      [
        "storage",
        "00c6bab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574aa4",
      "DATA",
      [
        "storage",
        "00c6ca80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057477c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574768.md#insn-0057477c) · [`00574780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574768.md#insn-00574780) · [`005747bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574768.md#insn-005747bc)
- 新版 [`00574a9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574a88.md#insn-00574a9c) · [`00574aa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574a88.md#insn-00574aa0) · [`00574adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574a88.md#insn-00574adc)

~~~diff
- 0057477c ["COPY", "register:4048:8", ["const:c6b000:8"]]
+ 00574a9c ["COPY", "register:4048:8", ["const:c6c000:8"]]
- 0057477c bytes a93700f0
+ 00574a9c bytes c9370090
- 00574780 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 00574780 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00574780 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00574780 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00574aa0 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 00574aa0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00574aa0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00574aa0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00574780 bytes 29c12a91
+ 00574aa0 bytes 29012a91
- 005747bc ["INT_ADD", "register:40f0:8", ["const:5747bc:8", "const:4:8"]]
- 005747bc ["CALL", null, ["callee:00c58f50:8"]]
+ 00574adc ["INT_ADD", "register:40f0:8", ["const:574adc:8", "const:4:8"]]
+ 00574adc ["CALL", null, ["callee:00c58f50:8"]]
- 005747bc bytes f18d1b94
+ 00574adc bytes 1d911b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0c9b63b73a12691d03ea4cc44a2b72d"></a>

### [`00574808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574808.md) → [`00574b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574b28.md) FUN_00574b28

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00574b2c",
      "incomplete_value": true,
      "site": "00574b30",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057480c",
      "incomplete_value": true,
      "site": "00574810",
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
            "const:b18:8"
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
      "00574b30",
      "DATA",
      [
        "storage",
        "00c6bb18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574b30",
      "DATA",
      [
        "storage",
        "00c6cae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574808.md#insn-00574808) · [`0057480c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574808.md#insn-0057480c)
- 新版 [`00574b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574b28.md#insn-00574b28) · [`00574b2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574b28.md#insn-00574b2c)

~~~diff
- 00574808 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00574b28 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00574808 bytes a83700f0
+ 00574b28 bytes c8370090
- 0057480c ["COPY", "tmp:0:8", ["const:b18:8"]]
- 0057480c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057480c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057480c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574b2c ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 00574b2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574b2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574b2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057480c bytes 08612c91
+ 00574b2c bytes 08a12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d572238b60089a7139fad444ca96c95"></a>

### [`00574818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574818.md) → [`00574b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574b38.md) FUN_00574b38

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
      "definition_site": "00574b48",
      "incomplete_value": false,
      "site": "00574b50",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574828",
      "incomplete_value": false,
      "site": "00574830",
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
            "const:b18:8"
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
      "00574b50",
      "DATA",
      [
        "storage",
        "00c6bb18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574b50",
      "DATA",
      [
        "storage",
        "00c6cae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574818.md#insn-00574824) · [`00574828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574818.md#insn-00574828) · [`00574834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574818.md#insn-00574834)
- 新版 [`00574b44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574b38.md#insn-00574b44) · [`00574b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574b38.md#insn-00574b48) · [`00574b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574b38.md#insn-00574b54)

~~~diff
- 00574824 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00574b44 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00574824 bytes a83700f0
+ 00574b44 bytes c8370090
- 00574828 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 00574828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00574828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00574828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574b48 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 00574b48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574b48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574b48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00574828 bytes 08612c91
+ 00574b48 bytes 08a12b91
- 00574834 ["INT_ADD", "register:40f0:8", ["const:574834:8", "const:4:8"]]
- 00574834 ["CALL", null, ["callee:00c58f40:8"]]
+ 00574b54 ["INT_ADD", "register:40f0:8", ["const:574b54:8", "const:4:8"]]
+ 00574b54 ["CALL", null, ["callee:00c58f40:8"]]
- 00574834 bytes cf8d1b94
+ 00574b54 bytes fb901b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37eb063be4d7c040526c13847ced5eac"></a>

### [`0057489c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/0057489c.md) → [`00574bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574bbc.md) FUN_00574bbc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00571320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571320.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 1件 [`00571640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571640.md) · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00574be0",
      "incomplete_value": false,
      "site": "00574be0",
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
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005748c0",
      "incomplete_value": false,
      "site": "005748c0",
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
            "const:b68:8"
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
      "00574be0",
      "DATA",
      [
        "storage",
        "00c6bb68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574be0",
      "DATA",
      [
        "storage",
        "00c6cb38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005748b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/0057489c.md#insn-005748b4) · [`005748b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/0057489c.md#insn-005748b8) · [`005748bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/0057489c.md#insn-005748bc)
- 新版 [`00574bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574bbc.md#insn-00574bd4) · [`00574bd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574bbc.md#insn-00574bd8)

~~~diff
- 005748b4 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00574bd4 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 005748b4 bytes a83700f0
+ 00574bd4 bytes c8370090
- 005748b8 ["COPY", "tmp:0:8", ["const:b68:8"]]
- 005748b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005748b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005748b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574bd8 ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 00574bd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574bd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574bd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005748b8 bytes 08a12d91
+ 00574bd8 bytes 08e12c91
- 005748bc ["COPY", "register:40a8:8", ["register:4000:8"]]
- 005748bc bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cb20bf8308dc06ceddbd8702a60bd05"></a>

### [`00574b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574b0c.md) → [`00574e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574e2c.md) FUN_00574e2c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00574848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574848.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00574b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574b68.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00574e44",
      "incomplete_value": false,
      "site": "00574e48",
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
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574b24",
      "incomplete_value": false,
      "site": "00574b28",
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
            "const:b68:8"
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
      "00574e48",
      "DATA",
      [
        "storage",
        "00c6bb68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574e48",
      "DATA",
      [
        "storage",
        "00c6cb38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574b0c.md#insn-00574b20) · [`00574b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574b0c.md#insn-00574b24) · [`00574b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574b0c.md#insn-00574b38)
- 新版 [`00574e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574e2c.md#insn-00574e40) · [`00574e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574e2c.md#insn-00574e44) · [`00574e58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574e2c.md#insn-00574e58)

~~~diff
- 00574b20 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00574e40 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00574b20 bytes a83700f0
+ 00574e40 bytes c8370090
- 00574b24 ["COPY", "tmp:0:8", ["const:b68:8"]]
- 00574b24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00574b24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00574b24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574e44 ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 00574e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00574b24 bytes 08a12d91
+ 00574e44 bytes 08e12c91
- 00574b38 ["INT_ADD", "register:40f0:8", ["const:574b38:8", "const:4:8"]]
- 00574b38 ["CALL", null, ["callee:00c54d90:8"]]
+ 00574e58 ["INT_ADD", "register:40f0:8", ["const:574e58:8", "const:4:8"]]
+ 00574e58 ["CALL", null, ["callee:00c54d90:8"]]
- 00574b38 bytes 9a7c1b94
+ 00574e58 bytes ce7f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36a0ebd45dcb8689ca3e68cde8499c41"></a>

### [`00574be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574be4.md) → [`00574f04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574f04.md) FUN_00574f04

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00573ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00573/00573ba0.md) · 呼出先 2件 [`0059769c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059769c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00573ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00573/00573ec0.md) · 呼出先 2件 [`005979bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005979bc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00574f2c",
      "incomplete_value": false,
      "site": "00574f34",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574c0c",
      "incomplete_value": false,
      "site": "00574c14",
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
            "const:b18:8"
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
      "definition_site": "00574f40",
      "incomplete_value": false,
      "site": "00574f40",
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
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00574c20",
      "incomplete_value": false,
      "site": "00574c20",
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
            "const:b68:8"
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
      "00574f34",
      "DATA",
      [
        "storage",
        "00c6bb18",
        null,
        "undefined *"
      ]
    ],
    [
      "00574f40",
      "DATA",
      [
        "storage",
        "00c6bb68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00574f34",
      "DATA",
      [
        "storage",
        "00c6cae8",
        null,
        "undefined *"
      ]
    ],
    [
      "00574f40",
      "DATA",
      [
        "storage",
        "00c6cb38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00574c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574be4.md#insn-00574c04) · [`00574c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574be4.md#insn-00574c08) · [`00574c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574be4.md#insn-00574c0c)
- 新版 [`00574f24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574f04.md#insn-00574f24) · [`00574f28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574f04.md#insn-00574f28) · [`00574f2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00574/00574f04.md#insn-00574f2c)

~~~diff
- 00574c04 ["INT_ADD", "register:40f0:8", ["const:574c04:8", "const:4:8"]]
- 00574c04 ["CALL", null, ["callee:00c58f30:8"]]
+ 00574f24 ["INT_ADD", "register:40f0:8", ["const:574f24:8", "const:4:8"]]
+ 00574f24 ["CALL", null, ["callee:00c58f30:8"]]
- 00574c04 bytes d78c1b94
+ 00574f24 bytes 03901b94
- 00574c08 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00574f28 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00574c08 bytes a83700f0
+ 00574f28 bytes c8370090
- 00574c0c ["COPY", "tmp:0:8", ["const:b18:8"]]
- 00574c0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00574c0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00574c0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00574f2c ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 00574f2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00574f2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00574f2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00574c0c bytes 08612c91
+ 00574f2c bytes 08a12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c8f6c2d36ada12a8f98e0a4d40b3443"></a>

### [`00575384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575384.md) → [`005756a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005756a4.md) FUN_005756a4

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00575228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575228.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`00575548`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575548.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "005756b0",
      "incomplete_value": false,
      "site": "005756b4",
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
      "definition_site": "00575390",
      "incomplete_value": false,
      "site": "00575394",
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
      "005756b0",
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
      "005756b0",
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

- 旧版 [`00575394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575384.md#insn-00575394) · [`0057538c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575384.md#insn-0057538c) · [`00575390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575384.md#insn-00575390)
- 新版 [`005756b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005756a4.md#insn-005756b4) · [`005756ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005756a4.md#insn-005756ac) · [`005756b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005756a4.md#insn-005756b0)

~~~diff
- 00575394 ["INT_ADD", "register:40f0:8", ["const:575394:8", "const:4:8"]]
- 00575394 ["CALL", null, ["callee:0043bad8:8"]]
+ 005756b4 ["INT_ADD", "register:40f0:8", ["const:5756b4:8", "const:4:8"]]
+ 005756b4 ["CALL", null, ["callee:0043bad8:8"]]
- 00575394 bytes 0919fb97
+ 005756b4 bytes 0919fb97
- 0057538c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 005756ac ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0057538c bytes 00eaffd0
+ 005756ac bytes 00eafff0
- 00575390 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00575390 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00575390 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00575390 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005756b0 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 005756b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005756b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005756b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00575390 bytes 00303e91
+ 005756b0 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-500e032ad47bcb0d400c1d9092389f2a"></a>

### [`00575398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575398.md) → [`005756b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005756b8.md) _INIT_29

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00571808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571808.md) [`00571838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00571b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571b28.md) [`00571b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571b58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 45.83% / 新版 45.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005756e0",
      "incomplete_value": false,
      "site": "005756e0",
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
                "const:ca7000:8"
              ],
              [
                "leaf",
                "const:230:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005753c0",
      "incomplete_value": false,
      "site": "005753c0",
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
                "const:270:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
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
      "definition_site": "005756fc",
      "incomplete_value": false,
      "site": "005756fc",
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
                "const:ca7000:8"
              ],
              [
                "leaf",
                "const:260:8"
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
      "definition_site": "005753dc",
      "incomplete_value": false,
      "site": "005753dc",
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
                "const:2a0:8"
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00575700",
      "incomplete_value": false,
      "site": "00575700",
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
                "const:ca7000:8"
              ],
              [
                "leaf",
                "const:260:8"
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
      "definition_site": "005753e0",
      "incomplete_value": false,
      "site": "005753e0",
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
                "const:2a0:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005756d0",
      "PARAM",
      [
        "storage",
        "00ca6270",
        null,
        null
      ]
    ],
    [
      "005756d8",
      "PARAM",
      [
        "storage",
        "00571808",
        null,
        null
      ]
    ],
    [
      "005756dc",
      "PARAM",
      [
        "storage",
        "00c63060",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005756d0",
      "PARAM",
      [
        "storage",
        "00ca7230",
        null,
        null
      ]
    ],
    [
      "005756d8",
      "PARAM",
      [
        "storage",
        "00571b28",
        null,
        null
      ]
    ],
    [
      "005756dc",
      "PARAM",
      [
        "storage",
        "00c64030",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005753c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575398.md#insn-005753c4) · [`005753a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575398.md#insn-005753a4) · [`005753a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575398.md#insn-005753a8)
- 新版 [`005756e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005756b8.md#insn-005756e4) · [`005756c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005756b8.md#insn-005756c4) · [`005756c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005756b8.md#insn-005756c8)

~~~diff
- 005753c4 ["INT_ADD", "register:40f0:8", ["const:5753c4:8", "const:4:8"]]
- 005753c4 ["CALL", null, ["callee:00c58ed0:8"]]
+ 005756e4 ["INT_ADD", "register:40f0:8", ["const:5756e4:8", "const:4:8"]]
+ 005756e4 ["CALL", null, ["callee:00c58ed0:8"]]
- 005753c4 bytes cf8a1b94
+ 005756e4 bytes fb8d1b94
- 005753a4 ["COPY", "register:4098:8", ["const:c63000:8"]]
+ 005756c4 ["COPY", "register:4098:8", ["const:c64000:8"]]
- 005753a4 bytes 733700d0
+ 005756c4 bytes 733700f0
- 005753a8 ["COPY", "tmp:0:8", ["const:60:8"]]
- 005753a8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005753a8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005753a8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005756c8 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 005756c8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005756c8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005756c8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005753a8 bytes 73820191
+ 005756c8 bytes 73c20091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb19494b5c9587f628cd5eedea39e44b"></a>

### [`00575458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575458.md) → [`00575778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575778.md) FUN_00575778

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509f0.md) · 呼出先 11件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`00550d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d10.md) · 呼出先 11件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.04% / 新版 89.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005757bc",
      "incomplete_value": true,
      "site": "005757d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:79d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057549c",
      "incomplete_value": true,
      "site": "005754b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:645:8"
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
      "definition_site": "005757d8",
      "incomplete_value": true,
      "site": "005757e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:56b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005754b8",
      "incomplete_value": true,
      "site": "005754c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:48d:8"
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
      "definition_site": "005757e8",
      "incomplete_value": true,
      "site": "005757e8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005754c8",
      "incomplete_value": true,
      "site": "005754c8",
      "value": [
        "LOAD",
        "8",
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
      "005757bc",
      "READ",
      [
        "storage",
        "002a5645",
        null,
        "string"
      ]
    ],
    [
      "005757d8",
      "READ",
      [
        "storage",
        "002bb48d",
        null,
        "string"
      ]
    ],
    [
      "005757dc",
      "READ",
      [
        "storage",
        "002bb49a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005757bc",
      "READ",
      [
        "storage",
        "002a579d",
        null,
        "string"
      ]
    ],
    [
      "005757d8",
      "READ",
      [
        "storage",
        "002bb56b",
        null,
        "string"
      ]
    ],
    [
      "005757dc",
      "READ",
      [
        "storage",
        "002bb578",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057547c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575458.md#insn-0057547c) · [`00575484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575458.md#insn-00575484) · [`00575490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575458.md#insn-00575490)
- 新版 [`0057579c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575778.md#insn-0057579c) · [`005757a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575778.md#insn-005757a4) · [`005757b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575778.md#insn-005757b0)

~~~diff
- 0057547c ["INT_ADD", "register:40f0:8", ["const:57547c:8", "const:4:8"]]
- 0057547c ["CALL", null, ["callee:005891cc:8"]]
+ 0057579c ["INT_ADD", "register:40f0:8", ["const:57579c:8", "const:4:8"]]
+ 0057579c ["CALL", null, ["callee:005891cc:8"]]
- 0057547c bytes 8c4e0094
+ 0057579c bytes 8c4e0094
- 00575484 ["INT_ADD", "register:40f0:8", ["const:575484:8", "const:4:8"]]
- 00575484 ["CALL", null, ["callee:005894bc:8"]]
+ 005757a4 ["INT_ADD", "register:40f0:8", ["const:5757a4:8", "const:4:8"]]
+ 005757a4 ["CALL", null, ["callee:005894bc:8"]]
- 00575484 bytes 464f0094
+ 005757a4 bytes 464f0094
- 00575490 ["COPY", "tmp:0:8", ["const:645:8"]]
- 00575490 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00575490 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00575490 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005757b0 ["COPY", "tmp:0:8", ["const:79d:8"]]
+ 005757b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005757b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005757b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00575490 bytes 29151991
+ 005757b0 bytes 29751e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0321c2f36ae676d1b5d54362295ad9c7"></a>

### [`005755c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/005755c8.md) → [`005758e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005758e8.md) FUN_005758e8

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005509f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509f4.md) · 呼出先 14件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00575dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575dcc.md) [`00575fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575fd8.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md)
- 新版 呼出元 1件 [`00550d14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d14.md) · 呼出先 14件 [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`005760ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005760ec.md) [`005762f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005762f8.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.40% / 新版 82.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00575938",
      "incomplete_value": true,
      "site": "00575948",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:3c5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00575618",
      "incomplete_value": true,
      "site": "00575628",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:2fa:8"
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
      "definition_site": "00575958",
      "incomplete_value": true,
      "site": "00575958",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00575638",
      "incomplete_value": true,
      "site": "00575638",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057594c",
      "incomplete_value": true,
      "site": "00575960",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057562c",
      "incomplete_value": true,
      "site": "00575640",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00575938",
      "READ",
      [
        "storage",
        "002a42fa",
        null,
        "string"
      ]
    ],
    [
      "0057593c",
      "READ",
      [
        "storage",
        "002a4309",
        null,
        "string"
      ]
    ],
    [
      "0057594c",
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
      "00575938",
      "READ",
      [
        "storage",
        "002a43c5",
        null,
        "string"
      ]
    ],
    [
      "0057593c",
      "READ",
      [
        "storage",
        "002a43d4",
        null,
        "string"
      ]
    ],
    [
      "0057594c",
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

- 旧版 [`0057573c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/005755c8.md#insn-0057573c) · [`00575760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/005755c8.md#insn-00575760) · [`00575784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/005755c8.md#insn-00575784)
- 新版 [`00575a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005758e8.md#insn-00575a5c) · [`00575a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005758e8.md#insn-00575a80) · [`00575aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/005758e8.md#insn-00575aa4)

~~~diff
- 0057573c ["INT_ADD", "register:40f0:8", ["const:57573c:8", "const:4:8"]]
- 0057573c ["CALL", null, ["callee:005762f8:8"]]
+ 00575a5c ["INT_ADD", "register:40f0:8", ["const:575a5c:8", "const:4:8"]]
+ 00575a5c ["CALL", null, ["callee:005762f8:8"]]
- 0057573c bytes 27020094
+ 00575a5c bytes 27020094
- 00575760 ["INT_ADD", "register:40f0:8", ["const:575760:8", "const:4:8"]]
- 00575760 ["CALL", null, ["callee:005760ec:8"]]
+ 00575a80 ["INT_ADD", "register:40f0:8", ["const:575a80:8", "const:4:8"]]
+ 00575a80 ["CALL", null, ["callee:005760ec:8"]]
- 00575760 bytes 9b010094
+ 00575a80 bytes 9b010094
- 00575784 ["INT_ADD", "register:40f0:8", ["const:575784:8", "const:4:8"]]
- 00575784 ["CALL", null, ["callee:005760ec:8"]]
+ 00575aa4 ["INT_ADD", "register:40f0:8", ["const:575aa4:8", "const:4:8"]]
+ 00575aa4 ["CALL", null, ["callee:005760ec:8"]]
- 00575784 bytes 92010094
+ 00575aa4 bytes 92010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc13f66a7364ddfe2666fd86e34ea1ac"></a>

### [`00575810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575810.md) → [`00575b30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575b30.md) FUN_00575b30

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005509f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509f8.md) · 呼出先 10件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00576190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576190.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)
- 新版 呼出元 1件 [`00550d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d18.md) · 呼出先 10件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005764b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005764b0.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.72% / 新版 90.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00575b78",
      "incomplete_value": true,
      "site": "00575b88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:581:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00575858",
      "incomplete_value": true,
      "site": "00575868",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4a3:8"
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
      "definition_site": "00575b7c",
      "incomplete_value": true,
      "site": "00575ba0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0057585c",
      "incomplete_value": true,
      "site": "00575880",
      "value": [
        "LOAD",
        "16",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00575b8c",
      "incomplete_value": true,
      "site": "00575ba4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0057586c",
      "incomplete_value": true,
      "site": "00575884",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00575b78",
      "READ",
      [
        "storage",
        "002bb4a3",
        null,
        "string"
      ]
    ],
    [
      "00575b7c",
      "READ",
      [
        "storage",
        "002bb4b0",
        null,
        "string"
      ]
    ],
    [
      "00575b8c",
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
      "00575b78",
      "READ",
      [
        "storage",
        "002bb581",
        null,
        "string"
      ]
    ],
    [
      "00575b7c",
      "READ",
      [
        "storage",
        "002bb58e",
        null,
        "string"
      ]
    ],
    [
      "00575b8c",
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

- 旧版 [`00575834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575810.md#insn-00575834) · [`0057583c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575810.md#insn-0057583c) · [`00575848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575810.md#insn-00575848)
- 新版 [`00575b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575b30.md#insn-00575b54) · [`00575b5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575b30.md#insn-00575b5c) · [`00575b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575b30.md#insn-00575b68)

~~~diff
- 00575834 ["INT_ADD", "register:40f0:8", ["const:575834:8", "const:4:8"]]
- 00575834 ["CALL", null, ["callee:005891cc:8"]]
+ 00575b54 ["INT_ADD", "register:40f0:8", ["const:575b54:8", "const:4:8"]]
+ 00575b54 ["CALL", null, ["callee:005891cc:8"]]
- 00575834 bytes 9e4d0094
+ 00575b54 bytes 9e4d0094
- 0057583c ["INT_ADD", "register:40f0:8", ["const:57583c:8", "const:4:8"]]
- 0057583c ["CALL", null, ["callee:005894bc:8"]]
+ 00575b5c ["INT_ADD", "register:40f0:8", ["const:575b5c:8", "const:4:8"]]
+ 00575b5c ["CALL", null, ["callee:005894bc:8"]]
- 0057583c bytes 584e0094
+ 00575b5c bytes 584e0094
- 00575848 ["INT_ADD", "register:40f0:8", ["const:575848:8", "const:4:8"]]
- 00575848 ["CALL", null, ["callee:00c58f30:8"]]
+ 00575b68 ["INT_ADD", "register:40f0:8", ["const:575b68:8", "const:4:8"]]
+ 00575b68 ["CALL", null, ["callee:00c58f30:8"]]
- 00575848 bytes c6891b94
+ 00575b68 bytes f28c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a23643fa5fc5b82f6185ab55d9e87770"></a>

### [`005759d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/005759d0.md) → [`00575cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575cf0.md) FUN_00575cf0

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005509fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509fc.md) · 呼出先 13件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)
- 新版 呼出元 1件 [`00550d1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d1c.md) · 呼出先 13件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.54% / 新版 95.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00575d54",
      "incomplete_value": true,
      "site": "00575d6c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:3dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00575a34",
      "incomplete_value": true,
      "site": "00575a4c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:312:8"
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
      "00575d54",
      "READ",
      [
        "storage",
        "002a4312",
        null,
        "string"
      ]
    ],
    [
      "00575d88",
      "READ",
      [
        "storage",
        "002bff72",
        null,
        "string"
      ]
    ],
    [
      "00575d88",
      "READ",
      [
        "storage",
        "002bff82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00575d54",
      "READ",
      [
        "storage",
        "002a43dd",
        null,
        "string"
      ]
    ],
    [
      "00575d88",
      "READ",
      [
        "storage",
        "002bffbc",
        null,
        "string"
      ]
    ],
    [
      "00575d88",
      "READ",
      [
        "storage",
        "002bffcc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00575a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/005759d0.md#insn-00575a1c) · [`00575a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/005759d0.md#insn-00575a24) · [`00575a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/005759d0.md#insn-00575a2c)
- 新版 [`00575d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575cf0.md#insn-00575d3c) · [`00575d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575cf0.md#insn-00575d44) · [`00575d4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575cf0.md#insn-00575d4c)

~~~diff
- 00575a1c ["INT_ADD", "register:40f0:8", ["const:575a1c:8", "const:4:8"]]
- 00575a1c ["CALL", null, ["callee:005891cc:8"]]
+ 00575d3c ["INT_ADD", "register:40f0:8", ["const:575d3c:8", "const:4:8"]]
+ 00575d3c ["CALL", null, ["callee:005891cc:8"]]
- 00575a1c bytes 244d0094
+ 00575d3c bytes 244d0094
- 00575a24 ["INT_ADD", "register:40f0:8", ["const:575a24:8", "const:4:8"]]
- 00575a24 ["CALL", null, ["callee:005894bc:8"]]
+ 00575d44 ["INT_ADD", "register:40f0:8", ["const:575d44:8", "const:4:8"]]
+ 00575d44 ["CALL", null, ["callee:005894bc:8"]]
- 00575a24 bytes de4d0094
+ 00575d44 bytes de4d0094
- 00575a2c ["COPY", "tmp:0:8", ["const:312:8"]]
- 00575a2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00575a2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00575a2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00575d4c ["COPY", "tmp:0:8", ["const:3dd:8"]]
+ 00575d4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00575d4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00575d4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00575a2c bytes 29490c91
+ 00575d4c bytes 29750f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97b4446ae83da5a4b6928eb78cb556d1"></a>

### [`00576394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576394.md) → [`005766b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005766b4.md) _INIT_30

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`005753f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/005753f8.md) [`00575428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575428.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00575718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575718.md) [`00575748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/00575748.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005766dc",
      "incomplete_value": false,
      "site": "005766dc",
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
                "const:ca7000:8"
              ],
              [
                "leaf",
                "const:280:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005763bc",
      "incomplete_value": false,
      "site": "005763bc",
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
                "const:2c0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
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
      "definition_site": "005766f8",
      "incomplete_value": false,
      "site": "005766f8",
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
                "const:ca7000:8"
              ],
              [
                "leaf",
                "const:2b0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005763d8",
      "incomplete_value": false,
      "site": "005763d8",
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
                "const:2f0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
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
      "definition_site": "005766d4",
      "incomplete_value": false,
      "site": "005766e0",
      "value": [
        "leaf",
        "const:575718:8"
      ]
    },
    "old": {
      "definition_site": "005763b4",
      "incomplete_value": false,
      "site": "005763c0",
      "value": [
        "leaf",
        "const:5753f8:8"
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
      "005766cc",
      "PARAM",
      [
        "storage",
        "00ca62c0",
        null,
        null
      ]
    ],
    [
      "005766d4",
      "PARAM",
      [
        "storage",
        "005753f8",
        null,
        null
      ]
    ],
    [
      "005766d8",
      "PARAM",
      [
        "storage",
        "00c63060",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005766cc",
      "PARAM",
      [
        "storage",
        "00ca7280",
        null,
        null
      ]
    ],
    [
      "005766d4",
      "PARAM",
      [
        "storage",
        "00575718",
        null,
        null
      ]
    ],
    [
      "005766d8",
      "PARAM",
      [
        "storage",
        "00c64030",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005763c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576394.md#insn-005763c0) · [`005763a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576394.md#insn-005763a0) · [`005763a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576394.md#insn-005763a4)
- 新版 [`005766e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005766b4.md#insn-005766e0) · [`005766c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005766b4.md#insn-005766c0) · [`005766c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005766b4.md#insn-005766c4)

~~~diff
- 005763c0 ["INT_ADD", "register:40f0:8", ["const:5763c0:8", "const:4:8"]]
- 005763c0 ["CALL", null, ["callee:00c58ed0:8"]]
+ 005766e0 ["INT_ADD", "register:40f0:8", ["const:5766e0:8", "const:4:8"]]
+ 005766e0 ["CALL", null, ["callee:00c58ed0:8"]]
- 005763c0 bytes d0861b94
+ 005766e0 bytes fc891b94
- 005763a0 ["COPY", "register:4098:8", ["const:c63000:8"]]
+ 005766c0 ["COPY", "register:4098:8", ["const:c64000:8"]]
- 005763a0 bytes 733700b0
+ 005766c0 bytes 733700d0
- 005763a4 ["COPY", "tmp:0:8", ["const:60:8"]]
- 005763a4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005763a4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005763a4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005766c4 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 005766c4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005766c4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005766c4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005763a4 bytes 73820191
+ 005766c4 bytes 73c20091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f12015b259d4e88823144766793b1f50"></a>

### [`005763ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005763ec.md) → [`0057670c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/0057670c.md) FUN_0057670c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00550a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a08.md) · 呼出先 4件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 1件 [`00550d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d28.md) · 呼出先 4件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00576750",
      "incomplete_value": false,
      "site": "00576768",
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
            "const:325:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576430",
      "incomplete_value": false,
      "site": "00576448",
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
            "const:25a:8"
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
      "definition_site": "00576758",
      "incomplete_value": false,
      "site": "00576768",
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
            "const:335:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576438",
      "incomplete_value": false,
      "site": "00576448",
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
            "const:26a:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00576750",
      "PARAM",
      [
        "storage",
        "002a325a",
        null,
        "string"
      ]
    ],
    [
      "00576758",
      "PARAM",
      [
        "storage",
        "002a326a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00576750",
      "PARAM",
      [
        "storage",
        "002a3325",
        null,
        "string"
      ]
    ],
    [
      "00576758",
      "PARAM",
      [
        "storage",
        "002a3335",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005763ec.md#insn-00576448) · [`005763fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005763ec.md#insn-005763fc) · [`00576404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005763ec.md#insn-00576404)
- 新版 [`00576768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/0057670c.md#insn-00576768) · [`0057671c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/0057670c.md#insn-0057671c) · [`00576724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/0057670c.md#insn-00576724)

~~~diff
- 00576448 ["COPY", "register:0:8", ["register:4040:8"]]
- 00576448 ["INT_ADD", "register:40f0:8", ["const:576448:8", "const:4:8"]]
- 00576448 ["CALLIND", null, ["register:0:8"]]
+ 00576768 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00576768 ["INT_ADD", "register:40f0:8", ["const:576768:8", "const:4:8"]]
+ 00576768 ["CALLIND", null, ["register:0:8"]]
- 00576448 bytes 00013fd6
+ 00576768 bytes 00013fd6
- 005763fc ["INT_ADD", "register:40f0:8", ["const:5763fc:8", "const:4:8"]]
- 005763fc ["CALL", null, ["callee:005891cc:8"]]
+ 0057671c ["INT_ADD", "register:40f0:8", ["const:57671c:8", "const:4:8"]]
+ 0057671c ["CALL", null, ["callee:005891cc:8"]]
- 005763fc bytes ac4a0094
+ 0057671c bytes ac4a0094
- 00576404 ["INT_ADD", "register:40f0:8", ["const:576404:8", "const:4:8"]]
- 00576404 ["CALL", null, ["callee:005894bc:8"]]
+ 00576724 ["INT_ADD", "register:40f0:8", ["const:576724:8", "const:4:8"]]
+ 00576724 ["CALL", null, ["callee:005894bc:8"]]
- 00576404 bytes 664b0094
+ 00576724 bytes 664b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-655b2df7db0710b0f5e4b64b5740f2d1"></a>

### [`00576480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576480.md) → [`005767a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005767a0.md) FUN_005767a0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00550a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a0c.md) · 呼出先 4件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 1件 [`00550d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d2c.md) · 呼出先 4件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005767f0",
      "incomplete_value": false,
      "site": "00576808",
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
            "const:dcd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005764d0",
      "incomplete_value": false,
      "site": "005764e8",
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
            "const:cf6:8"
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
      "definition_site": "005767f8",
      "incomplete_value": false,
      "site": "00576808",
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
            "const:921:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005764d8",
      "incomplete_value": false,
      "site": "005764e8",
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
            "const:854:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005767f0",
      "PARAM",
      [
        "storage",
        "002b0cf6",
        null,
        "string"
      ]
    ],
    [
      "005767f8",
      "PARAM",
      [
        "storage",
        "002ad854",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005767f0",
      "PARAM",
      [
        "storage",
        "002b0dcd",
        null,
        "string"
      ]
    ],
    [
      "005767f8",
      "PARAM",
      [
        "storage",
        "002ad921",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005764e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576480.md#insn-005764e8) · [`0057649c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576480.md#insn-0057649c) · [`005764a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576480.md#insn-005764a4)
- 新版 [`00576808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005767a0.md#insn-00576808) · [`005767bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005767a0.md#insn-005767bc) · [`005767c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/005767a0.md#insn-005767c4)

~~~diff
- 005764e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005764e8 ["INT_ADD", "register:40f0:8", ["const:5764e8:8", "const:4:8"]]
- 005764e8 ["CALLIND", null, ["register:0:8"]]
+ 00576808 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00576808 ["INT_ADD", "register:40f0:8", ["const:576808:8", "const:4:8"]]
+ 00576808 ["CALLIND", null, ["register:0:8"]]
- 005764e8 bytes 00013fd6
+ 00576808 bytes 00013fd6
- 0057649c ["INT_ADD", "register:40f0:8", ["const:57649c:8", "const:4:8"]]
- 0057649c ["CALL", null, ["callee:005891cc:8"]]
+ 005767bc ["INT_ADD", "register:40f0:8", ["const:5767bc:8", "const:4:8"]]
+ 005767bc ["CALL", null, ["callee:005891cc:8"]]
- 0057649c bytes 844a0094
+ 005767bc bytes 844a0094
- 005764a4 ["INT_ADD", "register:40f0:8", ["const:5764a4:8", "const:4:8"]]
- 005764a4 ["CALL", null, ["callee:005894bc:8"]]
+ 005767c4 ["INT_ADD", "register:40f0:8", ["const:5767c4:8", "const:4:8"]]
+ 005767c4 ["CALL", null, ["callee:005894bc:8"]]
- 005764a4 bytes 3e4b0094
+ 005767c4 bytes 3e4b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e39c461623db9d6bb89a03b703be5bd1"></a>

### [`00576540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576540.md) → [`00576860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576860.md) FUN_00576860

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00550a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a38.md) · 呼出先 4件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 1件 [`00550d58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d58.md) · 呼出先 4件 [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005768a4",
      "incomplete_value": false,
      "site": "005768bc",
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
            "const:4b5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576584",
      "incomplete_value": false,
      "site": "0057659c",
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
            "const:3d7:8"
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
      "definition_site": "005768ac",
      "incomplete_value": false,
      "site": "005768bc",
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
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057658c",
      "incomplete_value": false,
      "site": "0057659c",
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
            "const:a33:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005768a4",
      "PARAM",
      [
        "storage",
        "002ba3d7",
        null,
        "string"
      ]
    ],
    [
      "005768ac",
      "PARAM",
      [
        "storage",
        "002aea33",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005768a4",
      "PARAM",
      [
        "storage",
        "002ba4b5",
        null,
        "string"
      ]
    ],
    [
      "005768ac",
      "PARAM",
      [
        "storage",
        "002aeb00",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0057659c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576540.md#insn-0057659c) · [`00576550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576540.md#insn-00576550) · [`00576558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576540.md#insn-00576558)
- 新版 [`005768bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576860.md#insn-005768bc) · [`00576870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576860.md#insn-00576870) · [`00576878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576860.md#insn-00576878)

~~~diff
- 0057659c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057659c ["INT_ADD", "register:40f0:8", ["const:57659c:8", "const:4:8"]]
- 0057659c ["CALLIND", null, ["register:0:8"]]
+ 005768bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005768bc ["INT_ADD", "register:40f0:8", ["const:5768bc:8", "const:4:8"]]
+ 005768bc ["CALLIND", null, ["register:0:8"]]
- 0057659c bytes 00013fd6
+ 005768bc bytes 00013fd6
- 00576550 ["INT_ADD", "register:40f0:8", ["const:576550:8", "const:4:8"]]
- 00576550 ["CALL", null, ["callee:005891cc:8"]]
+ 00576870 ["INT_ADD", "register:40f0:8", ["const:576870:8", "const:4:8"]]
+ 00576870 ["CALL", null, ["callee:005891cc:8"]]
- 00576550 bytes 574a0094
+ 00576870 bytes 574a0094
- 00576558 ["INT_ADD", "register:40f0:8", ["const:576558:8", "const:4:8"]]
- 00576558 ["CALL", null, ["callee:005894bc:8"]]
+ 00576878 ["INT_ADD", "register:40f0:8", ["const:576878:8", "const:4:8"]]
+ 00576878 ["CALL", null, ["callee:005894bc:8"]]
- 00576558 bytes 114b0094
+ 00576878 bytes 114b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2b8b2c18af9962fcbc3f617ff890ef3"></a>

### [`005765fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005765fc.md) → [`0057691c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/0057691c.md) FUN_0057691c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00550a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a3c.md) · 呼出先 8件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`00550d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d5c.md) · 呼出先 8件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

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
      "definition_site": "00576958",
      "incomplete_value": true,
      "site": "00576970",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576638",
      "incomplete_value": true,
      "site": "00576650",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f3c:8"
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
      "00576958",
      "READ",
      [
        "storage",
        "002b4f3c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00576958",
      "READ",
      [
        "storage",
        "002b501a",
        null,
        "string"
      ]
    ],
    [
      "00576974",
      "DATA",
      [
        "storage",
        "00562928",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005765fc.md#insn-00576618) · [`00576620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005765fc.md#insn-00576620) · [`00576628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005765fc.md#insn-00576628)
- 新版 [`00576938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/0057691c.md#insn-00576938) · [`00576940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/0057691c.md#insn-00576940) · [`00576948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/0057691c.md#insn-00576948)

~~~diff
- 00576618 ["INT_ADD", "register:40f0:8", ["const:576618:8", "const:4:8"]]
- 00576618 ["CALL", null, ["callee:005891cc:8"]]
+ 00576938 ["INT_ADD", "register:40f0:8", ["const:576938:8", "const:4:8"]]
+ 00576938 ["CALL", null, ["callee:005891cc:8"]]
- 00576618 bytes 254a0094
+ 00576938 bytes 254a0094
- 00576620 ["INT_ADD", "register:40f0:8", ["const:576620:8", "const:4:8"]]
- 00576620 ["CALL", null, ["callee:005894bc:8"]]
+ 00576940 ["INT_ADD", "register:40f0:8", ["const:576940:8", "const:4:8"]]
+ 00576940 ["CALL", null, ["callee:005894bc:8"]]
- 00576620 bytes df4a0094
+ 00576940 bytes df4a0094
- 00576628 ["COPY", "register:4048:8", ["const:2b4000:8"]]
+ 00576948 ["COPY", "register:4048:8", ["const:2b5000:8"]]
- 00576628 bytes e9e9ffd0
+ 00576948 bytes e9e9fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1332094c01b941c396be85b3ca547b08"></a>

### [`00576740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576740.md) → [`00576a60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576a60.md) FUN_00576a60

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00576868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576868.md) · 呼出先 7件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 1件 [`00576b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576b88.md) · 呼出先 7件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00576a88",
      "incomplete_value": true,
      "site": "00576a8c",
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
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576768",
      "incomplete_value": true,
      "site": "0057676c",
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
            "const:c30:8"
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
      "00576a8c",
      "DATA",
      [
        "storage",
        "00c6bc30",
        null,
        "undefined *"
      ]
    ],
    [
      "00576ab0",
      "READ",
      [
        "storage",
        "002a326e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00576a8c",
      "DATA",
      [
        "storage",
        "00c6cc00",
        null,
        "undefined *"
      ]
    ],
    [
      "00576ab0",
      "READ",
      [
        "storage",
        "002a3339",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576740.md#insn-00576764) · [`00576768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576740.md#insn-00576768) · [`00576770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576740.md#insn-00576770)
- 新版 [`00576a84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576a60.md#insn-00576a84) · [`00576a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576a60.md#insn-00576a88) · [`00576a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576a60.md#insn-00576a90)

~~~diff
- 00576764 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 00576a84 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00576764 bytes a83700b0
+ 00576a84 bytes a83700d0
- 00576768 ["COPY", "tmp:0:8", ["const:c30:8"]]
- 00576768 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00576768 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00576768 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00576a88 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 00576a88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00576a88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00576a88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00576768 bytes 08c13091
+ 00576a88 bytes 08013091
- 00576770 ["INT_ADD", "register:40f0:8", ["const:576770:8", "const:4:8"]]
- 00576770 ["CALL", null, ["callee:005891cc:8"]]
+ 00576a90 ["INT_ADD", "register:40f0:8", ["const:576a90:8", "const:4:8"]]
+ 00576a90 ["CALL", null, ["callee:005891cc:8"]]
- 00576770 bytes cf490094
+ 00576a90 bytes cf490094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c794455e4f1016c51a3a82834891245"></a>

### [`005769dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005769dc.md) → [`00576cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576cfc.md) FUN_00576cfc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00577358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577358.md) [`00577920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577920.md) [`00577cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577cc0.md) · 呼出先 10件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`0057be4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md)
- 新版 呼出元 3件 [`00577678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577678.md) [`00577c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577c40.md) [`00577fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577fe0.md) · 呼出先 10件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00576618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576618.md) [`0057c16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c16c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.81% / 新版 96.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00576d70",
      "incomplete_value": true,
      "site": "00576d70",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:59f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00576a50",
      "incomplete_value": true,
      "site": "00576a50",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:4c1:8"
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
      "definition_site": "00576d74",
      "incomplete_value": true,
      "site": "00576d74",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00576a54",
      "incomplete_value": true,
      "site": "00576a54",
      "value": [
        "LOAD",
        "8",
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
      "00576d60",
      "READ",
      [
        "storage",
        "002bb4c1",
        null,
        "string"
      ]
    ],
    [
      "00576d68",
      "READ",
      [
        "storage",
        "002bb4c7",
        null,
        "string"
      ]
    ],
    [
      "00576dd8",
      "READ",
      [
        "storage",
        "002c12fb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00576d60",
      "READ",
      [
        "storage",
        "002bb59f",
        null,
        "string"
      ]
    ],
    [
      "00576d68",
      "READ",
      [
        "storage",
        "002bb5a5",
        null,
        "string"
      ]
    ],
    [
      "00576dd8",
      "READ",
      [
        "storage",
        "002c1345",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005769dc.md#insn-00576a20) · [`00576a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005769dc.md#insn-00576a30) · [`00576a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005769dc.md#insn-00576a3c)
- 新版 [`00576d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576cfc.md#insn-00576d40) · [`00576d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576cfc.md#insn-00576d50) · [`00576d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576cfc.md#insn-00576d5c)

~~~diff
- 00576a20 ["INT_ADD", "register:40f0:8", ["const:576a20:8", "const:4:8"]]
- 00576a20 ["CALL", null, ["callee:005891cc:8"]]
+ 00576d40 ["INT_ADD", "register:40f0:8", ["const:576d40:8", "const:4:8"]]
+ 00576d40 ["CALL", null, ["callee:005891cc:8"]]
- 00576a20 bytes 23490094
+ 00576d40 bytes 23490094
- 00576a30 ["INT_ADD", "register:40f0:8", ["const:576a30:8", "const:4:8"]]
- 00576a30 ["CALL", null, ["callee:005894bc:8"]]
+ 00576d50 ["INT_ADD", "register:40f0:8", ["const:576d50:8", "const:4:8"]]
+ 00576d50 ["CALL", null, ["callee:005894bc:8"]]
- 00576a30 bytes db490094
+ 00576d50 bytes db490094
- 00576a3c ["COPY", "tmp:0:8", ["const:4c1:8"]]
- 00576a3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00576a3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00576a3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00576d5c ["COPY", "tmp:0:8", ["const:59f:8"]]
+ 00576d5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00576d5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00576d5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00576a3c bytes 29051391
+ 00576d5c bytes 297d1691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8611926244eda320d0059550661acee"></a>

### [`00576f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576f48.md) → [`00577268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577268.md) FUN_00577268

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00577358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577358.md) [`00577cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577cc0.md) · 呼出先 10件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 2件 [`00577678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577678.md) [`00577fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577fe0.md) · 呼出先 10件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005772c8",
      "incomplete_value": true,
      "site": "005772dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00576fa8",
      "incomplete_value": true,
      "site": "00576fbc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005772e0",
      "incomplete_value": true,
      "site": "005772e0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00576fc0",
      "incomplete_value": true,
      "site": "00576fc0",
      "value": [
        "LOAD",
        "8",
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
      "005772ac",
      "READ",
      [
        "storage",
        "002a4327",
        null,
        "string"
      ]
    ],
    [
      "005772b4",
      "READ",
      [
        "storage",
        "002a432d",
        null,
        "string"
      ]
    ],
    [
      "005772c8",
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
      "005772ac",
      "READ",
      [
        "storage",
        "002a43f2",
        null,
        "string"
      ]
    ],
    [
      "005772b4",
      "READ",
      [
        "storage",
        "002a43f8",
        null,
        "string"
      ]
    ],
    [
      "005772c8",
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

- 旧版 [`00576f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576f48.md#insn-00576f74) · [`00576f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576f48.md#insn-00576f7c) · [`00576f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576f48.md#insn-00576f88)
- 新版 [`00577294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577268.md#insn-00577294) · [`0057729c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577268.md#insn-0057729c) · [`005772a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577268.md#insn-005772a8)

~~~diff
- 00576f74 ["INT_ADD", "register:40f0:8", ["const:576f74:8", "const:4:8"]]
- 00576f74 ["CALL", null, ["callee:005891cc:8"]]
+ 00577294 ["INT_ADD", "register:40f0:8", ["const:577294:8", "const:4:8"]]
+ 00577294 ["CALL", null, ["callee:005891cc:8"]]
- 00576f74 bytes ce470094
+ 00577294 bytes ce470094
- 00576f7c ["INT_ADD", "register:40f0:8", ["const:576f7c:8", "const:4:8"]]
- 00576f7c ["CALL", null, ["callee:005894bc:8"]]
+ 0057729c ["INT_ADD", "register:40f0:8", ["const:57729c:8", "const:4:8"]]
+ 0057729c ["CALL", null, ["callee:005894bc:8"]]
- 00576f7c bytes 88480094
+ 0057729c bytes 88480094
- 00576f88 ["COPY", "tmp:0:8", ["const:327:8"]]
- 00576f88 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00576f88 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00576f88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005772a8 ["COPY", "tmp:0:8", ["const:3f2:8"]]
+ 005772a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005772a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005772a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00576f88 bytes 299d0c91
+ 005772a8 bytes 29c90f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd2bb8174f7a27169d9545275206d07a"></a>

### [`0057718c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/0057718c.md) → [`005774ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/005774ac.md) FUN_005774ac

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00577920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577920.md) · 呼出先 10件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 1件 [`00577c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577c40.md) · 呼出先 10件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.33% / 新版 89.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00577508",
      "incomplete_value": true,
      "site": "00577508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7df:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005771e8",
      "incomplete_value": true,
      "site": "005771e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:701:8"
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
      "definition_site": "00577510",
      "incomplete_value": true,
      "site": "00577510",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005771f0",
      "incomplete_value": true,
      "site": "005771f0",
      "value": [
        "LOAD",
        "8",
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
      "005774f0",
      "READ",
      [
        "storage",
        "002bc701",
        null,
        "string"
      ]
    ],
    [
      "005774f8",
      "READ",
      [
        "storage",
        "002bc706",
        null,
        "string"
      ]
    ],
    [
      "0057750c",
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
      "005774f0",
      "READ",
      [
        "storage",
        "002bc7df",
        null,
        "string"
      ]
    ],
    [
      "005774f8",
      "READ",
      [
        "storage",
        "002bc7e4",
        null,
        "string"
      ]
    ],
    [
      "0057750c",
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

- 旧版 [`005771b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/0057718c.md#insn-005771b8) · [`005771c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/0057718c.md#insn-005771c0) · [`005771cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/0057718c.md#insn-005771cc)
- 新版 [`005774d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/005774ac.md#insn-005774d8) · [`005774e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/005774ac.md#insn-005774e0) · [`005774ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/005774ac.md#insn-005774ec)

~~~diff
- 005771b8 ["INT_ADD", "register:40f0:8", ["const:5771b8:8", "const:4:8"]]
- 005771b8 ["CALL", null, ["callee:005891cc:8"]]
+ 005774d8 ["INT_ADD", "register:40f0:8", ["const:5774d8:8", "const:4:8"]]
+ 005774d8 ["CALL", null, ["callee:005891cc:8"]]
- 005771b8 bytes 3d470094
+ 005774d8 bytes 3d470094
- 005771c0 ["INT_ADD", "register:40f0:8", ["const:5771c0:8", "const:4:8"]]
- 005771c0 ["CALL", null, ["callee:005894bc:8"]]
+ 005774e0 ["INT_ADD", "register:40f0:8", ["const:5774e0:8", "const:4:8"]]
+ 005774e0 ["CALL", null, ["callee:005894bc:8"]]
- 005771c0 bytes f7470094
+ 005774e0 bytes f7470094
- 005771cc ["COPY", "tmp:0:8", ["const:701:8"]]
- 005771cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005771cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005771cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005774ec ["COPY", "tmp:0:8", ["const:7df:8"]]
+ 005774ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005774ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005774ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005771cc bytes 29051c91
+ 005774ec bytes 297d1f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba9d50ee620db1bdd1ddafce1e1f7ae1"></a>

### [`00577358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577358.md) → [`00577678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577678.md) FUN_00577678

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a44.md) · 呼出先 15件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`005769dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005769dc.md) [`00576f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576f48.md) [`005770c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005770c0.md)
- 新版 呼出元 1件 [`00550d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d64.md) · 呼出先 15件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00576618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576618.md) [`00576cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576cfc.md) [`00577268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577268.md) [`005773e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/005773e0.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005777b4",
      "incomplete_value": false,
      "site": "005777bc",
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
      "definition_site": "00577494",
      "incomplete_value": false,
      "site": "0057749c",
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005777cc",
      "incomplete_value": false,
      "site": "005777cc",
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
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005774ac",
      "incomplete_value": false,
      "site": "005774ac",
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
            "const:c30:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00577878",
      "incomplete_value": true,
      "site": "00577878",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577558",
      "incomplete_value": true,
      "site": "00577558",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005776e0",
      "READ",
      [
        "storage",
        "002ba3e3",
        null,
        "string"
      ]
    ],
    [
      "005777bc",
      "DATA",
      [
        "storage",
        "00c6bf50",
        null,
        "undefined *"
      ]
    ],
    [
      "005777cc",
      "DATA",
      [
        "storage",
        "00c6bc30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005776e0",
      "READ",
      [
        "storage",
        "002ba4c1",
        null,
        "string"
      ]
    ],
    [
      "005777bc",
      "DATA",
      [
        "storage",
        "00c6cf20",
        null,
        "undefined *"
      ]
    ],
    [
      "005777cc",
      "DATA",
      [
        "storage",
        "00c6cc00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577358.md#insn-00577558) · [`005773a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577358.md#insn-005773a0) · [`005773a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577358.md#insn-005773a8)
- 新版 [`00577878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577678.md#insn-00577878) · [`005776c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577678.md#insn-005776c0) · [`005776c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577678.md#insn-005776c8)

~~~diff
- 00577558 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
- 00577558 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00577878 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:330:8"]]
+ 00577878 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00577558 bytes 09b901f9
+ 00577878 bytes 099901f9
- 005773a0 ["INT_ADD", "register:40f0:8", ["const:5773a0:8", "const:4:8"]]
- 005773a0 ["CALL", null, ["callee:005891cc:8"]]
+ 005776c0 ["INT_ADD", "register:40f0:8", ["const:5776c0:8", "const:4:8"]]
+ 005776c0 ["CALL", null, ["callee:005891cc:8"]]
- 005773a0 bytes c3460094
+ 005776c0 bytes c3460094
- 005773a8 ["INT_ADD", "register:40f0:8", ["const:5773a8:8", "const:4:8"]]
- 005773a8 ["CALL", null, ["callee:005894bc:8"]]
+ 005776c8 ["INT_ADD", "register:40f0:8", ["const:5776c8:8", "const:4:8"]]
+ 005776c8 ["CALL", null, ["callee:005894bc:8"]]
- 005773a8 bytes 7d470094
+ 005776c8 bytes 7d470094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc1915618f9bde8d453b7137ddc1afc3"></a>

### [`005776b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005776b8.md) → [`005779d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/005779d8.md) FUN_005779d8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0057782c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/0057782c.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)
- 新版 呼出元 1件 [`00577b4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577b4c.md) · 呼出先 1件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005779f8",
      "incomplete_value": false,
      "site": "005779f8",
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
      "definition_site": "005776d8",
      "incomplete_value": false,
      "site": "005776d8",
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
      "005779f8",
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
      "005779f8",
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

- 旧版 [`005776cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005776b8.md#insn-005776cc) · [`005776d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005776b8.md#insn-005776d0) · [`005776d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005776b8.md#insn-005776d4)
- 新版 [`005779ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/005779d8.md#insn-005779ec) · [`005779f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/005779d8.md#insn-005779f0)

~~~diff
- 005776cc ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 005779ec ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 005776cc bytes a8370090
+ 005779ec bytes a83700b0
- 005776d0 ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 005776d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005776d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005776d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005779f0 ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 005779f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005779f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005779f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005776d0 bytes 08e13291
+ 005779f0 bytes 08213291
- 005776d4 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 005776d4 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d7d43cc94c952cf14a8a40cf5ec6393"></a>

### [`00577920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577920.md) → [`00577c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577c40.md) FUN_00577c40

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`005769dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005769dc.md) [`005770c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005770c0.md) [`0057718c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/0057718c.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00576618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576618.md) [`00576cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576cfc.md) [`005773e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/005773e0.md) [`005774ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/005774ac.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 95.67% / 新版 95.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00577d80",
      "incomplete_value": false,
      "site": "00577d88",
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
      "definition_site": "00577a60",
      "incomplete_value": false,
      "site": "00577a68",
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00577e44",
      "incomplete_value": true,
      "site": "00577e44",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577b24",
      "incomplete_value": true,
      "site": "00577b24",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00577e40",
      "incomplete_value": true,
      "site": "00577e40",
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
      "definition_site": "00577b20",
      "incomplete_value": true,
      "site": "00577b20",
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
      "00577cac",
      "READ",
      [
        "storage",
        "002ba3e3",
        null,
        "string"
      ]
    ],
    [
      "00577d88",
      "DATA",
      [
        "storage",
        "00c6bf50",
        null,
        "undefined *"
      ]
    ],
    [
      "00577d98",
      "DATA",
      [
        "storage",
        "00c6bc30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00577cac",
      "READ",
      [
        "storage",
        "002ba4c1",
        null,
        "string"
      ]
    ],
    [
      "00577d88",
      "DATA",
      [
        "storage",
        "00c6cf20",
        null,
        "undefined *"
      ]
    ],
    [
      "00577d98",
      "DATA",
      [
        "storage",
        "00c6cc00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577920.md#insn-00577b24) · [`0057796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577920.md#insn-0057796c) · [`00577974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577920.md#insn-00577974)
- 新版 [`00577e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577c40.md#insn-00577e44) · [`00577c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577c40.md#insn-00577c8c) · [`00577c94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577c40.md#insn-00577c94)

~~~diff
- 00577b24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
- 00577b24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00577e44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:330:8"]]
+ 00577e44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00577b24 bytes 09b901f9
+ 00577e44 bytes 099901f9
- 0057796c ["INT_ADD", "register:40f0:8", ["const:57796c:8", "const:4:8"]]
- 0057796c ["CALL", null, ["callee:005891cc:8"]]
+ 00577c8c ["INT_ADD", "register:40f0:8", ["const:577c8c:8", "const:4:8"]]
+ 00577c8c ["CALL", null, ["callee:005891cc:8"]]
- 0057796c bytes 50450094
+ 00577c8c bytes 50450094
- 00577974 ["INT_ADD", "register:40f0:8", ["const:577974:8", "const:4:8"]]
- 00577974 ["CALL", null, ["callee:005894bc:8"]]
+ 00577c94 ["INT_ADD", "register:40f0:8", ["const:577c94:8", "const:4:8"]]
+ 00577c94 ["CALL", null, ["callee:005894bc:8"]]
- 00577974 bytes 0a460094
+ 00577c94 bytes 0a460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19a7d38aa82c577ee80ff2e7cfe21bf3"></a>

### [`00577cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577cc0.md) → [`00577fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577fe0.md) FUN_00577fe0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 16件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`005769dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005769dc.md) [`00576f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576f48.md) [`005770c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/005770c0.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00576618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576618.md) [`00576cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576cfc.md) [`00577268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577268.md) [`005773e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/005773e0.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 94.71% / 新版 94.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00578138",
      "incomplete_value": false,
      "site": "00578138",
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
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577e18",
      "incomplete_value": false,
      "site": "00577e18",
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
            "const:c30:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005781e4",
      "incomplete_value": true,
      "site": "005781e4",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00577ec4",
      "incomplete_value": true,
      "site": "00577ec4",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005781e0",
      "incomplete_value": true,
      "site": "005781e0",
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
      "definition_site": "00577ec0",
      "incomplete_value": true,
      "site": "00577ec0",
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
      "0057804c",
      "READ",
      [
        "storage",
        "002ba3e3",
        null,
        "string"
      ]
    ],
    [
      "00578128",
      "DATA",
      [
        "storage",
        "00c6bf50",
        null,
        "undefined *"
      ]
    ],
    [
      "00578138",
      "DATA",
      [
        "storage",
        "00c6bc30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0057804c",
      "READ",
      [
        "storage",
        "002ba4c1",
        null,
        "string"
      ]
    ],
    [
      "00578128",
      "DATA",
      [
        "storage",
        "00c6cf20",
        null,
        "undefined *"
      ]
    ],
    [
      "00578138",
      "DATA",
      [
        "storage",
        "00c6cc00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577cc0.md#insn-00577ec4) · [`00577d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577cc0.md#insn-00577d0c) · [`00577d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00577/00577cc0.md#insn-00577d14)
- 新版 [`005781e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577fe0.md#insn-005781e4) · [`0057802c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577fe0.md#insn-0057802c) · [`00578034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00577/00577fe0.md#insn-00578034)

~~~diff
- 00577ec4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
- 00577ec4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 005781e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:330:8"]]
+ 005781e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00577ec4 bytes 09b901f9
+ 005781e4 bytes 099901f9
- 00577d0c ["INT_ADD", "register:40f0:8", ["const:577d0c:8", "const:4:8"]]
- 00577d0c ["CALL", null, ["callee:005891cc:8"]]
+ 0057802c ["INT_ADD", "register:40f0:8", ["const:57802c:8", "const:4:8"]]
+ 0057802c ["CALL", null, ["callee:005891cc:8"]]
- 00577d0c bytes 68440094
+ 0057802c bytes 68440094
- 00577d14 ["INT_ADD", "register:40f0:8", ["const:577d14:8", "const:4:8"]]
- 00577d14 ["CALL", null, ["callee:005894bc:8"]]
+ 00578034 ["INT_ADD", "register:40f0:8", ["const:578034:8", "const:4:8"]]
+ 00578034 ["CALL", null, ["callee:005894bc:8"]]
- 00577d14 bytes 22450094
+ 00578034 bytes 22450094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2e97e3bf9a4258e352f77ed21999fb8"></a>

### [`00578060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578060.md) → [`00578380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578380.md) FUN_00578380

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00578204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578204.md) · 呼出先 10件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`0057c260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c260.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 1件 [`00578524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578524.md) · 呼出先 10件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`0057c580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c580.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.15% / 新版 95.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005783ac",
      "incomplete_value": false,
      "site": "005783b0",
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
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057808c",
      "incomplete_value": false,
      "site": "00578090",
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
            "const:cd8:8"
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
      "005783b0",
      "DATA",
      [
        "storage",
        "00c6bcd8",
        null,
        "undefined *"
      ]
    ],
    [
      "005783d4",
      "READ",
      [
        "storage",
        "002a326e",
        null,
        "string"
      ]
    ],
    [
      "00578474",
      "PARAM",
      [
        "storage",
        "00ca6370",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005783b0",
      "DATA",
      [
        "storage",
        "00c6cca8",
        null,
        "undefined *"
      ]
    ],
    [
      "005783d4",
      "READ",
      [
        "storage",
        "002a3339",
        null,
        "string"
      ]
    ],
    [
      "00578474",
      "PARAM",
      [
        "storage",
        "00ca7330",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578060.md#insn-00578088) · [`0057808c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578060.md#insn-0057808c) · [`00578094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578060.md#insn-00578094)
- 新版 [`005783a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578380.md#insn-005783a8) · [`005783ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578380.md#insn-005783ac) · [`005783b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578380.md#insn-005783b4)

~~~diff
- 00578088 ["COPY", "register:4040:8", ["const:c6b000:8"]]
+ 005783a8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00578088 bytes 883700f0
+ 005783a8 bytes a8370090
- 0057808c ["COPY", "tmp:0:8", ["const:cd8:8"]]
- 0057808c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0057808c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0057808c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005783ac ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 005783ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005783ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005783ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0057808c bytes 08613391
+ 005783ac bytes 08a13291
- 00578094 ["INT_ADD", "register:40f0:8", ["const:578094:8", "const:4:8"]]
- 00578094 ["CALL", null, ["callee:005891cc:8"]]
+ 005783b4 ["INT_ADD", "register:40f0:8", ["const:5783b4:8", "const:4:8"]]
+ 005783b4 ["CALL", null, ["callee:005891cc:8"]]
- 00578094 bytes 86430094
+ 005783b4 bytes 86430094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df98cee65b657ae5343d56bc36f124c5"></a>

### [`0057839c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/0057839c.md) → [`005786bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/005786bc.md) FUN_005786bc

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00578728",
      "incomplete_value": true,
      "site": "00578728",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:927:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578408",
      "incomplete_value": true,
      "site": "00578408",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:85a:8"
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
      "definition_site": "00578740",
      "incomplete_value": true,
      "site": "00578750",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578420",
      "incomplete_value": true,
      "site": "00578430",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:218:8"
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
      "definition_site": "00578754",
      "incomplete_value": true,
      "site": "00578754",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00578434",
      "incomplete_value": true,
      "site": "00578434",
      "value": [
        "LOAD",
        "8",
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
      "00578714",
      "READ",
      [
        "storage",
        "002ad85a",
        null,
        "string"
      ]
    ],
    [
      "00578740",
      "READ",
      [
        "storage",
        "002b6218",
        null,
        "string"
      ]
    ],
    [
      "00578744",
      "READ",
      [
        "storage",
        "002b6227",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578714",
      "READ",
      [
        "storage",
        "002ad927",
        null,
        "string"
      ]
    ],
    [
      "00578740",
      "READ",
      [
        "storage",
        "002b62e7",
        null,
        "string"
      ]
    ],
    [
      "00578744",
      "READ",
      [
        "storage",
        "002b62f6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/0057839c.md#insn-00578494) · [`005785c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/0057839c.md#insn-005785c4) · [`005783d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/0057839c.md#insn-005783d4)
- 新版 [`005787b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/005786bc.md#insn-005787b4) · [`005788e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/005786bc.md#insn-005788e4) · [`005786f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/005786bc.md#insn-005786f4)

~~~diff
- 00578494 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:368:8"]]
- 00578494 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:4"]]
+ 005787b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:328:8"]]
+ 005787b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:4"]]
- 00578494 bytes 166903b9
+ 005787b4 bytes 162903b9
- 005785c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:350:8"]]
- 005785c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 005788e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:310:8"]]
+ 005788e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 005785c4 bytes 09a901f9
+ 005788e4 bytes 098901f9
- 005783d4 ["INT_ADD", "register:40f0:8", ["const:5783d4:8", "const:4:8"]]
- 005783d4 ["CALL", null, ["callee:005891cc:8"]]
+ 005786f4 ["INT_ADD", "register:40f0:8", ["const:5786f4:8", "const:4:8"]]
+ 005786f4 ["CALL", null, ["callee:005891cc:8"]]
- 005783d4 bytes b6420094
+ 005786f4 bytes b6420094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4e1f6e36e0f2fa6fc32b646026381de"></a>

### [`005787d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/005787d0.md) → [`00578af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578af0.md) FUN_00578af0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.61% / 新版 89.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00578b4c",
      "incomplete_value": true,
      "site": "00578b4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:927:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0057882c",
      "incomplete_value": true,
      "site": "0057882c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:85a:8"
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
      "definition_site": "00578b60",
      "incomplete_value": true,
      "site": "00578b68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00578840",
      "incomplete_value": true,
      "site": "00578848",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00578b6c",
      "incomplete_value": true,
      "site": "00578b6c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0057884c",
      "incomplete_value": true,
      "site": "0057884c",
      "value": [
        "LOAD",
        "8",
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
      "00578b3c",
      "READ",
      [
        "storage",
        "002ad85a",
        null,
        "string"
      ]
    ],
    [
      "00578b60",
      "READ",
      [
        "storage",
        "002a6767",
        null,
        "string"
      ]
    ],
    [
      "00578b64",
      "READ",
      [
        "storage",
        "002a6775",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578b3c",
      "READ",
      [
        "storage",
        "002ad927",
        null,
        "string"
      ]
    ],
    [
      "00578b60",
      "READ",
      [
        "storage",
        "002a68bf",
        null,
        "string"
      ]
    ],
    [
      "00578b64",
      "READ",
      [
        "storage",
        "002a68cd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005787f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/005787d0.md#insn-005787f8) · [`00578800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/005787d0.md#insn-00578800) · [`00578818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/005787d0.md#insn-00578818)
- 新版 [`00578b18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578af0.md#insn-00578b18) · [`00578b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578af0.md#insn-00578b20) · [`00578b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578af0.md#insn-00578b38)

~~~diff
- 005787f8 ["INT_ADD", "register:40f0:8", ["const:5787f8:8", "const:4:8"]]
- 005787f8 ["CALL", null, ["callee:005891cc:8"]]
+ 00578b18 ["INT_ADD", "register:40f0:8", ["const:578b18:8", "const:4:8"]]
+ 00578b18 ["CALL", null, ["callee:005891cc:8"]]
- 005787f8 bytes ad410094
+ 00578b18 bytes ad410094
- 00578800 ["INT_ADD", "register:40f0:8", ["const:578800:8", "const:4:8"]]
- 00578800 ["CALL", null, ["callee:005894bc:8"]]
+ 00578b20 ["INT_ADD", "register:40f0:8", ["const:578b20:8", "const:4:8"]]
+ 00578b20 ["CALL", null, ["callee:005894bc:8"]]
- 00578800 bytes 67420094
+ 00578b20 bytes 67420094
- 00578818 ["COPY", "tmp:0:8", ["const:85a:8"]]
- 00578818 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00578818 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00578818 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00578b38 ["COPY", "tmp:0:8", ["const:927:8"]]
+ 00578b38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00578b38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00578b38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00578818 bytes 08692191
+ 00578b38 bytes 089d2491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99bb70e6292ede99bb933648868b6054"></a>

### [`00578950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578950.md) → [`00578c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578c70.md) FUN_00578c70

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00578cc8",
      "incomplete_value": true,
      "site": "00578cc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:645:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005789a8",
      "incomplete_value": true,
      "site": "005789a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:578:8"
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
      "definition_site": "00578cd0",
      "incomplete_value": true,
      "site": "00578cd0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005789b0",
      "incomplete_value": true,
      "site": "005789b0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00578ccc",
      "incomplete_value": true,
      "site": "00578ce0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2ff:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005789ac",
      "incomplete_value": true,
      "site": "005789c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:230:8"
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
      "00578cb0",
      "READ",
      [
        "storage",
        "002ab578",
        null,
        "string"
      ]
    ],
    [
      "00578cb8",
      "READ",
      [
        "storage",
        "002ab57d",
        null,
        "string"
      ]
    ],
    [
      "00578ccc",
      "READ",
      [
        "storage",
        "002b6230",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578cb0",
      "READ",
      [
        "storage",
        "002ab645",
        null,
        "string"
      ]
    ],
    [
      "00578cb8",
      "READ",
      [
        "storage",
        "002ab64a",
        null,
        "string"
      ]
    ],
    [
      "00578ccc",
      "READ",
      [
        "storage",
        "002b62ff",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578950.md#insn-00578978) · [`00578980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578950.md#insn-00578980) · [`0057898c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578950.md#insn-0057898c)
- 新版 [`00578c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578c70.md#insn-00578c98) · [`00578ca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578c70.md#insn-00578ca0) · [`00578cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578c70.md#insn-00578cac)

~~~diff
- 00578978 ["INT_ADD", "register:40f0:8", ["const:578978:8", "const:4:8"]]
- 00578978 ["CALL", null, ["callee:005891cc:8"]]
+ 00578c98 ["INT_ADD", "register:40f0:8", ["const:578c98:8", "const:4:8"]]
+ 00578c98 ["CALL", null, ["callee:005891cc:8"]]
- 00578978 bytes 4d410094
+ 00578c98 bytes 4d410094
- 00578980 ["INT_ADD", "register:40f0:8", ["const:578980:8", "const:4:8"]]
- 00578980 ["CALL", null, ["callee:005894bc:8"]]
+ 00578ca0 ["INT_ADD", "register:40f0:8", ["const:578ca0:8", "const:4:8"]]
+ 00578ca0 ["CALL", null, ["callee:005894bc:8"]]
- 00578980 bytes 07420094
+ 00578ca0 bytes 07420094
- 0057898c ["COPY", "tmp:0:8", ["const:578:8"]]
- 0057898c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0057898c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0057898c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00578cac ["COPY", "tmp:0:8", ["const:645:8"]]
+ 00578cac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00578cac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00578cac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0057898c bytes 29e11591
+ 00578cac bytes 29151991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-280ee407cddc4ff88287a931e519a082"></a>

### [`00578aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578aec.md) → [`00578e0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578e0c.md) FUN_00578e0c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894a4.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.80% / 新版 91.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00578e58",
      "incomplete_value": true,
      "site": "00578e58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e7e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578b38",
      "incomplete_value": true,
      "site": "00578b38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db1:8"
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
      "definition_site": "00578e5c",
      "incomplete_value": true,
      "site": "00578e5c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00578b3c",
      "incomplete_value": true,
      "site": "00578b3c",
      "value": [
        "LOAD",
        "8",
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
      "00578e48",
      "READ",
      [
        "storage",
        "002a8db1",
        null,
        "string"
      ]
    ],
    [
      "00578e50",
      "READ",
      [
        "storage",
        "002a8db6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578e48",
      "READ",
      [
        "storage",
        "002a8e7e",
        null,
        "string"
      ]
    ],
    [
      "00578e50",
      "READ",
      [
        "storage",
        "002a8e83",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578aec.md#insn-00578b10) · [`00578b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578aec.md#insn-00578b18) · [`00578b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578aec.md#insn-00578b24)
- 新版 [`00578e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578e0c.md#insn-00578e30) · [`00578e38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578e0c.md#insn-00578e38) · [`00578e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578e0c.md#insn-00578e44)

~~~diff
- 00578b10 ["INT_ADD", "register:40f0:8", ["const:578b10:8", "const:4:8"]]
- 00578b10 ["CALL", null, ["callee:005891cc:8"]]
+ 00578e30 ["INT_ADD", "register:40f0:8", ["const:578e30:8", "const:4:8"]]
+ 00578e30 ["CALL", null, ["callee:005891cc:8"]]
- 00578b10 bytes e7400094
+ 00578e30 bytes e7400094
- 00578b18 ["INT_ADD", "register:40f0:8", ["const:578b18:8", "const:4:8"]]
- 00578b18 ["CALL", null, ["callee:005894bc:8"]]
+ 00578e38 ["INT_ADD", "register:40f0:8", ["const:578e38:8", "const:4:8"]]
+ 00578e38 ["CALL", null, ["callee:005894bc:8"]]
- 00578b18 bytes a1410094
+ 00578e38 bytes a1410094
- 00578b24 ["COPY", "tmp:0:8", ["const:db1:8"]]
- 00578b24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00578b24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00578b24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00578e44 ["COPY", "tmp:0:8", ["const:e7e:8"]]
+ 00578e44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00578e44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00578e44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00578b24 bytes 29c53691
+ 00578e44 bytes 29f93991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3265e6219188d67adfb1372b4be13aa3"></a>

### [`00578c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578c1c.md) → [`00578f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578f3c.md) FUN_00578f3c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00578f88",
      "incomplete_value": true,
      "site": "00578f88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ddb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578c68",
      "incomplete_value": true,
      "site": "00578c68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d04:8"
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
      "definition_site": "00578f8c",
      "incomplete_value": true,
      "site": "00578f8c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00578c6c",
      "incomplete_value": true,
      "site": "00578c6c",
      "value": [
        "LOAD",
        "8",
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
      "00578f78",
      "READ",
      [
        "storage",
        "002b0d04",
        null,
        "string"
      ]
    ],
    [
      "00578f80",
      "READ",
      [
        "storage",
        "002b0d09",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00578f78",
      "READ",
      [
        "storage",
        "002b0ddb",
        null,
        "string"
      ]
    ],
    [
      "00578f80",
      "READ",
      [
        "storage",
        "002b0de0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578c1c.md#insn-00578c40) · [`00578c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578c1c.md#insn-00578c48) · [`00578c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578c1c.md#insn-00578c54)
- 新版 [`00578f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578f3c.md#insn-00578f60) · [`00578f68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578f3c.md#insn-00578f68) · [`00578f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00578/00578f3c.md#insn-00578f74)

~~~diff
- 00578c40 ["INT_ADD", "register:40f0:8", ["const:578c40:8", "const:4:8"]]
- 00578c40 ["CALL", null, ["callee:005891cc:8"]]
+ 00578f60 ["INT_ADD", "register:40f0:8", ["const:578f60:8", "const:4:8"]]
+ 00578f60 ["CALL", null, ["callee:005891cc:8"]]
- 00578c40 bytes 9b400094
+ 00578f60 bytes 9b400094
- 00578c48 ["INT_ADD", "register:40f0:8", ["const:578c48:8", "const:4:8"]]
- 00578c48 ["CALL", null, ["callee:005894bc:8"]]
+ 00578f68 ["INT_ADD", "register:40f0:8", ["const:578f68:8", "const:4:8"]]
+ 00578f68 ["CALL", null, ["callee:005894bc:8"]]
- 00578c48 bytes 55410094
+ 00578f68 bytes 55410094
- 00578c54 ["COPY", "tmp:0:8", ["const:d04:8"]]
- 00578c54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00578c54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00578c54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00578f74 ["COPY", "tmp:0:8", ["const:ddb:8"]]
+ 00578f74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00578f74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00578f74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00578c54 bytes 29113491
+ 00578f74 bytes 296d3791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13da59378654f3d1e12032aa76a747a9"></a>

### [`00578d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578d8c.md) → [`005790ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/005790ac.md) FUN_005790ac

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589680.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005790f8",
      "incomplete_value": true,
      "site": "005790f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ded:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00578dd8",
      "incomplete_value": true,
      "site": "00578dd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d0f:8"
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
      "definition_site": "005790fc",
      "incomplete_value": true,
      "site": "005790fc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00578ddc",
      "incomplete_value": true,
      "site": "00578ddc",
      "value": [
        "LOAD",
        "8",
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
      "005790e8",
      "READ",
      [
        "storage",
        "002b3d0f",
        null,
        "string"
      ]
    ],
    [
      "005790f0",
      "READ",
      [
        "storage",
        "002b3d14",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005790e8",
      "READ",
      [
        "storage",
        "002b3ded",
        null,
        "string"
      ]
    ],
    [
      "005790f0",
      "READ",
      [
        "storage",
        "002b3df2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00578db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578d8c.md#insn-00578db0) · [`00578db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578d8c.md#insn-00578db8) · [`00578dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578d8c.md#insn-00578dc4)
- 新版 [`005790d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/005790ac.md#insn-005790d0) · [`005790d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/005790ac.md#insn-005790d8) · [`005790e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/005790ac.md#insn-005790e4)

~~~diff
- 00578db0 ["INT_ADD", "register:40f0:8", ["const:578db0:8", "const:4:8"]]
- 00578db0 ["CALL", null, ["callee:005891cc:8"]]
+ 005790d0 ["INT_ADD", "register:40f0:8", ["const:5790d0:8", "const:4:8"]]
+ 005790d0 ["CALL", null, ["callee:005891cc:8"]]
- 00578db0 bytes 3f400094
+ 005790d0 bytes 3f400094
- 00578db8 ["INT_ADD", "register:40f0:8", ["const:578db8:8", "const:4:8"]]
- 00578db8 ["CALL", null, ["callee:005894bc:8"]]
+ 005790d8 ["INT_ADD", "register:40f0:8", ["const:5790d8:8", "const:4:8"]]
+ 005790d8 ["CALL", null, ["callee:005894bc:8"]]
- 00578db8 bytes f9400094
+ 005790d8 bytes f9400094
- 00578dc4 ["COPY", "tmp:0:8", ["const:d0f:8"]]
- 00578dc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00578dc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00578dc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005790e4 ["COPY", "tmp:0:8", ["const:ded:8"]]
+ 005790e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005790e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005790e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00578dc4 bytes 293d3491
+ 005790e4 bytes 29b53791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5112a980a13da6be2ab1d4e2d4d98d3b"></a>

### [`00578efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578efc.md) → [`0057921c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/0057921c.md) FUN_0057921c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 19件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00579564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00579/00579564.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)
- 新版 呼出元 0件  · 呼出先 19件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00579884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/00579884.md) [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 1件, `store_destination` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0057937c",
      "incomplete_value": true,
      "site": "0057937c",
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
      "definition_site": "0057905c",
      "incomplete_value": true,
      "site": "0057905c",
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
    "ordinal": 31,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005795f0",
      "incomplete_value": true,
      "site": "005795f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "005792d0",
      "incomplete_value": true,
      "site": "005792d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005795f4",
      "incomplete_value": true,
      "site": "005795f4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005792d4",
      "incomplete_value": true,
      "site": "005792d4",
      "value": [
        "LOAD",
        "8",
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
      "005792f8",
      "READ",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "0057935c",
      "DATA",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "0057936c",
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
      "005792f8",
      "READ",
      [
        "storage",
        "00ca7300",
        null,
        "undefined8"
      ]
    ],
    [
      "0057935c",
      "DATA",
      [
        "storage",
        "00ca7300",
        null,
        "undefined8"
      ]
    ],
    [
      "0057936c",
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

- 旧版 [`0057905c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578efc.md#insn-0057905c) · [`00579378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578efc.md#insn-00579378) · [`00578f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578efc.md#insn-00578f58)
- 新版 [`0057937c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/0057921c.md#insn-0057937c) · [`00579698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/0057921c.md#insn-00579698) · [`00579278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/0057921c.md#insn-00579278)

~~~diff
- 0057905c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:338:8"]]
- 0057905c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0057937c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2f8:8"]]
+ 0057937c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0057905c bytes 099d01f9
+ 0057937c bytes 097d01f9
- 00579378 ["INT_ADD", "register:40f0:8", ["const:579378:8", "const:4:8"]]
- 00579378 ["CALL", null, ["callee:00589bb8:8"]]
+ 00579698 ["INT_ADD", "register:40f0:8", ["const:579698:8", "const:4:8"]]
+ 00579698 ["CALL", null, ["callee:00589bb8:8"]]
- 00579378 bytes 48410094
+ 00579698 bytes 48410094
- 00578f58 ["COPY", "register:0:8", ["register:4048:8"]]
- 00578f58 ["INT_ADD", "register:40f0:8", ["const:578f58:8", "const:4:8"]]
- 00578f58 ["CALLIND", null, ["register:0:8"]]
+ 00579278 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00579278 ["INT_ADD", "register:40f0:8", ["const:579278:8", "const:4:8"]]
+ 00579278 ["CALLIND", null, ["register:0:8"]]
- 00578f58 bytes 20013fd6
+ 00579278 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

