# v16.0.2 → v16.0.3 · 最優先の変更候補 (3)

[一覧の目次](README.md)

<a id="compare-c36b964c3182dc316655596a836b0787"></a>

### [`0045aacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045aacc.md) → [`0045adec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045adec.md) FUN_0045adec

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00451e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451e0c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045212c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00452/0045212c.md)

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
      "definition_site": "0045adf4",
      "incomplete_value": false,
      "site": "0045adf4",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045aad4",
      "incomplete_value": false,
      "site": "0045aad4",
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
            "const:a50:8"
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
      "0045adf4",
      "DATA",
      [
        "storage",
        "00c63a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045adf4",
      "DATA",
      [
        "storage",
        "00c64a20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045aacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045aacc.md#insn-0045aacc) · [`0045aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045aacc.md#insn-0045aad0)
- 新版 [`0045adec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045adec.md#insn-0045adec) · [`0045adf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045adec.md#insn-0045adf0)

~~~diff
- 0045aacc ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045adec ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045aacc bytes 484000b0
+ 0045adec bytes 484000d0
- 0045aad0 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 0045aad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045aad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045aad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045adf0 ["COPY", "tmp:0:8", ["const:a20:8"]]
+ 0045adf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045adf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045adf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045aad0 bytes 08412991
+ 0045adf0 bytes 08812891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-532827a5b7fe2571376be08a67095f45"></a>

### [`0045aadc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045aadc.md) → [`0045adfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045adfc.md) FUN_0045adfc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00451e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451e0c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045212c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00452/0045212c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "0045ae14",
      "incomplete_value": false,
      "site": "0045ae14",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045aaf4",
      "incomplete_value": false,
      "site": "0045aaf4",
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
            "const:a50:8"
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
      "0045ae14",
      "DATA",
      [
        "storage",
        "00c63a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ae14",
      "DATA",
      [
        "storage",
        "00c64a20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045aae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045aadc.md#insn-0045aae8) · [`0045aaec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045aadc.md#insn-0045aaec) · [`0045aaf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045aadc.md#insn-0045aaf8)
- 新版 [`0045ae08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045adfc.md#insn-0045ae08) · [`0045ae0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045adfc.md#insn-0045ae0c) · [`0045ae18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045adfc.md#insn-0045ae18)

~~~diff
- 0045aae8 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045ae08 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045aae8 bytes 484000b0
+ 0045ae08 bytes 484000d0
- 0045aaec ["COPY", "tmp:0:8", ["const:a50:8"]]
- 0045aaec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045aaec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045aaec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045ae0c ["COPY", "tmp:0:8", ["const:a20:8"]]
+ 0045ae0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ae0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ae0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045aaec bytes 08412991
+ 0045ae0c bytes 08812891
- 0045aaf8 ["INT_ADD", "register:40f0:8", ["const:45aaf8:8", "const:4:8"]]
- 0045aaf8 ["CALL", null, ["callee:0045212c:8"]]
+ 0045ae18 ["INT_ADD", "register:40f0:8", ["const:45ae18:8", "const:4:8"]]
+ 0045ae18 ["CALL", null, ["callee:0045212c:8"]]
- 0045aaf8 bytes c5dcff97
+ 0045ae18 bytes c5dcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa81b91100b745e6346a5fadec8bba89"></a>

### [`0045ab0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045ab0c.md) → [`0045ae2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045ae2c.md) FUN_0045ae2c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0045b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b330.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045b650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045b650.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0045ae50",
      "incomplete_value": false,
      "site": "0045ae50",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ab30",
      "incomplete_value": false,
      "site": "0045ab30",
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
            "const:a50:8"
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
      "0045ae50",
      "DATA",
      [
        "storage",
        "00c63a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ae50",
      "DATA",
      [
        "storage",
        "00c64a20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ab20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045ab0c.md#insn-0045ab20) · [`0045ab28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045ab0c.md#insn-0045ab28) · [`0045ab2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045ab0c.md#insn-0045ab2c)
- 新版 [`0045ae40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045ae2c.md#insn-0045ae40) · [`0045ae48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045ae2c.md#insn-0045ae48) · [`0045ae4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045ae2c.md#insn-0045ae4c)

~~~diff
- 0045ab20 ["INT_ADD", "register:40f0:8", ["const:45ab20:8", "const:4:8"]]
- 0045ab20 ["CALL", null, ["callee:00c58f30:8"]]
+ 0045ae40 ["INT_ADD", "register:40f0:8", ["const:45ae40:8", "const:4:8"]]
+ 0045ae40 ["CALL", null, ["callee:00c58f30:8"]]
- 0045ab20 bytes 10f51f94
+ 0045ae40 bytes 3cf81f94
- 0045ab28 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045ae48 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045ab28 bytes 484000b0
+ 0045ae48 bytes 484000d0
- 0045ab2c ["COPY", "tmp:0:8", ["const:a50:8"]]
- 0045ab2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045ab2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045ab2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045ae4c ["COPY", "tmp:0:8", ["const:a20:8"]]
+ 0045ae4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ae4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ae4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045ab2c bytes 08412991
+ 0045ae4c bytes 08812891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc3d6e7b610f8329eff7c999ed1e2433"></a>

### [`0045ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045ab60.md) → [`0045ae80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045ae80.md) FUN_0045ae80

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0045b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b330.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045b650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045b650.md)

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
      "definition_site": "0045ae8c",
      "incomplete_value": false,
      "site": "0045ae8c",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ab6c",
      "incomplete_value": false,
      "site": "0045ab6c",
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
            "const:a50:8"
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
      "0045ae8c",
      "DATA",
      [
        "storage",
        "00c63a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ae8c",
      "DATA",
      [
        "storage",
        "00c64a20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ab64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045ab60.md#insn-0045ab64) · [`0045ab68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045ab60.md#insn-0045ab68)
- 新版 [`0045ae84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045ae80.md#insn-0045ae84) · [`0045ae88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045ae80.md#insn-0045ae88)

~~~diff
- 0045ab64 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 0045ae84 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0045ab64 bytes 494000b0
+ 0045ae84 bytes 494000d0
- 0045ab68 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 0045ab68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045ab68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045ab68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045ae88 ["COPY", "tmp:0:8", ["const:a20:8"]]
+ 0045ae88 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ae88 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ae88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045ab68 bytes 29412991
+ 0045ae88 bytes 29812891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d1719aed163d22c1ab148e9d1269a57"></a>

### [`0045abac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045abac.md) → [`0045aecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aecc.md) FUN_0045aecc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 18件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00450790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/00450790.md) [`00452c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0045b8ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b8ec.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00450ab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00450/00450ab0.md) [`00452fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00452/00452fb4.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0045bc0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045bc0c.md)

変更の種類 call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 96.35% / 新版 96.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 3件, `store_value` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045b1b4",
      "incomplete_value": false,
      "site": "0045b1b4",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ae94",
      "incomplete_value": false,
      "site": "0045ae94",
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
            "const:ac0:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045afec",
      "value": [
        "leaf",
        "ram:7694f8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045accc",
      "value": [
        "leaf",
        "ram:76911c:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0045ad34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045afec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0076911c"
      ]
    ],
    [
      "0045b04c",
      "READ",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:0045ad34",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ]
  ],
  "added": [
    [
      "0045afec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007694f8"
      ]
    ],
    [
      "0045b04c",
      "READ",
      [
        "storage",
        "00ca5b60",
        null,
        "undefined1"
      ]
    ],
    [
      "0045b054",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045accc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045abac.md#insn-0045accc) · [`0045ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045abac.md#insn-0045ad34) · [`0045ad3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045abac.md#insn-0045ad3c)
- 新版 [`0045afec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aecc.md#insn-0045afec) · [`0045b05c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aecc.md#insn-0045b05c)

~~~diff
- 0045accc ["INT_ADD", "register:40f0:8", ["const:45accc:8", "const:4:8"]]
- 0045accc ["CALL", null, ["ram:76911c:8"]]
+ 0045afec ["INT_ADD", "register:40f0:8", ["const:45afec:8", "const:4:8"]]
+ 0045afec ["CALL", null, ["ram:7694f8:8"]]
- 0045accc bytes 14390c94
+ 0045afec bytes 43390c94
- 0045ad34 ["INT_ADD", "register:40f0:8", ["const:45ad34:8", "const:4:8"]]
- 0045ad34 ["CALL", null, ["callee:008524fc:8"]]
- 0045ad34 bytes 07da0f94
- 0045ad3c ["INT_ADD", "register:40f0:8", ["const:45ad3c:8", "const:4:8"]]
- 0045ad3c ["CALL", null, ["ram:7643dc:8"]]
+ 0045b05c ["INT_ADD", "register:40f0:8", ["const:45b05c:8", "const:4:8"]]
+ 0045b05c ["CALL", null, ["ram:7647b8:8"]]
- 0045ad3c bytes a8250c94
+ 0045b05c bytes d7250c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af112b8f5b44bd402f16a85a35857307"></a>

### [`0045b6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b6a0.md) → [`0045b9c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045b9c0.md) FUN_0045b9c0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "0045b9d8",
      "incomplete_value": false,
      "site": "0045b9e4",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045b6b8",
      "incomplete_value": false,
      "site": "0045b6c4",
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
            "const:ac0:8"
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
      "0045b9e4",
      "DATA",
      [
        "storage",
        "00c63ac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045b9e4",
      "DATA",
      [
        "storage",
        "00c64a90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045b6b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b6a0.md#insn-0045b6b4) · [`0045b6b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b6a0.md#insn-0045b6b8) · [`0045b6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b6a0.md#insn-0045b6e8)
- 新版 [`0045b9d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045b9c0.md#insn-0045b9d4) · [`0045b9d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045b9c0.md#insn-0045b9d8) · [`0045ba08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045b9c0.md#insn-0045ba08)

~~~diff
- 0045b6b4 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045b9d4 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045b6b4 bytes 48400090
+ 0045b9d4 bytes 484000b0
- 0045b6b8 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 0045b6b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045b6b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045b6b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045b9d8 ["COPY", "tmp:0:8", ["const:a90:8"]]
+ 0045b9d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b9d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b9d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045b6b8 bytes 08012b91
+ 0045b9d8 bytes 08412a91
- 0045b6e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045b6e8 ["INT_ADD", "register:40f0:8", ["const:45b6e8:8", "const:4:8"]]
- 0045b6e8 ["CALLIND", null, ["register:0:8"]]
+ 0045ba08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045ba08 ["INT_ADD", "register:40f0:8", ["const:45ba08:8", "const:4:8"]]
+ 0045ba08 ["CALLIND", null, ["register:0:8"]]
- 0045b6e8 bytes 00013fd6
+ 0045ba08 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92fd9109883572da6890e4cdf4d756ed"></a>

### [`0045b78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b78c.md) → [`0045baac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045baac.md) FUN_0045baac

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045bac4",
      "incomplete_value": false,
      "site": "0045bad0",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045b7a4",
      "incomplete_value": false,
      "site": "0045b7b0",
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
            "const:ac0:8"
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
      "0045bad0",
      "DATA",
      [
        "storage",
        "00c63ac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045bad0",
      "DATA",
      [
        "storage",
        "00c64a90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045b7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b78c.md#insn-0045b7a0) · [`0045b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b78c.md#insn-0045b7a4) · [`0045b7d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b78c.md#insn-0045b7d4)
- 新版 [`0045bac0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045baac.md#insn-0045bac0) · [`0045bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045baac.md#insn-0045bac4) · [`0045baf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045baac.md#insn-0045baf4)

~~~diff
- 0045b7a0 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045bac0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045b7a0 bytes 48400090
+ 0045bac0 bytes 484000b0
- 0045b7a4 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 0045b7a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045b7a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045b7a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045bac4 ["COPY", "tmp:0:8", ["const:a90:8"]]
+ 0045bac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045b7a4 bytes 08012b91
+ 0045bac4 bytes 08412a91
- 0045b7d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045b7d4 ["INT_ADD", "register:40f0:8", ["const:45b7d4:8", "const:4:8"]]
- 0045b7d4 ["CALLIND", null, ["register:0:8"]]
+ 0045baf4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045baf4 ["INT_ADD", "register:40f0:8", ["const:45baf4:8", "const:4:8"]]
+ 0045baf4 ["CALLIND", null, ["register:0:8"]]
- 0045b7d4 bytes 00013fd6
+ 0045baf4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07febb50a2d2ee2d2690bb6bf513cfbe"></a>

### [`0045b874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b874.md) → [`0045bb94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045bb94.md) FUN_0045bb94

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0045bb3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bb3c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045be5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045be5c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0045bbb8",
      "incomplete_value": false,
      "site": "0045bbb8",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045b898",
      "incomplete_value": false,
      "site": "0045b898",
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
            "const:ac0:8"
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
      "0045bbb8",
      "DATA",
      [
        "storage",
        "00c63ac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045bbb8",
      "DATA",
      [
        "storage",
        "00c64a90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045b888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b874.md#insn-0045b888) · [`0045b890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b874.md#insn-0045b890) · [`0045b894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b874.md#insn-0045b894)
- 新版 [`0045bba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045bb94.md#insn-0045bba8) · [`0045bbb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045bb94.md#insn-0045bbb0) · [`0045bbb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045bb94.md#insn-0045bbb4)

~~~diff
- 0045b888 ["INT_ADD", "register:40f0:8", ["const:45b888:8", "const:4:8"]]
- 0045b888 ["CALL", null, ["callee:00c58f30:8"]]
+ 0045bba8 ["INT_ADD", "register:40f0:8", ["const:45bba8:8", "const:4:8"]]
+ 0045bba8 ["CALL", null, ["callee:00c58f30:8"]]
- 0045b888 bytes b6f11f94
+ 0045bba8 bytes e2f41f94
- 0045b890 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045bbb0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045b890 bytes 48400090
+ 0045bbb0 bytes 484000b0
- 0045b894 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 0045b894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045b894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045b894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045bbb4 ["COPY", "tmp:0:8", ["const:a90:8"]]
+ 0045bbb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bbb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bbb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045b894 bytes 08012b91
+ 0045bbb4 bytes 08412a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1330a22919f015592eed7e6fed9c09e"></a>

### [`0045b8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b8c8.md) → [`0045bbe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045bbe8.md) FUN_0045bbe8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0045bb3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bb3c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045be5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045be5c.md)

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
      "definition_site": "0045bbf4",
      "incomplete_value": false,
      "site": "0045bbf4",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045b8d4",
      "incomplete_value": false,
      "site": "0045b8d4",
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
            "const:ac0:8"
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
      "0045bbf4",
      "DATA",
      [
        "storage",
        "00c63ac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045bbf4",
      "DATA",
      [
        "storage",
        "00c64a90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045b8cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b8c8.md#insn-0045b8cc) · [`0045b8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b8c8.md#insn-0045b8d0)
- 新版 [`0045bbec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045bbe8.md#insn-0045bbec) · [`0045bbf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045bbe8.md#insn-0045bbf0)

~~~diff
- 0045b8cc ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 0045bbec ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0045b8cc bytes 49400090
+ 0045bbec bytes 494000b0
- 0045b8d0 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 0045b8d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045b8d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045b8d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045bbf0 ["COPY", "tmp:0:8", ["const:a90:8"]]
+ 0045bbf0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045bbf0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045bbf0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045b8d0 bytes 29012b91
+ 0045bbf0 bytes 29412a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98d4c4924631233af9ef28c606866349"></a>

### [`0045b914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b914.md) → [`0045bc34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045bc34.md) FUN_0045bc34

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`007643dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007643dc.md) [`00768ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768ee8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00450d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00450/00450d10.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`007647b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/007647b8.md) [`007692c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/007692c4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.17% / 新版 94.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045bc70",
      "value": [
        "leaf",
        "ram:7692c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045b950",
      "value": [
        "leaf",
        "ram:768ee8:8"
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
      "site": "0045bce8",
      "value": [
        "leaf",
        "ram:7647b8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045b9c8",
      "value": [
        "leaf",
        "ram:7643dc:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045bd9c",
      "incomplete_value": false,
      "site": "0045bda0",
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
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ba7c",
      "incomplete_value": false,
      "site": "0045ba80",
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
            "const:ba0:8"
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
      "0045bc70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768ee8"
      ]
    ],
    [
      "0045bc7c",
      "READ",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045bce8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007643dc"
      ]
    ]
  ],
  "added": [
    [
      "0045bc70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007692c4"
      ]
    ],
    [
      "0045bc7c",
      "READ",
      [
        "storage",
        "00ca5b60",
        null,
        "undefined1"
      ]
    ],
    [
      "0045bce8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007647b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045b950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b914.md#insn-0045b950) · [`0045b9c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b914.md#insn-0045b9c8) · [`0045ba80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b914.md#insn-0045ba80)
- 新版 [`0045bc70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045bc34.md#insn-0045bc70) · [`0045bce8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045bc34.md#insn-0045bce8) · [`0045bda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045b/0045bc34.md#insn-0045bda0)

~~~diff
- 0045b950 ["INT_ADD", "register:40f0:8", ["const:45b950:8", "const:4:8"]]
- 0045b950 ["CALL", null, ["ram:768ee8:8"]]
+ 0045bc70 ["INT_ADD", "register:40f0:8", ["const:45bc70:8", "const:4:8"]]
+ 0045bc70 ["CALL", null, ["ram:7692c4:8"]]
- 0045b950 bytes 66350c94
+ 0045bc70 bytes 95350c94
- 0045b9c8 ["INT_ADD", "register:40f0:8", ["const:45b9c8:8", "const:4:8"]]
- 0045b9c8 ["CALL", null, ["ram:7643dc:8"]]
+ 0045bce8 ["INT_ADD", "register:40f0:8", ["const:45bce8:8", "const:4:8"]]
+ 0045bce8 ["CALL", null, ["ram:7647b8:8"]]
- 0045b9c8 bytes 85220c94
+ 0045bce8 bytes b4220c94
- 0045ba80 ["INT_ADD", "register:40f0:8", ["const:45ba80:8", "const:4:8"]]
- 0045ba80 ["CALL", null, ["callee:00c58ef0:8"]]
+ 0045bda0 ["INT_ADD", "register:40f0:8", ["const:45bda0:8", "const:4:8"]]
+ 0045bda0 ["CALL", null, ["callee:00c58ef0:8"]]
- 0045ba80 bytes 28f11f94
+ 0045bda0 bytes 54f41f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3148f9f51ef21a299743f9712c2d8bce"></a>

### [`0045bdcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bdcc.md) → [`0045c0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c0ec.md) FUN_0045c0ec

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
      "definition_site": "0045c0f0",
      "incomplete_value": false,
      "site": "0045c0f4",
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
      "definition_site": "0045bdd0",
      "incomplete_value": false,
      "site": "0045bdd4",
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
      "0045c0f4",
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
      "0045c0f4",
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

- 旧版 [`0045bdcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bdcc.md#insn-0045bdcc) · [`0045bdd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bdcc.md#insn-0045bdd0)
- 新版 [`0045c0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c0ec.md#insn-0045c0ec) · [`0045c0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c0ec.md#insn-0045c0f0)

~~~diff
- 0045bdcc ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045c0ec ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045bdcc bytes 48400090
+ 0045c0ec bytes 48400090
- 0045bdd0 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 0045bdd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045bdd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045bdd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045c0f0 ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 0045c0f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c0f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c0f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045bdd0 bytes 08812d91
+ 0045c0f0 bytes 08c12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b2882128071e3c51ab5934396b28107"></a>

### [`0045bddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bddc.md) → [`0045c0fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c0fc.md) FUN_0045c0fc

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
      "definition_site": "0045c10c",
      "incomplete_value": false,
      "site": "0045c114",
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
      "definition_site": "0045bdec",
      "incomplete_value": false,
      "site": "0045bdf4",
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
      "0045c114",
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
      "0045c114",
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

- 旧版 [`0045bde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bddc.md#insn-0045bde8) · [`0045bdec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bddc.md#insn-0045bdec) · [`0045bdf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bddc.md#insn-0045bdf8)
- 新版 [`0045c108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c0fc.md#insn-0045c108) · [`0045c10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c0fc.md#insn-0045c10c) · [`0045c118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c0fc.md#insn-0045c118)

~~~diff
- 0045bde8 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045c108 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045bde8 bytes 48400090
+ 0045c108 bytes 48400090
- 0045bdec ["COPY", "tmp:0:8", ["const:b60:8"]]
- 0045bdec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045bdec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045bdec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045c10c ["COPY", "tmp:0:8", ["const:b30:8"]]
+ 0045c10c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c10c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c10c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045bdec bytes 08812d91
+ 0045c10c bytes 08c12c91
- 0045bdf8 ["INT_ADD", "register:40f0:8", ["const:45bdf8:8", "const:4:8"]]
- 0045bdf8 ["CALL", null, ["callee:00c58f40:8"]]
+ 0045c118 ["INT_ADD", "register:40f0:8", ["const:45c118:8", "const:4:8"]]
+ 0045c118 ["CALL", null, ["callee:00c58f40:8"]]
- 0045bdf8 bytes 5ef01f94
+ 0045c118 bytes 8af31f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98aca48db07457494d9a8bcde48dcc60"></a>

### [`0045be1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be1c.md) → [`0045c13c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c13c.md) FUN_0045c13c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0045be6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be6c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045c18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c18c.md)

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
      "definition_site": "0045c14c",
      "incomplete_value": false,
      "site": "0045c150",
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
            "const:b80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045be2c",
      "incomplete_value": false,
      "site": "0045be30",
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
            "const:bb0:8"
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
      "0045c150",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045c150",
      "DATA",
      [
        "storage",
        "00c64b80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045be28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be1c.md#insn-0045be28) · [`0045be2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be1c.md#insn-0045be2c)
- 新版 [`0045c148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c13c.md#insn-0045c148) · [`0045c14c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c13c.md#insn-0045c14c)

~~~diff
- 0045be28 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 0045c148 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0045be28 bytes 49400090
+ 0045c148 bytes 49400090
- 0045be2c ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 0045be2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045be2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045be2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045c14c ["COPY", "tmp:0:8", ["const:b80:8"]]
+ 0045c14c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045c14c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045c14c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045be2c bytes 29c12e91
+ 0045c14c bytes 29012e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e763e3f4adff3a1349c9a4335800e5b"></a>

### [`0045be38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be38.md) → [`0045c158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c158.md) FUN_0045c158

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 7件 [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md) [`00595d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md) [`007671a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/007671a0.md) [`00798ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798ef8.md) [`007abc7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007abc7c.md) · 呼出先 2件 [`0045be6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be6c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 7件 [`00595d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595d3c.md) [`0059607c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/0059607c.md) [`0076757c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00767/0076757c.md) [`007992d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00799/007992d4.md) [`007ac08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007ac/007ac08c.md) · 呼出先 2件 [`0045c18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c18c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "0045c174",
      "incomplete_value": false,
      "site": "0045c174",
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
            "const:b80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045be54",
      "incomplete_value": false,
      "site": "0045be54",
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
            "const:bb0:8"
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
      "0045c174",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045c174",
      "DATA",
      [
        "storage",
        "00c64b80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045be48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be38.md#insn-0045be48) · [`0045be4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be38.md#insn-0045be4c) · [`0045be58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be38.md#insn-0045be58)
- 新版 [`0045c168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c158.md#insn-0045c168) · [`0045c16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c158.md#insn-0045c16c) · [`0045c178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c158.md#insn-0045c178)

~~~diff
- 0045be48 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045c168 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045be48 bytes 48400090
+ 0045c168 bytes 48400090
- 0045be4c ["COPY", "tmp:0:8", ["const:bb0:8"]]
- 0045be4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045be4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045be4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045c16c ["COPY", "tmp:0:8", ["const:b80:8"]]
+ 0045c16c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c16c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c16c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045be4c bytes 08c12e91
+ 0045c16c bytes 08012e91
- 0045be58 ["INT_ADD", "register:40f0:8", ["const:45be58:8", "const:4:8"]]
- 0045be58 ["CALL", null, ["callee:0045c18c:8"]]
+ 0045c178 ["INT_ADD", "register:40f0:8", ["const:45c178:8", "const:4:8"]]
+ 0045c178 ["CALL", null, ["callee:0045c18c:8"]]
- 0045be58 bytes 05000094
+ 0045c178 bytes 05000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d54af72460a1e394035e29cfdb43dc58"></a>

### [`0045bed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bed4.md) → [`0045c1f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c1f4.md) FUN_0045c1f4

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
      "definition_site": "0045c200",
      "incomplete_value": false,
      "site": "0045c20c",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045bee0",
      "incomplete_value": false,
      "site": "0045beec",
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
            "const:c10:8"
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
      "0045c20c",
      "DATA",
      [
        "storage",
        "00c63c10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045c20c",
      "DATA",
      [
        "storage",
        "00c64be0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045bedc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bed4.md#insn-0045bedc) · [`0045bee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bed4.md#insn-0045bee0)
- 新版 [`0045c1fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c1f4.md#insn-0045c1fc) · [`0045c200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c1f4.md#insn-0045c200)

~~~diff
- 0045bedc ["COPY", "register:4050:8", ["const:c63000:8"]]
+ 0045c1fc ["COPY", "register:4050:8", ["const:c64000:8"]]
- 0045bedc bytes 4a400090
+ 0045c1fc bytes 4a400090
- 0045bee0 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 0045bee0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045bee0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045bee0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045c200 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 0045c200 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045c200 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045c200 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045bee0 bytes 4a413091
+ 0045c200 bytes 4a812f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fd6529f21113286ee2b0a5a1aeab463"></a>

### [`0045bf18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bf18.md) → [`0045c238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c238.md) FUN_0045c238

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
      "definition_site": "0045c250",
      "incomplete_value": false,
      "site": "0045c25c",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045bf30",
      "incomplete_value": false,
      "site": "0045bf3c",
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
            "const:c10:8"
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
      "0045c25c",
      "DATA",
      [
        "storage",
        "00c63c10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045c25c",
      "DATA",
      [
        "storage",
        "00c64be0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045bf2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bf18.md#insn-0045bf2c) · [`0045bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bf18.md#insn-0045bf30) · [`0045bf60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bf18.md#insn-0045bf60)
- 新版 [`0045c24c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c238.md#insn-0045c24c) · [`0045c250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c238.md#insn-0045c250) · [`0045c280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c238.md#insn-0045c280)

~~~diff
- 0045bf2c ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045c24c ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045bf2c bytes 48400090
+ 0045c24c bytes 48400090
- 0045bf30 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 0045bf30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045bf30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045bf30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045c250 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 0045c250 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c250 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c250 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045bf30 bytes 08413091
+ 0045c250 bytes 08812f91
- 0045bf60 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045bf60 ["INT_ADD", "register:40f0:8", ["const:45bf60:8", "const:4:8"]]
- 0045bf60 ["CALLIND", null, ["register:0:8"]]
+ 0045c280 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045c280 ["INT_ADD", "register:40f0:8", ["const:45c280:8", "const:4:8"]]
+ 0045c280 ["CALLIND", null, ["register:0:8"]]
- 0045bf60 bytes 00013fd6
+ 0045c280 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ad98b9ceedad0b50ba2b356c76d82ac"></a>

### [`0045bf74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bf74.md) → [`0045c294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c294.md) FUN_0045c294

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
      "definition_site": "0045c2c0",
      "incomplete_value": false,
      "site": "0045c2c0",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045bfa0",
      "incomplete_value": false,
      "site": "0045bfa0",
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
            "const:c10:8"
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
      "0045c2c0",
      "DATA",
      [
        "storage",
        "00c63c10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045c2c0",
      "DATA",
      [
        "storage",
        "00c64be0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045bf88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bf74.md#insn-0045bf88) · [`0045bf94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bf74.md#insn-0045bf94) · [`0045bf98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bf74.md#insn-0045bf98)
- 新版 [`0045c2a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c294.md#insn-0045c2a8) · [`0045c2b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c294.md#insn-0045c2b4) · [`0045c2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c294.md#insn-0045c2b8)

~~~diff
- 0045bf88 ["INT_ADD", "register:40f0:8", ["const:45bf88:8", "const:4:8"]]
- 0045bf88 ["CALL", null, ["callee:00c58f30:8"]]
+ 0045c2a8 ["INT_ADD", "register:40f0:8", ["const:45c2a8:8", "const:4:8"]]
+ 0045c2a8 ["CALL", null, ["callee:00c58f30:8"]]
- 0045bf88 bytes f6ef1f94
+ 0045c2a8 bytes 22f31f94
- 0045bf94 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045c2b4 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045bf94 bytes 48400090
+ 0045c2b4 bytes 48400090
- 0045bf98 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 0045bf98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045bf98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045bf98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045c2b8 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 0045c2b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c2b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c2b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045bf98 bytes 08413091
+ 0045c2b8 bytes 08812f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f15564d7f4f55797b91b6bbbe5f4d3f"></a>

### [`0045bffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bffc.md) → [`0045c31c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c31c.md) FUN_0045c31c

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045c338",
      "incomplete_value": false,
      "site": "0045c338",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c018",
      "incomplete_value": false,
      "site": "0045c018",
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
            "const:c10:8"
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
      "0045c338",
      "DATA",
      [
        "storage",
        "00c63c10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045c338",
      "DATA",
      [
        "storage",
        "00c64be0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045c010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bffc.md#insn-0045c010) · [`0045c014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bffc.md#insn-0045c014) · [`0045c038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bffc.md#insn-0045c038)
- 新版 [`0045c330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c31c.md#insn-0045c330) · [`0045c334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c31c.md#insn-0045c334) · [`0045c358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c31c.md#insn-0045c358)

~~~diff
- 0045c010 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 0045c330 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0045c010 bytes 294000f0
+ 0045c330 bytes 49400090
- 0045c014 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 0045c014 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045c014 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045c014 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045c334 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 0045c334 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045c334 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045c334 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045c014 bytes 29413091
+ 0045c334 bytes 29812f91
- 0045c038 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045c038 ["INT_ADD", "register:40f0:8", ["const:45c038:8", "const:4:8"]]
- 0045c038 ["CALLIND", null, ["register:0:8"]]
+ 0045c358 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045c358 ["INT_ADD", "register:40f0:8", ["const:45c358:8", "const:4:8"]]
+ 0045c358 ["CALLIND", null, ["register:0:8"]]
- 0045c038 bytes 20013fd6
+ 0045c358 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69730caaaf4e1d002a75defc860218ad"></a>

### [`0045c0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c0f8.md) → [`0045c418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c418.md) FUN_0045c418

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.26% / 新版 97.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045c460",
      "incomplete_value": true,
      "site": "0045c460",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2b4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c140",
      "incomplete_value": true,
      "site": "0045c140",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e5:8"
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
      "definition_site": "0045c5e4",
      "incomplete_value": true,
      "site": "0045c5f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c2c4",
      "incomplete_value": true,
      "site": "0045c2d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dce:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0045c6c4",
      "incomplete_value": true,
      "site": "0045c6c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c3a4",
      "incomplete_value": true,
      "site": "0045c3a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee0:8"
              ]
            ]
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
      "0045c43c",
      "READ",
      [
        "storage",
        "002b71e5",
        null,
        "string"
      ]
    ],
    [
      "0045c5e4",
      "READ",
      [
        "storage",
        "002a1dce",
        null,
        "string"
      ]
    ],
    [
      "0045c6b0",
      "READ",
      [
        "storage",
        "0029fee0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0045c43c",
      "READ",
      [
        "storage",
        "002b72b4",
        null,
        "string"
      ]
    ],
    [
      "0045c5e4",
      "READ",
      [
        "storage",
        "002a1e0e",
        null,
        "string"
      ]
    ],
    [
      "0045c6b0",
      "READ",
      [
        "storage",
        "0029ff20",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045c114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c0f8.md#insn-0045c114) · [`0045c150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c0f8.md#insn-0045c150) · [`0045c16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c0f8.md#insn-0045c16c)
- 新版 [`0045c434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c418.md#insn-0045c434) · [`0045c470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c418.md#insn-0045c470) · [`0045c48c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c418.md#insn-0045c48c)

~~~diff
- 0045c114 ["COPY", "tmp:0:8", ["const:1e5:8"]]
- 0045c114 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045c114 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045c114 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045c434 ["COPY", "tmp:0:8", ["const:2b4:8"]]
+ 0045c434 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045c434 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045c434 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045c114 bytes 4a950791
+ 0045c434 bytes 4ad10a91
- 0045c150 ["INT_ADD", "register:40f0:8", ["const:45c150:8", "const:4:8"]]
- 0045c150 ["CALL", null, ["callee:004413ec:8"]]
+ 0045c470 ["INT_ADD", "register:40f0:8", ["const:45c470:8", "const:4:8"]]
+ 0045c470 ["CALL", null, ["callee:004413ec:8"]]
- 0045c150 bytes df93ff97
+ 0045c470 bytes df93ff97
- 0045c16c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045c16c ["INT_ADD", "register:40f0:8", ["const:45c16c:8", "const:4:8"]]
- 0045c16c ["CALLIND", null, ["register:0:8"]]
+ 0045c48c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045c48c ["INT_ADD", "register:40f0:8", ["const:45c48c:8", "const:4:8"]]
+ 0045c48c ["CALLIND", null, ["register:0:8"]]
- 0045c16c bytes 00013fd6
+ 0045c48c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1123a0d11a2e29081392b9c6ce8c9054"></a>

### [`0045c724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c724.md) → [`0045ca44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045ca44.md) FUN_0045ca44

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
      "definition_site": "0045ca50",
      "incomplete_value": false,
      "site": "0045ca5c",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c730",
      "incomplete_value": false,
      "site": "0045c73c",
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
            "const:ca0:8"
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
      "0045ca5c",
      "DATA",
      [
        "storage",
        "00c63ca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ca5c",
      "DATA",
      [
        "storage",
        "00c64c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045c72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c724.md#insn-0045c72c) · [`0045c730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c724.md#insn-0045c730)
- 新版 [`0045ca4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045ca44.md#insn-0045ca4c) · [`0045ca50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045ca44.md#insn-0045ca50)

~~~diff
- 0045c72c ["COPY", "register:4050:8", ["const:c63000:8"]]
+ 0045ca4c ["COPY", "register:4050:8", ["const:c64000:8"]]
- 0045c72c bytes 2a4000f0
+ 0045ca4c bytes 4a400090
- 0045c730 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 0045c730 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045c730 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045c730 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045ca50 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 0045ca50 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045ca50 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045ca50 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045c730 bytes 4a813291
+ 0045ca50 bytes 4ac13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0350ee7ddc6c3d4f97495877a497df88"></a>

### [`0045c768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c768.md) → [`0045ca88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045ca88.md) FUN_0045ca88

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
      "definition_site": "0045caa0",
      "incomplete_value": false,
      "site": "0045caac",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c780",
      "incomplete_value": false,
      "site": "0045c78c",
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
            "const:ca0:8"
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
      "0045caac",
      "DATA",
      [
        "storage",
        "00c63ca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045caac",
      "DATA",
      [
        "storage",
        "00c64c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045c77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c768.md#insn-0045c77c) · [`0045c780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c768.md#insn-0045c780) · [`0045c7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c768.md#insn-0045c7b0)
- 新版 [`0045ca9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045ca88.md#insn-0045ca9c) · [`0045caa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045ca88.md#insn-0045caa0) · [`0045cad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045ca88.md#insn-0045cad0)

~~~diff
- 0045c77c ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045ca9c ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045c77c bytes 284000f0
+ 0045ca9c bytes 48400090
- 0045c780 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 0045c780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045c780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045c780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045caa0 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 0045caa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045caa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045caa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045c780 bytes 08813291
+ 0045caa0 bytes 08c13191
- 0045c7b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045c7b0 ["INT_ADD", "register:40f0:8", ["const:45c7b0:8", "const:4:8"]]
- 0045c7b0 ["CALLIND", null, ["register:0:8"]]
+ 0045cad0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045cad0 ["INT_ADD", "register:40f0:8", ["const:45cad0:8", "const:4:8"]]
+ 0045cad0 ["CALLIND", null, ["register:0:8"]]
- 0045c7b0 bytes 00013fd6
+ 0045cad0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-394b499ffbbee6c80fd19ed96136ea64"></a>

### [`0045c7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c7c4.md) → [`0045cae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045cae4.md) FUN_0045cae4

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
      "definition_site": "0045cb10",
      "incomplete_value": false,
      "site": "0045cb10",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c7f0",
      "incomplete_value": false,
      "site": "0045c7f0",
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
            "const:ca0:8"
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
      "0045cb10",
      "DATA",
      [
        "storage",
        "00c63ca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045cb10",
      "DATA",
      [
        "storage",
        "00c64c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045c7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c7c4.md#insn-0045c7d8) · [`0045c7e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c7c4.md#insn-0045c7e4) · [`0045c7e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c7c4.md#insn-0045c7e8)
- 新版 [`0045caf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045cae4.md#insn-0045caf8) · [`0045cb04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045cae4.md#insn-0045cb04) · [`0045cb08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045cae4.md#insn-0045cb08)

~~~diff
- 0045c7d8 ["INT_ADD", "register:40f0:8", ["const:45c7d8:8", "const:4:8"]]
- 0045c7d8 ["CALL", null, ["callee:00c58f30:8"]]
+ 0045caf8 ["INT_ADD", "register:40f0:8", ["const:45caf8:8", "const:4:8"]]
+ 0045caf8 ["CALL", null, ["callee:00c58f30:8"]]
- 0045c7d8 bytes e2ed1f94
+ 0045caf8 bytes 0ef11f94
- 0045c7e4 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045cb04 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045c7e4 bytes 284000f0
+ 0045cb04 bytes 48400090
- 0045c7e8 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 0045c7e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045c7e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045c7e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045cb08 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 0045cb08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045cb08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045cb08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045c7e8 bytes 08813291
+ 0045cb08 bytes 08c13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75453af3143aa26cb820b6808e9104f2"></a>

### [`0045c84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c84c.md) → [`0045cb6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045cb6c.md) FUN_0045cb6c

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045cb88",
      "incomplete_value": false,
      "site": "0045cb88",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c868",
      "incomplete_value": false,
      "site": "0045c868",
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
            "const:ca0:8"
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
      "0045cb88",
      "DATA",
      [
        "storage",
        "00c63ca0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045cb88",
      "DATA",
      [
        "storage",
        "00c64c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045c860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c84c.md#insn-0045c860) · [`0045c864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c84c.md#insn-0045c864) · [`0045c888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c84c.md#insn-0045c888)
- 新版 [`0045cb80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045cb6c.md#insn-0045cb80) · [`0045cb84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045cb6c.md#insn-0045cb84) · [`0045cba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045cb6c.md#insn-0045cba8)

~~~diff
- 0045c860 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 0045cb80 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0045c860 bytes 294000f0
+ 0045cb80 bytes 49400090
- 0045c864 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 0045c864 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045c864 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045c864 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045cb84 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 0045cb84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045cb84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045cb84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045c864 bytes 29813291
+ 0045cb84 bytes 29c13191
- 0045c888 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045c888 ["INT_ADD", "register:40f0:8", ["const:45c888:8", "const:4:8"]]
- 0045c888 ["CALLIND", null, ["register:0:8"]]
+ 0045cba8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045cba8 ["INT_ADD", "register:40f0:8", ["const:45cba8:8", "const:4:8"]]
+ 0045cba8 ["CALLIND", null, ["register:0:8"]]
- 0045c888 bytes 20013fd6
+ 0045cba8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07e3538963fbade7858db4562ab10f13"></a>

### [`0045cdcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cdcc.md) → [`0045d0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d0ec.md) FUN_0045d0ec

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0045cad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cad8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`0045cdf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045cdf8.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0045d0f8",
      "incomplete_value": false,
      "site": "0045d0fc",
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
      "definition_site": "0045cdd8",
      "incomplete_value": false,
      "site": "0045cddc",
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
      "0045d0f8",
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
      "0045d0f8",
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

- 旧版 [`0045cddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cdcc.md#insn-0045cddc) · [`0045cdd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cdcc.md#insn-0045cdd4) · [`0045cdd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cdcc.md#insn-0045cdd8)
- 新版 [`0045d0fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d0ec.md#insn-0045d0fc) · [`0045d0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d0ec.md#insn-0045d0f4) · [`0045d0f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d0ec.md#insn-0045d0f8)

~~~diff
- 0045cddc ["INT_ADD", "register:40f0:8", ["const:45cddc:8", "const:4:8"]]
- 0045cddc ["CALL", null, ["callee:0043bad8:8"]]
+ 0045d0fc ["INT_ADD", "register:40f0:8", ["const:45d0fc:8", "const:4:8"]]
+ 0045d0fc ["CALL", null, ["callee:0043bad8:8"]]
- 0045cddc bytes 777aff97
+ 0045d0fc bytes 777aff97
- 0045cdd4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0045d0f4 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0045cdd4 bytes c0f2fff0
+ 0045d0f4 bytes c0f2fff0
- 0045cdd8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0045cdd8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0045cdd8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0045cdd8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0045d0f8 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0045d0f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0045d0f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0045d0f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0045cdd8 bytes 00303e91
+ 0045d0f8 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a810a74d12252142216df4c03fdf2d50"></a>

### [`0045cde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cde0.md) → [`0045d100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d100.md) FUN_0045d100

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
      "definition_site": "0045d10c",
      "incomplete_value": false,
      "site": "0045d118",
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
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045cdec",
      "incomplete_value": false,
      "site": "0045cdf8",
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
            "const:d30:8"
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
      "0045d118",
      "DATA",
      [
        "storage",
        "00c63d30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045d118",
      "DATA",
      [
        "storage",
        "00c64d00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045cde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cde0.md#insn-0045cde8) · [`0045cdec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cde0.md#insn-0045cdec)
- 新版 [`0045d108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d100.md#insn-0045d108) · [`0045d10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d100.md#insn-0045d10c)

~~~diff
- 0045cde8 ["COPY", "register:4050:8", ["const:c63000:8"]]
+ 0045d108 ["COPY", "register:4050:8", ["const:c64000:8"]]
- 0045cde8 bytes 2a4000f0
+ 0045d108 bytes 2a4000f0
- 0045cdec ["COPY", "tmp:0:8", ["const:d30:8"]]
- 0045cdec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045cdec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045cdec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045d10c ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 0045d10c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045d10c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045d10c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045cdec bytes 4ac13491
+ 0045d10c bytes 4a013491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9e57b092cc08119c3280981e904047c"></a>

### [`0045ce24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045ce24.md) → [`0045d144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d144.md) FUN_0045d144

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
      "definition_site": "0045d15c",
      "incomplete_value": false,
      "site": "0045d168",
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
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ce3c",
      "incomplete_value": false,
      "site": "0045ce48",
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
            "const:d30:8"
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
      "0045d168",
      "DATA",
      [
        "storage",
        "00c63d30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045d168",
      "DATA",
      [
        "storage",
        "00c64d00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ce38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045ce24.md#insn-0045ce38) · [`0045ce3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045ce24.md#insn-0045ce3c) · [`0045ce6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045ce24.md#insn-0045ce6c)
- 新版 [`0045d158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d144.md#insn-0045d158) · [`0045d15c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d144.md#insn-0045d15c) · [`0045d18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d144.md#insn-0045d18c)

~~~diff
- 0045ce38 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045d158 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045ce38 bytes 284000f0
+ 0045d158 bytes 284000f0
- 0045ce3c ["COPY", "tmp:0:8", ["const:d30:8"]]
- 0045ce3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045ce3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045ce3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045d15c ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 0045d15c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045d15c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045d15c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045ce3c bytes 08c13491
+ 0045d15c bytes 08013491
- 0045ce6c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045ce6c ["INT_ADD", "register:40f0:8", ["const:45ce6c:8", "const:4:8"]]
- 0045ce6c ["CALLIND", null, ["register:0:8"]]
+ 0045d18c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045d18c ["INT_ADD", "register:40f0:8", ["const:45d18c:8", "const:4:8"]]
+ 0045d18c ["CALLIND", null, ["register:0:8"]]
- 0045ce6c bytes 00013fd6
+ 0045d18c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4d51d4d2f830139135112fdb12c44d6"></a>

### [`0045ce80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045ce80.md) → [`0045d1a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d1a0.md) FUN_0045d1a0

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
      "definition_site": "0045d1cc",
      "incomplete_value": false,
      "site": "0045d1cc",
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
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ceac",
      "incomplete_value": false,
      "site": "0045ceac",
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
            "const:d30:8"
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
      "0045d1cc",
      "DATA",
      [
        "storage",
        "00c63d30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045d1cc",
      "DATA",
      [
        "storage",
        "00c64d00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045ce80.md#insn-0045ce94) · [`0045cea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045ce80.md#insn-0045cea0) · [`0045cea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045ce80.md#insn-0045cea4)
- 新版 [`0045d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d1a0.md#insn-0045d1b4) · [`0045d1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d1a0.md#insn-0045d1c0) · [`0045d1c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d1a0.md#insn-0045d1c4)

~~~diff
- 0045ce94 ["INT_ADD", "register:40f0:8", ["const:45ce94:8", "const:4:8"]]
- 0045ce94 ["CALL", null, ["callee:00c58f30:8"]]
+ 0045d1b4 ["INT_ADD", "register:40f0:8", ["const:45d1b4:8", "const:4:8"]]
+ 0045d1b4 ["CALL", null, ["callee:00c58f30:8"]]
- 0045ce94 bytes 33ec1f94
+ 0045d1b4 bytes 5fef1f94
- 0045cea0 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045d1c0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045cea0 bytes 284000f0
+ 0045d1c0 bytes 284000f0
- 0045cea4 ["COPY", "tmp:0:8", ["const:d30:8"]]
- 0045cea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045cea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045cea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045d1c4 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 0045d1c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045d1c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045d1c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045cea4 bytes 08c13491
+ 0045d1c4 bytes 08013491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0752fe6154605517f017227bc107b836"></a>

### [`0045cf08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cf08.md) → [`0045d228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d228.md) FUN_0045d228

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045d244",
      "incomplete_value": false,
      "site": "0045d244",
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
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045cf24",
      "incomplete_value": false,
      "site": "0045cf24",
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
            "const:d30:8"
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
      "0045d244",
      "DATA",
      [
        "storage",
        "00c63d30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045d244",
      "DATA",
      [
        "storage",
        "00c64d00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045cf1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cf08.md#insn-0045cf1c) · [`0045cf20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cf08.md#insn-0045cf20) · [`0045cf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cf08.md#insn-0045cf44)
- 新版 [`0045d23c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d228.md#insn-0045d23c) · [`0045d240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d228.md#insn-0045d240) · [`0045d264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045d228.md#insn-0045d264)

~~~diff
- 0045cf1c ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 0045d23c ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0045cf1c bytes 294000f0
+ 0045d23c bytes 294000f0
- 0045cf20 ["COPY", "tmp:0:8", ["const:d30:8"]]
- 0045cf20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045cf20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045cf20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045d240 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 0045d240 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045d240 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045d240 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045cf20 bytes 29c13491
+ 0045d240 bytes 29013491
- 0045cf44 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045cf44 ["INT_ADD", "register:40f0:8", ["const:45cf44:8", "const:4:8"]]
- 0045cf44 ["CALLIND", null, ["register:0:8"]]
+ 0045d264 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045d264 ["INT_ADD", "register:40f0:8", ["const:45d264:8", "const:4:8"]]
+ 0045d264 ["CALLIND", null, ["register:0:8"]]
- 0045cf44 bytes 20013fd6
+ 0045d264 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18451802fd7cf79cbfd90d415f96d5c4"></a>

### [`0045d7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d7d0.md) → [`0045daf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045daf0.md) FUN_0045daf0

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
      "definition_site": "0045dafc",
      "incomplete_value": false,
      "site": "0045db08",
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
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045d7dc",
      "incomplete_value": false,
      "site": "0045d7e8",
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
            "const:db0:8"
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
      "0045db08",
      "DATA",
      [
        "storage",
        "00c63db0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045db08",
      "DATA",
      [
        "storage",
        "00c64d80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045d7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d7d0.md#insn-0045d7d8) · [`0045d7dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d7d0.md#insn-0045d7dc)
- 新版 [`0045daf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045daf0.md#insn-0045daf8) · [`0045dafc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045daf0.md#insn-0045dafc)

~~~diff
- 0045d7d8 ["COPY", "register:4050:8", ["const:c63000:8"]]
+ 0045daf8 ["COPY", "register:4050:8", ["const:c64000:8"]]
- 0045d7d8 bytes 2a4000d0
+ 0045daf8 bytes 2a4000f0
- 0045d7dc ["COPY", "tmp:0:8", ["const:db0:8"]]
- 0045d7dc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045d7dc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045d7dc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045dafc ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 0045dafc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045dafc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045dafc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045d7dc bytes 4ac13691
+ 0045dafc bytes 4a013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8a29f631b3eefe12c4c23bd2ff8efca"></a>

### [`0045d814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d814.md) → [`0045db34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045db34.md) FUN_0045db34

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
      "definition_site": "0045db4c",
      "incomplete_value": false,
      "site": "0045db58",
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
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045d82c",
      "incomplete_value": false,
      "site": "0045d838",
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
            "const:db0:8"
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
      "0045db58",
      "DATA",
      [
        "storage",
        "00c63db0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045db58",
      "DATA",
      [
        "storage",
        "00c64d80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045d828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d814.md#insn-0045d828) · [`0045d82c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d814.md#insn-0045d82c) · [`0045d85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d814.md#insn-0045d85c)
- 新版 [`0045db48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045db34.md#insn-0045db48) · [`0045db4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045db34.md#insn-0045db4c) · [`0045db7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045db34.md#insn-0045db7c)

~~~diff
- 0045d828 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045db48 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045d828 bytes 284000d0
+ 0045db48 bytes 284000f0
- 0045d82c ["COPY", "tmp:0:8", ["const:db0:8"]]
- 0045d82c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045d82c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045d82c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045db4c ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 0045db4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045db4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045db4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045d82c bytes 08c13691
+ 0045db4c bytes 08013691
- 0045d85c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d85c ["INT_ADD", "register:40f0:8", ["const:45d85c:8", "const:4:8"]]
- 0045d85c ["CALLIND", null, ["register:0:8"]]
+ 0045db7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045db7c ["INT_ADD", "register:40f0:8", ["const:45db7c:8", "const:4:8"]]
+ 0045db7c ["CALLIND", null, ["register:0:8"]]
- 0045d85c bytes 00013fd6
+ 0045db7c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58a12d2536326f239f356cd136f8e4b9"></a>

### [`0045d870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d870.md) → [`0045db90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045db90.md) FUN_0045db90

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
      "definition_site": "0045dbbc",
      "incomplete_value": false,
      "site": "0045dbbc",
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
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045d89c",
      "incomplete_value": false,
      "site": "0045d89c",
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
            "const:db0:8"
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
      "0045dbbc",
      "DATA",
      [
        "storage",
        "00c63db0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045dbbc",
      "DATA",
      [
        "storage",
        "00c64d80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045d884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d870.md#insn-0045d884) · [`0045d890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d870.md#insn-0045d890) · [`0045d894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d870.md#insn-0045d894)
- 新版 [`0045dba4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045db90.md#insn-0045dba4) · [`0045dbb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045db90.md#insn-0045dbb0) · [`0045dbb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045db90.md#insn-0045dbb4)

~~~diff
- 0045d884 ["INT_ADD", "register:40f0:8", ["const:45d884:8", "const:4:8"]]
- 0045d884 ["CALL", null, ["callee:00c58f30:8"]]
+ 0045dba4 ["INT_ADD", "register:40f0:8", ["const:45dba4:8", "const:4:8"]]
+ 0045dba4 ["CALL", null, ["callee:00c58f30:8"]]
- 0045d884 bytes b7e91f94
+ 0045dba4 bytes e3ec1f94
- 0045d890 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045dbb0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045d890 bytes 284000d0
+ 0045dbb0 bytes 284000f0
- 0045d894 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 0045d894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045d894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045d894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045dbb4 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 0045dbb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045dbb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045dbb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045d894 bytes 08c13691
+ 0045dbb4 bytes 08013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33ebd6eb940145235589a515d3422abc"></a>

### [`0045d8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d8f8.md) → [`0045dc18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045dc18.md) FUN_0045dc18

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045dc34",
      "incomplete_value": false,
      "site": "0045dc34",
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
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045d914",
      "incomplete_value": false,
      "site": "0045d914",
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
            "const:db0:8"
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
      "0045dc34",
      "DATA",
      [
        "storage",
        "00c63db0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045dc34",
      "DATA",
      [
        "storage",
        "00c64d80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045d90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d8f8.md#insn-0045d90c) · [`0045d910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d8f8.md#insn-0045d910) · [`0045d934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d8f8.md#insn-0045d934)
- 新版 [`0045dc2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045dc18.md#insn-0045dc2c) · [`0045dc30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045dc18.md#insn-0045dc30) · [`0045dc54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045dc18.md#insn-0045dc54)

~~~diff
- 0045d90c ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 0045dc2c ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0045d90c bytes 294000d0
+ 0045dc2c bytes 294000f0
- 0045d910 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 0045d910 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045d910 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045d910 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045dc30 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 0045dc30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045dc30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045dc30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045d910 bytes 29c13691
+ 0045dc30 bytes 29013691
- 0045d934 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045d934 ["INT_ADD", "register:40f0:8", ["const:45d934:8", "const:4:8"]]
- 0045d934 ["CALLIND", null, ["register:0:8"]]
+ 0045dc54 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045dc54 ["INT_ADD", "register:40f0:8", ["const:45dc54:8", "const:4:8"]]
+ 0045dc54 ["CALLIND", null, ["register:0:8"]]
- 0045d934 bytes 20013fd6
+ 0045dc54 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-747cb38b45e617e31bef44e22cc31fd3"></a>

### [`0045d9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d9f4.md) → [`0045dd14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045dd14.md) FUN_0045dd14

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00a1b6a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a1b/00a1b6a4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0045de28",
      "incomplete_value": false,
      "site": "0045de28",
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
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045db08",
      "incomplete_value": false,
      "site": "0045db08",
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
            "const:c18:8"
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
      "definition_site": "0045de2c",
      "incomplete_value": false,
      "site": "0045de2c",
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
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045db0c",
      "incomplete_value": false,
      "site": "0045db0c",
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
            "const:c30:8"
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
      "definition_site": "0045dd70",
      "incomplete_value": true,
      "site": "0045dd70",
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
      "definition_site": "0045da50",
      "incomplete_value": true,
      "site": "0045da50",
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
      "0045dd68",
      "READ",
      [
        "storage",
        "00ca4c10",
        null,
        "undefined8"
      ]
    ],
    [
      "0045dd68",
      "READ",
      [
        "storage",
        "00ca4c18",
        null,
        "undefined8"
      ]
    ],
    [
      "0045ddd4",
      "READ",
      [
        "storage",
        "00ca4c10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0045dd68",
      "READ",
      [
        "storage",
        "00ca5bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "0045dd68",
      "READ",
      [
        "storage",
        "00ca5bd8",
        null,
        "undefined8"
      ]
    ],
    [
      "0045ddd4",
      "READ",
      [
        "storage",
        "00ca5bd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045db08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d9f4.md#insn-0045db08) · [`0045db0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d9f4.md#insn-0045db0c) · [`0045da24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d9f4.md#insn-0045da24)
- 新版 [`0045de28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045dd14.md#insn-0045de28) · [`0045de2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045dd14.md#insn-0045de2c) · [`0045dd44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045dd14.md#insn-0045dd44)

~~~diff
- 0045db08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c18:8"]]
- 0045db08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0045de28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd8:8"]]
+ 0045de28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0045db08 bytes 130d06f9
+ 0045de28 bytes 13ed05f9
- 0045db0c ["COPY", "tmp:0:4", ["const:0:4"]]
- 0045db0c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0045db0c ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:c30:8"]]
- 0045db0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0045de2c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0045de2c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0045de2c ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:bf0:8"]]
+ 0045de2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0045db0c bytes 3fc13039
+ 0045de2c bytes 3fc12f39
- 0045da24 ["INT_ADD", "register:40f0:8", ["const:45da24:8", "const:4:8"]]
- 0045da24 ["CALL", null, ["callee:008524fc:8"]]
+ 0045dd44 ["INT_ADD", "register:40f0:8", ["const:45dd44:8", "const:4:8"]]
+ 0045dd44 ["CALL", null, ["callee:008524fc:8"]]
- 0045da24 bytes cbce0f94
+ 0045dd44 bytes eed10f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-229df317d29524abb3be58717bb7080b"></a>

### [`0045deac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045deac.md) → [`0045e1cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e1cc.md) FUN_0045e1cc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0045dbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045dbb8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`0045ded8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045ded8.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "0045e1d8",
      "incomplete_value": false,
      "site": "0045e1dc",
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
      "definition_site": "0045deb8",
      "incomplete_value": false,
      "site": "0045debc",
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
      "0045e1d8",
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
      "0045e1d8",
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

- 旧版 [`0045debc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045deac.md#insn-0045debc) · [`0045deb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045deac.md#insn-0045deb4) · [`0045deb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045deac.md#insn-0045deb8)
- 新版 [`0045e1dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e1cc.md#insn-0045e1dc) · [`0045e1d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e1cc.md#insn-0045e1d4) · [`0045e1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e1cc.md#insn-0045e1d8)

~~~diff
- 0045debc ["INT_ADD", "register:40f0:8", ["const:45debc:8", "const:4:8"]]
- 0045debc ["CALL", null, ["callee:0043bad8:8"]]
+ 0045e1dc ["INT_ADD", "register:40f0:8", ["const:45e1dc:8", "const:4:8"]]
+ 0045e1dc ["CALL", null, ["callee:0043bad8:8"]]
- 0045debc bytes 3f76ff97
+ 0045e1dc bytes 3f76ff97
- 0045deb4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0045e1d4 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0045deb4 bytes c0f2ffd0
+ 0045e1d4 bytes c0f2ffd0
- 0045deb8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0045deb8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0045deb8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0045deb8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0045e1d8 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0045e1d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0045e1d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0045e1d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0045deb8 bytes 00303e91
+ 0045e1d8 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccaf3b931d40cdf05e7c736524d1c055"></a>

### [`0045dec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045dec4.md) → [`0045e1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e1e4.md) FUN_0045e1e4

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
      "definition_site": "0045e208",
      "incomplete_value": false,
      "site": "0045e208",
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
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045dee8",
      "incomplete_value": false,
      "site": "0045dee8",
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
            "const:e40:8"
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
      "0045e208",
      "DATA",
      [
        "storage",
        "00c63e40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045e208",
      "DATA",
      [
        "storage",
        "00c64e10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ded8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045dec4.md#insn-0045ded8) · [`0045dee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045dec4.md#insn-0045dee0) · [`0045dee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045dec4.md#insn-0045dee4)
- 新版 [`0045e1f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e1e4.md#insn-0045e1f8) · [`0045e200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e1e4.md#insn-0045e200) · [`0045e204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e1e4.md#insn-0045e204)

~~~diff
- 0045ded8 ["INT_ADD", "register:40f0:8", ["const:45ded8:8", "const:4:8"]]
- 0045ded8 ["CALL", null, ["callee:00c58f30:8"]]
+ 0045e1f8 ["INT_ADD", "register:40f0:8", ["const:45e1f8:8", "const:4:8"]]
+ 0045e1f8 ["CALL", null, ["callee:00c58f30:8"]]
- 0045ded8 bytes 22e81f94
+ 0045e1f8 bytes 4eeb1f94
- 0045dee0 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045e200 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045dee0 bytes 284000d0
+ 0045e200 bytes 284000d0
- 0045dee4 ["COPY", "tmp:0:8", ["const:e40:8"]]
- 0045dee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045dee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045dee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045e204 ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 0045e204 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045e204 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045e204 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045dee4 bytes 08013991
+ 0045e204 bytes 08413891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56db5ac3b43f424bba56371272603a41"></a>

### [`0045def8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045def8.md) → [`0045e218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e218.md) FUN_0045e218

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
      "definition_site": "0045e224",
      "incomplete_value": false,
      "site": "0045e224",
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
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045df04",
      "incomplete_value": false,
      "site": "0045df04",
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
            "const:e40:8"
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
      "0045e224",
      "DATA",
      [
        "storage",
        "00c63e40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045e224",
      "DATA",
      [
        "storage",
        "00c64e10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045defc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045def8.md#insn-0045defc) · [`0045df00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045def8.md#insn-0045df00)
- 新版 [`0045e21c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e218.md#insn-0045e21c) · [`0045e220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e218.md#insn-0045e220)

~~~diff
- 0045defc ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 0045e21c ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0045defc bytes 294000d0
+ 0045e21c bytes 294000d0
- 0045df00 ["COPY", "tmp:0:8", ["const:e40:8"]]
- 0045df00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045df00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045df00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045e220 ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 0045e220 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045e220 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045e220 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045df00 bytes 29013991
+ 0045e220 bytes 29413891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cdd6908a2fa5bd34a486c91e4bfea0a"></a>

### [`0045df14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045df14.md) → [`0045e234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e234.md) FUN_0045e234

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59180.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.91% / 新版 93.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 1件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045e288",
      "incomplete_value": true,
      "site": "0045e288",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2b4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045df68",
      "incomplete_value": true,
      "site": "0045df68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e5:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "0045e614",
      "incomplete_value": false,
      "site": "0045e614",
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
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e2f4",
      "incomplete_value": false,
      "site": "0045e2f4",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0045e618",
      "incomplete_value": false,
      "site": "0045e618",
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
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e2f8",
      "incomplete_value": false,
      "site": "0045e2f8",
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
            "const:c88:8"
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
      "0045e254",
      "PARAM",
      [
        "storage",
        "00ca4c34",
        null,
        null
      ]
    ],
    [
      "0045e274",
      "READ",
      [
        "storage",
        "002b71e5",
        null,
        "string"
      ]
    ],
    [
      "0045e39c",
      "READ",
      [
        "storage",
        "00ca4c68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0045e254",
      "PARAM",
      [
        "storage",
        "00ca5bf4",
        null,
        null
      ]
    ],
    [
      "0045e274",
      "READ",
      [
        "storage",
        "002b72b4",
        null,
        "string"
      ]
    ],
    [
      "0045e39c",
      "READ",
      [
        "storage",
        "00ca5c28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045df44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045df14.md#insn-0045df44) · [`0045dfe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045df14.md#insn-0045dfe4) · [`0045e06c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045df14.md#insn-0045e06c)
- 新版 [`0045e264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e234.md#insn-0045e264) · [`0045e304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e234.md#insn-0045e304) · [`0045e38c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e234.md#insn-0045e38c)

~~~diff
- 0045df44 ["INT_ADD", "register:40f0:8", ["const:45df44:8", "const:4:8"]]
- 0045df44 ["CALL", null, ["callee:00c59180:8"]]
+ 0045e264 ["INT_ADD", "register:40f0:8", ["const:45e264:8", "const:4:8"]]
+ 0045e264 ["CALL", null, ["callee:00c59180:8"]]
- 0045df44 bytes 9be81f94
+ 0045e264 bytes c7eb1f94
- 0045dfe4 ["INT_ADD", "register:40f0:8", ["const:45dfe4:8", "const:4:8"]]
- 0045dfe4 ["CALL", null, ["callee:004413ec:8"]]
+ 0045e304 ["INT_ADD", "register:40f0:8", ["const:45e304:8", "const:4:8"]]
+ 0045e304 ["CALL", null, ["callee:004413ec:8"]]
- 0045dfe4 bytes 3a8cff97
+ 0045e304 bytes 3a8cff97
- 0045e06c ["INT_ADD", "register:40f0:8", ["const:45e06c:8", "const:4:8"]]
- 0045e06c ["CALL", null, ["callee:00c58f50:8"]]
+ 0045e38c ["INT_ADD", "register:40f0:8", ["const:45e38c:8", "const:4:8"]]
+ 0045e38c ["CALL", null, ["callee:00c58f50:8"]]
- 0045e06c bytes c5e71f94
+ 0045e38c bytes f1ea1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96f724cf6a645fe3e962c91a544a0aaf"></a>

### [`0045e4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e4b0.md) → [`0045e7d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e7d0.md) FUN_0045e7d0

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
      "definition_site": "0045e7f4",
      "incomplete_value": false,
      "site": "0045e7f4",
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
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e4d4",
      "incomplete_value": false,
      "site": "0045e4d4",
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
            "const:ec0:8"
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
      "0045e7f4",
      "DATA",
      [
        "storage",
        "00c63ec0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045e7f4",
      "DATA",
      [
        "storage",
        "00c64e90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045e4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e4b0.md#insn-0045e4c4) · [`0045e4cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e4b0.md#insn-0045e4cc) · [`0045e4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e4b0.md#insn-0045e4d0)
- 新版 [`0045e7e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e7d0.md#insn-0045e7e4) · [`0045e7ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e7d0.md#insn-0045e7ec) · [`0045e7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e7d0.md#insn-0045e7f0)

~~~diff
- 0045e4c4 ["INT_ADD", "register:40f0:8", ["const:45e4c4:8", "const:4:8"]]
- 0045e4c4 ["CALL", null, ["callee:00c58f30:8"]]
+ 0045e7e4 ["INT_ADD", "register:40f0:8", ["const:45e7e4:8", "const:4:8"]]
+ 0045e7e4 ["CALL", null, ["callee:00c58f30:8"]]
- 0045e4c4 bytes a7e61f94
+ 0045e7e4 bytes d3e91f94
- 0045e4cc ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045e7ec ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045e4cc bytes 284000b0
+ 0045e7ec bytes 284000d0
- 0045e4d0 ["COPY", "tmp:0:8", ["const:ec0:8"]]
- 0045e4d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045e4d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045e4d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045e7f0 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 0045e7f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045e7f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045e7f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045e4d0 bytes 08013b91
+ 0045e7f0 bytes 08413a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ebfcb9832417178a554f125bddfeb16"></a>

### [`0045e4e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e4e4.md) → [`0045e804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e804.md) FUN_0045e804

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
      "definition_site": "0045e810",
      "incomplete_value": false,
      "site": "0045e810",
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
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e4f0",
      "incomplete_value": false,
      "site": "0045e4f0",
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
            "const:ec0:8"
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
      "0045e810",
      "DATA",
      [
        "storage",
        "00c63ec0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045e810",
      "DATA",
      [
        "storage",
        "00c64e90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045e4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e4e4.md#insn-0045e4e8) · [`0045e4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e4e4.md#insn-0045e4ec)
- 新版 [`0045e808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e804.md#insn-0045e808) · [`0045e80c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e804.md#insn-0045e80c)

~~~diff
- 0045e4e8 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 0045e808 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0045e4e8 bytes 294000b0
+ 0045e808 bytes 294000d0
- 0045e4ec ["COPY", "tmp:0:8", ["const:ec0:8"]]
- 0045e4ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045e4ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045e4ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045e80c ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 0045e80c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045e80c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045e80c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045e4ec bytes 29013b91
+ 0045e80c bytes 29413a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17d7e8e3d6111225d0c6d209375a944e"></a>

### [`0045e500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e500.md) → [`0045e820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e820.md) FUN_0045e820

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00768a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768a80.md) [`0076911c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/0076911c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00768e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/00768e5c.md) [`007694f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/007694f8.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_value, call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_target` 2件, `store_destination` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0045e928",
      "incomplete_value": false,
      "site": "0045e928",
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
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e608",
      "incomplete_value": false,
      "site": "0045e608",
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
            "const:c70:8"
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
      "definition_site": "0045e92c",
      "incomplete_value": false,
      "site": "0045e92c",
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
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e60c",
      "incomplete_value": false,
      "site": "0045e60c",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0045e888",
      "incomplete_value": true,
      "site": "0045e888",
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
      "definition_site": "0045e568",
      "incomplete_value": true,
      "site": "0045e568",
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
      "0045e85c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768a80"
      ]
    ],
    [
      "unmatched:0045e540",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ],
    [
      "0045e864",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0076911c"
      ]
    ]
  ],
  "added": [
    [
      "0045e85c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768e5c"
      ]
    ],
    [
      "0045e860",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ],
    [
      "0045e864",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007694f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045e53c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e500.md#insn-0045e53c) · [`0045e540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e500.md#insn-0045e540) · [`0045e544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e500.md#insn-0045e544)
- 新版 [`0045e85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e820.md#insn-0045e85c) · [`0045e864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e820.md#insn-0045e864)

~~~diff
- 0045e53c ["INT_ADD", "register:40f0:8", ["const:45e53c:8", "const:4:8"]]
- 0045e53c ["CALL", null, ["ram:768a80:8"]]
+ 0045e85c ["INT_ADD", "register:40f0:8", ["const:45e85c:8", "const:4:8"]]
+ 0045e85c ["CALL", null, ["ram:768e5c:8"]]
- 0045e53c bytes 51290c94
+ 0045e85c bytes 80290c94
- 0045e540 ["INT_ADD", "register:40f0:8", ["const:45e540:8", "const:4:8"]]
- 0045e540 ["CALL", null, ["callee:008524fc:8"]]
- 0045e540 bytes 04cc0f94
- 0045e544 ["INT_ADD", "register:40f0:8", ["const:45e544:8", "const:4:8"]]
- 0045e544 ["CALL", null, ["ram:76911c:8"]]
+ 0045e864 ["INT_ADD", "register:40f0:8", ["const:45e864:8", "const:4:8"]]
+ 0045e864 ["CALL", null, ["ram:7694f8:8"]]
- 0045e544 bytes f62a0c94
+ 0045e864 bytes 252b0c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f4831ed35719091fa76c90a6b3c3ea7"></a>

### [`0045e6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e6a8.md) → [`0045e9c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e9c8.md) FUN_0045e9c8

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0045f3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f3a8.md) · 呼出先 6件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`0045ec24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ec24.md) [`00597f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f0c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0045f6c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f6c8.md) · 呼出先 6件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0045ef44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045ef44.md) [`0059822c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/0059822c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.64% / 新版 88.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045ea74",
      "incomplete_value": true,
      "site": "0045ea84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fa8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e754",
      "incomplete_value": true,
      "site": "0045e764",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ed9:8"
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
      "definition_site": "0045eaec",
      "incomplete_value": true,
      "site": "0045eaec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f99:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e7cc",
      "incomplete_value": true,
      "site": "0045e7cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f59:8"
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
      "definition_site": "0045eb88",
      "incomplete_value": true,
      "site": "0045eba0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0045e868",
      "incomplete_value": true,
      "site": "0045e880",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0045ea74",
      "READ",
      [
        "storage",
        "002b5ed9",
        null,
        "string"
      ]
    ],
    [
      "0045ead8",
      "READ",
      [
        "storage",
        "002a0f59",
        null,
        "string"
      ]
    ],
    [
      "0045eb88",
      "READ",
      [
        "storage",
        "002c26a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0045ea74",
      "READ",
      [
        "storage",
        "002b5fa8",
        null,
        "string"
      ]
    ],
    [
      "0045ead8",
      "READ",
      [
        "storage",
        "002a0f99",
        null,
        "string"
      ]
    ],
    [
      "0045eb88",
      "READ",
      [
        "storage",
        "002c26f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045e708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e6a8.md#insn-0045e708) · [`0045e728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e6a8.md#insn-0045e728) · [`0045e73c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e6a8.md#insn-0045e73c)
- 新版 [`0045ea28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e9c8.md#insn-0045ea28) · [`0045ea48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e9c8.md#insn-0045ea48) · [`0045ea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e9c8.md#insn-0045ea5c)

~~~diff
- 0045e708 ["INT_ADD", "register:40f0:8", ["const:45e708:8", "const:4:8"]]
- 0045e708 ["CALL", null, ["callee:004413ec:8"]]
+ 0045ea28 ["INT_ADD", "register:40f0:8", ["const:45ea28:8", "const:4:8"]]
+ 0045ea28 ["CALL", null, ["callee:004413ec:8"]]
- 0045e708 bytes 718aff97
+ 0045ea28 bytes 718aff97
- 0045e728 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045e728 ["INT_ADD", "register:40f0:8", ["const:45e728:8", "const:4:8"]]
- 0045e728 ["CALLIND", null, ["register:0:8"]]
+ 0045ea48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045ea48 ["INT_ADD", "register:40f0:8", ["const:45ea48:8", "const:4:8"]]
+ 0045ea48 ["CALLIND", null, ["register:0:8"]]
- 0045e728 bytes 00013fd6
+ 0045ea48 bytes 00013fd6
- 0045e73c ["INT_ADD", "register:40f0:8", ["const:45e73c:8", "const:4:8"]]
- 0045e73c ["CALL", null, ["callee:00c58f50:8"]]
+ 0045ea5c ["INT_ADD", "register:40f0:8", ["const:45ea5c:8", "const:4:8"]]
+ 0045ea5c ["CALL", null, ["callee:00c58f50:8"]]
- 0045e73c bytes 11e61f94
+ 0045ea5c bytes 3de91f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-419786465a8662358da2d488d6223a4d"></a>

### [`0045ec24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ec24.md) → [`0045ef44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045ef44.md) FUN_0045ef44

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0045e6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e6a8.md) · 呼出先 5件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00597f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f0c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0045e9c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e9c8.md) · 呼出先 5件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0059822c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/0059822c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.03% / 新版 82.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045ef90",
      "incomplete_value": true,
      "site": "0045ef90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ec70",
      "incomplete_value": true,
      "site": "0045ec70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a6e:8"
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
      "definition_site": "0045ef94",
      "incomplete_value": true,
      "site": "0045ef94",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0045ec74",
      "incomplete_value": true,
      "site": "0045ec74",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045effc",
      "incomplete_value": true,
      "site": "0045effc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fba:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ecdc",
      "incomplete_value": true,
      "site": "0045ecdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eeb:8"
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
      "0045ef80",
      "READ",
      [
        "storage",
        "002a8a6e",
        null,
        "string"
      ]
    ],
    [
      "0045ef84",
      "READ",
      [
        "storage",
        "002a8a74",
        null,
        "string"
      ]
    ],
    [
      "0045efe8",
      "READ",
      [
        "storage",
        "002b5eeb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0045ef80",
      "READ",
      [
        "storage",
        "002a8bc6",
        null,
        "string"
      ]
    ],
    [
      "0045ef84",
      "READ",
      [
        "storage",
        "002a8bcc",
        null,
        "string"
      ]
    ],
    [
      "0045efe8",
      "READ",
      [
        "storage",
        "002b5fba",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ec58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ec24.md#insn-0045ec58) · [`0045ec5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ec24.md#insn-0045ec5c) · [`0045ec84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ec24.md#insn-0045ec84)
- 新版 [`0045ef78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045ef44.md#insn-0045ef78) · [`0045efa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045ef44.md#insn-0045efa4)

~~~diff
- 0045ec58 ["COPY", "tmp:0:8", ["const:a6e:8"]]
- 0045ec58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045ec58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045ec58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045ef78 ["COPY", "tmp:0:8", ["const:bc6:8"]]
+ 0045ef78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ef78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ef78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045ec58 bytes 29b92991
+ 0045ef78 bytes 29192f91
- 0045ec5c ["COPY", "register:40b0:8", ["register:4000:8"]]
- 0045ec5c bytes f60300aa
- 0045ec84 ["INT_ADD", "register:40f0:8", ["const:45ec84:8", "const:4:8"]]
- 0045ec84 ["CALL", null, ["callee:004413ec:8"]]
+ 0045efa4 ["INT_ADD", "register:40f0:8", ["const:45efa4:8", "const:4:8"]]
+ 0045efa4 ["CALL", null, ["callee:004413ec:8"]]
- 0045ec84 bytes 1289ff97
+ 0045efa4 bytes 1289ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c921fd168d53dcdce408223cbb186235"></a>

### [`0045ee5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ee5c.md) → [`0045f17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f17c.md) FUN_0045f17c

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
      "definition_site": "0045f180",
      "incomplete_value": false,
      "site": "0045f184",
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
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ee60",
      "incomplete_value": false,
      "site": "0045ee64",
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
            "const:f40:8"
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
      "0045f184",
      "DATA",
      [
        "storage",
        "00c63f40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045f184",
      "DATA",
      [
        "storage",
        "00c64f10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ee5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ee5c.md#insn-0045ee5c) · [`0045ee60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ee5c.md#insn-0045ee60)
- 新版 [`0045f17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f17c.md#insn-0045f17c) · [`0045f180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f17c.md#insn-0045f180)

~~~diff
- 0045ee5c ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045f17c ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045ee5c bytes 284000b0
+ 0045f17c bytes 284000b0
- 0045ee60 ["COPY", "tmp:0:8", ["const:f40:8"]]
- 0045ee60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045ee60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045ee60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f180 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 0045f180 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f180 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f180 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045ee60 bytes 08013d91
+ 0045f180 bytes 08413c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef53d5ed3bdecbd3abd65cd1d93d7106"></a>

### [`0045ee6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ee6c.md) → [`0045f18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f18c.md) FUN_0045f18c

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
      "definition_site": "0045f19c",
      "incomplete_value": false,
      "site": "0045f1a4",
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
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ee7c",
      "incomplete_value": false,
      "site": "0045ee84",
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
            "const:f40:8"
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
      "0045f1a4",
      "DATA",
      [
        "storage",
        "00c63f40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045f1a4",
      "DATA",
      [
        "storage",
        "00c64f10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ee78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ee6c.md#insn-0045ee78) · [`0045ee7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ee6c.md#insn-0045ee7c) · [`0045ee88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ee6c.md#insn-0045ee88)
- 新版 [`0045f198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f18c.md#insn-0045f198) · [`0045f19c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f18c.md#insn-0045f19c) · [`0045f1a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f18c.md#insn-0045f1a8)

~~~diff
- 0045ee78 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045f198 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045ee78 bytes 284000b0
+ 0045f198 bytes 284000b0
- 0045ee7c ["COPY", "tmp:0:8", ["const:f40:8"]]
- 0045ee7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045ee7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045ee7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f19c ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 0045f19c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f19c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f19c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045ee7c bytes 08013d91
+ 0045f19c bytes 08413c91
- 0045ee88 ["INT_ADD", "register:40f0:8", ["const:45ee88:8", "const:4:8"]]
- 0045ee88 ["CALL", null, ["callee:00c58f40:8"]]
+ 0045f1a8 ["INT_ADD", "register:40f0:8", ["const:45f1a8:8", "const:4:8"]]
+ 0045f1a8 ["CALL", null, ["callee:00c58f40:8"]]
- 0045ee88 bytes 3ae41f94
+ 0045f1a8 bytes 66e71f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37ca0d752ead382c4bd6a01cfb9ab98f"></a>

### [`0045eea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045eea8.md) → [`0045f1c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f1c8.md) FUN_0045f1c8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f00.md) [`00c59170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59170.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045f1ec",
      "incomplete_value": true,
      "site": "0045f1ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0045eecc",
      "incomplete_value": true,
      "site": "0045eecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0045f1e0",
      "READ",
      [
        "storage",
        "00c9ad20",
        null,
        "pointer"
      ]
    ],
    [
      "0045f1ec",
      "DATA",
      [
        "storage",
        "00c92da8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0045f1e0",
      "READ",
      [
        "storage",
        "00c9bcf0",
        null,
        "pointer"
      ]
    ],
    [
      "0045f1ec",
      "DATA",
      [
        "storage",
        "00c93d78",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045eeb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045eea8.md#insn-0045eeb4) · [`0045eec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045eea8.md#insn-0045eec0) · [`0045eed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045eea8.md#insn-0045eed0)
- 新版 [`0045f1d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f1c8.md#insn-0045f1d4) · [`0045f1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f1c8.md#insn-0045f1e0) · [`0045f1f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f1c8.md#insn-0045f1f0)

~~~diff
- 0045eeb4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0045f1d4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0045eeb4 bytes e8410090
+ 0045f1d4 bytes e8410090
- 0045eec0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
- 0045eec0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0045f1e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cf0:8"]]
+ 0045f1e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0045eec0 bytes 089146f9
+ 0045f1e0 bytes 087946f9
- 0045eed0 ["INT_ADD", "register:40f0:8", ["const:45eed0:8", "const:4:8"]]
- 0045eed0 ["CALL", null, ["callee:00c59170:8"]]
+ 0045f1f0 ["INT_ADD", "register:40f0:8", ["const:45f1f0:8", "const:4:8"]]
+ 0045f1f0 ["CALL", null, ["callee:00c59170:8"]]
- 0045eed0 bytes b4e41f94
+ 0045f1f0 bytes e0e71f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f805ad26624f6eb8834bc3626b9fbc2"></a>

### [`0045eef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045eef4.md) → [`0045f214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f214.md) FUN_0045f214

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c58f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f00.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59170.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md) [`00c593a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c593a0.md)

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
      "definition_site": "0045f238",
      "incomplete_value": true,
      "site": "0045f238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0045ef18",
      "incomplete_value": true,
      "site": "0045ef18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0045f22c",
      "READ",
      [
        "storage",
        "00c9ad20",
        null,
        "pointer"
      ]
    ],
    [
      "0045f238",
      "DATA",
      [
        "storage",
        "00c92da8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0045f22c",
      "READ",
      [
        "storage",
        "00c9bcf0",
        null,
        "pointer"
      ]
    ],
    [
      "0045f238",
      "DATA",
      [
        "storage",
        "00c93d78",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ef00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045eef4.md#insn-0045ef00) · [`0045ef0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045eef4.md#insn-0045ef0c) · [`0045ef1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045eef4.md#insn-0045ef1c)
- 新版 [`0045f220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f214.md#insn-0045f220) · [`0045f22c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f214.md#insn-0045f22c) · [`0045f23c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f214.md#insn-0045f23c)

~~~diff
- 0045ef00 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0045f220 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0045ef00 bytes e8410090
+ 0045f220 bytes e8410090
- 0045ef0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
- 0045ef0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0045f22c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cf0:8"]]
+ 0045f22c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0045ef0c bytes 089146f9
+ 0045f22c bytes 087946f9
- 0045ef1c ["INT_ADD", "register:40f0:8", ["const:45ef1c:8", "const:4:8"]]
- 0045ef1c ["CALL", null, ["callee:00c59170:8"]]
+ 0045f23c ["INT_ADD", "register:40f0:8", ["const:45f23c:8", "const:4:8"]]
+ 0045f23c ["CALL", null, ["callee:00c59170:8"]]
- 0045ef1c bytes a1e41f94
+ 0045f23c bytes cde71f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b63ee0a9c0b1f6f65b6f7b0b2ba8643d"></a>

### [`0045ef54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ef54.md) → [`0045f274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f274.md) FUN_0045f274

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0045ee9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ee9c.md) · 呼出先 12件 [`0045a708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a708.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md)
- 新版 呼出元 1件 [`0045f1bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f1bc.md) · 呼出先 12件 [`0045aa28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aa28.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.52% / 新版 94.52%

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
      "definition_site": "0045f318",
      "incomplete_value": true,
      "site": "0045f31c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0045eff8",
      "incomplete_value": true,
      "site": "0045effc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0045f2f4",
      "incomplete_value": true,
      "site": "0045f2fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0045efd4",
      "incomplete_value": true,
      "site": "0045efdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
      "definition_site": "0045f2f0",
      "incomplete_value": false,
      "site": "0045f2fc",
      "value": [
        "leaf",
        "const:45aa28:8"
      ]
    },
    "old": {
      "definition_site": "0045efd0",
      "incomplete_value": false,
      "site": "0045efdc",
      "value": [
        "leaf",
        "const:45a708:8"
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
      "0045f2f0",
      "PARAM",
      [
        "storage",
        "0045a708",
        null,
        null
      ]
    ],
    [
      "0045f2f4",
      "READ",
      [
        "storage",
        "00c9ad28",
        null,
        "pointer"
      ]
    ],
    [
      "0045f2f4",
      "PARAM",
      [
        "storage",
        "00c92d80",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0045f2f0",
      "PARAM",
      [
        "storage",
        "0045aa28",
        null,
        null
      ]
    ],
    [
      "0045f2f4",
      "READ",
      [
        "storage",
        "00c9bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "0045f2f4",
      "PARAM",
      [
        "storage",
        "00c93d50",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045efdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ef54.md#insn-0045efdc) · [`0045ef94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ef54.md#insn-0045ef94) · [`0045efac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ef54.md#insn-0045efac)
- 新版 [`0045f2fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f274.md#insn-0045f2fc) · [`0045f2b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f274.md#insn-0045f2b4) · [`0045f2cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f274.md#insn-0045f2cc)

~~~diff
- 0045efdc ["INT_ADD", "register:40f0:8", ["const:45efdc:8", "const:4:8"]]
- 0045efdc ["CALL", null, ["callee:00c593d0:8"]]
+ 0045f2fc ["INT_ADD", "register:40f0:8", ["const:45f2fc:8", "const:4:8"]]
+ 0045f2fc ["CALL", null, ["callee:00c593d0:8"]]
- 0045efdc bytes 09e51f94
+ 0045f2fc bytes 35e81f94
- 0045ef94 ["INT_ADD", "register:40f0:8", ["const:45ef94:8", "const:4:8"]]
- 0045ef94 ["CALL", null, ["callee:00c59390:8"]]
+ 0045f2b4 ["INT_ADD", "register:40f0:8", ["const:45f2b4:8", "const:4:8"]]
+ 0045f2b4 ["CALL", null, ["callee:00c59390:8"]]
- 0045ef94 bytes 0be51f94
+ 0045f2b4 bytes 37e81f94
- 0045efac ["INT_ADD", "register:40f0:8", ["const:45efac:8", "const:4:8"]]
- 0045efac ["CALL", null, ["callee:00c593b0:8"]]
+ 0045f2cc ["INT_ADD", "register:40f0:8", ["const:45f2cc:8", "const:4:8"]]
+ 0045f2cc ["CALL", null, ["callee:00c593b0:8"]]
- 0045efac bytes 0de51f94
+ 0045f2cc bytes 39e81f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f464b0e94a0ff82217e3664e924d77d"></a>

### [`0045f178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f178.md) → [`0045f498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f498.md) FUN_0045f498

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
      "definition_site": "0045f4a4",
      "incomplete_value": false,
      "site": "0045f4b0",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f184",
      "incomplete_value": false,
      "site": "0045f190",
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
            "const:fe8:8"
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
      "0045f4b0",
      "DATA",
      [
        "storage",
        "00c63fe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f4b0",
      "DATA",
      [
        "storage",
        "00c64fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f178.md#insn-0045f180) · [`0045f184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f178.md#insn-0045f184)
- 新版 [`0045f4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f498.md#insn-0045f4a0) · [`0045f4a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f498.md#insn-0045f4a4)

~~~diff
- 0045f180 ["COPY", "register:4050:8", ["const:c63000:8"]]
+ 0045f4a0 ["COPY", "register:4050:8", ["const:c64000:8"]]
- 0045f180 bytes 2a400090
+ 0045f4a0 bytes 2a4000b0
- 0045f184 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 0045f184 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045f184 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045f184 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045f4a4 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 0045f4a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045f4a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045f4a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045f184 bytes 4aa13f91
+ 0045f4a4 bytes 4ae13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-754ab4e89bc55b5e1abc3d9faccad47c"></a>

### [`0045f1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f1bc.md) → [`0045f4dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f4dc.md) FUN_0045f4dc

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
      "definition_site": "0045f4f4",
      "incomplete_value": false,
      "site": "0045f500",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f1d4",
      "incomplete_value": false,
      "site": "0045f1e0",
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
            "const:fe8:8"
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
      "0045f500",
      "DATA",
      [
        "storage",
        "00c63fe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f500",
      "DATA",
      [
        "storage",
        "00c64fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f1bc.md#insn-0045f1d0) · [`0045f1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f1bc.md#insn-0045f1d4) · [`0045f204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f1bc.md#insn-0045f204)
- 新版 [`0045f4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f4dc.md#insn-0045f4f0) · [`0045f4f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f4dc.md#insn-0045f4f4) · [`0045f524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f4dc.md#insn-0045f524)

~~~diff
- 0045f1d0 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045f4f0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045f1d0 bytes 28400090
+ 0045f4f0 bytes 284000b0
- 0045f1d4 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 0045f1d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f1d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f1d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f4f4 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 0045f4f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f4f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f4f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f1d4 bytes 08a13f91
+ 0045f4f4 bytes 08e13e91
- 0045f204 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f204 ["INT_ADD", "register:40f0:8", ["const:45f204:8", "const:4:8"]]
- 0045f204 ["CALLIND", null, ["register:0:8"]]
+ 0045f524 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f524 ["INT_ADD", "register:40f0:8", ["const:45f524:8", "const:4:8"]]
+ 0045f524 ["CALLIND", null, ["register:0:8"]]
- 0045f204 bytes 00013fd6
+ 0045f524 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6493a5e818a13072662e22bd0baf08b"></a>

### [`0045f218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f218.md) → [`0045f538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f538.md) FUN_0045f538

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0045f564",
      "incomplete_value": false,
      "site": "0045f564",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f244",
      "incomplete_value": false,
      "site": "0045f244",
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
            "const:fe8:8"
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
      "0045f564",
      "DATA",
      [
        "storage",
        "00c63fe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f564",
      "DATA",
      [
        "storage",
        "00c64fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f218.md#insn-0045f22c) · [`0045f238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f218.md#insn-0045f238) · [`0045f23c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f218.md#insn-0045f23c)
- 新版 [`0045f54c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f538.md#insn-0045f54c) · [`0045f558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f538.md#insn-0045f558) · [`0045f55c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f538.md#insn-0045f55c)

~~~diff
- 0045f22c ["INT_ADD", "register:40f0:8", ["const:45f22c:8", "const:4:8"]]
- 0045f22c ["CALL", null, ["callee:00c58f30:8"]]
+ 0045f54c ["INT_ADD", "register:40f0:8", ["const:45f54c:8", "const:4:8"]]
+ 0045f54c ["CALL", null, ["callee:00c58f30:8"]]
- 0045f22c bytes 4de31f94
+ 0045f54c bytes 79e61f94
- 0045f238 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045f558 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045f238 bytes 28400090
+ 0045f558 bytes 284000b0
- 0045f23c ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 0045f23c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f23c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f23c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f55c ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 0045f55c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f55c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f55c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f23c bytes 08a13f91
+ 0045f55c bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a45dd84e405bc6db64033345d15adb93"></a>

### [`0045f2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f2a8.md) → [`0045f5c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f5c8.md) FUN_0045f5c8

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
      "definition_site": "0045f5e8",
      "incomplete_value": false,
      "site": "0045f5e8",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f2c8",
      "incomplete_value": false,
      "site": "0045f2c8",
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
            "const:fe8:8"
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
      "0045f5e8",
      "DATA",
      [
        "storage",
        "00c63fe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f5e8",
      "DATA",
      [
        "storage",
        "00c64fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f2a8.md#insn-0045f2c0) · [`0045f2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f2a8.md#insn-0045f2c4) · [`0045f2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f2a8.md#insn-0045f2e4)
- 新版 [`0045f5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f5c8.md#insn-0045f5e0) · [`0045f5e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f5c8.md#insn-0045f5e4) · [`0045f604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f5c8.md#insn-0045f604)

~~~diff
- 0045f2c0 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045f5e0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045f2c0 bytes 28400090
+ 0045f5e0 bytes 284000b0
- 0045f2c4 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 0045f2c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f2c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f2c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f5e4 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 0045f5e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f5e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f5e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f2c4 bytes 08a13f91
+ 0045f5e4 bytes 08e13e91
- 0045f2e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f2e4 ["INT_ADD", "register:40f0:8", ["const:45f2e4:8", "const:4:8"]]
- 0045f2e4 ["CALLIND", null, ["register:0:8"]]
+ 0045f604 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f604 ["INT_ADD", "register:40f0:8", ["const:45f604:8", "const:4:8"]]
+ 0045f604 ["CALLIND", null, ["register:0:8"]]
- 0045f2e4 bytes 00013fd6
+ 0045f604 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1883060e99a433bf5171e45ecfe217fc"></a>

### [`0045f3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f3a8.md) → [`0045f6c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f6c8.md) FUN_0045f6c8

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0045e6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e6a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0045e9c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045e/0045e9c8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045f774",
      "incomplete_value": true,
      "site": "0045f774",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e23:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f454",
      "incomplete_value": true,
      "site": "0045f454",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de3:8"
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
      "0045f760",
      "READ",
      [
        "storage",
        "002a1de3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0045f760",
      "READ",
      [
        "storage",
        "002a1e23",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f3a8.md#insn-0045f400) · [`0045f42c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f3a8.md#insn-0045f42c) · [`0045f438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f3a8.md#insn-0045f438)
- 新版 [`0045f720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f6c8.md#insn-0045f720) · [`0045f74c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f6c8.md#insn-0045f74c) · [`0045f758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f6c8.md#insn-0045f758)

~~~diff
- 0045f400 ["INT_ADD", "register:40f0:8", ["const:45f400:8", "const:4:8"]]
- 0045f400 ["CALL", null, ["callee:004413ec:8"]]
+ 0045f720 ["INT_ADD", "register:40f0:8", ["const:45f720:8", "const:4:8"]]
+ 0045f720 ["CALL", null, ["callee:004413ec:8"]]
- 0045f400 bytes 3387ff97
+ 0045f720 bytes 3387ff97
- 0045f42c ["INT_ADD", "register:40f0:8", ["const:45f42c:8", "const:4:8"]]
- 0045f42c ["CALL", null, ["callee:00c58f50:8"]]
+ 0045f74c ["INT_ADD", "register:40f0:8", ["const:45f74c:8", "const:4:8"]]
+ 0045f74c ["CALL", null, ["callee:00c58f50:8"]]
- 0045f42c bytes d5e21f94
+ 0045f74c bytes 01e61f94
- 0045f438 ["COPY", "tmp:0:8", ["const:de3:8"]]
- 0045f438 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045f438 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045f438 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045f758 ["COPY", "tmp:0:8", ["const:e23:8"]]
+ 0045f758 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045f758 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045f758 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045f438 bytes 298d3791
+ 0045f758 bytes 298d3891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92366847cc48e6e41fd9a6215a49c398"></a>

### [`0045f66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f66c.md) → [`0045f98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f98c.md) FUN_0045f98c

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
      "definition_site": "0045f998",
      "incomplete_value": false,
      "site": "0045f9a4",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f678",
      "incomplete_value": false,
      "site": "0045f684",
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
            "const:68:8"
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
      "0045f9a4",
      "DATA",
      [
        "storage",
        "00c64068",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f9a4",
      "DATA",
      [
        "storage",
        "00c65038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f66c.md#insn-0045f674) · [`0045f678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f66c.md#insn-0045f678)
- 新版 [`0045f994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f98c.md#insn-0045f994) · [`0045f998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f98c.md#insn-0045f998)

~~~diff
- 0045f674 ["COPY", "register:4050:8", ["const:c64000:8"]]
+ 0045f994 ["COPY", "register:4050:8", ["const:c65000:8"]]
- 0045f674 bytes 2a4000b0
+ 0045f994 bytes 2a4000d0
- 0045f678 ["COPY", "tmp:0:8", ["const:68:8"]]
- 0045f678 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045f678 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045f678 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045f998 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0045f998 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045f998 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045f998 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045f678 bytes 4aa10191
+ 0045f998 bytes 4ae10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c75be90f6e603ae7155c1446ec3e95e1"></a>

### [`0045f6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f6b0.md) → [`0045f9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f9d0.md) FUN_0045f9d0

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
      "definition_site": "0045f9e8",
      "incomplete_value": false,
      "site": "0045f9f4",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f6c8",
      "incomplete_value": false,
      "site": "0045f6d4",
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
            "const:68:8"
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
      "0045f9f4",
      "DATA",
      [
        "storage",
        "00c64068",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f9f4",
      "DATA",
      [
        "storage",
        "00c65038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f6b0.md#insn-0045f6c4) · [`0045f6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f6b0.md#insn-0045f6c8) · [`0045f6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f6b0.md#insn-0045f6f8)
- 新版 [`0045f9e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f9d0.md#insn-0045f9e4) · [`0045f9e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f9d0.md#insn-0045f9e8) · [`0045fa18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045f9d0.md#insn-0045fa18)

~~~diff
- 0045f6c4 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0045f9e4 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0045f6c4 bytes 284000b0
+ 0045f9e4 bytes 284000d0
- 0045f6c8 ["COPY", "tmp:0:8", ["const:68:8"]]
- 0045f6c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f6c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f6c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f9e8 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0045f9e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f9e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f9e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f6c8 bytes 08a10191
+ 0045f9e8 bytes 08e10091
- 0045f6f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f6f8 ["INT_ADD", "register:40f0:8", ["const:45f6f8:8", "const:4:8"]]
- 0045f6f8 ["CALLIND", null, ["register:0:8"]]
+ 0045fa18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045fa18 ["INT_ADD", "register:40f0:8", ["const:45fa18:8", "const:4:8"]]
+ 0045fa18 ["CALLIND", null, ["register:0:8"]]
- 0045f6f8 bytes 00013fd6
+ 0045fa18 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab6f8d2268a44718e0f1e2cede0a4cc4"></a>

### [`0045f70c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f70c.md) → [`0045fa2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fa2c.md) FUN_0045fa2c

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
      "definition_site": "0045fa58",
      "incomplete_value": false,
      "site": "0045fa58",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f738",
      "incomplete_value": false,
      "site": "0045f738",
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
            "const:68:8"
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
      "0045fa58",
      "DATA",
      [
        "storage",
        "00c64068",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fa58",
      "DATA",
      [
        "storage",
        "00c65038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f70c.md#insn-0045f720) · [`0045f72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f70c.md#insn-0045f72c) · [`0045f730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f70c.md#insn-0045f730)
- 新版 [`0045fa40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fa2c.md#insn-0045fa40) · [`0045fa4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fa2c.md#insn-0045fa4c) · [`0045fa50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fa2c.md#insn-0045fa50)

~~~diff
- 0045f720 ["INT_ADD", "register:40f0:8", ["const:45f720:8", "const:4:8"]]
- 0045f720 ["CALL", null, ["callee:00c58f30:8"]]
+ 0045fa40 ["INT_ADD", "register:40f0:8", ["const:45fa40:8", "const:4:8"]]
+ 0045fa40 ["CALL", null, ["callee:00c58f30:8"]]
- 0045f720 bytes 10e21f94
+ 0045fa40 bytes 3ce51f94
- 0045f72c ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0045fa4c ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0045f72c bytes 284000b0
+ 0045fa4c bytes 284000d0
- 0045f730 ["COPY", "tmp:0:8", ["const:68:8"]]
- 0045f730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045fa50 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0045fa50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fa50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fa50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f730 bytes 08a10191
+ 0045fa50 bytes 08e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3836171c9f91b84323eb0b65bf3fde7c"></a>

### [`0045f794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f794.md) → [`0045fab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fab4.md) FUN_0045fab4

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045fad0",
      "incomplete_value": false,
      "site": "0045fad0",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f7b0",
      "incomplete_value": false,
      "site": "0045f7b0",
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
            "const:68:8"
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
      "0045fad0",
      "DATA",
      [
        "storage",
        "00c64068",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fad0",
      "DATA",
      [
        "storage",
        "00c65038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f7a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f794.md#insn-0045f7a8) · [`0045f7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f794.md#insn-0045f7ac) · [`0045f7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f794.md#insn-0045f7d0)
- 新版 [`0045fac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fab4.md#insn-0045fac8) · [`0045facc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fab4.md#insn-0045facc) · [`0045faf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fab4.md#insn-0045faf0)

~~~diff
- 0045f7a8 ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 0045fac8 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 0045f7a8 bytes 294000b0
+ 0045fac8 bytes 294000d0
- 0045f7ac ["COPY", "tmp:0:8", ["const:68:8"]]
- 0045f7ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045f7ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045f7ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045facc ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0045facc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045facc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045facc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045f7ac bytes 29a10191
+ 0045facc bytes 29e10091
- 0045f7d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045f7d0 ["INT_ADD", "register:40f0:8", ["const:45f7d0:8", "const:4:8"]]
- 0045f7d0 ["CALLIND", null, ["register:0:8"]]
+ 0045faf0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045faf0 ["INT_ADD", "register:40f0:8", ["const:45faf0:8", "const:4:8"]]
+ 0045faf0 ["CALLIND", null, ["register:0:8"]]
- 0045f7d0 bytes 20013fd6
+ 0045faf0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-134024b349013cd97f294401688ac7d3"></a>

### [`0045f940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f940.md) → [`0045fc60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fc60.md) FUN_0045fc60

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

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
      "definition_site": "0045fc74",
      "incomplete_value": false,
      "site": "0045fc78",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f954",
      "incomplete_value": false,
      "site": "0045f958",
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
      "0045fc78",
      "DATA",
      [
        "storage",
        "00c640e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fc78",
      "DATA",
      [
        "storage",
        "00c650b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f940.md#insn-0045f950) · [`0045f954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f940.md#insn-0045f954) · [`0045f968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f940.md#insn-0045f968)
- 新版 [`0045fc70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fc60.md#insn-0045fc70) · [`0045fc74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fc60.md#insn-0045fc74) · [`0045fc88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fc60.md#insn-0045fc88)

~~~diff
- 0045f950 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0045fc70 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0045f950 bytes 284000b0
+ 0045fc70 bytes 284000d0
- 0045f954 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 0045f954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045fc74 ["COPY", "tmp:0:8", ["const:b8:8"]]
+ 0045fc74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fc74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fc74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f954 bytes 08a10391
+ 0045fc74 bytes 08e10291
- 0045f968 ["INT_ADD", "register:40f0:8", ["const:45f968:8", "const:4:8"]]
- 0045f968 ["CALL", null, ["callee:00c54d90:8"]]
+ 0045fc88 ["INT_ADD", "register:40f0:8", ["const:45fc88:8", "const:4:8"]]
+ 0045fc88 ["CALL", null, ["callee:00c54d90:8"]]
- 0045f968 bytes 0ed11f94
+ 0045fc88 bytes 42d41f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c4e576f04cb409cf6d977dc1ac04b08"></a>

### [`0045f99c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f99c.md) → [`0045fcbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fcbc.md) FUN_0045fcbc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "0045fcd4",
      "incomplete_value": false,
      "site": "0045fcd8",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f9b4",
      "incomplete_value": false,
      "site": "0045f9b8",
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
            "const:e8:8"
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
      "0045fcd8",
      "DATA",
      [
        "storage",
        "00c640e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fcd8",
      "DATA",
      [
        "storage",
        "00c650b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f99c.md#insn-0045f9b0) · [`0045f9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f99c.md#insn-0045f9b4) · [`0045f9c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f99c.md#insn-0045f9c8)
- 新版 [`0045fcd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fcbc.md#insn-0045fcd0) · [`0045fcd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fcbc.md#insn-0045fcd4) · [`0045fce8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fcbc.md#insn-0045fce8)

~~~diff
- 0045f9b0 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0045fcd0 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0045f9b0 bytes 284000b0
+ 0045fcd0 bytes 284000d0
- 0045f9b4 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 0045f9b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f9b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f9b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045fcd4 ["COPY", "tmp:0:8", ["const:b8:8"]]
+ 0045fcd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fcd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fcd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f9b4 bytes 08a10391
+ 0045fcd4 bytes 08e10291
- 0045f9c8 ["INT_ADD", "register:40f0:8", ["const:45f9c8:8", "const:4:8"]]
- 0045f9c8 ["CALL", null, ["callee:00c54d90:8"]]
+ 0045fce8 ["INT_ADD", "register:40f0:8", ["const:45fce8:8", "const:4:8"]]
+ 0045fce8 ["CALL", null, ["callee:00c54d90:8"]]
- 0045f9c8 bytes f6d01f94
+ 0045fce8 bytes 2ad41f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-852522a7d80614478fb5d128f137f92f"></a>

### [`0045f9f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f9f8.md) → [`0045fd18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fd18.md) FUN_0045fd18

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
      "definition_site": "0045fd3c",
      "incomplete_value": false,
      "site": "0045fd3c",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045fa1c",
      "incomplete_value": false,
      "site": "0045fa1c",
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
      "0045fd3c",
      "DATA",
      [
        "storage",
        "00c640e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fd3c",
      "DATA",
      [
        "storage",
        "00c650b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fa0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f9f8.md#insn-0045fa0c) · [`0045fa14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f9f8.md#insn-0045fa14) · [`0045fa18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f9f8.md#insn-0045fa18)
- 新版 [`0045fd2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fd18.md#insn-0045fd2c) · [`0045fd34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fd18.md#insn-0045fd34) · [`0045fd38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fd18.md#insn-0045fd38)

~~~diff
- 0045fa0c ["INT_ADD", "register:40f0:8", ["const:45fa0c:8", "const:4:8"]]
- 0045fa0c ["CALL", null, ["callee:00c58f30:8"]]
+ 0045fd2c ["INT_ADD", "register:40f0:8", ["const:45fd2c:8", "const:4:8"]]
+ 0045fd2c ["CALL", null, ["callee:00c58f30:8"]]
- 0045fa0c bytes 55e11f94
+ 0045fd2c bytes 81e41f94
- 0045fa14 ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 0045fd34 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 0045fa14 bytes 294000b0
+ 0045fd34 bytes 294000d0
- 0045fa18 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 0045fa18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045fa18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045fa18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045fd38 ["COPY", "tmp:0:8", ["const:b8:8"]]
+ 0045fd38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045fd38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045fd38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045fa18 bytes 29a10391
+ 0045fd38 bytes 29e10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ad755ced090efc74d4e7833b9aad194"></a>

### [`0045fa48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fa48.md) → [`0045fd68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fd68.md) FUN_0045fd68

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
      "definition_site": "0045fd74",
      "incomplete_value": false,
      "site": "0045fd74",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045fa54",
      "incomplete_value": false,
      "site": "0045fa54",
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
      "0045fd74",
      "DATA",
      [
        "storage",
        "00c640e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fd74",
      "DATA",
      [
        "storage",
        "00c650b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fa4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fa48.md#insn-0045fa4c) · [`0045fa50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fa48.md#insn-0045fa50) · [`0045fa70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fa48.md#insn-0045fa70)
- 新版 [`0045fd6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fd68.md#insn-0045fd6c) · [`0045fd70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fd68.md#insn-0045fd70) · [`0045fd90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fd68.md#insn-0045fd90)

~~~diff
- 0045fa4c ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 0045fd6c ["COPY", "register:4048:8", ["const:c65000:8"]]
- 0045fa4c bytes 294000b0
+ 0045fd6c bytes 294000d0
- 0045fa50 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 0045fa50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045fa50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045fa50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045fd70 ["COPY", "tmp:0:8", ["const:b8:8"]]
+ 0045fd70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045fd70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045fd70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045fa50 bytes 29a10391
+ 0045fd70 bytes 29e10291
- 0045fa70 ["INT_ADD", "register:40f0:8", ["const:45fa70:8", "const:4:8"]]
- 0045fa70 ["CALL", null, ["callee:00c54d60:8"]]
+ 0045fd90 ["INT_ADD", "register:40f0:8", ["const:45fd90:8", "const:4:8"]]
+ 0045fd90 ["CALL", null, ["callee:00c54d60:8"]]
- 0045fa70 bytes c0d01f94
+ 0045fd90 bytes f4d31f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d58b2950cf569534ac734c418ec95fd3"></a>

### [`0045fbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fbdc.md) → [`0045fefc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fefc.md) FUN_0045fefc

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
      "definition_site": "0045ff08",
      "incomplete_value": false,
      "site": "0045ff14",
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
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045fbe8",
      "incomplete_value": false,
      "site": "0045fbf4",
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
      "0045ff14",
      "DATA",
      [
        "storage",
        "00c64168",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ff14",
      "DATA",
      [
        "storage",
        "00c65138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fbdc.md#insn-0045fbe4) · [`0045fbe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fbdc.md#insn-0045fbe8)
- 新版 [`0045ff04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fefc.md#insn-0045ff04) · [`0045ff08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045fefc.md#insn-0045ff08)

~~~diff
- 0045fbe4 ["COPY", "register:4050:8", ["const:c64000:8"]]
+ 0045ff04 ["COPY", "register:4050:8", ["const:c65000:8"]]
- 0045fbe4 bytes 2a4000b0
+ 0045ff04 bytes 2a4000d0
- 0045fbe8 ["COPY", "tmp:0:8", ["const:168:8"]]
- 0045fbe8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045fbe8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045fbe8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045ff08 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 0045ff08 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045ff08 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045ff08 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045fbe8 bytes 4aa10591
+ 0045ff08 bytes 4ae10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-428acf170ae2438465e7a2aa06d49425"></a>

### [`0045fc20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fc20.md) → [`0045ff40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045ff40.md) FUN_0045ff40

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
      "definition_site": "0045ff58",
      "incomplete_value": false,
      "site": "0045ff64",
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
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045fc38",
      "incomplete_value": false,
      "site": "0045fc44",
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
      "0045ff64",
      "DATA",
      [
        "storage",
        "00c64168",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ff64",
      "DATA",
      [
        "storage",
        "00c65138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fc34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fc20.md#insn-0045fc34) · [`0045fc38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fc20.md#insn-0045fc38) · [`0045fc68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fc20.md#insn-0045fc68)
- 新版 [`0045ff54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045ff40.md#insn-0045ff54) · [`0045ff58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045ff40.md#insn-0045ff58) · [`0045ff88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045ff40.md#insn-0045ff88)

~~~diff
- 0045fc34 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0045ff54 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0045fc34 bytes 284000b0
+ 0045ff54 bytes 284000d0
- 0045fc38 ["COPY", "tmp:0:8", ["const:168:8"]]
- 0045fc38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045fc38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045fc38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045ff58 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 0045ff58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ff58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ff58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045fc38 bytes 08a10591
+ 0045ff58 bytes 08e10491
- 0045fc68 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045fc68 ["INT_ADD", "register:40f0:8", ["const:45fc68:8", "const:4:8"]]
- 0045fc68 ["CALLIND", null, ["register:0:8"]]
+ 0045ff88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045ff88 ["INT_ADD", "register:40f0:8", ["const:45ff88:8", "const:4:8"]]
+ 0045ff88 ["CALLIND", null, ["register:0:8"]]
- 0045fc68 bytes 00013fd6
+ 0045ff88 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-614e52efd58c1c63e5319c1cdd181055"></a>

### [`0045fc7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fc7c.md) → [`0045ff9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045ff9c.md) FUN_0045ff9c

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
      "definition_site": "0045ffc8",
      "incomplete_value": false,
      "site": "0045ffc8",
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
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045fca8",
      "incomplete_value": false,
      "site": "0045fca8",
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
            "const:168:8"
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
      "0045ffc8",
      "DATA",
      [
        "storage",
        "00c64168",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ffc8",
      "DATA",
      [
        "storage",
        "00c65138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fc7c.md#insn-0045fc90) · [`0045fc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fc7c.md#insn-0045fc9c) · [`0045fca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fc7c.md#insn-0045fca0)
- 新版 [`0045ffb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045ff9c.md#insn-0045ffb0) · [`0045ffbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045ff9c.md#insn-0045ffbc) · [`0045ffc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045f/0045ff9c.md#insn-0045ffc0)

~~~diff
- 0045fc90 ["INT_ADD", "register:40f0:8", ["const:45fc90:8", "const:4:8"]]
- 0045fc90 ["CALL", null, ["callee:00c58f30:8"]]
+ 0045ffb0 ["INT_ADD", "register:40f0:8", ["const:45ffb0:8", "const:4:8"]]
+ 0045ffb0 ["CALL", null, ["callee:00c58f30:8"]]
- 0045fc90 bytes b4e01f94
+ 0045ffb0 bytes e0e31f94
- 0045fc9c ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0045ffbc ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0045fc9c bytes 284000b0
+ 0045ffbc bytes 284000d0
- 0045fca0 ["COPY", "tmp:0:8", ["const:168:8"]]
- 0045fca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045fca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045fca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045ffc0 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 0045ffc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ffc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ffc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045fca0 bytes 08a10591
+ 0045ffc0 bytes 08e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5817d490efdfd9e0864a88028449fb20"></a>

### [`0045fd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fd04.md) → [`00460024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460024.md) FUN_00460024

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00460040",
      "incomplete_value": false,
      "site": "00460040",
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
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045fd20",
      "incomplete_value": false,
      "site": "0045fd20",
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
      "00460040",
      "DATA",
      [
        "storage",
        "00c64168",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00460040",
      "DATA",
      [
        "storage",
        "00c65138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fd18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fd04.md#insn-0045fd18) · [`0045fd1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fd04.md#insn-0045fd1c) · [`0045fd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fd04.md#insn-0045fd40)
- 新版 [`00460038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460024.md#insn-00460038) · [`0046003c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460024.md#insn-0046003c) · [`00460060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460024.md#insn-00460060)

~~~diff
- 0045fd18 ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 00460038 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 0045fd18 bytes 294000b0
+ 00460038 bytes 294000b0
- 0045fd1c ["COPY", "tmp:0:8", ["const:168:8"]]
- 0045fd1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045fd1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045fd1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0046003c ["COPY", "tmp:0:8", ["const:138:8"]]
+ 0046003c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0046003c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0046003c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045fd1c bytes 29a10591
+ 0046003c bytes 29e10491
- 0045fd40 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045fd40 ["INT_ADD", "register:40f0:8", ["const:45fd40:8", "const:4:8"]]
- 0045fd40 ["CALLIND", null, ["register:0:8"]]
+ 00460060 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00460060 ["INT_ADD", "register:40f0:8", ["const:460060:8", "const:4:8"]]
+ 00460060 ["CALLIND", null, ["register:0:8"]]
- 0045fd40 bytes 20013fd6
+ 00460060 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1413c8d3d53e97a9321c55067f341334"></a>

### [`0045fe48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fe48.md) → [`00460168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460168.md) FUN_00460168

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
      "definition_site": "00460174",
      "incomplete_value": false,
      "site": "00460180",
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
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045fe54",
      "incomplete_value": false,
      "site": "0045fe60",
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
      "00460180",
      "DATA",
      [
        "storage",
        "00c641e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00460180",
      "DATA",
      [
        "storage",
        "00c651b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fe50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fe48.md#insn-0045fe50) · [`0045fe54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fe48.md#insn-0045fe54)
- 新版 [`00460170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460168.md#insn-00460170) · [`00460174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460168.md#insn-00460174)

~~~diff
- 0045fe50 ["COPY", "register:4050:8", ["const:c64000:8"]]
+ 00460170 ["COPY", "register:4050:8", ["const:c65000:8"]]
- 0045fe50 bytes 2a4000b0
+ 00460170 bytes 2a4000b0
- 0045fe54 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 0045fe54 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045fe54 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045fe54 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00460174 ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 00460174 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00460174 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00460174 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045fe54 bytes 4aa10791
+ 00460174 bytes 4ae10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-759bcdd3a4d8c4d2d6d3cb46221fc3b3"></a>

### [`0045fe8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fe8c.md) → [`004601ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/004601ac.md) FUN_004601ac

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
      "definition_site": "004601c4",
      "incomplete_value": false,
      "site": "004601d0",
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
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045fea4",
      "incomplete_value": false,
      "site": "0045feb0",
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
      "004601d0",
      "DATA",
      [
        "storage",
        "00c641e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004601d0",
      "DATA",
      [
        "storage",
        "00c651b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fe8c.md#insn-0045fea0) · [`0045fea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fe8c.md#insn-0045fea4) · [`0045fed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fe8c.md#insn-0045fed4)
- 新版 [`004601c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/004601ac.md#insn-004601c0) · [`004601c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/004601ac.md#insn-004601c4) · [`004601f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/004601ac.md#insn-004601f4)

~~~diff
- 0045fea0 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 004601c0 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0045fea0 bytes 284000b0
+ 004601c0 bytes 284000b0
- 0045fea4 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 0045fea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045fea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045fea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004601c4 ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 004601c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004601c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004601c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045fea4 bytes 08a10791
+ 004601c4 bytes 08e10691
- 0045fed4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045fed4 ["INT_ADD", "register:40f0:8", ["const:45fed4:8", "const:4:8"]]
- 0045fed4 ["CALLIND", null, ["register:0:8"]]
+ 004601f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004601f4 ["INT_ADD", "register:40f0:8", ["const:4601f4:8", "const:4:8"]]
+ 004601f4 ["CALLIND", null, ["register:0:8"]]
- 0045fed4 bytes 00013fd6
+ 004601f4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d98554e2359ff8e377c77a97dd6c9ad5"></a>

### [`0045fee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fee8.md) → [`00460208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460208.md) FUN_00460208

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
      "definition_site": "00460234",
      "incomplete_value": false,
      "site": "00460234",
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
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ff14",
      "incomplete_value": false,
      "site": "0045ff14",
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
            "const:1e8:8"
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
      "00460234",
      "DATA",
      [
        "storage",
        "00c641e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00460234",
      "DATA",
      [
        "storage",
        "00c651b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fefc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fee8.md#insn-0045fefc) · [`0045ff08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fee8.md#insn-0045ff08) · [`0045ff0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fee8.md#insn-0045ff0c)
- 新版 [`0046021c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460208.md#insn-0046021c) · [`00460228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460208.md#insn-00460228) · [`0046022c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460208.md#insn-0046022c)

~~~diff
- 0045fefc ["INT_ADD", "register:40f0:8", ["const:45fefc:8", "const:4:8"]]
- 0045fefc ["CALL", null, ["callee:00c58f30:8"]]
+ 0046021c ["INT_ADD", "register:40f0:8", ["const:46021c:8", "const:4:8"]]
+ 0046021c ["CALL", null, ["callee:00c58f30:8"]]
- 0045fefc bytes 19e01f94
+ 0046021c bytes 45e31f94
- 0045ff08 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 00460228 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0045ff08 bytes 284000b0
+ 00460228 bytes 284000b0
- 0045ff0c ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 0045ff0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045ff0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045ff0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046022c ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 0046022c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046022c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046022c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045ff0c bytes 08a10791
+ 0046022c bytes 08e10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f53eab268c6fca1e2dd347afc834765"></a>

### [`0045ff70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045ff70.md) → [`00460290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460290.md) FUN_00460290

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004602ac",
      "incomplete_value": false,
      "site": "004602ac",
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
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ff8c",
      "incomplete_value": false,
      "site": "0045ff8c",
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
      "004602ac",
      "DATA",
      [
        "storage",
        "00c641e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004602ac",
      "DATA",
      [
        "storage",
        "00c651b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ff84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045ff70.md#insn-0045ff84) · [`0045ff88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045ff70.md#insn-0045ff88) · [`0045ffac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045ff70.md#insn-0045ffac)
- 新版 [`004602a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460290.md#insn-004602a4) · [`004602a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460290.md#insn-004602a8) · [`004602cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460290.md#insn-004602cc)

~~~diff
- 0045ff84 ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 004602a4 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 0045ff84 bytes 294000b0
+ 004602a4 bytes 294000b0
- 0045ff88 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 0045ff88 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045ff88 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045ff88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004602a8 ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 004602a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004602a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004602a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045ff88 bytes 29a10791
+ 004602a8 bytes 29e10691
- 0045ffac ["COPY", "register:0:8", ["register:4048:8"]]
- 0045ffac ["INT_ADD", "register:40f0:8", ["const:45ffac:8", "const:4:8"]]
- 0045ffac ["CALLIND", null, ["register:0:8"]]
+ 004602cc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004602cc ["INT_ADD", "register:40f0:8", ["const:4602cc:8", "const:4:8"]]
+ 004602cc ["CALLIND", null, ["register:0:8"]]
- 0045ffac bytes 20013fd6
+ 004602cc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76c21d217f95a38d94f0c828d0895a18"></a>

### [`00460110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/00460110.md) → [`00460430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460430.md) FUN_00460430

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
      "definition_site": "00460444",
      "incomplete_value": false,
      "site": "00460448",
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
            "const:238:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00460124",
      "incomplete_value": false,
      "site": "00460128",
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
            "const:268:8"
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
      "00460448",
      "DATA",
      [
        "storage",
        "00c64268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00460448",
      "DATA",
      [
        "storage",
        "00c65238",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046011c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/00460110.md#insn-0046011c) · [`00460120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/00460110.md#insn-00460120) · [`00460124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/00460110.md#insn-00460124)
- 新版 [`0046043c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460430.md#insn-0046043c) · [`00460440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460430.md#insn-00460440) · [`00460444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460430.md#insn-00460444)

~~~diff
- 0046011c ["INT_ADD", "register:40f0:8", ["const:46011c:8", "const:4:8"]]
- 0046011c ["CALL", null, ["callee:00c58f30:8"]]
+ 0046043c ["INT_ADD", "register:40f0:8", ["const:46043c:8", "const:4:8"]]
+ 0046043c ["CALL", null, ["callee:00c58f30:8"]]
- 0046011c bytes 91df1f94
+ 0046043c bytes bde21f94
- 00460120 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 00460440 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00460120 bytes 28400090
+ 00460440 bytes 284000b0
- 00460124 ["COPY", "tmp:0:8", ["const:268:8"]]
- 00460124 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00460124 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00460124 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00460444 ["COPY", "tmp:0:8", ["const:238:8"]]
+ 00460444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00460444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00460444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00460124 bytes 08a10991
+ 00460444 bytes 08e10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8850569480a4ef338c7735308b4f182"></a>

### [`00460134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/00460134.md) → [`00460454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460454.md) FUN_00460454

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
      "definition_site": "00460458",
      "incomplete_value": false,
      "site": "0046045c",
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
            "const:238:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00460138",
      "incomplete_value": false,
      "site": "0046013c",
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
            "const:268:8"
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
      "0046045c",
      "DATA",
      [
        "storage",
        "00c64268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0046045c",
      "DATA",
      [
        "storage",
        "00c65238",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00460134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/00460134.md#insn-00460134) · [`00460138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/00460134.md#insn-00460138)
- 新版 [`00460454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460454.md#insn-00460454) · [`00460458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460454.md#insn-00460458)

~~~diff
- 00460134 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 00460454 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00460134 bytes 28400090
+ 00460454 bytes 284000b0
- 00460138 ["COPY", "tmp:0:8", ["const:268:8"]]
- 00460138 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00460138 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00460138 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00460458 ["COPY", "tmp:0:8", ["const:238:8"]]
+ 00460458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00460458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00460458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00460138 bytes 08a10991
+ 00460458 bytes 08e10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cc27b1b90be318519c2597c4254f1fb"></a>

### [`0046014c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/0046014c.md) → [`0046046c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/0046046c.md) FUN_0046046c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00596d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`00597070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597070.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ef0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.77% / 新版 91.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00460598",
      "incomplete_value": true,
      "site": "00460598",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f9e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00460278",
      "incomplete_value": true,
      "site": "00460278",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ecf:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00460634",
      "incomplete_value": true,
      "site": "00460634",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00460314",
      "incomplete_value": true,
      "site": "00460314",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00460624",
      "incomplete_value": true,
      "site": "00460634",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00460304",
      "incomplete_value": true,
      "site": "00460314",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b98:8"
              ]
            ]
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
      "00460588",
      "READ",
      [
        "storage",
        "002b5ecf",
        null,
        "string"
      ]
    ],
    [
      "004605d0",
      "READ",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "004605dc",
      "READ",
      [
        "storage",
        "00ca4b98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00460588",
      "READ",
      [
        "storage",
        "002b5f9e",
        null,
        "string"
      ]
    ],
    [
      "004605d0",
      "READ",
      [
        "storage",
        "00ca5b60",
        null,
        "undefined1"
      ]
    ],
    [
      "004605dc",
      "READ",
      [
        "storage",
        "00ca5b58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00460314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/0046014c.md#insn-00460314) · [`00460390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/0046014c.md#insn-00460390) · [`0046043c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/0046014c.md#insn-0046043c)
- 新版 [`00460634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/0046046c.md#insn-00460634) · [`004606b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/0046046c.md#insn-004606b0) · [`0046075c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/0046046c.md#insn-0046075c)

~~~diff
- 00460314 ["COPY", "register:0:8", ["register:4040:8"]]
- 00460314 ["INT_ADD", "register:40f0:8", ["const:460314:8", "const:4:8"]]
- 00460314 ["CALLIND", null, ["register:0:8"]]
+ 00460634 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00460634 ["INT_ADD", "register:40f0:8", ["const:460634:8", "const:4:8"]]
+ 00460634 ["CALLIND", null, ["register:0:8"]]
- 00460314 bytes 00013fd6
+ 00460634 bytes 00013fd6
- 00460390 ["COPY", "register:0:8", ["register:4040:8"]]
- 00460390 ["INT_ADD", "register:40f0:8", ["const:460390:8", "const:4:8"]]
- 00460390 ["CALLIND", null, ["register:0:8"]]
+ 004606b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004606b0 ["INT_ADD", "register:40f0:8", ["const:4606b0:8", "const:4:8"]]
+ 004606b0 ["CALLIND", null, ["register:0:8"]]
- 00460390 bytes 00013fd6
+ 004606b0 bytes 00013fd6
- 0046043c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046043c ["INT_ADD", "register:40f0:8", ["const:46043c:8", "const:4:8"]]
- 0046043c ["CALLIND", null, ["register:0:8"]]
+ 0046075c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046075c ["INT_ADD", "register:40f0:8", ["const:46075c:8", "const:4:8"]]
+ 0046075c ["CALLIND", null, ["register:0:8"]]
- 0046043c bytes 00013fd6
+ 0046075c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a0fb016acb163a1018545ae4a08c6a5"></a>

### [`004605ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004605ac.md) → [`004608cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/004608cc.md) FUN_004608cc

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
      "definition_site": "004608d8",
      "incomplete_value": false,
      "site": "004608e4",
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
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004605b8",
      "incomplete_value": false,
      "site": "004605c4",
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
            "const:2e8:8"
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
      "004608e4",
      "DATA",
      [
        "storage",
        "00c642e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004608e4",
      "DATA",
      [
        "storage",
        "00c652b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004605b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004605ac.md#insn-004605b4) · [`004605b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004605ac.md#insn-004605b8)
- 新版 [`004608d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/004608cc.md#insn-004608d4) · [`004608d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/004608cc.md#insn-004608d8)

~~~diff
- 004605b4 ["COPY", "register:4050:8", ["const:c64000:8"]]
+ 004608d4 ["COPY", "register:4050:8", ["const:c65000:8"]]
- 004605b4 bytes 2a400090
+ 004608d4 bytes 2a4000b0
- 004605b8 ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 004605b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004605b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004605b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004608d8 ["COPY", "tmp:0:8", ["const:2b8:8"]]
+ 004608d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004608d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004608d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004605b8 bytes 4aa10b91
+ 004608d8 bytes 4ae10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ac5e758a4309b12f575251b14362952"></a>

### [`004605f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004605f0.md) → [`00460910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460910.md) FUN_00460910

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
      "definition_site": "00460928",
      "incomplete_value": false,
      "site": "00460934",
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
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00460608",
      "incomplete_value": false,
      "site": "00460614",
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
            "const:2e8:8"
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
      "00460934",
      "DATA",
      [
        "storage",
        "00c642e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00460934",
      "DATA",
      [
        "storage",
        "00c652b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00460604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004605f0.md#insn-00460604) · [`00460608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004605f0.md#insn-00460608) · [`00460638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004605f0.md#insn-00460638)
- 新版 [`00460924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460910.md#insn-00460924) · [`00460928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460910.md#insn-00460928) · [`00460958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460910.md#insn-00460958)

~~~diff
- 00460604 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 00460924 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00460604 bytes 28400090
+ 00460924 bytes 284000b0
- 00460608 ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 00460608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00460608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00460608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00460928 ["COPY", "tmp:0:8", ["const:2b8:8"]]
+ 00460928 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00460928 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00460928 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00460608 bytes 08a10b91
+ 00460928 bytes 08e10a91
- 00460638 ["COPY", "register:0:8", ["register:4040:8"]]
- 00460638 ["INT_ADD", "register:40f0:8", ["const:460638:8", "const:4:8"]]
- 00460638 ["CALLIND", null, ["register:0:8"]]
+ 00460958 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00460958 ["INT_ADD", "register:40f0:8", ["const:460958:8", "const:4:8"]]
+ 00460958 ["CALLIND", null, ["register:0:8"]]
- 00460638 bytes 00013fd6
+ 00460958 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6aa15fcbb6457d1351d27c77910de3a8"></a>

### [`0046064c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/0046064c.md) → [`0046096c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/0046096c.md) FUN_0046096c

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
      "definition_site": "00460998",
      "incomplete_value": false,
      "site": "00460998",
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
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00460678",
      "incomplete_value": false,
      "site": "00460678",
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
            "const:2e8:8"
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
      "00460998",
      "DATA",
      [
        "storage",
        "00c642e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00460998",
      "DATA",
      [
        "storage",
        "00c652b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00460660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/0046064c.md#insn-00460660) · [`0046066c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/0046064c.md#insn-0046066c) · [`00460670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/0046064c.md#insn-00460670)
- 新版 [`00460980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/0046096c.md#insn-00460980) · [`0046098c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/0046096c.md#insn-0046098c) · [`00460990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/0046096c.md#insn-00460990)

~~~diff
- 00460660 ["INT_ADD", "register:40f0:8", ["const:460660:8", "const:4:8"]]
- 00460660 ["CALL", null, ["callee:00c58f30:8"]]
+ 00460980 ["INT_ADD", "register:40f0:8", ["const:460980:8", "const:4:8"]]
+ 00460980 ["CALL", null, ["callee:00c58f30:8"]]
- 00460660 bytes 40de1f94
+ 00460980 bytes 6ce11f94
- 0046066c ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0046098c ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0046066c bytes 28400090
+ 0046098c bytes 284000b0
- 00460670 ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 00460670 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00460670 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00460670 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00460990 ["COPY", "tmp:0:8", ["const:2b8:8"]]
+ 00460990 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00460990 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00460990 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00460670 bytes 08a10b91
+ 00460990 bytes 08e10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88d0a701e2e1bdd4a82d58771357151b"></a>

### [`004606d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004606d4.md) → [`004609f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/004609f4.md) FUN_004609f4

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00460a10",
      "incomplete_value": false,
      "site": "00460a10",
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
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004606f0",
      "incomplete_value": false,
      "site": "004606f0",
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
            "const:2e8:8"
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
      "00460a10",
      "DATA",
      [
        "storage",
        "00c642e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00460a10",
      "DATA",
      [
        "storage",
        "00c652b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004606e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004606d4.md#insn-004606e8) · [`004606ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004606d4.md#insn-004606ec) · [`00460710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004606d4.md#insn-00460710)
- 新版 [`00460a08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/004609f4.md#insn-00460a08) · [`00460a0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/004609f4.md#insn-00460a0c) · [`00460a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/004609f4.md#insn-00460a30)

~~~diff
- 004606e8 ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 00460a08 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 004606e8 bytes 29400090
+ 00460a08 bytes 294000b0
- 004606ec ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 004606ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004606ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004606ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00460a0c ["COPY", "tmp:0:8", ["const:2b8:8"]]
+ 00460a0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00460a0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00460a0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004606ec bytes 29a10b91
+ 00460a0c bytes 29e10a91
- 00460710 ["COPY", "register:0:8", ["register:4048:8"]]
- 00460710 ["INT_ADD", "register:40f0:8", ["const:460710:8", "const:4:8"]]
- 00460710 ["CALLIND", null, ["register:0:8"]]
+ 00460a30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00460a30 ["INT_ADD", "register:40f0:8", ["const:460a30:8", "const:4:8"]]
+ 00460a30 ["CALLIND", null, ["register:0:8"]]
- 00460710 bytes 20013fd6
+ 00460a30 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43c5879c1ad4dcb33cc82abddd525b00"></a>

### [`004607d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004607d0.md) → [`00460af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460af0.md) FUN_00460af0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`004614f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004614f0.md) [`00461710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461710.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00461810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00461/00461810.md) [`00461a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00461/00461a30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.41% / 新版 97.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00460c78",
      "incomplete_value": true,
      "site": "00460c84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9ec:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00460958",
      "incomplete_value": true,
      "site": "00460964",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 39,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00460de4",
      "incomplete_value": true,
      "site": "00460df4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2c7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00460ac4",
      "incomplete_value": true,
      "site": "00460ad4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1f8:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00460df8",
      "incomplete_value": true,
      "site": "00460df8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00460ad8",
      "incomplete_value": true,
      "site": "00460ad8",
      "value": [
        "LOAD",
        "8",
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
      "00460c78",
      "READ",
      [
        "storage",
        "002b29a2",
        null,
        "string"
      ]
    ],
    [
      "00460de4",
      "READ",
      [
        "storage",
        "002b71f8",
        null,
        "string"
      ]
    ],
    [
      "00460dec",
      "READ",
      [
        "storage",
        "002b71fd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00460c78",
      "READ",
      [
        "storage",
        "002b29ec",
        null,
        "string"
      ]
    ],
    [
      "00460de4",
      "READ",
      [
        "storage",
        "002b72c7",
        null,
        "string"
      ]
    ],
    [
      "00460dec",
      "READ",
      [
        "storage",
        "002b72cc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00460838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004607d0.md#insn-00460838) · [`00460864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004607d0.md#insn-00460864) · [`00460894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004607d0.md#insn-00460894)
- 新版 [`00460b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460af0.md#insn-00460b58) · [`00460b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460af0.md#insn-00460b84) · [`00460bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/00460af0.md#insn-00460bb4)

~~~diff
- 00460838 ["INT_ADD", "register:40f0:8", ["const:460838:8", "const:4:8"]]
- 00460838 ["CALL", null, ["callee:004413ec:8"]]
+ 00460b58 ["INT_ADD", "register:40f0:8", ["const:460b58:8", "const:4:8"]]
+ 00460b58 ["CALL", null, ["callee:004413ec:8"]]
- 00460838 bytes 2582ff97
+ 00460b58 bytes 2582ff97
- 00460864 ["INT_ADD", "register:40f0:8", ["const:460864:8", "const:4:8"]]
- 00460864 ["CALL", null, ["callee:00c58f50:8"]]
+ 00460b84 ["INT_ADD", "register:40f0:8", ["const:460b84:8", "const:4:8"]]
+ 00460b84 ["CALL", null, ["callee:00c58f50:8"]]
- 00460864 bytes c7dd1f94
+ 00460b84 bytes f3e01f94
- 00460894 ["INT_ADD", "register:40f0:8", ["const:460894:8", "const:4:8"]]
- 00460894 ["CALL", null, ["callee:004413ec:8"]]
+ 00460bb4 ["INT_ADD", "register:40f0:8", ["const:460bb4:8", "const:4:8"]]
+ 00460bb4 ["CALL", null, ["callee:004413ec:8"]]
- 00460894 bytes 0e82ff97
+ 00460bb4 bytes 0e82ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23c15da970da1fbad9f13df754f2314e"></a>

### [`004616a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004616a0.md) → [`004619c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00461/004619c0.md) FUN_004619c0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004614f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004614f0.md) [`00461e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461e08.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`00461810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00461/00461810.md) [`00462128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462128.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "004619cc",
      "incomplete_value": false,
      "site": "004619d0",
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
      "definition_site": "004616ac",
      "incomplete_value": false,
      "site": "004616b0",
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
      "004619cc",
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
      "004619cc",
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

- 旧版 [`004616b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004616a0.md#insn-004616b0) · [`004616a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004616a0.md#insn-004616a8) · [`004616ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004616a0.md#insn-004616ac)
- 新版 [`004619d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00461/004619c0.md#insn-004619d0) · [`004619c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00461/004619c0.md#insn-004619c8) · [`004619cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00461/004619c0.md#insn-004619cc)

~~~diff
- 004616b0 ["INT_ADD", "register:40f0:8", ["const:4616b0:8", "const:4:8"]]
- 004616b0 ["CALL", null, ["callee:0043bad8:8"]]
+ 004619d0 ["INT_ADD", "register:40f0:8", ["const:4619d0:8", "const:4:8"]]
+ 004619d0 ["CALL", null, ["callee:0043bad8:8"]]
- 004616b0 bytes 4268ff97
+ 004619d0 bytes 4268ff97
- 004616a8 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 004619c8 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 004616a8 bytes a0f2ffd0
+ 004619c8 bytes a0f2fff0
- 004616ac ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 004616ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004616ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004616ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004619cc ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 004619cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004619cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004619cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004616ac bytes 00303e91
+ 004619cc bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-341090d5cd4ec3a33867a54f45c6cbb6"></a>

### [`00461a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461a58.md) → [`00461d78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00461/00461d78.md) FUN_00461d78

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00461858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461858.md) [`00461b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461b78.md) [`009bf268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009bf/009bf268.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 3件 [`00461b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00461/00461b78.md) [`00461e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00461/00461e98.md) [`009c0214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009c0/009c0214.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00461d84",
      "incomplete_value": false,
      "site": "00461d88",
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
      "definition_site": "00461a64",
      "incomplete_value": false,
      "site": "00461a68",
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
      "00461d84",
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
      "00461d84",
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

- 旧版 [`00461a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461a58.md#insn-00461a68) · [`00461a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461a58.md#insn-00461a60) · [`00461a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461a58.md#insn-00461a64)
- 新版 [`00461d88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00461/00461d78.md#insn-00461d88) · [`00461d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00461/00461d78.md#insn-00461d80) · [`00461d84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00461/00461d78.md#insn-00461d84)

~~~diff
- 00461a68 ["INT_ADD", "register:40f0:8", ["const:461a68:8", "const:4:8"]]
- 00461a68 ["CALL", null, ["callee:0043bad8:8"]]
+ 00461d88 ["INT_ADD", "register:40f0:8", ["const:461d88:8", "const:4:8"]]
+ 00461d88 ["CALL", null, ["callee:0043bad8:8"]]
- 00461a68 bytes 5467ff97
+ 00461d88 bytes 5467ff97
- 00461a60 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00461d80 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00461a60 bytes a0f2ffd0
+ 00461d80 bytes a0f2fff0
- 00461a64 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00461a64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00461a64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00461a64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00461d84 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00461d84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00461d84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00461d84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00461a64 bytes 00303e91
+ 00461d84 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15ac278a12dc48dcd7d0de95b2041f7b"></a>

### [`00462070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462070.md) → [`00462390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462390.md) FUN_00462390

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
      "definition_site": "0046239c",
      "incomplete_value": false,
      "site": "004623a8",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046207c",
      "incomplete_value": false,
      "site": "00462088",
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
            "const:368:8"
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
      "004623a8",
      "DATA",
      [
        "storage",
        "00c64368",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004623a8",
      "DATA",
      [
        "storage",
        "00c65338",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462070.md#insn-00462078) · [`0046207c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462070.md#insn-0046207c)
- 新版 [`00462398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462390.md#insn-00462398) · [`0046239c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462390.md#insn-0046239c)

~~~diff
- 00462078 ["COPY", "register:4050:8", ["const:c64000:8"]]
+ 00462398 ["COPY", "register:4050:8", ["const:c65000:8"]]
- 00462078 bytes 0a4000d0
+ 00462398 bytes 0a4000f0
- 0046207c ["COPY", "tmp:0:8", ["const:368:8"]]
- 0046207c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0046207c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0046207c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046239c ["COPY", "tmp:0:8", ["const:338:8"]]
+ 0046239c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046239c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046239c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0046207c bytes 4aa10d91
+ 0046239c bytes 4ae10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-308e77af01f68150c84641016b0623b0"></a>

### [`004620b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004620b4.md) → [`004623d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/004623d4.md) FUN_004623d4

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
      "definition_site": "004623ec",
      "incomplete_value": false,
      "site": "004623f8",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004620cc",
      "incomplete_value": false,
      "site": "004620d8",
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
            "const:368:8"
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
      "004623f8",
      "DATA",
      [
        "storage",
        "00c64368",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004623f8",
      "DATA",
      [
        "storage",
        "00c65338",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004620c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004620b4.md#insn-004620c8) · [`004620cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004620b4.md#insn-004620cc) · [`004620fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004620b4.md#insn-004620fc)
- 新版 [`004623e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/004623d4.md#insn-004623e8) · [`004623ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/004623d4.md#insn-004623ec) · [`0046241c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/004623d4.md#insn-0046241c)

~~~diff
- 004620c8 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 004623e8 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 004620c8 bytes 084000d0
+ 004623e8 bytes 084000f0
- 004620cc ["COPY", "tmp:0:8", ["const:368:8"]]
- 004620cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004620cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004620cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004623ec ["COPY", "tmp:0:8", ["const:338:8"]]
+ 004623ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004623ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004623ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004620cc bytes 08a10d91
+ 004623ec bytes 08e10c91
- 004620fc ["COPY", "register:0:8", ["register:4040:8"]]
- 004620fc ["INT_ADD", "register:40f0:8", ["const:4620fc:8", "const:4:8"]]
- 004620fc ["CALLIND", null, ["register:0:8"]]
+ 0046241c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046241c ["INT_ADD", "register:40f0:8", ["const:46241c:8", "const:4:8"]]
+ 0046241c ["CALLIND", null, ["register:0:8"]]
- 004620fc bytes 00013fd6
+ 0046241c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a370aa97cb44f4d4f797a5e10fcdd283"></a>

### [`00462110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462110.md) → [`00462430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462430.md) FUN_00462430

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
      "definition_site": "0046245c",
      "incomplete_value": false,
      "site": "0046245c",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046213c",
      "incomplete_value": false,
      "site": "0046213c",
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
            "const:368:8"
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
      "0046245c",
      "DATA",
      [
        "storage",
        "00c64368",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0046245c",
      "DATA",
      [
        "storage",
        "00c65338",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462110.md#insn-00462124) · [`00462130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462110.md#insn-00462130) · [`00462134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462110.md#insn-00462134)
- 新版 [`00462444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462430.md#insn-00462444) · [`00462450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462430.md#insn-00462450) · [`00462454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462430.md#insn-00462454)

~~~diff
- 00462124 ["INT_ADD", "register:40f0:8", ["const:462124:8", "const:4:8"]]
- 00462124 ["CALL", null, ["callee:00c58f30:8"]]
+ 00462444 ["INT_ADD", "register:40f0:8", ["const:462444:8", "const:4:8"]]
+ 00462444 ["CALL", null, ["callee:00c58f30:8"]]
- 00462124 bytes 8fd71f94
+ 00462444 bytes bbda1f94
- 00462130 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 00462450 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00462130 bytes 084000d0
+ 00462450 bytes 084000f0
- 00462134 ["COPY", "tmp:0:8", ["const:368:8"]]
- 00462134 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00462134 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00462134 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462454 ["COPY", "tmp:0:8", ["const:338:8"]]
+ 00462454 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462454 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00462134 bytes 08a10d91
+ 00462454 bytes 08e10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6a12f7f70187e13b7f042df62ea6117"></a>

### [`00462198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462198.md) → [`004624b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/004624b8.md) FUN_004624b8

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004624d4",
      "incomplete_value": false,
      "site": "004624d4",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004621b4",
      "incomplete_value": false,
      "site": "004621b4",
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
            "const:368:8"
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
      "004624d4",
      "DATA",
      [
        "storage",
        "00c64368",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004624d4",
      "DATA",
      [
        "storage",
        "00c65338",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004621ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462198.md#insn-004621ac) · [`004621b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462198.md#insn-004621b0) · [`004621d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462198.md#insn-004621d4)
- 新版 [`004624cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/004624b8.md#insn-004624cc) · [`004624d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/004624b8.md#insn-004624d0) · [`004624f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/004624b8.md#insn-004624f4)

~~~diff
- 004621ac ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 004624cc ["COPY", "register:4048:8", ["const:c65000:8"]]
- 004621ac bytes 094000d0
+ 004624cc bytes 094000f0
- 004621b0 ["COPY", "tmp:0:8", ["const:368:8"]]
- 004621b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004621b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004621b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004624d0 ["COPY", "tmp:0:8", ["const:338:8"]]
+ 004624d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004624d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004624d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004621b0 bytes 29a10d91
+ 004624d0 bytes 29e10c91
- 004621d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004621d4 ["INT_ADD", "register:40f0:8", ["const:4621d4:8", "const:4:8"]]
- 004621d4 ["CALLIND", null, ["register:0:8"]]
+ 004624f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004624f4 ["INT_ADD", "register:40f0:8", ["const:4624f4:8", "const:4:8"]]
+ 004624f4 ["CALLIND", null, ["register:0:8"]]
- 004621d4 bytes 20013fd6
+ 004624f4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c61541898b484f9324c93c6b22ae0d0e"></a>

### [`00462400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462400.md) → [`00462720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462720.md) FUN_00462720

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
      "definition_site": "0046272c",
      "incomplete_value": false,
      "site": "00462738",
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
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046240c",
      "incomplete_value": false,
      "site": "00462418",
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
            "const:3e8:8"
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
      "00462738",
      "DATA",
      [
        "storage",
        "00c643e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462738",
      "DATA",
      [
        "storage",
        "00c653b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462400.md#insn-00462408) · [`0046240c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462400.md#insn-0046240c)
- 新版 [`00462728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462720.md#insn-00462728) · [`0046272c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462720.md#insn-0046272c)

~~~diff
- 00462408 ["COPY", "register:4050:8", ["const:c64000:8"]]
+ 00462728 ["COPY", "register:4050:8", ["const:c65000:8"]]
- 00462408 bytes 0a4000d0
+ 00462728 bytes 0a4000f0
- 0046240c ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 0046240c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0046240c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0046240c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046272c ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 0046272c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046272c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046272c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0046240c bytes 4aa10f91
+ 0046272c bytes 4ae10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-203532d9ad2f5c4027ea4886e961255b"></a>

### [`00462444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462444.md) → [`00462764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462764.md) FUN_00462764

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
      "definition_site": "0046277c",
      "incomplete_value": false,
      "site": "00462788",
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
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046245c",
      "incomplete_value": false,
      "site": "00462468",
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
            "const:3e8:8"
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
      "00462788",
      "DATA",
      [
        "storage",
        "00c643e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462788",
      "DATA",
      [
        "storage",
        "00c653b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462444.md#insn-00462458) · [`0046245c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462444.md#insn-0046245c) · [`0046248c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462444.md#insn-0046248c)
- 新版 [`00462778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462764.md#insn-00462778) · [`0046277c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462764.md#insn-0046277c) · [`004627ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462764.md#insn-004627ac)

~~~diff
- 00462458 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 00462778 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00462458 bytes 084000d0
+ 00462778 bytes 084000f0
- 0046245c ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 0046245c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046245c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046245c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046277c ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 0046277c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046277c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046277c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046245c bytes 08a10f91
+ 0046277c bytes 08e10e91
- 0046248c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046248c ["INT_ADD", "register:40f0:8", ["const:46248c:8", "const:4:8"]]
- 0046248c ["CALLIND", null, ["register:0:8"]]
+ 004627ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 004627ac ["INT_ADD", "register:40f0:8", ["const:4627ac:8", "const:4:8"]]
+ 004627ac ["CALLIND", null, ["register:0:8"]]
- 0046248c bytes 00013fd6
+ 004627ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51f98300014bd1a0a55dd20e3c76e6f6"></a>

### [`004624a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004624a0.md) → [`004627c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/004627c0.md) FUN_004627c0

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
      "definition_site": "004627ec",
      "incomplete_value": false,
      "site": "004627ec",
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
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004624cc",
      "incomplete_value": false,
      "site": "004624cc",
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
            "const:3e8:8"
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
      "004627ec",
      "DATA",
      [
        "storage",
        "00c643e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004627ec",
      "DATA",
      [
        "storage",
        "00c653b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004624b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004624a0.md#insn-004624b4) · [`004624c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004624a0.md#insn-004624c0) · [`004624c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004624a0.md#insn-004624c4)
- 新版 [`004627d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/004627c0.md#insn-004627d4) · [`004627e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/004627c0.md#insn-004627e0) · [`004627e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/004627c0.md#insn-004627e4)

~~~diff
- 004624b4 ["INT_ADD", "register:40f0:8", ["const:4624b4:8", "const:4:8"]]
- 004624b4 ["CALL", null, ["callee:00c58f30:8"]]
+ 004627d4 ["INT_ADD", "register:40f0:8", ["const:4627d4:8", "const:4:8"]]
+ 004627d4 ["CALL", null, ["callee:00c58f30:8"]]
- 004624b4 bytes abd61f94
+ 004627d4 bytes d7d91f94
- 004624c0 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 004627e0 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 004624c0 bytes 084000d0
+ 004627e0 bytes 084000f0
- 004624c4 ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 004624c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004624c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004624c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004627e4 ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 004627e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004627e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004627e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004624c4 bytes 08a10f91
+ 004627e4 bytes 08e10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bacdd7a6556e459089deb9ef5f6e52e9"></a>

### [`00462528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462528.md) → [`00462848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462848.md) FUN_00462848

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00462864",
      "incomplete_value": false,
      "site": "00462864",
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
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462544",
      "incomplete_value": false,
      "site": "00462544",
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
            "const:3e8:8"
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
      "00462864",
      "DATA",
      [
        "storage",
        "00c643e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462864",
      "DATA",
      [
        "storage",
        "00c653b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046253c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462528.md#insn-0046253c) · [`00462540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462528.md#insn-00462540) · [`00462564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462528.md#insn-00462564)
- 新版 [`0046285c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462848.md#insn-0046285c) · [`00462860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462848.md#insn-00462860) · [`00462884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462848.md#insn-00462884)

~~~diff
- 0046253c ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 0046285c ["COPY", "register:4048:8", ["const:c65000:8"]]
- 0046253c bytes 094000d0
+ 0046285c bytes 094000f0
- 00462540 ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 00462540 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00462540 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00462540 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00462860 ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 00462860 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00462860 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00462860 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00462540 bytes 29a10f91
+ 00462860 bytes 29e10e91
- 00462564 ["COPY", "register:0:8", ["register:4048:8"]]
- 00462564 ["INT_ADD", "register:40f0:8", ["const:462564:8", "const:4:8"]]
- 00462564 ["CALLIND", null, ["register:0:8"]]
+ 00462884 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00462884 ["INT_ADD", "register:40f0:8", ["const:462884:8", "const:4:8"]]
+ 00462884 ["CALLIND", null, ["register:0:8"]]
- 00462564 bytes 20013fd6
+ 00462884 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70812f00c0d767c486232baeb955f530"></a>

### [`004626c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004626c0.md) → [`004629e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/004629e0.md) FUN_004629e0

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
      "definition_site": "004629ec",
      "incomplete_value": false,
      "site": "004629f8",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004626cc",
      "incomplete_value": false,
      "site": "004626d8",
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
            "const:468:8"
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
      "004629f8",
      "DATA",
      [
        "storage",
        "00c64468",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004629f8",
      "DATA",
      [
        "storage",
        "00c65438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004626c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004626c0.md#insn-004626c8) · [`004626cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004626c0.md#insn-004626cc)
- 新版 [`004629e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/004629e0.md#insn-004629e8) · [`004629ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/004629e0.md#insn-004629ec)

~~~diff
- 004626c8 ["COPY", "register:4050:8", ["const:c64000:8"]]
+ 004629e8 ["COPY", "register:4050:8", ["const:c65000:8"]]
- 004626c8 bytes 0a4000d0
+ 004629e8 bytes 0a4000f0
- 004626cc ["COPY", "tmp:0:8", ["const:468:8"]]
- 004626cc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004626cc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004626cc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004629ec ["COPY", "tmp:0:8", ["const:438:8"]]
+ 004629ec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004629ec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004629ec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004626cc bytes 4aa11191
+ 004629ec bytes 4ae11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64bb31b7d66029571e23fa68028c991a"></a>

### [`00462704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462704.md) → [`00462a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462a24.md) FUN_00462a24

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
      "definition_site": "00462a3c",
      "incomplete_value": false,
      "site": "00462a48",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046271c",
      "incomplete_value": false,
      "site": "00462728",
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
            "const:468:8"
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
      "00462a48",
      "DATA",
      [
        "storage",
        "00c64468",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462a48",
      "DATA",
      [
        "storage",
        "00c65438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462704.md#insn-00462718) · [`0046271c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462704.md#insn-0046271c) · [`0046274c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462704.md#insn-0046274c)
- 新版 [`00462a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462a24.md#insn-00462a38) · [`00462a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462a24.md#insn-00462a3c) · [`00462a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462a24.md#insn-00462a6c)

~~~diff
- 00462718 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 00462a38 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00462718 bytes 084000d0
+ 00462a38 bytes 084000f0
- 0046271c ["COPY", "tmp:0:8", ["const:468:8"]]
- 0046271c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046271c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046271c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462a3c ["COPY", "tmp:0:8", ["const:438:8"]]
+ 00462a3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462a3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462a3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046271c bytes 08a11191
+ 00462a3c bytes 08e11091
- 0046274c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046274c ["INT_ADD", "register:40f0:8", ["const:46274c:8", "const:4:8"]]
- 0046274c ["CALLIND", null, ["register:0:8"]]
+ 00462a6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00462a6c ["INT_ADD", "register:40f0:8", ["const:462a6c:8", "const:4:8"]]
+ 00462a6c ["CALLIND", null, ["register:0:8"]]
- 0046274c bytes 00013fd6
+ 00462a6c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e65a49909d38c8ca469ffd6261d4d7e"></a>

### [`00462760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462760.md) → [`00462a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462a80.md) FUN_00462a80

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
      "definition_site": "00462aac",
      "incomplete_value": false,
      "site": "00462aac",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046278c",
      "incomplete_value": false,
      "site": "0046278c",
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
            "const:468:8"
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
      "00462aac",
      "DATA",
      [
        "storage",
        "00c64468",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462aac",
      "DATA",
      [
        "storage",
        "00c65438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462760.md#insn-00462774) · [`00462780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462760.md#insn-00462780) · [`00462784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462760.md#insn-00462784)
- 新版 [`00462a94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462a80.md#insn-00462a94) · [`00462aa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462a80.md#insn-00462aa0) · [`00462aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462a80.md#insn-00462aa4)

~~~diff
- 00462774 ["INT_ADD", "register:40f0:8", ["const:462774:8", "const:4:8"]]
- 00462774 ["CALL", null, ["callee:00c58f30:8"]]
+ 00462a94 ["INT_ADD", "register:40f0:8", ["const:462a94:8", "const:4:8"]]
+ 00462a94 ["CALL", null, ["callee:00c58f30:8"]]
- 00462774 bytes fbd51f94
+ 00462a94 bytes 27d91f94
- 00462780 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 00462aa0 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00462780 bytes 084000d0
+ 00462aa0 bytes 084000f0
- 00462784 ["COPY", "tmp:0:8", ["const:468:8"]]
- 00462784 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00462784 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00462784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462aa4 ["COPY", "tmp:0:8", ["const:438:8"]]
+ 00462aa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462aa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462aa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00462784 bytes 08a11191
+ 00462aa4 bytes 08e11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bc73ddc2c8832048fb90b80d7948a56"></a>

### [`004627e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004627e8.md) → [`00462b08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462b08.md) FUN_00462b08

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00462b24",
      "incomplete_value": false,
      "site": "00462b24",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462804",
      "incomplete_value": false,
      "site": "00462804",
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
            "const:468:8"
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
      "00462b24",
      "DATA",
      [
        "storage",
        "00c64468",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462b24",
      "DATA",
      [
        "storage",
        "00c65438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004627fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004627e8.md#insn-004627fc) · [`00462800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004627e8.md#insn-00462800) · [`00462824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004627e8.md#insn-00462824)
- 新版 [`00462b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462b08.md#insn-00462b1c) · [`00462b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462b08.md#insn-00462b20) · [`00462b44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462b08.md#insn-00462b44)

~~~diff
- 004627fc ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 00462b1c ["COPY", "register:4048:8", ["const:c65000:8"]]
- 004627fc bytes 094000d0
+ 00462b1c bytes 094000f0
- 00462800 ["COPY", "tmp:0:8", ["const:468:8"]]
- 00462800 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00462800 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00462800 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00462b20 ["COPY", "tmp:0:8", ["const:438:8"]]
+ 00462b20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00462b20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00462b20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00462800 bytes 29a11191
+ 00462b20 bytes 29e11091
- 00462824 ["COPY", "register:0:8", ["register:4048:8"]]
- 00462824 ["INT_ADD", "register:40f0:8", ["const:462824:8", "const:4:8"]]
- 00462824 ["CALLIND", null, ["register:0:8"]]
+ 00462b44 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00462b44 ["INT_ADD", "register:40f0:8", ["const:462b44:8", "const:4:8"]]
+ 00462b44 ["CALLIND", null, ["register:0:8"]]
- 00462824 bytes 20013fd6
+ 00462b44 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7afcf3438cc488808087a839339f1b31"></a>

### [`00462980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462980.md) → [`00462ca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462ca0.md) FUN_00462ca0

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
      "definition_site": "00462cac",
      "incomplete_value": false,
      "site": "00462cb8",
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
            "const:4b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046298c",
      "incomplete_value": false,
      "site": "00462998",
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
      "00462cb8",
      "DATA",
      [
        "storage",
        "00c644e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462cb8",
      "DATA",
      [
        "storage",
        "00c654b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462980.md#insn-00462988) · [`0046298c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462980.md#insn-0046298c)
- 新版 [`00462ca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462ca0.md#insn-00462ca8) · [`00462cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462ca0.md#insn-00462cac)

~~~diff
- 00462988 ["COPY", "register:4050:8", ["const:c64000:8"]]
+ 00462ca8 ["COPY", "register:4050:8", ["const:c65000:8"]]
- 00462988 bytes 0a4000d0
+ 00462ca8 bytes 0a4000f0
- 0046298c ["COPY", "tmp:0:8", ["const:4e8:8"]]
- 0046298c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0046298c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0046298c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00462cac ["COPY", "tmp:0:8", ["const:4b8:8"]]
+ 00462cac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00462cac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00462cac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0046298c bytes 4aa11391
+ 00462cac bytes 4ae11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc008f7a43a5490df60097bfdc73d400"></a>

### [`004629c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004629c4.md) → [`00462ce4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462ce4.md) FUN_00462ce4

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
      "definition_site": "00462cfc",
      "incomplete_value": false,
      "site": "00462d08",
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
            "const:4b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004629dc",
      "incomplete_value": false,
      "site": "004629e8",
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
      "00462d08",
      "DATA",
      [
        "storage",
        "00c644e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462d08",
      "DATA",
      [
        "storage",
        "00c654b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004629d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004629c4.md#insn-004629d8) · [`004629dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004629c4.md#insn-004629dc) · [`00462a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004629c4.md#insn-00462a0c)
- 新版 [`00462cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462ce4.md#insn-00462cf8) · [`00462cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462ce4.md#insn-00462cfc) · [`00462d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462ce4.md#insn-00462d2c)

~~~diff
- 004629d8 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 00462cf8 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 004629d8 bytes 084000d0
+ 00462cf8 bytes 084000f0
- 004629dc ["COPY", "tmp:0:8", ["const:4e8:8"]]
- 004629dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004629dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004629dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462cfc ["COPY", "tmp:0:8", ["const:4b8:8"]]
+ 00462cfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462cfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462cfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004629dc bytes 08a11391
+ 00462cfc bytes 08e11291
- 00462a0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00462a0c ["INT_ADD", "register:40f0:8", ["const:462a0c:8", "const:4:8"]]
- 00462a0c ["CALLIND", null, ["register:0:8"]]
+ 00462d2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00462d2c ["INT_ADD", "register:40f0:8", ["const:462d2c:8", "const:4:8"]]
+ 00462d2c ["CALLIND", null, ["register:0:8"]]
- 00462a0c bytes 00013fd6
+ 00462d2c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17f8177f8d00c47d7219baa4646f9ea8"></a>

### [`00462a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462a20.md) → [`00462d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462d40.md) FUN_00462d40

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
      "definition_site": "00462d6c",
      "incomplete_value": false,
      "site": "00462d6c",
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
            "const:4b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462a4c",
      "incomplete_value": false,
      "site": "00462a4c",
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
      "00462d6c",
      "DATA",
      [
        "storage",
        "00c644e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462d6c",
      "DATA",
      [
        "storage",
        "00c654b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462a34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462a20.md#insn-00462a34) · [`00462a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462a20.md#insn-00462a40) · [`00462a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462a20.md#insn-00462a44)
- 新版 [`00462d54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462d40.md#insn-00462d54) · [`00462d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462d40.md#insn-00462d60) · [`00462d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462d40.md#insn-00462d64)

~~~diff
- 00462a34 ["INT_ADD", "register:40f0:8", ["const:462a34:8", "const:4:8"]]
- 00462a34 ["CALL", null, ["callee:00c58f30:8"]]
+ 00462d54 ["INT_ADD", "register:40f0:8", ["const:462d54:8", "const:4:8"]]
+ 00462d54 ["CALL", null, ["callee:00c58f30:8"]]
- 00462a34 bytes 4bd51f94
+ 00462d54 bytes 77d81f94
- 00462a40 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 00462d60 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00462a40 bytes 084000d0
+ 00462d60 bytes 084000f0
- 00462a44 ["COPY", "tmp:0:8", ["const:4e8:8"]]
- 00462a44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00462a44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00462a44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462d64 ["COPY", "tmp:0:8", ["const:4b8:8"]]
+ 00462d64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462d64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462d64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00462a44 bytes 08a11391
+ 00462d64 bytes 08e11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c72dd5886454ee3522a0190d6e0d92ec"></a>

### [`00462aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462aa8.md) → [`00462dc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462dc8.md) FUN_00462dc8

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00462de4",
      "incomplete_value": false,
      "site": "00462de4",
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
            "const:4b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462ac4",
      "incomplete_value": false,
      "site": "00462ac4",
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
      "00462de4",
      "DATA",
      [
        "storage",
        "00c644e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462de4",
      "DATA",
      [
        "storage",
        "00c654b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462abc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462aa8.md#insn-00462abc) · [`00462ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462aa8.md#insn-00462ac0) · [`00462ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462aa8.md#insn-00462ae4)
- 新版 [`00462ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462dc8.md#insn-00462ddc) · [`00462de0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462dc8.md#insn-00462de0) · [`00462e04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00462/00462dc8.md#insn-00462e04)

~~~diff
- 00462abc ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 00462ddc ["COPY", "register:4048:8", ["const:c65000:8"]]
- 00462abc bytes 094000d0
+ 00462ddc bytes 094000f0
- 00462ac0 ["COPY", "tmp:0:8", ["const:4e8:8"]]
- 00462ac0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00462ac0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00462ac0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00462de0 ["COPY", "tmp:0:8", ["const:4b8:8"]]
+ 00462de0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00462de0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00462de0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00462ac0 bytes 29a11391
+ 00462de0 bytes 29e11291
- 00462ae4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00462ae4 ["INT_ADD", "register:40f0:8", ["const:462ae4:8", "const:4:8"]]
- 00462ae4 ["CALLIND", null, ["register:0:8"]]
+ 00462e04 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00462e04 ["INT_ADD", "register:40f0:8", ["const:462e04:8", "const:4:8"]]
+ 00462e04 ["CALLIND", null, ["register:0:8"]]
- 00462ae4 bytes 20013fd6
+ 00462e04 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19f1edc1729d46e0fec933c438ea5d47"></a>

### [`00462dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462dfc.md) → [`0046311c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/0046311c.md) FUN_0046311c

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
      "definition_site": "00463128",
      "incomplete_value": false,
      "site": "00463134",
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
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462e08",
      "incomplete_value": false,
      "site": "00462e14",
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
            "const:568:8"
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
      "00463134",
      "DATA",
      [
        "storage",
        "00c64568",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463134",
      "DATA",
      [
        "storage",
        "00c65538",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462dfc.md#insn-00462e04) · [`00462e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462dfc.md#insn-00462e08)
- 新版 [`00463124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/0046311c.md#insn-00463124) · [`00463128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/0046311c.md#insn-00463128)

~~~diff
- 00462e04 ["COPY", "register:4050:8", ["const:c64000:8"]]
+ 00463124 ["COPY", "register:4050:8", ["const:c65000:8"]]
- 00462e04 bytes 0a4000d0
+ 00463124 bytes 0a4000d0
- 00462e08 ["COPY", "tmp:0:8", ["const:568:8"]]
- 00462e08 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00462e08 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00462e08 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00463128 ["COPY", "tmp:0:8", ["const:538:8"]]
+ 00463128 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00463128 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00463128 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00462e08 bytes 4aa11591
+ 00463128 bytes 4ae11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32c691716a958dccec24b8b3cf94cfcf"></a>

### [`00462e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462e40.md) → [`00463160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/00463160.md) FUN_00463160

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
      "definition_site": "00463178",
      "incomplete_value": false,
      "site": "00463184",
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
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462e58",
      "incomplete_value": false,
      "site": "00462e64",
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
            "const:568:8"
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
      "00463184",
      "DATA",
      [
        "storage",
        "00c64568",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463184",
      "DATA",
      [
        "storage",
        "00c65538",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462e54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462e40.md#insn-00462e54) · [`00462e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462e40.md#insn-00462e58) · [`00462e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462e40.md#insn-00462e88)
- 新版 [`00463174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/00463160.md#insn-00463174) · [`00463178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/00463160.md#insn-00463178) · [`004631a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/00463160.md#insn-004631a8)

~~~diff
- 00462e54 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 00463174 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00462e54 bytes 084000d0
+ 00463174 bytes 084000d0
- 00462e58 ["COPY", "tmp:0:8", ["const:568:8"]]
- 00462e58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00462e58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00462e58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463178 ["COPY", "tmp:0:8", ["const:538:8"]]
+ 00463178 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463178 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463178 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00462e58 bytes 08a11591
+ 00463178 bytes 08e11491
- 00462e88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00462e88 ["INT_ADD", "register:40f0:8", ["const:462e88:8", "const:4:8"]]
- 00462e88 ["CALLIND", null, ["register:0:8"]]
+ 004631a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004631a8 ["INT_ADD", "register:40f0:8", ["const:4631a8:8", "const:4:8"]]
+ 004631a8 ["CALLIND", null, ["register:0:8"]]
- 00462e88 bytes 00013fd6
+ 004631a8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-486c7ab603e9f6860e543686eb506360"></a>

### [`00462e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462e9c.md) → [`004631bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/004631bc.md) FUN_004631bc

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
      "definition_site": "004631e8",
      "incomplete_value": false,
      "site": "004631e8",
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
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462ec8",
      "incomplete_value": false,
      "site": "00462ec8",
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
            "const:568:8"
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
      "004631e8",
      "DATA",
      [
        "storage",
        "00c64568",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004631e8",
      "DATA",
      [
        "storage",
        "00c65538",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462e9c.md#insn-00462eb0) · [`00462ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462e9c.md#insn-00462ebc) · [`00462ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462e9c.md#insn-00462ec0)
- 新版 [`004631d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/004631bc.md#insn-004631d0) · [`004631dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/004631bc.md#insn-004631dc) · [`004631e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/004631bc.md#insn-004631e0)

~~~diff
- 00462eb0 ["INT_ADD", "register:40f0:8", ["const:462eb0:8", "const:4:8"]]
- 00462eb0 ["CALL", null, ["callee:00c58f30:8"]]
+ 004631d0 ["INT_ADD", "register:40f0:8", ["const:4631d0:8", "const:4:8"]]
+ 004631d0 ["CALL", null, ["callee:00c58f30:8"]]
- 00462eb0 bytes 2cd41f94
+ 004631d0 bytes 58d71f94
- 00462ebc ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 004631dc ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00462ebc bytes 084000d0
+ 004631dc bytes 084000d0
- 00462ec0 ["COPY", "tmp:0:8", ["const:568:8"]]
- 00462ec0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00462ec0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00462ec0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004631e0 ["COPY", "tmp:0:8", ["const:538:8"]]
+ 004631e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004631e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004631e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00462ec0 bytes 08a11591
+ 004631e0 bytes 08e11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1117c968a5b740b4df6d63f53864d4e5"></a>

### [`00462f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462f24.md) → [`00463244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/00463244.md) FUN_00463244

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463260",
      "incomplete_value": false,
      "site": "00463260",
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
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462f40",
      "incomplete_value": false,
      "site": "00462f40",
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
            "const:568:8"
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
      "00463260",
      "DATA",
      [
        "storage",
        "00c64568",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463260",
      "DATA",
      [
        "storage",
        "00c65538",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462f24.md#insn-00462f38) · [`00462f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462f24.md#insn-00462f3c) · [`00462f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462f24.md#insn-00462f60)
- 新版 [`00463258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/00463244.md#insn-00463258) · [`0046325c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/00463244.md#insn-0046325c) · [`00463280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/00463244.md#insn-00463280)

~~~diff
- 00462f38 ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 00463258 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 00462f38 bytes 094000d0
+ 00463258 bytes 094000d0
- 00462f3c ["COPY", "tmp:0:8", ["const:568:8"]]
- 00462f3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00462f3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00462f3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0046325c ["COPY", "tmp:0:8", ["const:538:8"]]
+ 0046325c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0046325c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0046325c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00462f3c bytes 29a11591
+ 0046325c bytes 29e11491
- 00462f60 ["COPY", "register:0:8", ["register:4048:8"]]
- 00462f60 ["INT_ADD", "register:40f0:8", ["const:462f60:8", "const:4:8"]]
- 00462f60 ["CALLIND", null, ["register:0:8"]]
+ 00463280 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00463280 ["INT_ADD", "register:40f0:8", ["const:463280:8", "const:4:8"]]
+ 00463280 ["CALLIND", null, ["register:0:8"]]
- 00462f60 bytes 20013fd6
+ 00463280 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4deb6a015f32d4c6af7fa133c323b3af"></a>

### [`004630c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/004630c4.md) → [`004633e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/004633e4.md) FUN_004633e4

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
      "definition_site": "004633f0",
      "incomplete_value": false,
      "site": "004633fc",
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
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004630d0",
      "incomplete_value": false,
      "site": "004630dc",
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
            "const:5e8:8"
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
      "004633fc",
      "DATA",
      [
        "storage",
        "00c645e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004633fc",
      "DATA",
      [
        "storage",
        "00c655b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004630cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/004630c4.md#insn-004630cc) · [`004630d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/004630c4.md#insn-004630d0)
- 新版 [`004633ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/004633e4.md#insn-004633ec) · [`004633f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/004633e4.md#insn-004633f0)

~~~diff
- 004630cc ["COPY", "register:4050:8", ["const:c64000:8"]]
+ 004633ec ["COPY", "register:4050:8", ["const:c65000:8"]]
- 004630cc bytes 0a4000b0
+ 004633ec bytes 0a4000d0
- 004630d0 ["COPY", "tmp:0:8", ["const:5e8:8"]]
- 004630d0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004630d0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004630d0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004633f0 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 004633f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004633f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004633f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004630d0 bytes 4aa11791
+ 004633f0 bytes 4ae11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0262304cc60afe5f7ffefe3cd9e49fa4"></a>

### [`00463108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463108.md) → [`00463428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/00463428.md) FUN_00463428

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
      "definition_site": "00463440",
      "incomplete_value": false,
      "site": "0046344c",
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
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463120",
      "incomplete_value": false,
      "site": "0046312c",
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
            "const:5e8:8"
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
      "0046344c",
      "DATA",
      [
        "storage",
        "00c645e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0046344c",
      "DATA",
      [
        "storage",
        "00c655b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046311c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463108.md#insn-0046311c) · [`00463120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463108.md#insn-00463120) · [`00463150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463108.md#insn-00463150)
- 新版 [`0046343c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/00463428.md#insn-0046343c) · [`00463440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/00463428.md#insn-00463440) · [`00463470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00463/00463428.md#insn-00463470)

~~~diff
- 0046311c ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0046343c ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0046311c bytes 084000b0
+ 0046343c bytes 084000d0
- 00463120 ["COPY", "tmp:0:8", ["const:5e8:8"]]
- 00463120 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00463120 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00463120 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463440 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 00463440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00463120 bytes 08a11791
+ 00463440 bytes 08e11691
- 00463150 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463150 ["INT_ADD", "register:40f0:8", ["const:463150:8", "const:4:8"]]
- 00463150 ["CALLIND", null, ["register:0:8"]]
+ 00463470 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463470 ["INT_ADD", "register:40f0:8", ["const:463470:8", "const:4:8"]]
+ 00463470 ["CALLIND", null, ["register:0:8"]]
- 00463150 bytes 00013fd6
+ 00463470 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

