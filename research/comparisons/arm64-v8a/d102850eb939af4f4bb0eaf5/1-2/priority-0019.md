# v16.0.2 → v16.0.3 · 最優先の変更候補 (19)

[一覧の目次](README.md)

<a id="compare-d56e7bb4be5952ea6b343429f368b698"></a>

### [`0058f678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f678.md) → [`0058f998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f998.md) FUN_0058f998

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
      "definition_site": "0058f99c",
      "incomplete_value": false,
      "site": "0058f9a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f67c",
      "incomplete_value": false,
      "site": "0058f680",
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
      "0058f9a0",
      "DATA",
      [
        "storage",
        "00c6d090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058f9a0",
      "DATA",
      [
        "storage",
        "00c6e060",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f678.md#insn-0058f678) · [`0058f67c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f678.md#insn-0058f67c)
- 新版 [`0058f998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f998.md#insn-0058f998) · [`0058f99c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f998.md#insn-0058f99c)

~~~diff
- 0058f678 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0058f998 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0058f678 bytes e83600d0
+ 0058f998 bytes e83600f0
- 0058f67c ["COPY", "tmp:0:8", ["const:90:8"]]
- 0058f67c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f67c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f67c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f99c ["COPY", "tmp:0:8", ["const:60:8"]]
+ 0058f99c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f99c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f99c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f67c bytes 08410291
+ 0058f99c bytes 08810191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba283c2542ba4b573606865c2ef902d3"></a>

### [`0058f688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f688.md) → [`0058f9a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f9a8.md) FUN_0058f9a8

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
      "definition_site": "0058f9b8",
      "incomplete_value": false,
      "site": "0058f9c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f698",
      "incomplete_value": false,
      "site": "0058f6a0",
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
      "0058f9c0",
      "DATA",
      [
        "storage",
        "00c6d090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058f9c0",
      "DATA",
      [
        "storage",
        "00c6e060",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f688.md#insn-0058f694) · [`0058f698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f688.md#insn-0058f698) · [`0058f6a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f688.md#insn-0058f6a4)
- 新版 [`0058f9b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f9a8.md#insn-0058f9b4) · [`0058f9b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f9a8.md#insn-0058f9b8) · [`0058f9c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f9a8.md#insn-0058f9c4)

~~~diff
- 0058f694 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0058f9b4 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0058f694 bytes e83600d0
+ 0058f9b4 bytes e83600f0
- 0058f698 ["COPY", "tmp:0:8", ["const:90:8"]]
- 0058f698 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f698 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f698 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f9b8 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 0058f9b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f9b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f9b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f698 bytes 08410291
+ 0058f9b8 bytes 08810191
- 0058f6a4 ["INT_ADD", "register:40f0:8", ["const:58f6a4:8", "const:4:8"]]
- 0058f6a4 ["CALL", null, ["callee:00c58f40:8"]]
+ 0058f9c4 ["INT_ADD", "register:40f0:8", ["const:58f9c4:8", "const:4:8"]]
+ 0058f9c4 ["CALL", null, ["callee:00c58f40:8"]]
- 0058f6a4 bytes 33221b94
+ 0058f9c4 bytes 5f251b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee59ff1f36eafc977116d1a60bf7baf2"></a>

### [`0058f6b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f6b8.md) → [`0058f9d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f9d8.md) FUN_0058f9d8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0058a8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8fc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0058ac1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058a/0058ac1c.md)

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
      "definition_site": "0058f9e8",
      "incomplete_value": false,
      "site": "0058f9f0",
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
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f6c8",
      "incomplete_value": false,
      "site": "0058f6d0",
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
            "const:8:8"
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
      "0058f9f0",
      "DATA",
      [
        "storage",
        "00c6d008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058f9f0",
      "DATA",
      [
        "storage",
        "00c6dfd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f6b8.md#insn-0058f6c8) · [`0058f6d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f6b8.md#insn-0058f6d8)
- 新版 [`0058f9e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f9d8.md#insn-0058f9e8) · [`0058f9f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f9d8.md#insn-0058f9f8)

~~~diff
- 0058f6c8 ["COPY", "tmp:0:8", ["const:8:8"]]
- 0058f6c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058f6c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058f6c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058f9e8 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 0058f9e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f9e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058f9e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058f6c8 bytes 08210091
+ 0058f9e8 bytes 08613f91
- 0058f6d8 ["INT_ADD", "register:40f0:8", ["const:58f6d8:8", "const:4:8"]]
- 0058f6d8 ["CALL", null, ["callee:0058ac1c:8"]]
+ 0058f9f8 ["INT_ADD", "register:40f0:8", ["const:58f9f8:8", "const:4:8"]]
+ 0058f9f8 ["CALL", null, ["callee:0058ac1c:8"]]
- 0058f6d8 bytes 89ecff97
+ 0058f9f8 bytes 89ecff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4734053d7aae2a5ad0ad08fafba1fd0"></a>

### [`0058f6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f6f0.md) → [`0058fa10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fa10.md) _INIT_34

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`0057a998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057a/0057a998.md) [`0058ccc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058ccc0.md) [`00bfa1ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfa1ac.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0057acb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057a/0057acb8.md) [`0058cfe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058c/0058cfe0.md) [`00bfb1a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfb1a0.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fa3c",
      "incomplete_value": false,
      "site": "0058fa3c",
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
                "const:458:8"
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
      "definition_site": "0058f71c",
      "incomplete_value": false,
      "site": "0058f71c",
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
                "const:498:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fa40",
      "incomplete_value": false,
      "site": "0058fa40",
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
                "const:458:8"
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
      "definition_site": "0058f720",
      "incomplete_value": false,
      "site": "0058f720",
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
                "const:498:8"
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
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fa44",
      "incomplete_value": false,
      "site": "0058fa44",
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
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f724",
      "incomplete_value": false,
      "site": "0058f724",
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
            "const:498:8"
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
      "0058fa20",
      "PARAM",
      [
        "storage",
        "00ca6498",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fa34",
      "PARAM",
      [
        "storage",
        "0057a998",
        null,
        null
      ]
    ],
    [
      "0058fa38",
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
      "0058fa20",
      "PARAM",
      [
        "storage",
        "00ca7458",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fa34",
      "PARAM",
      [
        "storage",
        "0057acb8",
        null,
        null
      ]
    ],
    [
      "0058fa38",
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

- 旧版 [`0058f728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f6f0.md#insn-0058f728) · [`0058f740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f6f0.md#insn-0058f740) · [`0058f6fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f6f0.md#insn-0058f6fc)
- 新版 [`0058fa48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fa10.md#insn-0058fa48) · [`0058fa60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fa10.md#insn-0058fa60) · [`0058fa1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fa10.md#insn-0058fa1c)

~~~diff
- 0058f728 ["INT_ADD", "register:40f0:8", ["const:58f728:8", "const:4:8"]]
- 0058f728 ["CALL", null, ["callee:00c58ed0:8"]]
+ 0058fa48 ["INT_ADD", "register:40f0:8", ["const:58fa48:8", "const:4:8"]]
+ 0058fa48 ["CALL", null, ["callee:00c58ed0:8"]]
- 0058f728 bytes f6211b94
+ 0058fa48 bytes 22251b94
- 0058f740 ["INT_ADD", "register:40f0:8", ["const:58f740:8", "const:4:8"]]
- 0058f740 ["CALL", null, ["callee:00c58ed0:8"]]
+ 0058fa60 ["INT_ADD", "register:40f0:8", ["const:58fa60:8", "const:4:8"]]
+ 0058fa60 ["CALL", null, ["callee:00c58ed0:8"]]
- 0058f740 bytes f0211b94
+ 0058fa60 bytes 1c251b94
- 0058f6fc ["COPY", "register:4008:8", ["const:ca6000:8"]]
+ 0058fa1c ["COPY", "register:4008:8", ["const:ca7000:8"]]
- 0058f6fc bytes a13800f0
+ 0058fa1c bytes c1380090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7a1f1d40fef1ff7abc906acd3046158"></a>

### [`0058f7c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f7c8.md) → [`0058fae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fae8.md) FUN_0058fae8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058fa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fa88.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0058fda8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fda8.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fb40",
      "incomplete_value": false,
      "site": "0058fb40",
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
                "const:534:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f820",
      "incomplete_value": false,
      "site": "0058f820",
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
                "const:574:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fb48",
      "incomplete_value": false,
      "site": "0058fb48",
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
                "const:534:8"
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
      "definition_site": "0058f828",
      "incomplete_value": false,
      "site": "0058f828",
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
                "const:574:8"
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
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0058fbf8",
      "incomplete_value": true,
      "site": "0058fbf8",
      "value": [
        "LOAD",
        "8",
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
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058f8d8",
      "incomplete_value": true,
      "site": "0058f8d8",
      "value": [
        "LOAD",
        "8",
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
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058fb34",
      "READ",
      [
        "storage",
        "00ca6610",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fb40",
      "WRITE",
      [
        "storage",
        "00ca6580",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fb48",
      "WRITE",
      [
        "storage",
        "00ca6578",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058fb34",
      "READ",
      [
        "storage",
        "00ca75d0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fb40",
      "WRITE",
      [
        "storage",
        "00ca7540",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fb48",
      "WRITE",
      [
        "storage",
        "00ca7538",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f7c8.md#insn-0058f8d8) · [`0058f8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f7c8.md#insn-0058f8f0) · [`0058f7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f7c8.md#insn-0058f7fc)
- 新版 [`0058fbf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fae8.md#insn-0058fbf8) · [`0058fc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fae8.md#insn-0058fc10) · [`0058fb1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fae8.md#insn-0058fb1c)

~~~diff
- 0058f8d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f8d8 ["INT_ADD", "register:40f0:8", ["const:58f8d8:8", "const:4:8"]]
- 0058f8d8 ["CALLIND", null, ["register:0:8"]]
+ 0058fbf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058fbf8 ["INT_ADD", "register:40f0:8", ["const:58fbf8:8", "const:4:8"]]
+ 0058fbf8 ["CALLIND", null, ["register:0:8"]]
- 0058f8d8 bytes 00013fd6
+ 0058fbf8 bytes 00013fd6
- 0058f8f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058f8f0 ["INT_ADD", "register:40f0:8", ["const:58f8f0:8", "const:4:8"]]
- 0058f8f0 ["CALLIND", null, ["register:0:8"]]
+ 0058fc10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058fc10 ["INT_ADD", "register:40f0:8", ["const:58fc10:8", "const:4:8"]]
+ 0058fc10 ["CALLIND", null, ["register:0:8"]]
- 0058f8f0 bytes 00013fd6
+ 0058fc10 bytes 00013fd6
- 0058f7fc ["COPY", "register:40a8:8", ["const:ca6000:8"]]
+ 0058fb1c ["COPY", "register:40a8:8", ["const:ca7000:8"]]
- 0058f7fc bytes b53800f0
+ 0058fb1c bytes d5380090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e96e9d563f566e7511431d96048257e"></a>

### [`0058f940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f940.md) → [`0058fc60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fc60.md) FUN_0058fc60

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0058fa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fa88.md) · 呼出先 3件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`0058fda8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fda8.md) · 呼出先 3件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 75.61% / 新版 75.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 4件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fd3c",
      "incomplete_value": false,
      "site": "0058fd3c",
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
                "const:5d8:8"
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
      "definition_site": "0058fa1c",
      "incomplete_value": false,
      "site": "0058fa1c",
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
                "const:618:8"
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
      "definition_site": "0058fd44",
      "incomplete_value": false,
      "site": "0058fd44",
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
                "const:5d8:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fa24",
      "incomplete_value": false,
      "site": "0058fa24",
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
                "const:618:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:18:8"
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
      "definition_site": "0058fd44",
      "incomplete_value": false,
      "site": "0058fd44",
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
                "const:18:8"
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
      "definition_site": "0058fa24",
      "incomplete_value": false,
      "site": "0058fa24",
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
                "const:18:8"
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
      "0058fc80",
      "READ",
      [
        "storage",
        "00ca6530",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fca8",
      "READ",
      [
        "storage",
        "00ca6538",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fcac",
      "WRITE",
      [
        "storage",
        "00ca6530",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058fc80",
      "READ",
      [
        "storage",
        "00ca74f0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fca8",
      "READ",
      [
        "storage",
        "00ca74f8",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fcac",
      "WRITE",
      [
        "storage",
        "00ca74f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058f95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f940.md#insn-0058f95c) · [`0058f960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f940.md#insn-0058f960) · [`0058f97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f940.md#insn-0058f97c)
- 新版 [`0058fc7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fc60.md#insn-0058fc7c) · [`0058fc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fc60.md#insn-0058fc80) · [`0058fc9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fc60.md#insn-0058fc9c)

~~~diff
- 0058f95c ["COPY", "register:4040:8", ["const:ca6000:8"]]
+ 0058fc7c ["COPY", "register:4040:8", ["const:ca7000:8"]]
- 0058f95c bytes a83800f0
+ 0058fc7c bytes c8380090
- 0058f960 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:530:8"]]
- 0058f960 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0058fc80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4f0:8"]]
+ 0058fc80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0058f960 bytes 089942f9
+ 0058fc80 bytes 087942f9
- 0058f97c ["INT_ADD", "register:40f0:8", ["const:58f97c:8", "const:4:8"]]
- 0058f97c ["CALL", null, ["callee:00c54d60:8"]]
+ 0058fc9c ["INT_ADD", "register:40f0:8", ["const:58fc9c:8", "const:4:8"]]
+ 0058fc9c ["CALL", null, ["callee:00c54d60:8"]]
- 0058f97c bytes fd101b94
+ 0058fc9c bytes 31141b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcd50a6810cd3c396fd7a62e5dc414ac"></a>

### [`0058fa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fa88.md) → [`0058fda8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fda8.md) FUN_0058fda8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0043b03c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b03c.md) [`0043b2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2ec.md) [`00467d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467d84.md) · 呼出先 5件 [`0058f7c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f7c8.md) [`0058f940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f940.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 3件 [`0043b35c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b35c.md) [`0043b60c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b60c.md) [`004680a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/004680a4.md) · 呼出先 5件 [`0058fae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fae8.md) [`0058fc60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fc60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 81.16% / 新版 81.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_destination` 2件

アドレスに依存する影響 `store_destination` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fde8",
      "incomplete_value": false,
      "site": "0058fde8",
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
            "const:51c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fac8",
      "incomplete_value": false,
      "site": "0058fac8",
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
            "const:55c:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fdf0",
      "incomplete_value": false,
      "site": "0058fdf0",
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
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fad0",
      "incomplete_value": false,
      "site": "0058fad0",
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
            "const:560:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fdf8",
      "incomplete_value": false,
      "site": "0058fdf8",
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
            "const:524:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fad8",
      "incomplete_value": false,
      "site": "0058fad8",
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
            "const:564:8"
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
      "0058fde8",
      "WRITE",
      [
        "storage",
        "00ca655c",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fdf0",
      "WRITE",
      [
        "storage",
        "00ca6560",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fdf8",
      "WRITE",
      [
        "storage",
        "00ca6564",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0058fde8",
      "WRITE",
      [
        "storage",
        "00ca751c",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fdf0",
      "WRITE",
      [
        "storage",
        "00ca7520",
        null,
        "undefined4"
      ]
    ],
    [
      "0058fdf8",
      "WRITE",
      [
        "storage",
        "00ca7524",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fa88.md#insn-0058fac8) · [`0058fad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fa88.md#insn-0058fad0) · [`0058fad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fa88.md#insn-0058fad8)
- 新版 [`0058fde8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fda8.md#insn-0058fde8) · [`0058fdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fda8.md#insn-0058fdf0) · [`0058fdf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fda8.md#insn-0058fdf8)

~~~diff
- 0058fac8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:55c:8"]]
- 0058fac8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4020:4"]]
+ 0058fde8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:51c:8"]]
+ 0058fde8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4020:4"]]
- 0058fac8 bytes 045d05b9
+ 0058fde8 bytes 041d05b9
- 0058fad0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
- 0058fad0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:4"]]
+ 0058fdf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:520:8"]]
+ 0058fdf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:4"]]
- 0058fad0 bytes 056105b9
+ 0058fdf0 bytes 052105b9
- 0058fad8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:564:8"]]
- 0058fad8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
+ 0058fdf8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:524:8"]]
+ 0058fdf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
- 0058fad8 bytes 006505b9
+ 0058fdf8 bytes 002505b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec5341602fdc7682305390afb0e2bac9"></a>

### [`0058fbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fbc0.md) → [`0058fee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fee0.md) FUN_0058fee0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0061a10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061a10c.md) [`008ab940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ab/008ab940.md) [`008ac9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ac/008ac9b4.md) [`008d94b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d94b8.md) · 呼出先 0件 
- 新版 呼出元 4件 [`0061a4bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0061a/0061a4bc.md) [`008ac8ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ac/008ac8ec.md) [`008ad960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ad/008ad960.md) [`008da464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008da464.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058fefc",
      "incomplete_value": false,
      "site": "0058fefc",
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
            "const:524:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fbdc",
      "incomplete_value": false,
      "site": "0058fbdc",
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
            "const:564:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058ff04",
      "incomplete_value": false,
      "site": "0058ff04",
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
            "const:528:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fbe4",
      "incomplete_value": false,
      "site": "0058fbe4",
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
            "const:568:8"
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
      "definition_site": "0058ff10",
      "incomplete_value": false,
      "site": "0058ff10",
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
            "const:52c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fbf0",
      "incomplete_value": false,
      "site": "0058fbf0",
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
            "const:56c:8"
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
      "0058fef0",
      "READ",
      [
        "storage",
        "00ca6610",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fefc",
      "WRITE",
      [
        "storage",
        "00ca6564",
        null,
        "undefined4"
      ]
    ],
    [
      "0058ff04",
      "WRITE",
      [
        "storage",
        "00ca6568",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0058fef0",
      "READ",
      [
        "storage",
        "00ca75d0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058fefc",
      "WRITE",
      [
        "storage",
        "00ca7524",
        null,
        "undefined4"
      ]
    ],
    [
      "0058ff04",
      "WRITE",
      [
        "storage",
        "00ca7528",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fbc0.md#insn-0058fbdc) · [`0058fbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fbc0.md#insn-0058fbe4) · [`0058fbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fbc0.md#insn-0058fbf0)
- 新版 [`0058fefc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fee0.md#insn-0058fefc) · [`0058ff04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fee0.md#insn-0058ff04) · [`0058ff10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fee0.md#insn-0058ff10)

~~~diff
- 0058fbdc ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:564:8"]]
- 0058fbdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 0058fefc ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:524:8"]]
+ 0058fefc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 0058fbdc bytes 886505b9
+ 0058fefc bytes 882505b9
- 0058fbe4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:568:8"]]
- 0058fbe4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 0058ff04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:528:8"]]
+ 0058ff04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 0058fbe4 bytes 096905b9
+ 0058ff04 bytes 092905b9
- 0058fbf0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:56c:8"]]
- 0058fbf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
+ 0058ff10 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:52c:8"]]
+ 0058ff10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
- 0058fbf0 bytes 4b6d05b9
+ 0058ff10 bytes 4b2d05b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28fad6f6ff78a4eac8769c2cd3441f6f"></a>

### [`0058fc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fc04.md) → [`0058ff24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058ff24.md) FUN_0058ff24

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00591b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591b74.md) [`00591c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591c00.md) [`00591cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591cbc.md) [`00591e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591e04.md) · 呼出先 0件 
- 新版 呼出元 4件 [`00591e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591e94.md) [`00591f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591f20.md) [`00591fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591fdc.md) [`00592124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592124.md) · 呼出先 0件 

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 38.71% / 新版 38.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 9件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058ff5c",
      "incomplete_value": false,
      "site": "0058ff5c",
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
                "const:5d8:8"
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
      "definition_site": "0058fc3c",
      "incomplete_value": false,
      "site": "0058fc3c",
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
                "const:618:8"
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
      "definition_site": "0058ff60",
      "incomplete_value": false,
      "site": "0058ff60",
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
                "const:5d8:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fc40",
      "incomplete_value": false,
      "site": "0058fc40",
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
                "const:618:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:18:8"
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
      "definition_site": "0058ff60",
      "incomplete_value": false,
      "site": "0058ff60",
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
                "const:18:8"
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
      "definition_site": "0058fc40",
      "incomplete_value": false,
      "site": "0058fc40",
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
                "const:18:8"
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
      "0058ff34",
      "READ",
      [
        "storage",
        "00ca6608",
        null,
        "undefined1"
      ]
    ],
    [
      "0058ff48",
      "READ",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ff48",
      "READ",
      [
        "storage",
        "00ca65c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058ff34",
      "READ",
      [
        "storage",
        "00ca75c8",
        null,
        "undefined1"
      ]
    ],
    [
      "0058ff48",
      "READ",
      [
        "storage",
        "00ca7580",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ff48",
      "READ",
      [
        "storage",
        "00ca7588",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fc6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fc04.md#insn-0058fc6c) · [`0058fc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fc04.md#insn-0058fc70) · [`0058fc10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fc04.md#insn-0058fc10)
- 新版 [`0058ff8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058ff24.md#insn-0058ff8c) · [`0058ff90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058ff24.md#insn-0058ff90) · [`0058ff30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058ff24.md#insn-0058ff30)

~~~diff
- 0058fc6c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058fc6c ["INT_ADD", "register:40f0:8", ["const:58fc6c:8", "const:4:8"]]
- 0058fc6c ["CALLIND", null, ["register:0:8"]]
+ 0058ff8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058ff8c ["INT_ADD", "register:40f0:8", ["const:58ff8c:8", "const:4:8"]]
+ 0058ff8c ["CALLIND", null, ["register:0:8"]]
- 0058fc6c bytes 00013fd6
+ 0058ff8c bytes 00013fd6
- 0058fc70 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0058fc70 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0058fc70 ["INT_ADD", "tmp:2:8", ["register:4098:8", "const:608:8"]]
- 0058fc70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0058ff90 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0058ff90 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0058ff90 ["INT_ADD", "tmp:2:8", ["register:4098:8", "const:5c8:8"]]
+ 0058ff90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0058fc70 bytes 7f221839
+ 0058ff90 bytes 7f221739
- 0058fc10 ["COPY", "register:4098:8", ["const:ca6000:8"]]
+ 0058ff30 ["COPY", "register:4098:8", ["const:ca7000:8"]]
- 0058fc10 bytes b33800f0
+ 0058ff30 bytes d3380090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f95547c0e2f0e1e071ea3f9297d0cc0a"></a>

### [`0058fd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fd14.md) → [`00590034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590034.md) FUN_00590034

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0055d628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d628.md) [`0055d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md) [`0055d9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d9dc.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`0055d948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055d/0055d948.md) [`0055db20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055d/0055db20.md) [`0055dcfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055d/0055dcfc.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_value, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 44.00% / 新版 44.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058fd98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058fd9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0058fda0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00590038",
      "READ",
      [
        "storage",
        "00ca6600",
        null,
        "undefined8"
      ]
    ],
    [
      "0059004c",
      "READ",
      [
        "storage",
        "00ca65f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:0058fd4c",
      "READ",
      [
        "storage",
        "00ca65e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00590038",
      "READ",
      [
        "storage",
        "00ca75c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0059004c",
      "READ",
      [
        "storage",
        "00ca75b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0059006c",
      "READ",
      [
        "storage",
        "00ca75a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fd80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fd14.md#insn-0058fd80) · [`0058fd98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fd14.md#insn-0058fd98) · [`0058fd9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fd14.md#insn-0058fd9c)

~~~diff
- 0058fd80 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0058fd80 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 0058fd80 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 0058fd80 ["COPY", "tmp:1:8", ["register:4080:8"]]
- 0058fd80 bytes eb03909a
- 0058fd98 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:20:8"]]
- 0058fd98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4060:8"]]
- 0058fd98 bytes 4c1100f9
- 0058fd9c ["INT_ADD", "tmp:0:8", ["register:4070:8", "const:10:8"]]
- 0058fd9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4078:8"]]
- 0058fd9c bytes cf0900f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed920668ec98bab9fda5c66c28f41875"></a>

### [`0058fddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fddc.md) → [`005900fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/005900fc.md) FUN_005900fc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0055d628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d628.md) [`0055d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md) [`0055d9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d9dc.md) · 呼出先 1件 [`005903f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/005903f8.md)
- 新版 呼出元 3件 [`0055d948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055d/0055d948.md) [`0055db20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055d/0055db20.md) [`0055dcfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055d/0055dcfc.md) · 呼出先 1件 [`00590718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590718.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00590194",
      "incomplete_value": true,
      "site": "0059019c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058fe74",
      "incomplete_value": true,
      "site": "0058fe7c",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00590198",
      "incomplete_value": true,
      "site": "005901a0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:580:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fe78",
      "incomplete_value": true,
      "site": "0058fe80",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:5c0:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005901b0",
      "incomplete_value": false,
      "site": "005901b0",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058fe90",
      "incomplete_value": false,
      "site": "0058fe90",
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
            "const:600:8"
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
      "00590114",
      "READ",
      [
        "storage",
        "00ca65e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00590134",
      "READ",
      [
        "storage",
        "00ca65f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00590134",
      "READ",
      [
        "storage",
        "00ca6600",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00590114",
      "READ",
      [
        "storage",
        "00ca75a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00590134",
      "READ",
      [
        "storage",
        "00ca75b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00590134",
      "READ",
      [
        "storage",
        "00ca75c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058fe34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fddc.md#insn-0058fe34) · [`0058fe90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fddc.md#insn-0058fe90) · [`0058fde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fddc.md#insn-0058fde8)
- 新版 [`00590154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/005900fc.md#insn-00590154) · [`005901b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/005900fc.md#insn-005901b0) · [`00590108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/005900fc.md#insn-00590108)

~~~diff
- 0058fe34 ["INT_ADD", "register:40f0:8", ["const:58fe34:8", "const:4:8"]]
- 0058fe34 ["CALL", null, ["callee:00590718:8"]]
+ 00590154 ["INT_ADD", "register:40f0:8", ["const:590154:8", "const:4:8"]]
+ 00590154 ["CALL", null, ["callee:00590718:8"]]
- 0058fe34 bytes 71010094
+ 00590154 bytes 71010094
- 0058fe90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:600:8"]]
- 0058fe90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 005901b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5c0:8"]]
+ 005901b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0058fe90 bytes 090103f9
+ 005901b0 bytes 09e102f9
- 0058fde8 ["COPY", "register:4048:8", ["const:ca6000:8"]]
+ 00590108 ["COPY", "register:4048:8", ["const:ca7000:8"]]
- 0058fde8 bytes a93800f0
+ 00590108 bytes a93800f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bb03879ad91d9fe7ce8c07ddc44958e"></a>

### [`0058fea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fea0.md) → [`005901c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/005901c0.md) FUN_005901c0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0055d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md) · 呼出先 1件 [`00c58460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58460.md)
- 新版 呼出元 1件 [`0055db20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055d/0055db20.md) · 呼出先 1件 [`00c59430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59430.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590228",
      "incomplete_value": false,
      "site": "00590228",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ff08",
      "incomplete_value": false,
      "site": "0058ff08",
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
            "const:608:8"
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
      "005901e0",
      "READ",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ],
    [
      "005901f4",
      "READ",
      [
        "storage",
        "00ca65c8",
        null,
        "undefined8"
      ]
    ],
    [
      "005901f4",
      "READ",
      [
        "storage",
        "00ca65cc",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005901e0",
      "READ",
      [
        "storage",
        "00ca7580",
        null,
        "undefined8"
      ]
    ],
    [
      "005901f4",
      "READ",
      [
        "storage",
        "00ca7588",
        null,
        "undefined8"
      ]
    ],
    [
      "005901f4",
      "READ",
      [
        "storage",
        "00ca758c",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ff08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fea0.md#insn-0058ff08) · [`0058feb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fea0.md#insn-0058feb4) · [`0058feb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fea0.md#insn-0058feb8)
- 新版 [`00590228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/005901c0.md#insn-00590228) · [`005901d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/005901c0.md#insn-005901d4) · [`005901d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/005901c0.md#insn-005901d8)

~~~diff
- 0058ff08 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0058ff08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:608:8"]]
- 0058ff08 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00590228 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00590228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:5c8:8"]]
+ 00590228 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0058ff08 bytes 09211839
+ 00590228 bytes 09211739
- 0058feb4 ["COPY", "register:4098:8", ["const:ca6000:8"]]
+ 005901d4 ["COPY", "register:4098:8", ["const:ca7000:8"]]
- 0058feb4 bytes b33800f0
+ 005901d4 bytes b33800f0
- 0058feb8 ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 0058feb8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0058feb8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0058feb8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005901d8 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 005901d8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005901d8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005901d8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0058feb8 bytes 73021791
+ 005901d8 bytes 73021691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a493db4950acf28329fd164cbe882839"></a>

### [`0058ff20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff20.md) → [`00590240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590240.md) FUN_00590240

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0055a6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a6e8.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0055aa08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055a/0055aa08.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 62.50% / 新版 62.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590250",
      "incomplete_value": false,
      "site": "00590250",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ff30",
      "incomplete_value": false,
      "site": "0058ff30",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590258",
      "incomplete_value": true,
      "site": "00590258",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ff38",
      "incomplete_value": true,
      "site": "0058ff38",
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
            "const:5c0:8"
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
      "0059024c",
      "READ",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00590250",
      "WRITE",
      [
        "storage",
        "00ca6608",
        null,
        "undefined1"
      ]
    ],
    [
      "00590258",
      "WRITE",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0059024c",
      "READ",
      [
        "storage",
        "00ca7580",
        null,
        "undefined8"
      ]
    ],
    [
      "00590250",
      "WRITE",
      [
        "storage",
        "00ca75c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00590258",
      "WRITE",
      [
        "storage",
        "00ca7580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ff30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff20.md#insn-0058ff30) · [`0058ff38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff20.md#insn-0058ff38) · [`0058ff20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff20.md#insn-0058ff20)
- 新版 [`00590250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590240.md#insn-00590250) · [`00590258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590240.md#insn-00590258) · [`00590240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590240.md#insn-00590240)

~~~diff
- 0058ff30 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 0058ff30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:608:8"]]
- 0058ff30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00590250 ["COPY", "tmp:0:4", ["register:4050:4"]]
+ 00590250 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:5c8:8"]]
+ 00590250 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0058ff30 bytes 2a211839
+ 00590250 bytes 2a211739
- 0058ff38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5c0:8"]]
- 0058ff38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 00590258 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:580:8"]]
+ 00590258 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0058ff38 bytes 0071813d
+ 00590258 bytes 0061813d
- 0058ff20 ["COPY", "register:4040:8", ["const:ca6000:8"]]
+ 00590240 ["COPY", "register:4040:8", ["const:ca7000:8"]]
- 0058ff20 bytes a83800f0
+ 00590240 bytes a83800f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4df0dc2c6b0910d75e77b4bd45f9949f"></a>

### [`0058ff40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff40.md) → [`00590260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590260.md) FUN_00590260

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0055a6ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a6ec.md) [`0055d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md) · 呼出先 0件 
- 新版 呼出元 2件 [`0055aa0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055a/0055aa0c.md) [`0055db20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055d/0055db20.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590274",
      "incomplete_value": true,
      "site": "00590274",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ff54",
      "incomplete_value": true,
      "site": "0058ff54",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590280",
      "incomplete_value": true,
      "site": "00590280",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ff60",
      "incomplete_value": true,
      "site": "0058ff60",
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
            "const:5c0:8"
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
      "00590270",
      "READ",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00590274",
      "WRITE",
      [
        "storage",
        "00ca6608",
        null,
        "undefined1"
      ]
    ],
    [
      "00590280",
      "WRITE",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00590270",
      "READ",
      [
        "storage",
        "00ca7580",
        null,
        "undefined8"
      ]
    ],
    [
      "00590274",
      "WRITE",
      [
        "storage",
        "00ca75c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00590280",
      "WRITE",
      [
        "storage",
        "00ca7580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ff54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff40.md#insn-0058ff54) · [`0058ff60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff40.md#insn-0058ff60) · [`0058ff40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff40.md#insn-0058ff40)
- 新版 [`00590274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590260.md#insn-00590274) · [`00590280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590260.md#insn-00590280) · [`00590260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590260.md#insn-00590260)

~~~diff
- 0058ff54 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 0058ff54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:608:8"]]
- 0058ff54 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00590274 ["COPY", "tmp:0:4", ["register:4050:4"]]
+ 00590274 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:5c8:8"]]
+ 00590274 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0058ff54 bytes 2a211839
+ 00590274 bytes 2a211739
- 0058ff60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5c0:8"]]
- 0058ff60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 00590280 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:580:8"]]
+ 00590280 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0058ff60 bytes 0071813d
+ 00590280 bytes 0061813d
- 0058ff40 ["COPY", "register:4040:8", ["const:ca6000:8"]]
+ 00590260 ["COPY", "register:4040:8", ["const:ca7000:8"]]
- 0058ff40 bytes a83800f0
+ 00590260 bytes a83800f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43a4babcbe2b843e9036eeec316ed21e"></a>

### [`0058ff68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff68.md) → [`00590288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590288.md) FUN_00590288

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0055a6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a6f0.md) [`0055d628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d628.md) [`0055d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md) · 呼出先 0件 
- 新版 呼出元 3件 [`0055aa10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055a/0055aa10.md) [`0055d948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055d/0055d948.md) [`0055db20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055d/0055db20.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 58.33% / 新版 58.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0059029c",
      "incomplete_value": false,
      "site": "0059029c",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ff7c",
      "incomplete_value": false,
      "site": "0058ff7c",
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
            "const:608:8"
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
      "00590294",
      "READ",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00590294",
      "READ",
      [
        "storage",
        "00ca65c8",
        null,
        "undefined8"
      ]
    ],
    [
      "0059029c",
      "WRITE",
      [
        "storage",
        "00ca6608",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00590294",
      "READ",
      [
        "storage",
        "00ca7580",
        null,
        "undefined8"
      ]
    ],
    [
      "00590294",
      "READ",
      [
        "storage",
        "00ca7588",
        null,
        "undefined8"
      ]
    ],
    [
      "0059029c",
      "WRITE",
      [
        "storage",
        "00ca75c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ff7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff68.md#insn-0058ff7c) · [`0058ff68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff68.md#insn-0058ff68) · [`0058ff6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ff68.md#insn-0058ff6c)
- 新版 [`0059029c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590288.md#insn-0059029c) · [`0059028c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590288.md#insn-0059028c)

~~~diff
- 0058ff7c ["COPY", "tmp:0:4", ["register:4050:4"]]
- 0058ff7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:608:8"]]
- 0058ff7c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0059029c ["COPY", "tmp:0:4", ["register:4050:4"]]
+ 0059029c ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:5c8:8"]]
+ 0059029c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0058ff7c bytes 2a211839
+ 0059029c bytes 2a211739
- 0058ff68 ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 0058ff68 bytes a83800f0
- 0058ff6c ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 0058ff6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058ff6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058ff6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059028c ["COPY", "tmp:0:8", ["const:580:8"]]
+ 0059028c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059028c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059028c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058ff6c bytes 08011791
+ 0059028c bytes 08011691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-620dada3cdd473de2cba419c30b697d9"></a>

### [`0058ffe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ffe8.md) → [`00590308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590308.md) FUN_00590308

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`00468200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468200.md) [`005554b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005554b8.md) [`00555cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/00555cd4.md) [`005599a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00559/005599a4.md) [`0055a478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a478.md) · 呼出先 0件 
- 新版 呼出元 5件 [`00468520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468520.md) [`005557d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/005557d8.md) [`00555ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/00555ff4.md) [`00559cc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00559/00559cc4.md) [`0055a798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055a/0055a798.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 65.91% / 新版 65.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 5件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590350",
      "incomplete_value": false,
      "site": "00590350",
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
                "const:5d8:8"
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
      "definition_site": "00590030",
      "incomplete_value": false,
      "site": "00590030",
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
                "const:618:8"
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
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590358",
      "incomplete_value": false,
      "site": "00590358",
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
                "const:5d8:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590038",
      "incomplete_value": false,
      "site": "00590038",
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
                "const:618:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590358",
      "incomplete_value": false,
      "site": "00590358",
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
                "const:18:8"
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
      "definition_site": "00590038",
      "incomplete_value": false,
      "site": "00590038",
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
                "const:18:8"
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
      "00590328",
      "READ",
      [
        "storage",
        "00ca6608",
        null,
        "undefined1"
      ]
    ],
    [
      "00590344",
      "PARAM",
      [
        "storage",
        "00ca6618",
        null,
        "undefined8"
      ]
    ],
    [
      "00590348",
      "READ",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00590328",
      "READ",
      [
        "storage",
        "00ca75c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00590344",
      "PARAM",
      [
        "storage",
        "00ca75d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00590348",
      "READ",
      [
        "storage",
        "00ca7580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ffe8.md#insn-00590068) · [`0058fffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ffe8.md#insn-0058fffc) · [`00590008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058ffe8.md#insn-00590008)
- 新版 [`00590388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590308.md#insn-00590388) · [`0059031c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590308.md#insn-0059031c) · [`00590328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590308.md#insn-00590328)

~~~diff
- 00590068 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00590068 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00590068 ["INT_ADD", "tmp:2:8", ["register:40b0:8", "const:608:8"]]
- 00590068 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00590388 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00590388 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00590388 ["INT_ADD", "tmp:2:8", ["register:40b0:8", "const:5c8:8"]]
+ 00590388 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00590068 bytes df221839
+ 00590388 bytes df221739
- 0058fffc ["COPY", "register:40b0:8", ["const:ca6000:8"]]
+ 0059031c ["COPY", "register:40b0:8", ["const:ca7000:8"]]
- 0058fffc bytes b63800f0
+ 0059031c bytes b63800f0
- 00590008 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:608:8"]]
- 00590008 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00590008 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00590328 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:5c8:8"]]
+ 00590328 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00590328 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00590008 bytes c8225839
+ 00590328 bytes c8225739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5a6356bfd41de1853fbbc035d07661a"></a>

### [`00590098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590098.md) → [`005903b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/005903b8.md) FUN_005903b8

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 13件 [`005514c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00551/005514c8.md) [`0055155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00551/0055155c.md) [`005515f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00551/005515f0.md) [`0055183c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00551/0055183c.md) [`005519ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00551/005519ac.md) · 呼出先 0件 
- 新版 呼出元 13件 [`005517e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00551/005517e8.md) [`0055187c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00551/0055187c.md) [`00551910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00551/00551910.md) [`00551b5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00551/00551b5c.md) [`00551ccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00551/00551ccc.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00590430",
      "incomplete_value": true,
      "site": "00590430",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590110",
      "incomplete_value": true,
      "site": "00590110",
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
            "const:608:8"
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
      "005903d4",
      "READ",
      [
        "storage",
        "00ca6608",
        null,
        "undefined1"
      ]
    ],
    [
      "005903ec",
      "PARAM",
      [
        "storage",
        "00ca6618",
        null,
        "undefined8"
      ]
    ],
    [
      "005903f0",
      "READ",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005903d4",
      "READ",
      [
        "storage",
        "00ca75c8",
        null,
        "undefined1"
      ]
    ],
    [
      "005903ec",
      "PARAM",
      [
        "storage",
        "00ca75d8",
        null,
        "undefined8"
      ]
    ],
    [
      "005903f0",
      "READ",
      [
        "storage",
        "00ca7580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590098.md#insn-00590110) · [`005900a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590098.md#insn-005900a8) · [`005900b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590098.md#insn-005900b4)
- 新版 [`00590430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/005903b8.md#insn-00590430) · [`005903c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/005903b8.md#insn-005903c8) · [`005903d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/005903b8.md#insn-005903d4)

~~~diff
- 00590110 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00590110 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00590110 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:608:8"]]
- 00590110 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00590430 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00590430 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00590430 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5c8:8"]]
+ 00590430 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00590110 bytes bf221839
+ 00590430 bytes bf221739
- 005900a8 ["COPY", "register:40a8:8", ["const:ca6000:8"]]
+ 005903c8 ["COPY", "register:40a8:8", ["const:ca7000:8"]]
- 005900a8 bytes b53800d0
+ 005903c8 bytes b53800f0
- 005900b4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:608:8"]]
- 005900b4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 005900b4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 005903d4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5c8:8"]]
+ 005903d4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 005903d4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 005900b4 bytes a8225839
+ 005903d4 bytes a8225739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fb9898660ae6eaaeadcb529a8807ca2"></a>

### [`00590138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590138.md) → [`00590458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590458.md) FUN_00590458

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0055d628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d628.md) [`0055d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md) [`0055d9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d9dc.md) · 呼出先 0件 
- 新版 呼出元 3件 [`0055d948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055d/0055d948.md) [`0055db20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055d/0055db20.md) [`0055dcfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055d/0055dcfc.md) · 呼出先 0件 

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 62.90% / 新版 62.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005904e4",
      "incomplete_value": true,
      "site": "005904e4",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005901c4",
      "incomplete_value": true,
      "site": "005901c4",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005904fc",
      "incomplete_value": true,
      "site": "005904fc",
      "value": [
        "LOAD",
        "8",
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
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005901dc",
      "incomplete_value": true,
      "site": "005901dc",
      "value": [
        "LOAD",
        "8",
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
                "const:48:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005904e8",
      "incomplete_value": true,
      "site": "005904fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:5d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005901c8",
      "incomplete_value": true,
      "site": "005901dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:610:8"
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
      "0059047c",
      "READ",
      [
        "storage",
        "00ca6608",
        null,
        "undefined1"
      ]
    ],
    [
      "005904a0",
      "PARAM",
      [
        "storage",
        "00ca6618",
        null,
        "undefined8"
      ]
    ],
    [
      "005904a4",
      "READ",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0059047c",
      "READ",
      [
        "storage",
        "00ca75c8",
        null,
        "undefined1"
      ]
    ],
    [
      "005904a0",
      "PARAM",
      [
        "storage",
        "00ca75d8",
        null,
        "undefined8"
      ]
    ],
    [
      "005904a4",
      "READ",
      [
        "storage",
        "00ca7580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005901c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590138.md#insn-005901c4) · [`005901dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590138.md#insn-005901dc) · [`00590200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590138.md#insn-00590200)
- 新版 [`005904e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590458.md#insn-005904e4) · [`005904fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590458.md#insn-005904fc) · [`00590520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590458.md#insn-00590520)

~~~diff
- 005901c4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 005901c4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 005901c4 ["INT_ADD", "tmp:2:8", ["register:40c8:8", "const:608:8"]]
- 005901c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 005904e4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 005904e4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 005904e4 ["INT_ADD", "tmp:2:8", ["register:40c8:8", "const:5c8:8"]]
+ 005904e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 005901c4 bytes 3f231839
+ 005904e4 bytes 3f231739
- 005901dc ["COPY", "register:0:8", ["register:4040:8"]]
- 005901dc ["INT_ADD", "register:40f0:8", ["const:5901dc:8", "const:4:8"]]
- 005901dc ["CALLIND", null, ["register:0:8"]]
+ 005904fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005904fc ["INT_ADD", "register:40f0:8", ["const:5904fc:8", "const:4:8"]]
+ 005904fc ["CALLIND", null, ["register:0:8"]]
- 005901dc bytes 00013fd6
+ 005904fc bytes 00013fd6
- 00590200 ["COPY", "register:0:8", ["register:4040:8"]]
- 00590200 ["INT_ADD", "register:40f0:8", ["const:590200:8", "const:4:8"]]
- 00590200 ["CALLIND", null, ["register:0:8"]]
+ 00590520 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00590520 ["INT_ADD", "register:40f0:8", ["const:590520:8", "const:4:8"]]
+ 00590520 ["CALLIND", null, ["register:0:8"]]
- 00590200 bytes 00013fd6
+ 00590520 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7b76171205c086faf5381ce81ec1f84"></a>

### [`00590230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590230.md) → [`00590550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590550.md) FUN_00590550

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0055d628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d628.md) [`0055d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d800.md) [`0055d9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055d/0055d9dc.md) · 呼出先 0件 
- 新版 呼出元 3件 [`0055d948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055d/0055d948.md) [`0055db20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055d/0055db20.md) [`0055dcfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055d/0055dcfc.md) · 呼出先 0件 

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 55.77% / 新版 55.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 9件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005905a8",
      "incomplete_value": false,
      "site": "005905a8",
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
                "const:5d8:8"
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
      "definition_site": "00590288",
      "incomplete_value": false,
      "site": "00590288",
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
                "const:618:8"
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
      "definition_site": "005905b0",
      "incomplete_value": false,
      "site": "005905b0",
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
                "const:5d8:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590290",
      "incomplete_value": false,
      "site": "00590290",
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
                "const:618:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:18:8"
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
      "definition_site": "005905b0",
      "incomplete_value": false,
      "site": "005905b0",
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
                "const:18:8"
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
      "definition_site": "00590290",
      "incomplete_value": false,
      "site": "00590290",
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
                "const:18:8"
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
      "00590574",
      "READ",
      [
        "storage",
        "00ca6608",
        null,
        "undefined1"
      ]
    ],
    [
      "0059059c",
      "PARAM",
      [
        "storage",
        "00ca6618",
        null,
        "undefined8"
      ]
    ],
    [
      "005905a0",
      "READ",
      [
        "storage",
        "00ca65c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00590574",
      "READ",
      [
        "storage",
        "00ca75c8",
        null,
        "undefined1"
      ]
    ],
    [
      "0059059c",
      "PARAM",
      [
        "storage",
        "00ca75d8",
        null,
        "undefined8"
      ]
    ],
    [
      "005905a0",
      "READ",
      [
        "storage",
        "00ca7580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005902bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590230.md#insn-005902bc) · [`005902c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590230.md#insn-005902c0) · [`00590248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590230.md#insn-00590248)
- 新版 [`005905dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590550.md#insn-005905dc) · [`005905e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590550.md#insn-005905e0) · [`00590568`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00590/00590550.md#insn-00590568)

~~~diff
- 005902bc ["COPY", "register:0:8", ["register:4040:8"]]
- 005902bc ["INT_ADD", "register:40f0:8", ["const:5902bc:8", "const:4:8"]]
- 005902bc ["CALLIND", null, ["register:0:8"]]
+ 005905dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005905dc ["INT_ADD", "register:40f0:8", ["const:5905dc:8", "const:4:8"]]
+ 005905dc ["CALLIND", null, ["register:0:8"]]
- 005902bc bytes 00013fd6
+ 005905dc bytes 00013fd6
- 005902c0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 005902c0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 005902c0 ["INT_ADD", "tmp:2:8", ["register:40c8:8", "const:608:8"]]
- 005902c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 005905e0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 005905e0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 005905e0 ["INT_ADD", "tmp:2:8", ["register:40c8:8", "const:5c8:8"]]
+ 005905e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 005902c0 bytes 3f231839
+ 005905e0 bytes 3f231739
- 00590248 ["COPY", "register:40c8:8", ["const:ca6000:8"]]
+ 00590568 ["COPY", "register:40c8:8", ["const:ca7000:8"]]
- 00590248 bytes b93800d0
+ 00590568 bytes b93800f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b95de3ef0830ba24864cc53b3c1da04"></a>

### [`00590df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590df8.md) → [`00591118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591118.md) FUN_00591118

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005923f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005923f0.md) · 呼出先 17件 [`00550c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c44.md) [`005552b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552b4.md) [`0059129c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059129c.md) [`005925b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005925b8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 1件 [`00592710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592710.md) · 呼出先 17件 [`00550f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550f64.md) [`005555d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/005555d4.md) [`005915bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/005915bc.md) [`005928d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/005928d8.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.02% / 新版 94.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00591144",
      "incomplete_value": false,
      "site": "00591150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590e24",
      "incomplete_value": false,
      "site": "00590e30",
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
            "const:e0:8"
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
      "definition_site": "00591184",
      "incomplete_value": true,
      "site": "00591184",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:222:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590e64",
      "incomplete_value": true,
      "site": "00590e64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e2:8"
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
      "definition_site": "005911c4",
      "incomplete_value": true,
      "site": "005911c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e09:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00590ea4",
      "incomplete_value": true,
      "site": "00590ea4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d2b:8"
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
      "00591150",
      "DATA",
      [
        "storage",
        "00c6d0e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00591174",
      "READ",
      [
        "storage",
        "002a01e2",
        null,
        "string"
      ]
    ],
    [
      "005911b4",
      "READ",
      [
        "storage",
        "002b3d2b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00591150",
      "DATA",
      [
        "storage",
        "00c6e0b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00591174",
      "READ",
      [
        "storage",
        "002a0222",
        null,
        "string"
      ]
    ],
    [
      "005911b4",
      "READ",
      [
        "storage",
        "002b3e09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00590f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590df8.md#insn-00590f28) · [`00590fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590df8.md#insn-00590fbc) · [`00590fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590df8.md#insn-00590fec)
- 新版 [`00591248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591118.md#insn-00591248) · [`005912dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591118.md#insn-005912dc) · [`0059130c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591118.md#insn-0059130c)

~~~diff
- 00590f28 ["INT_ADD", "register:40f0:8", ["const:590f28:8", "const:4:8"]]
- 00590f28 ["CALL", null, ["callee:00c596b0:8"]]
+ 00591248 ["INT_ADD", "register:40f0:8", ["const:591248:8", "const:4:8"]]
+ 00591248 ["CALL", null, ["callee:00c596b0:8"]]
- 00590f28 bytes ee1d1b94
+ 00591248 bytes 1a211b94
- 00590fbc ["INT_ADD", "register:40f0:8", ["const:590fbc:8", "const:4:8"]]
- 00590fbc ["CALL", null, ["callee:005928d8:8"]]
+ 005912dc ["INT_ADD", "register:40f0:8", ["const:5912dc:8", "const:4:8"]]
+ 005912dc ["CALL", null, ["callee:005928d8:8"]]
- 00590fbc bytes 7f050094
+ 005912dc bytes 7f050094
- 00590fec ["INT_ADD", "register:40f0:8", ["const:590fec:8", "const:4:8"]]
- 00590fec ["CALL", null, ["callee:005928d8:8"]]
+ 0059130c ["INT_ADD", "register:40f0:8", ["const:59130c:8", "const:4:8"]]
+ 0059130c ["CALL", null, ["callee:005928d8:8"]]
- 00590fec bytes 73050094
+ 0059130c bytes 73050094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcb8c60a023811841c90dd216338acd7"></a>

### [`005912f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005912f8.md) → [`00591618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591618.md) FUN_00591618

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a440.md)
- 新版 呼出元 0件  · 呼出先 6件 [`005555e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/005555e8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b400.md) [`00c5b410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b410.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.73% / 新版 88.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005916e4",
      "incomplete_value": false,
      "site": "005916e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005913c4",
      "incomplete_value": false,
      "site": "005913c4",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005916fc",
      "incomplete_value": true,
      "site": "00591704",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005913dc",
      "incomplete_value": true,
      "site": "005913e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:750:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591674",
      "incomplete_value": true,
      "site": "00591678",
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
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591354",
      "incomplete_value": true,
      "site": "00591358",
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
              "LOAD"
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
      "00591670",
      "READ",
      [
        "storage",
        "00c9b350",
        null,
        "pointer"
      ]
    ],
    [
      "00591674",
      "READ",
      [
        "storage",
        "00ca3f14",
        null,
        "undefined4"
      ]
    ],
    [
      "0059167c",
      "READ",
      [
        "storage",
        "00ca3f18",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00591670",
      "READ",
      [
        "storage",
        "00c9c320",
        null,
        "pointer"
      ]
    ],
    [
      "00591674",
      "READ",
      [
        "storage",
        "00ca4ee4",
        null,
        "undefined4"
      ]
    ],
    [
      "0059167c",
      "READ",
      [
        "storage",
        "00ca4ee8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005912f8.md#insn-00591358) · [`00591334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005912f8.md#insn-00591334) · [`00591340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005912f8.md#insn-00591340)
- 新版 [`00591678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591618.md#insn-00591678) · [`00591654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591618.md#insn-00591654) · [`00591660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591618.md#insn-00591660)

~~~diff
- 00591358 ["INT_ADD", "register:40f0:8", ["const:591358:8", "const:4:8"]]
- 00591358 ["CALL", null, ["callee:00c5b420:8"]]
+ 00591678 ["INT_ADD", "register:40f0:8", ["const:591678:8", "const:4:8"]]
+ 00591678 ["CALL", null, ["callee:00c5b420:8"]]
- 00591358 bytes 3e241b94
+ 00591678 bytes 6a271b94
- 00591334 ["INT_ADD", "register:40f0:8", ["const:591334:8", "const:4:8"]]
- 00591334 ["CALL", null, ["callee:00c5b400:8"]]
+ 00591654 ["INT_ADD", "register:40f0:8", ["const:591654:8", "const:4:8"]]
+ 00591654 ["CALL", null, ["callee:00c5b400:8"]]
- 00591334 bytes 3f241b94
+ 00591654 bytes 6b271b94
- 00591340 ["INT_ADD", "register:40f0:8", ["const:591340:8", "const:4:8"]]
- 00591340 ["CALL", null, ["callee:00c5b410:8"]]
+ 00591660 ["INT_ADD", "register:40f0:8", ["const:591660:8", "const:4:8"]]
+ 00591660 ["CALL", null, ["callee:00c5b410:8"]]
- 00591340 bytes 40241b94
+ 00591660 bytes 6c271b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fb980419e14484909a1d157363a24c3"></a>

### [`00591440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591440.md) → [`00591760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591760.md) FUN_00591760

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a440.md)
- 新版 呼出元 0件  · 呼出先 10件 [`005555e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/005555e8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b400.md) [`00c5b410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b410.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.35% / 新版 84.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059183c",
      "incomplete_value": false,
      "site": "00591844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059151c",
      "incomplete_value": false,
      "site": "00591524",
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
            "const:2b0:8"
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
      "definition_site": "0059185c",
      "incomplete_value": false,
      "site": "0059185c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059153c",
      "incomplete_value": false,
      "site": "0059153c",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00591874",
      "incomplete_value": true,
      "site": "00591878",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591554",
      "incomplete_value": true,
      "site": "00591558",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:750:8"
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
      "005917c0",
      "READ",
      [
        "storage",
        "00c9b350",
        null,
        "pointer"
      ]
    ],
    [
      "005917c4",
      "READ",
      [
        "storage",
        "00ca3f14",
        null,
        "undefined4"
      ]
    ],
    [
      "005917cc",
      "READ",
      [
        "storage",
        "00ca3f18",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "005917c0",
      "READ",
      [
        "storage",
        "00c9c320",
        null,
        "pointer"
      ]
    ],
    [
      "005917c4",
      "READ",
      [
        "storage",
        "00ca4ee4",
        null,
        "undefined4"
      ]
    ],
    [
      "005917cc",
      "READ",
      [
        "storage",
        "00ca4ee8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005914a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591440.md#insn-005914a8) · [`00591484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591440.md#insn-00591484) · [`00591490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591440.md#insn-00591490)
- 新版 [`005917c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591760.md#insn-005917c8) · [`005917a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591760.md#insn-005917a4) · [`005917b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591760.md#insn-005917b0)

~~~diff
- 005914a8 ["INT_ADD", "register:40f0:8", ["const:5914a8:8", "const:4:8"]]
- 005914a8 ["CALL", null, ["callee:00c5b420:8"]]
+ 005917c8 ["INT_ADD", "register:40f0:8", ["const:5917c8:8", "const:4:8"]]
+ 005917c8 ["CALL", null, ["callee:00c5b420:8"]]
- 005914a8 bytes ea231b94
+ 005917c8 bytes 16271b94
- 00591484 ["INT_ADD", "register:40f0:8", ["const:591484:8", "const:4:8"]]
- 00591484 ["CALL", null, ["callee:00c5b400:8"]]
+ 005917a4 ["INT_ADD", "register:40f0:8", ["const:5917a4:8", "const:4:8"]]
+ 005917a4 ["CALL", null, ["callee:00c5b400:8"]]
- 00591484 bytes eb231b94
+ 005917a4 bytes 17271b94
- 00591490 ["INT_ADD", "register:40f0:8", ["const:591490:8", "const:4:8"]]
- 00591490 ["CALL", null, ["callee:00c5b410:8"]]
+ 005917b0 ["INT_ADD", "register:40f0:8", ["const:5917b0:8", "const:4:8"]]
+ 005917b0 ["CALL", null, ["callee:00c5b410:8"]]
- 00591490 bytes ec231b94
+ 005917b0 bytes 18271b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53afb3b1461f3dc48ff70b3f9ae028be"></a>

### [`0059163c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059163c.md) → [`0059195c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/0059195c.md) FUN_0059195c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a4d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`005555e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/005555e8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b4a0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.93% / 新版 82.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005919a0",
      "incomplete_value": false,
      "site": "005919a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591680",
      "incomplete_value": false,
      "site": "00591688",
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
            "const:420:8"
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
      "definition_site": "005919c0",
      "incomplete_value": false,
      "site": "005919c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005916a0",
      "incomplete_value": false,
      "site": "005916a0",
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
            "const:470:8"
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
      "005919a8",
      "DATA",
      [
        "storage",
        "00c6d420",
        null,
        "undefined *"
      ]
    ],
    [
      "005919c0",
      "DATA",
      [
        "storage",
        "00c6d470",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005919a8",
      "DATA",
      [
        "storage",
        "00c6e3f0",
        null,
        "undefined *"
      ]
    ],
    [
      "005919c0",
      "DATA",
      [
        "storage",
        "00c6e440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059163c.md#insn-00591670) · [`00591678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059163c.md#insn-00591678) · [`0059167c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059163c.md#insn-0059167c)
- 新版 [`00591990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/0059195c.md#insn-00591990) · [`00591998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/0059195c.md#insn-00591998) · [`0059199c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/0059195c.md#insn-0059199c)

~~~diff
- 00591670 ["INT_ADD", "register:40f0:8", ["const:591670:8", "const:4:8"]]
- 00591670 ["CALL", null, ["callee:00c5b4a0:8"]]
+ 00591990 ["INT_ADD", "register:40f0:8", ["const:591990:8", "const:4:8"]]
+ 00591990 ["CALL", null, ["callee:00c5b4a0:8"]]
- 00591670 bytes 98231b94
+ 00591990 bytes c4261b94
- 00591678 ["INT_ADD", "register:40f0:8", ["const:591678:8", "const:4:8"]]
- 00591678 ["CALL", null, ["callee:00c58f30:8"]]
+ 00591998 ["INT_ADD", "register:40f0:8", ["const:591998:8", "const:4:8"]]
+ 00591998 ["CALL", null, ["callee:00c58f30:8"]]
- 00591678 bytes 3a1a1b94
+ 00591998 bytes 661d1b94
- 0059167c ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059199c ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059167c bytes e8360090
+ 0059199c bytes e83600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a782a619fb36a6af04b8554c9b0fc30"></a>

### [`005917c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005917c8.md) → [`00591ae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591ae8.md) FUN_00591ae8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`005925b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005925b8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005928d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/005928d8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591b00",
      "incomplete_value": false,
      "site": "00591b0c",
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
            "const:f31:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005917e0",
      "incomplete_value": false,
      "site": "005917ec",
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
            "const:e53:8"
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
      "00591b00",
      "PARAM",
      [
        "storage",
        "002bee53",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00591b00",
      "PARAM",
      [
        "storage",
        "002bef31",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005917ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005917c8.md#insn-005917ec) · [`005917e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005917c8.md#insn-005917e0)
- 新版 [`00591b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591ae8.md#insn-00591b0c) · [`00591b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591ae8.md#insn-00591b00)

~~~diff
- 005917ec ["INT_ADD", "register:40f0:8", ["const:5917ec:8", "const:4:8"]]
- 005917ec ["CALL", null, ["callee:005928d8:8"]]
+ 00591b0c ["INT_ADD", "register:40f0:8", ["const:591b0c:8", "const:4:8"]]
+ 00591b0c ["CALL", null, ["callee:005928d8:8"]]
- 005917ec bytes 73030094
+ 00591b0c bytes 73030094
- 005917e0 ["COPY", "tmp:0:8", ["const:e53:8"]]
- 005917e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005917e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005917e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00591b00 ["COPY", "tmp:0:8", ["const:f31:8"]]
+ 00591b00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00591b00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00591b00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005917e0 bytes 214c3991
+ 00591b00 bytes 21c43c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f69fbd73ba64ad48e552cd49c375b039"></a>

### [`00591880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591880.md) → [`00591ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591ba0.md) FUN_00591ba0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`005925b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005925b8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005928d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/005928d8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591bb8",
      "incomplete_value": false,
      "site": "00591bc4",
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
            "const:355:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591898",
      "incomplete_value": false,
      "site": "005918a4",
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
            "const:28a:8"
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
      "00591bb8",
      "PARAM",
      [
        "storage",
        "002a328a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00591bb8",
      "PARAM",
      [
        "storage",
        "002a3355",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005918a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591880.md#insn-005918a4) · [`00591898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591880.md#insn-00591898)
- 新版 [`00591bc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591ba0.md#insn-00591bc4) · [`00591bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591ba0.md#insn-00591bb8)

~~~diff
- 005918a4 ["INT_ADD", "register:40f0:8", ["const:5918a4:8", "const:4:8"]]
- 005918a4 ["CALL", null, ["callee:005928d8:8"]]
+ 00591bc4 ["INT_ADD", "register:40f0:8", ["const:591bc4:8", "const:4:8"]]
+ 00591bc4 ["CALL", null, ["callee:005928d8:8"]]
- 005918a4 bytes 45030094
+ 00591bc4 bytes 45030094
- 00591898 ["COPY", "tmp:0:8", ["const:28a:8"]]
- 00591898 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00591898 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00591898 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00591bb8 ["COPY", "tmp:0:8", ["const:355:8"]]
+ 00591bb8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00591bb8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00591bb8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00591898 bytes 21280a91
+ 00591bb8 bytes 21540d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf201e31b99a137a1b4015e149e59b0b"></a>

### [`005918c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005918c8.md) → [`00591be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591be8.md) FUN_00591be8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`005925b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005925b8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005928d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/005928d8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591c00",
      "incomplete_value": false,
      "site": "00591c10",
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
            "const:9a5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005918e0",
      "incomplete_value": false,
      "site": "005918f0",
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
            "const:8d8:8"
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
      "00591c00",
      "PARAM",
      [
        "storage",
        "002ad8d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00591c00",
      "PARAM",
      [
        "storage",
        "002ad9a5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005918f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005918c8.md#insn-005918f0) · [`005918e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005918c8.md#insn-005918e0)
- 新版 [`00591c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591be8.md#insn-00591c10) · [`00591c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591be8.md#insn-00591c00)

~~~diff
- 005918f0 ["INT_ADD", "register:40f0:8", ["const:5918f0:8", "const:4:8"]]
- 005918f0 ["CALL", null, ["callee:005928d8:8"]]
+ 00591c10 ["INT_ADD", "register:40f0:8", ["const:591c10:8", "const:4:8"]]
+ 00591c10 ["CALL", null, ["callee:005928d8:8"]]
- 005918f0 bytes 32030094
+ 00591c10 bytes 32030094
- 005918e0 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 005918e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005918e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005918e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00591c00 ["COPY", "tmp:0:8", ["const:9a5:8"]]
+ 00591c00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00591c00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00591c00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005918e0 bytes 21602391
+ 00591c00 bytes 21942691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e128a89ac36c26347473d3ffb3f4956b"></a>

### [`005919f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005919f8.md) → [`00591d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591d18.md) FUN_00591d18

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md) [`00c5a540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a540.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c596b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596b0.md) [`00c5b510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b510.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00591d40",
      "incomplete_value": false,
      "site": "00591d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591a20",
      "incomplete_value": false,
      "site": "00591a30",
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
            "const:290:8"
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
      "definition_site": "00591d44",
      "incomplete_value": true,
      "site": "00591d50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:380:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591a24",
      "incomplete_value": true,
      "site": "00591a30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
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
      "00591d40",
      "PARAM",
      [
        "storage",
        "00c6d290",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591d44",
      "READ",
      [
        "storage",
        "00c9b3b0",
        null,
        "pointer"
      ]
    ],
    [
      "00591d44",
      "PARAM",
      [
        "storage",
        "00c6d5b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00591d40",
      "PARAM",
      [
        "storage",
        "00c6e260",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00591d44",
      "READ",
      [
        "storage",
        "00c9c380",
        null,
        "pointer"
      ]
    ],
    [
      "00591d44",
      "PARAM",
      [
        "storage",
        "00c6e580",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005919f8.md#insn-00591a30) · [`00591a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005919f8.md#insn-00591a14) · [`00591a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/005919f8.md#insn-00591a1c)
- 新版 [`00591d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591d18.md#insn-00591d50) · [`00591d34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591d18.md#insn-00591d34) · [`00591d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591d18.md#insn-00591d3c)

~~~diff
- 00591a30 ["INT_ADD", "register:40f0:8", ["const:591a30:8", "const:4:8"]]
- 00591a30 ["CALL", null, ["callee:00c596b0:8"]]
+ 00591d50 ["INT_ADD", "register:40f0:8", ["const:591d50:8", "const:4:8"]]
+ 00591d50 ["CALL", null, ["callee:00c596b0:8"]]
- 00591a30 bytes 2c1b1b94
+ 00591d50 bytes 581e1b94
- 00591a14 ["COPY", "register:4010:8", ["const:c9b000:8"]]
+ 00591d34 ["COPY", "register:4010:8", ["const:c9c000:8"]]
- 00591a14 bytes 423800d0
+ 00591d34 bytes 423800f0
- 00591a1c ["COPY", "register:4008:8", ["const:c6d000:8"]]
+ 00591d3c ["COPY", "register:4008:8", ["const:c6e000:8"]]
- 00591a1c bytes e1360090
+ 00591d3c bytes e13600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad5f056ba12f7ea5f3ec9400dd6c6cdf"></a>

### [`00591cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591cbc.md) → [`00591fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591fdc.md) FUN_00591fdc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0058fc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fc04.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md) [`00c5a440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a440.md) [`00c5a470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a470.md) [`00c5a5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a5a0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0058ff24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058ff24.md) [`00c596b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596b0.md) [`00c5b410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b410.md) [`00c5b440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b440.md) [`00c5b570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b570.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0059201c",
      "incomplete_value": true,
      "site": "00592028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591cfc",
      "incomplete_value": true,
      "site": "00591d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:200:8"
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
      "definition_site": "00592040",
      "incomplete_value": false,
      "site": "00592050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591d20",
      "incomplete_value": false,
      "site": "00591d30",
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
            "const:218:8"
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
      "definition_site": "00592048",
      "incomplete_value": false,
      "site": "00592050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591d28",
      "incomplete_value": false,
      "site": "00591d30",
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
            "const:228:8"
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
      "00592014",
      "PARAM",
      [
        "storage",
        "00c6d1f0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0059201c",
      "PARAM",
      [
        "storage",
        "00c6d200",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00592040",
      "PARAM",
      [
        "storage",
        "00c6d218",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00592014",
      "PARAM",
      [
        "storage",
        "00c6e1c0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0059201c",
      "PARAM",
      [
        "storage",
        "00c6e1d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00592040",
      "PARAM",
      [
        "storage",
        "00c6e1e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591cbc.md#insn-00591d08) · [`00591d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591cbc.md#insn-00591d30) · [`00591cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591cbc.md#insn-00591cf0)
- 新版 [`00592028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591fdc.md#insn-00592028) · [`00592050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591fdc.md#insn-00592050) · [`00592010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591fdc.md#insn-00592010)

~~~diff
- 00591d08 ["INT_ADD", "register:40f0:8", ["const:591d08:8", "const:4:8"]]
- 00591d08 ["CALL", null, ["callee:00c596b0:8"]]
+ 00592028 ["INT_ADD", "register:40f0:8", ["const:592028:8", "const:4:8"]]
+ 00592028 ["CALL", null, ["callee:00c596b0:8"]]
- 00591d08 bytes 761a1b94
+ 00592028 bytes a21d1b94
- 00591d30 ["INT_ADD", "register:40f0:8", ["const:591d30:8", "const:4:8"]]
- 00591d30 ["CALL", null, ["callee:00c596b0:8"]]
+ 00592050 ["INT_ADD", "register:40f0:8", ["const:592050:8", "const:4:8"]]
+ 00592050 ["CALL", null, ["callee:00c596b0:8"]]
- 00591d30 bytes 6c1a1b94
+ 00592050 bytes 981d1b94
- 00591cf0 ["COPY", "register:4008:8", ["const:c6d000:8"]]
+ 00592010 ["COPY", "register:4008:8", ["const:c6e000:8"]]
- 00591cf0 bytes e1360090
+ 00592010 bytes e1360090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8edc12b41b21288101e5e84d6c63b4a"></a>

### [`00591e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591e04.md) → [`00592124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592124.md) FUN_00592124

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0058fc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fc04.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md) [`00c5a440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a440.md) [`00c5a470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a470.md) [`00c5a5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a5a0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0058ff24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058ff24.md) [`00c596b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596b0.md) [`00c5b410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b410.md) [`00c5b440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b440.md) [`00c5b570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b570.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.50% / 新版 94.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00592194",
      "incomplete_value": false,
      "site": "0059219c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591e74",
      "incomplete_value": false,
      "site": "00591e7c",
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
            "const:228:8"
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
      "definition_site": "005921b0",
      "incomplete_value": false,
      "site": "005921c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591e90",
      "incomplete_value": false,
      "site": "00591ea0",
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
            "const:218:8"
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
      "definition_site": "005921b8",
      "incomplete_value": false,
      "site": "005921c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00591e98",
      "incomplete_value": false,
      "site": "00591ea0",
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
            "const:228:8"
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
      "00592164",
      "PARAM",
      [
        "storage",
        "00c6d1f0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0059216c",
      "PARAM",
      [
        "storage",
        "00c6d200",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0059218c",
      "PARAM",
      [
        "storage",
        "00c6d218",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00592164",
      "PARAM",
      [
        "storage",
        "00c6e1c0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0059216c",
      "PARAM",
      [
        "storage",
        "00c6e1d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0059218c",
      "PARAM",
      [
        "storage",
        "00c6e1e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00591e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591e04.md#insn-00591e7c) · [`00591ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591e04.md#insn-00591ea0) · [`00591e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/00591e04.md#insn-00591e40)
- 新版 [`0059219c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592124.md#insn-0059219c) · [`005921c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592124.md#insn-005921c0) · [`00592160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592124.md#insn-00592160)

~~~diff
- 00591e7c ["INT_ADD", "register:40f0:8", ["const:591e7c:8", "const:4:8"]]
- 00591e7c ["CALL", null, ["callee:00c596b0:8"]]
+ 0059219c ["INT_ADD", "register:40f0:8", ["const:59219c:8", "const:4:8"]]
+ 0059219c ["CALL", null, ["callee:00c596b0:8"]]
- 00591e7c bytes 191a1b94
+ 0059219c bytes 451d1b94
- 00591ea0 ["INT_ADD", "register:40f0:8", ["const:591ea0:8", "const:4:8"]]
- 00591ea0 ["CALL", null, ["callee:00c596b0:8"]]
+ 005921c0 ["INT_ADD", "register:40f0:8", ["const:5921c0:8", "const:4:8"]]
+ 005921c0 ["CALL", null, ["callee:00c596b0:8"]]
- 00591ea0 bytes 101a1b94
+ 005921c0 bytes 3c1d1b94
- 00591e40 ["COPY", "register:4008:8", ["const:c6d000:8"]]
+ 00592160 ["COPY", "register:4008:8", ["const:c6e000:8"]]
- 00591e40 bytes e1360090
+ 00592160 bytes e1360090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa77fa20ec074a0ff7a438bcec297910"></a>

### [`00592100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592100.md) → [`00592420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592420.md) FUN_00592420

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00592188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592188.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005924a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/005924a8.md) [`00c596b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00592448",
      "incomplete_value": false,
      "site": "00592464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592128",
      "incomplete_value": false,
      "site": "00592144",
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
            "const:240:8"
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
      "definition_site": "00592450",
      "incomplete_value": false,
      "site": "00592464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592130",
      "incomplete_value": false,
      "site": "00592144",
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
            "const:250:8"
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
      "00592448",
      "PARAM",
      [
        "storage",
        "00c6d240",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00592450",
      "PARAM",
      [
        "storage",
        "00c6d250",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00592448",
      "PARAM",
      [
        "storage",
        "00c6e210",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00592450",
      "PARAM",
      [
        "storage",
        "00c6e220",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592100.md#insn-00592144) · [`00592124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592100.md#insn-00592124) · [`00592128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592100.md#insn-00592128)
- 新版 [`00592464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592420.md#insn-00592464) · [`00592444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592420.md#insn-00592444) · [`00592448`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592420.md#insn-00592448)

~~~diff
- 00592144 ["INT_ADD", "register:40f0:8", ["const:592144:8", "const:4:8"]]
- 00592144 ["CALL", null, ["callee:00c596b0:8"]]
+ 00592464 ["INT_ADD", "register:40f0:8", ["const:592464:8", "const:4:8"]]
+ 00592464 ["CALL", null, ["callee:00c596b0:8"]]
- 00592144 bytes 67191b94
+ 00592464 bytes 931c1b94
- 00592124 ["COPY", "register:4008:8", ["const:c6d000:8"]]
+ 00592444 ["COPY", "register:4008:8", ["const:c6e000:8"]]
- 00592124 bytes c13600f0
+ 00592444 bytes e1360090
- 00592128 ["COPY", "tmp:0:8", ["const:240:8"]]
- 00592128 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00592128 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00592128 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00592448 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 00592448 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00592448 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00592448 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00592128 bytes 21000991
+ 00592448 bytes 21400891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c15830fca32193728d4d349fc04ee9e4"></a>

### [`005923f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005923f0.md) → [`00592710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592710.md) FUN_00592710

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0043b128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b128.md) · 呼出先 2件 [`00590df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00590/00590df8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`0043b448`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b448.md) · 呼出先 2件 [`00591118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591118.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00592734",
      "incomplete_value": false,
      "site": "00592740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592414",
      "incomplete_value": false,
      "site": "00592420",
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
            "const:530:8"
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
      "00592740",
      "DATA",
      [
        "storage",
        "00c6d530",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592740",
      "DATA",
      [
        "storage",
        "00c6e500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005923f0.md#insn-00592408) · [`00592410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005923f0.md#insn-00592410) · [`00592414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005923f0.md#insn-00592414)
- 新版 [`00592728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592710.md#insn-00592728) · [`00592730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592710.md#insn-00592730) · [`00592734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592710.md#insn-00592734)

~~~diff
- 00592408 ["INT_ADD", "register:40f0:8", ["const:592408:8", "const:4:8"]]
- 00592408 ["CALL", null, ["callee:00c58f30:8"]]
+ 00592728 ["INT_ADD", "register:40f0:8", ["const:592728:8", "const:4:8"]]
+ 00592728 ["CALL", null, ["callee:00c58f30:8"]]
- 00592408 bytes d6161b94
+ 00592728 bytes 021a1b94
- 00592410 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00592730 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00592410 bytes c83600f0
+ 00592730 bytes e8360090
- 00592414 ["COPY", "tmp:0:8", ["const:530:8"]]
- 00592414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592734 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 00592734 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592734 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592734 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592414 bytes 08c11491
+ 00592734 bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b89a5a50c18d2cc22415aa82fd897da"></a>

### [`0059245c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059245c.md) → [`0059277c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/0059277c.md) FUN_0059277c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

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
      "definition_site": "00592794",
      "incomplete_value": false,
      "site": "00592798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592474",
      "incomplete_value": false,
      "site": "00592478",
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
            "const:e0:8"
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
      "00592798",
      "DATA",
      [
        "storage",
        "00c6d0e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592798",
      "DATA",
      [
        "storage",
        "00c6e0b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059245c.md#insn-00592470) · [`00592474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059245c.md#insn-00592474) · [`00592488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059245c.md#insn-00592488)
- 新版 [`00592790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/0059277c.md#insn-00592790) · [`00592794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/0059277c.md#insn-00592794) · [`005927a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/0059277c.md#insn-005927a8)

~~~diff
- 00592470 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00592790 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00592470 bytes c83600f0
+ 00592790 bytes e8360090
- 00592474 ["COPY", "tmp:0:8", ["const:e0:8"]]
- 00592474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592794 ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 00592794 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592794 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592794 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592474 bytes 08810391
+ 00592794 bytes 08c10291
- 00592488 ["INT_ADD", "register:40f0:8", ["const:592488:8", "const:4:8"]]
- 00592488 ["CALL", null, ["callee:00c54d90:8"]]
+ 005927a8 ["INT_ADD", "register:40f0:8", ["const:5927a8:8", "const:4:8"]]
+ 005927a8 ["CALL", null, ["callee:00c54d90:8"]]
- 00592488 bytes 46061b94
+ 005927a8 bytes 7a091b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33fb769458d1a96d3157500a37ef6e76"></a>

### [`005924f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005924f8.md) → [`00592818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592818.md) FUN_00592818

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592830",
      "incomplete_value": false,
      "site": "00592834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592510",
      "incomplete_value": false,
      "site": "00592514",
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
            "const:e0:8"
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
      "00592834",
      "DATA",
      [
        "storage",
        "00c6d0e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592834",
      "DATA",
      [
        "storage",
        "00c6e0b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059250c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005924f8.md#insn-0059250c) · [`00592510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005924f8.md#insn-00592510) · [`00592524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005924f8.md#insn-00592524)
- 新版 [`0059282c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592818.md#insn-0059282c) · [`00592830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592818.md#insn-00592830) · [`00592844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592818.md#insn-00592844)

~~~diff
- 0059250c ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059282c ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059250c bytes c83600f0
+ 0059282c bytes e8360090
- 00592510 ["COPY", "tmp:0:8", ["const:e0:8"]]
- 00592510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592830 ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 00592830 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592830 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592830 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592510 bytes 08810391
+ 00592830 bytes 08c10291
- 00592524 ["INT_ADD", "register:40f0:8", ["const:592524:8", "const:4:8"]]
- 00592524 ["CALL", null, ["callee:00c54d90:8"]]
+ 00592844 ["INT_ADD", "register:40f0:8", ["const:592844:8", "const:4:8"]]
+ 00592844 ["CALL", null, ["callee:00c54d90:8"]]
- 00592524 bytes 1f061b94
+ 00592844 bytes 53091b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6c44d032b1d40179c8aaf63038ecf30"></a>

### [`00592604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592604.md) → [`00592924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592924.md) FUN_00592924

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
      "definition_site": "00592928",
      "incomplete_value": false,
      "site": "0059292c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592608",
      "incomplete_value": false,
      "site": "0059260c",
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
            "const:2b0:8"
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
      "0059292c",
      "DATA",
      [
        "storage",
        "00c6d2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059292c",
      "DATA",
      [
        "storage",
        "00c6e280",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592604.md#insn-00592604) · [`00592608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592604.md#insn-00592608)
- 新版 [`00592924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592924.md#insn-00592924) · [`00592928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592924.md#insn-00592928)

~~~diff
- 00592604 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00592924 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00592604 bytes c83600f0
+ 00592924 bytes e8360090
- 00592608 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 00592608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592928 ["COPY", "tmp:0:8", ["const:280:8"]]
+ 00592928 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592928 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592928 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592608 bytes 08c10a91
+ 00592928 bytes 08010a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-259a487f952b7b923ba66630e64af015"></a>

### [`00592614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592614.md) → [`00592934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592934.md) FUN_00592934

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
      "definition_site": "00592944",
      "incomplete_value": false,
      "site": "0059294c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592624",
      "incomplete_value": false,
      "site": "0059262c",
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
            "const:2b0:8"
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
      "0059294c",
      "DATA",
      [
        "storage",
        "00c6d2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059294c",
      "DATA",
      [
        "storage",
        "00c6e280",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592614.md#insn-00592620) · [`00592624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592614.md#insn-00592624) · [`00592630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592614.md#insn-00592630)
- 新版 [`00592940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592934.md#insn-00592940) · [`00592944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592934.md#insn-00592944) · [`00592950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592934.md#insn-00592950)

~~~diff
- 00592620 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00592940 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00592620 bytes c83600f0
+ 00592940 bytes e8360090
- 00592624 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 00592624 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592624 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592624 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592944 ["COPY", "tmp:0:8", ["const:280:8"]]
+ 00592944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592624 bytes 08c10a91
+ 00592944 bytes 08010a91
- 00592630 ["INT_ADD", "register:40f0:8", ["const:592630:8", "const:4:8"]]
- 00592630 ["CALL", null, ["callee:00c58f40:8"]]
+ 00592950 ["INT_ADD", "register:40f0:8", ["const:592950:8", "const:4:8"]]
+ 00592950 ["CALL", null, ["callee:00c58f40:8"]]
- 00592630 bytes 50161b94
+ 00592950 bytes 7c191b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4420645cac0018a182e6e7eec5193e5d"></a>

### [`00592654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592654.md) → [`00592974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592974.md) FUN_00592974

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00c5a620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a620.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005555e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/005555e8.md) [`00c5b5f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b5f0.md)

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
      "definition_site": "0059298c",
      "incomplete_value": false,
      "site": "00592990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059266c",
      "incomplete_value": false,
      "site": "00592670",
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
      "00592990",
      "DATA",
      [
        "storage",
        "00c6d300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592990",
      "DATA",
      [
        "storage",
        "00c6e2d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592654.md#insn-00592668) · [`0059266c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592654.md#insn-0059266c) · [`00592674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592654.md#insn-00592674)
- 新版 [`00592988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592974.md#insn-00592988) · [`0059298c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592974.md#insn-0059298c) · [`00592994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592974.md#insn-00592994)

~~~diff
- 00592668 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00592988 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00592668 bytes c83600f0
+ 00592988 bytes e8360090
- 0059266c ["COPY", "tmp:0:8", ["const:300:8"]]
- 0059266c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059266c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059266c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059298c ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 0059298c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059298c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059298c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059266c bytes 08010c91
+ 0059298c bytes 08410b91
- 00592674 ["INT_ADD", "register:40f0:8", ["const:592674:8", "const:4:8"]]
- 00592674 ["CALL", null, ["callee:005555e8:8"]]
+ 00592994 ["INT_ADD", "register:40f0:8", ["const:592994:8", "const:4:8"]]
+ 00592994 ["CALL", null, ["callee:005555e8:8"]]
- 00592674 bytes 150bff97
+ 00592994 bytes 150bff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6722202dcfa43b5d0950d6e596a99a7f"></a>

### [`0059269c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059269c.md) → [`005929bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/005929bc.md) FUN_005929bc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a620.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005555e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/005555e8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b5f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b5f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005929d4",
      "incomplete_value": false,
      "site": "005929d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005926b4",
      "incomplete_value": false,
      "site": "005926b8",
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
      "005929d8",
      "DATA",
      [
        "storage",
        "00c6d300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005929d8",
      "DATA",
      [
        "storage",
        "00c6e2d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005926b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059269c.md#insn-005926b0) · [`005926b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059269c.md#insn-005926b4) · [`005926bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059269c.md#insn-005926bc)
- 新版 [`005929d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/005929bc.md#insn-005929d0) · [`005929d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/005929bc.md#insn-005929d4) · [`005929dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/005929bc.md#insn-005929dc)

~~~diff
- 005926b0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 005929d0 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005926b0 bytes c83600f0
+ 005929d0 bytes e8360090
- 005926b4 ["COPY", "tmp:0:8", ["const:300:8"]]
- 005926b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005926b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005926b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005929d4 ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 005929d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005929d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005929d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005926b4 bytes 08010c91
+ 005929d4 bytes 08410b91
- 005926bc ["INT_ADD", "register:40f0:8", ["const:5926bc:8", "const:4:8"]]
- 005926bc ["CALL", null, ["callee:005555e8:8"]]
+ 005929dc ["INT_ADD", "register:40f0:8", ["const:5929dc:8", "const:4:8"]]
+ 005929dc ["CALL", null, ["callee:005555e8:8"]]
- 005926bc bytes 030bff97
+ 005929dc bytes 030bff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-747389a58d6c5d8ea04f9bab1c996225"></a>

### [`0059288c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059288c.md) → [`00592bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592bac.md) FUN_00592bac

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
      "definition_site": "00592bb0",
      "incomplete_value": false,
      "site": "00592bb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592890",
      "incomplete_value": false,
      "site": "00592894",
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
      "00592bb4",
      "DATA",
      [
        "storage",
        "00c6d368",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592bb4",
      "DATA",
      [
        "storage",
        "00c6e338",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059288c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059288c.md#insn-0059288c) · [`00592890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059288c.md#insn-00592890)
- 新版 [`00592bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592bac.md#insn-00592bac) · [`00592bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592bac.md#insn-00592bb0)

~~~diff
- 0059288c ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00592bac ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059288c bytes c83600f0
+ 00592bac bytes e8360090
- 00592890 ["COPY", "tmp:0:8", ["const:368:8"]]
- 00592890 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592890 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592890 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592bb0 ["COPY", "tmp:0:8", ["const:338:8"]]
+ 00592bb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592bb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592bb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592890 bytes 08a10d91
+ 00592bb0 bytes 08e10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d8660f02b7fbd4ffb71edb6c27dae1f"></a>

### [`0059289c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059289c.md) → [`00592bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592bbc.md) FUN_00592bbc

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
      "definition_site": "00592bcc",
      "incomplete_value": false,
      "site": "00592bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005928ac",
      "incomplete_value": false,
      "site": "005928b4",
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
      "00592bd4",
      "DATA",
      [
        "storage",
        "00c6d368",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592bd4",
      "DATA",
      [
        "storage",
        "00c6e338",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005928a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059289c.md#insn-005928a8) · [`005928ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059289c.md#insn-005928ac) · [`005928b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/0059289c.md#insn-005928b8)
- 新版 [`00592bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592bbc.md#insn-00592bc8) · [`00592bcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592bbc.md#insn-00592bcc) · [`00592bd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592bbc.md#insn-00592bd8)

~~~diff
- 005928a8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00592bc8 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005928a8 bytes c83600f0
+ 00592bc8 bytes e8360090
- 005928ac ["COPY", "tmp:0:8", ["const:368:8"]]
- 005928ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005928ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005928ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592bcc ["COPY", "tmp:0:8", ["const:338:8"]]
+ 00592bcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592bcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592bcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005928ac bytes 08a10d91
+ 00592bcc bytes 08e10c91
- 005928b8 ["INT_ADD", "register:40f0:8", ["const:5928b8:8", "const:4:8"]]
- 005928b8 ["CALL", null, ["callee:00c58f40:8"]]
+ 00592bd8 ["INT_ADD", "register:40f0:8", ["const:592bd8:8", "const:4:8"]]
+ 00592bd8 ["CALL", null, ["callee:00c58f40:8"]]
- 005928b8 bytes ae151b94
+ 00592bd8 bytes da181b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-391db45609896d8ec16107a1c1755c9d"></a>

### [`005928dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005928dc.md) → [`00592bfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592bfc.md) FUN_00592bfc

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00c5a630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a630.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005555e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/005555e8.md) [`00c5b600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b600.md)

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
      "definition_site": "00592c14",
      "incomplete_value": false,
      "site": "00592c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005928f4",
      "incomplete_value": false,
      "site": "005928f8",
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
            "const:3b8:8"
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
      "00592c18",
      "DATA",
      [
        "storage",
        "00c6d3b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592c18",
      "DATA",
      [
        "storage",
        "00c6e388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005928f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005928dc.md#insn-005928f0) · [`005928f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005928dc.md#insn-005928f4) · [`005928fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005928dc.md#insn-005928fc)
- 新版 [`00592c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592bfc.md#insn-00592c10) · [`00592c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592bfc.md#insn-00592c14) · [`00592c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592bfc.md#insn-00592c1c)

~~~diff
- 005928f0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00592c10 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005928f0 bytes c83600f0
+ 00592c10 bytes e8360090
- 005928f4 ["COPY", "tmp:0:8", ["const:3b8:8"]]
- 005928f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005928f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005928f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592c14 ["COPY", "tmp:0:8", ["const:388:8"]]
+ 00592c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005928f4 bytes 08e10e91
+ 00592c14 bytes 08210e91
- 005928fc ["INT_ADD", "register:40f0:8", ["const:5928fc:8", "const:4:8"]]
- 005928fc ["CALL", null, ["callee:005555e8:8"]]
+ 00592c1c ["INT_ADD", "register:40f0:8", ["const:592c1c:8", "const:4:8"]]
+ 00592c1c ["CALL", null, ["callee:005555e8:8"]]
- 005928fc bytes 730aff97
+ 00592c1c bytes 730aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42339d7f1c8174359e88f3c4eeccff39"></a>

### [`00592924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592924.md) → [`00592c44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592c44.md) FUN_00592c44

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a630.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005555e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/005555e8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b600.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592c5c",
      "incomplete_value": false,
      "site": "00592c60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059293c",
      "incomplete_value": false,
      "site": "00592940",
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
            "const:3b8:8"
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
      "00592c60",
      "DATA",
      [
        "storage",
        "00c6d3b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592c60",
      "DATA",
      [
        "storage",
        "00c6e388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592924.md#insn-00592938) · [`0059293c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592924.md#insn-0059293c) · [`00592944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592924.md#insn-00592944)
- 新版 [`00592c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592c44.md#insn-00592c58) · [`00592c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592c44.md#insn-00592c5c) · [`00592c64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592c44.md#insn-00592c64)

~~~diff
- 00592938 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00592c58 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00592938 bytes c83600f0
+ 00592c58 bytes e8360090
- 0059293c ["COPY", "tmp:0:8", ["const:3b8:8"]]
- 0059293c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059293c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059293c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592c5c ["COPY", "tmp:0:8", ["const:388:8"]]
+ 00592c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059293c bytes 08e10e91
+ 00592c5c bytes 08210e91
- 00592944 ["INT_ADD", "register:40f0:8", ["const:592944:8", "const:4:8"]]
- 00592944 ["CALL", null, ["callee:005555e8:8"]]
+ 00592c64 ["INT_ADD", "register:40f0:8", ["const:592c64:8", "const:4:8"]]
+ 00592c64 ["CALL", null, ["callee:005555e8:8"]]
- 00592944 bytes 610aff97
+ 00592c64 bytes 610aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c0fc6078b2f2d7bce6b0c4dab55c2ff"></a>

### [`005929b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005929b8.md) → [`00592cd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592cd8.md) FUN_00592cd8

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
      "definition_site": "00592cdc",
      "incomplete_value": false,
      "site": "00592ce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005929bc",
      "incomplete_value": false,
      "site": "005929c0",
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
            "const:420:8"
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
      "00592ce0",
      "DATA",
      [
        "storage",
        "00c6d420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592ce0",
      "DATA",
      [
        "storage",
        "00c6e3f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005929b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005929b8.md#insn-005929b8) · [`005929bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005929b8.md#insn-005929bc)
- 新版 [`00592cd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592cd8.md#insn-00592cd8) · [`00592cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592cd8.md#insn-00592cdc)

~~~diff
- 005929b8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00592cd8 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005929b8 bytes c83600f0
+ 00592cd8 bytes e8360090
- 005929bc ["COPY", "tmp:0:8", ["const:420:8"]]
- 005929bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005929bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005929bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592cdc ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 00592cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005929bc bytes 08811091
+ 00592cdc bytes 08c10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ac64f8dc4dd134b9771a23f5ae686bd"></a>

### [`005929c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005929c8.md) → [`00592ce8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592ce8.md) FUN_00592ce8

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
      "definition_site": "00592cf8",
      "incomplete_value": false,
      "site": "00592d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005929d8",
      "incomplete_value": false,
      "site": "005929e0",
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
            "const:420:8"
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
      "00592d00",
      "DATA",
      [
        "storage",
        "00c6d420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592d00",
      "DATA",
      [
        "storage",
        "00c6e3f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005929d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005929c8.md#insn-005929d4) · [`005929d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005929c8.md#insn-005929d8) · [`005929e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/005929c8.md#insn-005929e4)
- 新版 [`00592cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592ce8.md#insn-00592cf4) · [`00592cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592ce8.md#insn-00592cf8) · [`00592d04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592ce8.md#insn-00592d04)

~~~diff
- 005929d4 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00592cf4 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005929d4 bytes c83600f0
+ 00592cf4 bytes e8360090
- 005929d8 ["COPY", "tmp:0:8", ["const:420:8"]]
- 005929d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005929d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005929d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592cf8 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 00592cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005929d8 bytes 08811091
+ 00592cf8 bytes 08c10f91
- 005929e4 ["INT_ADD", "register:40f0:8", ["const:5929e4:8", "const:4:8"]]
- 005929e4 ["CALL", null, ["callee:00c58f40:8"]]
+ 00592d04 ["INT_ADD", "register:40f0:8", ["const:592d04:8", "const:4:8"]]
+ 00592d04 ["CALL", null, ["callee:00c58f40:8"]]
- 005929e4 bytes 63151b94
+ 00592d04 bytes 8f181b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fba9e832ef66614ebc94fef2c768de39"></a>

### [`00592a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a08.md) → [`00592d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592d28.md) FUN_00592d28

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00c5a640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a640.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005555e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/005555e8.md) [`00c5b610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b610.md)

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
      "definition_site": "00592d40",
      "incomplete_value": false,
      "site": "00592d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592a20",
      "incomplete_value": false,
      "site": "00592a24",
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
            "const:470:8"
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
      "00592d44",
      "DATA",
      [
        "storage",
        "00c6d470",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592d44",
      "DATA",
      [
        "storage",
        "00c6e440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a08.md#insn-00592a1c) · [`00592a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a08.md#insn-00592a20) · [`00592a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a08.md#insn-00592a28)
- 新版 [`00592d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592d28.md#insn-00592d3c) · [`00592d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592d28.md#insn-00592d40) · [`00592d48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592d28.md#insn-00592d48)

~~~diff
- 00592a1c ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00592d3c ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00592a1c bytes c83600f0
+ 00592d3c bytes e8360090
- 00592a20 ["COPY", "tmp:0:8", ["const:470:8"]]
- 00592a20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592a20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592a20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592d40 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 00592d40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592d40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592d40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592a20 bytes 08c11191
+ 00592d40 bytes 08011191
- 00592a28 ["INT_ADD", "register:40f0:8", ["const:592a28:8", "const:4:8"]]
- 00592a28 ["CALL", null, ["callee:005555e8:8"]]
+ 00592d48 ["INT_ADD", "register:40f0:8", ["const:592d48:8", "const:4:8"]]
+ 00592d48 ["CALL", null, ["callee:005555e8:8"]]
- 00592a28 bytes 280aff97
+ 00592d48 bytes 280aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8084de28f2dd37a314e9241b20ef716f"></a>

### [`00592a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a50.md) → [`00592d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592d70.md) FUN_00592d70

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a640.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005555e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/005555e8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b610.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592d88",
      "incomplete_value": false,
      "site": "00592d8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592a68",
      "incomplete_value": false,
      "site": "00592a6c",
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
            "const:470:8"
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
      "00592d8c",
      "DATA",
      [
        "storage",
        "00c6d470",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592d8c",
      "DATA",
      [
        "storage",
        "00c6e440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a50.md#insn-00592a64) · [`00592a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a50.md#insn-00592a68) · [`00592a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592a50.md#insn-00592a70)
- 新版 [`00592d84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592d70.md#insn-00592d84) · [`00592d88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592d70.md#insn-00592d88) · [`00592d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592d70.md#insn-00592d90)

~~~diff
- 00592a64 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00592d84 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00592a64 bytes c83600f0
+ 00592d84 bytes e8360090
- 00592a68 ["COPY", "tmp:0:8", ["const:470:8"]]
- 00592a68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592a68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592a68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592d88 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 00592d88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592d88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592d88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592a68 bytes 08c11191
+ 00592d88 bytes 08011191
- 00592a70 ["INT_ADD", "register:40f0:8", ["const:592a70:8", "const:4:8"]]
- 00592a70 ["CALL", null, ["callee:005555e8:8"]]
+ 00592d90 ["INT_ADD", "register:40f0:8", ["const:592d90:8", "const:4:8"]]
+ 00592d90 ["CALL", null, ["callee:005555e8:8"]]
- 00592a70 bytes 160aff97
+ 00592d90 bytes 160aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c58e354e142247291e9e3d8064c1983"></a>

### [`00592bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592bac.md) → [`00592ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592ecc.md) FUN_00592ecc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0059170c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059170c.md) · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5a680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a680.md)
- 新版 呼出元 1件 [`00591a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/00591a2c.md) · 呼出先 2件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5b650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b650.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00592ef4",
      "incomplete_value": false,
      "site": "00592f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592bd4",
      "incomplete_value": false,
      "site": "00592bec",
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
            "const:4a8:8"
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
      "definition_site": "00592f10",
      "incomplete_value": false,
      "site": "00592f10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592bf0",
      "incomplete_value": false,
      "site": "00592bf0",
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
            "const:4f8:8"
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
      "00592f0c",
      "DATA",
      [
        "storage",
        "00c6d4a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00592f10",
      "DATA",
      [
        "storage",
        "00c6d4f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592f0c",
      "DATA",
      [
        "storage",
        "00c6e478",
        null,
        "undefined *"
      ]
    ],
    [
      "00592f10",
      "DATA",
      [
        "storage",
        "00c6e4c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592bac.md#insn-00592bc4) · [`00592bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592bac.md#insn-00592bd0) · [`00592bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592bac.md#insn-00592bd4)
- 新版 [`00592ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592ecc.md#insn-00592ee4) · [`00592ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592ecc.md#insn-00592ef0) · [`00592ef4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592ecc.md#insn-00592ef4)

~~~diff
- 00592bc4 ["INT_ADD", "register:40f0:8", ["const:592bc4:8", "const:4:8"]]
- 00592bc4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00592ee4 ["INT_ADD", "register:40f0:8", ["const:592ee4:8", "const:4:8"]]
+ 00592ee4 ["CALL", null, ["callee:00c58f30:8"]]
- 00592bc4 bytes e7141b94
+ 00592ee4 bytes 13181b94
- 00592bd0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00592ef0 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00592bd0 bytes c83600f0
+ 00592ef0 bytes e8360090
- 00592bd4 ["COPY", "tmp:0:8", ["const:4a8:8"]]
- 00592bd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592bd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592bd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592ef4 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 00592ef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592ef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592ef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592bd4 bytes 08a11291
+ 00592ef4 bytes 08e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12a23d9243edbe0137db7ef6a6881989"></a>

### [`00592c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592c54.md) → [`00592f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592f74.md) FUN_00592f74

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
      "definition_site": "00592f78",
      "incomplete_value": false,
      "site": "00592f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592c58",
      "incomplete_value": false,
      "site": "00592c5c",
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
            "const:4a8:8"
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
      "00592f7c",
      "DATA",
      [
        "storage",
        "00c6d4a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592f7c",
      "DATA",
      [
        "storage",
        "00c6e478",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592c54.md#insn-00592c54) · [`00592c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592c54.md#insn-00592c58)
- 新版 [`00592f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592f74.md#insn-00592f74) · [`00592f78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592f74.md#insn-00592f78)

~~~diff
- 00592c54 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00592f74 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00592c54 bytes c83600f0
+ 00592f74 bytes e8360090
- 00592c58 ["COPY", "tmp:0:8", ["const:4a8:8"]]
- 00592c58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592c58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592c58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592f78 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 00592f78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592f78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592f78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592c58 bytes 08a11291
+ 00592f78 bytes 08e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1eb619124609e08181ceacfc26c4dc80"></a>

### [`00592c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592c64.md) → [`00592f84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592f84.md) FUN_00592f84

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
      "definition_site": "00592f94",
      "incomplete_value": false,
      "site": "00592f9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592c74",
      "incomplete_value": false,
      "site": "00592c7c",
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
            "const:4a8:8"
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
      "00592f9c",
      "DATA",
      [
        "storage",
        "00c6d4a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00592f9c",
      "DATA",
      [
        "storage",
        "00c6e478",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592c64.md#insn-00592c70) · [`00592c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592c64.md#insn-00592c74) · [`00592c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592c64.md#insn-00592c80)
- 新版 [`00592f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592f84.md#insn-00592f90) · [`00592f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592f84.md#insn-00592f94) · [`00592fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00592/00592f84.md#insn-00592fa0)

~~~diff
- 00592c70 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00592f90 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00592c70 bytes c83600f0
+ 00592f90 bytes e8360090
- 00592c74 ["COPY", "tmp:0:8", ["const:4a8:8"]]
- 00592c74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592c74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592c74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00592f94 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 00592f94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00592f94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00592f94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592c74 bytes 08a11291
+ 00592f94 bytes 08e11191
- 00592c80 ["INT_ADD", "register:40f0:8", ["const:592c80:8", "const:4:8"]]
- 00592c80 ["CALL", null, ["callee:00c58f40:8"]]
+ 00592fa0 ["INT_ADD", "register:40f0:8", ["const:592fa0:8", "const:4:8"]]
+ 00592fa0 ["CALL", null, ["callee:00c58f40:8"]]
- 00592c80 bytes bc141b94
+ 00592fa0 bytes e8171b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f52684e9e8b3b3e64490d2e58044c61"></a>

### [`00592cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592cf4.md) → [`00593014`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/00593014.md) FUN_00593014

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

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
      "definition_site": "0059302c",
      "incomplete_value": false,
      "site": "00593030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592d0c",
      "incomplete_value": false,
      "site": "00592d10",
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
            "const:4f8:8"
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
      "00593030",
      "DATA",
      [
        "storage",
        "00c6d4f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593030",
      "DATA",
      [
        "storage",
        "00c6e4c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592cf4.md#insn-00592d08) · [`00592d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592cf4.md#insn-00592d0c) · [`00592d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592cf4.md#insn-00592d20)
- 新版 [`00593028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/00593014.md#insn-00593028) · [`0059302c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/00593014.md#insn-0059302c) · [`00593040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/00593014.md#insn-00593040)

~~~diff
- 00592d08 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00593028 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00592d08 bytes c83600f0
+ 00593028 bytes c83600f0
- 00592d0c ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 00592d0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592d0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592d0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059302c ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 0059302c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059302c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059302c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592d0c bytes 08e11391
+ 0059302c bytes 08211391
- 00592d20 ["INT_ADD", "register:40f0:8", ["const:592d20:8", "const:4:8"]]
- 00592d20 ["CALL", null, ["callee:00c54d90:8"]]
+ 00593040 ["INT_ADD", "register:40f0:8", ["const:593040:8", "const:4:8"]]
+ 00593040 ["CALL", null, ["callee:00c54d90:8"]]
- 00592d20 bytes 20041b94
+ 00593040 bytes 54071b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-013cd1da9ce1466b2baded9019ab15ad"></a>

### [`00592dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592dc0.md) → [`005930e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/005930e0.md) FUN_005930e0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "005930f8",
      "incomplete_value": false,
      "site": "005930fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00592dd8",
      "incomplete_value": false,
      "site": "00592ddc",
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
            "const:4f8:8"
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
      "005930fc",
      "DATA",
      [
        "storage",
        "00c6d4f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005930fc",
      "DATA",
      [
        "storage",
        "00c6e4c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00592dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592dc0.md#insn-00592dd4) · [`00592dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592dc0.md#insn-00592dd8) · [`00592dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592dc0.md#insn-00592dec)
- 新版 [`005930f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/005930e0.md#insn-005930f4) · [`005930f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/005930e0.md#insn-005930f8) · [`0059310c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/005930e0.md#insn-0059310c)

~~~diff
- 00592dd4 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 005930f4 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00592dd4 bytes c83600f0
+ 005930f4 bytes c83600f0
- 00592dd8 ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 00592dd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00592dd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00592dd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005930f8 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 005930f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005930f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005930f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00592dd8 bytes 08e11391
+ 005930f8 bytes 08211391
- 00592dec ["INT_ADD", "register:40f0:8", ["const:592dec:8", "const:4:8"]]
- 00592dec ["CALL", null, ["callee:00c54d90:8"]]
+ 0059310c ["INT_ADD", "register:40f0:8", ["const:59310c:8", "const:4:8"]]
+ 0059310c ["CALL", null, ["callee:00c54d90:8"]]
- 00592dec bytes ed031b94
+ 0059310c bytes 21071b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc840df140f5ee33807bcb4020d7679a"></a>

### [`00592ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592ff8.md) → [`00593318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/00593318.md) FUN_00593318

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f70.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00593350",
      "incomplete_value": false,
      "site": "00593364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593030",
      "incomplete_value": false,
      "site": "00593044",
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
            "const:1f0:8"
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
      "definition_site": "00593358",
      "incomplete_value": false,
      "site": "00593364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593038",
      "incomplete_value": false,
      "site": "00593044",
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
            "const:200:8"
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
      "00593350",
      "PARAM",
      [
        "storage",
        "00c6d1f0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00593358",
      "PARAM",
      [
        "storage",
        "00c6d200",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00593350",
      "PARAM",
      [
        "storage",
        "00c6e1c0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00593358",
      "PARAM",
      [
        "storage",
        "00c6e1d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592ff8.md#insn-00593044) · [`0059302c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592ff8.md#insn-0059302c) · [`00593030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00592/00592ff8.md#insn-00593030)
- 新版 [`00593364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/00593318.md#insn-00593364) · [`0059334c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/00593318.md#insn-0059334c) · [`00593350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/00593318.md#insn-00593350)

~~~diff
- 00593044 ["INT_ADD", "register:40f0:8", ["const:593044:8", "const:4:8"]]
- 00593044 ["CALL", null, ["callee:00c596b0:8"]]
+ 00593364 ["INT_ADD", "register:40f0:8", ["const:593364:8", "const:4:8"]]
+ 00593364 ["CALL", null, ["callee:00c596b0:8"]]
- 00593044 bytes a7151b94
+ 00593364 bytes d3181b94
- 0059302c ["COPY", "register:4008:8", ["const:c6d000:8"]]
+ 0059334c ["COPY", "register:4008:8", ["const:c6e000:8"]]
- 0059302c bytes c13600d0
+ 0059334c bytes c13600f0
- 00593030 ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 00593030 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00593030 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00593030 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00593350 ["COPY", "tmp:0:8", ["const:1c0:8"]]
+ 00593350 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00593350 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00593350 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00593030 bytes 21c00791
+ 00593350 bytes 21000791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afdedbacf505f02ad559ab14c02acfe2"></a>

### [`005931b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005931b4.md) → [`005934d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/005934d4.md) FUN_005934d4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f70.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

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
      "definition_site": "00593514",
      "incomplete_value": true,
      "site": "00593520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005931f4",
      "incomplete_value": true,
      "site": "00593200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:200:8"
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
      "0059350c",
      "PARAM",
      [
        "storage",
        "00c6d1f0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00593514",
      "PARAM",
      [
        "storage",
        "00c6d200",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0059350c",
      "PARAM",
      [
        "storage",
        "00c6e1c0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00593514",
      "PARAM",
      [
        "storage",
        "00c6e1d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005931b4.md#insn-00593200) · [`005931e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005931b4.md#insn-005931e8) · [`005931ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005931b4.md#insn-005931ec)
- 新版 [`00593520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/005934d4.md#insn-00593520) · [`00593508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/005934d4.md#insn-00593508) · [`0059350c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/005934d4.md#insn-0059350c)

~~~diff
- 00593200 ["INT_ADD", "register:40f0:8", ["const:593200:8", "const:4:8"]]
- 00593200 ["CALL", null, ["callee:00c596b0:8"]]
+ 00593520 ["INT_ADD", "register:40f0:8", ["const:593520:8", "const:4:8"]]
+ 00593520 ["CALL", null, ["callee:00c596b0:8"]]
- 00593200 bytes 38151b94
+ 00593520 bytes 64181b94
- 005931e8 ["COPY", "register:4008:8", ["const:c6d000:8"]]
+ 00593508 ["COPY", "register:4008:8", ["const:c6e000:8"]]
- 005931e8 bytes c13600d0
+ 00593508 bytes c13600f0
- 005931ec ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 005931ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005931ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005931ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0059350c ["COPY", "tmp:0:8", ["const:1c0:8"]]
+ 0059350c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0059350c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0059350c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005931ec bytes 21c00791
+ 0059350c bytes 21000791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2aef4ce7742725afb4d6103308710f2c"></a>

### [`00593370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593370.md) → [`00593690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/00593690.md) FUN_00593690

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
      "definition_site": "00593694",
      "incomplete_value": false,
      "site": "00593698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593374",
      "incomplete_value": false,
      "site": "00593378",
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
            "const:530:8"
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
      "00593698",
      "DATA",
      [
        "storage",
        "00c6d530",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593698",
      "DATA",
      [
        "storage",
        "00c6e500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593370.md#insn-00593370) · [`00593374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593370.md#insn-00593374)
- 新版 [`00593690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/00593690.md#insn-00593690) · [`00593694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/00593690.md#insn-00593694)

~~~diff
- 00593370 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00593690 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00593370 bytes c83600d0
+ 00593690 bytes c83600f0
- 00593374 ["COPY", "tmp:0:8", ["const:530:8"]]
- 00593374 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593374 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593374 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593694 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 00593694 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593694 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593694 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593374 bytes 08c11491
+ 00593694 bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9dc59c0584efaa173e0ea9c28e5b11f"></a>

### [`00593380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593380.md) → [`005936a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/005936a0.md) FUN_005936a0

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
      "definition_site": "005936b0",
      "incomplete_value": false,
      "site": "005936b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593390",
      "incomplete_value": false,
      "site": "00593398",
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
            "const:530:8"
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
      "005936b8",
      "DATA",
      [
        "storage",
        "00c6d530",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005936b8",
      "DATA",
      [
        "storage",
        "00c6e500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059338c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593380.md#insn-0059338c) · [`00593390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593380.md#insn-00593390) · [`0059339c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593380.md#insn-0059339c)
- 新版 [`005936ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/005936a0.md#insn-005936ac) · [`005936b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/005936a0.md#insn-005936b0) · [`005936bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/005936a0.md#insn-005936bc)

~~~diff
- 0059338c ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 005936ac ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059338c bytes c83600d0
+ 005936ac bytes c83600f0
- 00593390 ["COPY", "tmp:0:8", ["const:530:8"]]
- 00593390 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593390 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593390 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005936b0 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 005936b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005936b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005936b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593390 bytes 08c11491
+ 005936b0 bytes 08011491
- 0059339c ["INT_ADD", "register:40f0:8", ["const:59339c:8", "const:4:8"]]
- 0059339c ["CALL", null, ["callee:00c58f40:8"]]
+ 005936bc ["INT_ADD", "register:40f0:8", ["const:5936bc:8", "const:4:8"]]
+ 005936bc ["CALL", null, ["callee:00c58f40:8"]]
- 0059339c bytes f5121b94
+ 005936bc bytes 21161b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f45b240e3371c114f67079b0ea8a2763"></a>

### [`005933c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005933c0.md) → [`005936e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/005936e0.md) FUN_005936e0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00593ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593ce4.md) · 呼出先 14件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00446db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446db0.md) [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00593804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593804.md)
- 新版 呼出元 1件 [`00594004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594004.md) · 呼出先 14件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`004470d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00447/004470d0.md) [`005555e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/005555e8.md) [`00593b24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/00593b24.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.09% / 新版 99.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00593720",
      "incomplete_value": false,
      "site": "00593724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593400",
      "incomplete_value": false,
      "site": "00593404",
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
            "const:580:8"
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
      "00593724",
      "DATA",
      [
        "storage",
        "00c6d580",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593724",
      "DATA",
      [
        "storage",
        "00c6e550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005933c0.md#insn-00593724) · [`005933fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005933c0.md#insn-005933fc) · [`00593400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005933c0.md#insn-00593400)
- 新版 [`00593a44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/005936e0.md#insn-00593a44) · [`0059371c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/005936e0.md#insn-0059371c) · [`00593720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/005936e0.md#insn-00593720)

~~~diff
- 00593724 ["INT_ADD", "register:40f0:8", ["const:593724:8", "const:4:8"]]
- 00593724 ["CALL", null, ["callee:0043bac4:8"]]
+ 00593a44 ["INT_ADD", "register:40f0:8", ["const:593a44:8", "const:4:8"]]
+ 00593a44 ["CALL", null, ["callee:0043bac4:8"]]
- 00593724 bytes 20a0fa97
+ 00593a44 bytes 20a0fa97
- 005933fc ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059371c ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005933fc bytes c83600d0
+ 0059371c bytes c83600f0
- 00593400 ["COPY", "tmp:0:8", ["const:580:8"]]
- 00593400 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593400 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593400 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593720 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00593720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593400 bytes 08011691
+ 00593720 bytes 08411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ce0d3b80cc13634b254f604179c3996"></a>

### [`00593ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593ce4.md) → [`00594004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594004.md) FUN_00594004

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0059129c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00591/0059129c.md) · 呼出先 21件 [`005933c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/005933c0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md)
- 新版 呼出元 1件 [`005915bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00591/005915bc.md) · 呼出先 21件 [`005936e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00593/005936e0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005944f0",
      "incomplete_value": false,
      "site": "005944fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005941d0",
      "incomplete_value": false,
      "site": "005941dc",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005940f0",
      "incomplete_value": false,
      "site": "005940fc",
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
            "const:337:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593dd0",
      "incomplete_value": false,
      "site": "00593ddc",
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
            "const:268:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0059411c",
      "incomplete_value": false,
      "site": "00594124",
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
      "definition_site": "00593dfc",
      "incomplete_value": false,
      "site": "00593e04",
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
      "005940f0",
      "PARAM",
      [
        "storage",
        "002b6268",
        null,
        "string"
      ]
    ],
    [
      "0059411c",
      "PARAM",
      [
        "storage",
        "002b4c11",
        null,
        null
      ]
    ],
    [
      "00594234",
      "PARAM",
      [
        "storage",
        "002a01ed",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005940f0",
      "PARAM",
      [
        "storage",
        "002b6337",
        null,
        "string"
      ]
    ],
    [
      "0059411c",
      "PARAM",
      [
        "storage",
        "002b4cef",
        null,
        null
      ]
    ],
    [
      "00594234",
      "PARAM",
      [
        "storage",
        "002a022d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593ce4.md#insn-00593ddc) · [`00593e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593ce4.md#insn-00593e04) · [`00593e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00593/00593ce4.md#insn-00593e40)
- 新版 [`005940fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594004.md#insn-005940fc) · [`00594124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594004.md#insn-00594124) · [`00594160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594004.md#insn-00594160)

~~~diff
- 00593ddc ["INT_ADD", "register:40f0:8", ["const:593ddc:8", "const:4:8"]]
- 00593ddc ["CALL", null, ["callee:00c59000:8"]]
+ 005940fc ["INT_ADD", "register:40f0:8", ["const:5940fc:8", "const:4:8"]]
+ 005940fc ["CALL", null, ["callee:00c59000:8"]]
- 00593ddc bytes 95101b94
+ 005940fc bytes c1131b94
- 00593e04 ["INT_ADD", "register:40f0:8", ["const:593e04:8", "const:4:8"]]
- 00593e04 ["CALL", null, ["callee:00c59010:8"]]
+ 00594124 ["INT_ADD", "register:40f0:8", ["const:594124:8", "const:4:8"]]
+ 00594124 ["CALL", null, ["callee:00c59010:8"]]
- 00593e04 bytes 8f101b94
+ 00594124 bytes bb131b94
- 00593e40 ["INT_ADD", "register:40f0:8", ["const:593e40:8", "const:4:8"]]
- 00593e40 ["CALL", null, ["callee:00c59020:8"]]
+ 00594160 ["INT_ADD", "register:40f0:8", ["const:594160:8", "const:4:8"]]
+ 00594160 ["CALL", null, ["callee:00c59020:8"]]
- 00593e40 bytes 84101b94
+ 00594160 bytes b0131b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a86070ab2e5664f8d6f50bc20fd9058"></a>

### [`005948e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005948e0.md) → [`00594c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594c00.md) FUN_00594c00

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
      "definition_site": "00594c04",
      "incomplete_value": false,
      "site": "00594c08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005948e4",
      "incomplete_value": false,
      "site": "005948e8",
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
            "const:5d8:8"
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
      "00594c08",
      "DATA",
      [
        "storage",
        "00c6d5d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594c08",
      "DATA",
      [
        "storage",
        "00c6e5a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005948e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005948e0.md#insn-005948e0) · [`005948e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005948e0.md#insn-005948e4)
- 新版 [`00594c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594c00.md#insn-00594c00) · [`00594c04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594c00.md#insn-00594c04)

~~~diff
- 005948e0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00594c00 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005948e0 bytes c83600b0
+ 00594c00 bytes c83600d0
- 005948e4 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 005948e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005948e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005948e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00594c04 ["COPY", "tmp:0:8", ["const:5a8:8"]]
+ 00594c04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00594c04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00594c04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005948e4 bytes 08611791
+ 00594c04 bytes 08a11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-262a2b3f531925c21a2592ed65c8bb3a"></a>

### [`005948f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005948f0.md) → [`00594c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594c10.md) FUN_00594c10

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
      "definition_site": "00594c20",
      "incomplete_value": false,
      "site": "00594c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594900",
      "incomplete_value": false,
      "site": "00594908",
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
            "const:5d8:8"
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
      "00594c28",
      "DATA",
      [
        "storage",
        "00c6d5d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594c28",
      "DATA",
      [
        "storage",
        "00c6e5a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005948fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005948f0.md#insn-005948fc) · [`00594900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005948f0.md#insn-00594900) · [`0059490c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/005948f0.md#insn-0059490c)
- 新版 [`00594c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594c10.md#insn-00594c1c) · [`00594c20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594c10.md#insn-00594c20) · [`00594c2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594c10.md#insn-00594c2c)

~~~diff
- 005948fc ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00594c1c ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005948fc bytes c83600b0
+ 00594c1c bytes c83600d0
- 00594900 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00594900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00594900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00594900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00594c20 ["COPY", "tmp:0:8", ["const:5a8:8"]]
+ 00594c20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00594c20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00594c20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00594900 bytes 08611791
+ 00594c20 bytes 08a11691
- 0059490c ["INT_ADD", "register:40f0:8", ["const:59490c:8", "const:4:8"]]
- 0059490c ["CALL", null, ["callee:00c58f40:8"]]
+ 00594c2c ["INT_ADD", "register:40f0:8", ["const:594c2c:8", "const:4:8"]]
+ 00594c2c ["CALL", null, ["callee:00c58f40:8"]]
- 0059490c bytes 990d1b94
+ 00594c2c bytes c5101b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3e64850d461ac24931086451bd472cf"></a>

### [`00594920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594920.md) → [`00594c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594c40.md) FUN_00594c40

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`005552c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005552c8.md) [`00594380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594380.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a710.md)
- 新版 呼出元 0件  · 呼出先 4件 [`005555e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00555/005555e8.md) [`005946a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/005946a0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b6e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b6e0.md)

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
      "definition_site": "00594c54",
      "incomplete_value": false,
      "site": "00594c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594934",
      "incomplete_value": false,
      "site": "00594938",
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
            "const:580:8"
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
      "00594c58",
      "DATA",
      [
        "storage",
        "00c6d580",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594c58",
      "DATA",
      [
        "storage",
        "00c6e550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594920.md#insn-00594930) · [`00594934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594920.md#insn-00594934) · [`0059493c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594920.md#insn-0059493c)
- 新版 [`00594c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594c40.md#insn-00594c50) · [`00594c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594c40.md#insn-00594c54) · [`00594c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594c40.md#insn-00594c5c)

~~~diff
- 00594930 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00594c50 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00594930 bytes c83600b0
+ 00594c50 bytes c83600d0
- 00594934 ["COPY", "tmp:0:8", ["const:580:8"]]
- 00594934 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00594934 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00594934 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00594c54 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00594c54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00594c54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00594c54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00594934 bytes 08011691
+ 00594c54 bytes 08411591
- 0059493c ["INT_ADD", "register:40f0:8", ["const:59493c:8", "const:4:8"]]
- 0059493c ["CALL", null, ["callee:005555e8:8"]]
+ 00594c5c ["INT_ADD", "register:40f0:8", ["const:594c5c:8", "const:4:8"]]
+ 00594c5c ["CALL", null, ["callee:005555e8:8"]]
- 0059493c bytes 6302ff97
+ 00594c5c bytes 6302ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a906f79aedfde250c53c08e966bc364a"></a>

### [`00594978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594978.md) → [`00594c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594c98.md) FUN_00594c98

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00588508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588508.md) · 呼出先 7件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00594bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594bac.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00588828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/00588828.md) · 呼出先 7件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00594ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594ecc.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.69% / 新版 96.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00594ccc",
      "incomplete_value": false,
      "site": "00594cdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005949ac",
      "incomplete_value": false,
      "site": "005949bc",
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
      "definition_site": "00594e00",
      "incomplete_value": true,
      "site": "00594e0c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:dc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594ae0",
      "incomplete_value": true,
      "site": "00594aec",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d78:8"
              ]
            ]
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
      "00594cdc",
      "DATA",
      [
        "storage",
        "00c6d628",
        null,
        "undefined *"
      ]
    ],
    [
      "00594e00",
      "READ",
      [
        "storage",
        "002c3d78",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00594cdc",
      "DATA",
      [
        "storage",
        "00c6e5f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00594e00",
      "READ",
      [
        "storage",
        "002c3dc8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005949a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594978.md#insn-005949a8) · [`005949ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594978.md#insn-005949ac) · [`005949e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594978.md#insn-005949e0)
- 新版 [`00594cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594c98.md#insn-00594cc8) · [`00594ccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594c98.md#insn-00594ccc) · [`00594d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594c98.md#insn-00594d00)

~~~diff
- 005949a8 ["COPY", "register:4048:8", ["const:c6d000:8"]]
+ 00594cc8 ["COPY", "register:4048:8", ["const:c6e000:8"]]
- 005949a8 bytes c93600b0
+ 00594cc8 bytes c93600d0
- 005949ac ["COPY", "tmp:0:8", ["const:628:8"]]
- 005949ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005949ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005949ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00594ccc ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 00594ccc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00594ccc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00594ccc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005949ac bytes 29a11891
+ 00594ccc bytes 29e11791
- 005949e0 ["INT_ADD", "register:40f0:8", ["const:5949e0:8", "const:4:8"]]
- 005949e0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00594d00 ["INT_ADD", "register:40f0:8", ["const:594d00:8", "const:4:8"]]
+ 00594d00 ["CALL", null, ["callee:00c58f30:8"]]
- 005949e0 bytes 600d1b94
+ 00594d00 bytes 8c101b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d74dd166a78a1807f1fa31451c8b950"></a>

### [`00594bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594bac.md) → [`00594ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594ecc.md) FUN_00594ecc

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00594978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594978.md) · 呼出先 12件 [`0055f504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f504.md) [`0055f56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f56c.md) [`0055f580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f580.md) [`0055f5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055f5a0.md) [`005951d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005951d0.md)
- 新版 呼出元 1件 [`00594c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594c98.md) · 呼出先 12件 [`0055f824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055f/0055f824.md) [`0055f88c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055f/0055f88c.md) [`0055f8a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055f/0055f8a0.md) [`0055f8c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0055f/0055f8c0.md) [`005954f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/005954f0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.23% / 新版 97.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00595054",
      "incomplete_value": true,
      "site": "00595064",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bda:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594d34",
      "incomplete_value": true,
      "site": "00594d44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b03:8"
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
      "00595054",
      "READ",
      [
        "storage",
        "002afb03",
        null,
        "string"
      ]
    ],
    [
      "00595058",
      "READ",
      [
        "storage",
        "002afb0e",
        null,
        "string"
      ]
    ],
    [
      "0059505c",
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
      "00595054",
      "READ",
      [
        "storage",
        "002afbda",
        null,
        "string"
      ]
    ],
    [
      "00595058",
      "READ",
      [
        "storage",
        "002afbe5",
        null,
        "string"
      ]
    ],
    [
      "0059505c",
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

- 旧版 [`00594c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594bac.md#insn-00594c00) · [`00594c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594bac.md#insn-00594c1c) · [`00594c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594bac.md#insn-00594c3c)
- 新版 [`00594f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594ecc.md#insn-00594f20) · [`00594f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594ecc.md#insn-00594f3c) · [`00594f5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00594/00594ecc.md#insn-00594f5c)

~~~diff
- 00594c00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00594c00 ["INT_ADD", "register:40f0:8", ["const:594c00:8", "const:4:8"]]
- 00594c00 ["CALLIND", null, ["register:0:8"]]
+ 00594f20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00594f20 ["INT_ADD", "register:40f0:8", ["const:594f20:8", "const:4:8"]]
+ 00594f20 ["CALLIND", null, ["register:0:8"]]
- 00594c00 bytes 00013fd6
+ 00594f20 bytes 00013fd6
- 00594c1c ["COPY", "register:0:8", ["register:4048:8"]]
- 00594c1c ["INT_ADD", "register:40f0:8", ["const:594c1c:8", "const:4:8"]]
- 00594c1c ["CALLIND", null, ["register:0:8"]]
+ 00594f3c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00594f3c ["INT_ADD", "register:40f0:8", ["const:594f3c:8", "const:4:8"]]
+ 00594f3c ["CALLIND", null, ["register:0:8"]]
- 00594c1c bytes 20013fd6
+ 00594f3c bytes 20013fd6
- 00594c3c ["INT_ADD", "register:40f0:8", ["const:594c3c:8", "const:4:8"]]
- 00594c3c ["CALL", null, ["callee:0055f824:8"]]
+ 00594f5c ["INT_ADD", "register:40f0:8", ["const:594f5c:8", "const:4:8"]]
+ 00594f5c ["CALL", null, ["callee:0055f824:8"]]
- 00594c3c bytes 322aff97
+ 00594f5c bytes 322aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ca1ea81b64dc353078e5ee2d43c322e"></a>

### [`00594ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594ff8.md) → [`00595318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595318.md) FUN_00595318

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005885dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/005885dc.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`005888fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00588/005888fc.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00595330",
      "incomplete_value": false,
      "site": "00595334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595010",
      "incomplete_value": false,
      "site": "00595014",
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
            "const:628:8"
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
      "00595334",
      "DATA",
      [
        "storage",
        "00c6d628",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00595334",
      "DATA",
      [
        "storage",
        "00c6e5f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059500c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594ff8.md#insn-0059500c) · [`00595010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594ff8.md#insn-00595010) · [`00595020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594ff8.md#insn-00595020)
- 新版 [`0059532c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595318.md#insn-0059532c) · [`00595330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595318.md#insn-00595330) · [`00595340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595318.md#insn-00595340)

~~~diff
- 0059500c ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059532c ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059500c bytes c8360090
+ 0059532c bytes c83600b0
- 00595010 ["COPY", "tmp:0:8", ["const:628:8"]]
- 00595010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00595010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00595010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00595330 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 00595330 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00595330 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00595330 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00595010 bytes 08a11891
+ 00595330 bytes 08e11791
- 00595020 ["INT_ADD", "register:40f0:8", ["const:595020:8", "const:4:8"]]
- 00595020 ["CALL", null, ["callee:00c58f50:8"]]
+ 00595340 ["INT_ADD", "register:40f0:8", ["const:595340:8", "const:4:8"]]
+ 00595340 ["CALL", null, ["callee:00c58f50:8"]]
- 00595020 bytes d80b1b94
+ 00595340 bytes 040f1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e8195e9555601b9079c495fa4cef414"></a>

### [`005953ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005953ac.md) → [`005956cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/005956cc.md) FUN_005956cc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.98% / 新版 93.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005957a4",
      "incomplete_value": false,
      "site": "005957a8",
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
            "const:77a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595484",
      "incomplete_value": false,
      "site": "00595488",
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
            "const:622:8"
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
      "definition_site": "005957d4",
      "incomplete_value": false,
      "site": "005957d8",
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
      "definition_site": "005954b4",
      "incomplete_value": false,
      "site": "005954b8",
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
      "00595744",
      "PARAM",
      [
        "storage",
        "002ae69e",
        null,
        null
      ]
    ],
    [
      "00595744",
      "PARAM",
      [
        "storage",
        "0029ede0",
        null,
        "string"
      ]
    ],
    [
      "005957a4",
      "PARAM",
      [
        "storage",
        "002a7622",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00595744",
      "PARAM",
      [
        "storage",
        "002ae76b",
        null,
        null
      ]
    ],
    [
      "00595744",
      "PARAM",
      [
        "storage",
        "0029ee20",
        null,
        "string"
      ]
    ],
    [
      "005957a4",
      "PARAM",
      [
        "storage",
        "002a777a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00595488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005953ac.md#insn-00595488) · [`005954b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005953ac.md#insn-005954b8) · [`00595410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005953ac.md#insn-00595410)
- 新版 [`005957a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/005956cc.md#insn-005957a8) · [`005957d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/005956cc.md#insn-005957d8) · [`00595730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/005956cc.md#insn-00595730)

~~~diff
- 00595488 ["INT_ADD", "register:40f0:8", ["const:595488:8", "const:4:8"]]
- 00595488 ["CALL", null, ["callee:00c59080:8"]]
+ 005957a8 ["INT_ADD", "register:40f0:8", ["const:5957a8:8", "const:4:8"]]
+ 005957a8 ["CALL", null, ["callee:00c59080:8"]]
- 00595488 bytes 0a0b1b94
+ 005957a8 bytes 360e1b94
- 005954b8 ["INT_ADD", "register:40f0:8", ["const:5954b8:8", "const:4:8"]]
- 005954b8 ["CALL", null, ["callee:00c59080:8"]]
+ 005957d8 ["INT_ADD", "register:40f0:8", ["const:5957d8:8", "const:4:8"]]
+ 005957d8 ["CALL", null, ["callee:00c59080:8"]]
- 005954b8 bytes fe0a1b94
+ 005957d8 bytes 2a0e1b94
- 00595410 ["COPY", "tmp:0:8", ["const:69e:8"]]
- 00595410 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00595410 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00595410 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00595730 ["COPY", "tmp:0:8", ["const:76b:8"]]
+ 00595730 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00595730 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00595730 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00595410 bytes 29791a91
+ 00595730 bytes 29ad1d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-332f64854bb9e6a237f74113ba824a7b"></a>

### [`005955c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005955c0.md) → [`005958e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/005958e0.md) FUN_005958e0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00596d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md) · 呼出先 2件 [`005956cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005956cc.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 1件 [`00597070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597070.md) · 呼出先 2件 [`005959ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/005959ec.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

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
      "definition_site": "005958f4",
      "incomplete_value": false,
      "site": "005958fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005955d4",
      "incomplete_value": false,
      "site": "005955dc",
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
            "const:6b8:8"
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
      "005958fc",
      "DATA",
      [
        "storage",
        "00c6d6b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005958fc",
      "DATA",
      [
        "storage",
        "00c6e688",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005955d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005955c0.md#insn-005955d0) · [`005955d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005955c0.md#insn-005955d4) · [`00595604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005955c0.md#insn-00595604)
- 新版 [`005958f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/005958e0.md#insn-005958f0) · [`005958f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/005958e0.md#insn-005958f4) · [`00595924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/005958e0.md#insn-00595924)

~~~diff
- 005955d0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 005958f0 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005955d0 bytes c8360090
+ 005958f0 bytes c83600b0
- 005955d4 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 005955d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005955d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005955d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005958f4 ["COPY", "tmp:0:8", ["const:688:8"]]
+ 005958f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005958f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005958f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005955d4 bytes 08e11a91
+ 005958f4 bytes 08211a91
- 00595604 ["INT_ADD", "register:40f0:8", ["const:595604:8", "const:4:8"]]
- 00595604 ["CALL", null, ["callee:00c54d60:8"]]
+ 00595924 ["INT_ADD", "register:40f0:8", ["const:595924:8", "const:4:8"]]
+ 00595924 ["CALL", null, ["callee:00c54d60:8"]]
- 00595604 bytes dbf91a94
+ 00595924 bytes 0ffd1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-102ee9b92eeb938f2f62bc946b614031"></a>

### [`005956cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005956cc.md) → [`005959ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/005959ec.md) FUN_005959ec

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005955c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005955c0.md) · 呼出先 4件 [`005958b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005958b0.md) [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md) [`00595d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`005958e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/005958e0.md) · 呼出先 4件 [`00595bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595bd0.md) [`00595d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595d3c.md) [`0059607c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/0059607c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00595a40",
      "incomplete_value": false,
      "site": "00595a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595720",
      "incomplete_value": false,
      "site": "00595724",
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
            "const:748:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00595a94",
      "incomplete_value": false,
      "site": "00595a98",
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
      "definition_site": "00595774",
      "incomplete_value": false,
      "site": "00595778",
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
      "00595a44",
      "DATA",
      [
        "storage",
        "00c6d748",
        null,
        "pointer"
      ]
    ],
    [
      "00595a98",
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
      "00595a44",
      "DATA",
      [
        "storage",
        "00c6e718",
        null,
        "pointer"
      ]
    ],
    [
      "00595a98",
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

- 旧版 [`005956e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005956cc.md#insn-005956e8) · [`00595708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005956cc.md#insn-00595708) · [`0059571c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005956cc.md#insn-0059571c)
- 新版 [`00595a08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/005959ec.md#insn-00595a08) · [`00595a28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/005959ec.md#insn-00595a28) · [`00595a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/005959ec.md#insn-00595a3c)

~~~diff
- 005956e8 ["INT_ADD", "register:40f0:8", ["const:5956e8:8", "const:4:8"]]
- 005956e8 ["CALL", null, ["callee:00595bd0:8"]]
+ 00595a08 ["INT_ADD", "register:40f0:8", ["const:595a08:8", "const:4:8"]]
+ 00595a08 ["CALL", null, ["callee:00595bd0:8"]]
- 005956e8 bytes 72000094
+ 00595a08 bytes 72000094
- 00595708 ["INT_ADD", "register:40f0:8", ["const:595708:8", "const:4:8"]]
- 00595708 ["CALL", null, ["callee:00c58f30:8"]]
+ 00595a28 ["INT_ADD", "register:40f0:8", ["const:595a28:8", "const:4:8"]]
+ 00595a28 ["CALL", null, ["callee:00c58f30:8"]]
- 00595708 bytes 160a1b94
+ 00595a28 bytes 420d1b94
- 0059571c ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00595a3c ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059571c bytes c8360090
+ 00595a3c bytes c83600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c591f604b59b820517fb84099c7f8a1"></a>

### [`005957c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005957c4.md) → [`00595ae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595ae4.md) FUN_00595ae4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

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
      "definition_site": "00595afc",
      "incomplete_value": false,
      "site": "00595b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005957dc",
      "incomplete_value": false,
      "site": "005957e4",
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
            "const:6b8:8"
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
      "00595b04",
      "DATA",
      [
        "storage",
        "00c6d6b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00595b04",
      "DATA",
      [
        "storage",
        "00c6e688",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005957d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005957c4.md#insn-005957d8) · [`005957dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005957c4.md#insn-005957dc) · [`005957f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005957c4.md#insn-005957f4)
- 新版 [`00595af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595ae4.md#insn-00595af8) · [`00595afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595ae4.md#insn-00595afc) · [`00595b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595ae4.md#insn-00595b14)

~~~diff
- 005957d8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00595af8 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005957d8 bytes c8360090
+ 00595af8 bytes c83600b0
- 005957dc ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 005957dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005957dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005957dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00595afc ["COPY", "tmp:0:8", ["const:688:8"]]
+ 00595afc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00595afc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00595afc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005957dc bytes 08e11a91
+ 00595afc bytes 08211a91
- 005957f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005957f4 ["INT_ADD", "register:40f0:8", ["const:5957f4:8", "const:4:8"]]
- 005957f4 ["CALLIND", null, ["register:0:8"]]
+ 00595b14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00595b14 ["INT_ADD", "register:40f0:8", ["const:595b14:8", "const:4:8"]]
+ 00595b14 ["CALLIND", null, ["register:0:8"]]
- 005957f4 bytes 00013fd6
+ 00595b14 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f91de271477ed143612d983d66cb2e1e"></a>

### [`0059583c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/0059583c.md) → [`00595b5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595b5c.md) FUN_00595b5c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00595b74",
      "incomplete_value": false,
      "site": "00595b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595854",
      "incomplete_value": false,
      "site": "0059585c",
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
            "const:6b8:8"
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
      "00595b7c",
      "DATA",
      [
        "storage",
        "00c6d6b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00595b7c",
      "DATA",
      [
        "storage",
        "00c6e688",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00595850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/0059583c.md#insn-00595850) · [`00595854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/0059583c.md#insn-00595854) · [`0059586c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/0059583c.md#insn-0059586c)
- 新版 [`00595b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595b5c.md#insn-00595b70) · [`00595b74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595b5c.md#insn-00595b74) · [`00595b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595b5c.md#insn-00595b8c)

~~~diff
- 00595850 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00595b70 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00595850 bytes c8360090
+ 00595b70 bytes c83600b0
- 00595854 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 00595854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00595854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00595854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00595b74 ["COPY", "tmp:0:8", ["const:688:8"]]
+ 00595b74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00595b74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00595b74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00595854 bytes 08e11a91
+ 00595b74 bytes 08211a91
- 0059586c ["COPY", "register:0:8", ["register:4040:8"]]
- 0059586c ["INT_ADD", "register:40f0:8", ["const:59586c:8", "const:4:8"]]
- 0059586c ["CALLIND", null, ["register:0:8"]]
+ 00595b8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00595b8c ["INT_ADD", "register:40f0:8", ["const:595b8c:8", "const:4:8"]]
+ 00595b8c ["CALLIND", null, ["register:0:8"]]
- 0059586c bytes 00013fd6
+ 00595b8c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdbcaeb8ec2f94c279e5530c9e6a8319"></a>

### [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md) → [`00595d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595d3c.md) FUN_00595d3c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005956cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005956cc.md) [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md) [`00595d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md) · 呼出先 13件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`0045be38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be38.md) [`005958b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005958b0.md) [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md)
- 新版 呼出元 3件 [`005959ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/005959ec.md) [`00595d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595d3c.md) [`0059607c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/0059607c.md) · 呼出先 13件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00459830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459830.md) [`0045c158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c158.md) [`00595bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595bd0.md) [`00595d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595d3c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.88% / 新版 95.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00595dd4",
      "incomplete_value": false,
      "site": "00595dd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595ab4",
      "incomplete_value": false,
      "site": "00595ab8",
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
            "const:748:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00595e68",
      "incomplete_value": false,
      "site": "00595e6c",
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
      "definition_site": "00595b48",
      "incomplete_value": false,
      "site": "00595b4c",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00595ff8",
      "incomplete_value": true,
      "site": "00595ffc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:388:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595cd8",
      "incomplete_value": true,
      "site": "00595cdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
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
      "00595dd8",
      "DATA",
      [
        "storage",
        "00c6d748",
        null,
        "pointer"
      ]
    ],
    [
      "00595e6c",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ],
    [
      "00595fbc",
      "READ",
      [
        "storage",
        "00c63bb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00595dd8",
      "DATA",
      [
        "storage",
        "00c6e718",
        null,
        "pointer"
      ]
    ],
    [
      "00595e6c",
      "DATA",
      [
        "storage",
        "00c64b80",
        null,
        "pointer"
      ]
    ],
    [
      "00595fbc",
      "READ",
      [
        "storage",
        "00c64b88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00595cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md#insn-00595cdc) · [`00595a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md#insn-00595a40) · [`00595a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md#insn-00595a60)
- 新版 [`00595ffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595d3c.md#insn-00595ffc) · [`00595d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595d3c.md#insn-00595d60) · [`00595d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595d3c.md#insn-00595d80)

~~~diff
- 00595cdc ["INT_ADD", "register:40f0:8", ["const:595cdc:8", "const:4:8"]]
- 00595cdc ["CALL", null, ["callee:00459830:8"]]
+ 00595ffc ["INT_ADD", "register:40f0:8", ["const:595ffc:8", "const:4:8"]]
+ 00595ffc ["CALL", null, ["callee:00459830:8"]]
- 00595cdc bytes 0d0efb97
+ 00595ffc bytes 0d0efb97
- 00595a40 ["INT_ADD", "register:40f0:8", ["const:595a40:8", "const:4:8"]]
- 00595a40 ["CALL", null, ["callee:00595bd0:8"]]
+ 00595d60 ["INT_ADD", "register:40f0:8", ["const:595d60:8", "const:4:8"]]
+ 00595d60 ["CALL", null, ["callee:00595bd0:8"]]
- 00595a40 bytes 9cffff97
+ 00595d60 bytes 9cffff97
- 00595a60 ["INT_ADD", "register:40f0:8", ["const:595a60:8", "const:4:8"]]
- 00595a60 ["CALL", null, ["callee:00595bd0:8"]]
+ 00595d80 ["INT_ADD", "register:40f0:8", ["const:595d80:8", "const:4:8"]]
+ 00595d80 ["CALL", null, ["callee:00595bd0:8"]]
- 00595a60 bytes 94ffff97
+ 00595d80 bytes 94ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d061c81b0528665f5aea36420a3243a"></a>

### [`00595d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md) → [`0059607c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/0059607c.md) FUN_0059607c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`005956cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005956cc.md) [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md) [`00595d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md) · 呼出先 15件 [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00459b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459b10.md) [`0045be38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be38.md) [`005958b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005958b0.md) [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md)
- 新版 呼出元 3件 [`005959ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/005959ec.md) [`00595d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595d3c.md) [`0059607c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/0059607c.md) · 呼出先 15件 [`00459830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459830.md) [`00459e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459e30.md) [`0045c158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045c158.md) [`00595bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595bd0.md) [`00595d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595d3c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.46% / 新版 93.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00596344",
      "incomplete_value": true,
      "site": "00596348",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:388:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596024",
      "incomplete_value": true,
      "site": "00596028",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
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
      "definition_site": "0059639c",
      "incomplete_value": false,
      "site": "005963a0",
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
            "const:7f2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059607c",
      "incomplete_value": false,
      "site": "00596080",
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
            "const:69a:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005963b0",
      "incomplete_value": true,
      "site": "005963b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:388:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596090",
      "incomplete_value": true,
      "site": "00596094",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
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
      "0059615c",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ],
    [
      "005961e0",
      "DATA",
      [
        "storage",
        "00c6d748",
        null,
        "pointer"
      ]
    ],
    [
      "005962a4",
      "READ",
      [
        "storage",
        "00c63bb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059615c",
      "DATA",
      [
        "storage",
        "00c64b80",
        null,
        "pointer"
      ]
    ],
    [
      "005961e0",
      "DATA",
      [
        "storage",
        "00c6e718",
        null,
        "pointer"
      ]
    ],
    [
      "005962a4",
      "READ",
      [
        "storage",
        "00c64b88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00596028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md#insn-00596028) · [`00596080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md#insn-00596080) · [`00596094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md#insn-00596094)
- 新版 [`00596348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/0059607c.md#insn-00596348) · [`005963a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/0059607c.md#insn-005963a0) · [`005963b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/0059607c.md#insn-005963b4)

~~~diff
- 00596028 ["INT_ADD", "register:40f0:8", ["const:596028:8", "const:4:8"]]
- 00596028 ["CALL", null, ["callee:00459830:8"]]
+ 00596348 ["INT_ADD", "register:40f0:8", ["const:596348:8", "const:4:8"]]
+ 00596348 ["CALL", null, ["callee:00459830:8"]]
- 00596028 bytes 3a0dfb97
+ 00596348 bytes 3a0dfb97
- 00596080 ["INT_ADD", "register:40f0:8", ["const:596080:8", "const:4:8"]]
- 00596080 ["CALL", null, ["callee:00c59080:8"]]
+ 005963a0 ["INT_ADD", "register:40f0:8", ["const:5963a0:8", "const:4:8"]]
+ 005963a0 ["CALL", null, ["callee:00c59080:8"]]
- 00596080 bytes 0c081b94
+ 005963a0 bytes 380b1b94
- 00596094 ["INT_ADD", "register:40f0:8", ["const:596094:8", "const:4:8"]]
- 00596094 ["CALL", null, ["callee:00459830:8"]]
+ 005963b4 ["INT_ADD", "register:40f0:8", ["const:5963b4:8", "const:4:8"]]
+ 005963b4 ["CALL", null, ["callee:00459830:8"]]
- 00596094 bytes 1f0dfb97
+ 005963b4 bytes 1f0dfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adfaf68ae31fea74171d181b27af37d3"></a>

### [`00596134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596134.md) → [`00596454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/00596454.md) FUN_00596454

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md) [`00595d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md) · 呼出先 3件 [`005964e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/005964e4.md) [`00596878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596878.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`00595d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595d3c.md) [`0059607c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/0059607c.md) · 呼出先 3件 [`00596804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/00596804.md) [`00596b98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/00596b98.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005964b8",
      "incomplete_value": false,
      "site": "005964c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596198",
      "incomplete_value": false,
      "site": "005961a0",
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
            "const:6d8:8"
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
      "definition_site": "005964e0",
      "incomplete_value": false,
      "site": "005964e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005961c0",
      "incomplete_value": false,
      "site": "005961c8",
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
            "const:6d8:8"
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
      "005964c0",
      "DATA",
      [
        "storage",
        "00c6d6d8",
        null,
        "pointer"
      ]
    ],
    [
      "005964e8",
      "DATA",
      [
        "storage",
        "00c6d6d8",
        null,
        "pointer"
      ]
    ],
    [
      "00596514",
      "DATA",
      [
        "storage",
        "00c6d6d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005964c0",
      "DATA",
      [
        "storage",
        "00c6e6a8",
        null,
        "pointer"
      ]
    ],
    [
      "005964e8",
      "DATA",
      [
        "storage",
        "00c6e6a8",
        null,
        "pointer"
      ]
    ],
    [
      "00596514",
      "DATA",
      [
        "storage",
        "00c6e6a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00596190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596134.md#insn-00596190) · [`00596194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596134.md#insn-00596194) · [`00596198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596134.md#insn-00596198)
- 新版 [`005964b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/00596454.md#insn-005964b0) · [`005964b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/00596454.md#insn-005964b4) · [`005964b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/00596454.md#insn-005964b8)

~~~diff
- 00596190 ["INT_ADD", "register:40f0:8", ["const:596190:8", "const:4:8"]]
- 00596190 ["CALL", null, ["callee:00c58f30:8"]]
+ 005964b0 ["INT_ADD", "register:40f0:8", ["const:5964b0:8", "const:4:8"]]
+ 005964b0 ["CALL", null, ["callee:00c58f30:8"]]
- 00596190 bytes 74071b94
+ 005964b0 bytes a00a1b94
- 00596194 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 005964b4 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00596194 bytes a83600f0
+ 005964b4 bytes c8360090
- 00596198 ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 00596198 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00596198 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00596198 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005964b8 ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 005964b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005964b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005964b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00596198 bytes 08611b91
+ 005964b8 bytes 08a11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c513b21f80bb3889fa33de94c3885d0b"></a>

### [`005964e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/005964e4.md) → [`00596804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/00596804.md) FUN_00596804

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00596134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596134.md) · 呼出先 12件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00596454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/00596454.md) · 呼出先 12件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.73% / 新版 95.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00596954",
      "incomplete_value": false,
      "site": "00596958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596634",
      "incomplete_value": false,
      "site": "00596638",
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
            "const:6d8:8"
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
      "definition_site": "005969f4",
      "incomplete_value": false,
      "site": "005969f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005966d4",
      "incomplete_value": false,
      "site": "005966d8",
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
            "const:6d8:8"
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
      "definition_site": "00596af4",
      "incomplete_value": false,
      "site": "00596afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005967d4",
      "incomplete_value": false,
      "site": "005967dc",
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
            "const:6d8:8"
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
      "005968e8",
      "PARAM",
      [
        "storage",
        "002b8f0b",
        null,
        null
      ]
    ],
    [
      "00596914",
      "PARAM",
      [
        "storage",
        "002b8f0b",
        null,
        null
      ]
    ],
    [
      "00596958",
      "DATA",
      [
        "storage",
        "00c6d6d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005968e8",
      "PARAM",
      [
        "storage",
        "002b8fda",
        null,
        null
      ]
    ],
    [
      "00596914",
      "PARAM",
      [
        "storage",
        "002b8fda",
        null,
        null
      ]
    ],
    [
      "00596958",
      "DATA",
      [
        "storage",
        "00c6e6a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005965cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/005964e4.md#insn-005965cc) · [`00596584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/005964e4.md#insn-00596584) · [`005965a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/005964e4.md#insn-005965a4)
- 新版 [`005968ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/00596804.md#insn-005968ec) · [`005968a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/00596804.md#insn-005968a4) · [`005968c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/00596804.md#insn-005968c4)

~~~diff
- 005965cc ["INT_ADD", "register:40f0:8", ["const:5965cc:8", "const:4:8"]]
- 005965cc ["CALL", null, ["callee:00c59080:8"]]
+ 005968ec ["INT_ADD", "register:40f0:8", ["const:5968ec:8", "const:4:8"]]
+ 005968ec ["CALL", null, ["callee:00c59080:8"]]
- 005965cc bytes b9061b94
+ 005968ec bytes e5091b94
- 00596584 ["INT_ADD", "register:40f0:8", ["const:596584:8", "const:4:8"]]
- 00596584 ["CALL", null, ["callee:00c58f30:8"]]
+ 005968a4 ["INT_ADD", "register:40f0:8", ["const:5968a4:8", "const:4:8"]]
+ 005968a4 ["CALL", null, ["callee:00c58f30:8"]]
- 00596584 bytes 77061b94
+ 005968a4 bytes a3091b94
- 005965a4 ["INT_ADD", "register:40f0:8", ["const:5965a4:8", "const:4:8"]]
- 005965a4 ["CALL", null, ["callee:00c58fe0:8"]]
+ 005968c4 ["INT_ADD", "register:40f0:8", ["const:5968c4:8", "const:4:8"]]
+ 005968c4 ["CALL", null, ["callee:00c58fe0:8"]]
- 005965a4 bytes 9b061b94
+ 005968c4 bytes c7091b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f30dd0ceff4d323f4f764e4639ee85e"></a>

### [`00596878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596878.md) → [`00596b98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/00596b98.md) FUN_00596b98

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00596134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596134.md) · 呼出先 14件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00596454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/00596454.md) · 呼出先 14件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00459830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459830.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.15% / 新版 97.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00596f54",
      "incomplete_value": false,
      "site": "00596f58",
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
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596c34",
      "incomplete_value": false,
      "site": "00596c38",
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
            "const:830:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00596d0c",
      "incomplete_value": false,
      "site": "00596d18",
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
            "const:b22:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005969ec",
      "incomplete_value": false,
      "site": "005969f8",
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
            "const:a55:8"
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
      "00596bec",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ],
    [
      "00596c68",
      "PARAM",
      [
        "storage",
        "002aea55",
        null,
        null
      ]
    ],
    [
      "00596cd8",
      "PARAM",
      [
        "storage",
        "002a329e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00596bec",
      "READ",
      [
        "storage",
        "00c9c388",
        null,
        "pointer"
      ]
    ],
    [
      "00596c68",
      "PARAM",
      [
        "storage",
        "002aeb22",
        null,
        null
      ]
    ],
    [
      "00596cd8",
      "PARAM",
      [
        "storage",
        "002a3369",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005969f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596878.md#insn-005969f8) · [`005968c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596878.md#insn-005968c0) · [`005968c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596878.md#insn-005968c8)
- 新版 [`00596d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/00596b98.md#insn-00596d18) · [`00596be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/00596b98.md#insn-00596be0) · [`00596be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/00596b98.md#insn-00596be8)

~~~diff
- 005969f8 ["INT_ADD", "register:40f0:8", ["const:5969f8:8", "const:4:8"]]
- 005969f8 ["CALL", null, ["callee:00c59080:8"]]
+ 00596d18 ["INT_ADD", "register:40f0:8", ["const:596d18:8", "const:4:8"]]
+ 00596d18 ["CALL", null, ["callee:00c59080:8"]]
- 005969f8 bytes ae051b94
+ 00596d18 bytes da081b94
- 005968c0 ["COPY", "register:40a8:8", ["const:c9b000:8"]]
+ 00596be0 ["COPY", "register:40a8:8", ["const:c9c000:8"]]
- 005968c0 bytes 353800b0
+ 00596be0 bytes 353800d0
- 005968c8 ["COPY", "tmp:0:8", ["const:29e:8"]]
- 005968c8 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 005968c8 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 005968c8 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00596be8 ["COPY", "tmp:0:8", ["const:369:8"]]
+ 00596be8 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00596be8 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00596be8 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 005968c8 bytes 947a0a91
+ 00596be8 bytes 94a60d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28f166e1a7b5234abf2d26a5a9ce57e6"></a>

### [`00596d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md) → [`00597070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597070.md) FUN_00597070

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 14件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0043f95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f95c.md) [`0045a030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a030.md) [`0045a7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a7b0.md) [`0046014c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/0046014c.md) · 呼出先 5件 [`005955c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005955c0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 14件 [`0043c5b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c5b8.md) [`0043fc7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043fc7c.md) [`0045a350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a350.md) [`0045aad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aad0.md) [`0046046c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00460/0046046c.md) · 呼出先 5件 [`005958e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/005958e0.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005970c8",
      "incomplete_value": false,
      "site": "005970c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596da8",
      "incomplete_value": false,
      "site": "00596da8",
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
            "const:7a8:8"
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
      "definition_site": "005970f8",
      "incomplete_value": false,
      "site": "00597100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596dd8",
      "incomplete_value": false,
      "site": "00596de0",
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
            "const:6b8:8"
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
      "005970c8",
      "DATA",
      [
        "storage",
        "00c6d7a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00597100",
      "DATA",
      [
        "storage",
        "00c6d6b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005970c8",
      "DATA",
      [
        "storage",
        "00c6e778",
        null,
        "undefined *"
      ]
    ],
    [
      "00597100",
      "DATA",
      [
        "storage",
        "00c6e688",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00596d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md#insn-00596d84) · [`00596d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md#insn-00596d98) · [`00596d9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md#insn-00596d9c)
- 新版 [`005970a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597070.md#insn-005970a4) · [`005970b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597070.md#insn-005970b8) · [`005970bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597070.md#insn-005970bc)

~~~diff
- 00596d84 ["INT_ADD", "register:40f0:8", ["const:596d84:8", "const:4:8"]]
- 00596d84 ["CALL", null, ["callee:005958e0:8"]]
+ 005970a4 ["INT_ADD", "register:40f0:8", ["const:5970a4:8", "const:4:8"]]
+ 005970a4 ["CALL", null, ["callee:005958e0:8"]]
- 00596d84 bytes 0ffaff97
+ 005970a4 bytes 0ffaff97
- 00596d98 ["INT_ADD", "register:40f0:8", ["const:596d98:8", "const:4:8"]]
- 00596d98 ["CALL", null, ["callee:00c58f30:8"]]
+ 005970b8 ["INT_ADD", "register:40f0:8", ["const:5970b8:8", "const:4:8"]]
+ 005970b8 ["CALL", null, ["callee:00c58f30:8"]]
- 00596d98 bytes 72041b94
+ 005970b8 bytes 9e071b94
- 00596d9c ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 005970bc ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00596d9c bytes a83600f0
+ 005970bc bytes a83600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ff363df3340f65a4a93dc593d1088a4"></a>

### [`00596f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596f6c.md) → [`0059728c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059728c.md) FUN_0059728c

採用 · 移動量 `+0x320` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 42件 [`0045039c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045039c.md) [`00476b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476b90.md) [`00571320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571320.md) [`00572ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572ca8.md) [`0058570c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058570c.md) · 呼出先 6件 [`00596d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 42件 [`004506bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00450/004506bc.md) [`00476eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00476/00476eb0.md) [`00571640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00571/00571640.md) [`00572fc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00572/00572fc8.md) [`00585a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00585/00585a2c.md) · 呼出先 6件 [`00597070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597070.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005972cc",
      "incomplete_value": false,
      "site": "005972dc",
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
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596fac",
      "incomplete_value": false,
      "site": "00596fbc",
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
            "const:868:8"
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
      "definition_site": "005972d4",
      "incomplete_value": false,
      "site": "005972dc",
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
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596fb4",
      "incomplete_value": false,
      "site": "00596fbc",
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
            "const:be8:8"
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
      "005972cc",
      "PARAM",
      [
        "storage",
        "00c63868",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005972d4",
      "PARAM",
      [
        "storage",
        "00c63be8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005972cc",
      "PARAM",
      [
        "storage",
        "00c64838",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005972d4",
      "PARAM",
      [
        "storage",
        "00c64bb8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00596fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596f6c.md#insn-00596fbc) · [`00596f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596f6c.md#insn-00596f90) · [`00596fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596f6c.md#insn-00596fa8)
- 新版 [`005972dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059728c.md#insn-005972dc) · [`005972b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059728c.md#insn-005972b0) · [`005972c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059728c.md#insn-005972c8)

~~~diff
- 00596fbc ["INT_ADD", "register:40f0:8", ["const:596fbc:8", "const:4:8"]]
- 00596fbc ["CALL", null, ["callee:00c596b0:8"]]
+ 005972dc ["INT_ADD", "register:40f0:8", ["const:5972dc:8", "const:4:8"]]
+ 005972dc ["CALL", null, ["callee:00c596b0:8"]]
- 00596fbc bytes c9051b94
+ 005972dc bytes f5081b94
- 00596f90 ["INT_ADD", "register:40f0:8", ["const:596f90:8", "const:4:8"]]
- 00596f90 ["CALL", null, ["callee:00597070:8"]]
+ 005972b0 ["INT_ADD", "register:40f0:8", ["const:5972b0:8", "const:4:8"]]
+ 005972b0 ["CALL", null, ["callee:00597070:8"]]
- 00596f90 bytes 70ffff97
+ 005972b0 bytes 70ffff97
- 00596fa8 ["COPY", "register:4008:8", ["const:c63000:8"]]
+ 005972c8 ["COPY", "register:4008:8", ["const:c64000:8"]]
- 00596fa8 bytes 613600b0
+ 005972c8 bytes 613600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d1dcbc63a9c8c6ea689f2e145dc2445"></a>

### [`0059705c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059705c.md) → [`0059737c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059737c.md) FUN_0059737c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00496a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00496/00496a9c.md) [`00765e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765e74.md) · 呼出先 6件 [`00596e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596e5c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`00496dbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00496/00496dbc.md) [`00766250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00766/00766250.md) · 呼出先 6件 [`0059717c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059717c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005973bc",
      "incomplete_value": false,
      "site": "005973cc",
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
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059709c",
      "incomplete_value": false,
      "site": "005970ac",
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
            "const:868:8"
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
      "definition_site": "005973c4",
      "incomplete_value": false,
      "site": "005973cc",
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
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005970a4",
      "incomplete_value": false,
      "site": "005970ac",
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
            "const:be8:8"
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
      "005973bc",
      "PARAM",
      [
        "storage",
        "00c63868",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005973c4",
      "PARAM",
      [
        "storage",
        "00c63be8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005973bc",
      "PARAM",
      [
        "storage",
        "00c64838",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005973c4",
      "PARAM",
      [
        "storage",
        "00c64bb8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005970ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059705c.md#insn-005970ac) · [`00597080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059705c.md#insn-00597080) · [`00597098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059705c.md#insn-00597098)
- 新版 [`005973cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059737c.md#insn-005973cc) · [`005973a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059737c.md#insn-005973a0) · [`005973b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059737c.md#insn-005973b8)

~~~diff
- 005970ac ["INT_ADD", "register:40f0:8", ["const:5970ac:8", "const:4:8"]]
- 005970ac ["CALL", null, ["callee:00c596b0:8"]]
+ 005973cc ["INT_ADD", "register:40f0:8", ["const:5973cc:8", "const:4:8"]]
+ 005973cc ["CALL", null, ["callee:00c596b0:8"]]
- 005970ac bytes 8d051b94
+ 005973cc bytes b9081b94
- 00597080 ["INT_ADD", "register:40f0:8", ["const:597080:8", "const:4:8"]]
- 00597080 ["CALL", null, ["callee:0059717c:8"]]
+ 005973a0 ["INT_ADD", "register:40f0:8", ["const:5973a0:8", "const:4:8"]]
+ 005973a0 ["CALL", null, ["callee:0059717c:8"]]
- 00597080 bytes 77ffff97
+ 005973a0 bytes 77ffff97
- 00597098 ["COPY", "register:4008:8", ["const:c63000:8"]]
+ 005973b8 ["COPY", "register:4008:8", ["const:c64000:8"]]
- 00597098 bytes 61360090
+ 005973b8 bytes 613600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d45bec800ae7a2074944eb1ef291a74"></a>

### [`00597154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597154.md) → [`00597474`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597474.md) FUN_00597474

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0059748c",
      "incomplete_value": false,
      "site": "00597490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059716c",
      "incomplete_value": false,
      "site": "00597170",
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
            "const:748:8"
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
      "00597490",
      "DATA",
      [
        "storage",
        "00c6d748",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00597490",
      "DATA",
      [
        "storage",
        "00c6e718",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00597168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597154.md#insn-00597168) · [`0059716c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597154.md#insn-0059716c) · [`005971ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597154.md#insn-005971ac)
- 新版 [`00597488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597474.md#insn-00597488) · [`0059748c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597474.md#insn-0059748c) · [`005974cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597474.md#insn-005974cc)

~~~diff
- 00597168 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00597488 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00597168 bytes a83600d0
+ 00597488 bytes a83600f0
- 0059716c ["COPY", "tmp:0:8", ["const:748:8"]]
- 0059716c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059716c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059716c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059748c ["COPY", "tmp:0:8", ["const:718:8"]]
+ 0059748c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059748c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059748c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059716c bytes 08211d91
+ 0059748c bytes 08611c91
- 005971ac ["COPY", "register:0:8", ["register:4040:8"]]
- 005971ac ["INT_ADD", "register:40f0:8", ["const:5971ac:8", "const:4:8"]]
- 005971ac ["CALLIND", null, ["register:0:8"]]
+ 005974cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005974cc ["INT_ADD", "register:40f0:8", ["const:5974cc:8", "const:4:8"]]
+ 005974cc ["CALLIND", null, ["register:0:8"]]
- 005971ac bytes 00013fd6
+ 005974cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-638564fb5b6e61413ce6b8a756a6b941"></a>

### [`005971dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005971dc.md) → [`005974fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005974fc.md) FUN_005974fc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md) [`00595d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md) [`005a14b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a14b0.md) [`00765e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00765/00765e74.md) [`00798ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798ef8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 6件 [`00595d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595d3c.md) [`0059607c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00596/0059607c.md) [`005a17d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a1/005a17d0.md) [`00766250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00766/00766250.md) [`007992d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00799/007992d4.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00597518",
      "incomplete_value": false,
      "site": "0059751c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005971f8",
      "incomplete_value": false,
      "site": "005971fc",
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
            "const:748:8"
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
      "0059751c",
      "DATA",
      [
        "storage",
        "00c6d748",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059751c",
      "DATA",
      [
        "storage",
        "00c6e718",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005971f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005971dc.md#insn-005971f4) · [`005971f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005971dc.md#insn-005971f8) · [`00597234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005971dc.md#insn-00597234)
- 新版 [`00597514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005974fc.md#insn-00597514) · [`00597518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005974fc.md#insn-00597518) · [`00597554`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/005974fc.md#insn-00597554)

~~~diff
- 005971f4 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00597514 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005971f4 bytes a83600d0
+ 00597514 bytes a83600f0
- 005971f8 ["COPY", "tmp:0:8", ["const:748:8"]]
- 005971f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005971f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005971f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00597518 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 00597518 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00597518 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00597518 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005971f8 bytes 08211d91
+ 00597518 bytes 08611c91
- 00597234 ["COPY", "register:0:8", ["register:4040:8"]]
- 00597234 ["INT_ADD", "register:40f0:8", ["const:597234:8", "const:4:8"]]
- 00597234 ["CALLIND", null, ["register:0:8"]]
+ 00597554 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00597554 ["INT_ADD", "register:40f0:8", ["const:597554:8", "const:4:8"]]
+ 00597554 ["CALLIND", null, ["register:0:8"]]
- 00597234 bytes 00013fd6
+ 00597554 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfab012e97d1475a13aed475e25af42a"></a>

### [`0059725c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059725c.md) → [`0059757c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059757c.md) FUN_0059757c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md) [`00597544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597544.md) [`00767074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767074.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 3件 [`00595d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00595/00595d3c.md) [`00597864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597864.md) [`00767450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00767/00767450.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00597588",
      "incomplete_value": false,
      "site": "0059758c",
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
      "definition_site": "00597268",
      "incomplete_value": false,
      "site": "0059726c",
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
      "00597588",
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
      "00597588",
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

- 旧版 [`0059726c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059725c.md#insn-0059726c) · [`00597264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059725c.md#insn-00597264) · [`00597268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059725c.md#insn-00597268)
- 新版 [`0059758c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059757c.md#insn-0059758c) · [`00597584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059757c.md#insn-00597584) · [`00597588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059757c.md#insn-00597588)

~~~diff
- 0059726c ["INT_ADD", "register:40f0:8", ["const:59726c:8", "const:4:8"]]
- 0059726c ["CALL", null, ["callee:0043bad8:8"]]
+ 0059758c ["INT_ADD", "register:40f0:8", ["const:59758c:8", "const:4:8"]]
+ 0059758c ["CALL", null, ["callee:0043bad8:8"]]
- 0059726c bytes 5391fa97
+ 0059758c bytes 5391fa97
- 00597264 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00597584 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00597264 bytes 00e9ff90
+ 00597584 bytes 00e9ffb0
- 00597268 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00597268 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00597268 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00597268 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00597588 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00597588 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00597588 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00597588 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00597268 bytes 00303e91
+ 00597588 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82280396c94adb63c6412c3719ff36cb"></a>

### [`00597920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597920.md) → [`00597c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597c40.md) FUN_00597c40

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005977fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005977fc.md) · 呼出先 8件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58350.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 1件 [`00597b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597b1c.md) · 呼出先 8件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md) [`00c59320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59320.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00597ca8",
      "incomplete_value": true,
      "site": "00597cac",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:390:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597988",
      "incomplete_value": true,
      "site": "0059798c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:3c0:8"
              ]
            ]
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
      "00597ca8",
      "READ",
      [
        "storage",
        "00c9b3c0",
        null,
        "pointer"
      ]
    ],
    [
      "00597ca8",
      "PARAM",
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
      "00597ca8",
      "READ",
      [
        "storage",
        "00c9c390",
        null,
        "pointer"
      ]
    ],
    [
      "00597ca8",
      "PARAM",
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

- 旧版 [`0059798c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597920.md#insn-0059798c) · [`0059795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597920.md#insn-0059795c) · [`0059797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597920.md#insn-0059797c)
- 新版 [`00597cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597c40.md#insn-00597cac) · [`00597c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597c40.md#insn-00597c7c) · [`00597c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597c40.md#insn-00597c9c)

~~~diff
- 0059798c ["INT_ADD", "register:40f0:8", ["const:59798c:8", "const:4:8"]]
- 0059798c ["CALL", null, ["callee:00c59320:8"]]
+ 00597cac ["INT_ADD", "register:40f0:8", ["const:597cac:8", "const:4:8"]]
+ 00597cac ["CALL", null, ["callee:00c59320:8"]]
- 0059798c bytes 71021b94
+ 00597cac bytes 9d051b94
- 0059795c ["INT_ADD", "register:40f0:8", ["const:59795c:8", "const:4:8"]]
- 0059795c ["CALL", null, ["callee:00c5ae70:8"]]
+ 00597c7c ["INT_ADD", "register:40f0:8", ["const:597c7c:8", "const:4:8"]]
+ 00597c7c ["CALL", null, ["callee:00c5ae70:8"]]
- 0059795c bytes 51091b94
+ 00597c7c bytes 7d0c1b94
- 0059797c ["INT_ADD", "register:40f0:8", ["const:59797c:8", "const:4:8"]]
- 0059797c ["CALL", null, ["callee:00c59310:8"]]
+ 00597c9c ["INT_ADD", "register:40f0:8", ["const:597c9c:8", "const:4:8"]]
+ 00597c9c ["CALL", null, ["callee:00c59310:8"]]
- 0059797c bytes 71021b94
+ 00597c9c bytes 9d051b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2076c64b95453585a5d74ab2460bc457"></a>

### [`00597ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597ad4.md) → [`00597df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597df4.md) FUN_00597df4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00579564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00579/00579564.md) [`009bad54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ba/009bad54.md) · 呼出先 9件 [`00597c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597c80.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md) [`00c58080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58080.md)
- 新版 呼出元 2件 [`00579884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00579/00579884.md) [`009bbd00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009bb/009bbd00.md) · 呼出先 9件 [`00597fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597fa0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59040.md) [`00c59050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59050.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00597eac",
      "incomplete_value": true,
      "site": "00597eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00597b8c",
      "incomplete_value": true,
      "site": "00597b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00597e28",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00597e2c",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "00597e44",
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
      "00597e28",
      "READ",
      [
        "storage",
        "00c9bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00597e2c",
      "READ",
      [
        "storage",
        "00c9bc58",
        null,
        "pointer"
      ]
    ],
    [
      "00597e44",
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

- 旧版 [`00597af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597ad4.md#insn-00597af8) · [`00597afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597ad4.md#insn-00597afc) · [`00597b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597ad4.md#insn-00597b08)
- 新版 [`00597e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597df4.md#insn-00597e18) · [`00597e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597df4.md#insn-00597e1c) · [`00597e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597df4.md#insn-00597e28)

~~~diff
- 00597af8 ["COPY", "register:40d0:8", ["const:c9a000:8"]]
+ 00597e18 ["COPY", "register:40d0:8", ["const:c9b000:8"]]
- 00597af8 bytes 1a3800f0
+ 00597e18 bytes 3a380090
- 00597afc ["COPY", "register:40c8:8", ["const:c9a000:8"]]
+ 00597e1c ["COPY", "register:40c8:8", ["const:c9b000:8"]]
- 00597afc bytes 193800f0
+ 00597e1c bytes 39380090
- 00597b08 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:d58:8"]]
- 00597b08 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00597e28 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:d28:8"]]
+ 00597e28 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00597b08 bytes 5aaf46f9
+ 00597e28 bytes 5a9746f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c359c01ba534b6d28b50fa5a77fd217a"></a>

### [`00597c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597c80.md) → [`00597fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597fa0.md) FUN_00597fa0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597ad4.md) · 呼出先 9件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58330.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58350.md)
- 新版 呼出元 1件 [`00597df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597df4.md) · 呼出先 9件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c59300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59300.md) [`00c59310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59310.md) [`00c59320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59320.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00598000",
      "incomplete_value": true,
      "site": "00598004",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00597ce0",
      "incomplete_value": true,
      "site": "00597ce4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00598044",
      "incomplete_value": true,
      "site": "00598048",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00597d24",
      "incomplete_value": true,
      "site": "00597d28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00598000",
      "READ",
      [
        "storage",
        "00c9b3c8",
        null,
        "pointer"
      ]
    ],
    [
      "00598000",
      "PARAM",
      [
        "storage",
        "01127cd8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00598044",
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
      "00598000",
      "READ",
      [
        "storage",
        "00c9c398",
        null,
        "pointer"
      ]
    ],
    [
      "00598000",
      "PARAM",
      [
        "storage",
        "01128c98",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00598044",
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

- 旧版 [`00597ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597c80.md#insn-00597ce4) · [`00597d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597c80.md#insn-00597d28) · [`00597cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597c80.md#insn-00597cb8)
- 新版 [`00598004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597fa0.md#insn-00598004) · [`00598048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597fa0.md#insn-00598048) · [`00597fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597fa0.md#insn-00597fd8)

~~~diff
- 00597ce4 ["INT_ADD", "register:40f0:8", ["const:597ce4:8", "const:4:8"]]
- 00597ce4 ["CALL", null, ["callee:00c59320:8"]]
+ 00598004 ["INT_ADD", "register:40f0:8", ["const:598004:8", "const:4:8"]]
+ 00598004 ["CALL", null, ["callee:00c59320:8"]]
- 00597ce4 bytes 9b011b94
+ 00598004 bytes c7041b94
- 00597d28 ["INT_ADD", "register:40f0:8", ["const:597d28:8", "const:4:8"]]
- 00597d28 ["CALL", null, ["callee:00c59320:8"]]
+ 00598048 ["INT_ADD", "register:40f0:8", ["const:598048:8", "const:4:8"]]
+ 00598048 ["CALL", null, ["callee:00c59320:8"]]
- 00597d28 bytes 8a011b94
+ 00598048 bytes b6041b94
- 00597cb8 ["INT_ADD", "register:40f0:8", ["const:597cb8:8", "const:4:8"]]
- 00597cb8 ["CALL", null, ["callee:00c59300:8"]]
+ 00597fd8 ["INT_ADD", "register:40f0:8", ["const:597fd8:8", "const:4:8"]]
+ 00597fd8 ["CALL", null, ["callee:00c59300:8"]]
- 00597cb8 bytes 9e011b94
+ 00597fd8 bytes ca041b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1524c091a302ff1e011d4b5f28881cbf"></a>

### [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) → [`00598230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598230.md) FUN_00598230

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 18件 [`005aca50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005aca50.md) [`005b71c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b71c4.md) [`005b77ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b77ec.md) [`005b7d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7d38.md) [`005b811c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b811c.md) · 呼出先 0件 
- 新版 呼出元 18件 [`005ace00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ac/005ace00.md) [`005b7574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7574.md) [`005b7b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b7b9c.md) [`005b80e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b80e8.md) [`005b84cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b8/005b84cc.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00598238",
      "incomplete_value": false,
      "site": "0059823c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597f18",
      "incomplete_value": false,
      "site": "00597f1c",
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
            "const:7f8:8"
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
      "0059823c",
      "DATA",
      [
        "storage",
        "00c6d7f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059823c",
      "DATA",
      [
        "storage",
        "00c6e7c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00597f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md#insn-00597f14) · [`00597f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md#insn-00597f18)
- 新版 [`00598234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598230.md#insn-00598234) · [`00598238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598230.md#insn-00598238)

~~~diff
- 00597f14 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 00598234 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00597f14 bytes a83600d0
+ 00598234 bytes a83600d0
- 00597f18 ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 00597f18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00597f18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00597f18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00598238 ["COPY", "tmp:0:8", ["const:7c8:8"]]
+ 00598238 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00598238 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00598238 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00597f18 bytes 08e11f91
+ 00598238 bytes 08211f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4687697eab1cf1a35951014ec62fb706"></a>

### [`00597f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f3c.md) → [`0059825c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/0059825c.md) FUN_0059825c

採用 · 移動量 `+0x320` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00598e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598e00.md) [`0059929c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/0059929c.md) [`005aca84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005aca84.md) [`005acf00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005acf00.md) · 呼出先 24件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`0044ff9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044ff9c.md) [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md)
- 新版 呼出元 4件 [`00599120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599120.md) [`005995bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/005995bc.md) [`005ace34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ac/005ace34.md) [`005ad2b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ad/005ad2b0.md) · 呼出先 24件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`004502bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00450/004502bc.md) [`00451c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00451/00451c10.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.96% / 新版 92.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `store_destination` 1件, `store_value` 8件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00598704",
      "incomplete_value": true,
      "site": "0059870c",
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
      "definition_site": "005983e4",
      "incomplete_value": true,
      "site": "005983ec",
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
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00598714",
      "incomplete_value": true,
      "site": "00598714",
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
                "const:f0:8"
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
      "definition_site": "005983f4",
      "incomplete_value": true,
      "site": "005983f4",
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
                "const:f0:8"
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
    "ordinal": 45,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00598714",
      "incomplete_value": true,
      "site": "00598714",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005983f4",
      "incomplete_value": true,
      "site": "005983f4",
      "value": [
        "LOAD",
        "8",
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
      "005982fc",
      "READ",
      [
        "storage",
        "00c9b3d0",
        null,
        "pointer"
      ]
    ],
    [
      "0059830c",
      "READ",
      [
        "storage",
        "00ca66d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00598318",
      "READ",
      [
        "storage",
        "00ca66d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005982fc",
      "READ",
      [
        "storage",
        "00c9c3a0",
        null,
        "pointer"
      ]
    ],
    [
      "0059830c",
      "READ",
      [
        "storage",
        "00ca7690",
        null,
        "undefined1"
      ]
    ],
    [
      "00598318",
      "READ",
      [
        "storage",
        "00ca7698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00598078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f3c.md#insn-00598078) · [`00598088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f3c.md#insn-00598088) · [`005980d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f3c.md#insn-005980d4)
- 新版 [`00598398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/0059825c.md#insn-00598398) · [`005983a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/0059825c.md#insn-005983a8) · [`005983f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/0059825c.md#insn-005983f4)

~~~diff
- 00598078 ["INT_ADD", "register:40f0:8", ["const:598078:8", "const:4:8"]]
- 00598078 ["CALL", null, ["callee:00c59150:8"]]
+ 00598398 ["INT_ADD", "register:40f0:8", ["const:598398:8", "const:4:8"]]
+ 00598398 ["CALL", null, ["callee:00c59150:8"]]
- 00598078 bytes 42001b94
+ 00598398 bytes 6e031b94
- 00598088 ["INT_ADD", "register:40f0:8", ["const:598088:8", "const:4:8"]]
- 00598088 ["CALL", null, ["callee:00c59010:8"]]
+ 005983a8 ["INT_ADD", "register:40f0:8", ["const:5983a8:8", "const:4:8"]]
+ 005983a8 ["CALL", null, ["callee:00c59010:8"]]
- 00598088 bytes eeff1a94
+ 005983a8 bytes 1a031b94
- 005980d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005980d4 ["INT_ADD", "register:40f0:8", ["const:5980d4:8", "const:4:8"]]
- 005980d4 ["CALLIND", null, ["register:0:8"]]
+ 005983f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005983f4 ["INT_ADD", "register:40f0:8", ["const:5983f4:8", "const:4:8"]]
+ 005983f4 ["CALLIND", null, ["register:0:8"]]
- 005980d4 bytes 20013fd6
+ 005983f4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66c92a5f1ce331bedd5e15967059a2a9"></a>

### [`00598b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b7c.md) → [`00598e9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598e9c.md) FUN_00598e9c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) · 呼出先 3件 [`0059a208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a208.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00598e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598e94.md) · 呼出先 3件 [`0059a528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a528.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.85% / 新版 97.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00598f3c",
      "incomplete_value": false,
      "site": "00598f40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00598c1c",
      "incomplete_value": false,
      "site": "00598c20",
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
            "const:860:8"
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
      "00598f40",
      "DATA",
      [
        "storage",
        "00c6d860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00598f40",
      "DATA",
      [
        "storage",
        "00c6e830",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00598bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b7c.md#insn-00598bbc) · [`00598bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b7c.md#insn-00598bf8) · [`00598c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b7c.md#insn-00598c0c)
- 新版 [`00598edc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598e9c.md#insn-00598edc) · [`00598f18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598e9c.md#insn-00598f18) · [`00598f2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598e9c.md#insn-00598f2c)

~~~diff
- 00598bbc ["COPY", "register:0:8", ["register:4048:8"]]
- 00598bbc ["INT_ADD", "register:40f0:8", ["const:598bbc:8", "const:4:8"]]
- 00598bbc ["CALLIND", null, ["register:0:8"]]
+ 00598edc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00598edc ["INT_ADD", "register:40f0:8", ["const:598edc:8", "const:4:8"]]
+ 00598edc ["CALLIND", null, ["register:0:8"]]
- 00598bbc bytes 20013fd6
+ 00598edc bytes 20013fd6
- 00598bf8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00598bf8 ["INT_ADD", "register:40f0:8", ["const:598bf8:8", "const:4:8"]]
- 00598bf8 ["CALLIND", null, ["register:0:8"]]
+ 00598f18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00598f18 ["INT_ADD", "register:40f0:8", ["const:598f18:8", "const:4:8"]]
+ 00598f18 ["CALLIND", null, ["register:0:8"]]
- 00598bf8 bytes 00013fd6
+ 00598f18 bytes 00013fd6
- 00598c0c ["INT_ADD", "register:40f0:8", ["const:598c0c:8", "const:4:8"]]
- 00598c0c ["CALL", null, ["callee:00c58f30:8"]]
+ 00598f2c ["INT_ADD", "register:40f0:8", ["const:598f2c:8", "const:4:8"]]
+ 00598f2c ["CALL", null, ["callee:00c58f30:8"]]
- 00598c0c bytes d5fc1a94
+ 00598f2c bytes 01001b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26f88cde8d1bb27f6b237fcd558cdc87"></a>

### [`00598e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598e00.md) → [`00599120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599120.md) FUN_00599120

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00597f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f3c.md) [`0059925c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/0059925c.md) [`0059a4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a4d8.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0059825c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/0059825c.md) [`0059957c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/0059957c.md) [`0059a7f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a7f8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00599340",
      "incomplete_value": false,
      "site": "00599340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599020",
      "incomplete_value": false,
      "site": "00599020",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00599224",
      "PARAM",
      [
        "storage",
        "00ca6688",
        null,
        "undefined1"
      ]
    ],
    [
      "00599340",
      "DATA",
      [
        "storage",
        "00c6d950",
        null,
        "undefined *"
      ]
    ],
    [
      "005993b0",
      "READ",
      [
        "storage",
        "00c6d978",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00599224",
      "PARAM",
      [
        "storage",
        "00ca7648",
        null,
        "undefined1"
      ]
    ],
    [
      "00599340",
      "DATA",
      [
        "storage",
        "00c6e920",
        null,
        "undefined *"
      ]
    ],
    [
      "005993b0",
      "READ",
      [
        "storage",
        "00c6e948",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00598e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598e00.md#insn-00598e2c) · [`00598e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598e00.md#insn-00598e4c) · [`00598e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598e00.md#insn-00598e60)
- 新版 [`0059914c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599120.md#insn-0059914c) · [`0059916c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599120.md#insn-0059916c) · [`00599180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599120.md#insn-00599180)

~~~diff
- 00598e2c ["INT_ADD", "register:40f0:8", ["const:598e2c:8", "const:4:8"]]
- 00598e2c ["CALL", null, ["callee:0059825c:8"]]
+ 0059914c ["INT_ADD", "register:40f0:8", ["const:59914c:8", "const:4:8"]]
+ 0059914c ["CALL", null, ["callee:0059825c:8"]]
- 00598e2c bytes 44fcff97
+ 0059914c bytes 44fcff97
- 00598e4c ["INT_ADD", "register:40f0:8", ["const:598e4c:8", "const:4:8"]]
- 00598e4c ["CALL", null, ["callee:00c54d90:8"]]
+ 0059916c ["INT_ADD", "register:40f0:8", ["const:59916c:8", "const:4:8"]]
+ 0059916c ["CALL", null, ["callee:00c54d90:8"]]
- 00598e4c bytes d5eb1a94
+ 0059916c bytes 09ef1a94
- 00598e60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00598e60 ["INT_ADD", "register:40f0:8", ["const:598e60:8", "const:4:8"]]
- 00598e60 ["CALLIND", null, ["register:0:8"]]
+ 00599180 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599180 ["INT_ADD", "register:40f0:8", ["const:599180:8", "const:4:8"]]
+ 00599180 ["CALLIND", null, ["register:0:8"]]
- 00598e60 bytes 00013fd6
+ 00599180 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65ac8d8eb9380cd6cc0803180fa1744e"></a>

### [`0059929c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/0059929c.md) → [`005995bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/005995bc.md) FUN_005995bc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00597f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f3c.md) [`0059adf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059adf8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0059825c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/0059825c.md) [`0059b118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059b/0059b118.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.06% / 新版 98.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00599784",
      "incomplete_value": false,
      "site": "0059978c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599464",
      "incomplete_value": false,
      "site": "0059946c",
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
            "const:9d0:8"
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
      "definition_site": "00599678",
      "incomplete_value": false,
      "site": "00599680",
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
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599358",
      "incomplete_value": false,
      "site": "00599360",
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
            "const:688:8"
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
      "00599678",
      "PARAM",
      [
        "storage",
        "00ca6688",
        null,
        "undefined1"
      ]
    ],
    [
      "0059978c",
      "DATA",
      [
        "storage",
        "00c6d9d0",
        null,
        "undefined *"
      ]
    ],
    [
      "00599818",
      "READ",
      [
        "storage",
        "00c6d9f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00599678",
      "PARAM",
      [
        "storage",
        "00ca7648",
        null,
        "undefined1"
      ]
    ],
    [
      "0059978c",
      "DATA",
      [
        "storage",
        "00c6e9a0",
        null,
        "undefined *"
      ]
    ],
    [
      "00599818",
      "READ",
      [
        "storage",
        "00c6e9c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00599360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/0059929c.md#insn-00599360) · [`005992cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/0059929c.md#insn-005992cc) · [`005992ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/0059929c.md#insn-005992ec)
- 新版 [`00599680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/005995bc.md#insn-00599680) · [`005995ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/005995bc.md#insn-005995ec) · [`0059960c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/005995bc.md#insn-0059960c)

~~~diff
- 00599360 ["INT_ADD", "register:40f0:8", ["const:599360:8", "const:4:8"]]
- 00599360 ["CALL", null, ["callee:004413ec:8"]]
+ 00599680 ["INT_ADD", "register:40f0:8", ["const:599680:8", "const:4:8"]]
+ 00599680 ["CALL", null, ["callee:004413ec:8"]]
- 00599360 bytes 5b9ffa97
+ 00599680 bytes 5b9ffa97
- 005992cc ["INT_ADD", "register:40f0:8", ["const:5992cc:8", "const:4:8"]]
- 005992cc ["CALL", null, ["callee:0059825c:8"]]
+ 005995ec ["INT_ADD", "register:40f0:8", ["const:5995ec:8", "const:4:8"]]
+ 005995ec ["CALL", null, ["callee:0059825c:8"]]
- 005992cc bytes 1cfbff97
+ 005995ec bytes 1cfbff97
- 005992ec ["INT_ADD", "register:40f0:8", ["const:5992ec:8", "const:4:8"]]
- 005992ec ["CALL", null, ["callee:00c54d90:8"]]
+ 0059960c ["INT_ADD", "register:40f0:8", ["const:59960c:8", "const:4:8"]]
+ 0059960c ["CALL", null, ["callee:00c54d90:8"]]
- 005992ec bytes adea1a94
+ 0059960c bytes e1ed1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b6bf402484925e203ba48a24901bd0d"></a>

### [`005996f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/005996f4.md) → [`00599a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599a14.md) FUN_00599a14

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0059a748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a748.md) [`0059ae58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059ae58.md) · 呼出先 6件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00599844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599844.md) [`0076911c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/0076911c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md)
- 新版 呼出元 2件 [`0059aa68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059aa68.md) [`0059b178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059b/0059b178.md) · 呼出先 6件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`00599b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599b64.md) [`007694f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/007694f8.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00a1b6a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a1b/00a1b6a4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00599a3c",
      "incomplete_value": false,
      "site": "00599a4c",
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
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059971c",
      "incomplete_value": false,
      "site": "0059972c",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00599a94",
      "value": [
        "leaf",
        "ram:7694f8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00599774",
      "value": [
        "leaf",
        "ram:76911c:8"
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
      "00599a3c",
      "PARAM",
      [
        "storage",
        "00ca6670",
        null,
        "undefined1"
      ]
    ],
    [
      "00599a94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0076911c"
      ]
    ]
  ],
  "added": [
    [
      "00599a3c",
      "PARAM",
      [
        "storage",
        "00ca7630",
        null,
        "undefined1"
      ]
    ],
    [
      "00599a94",
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

- 旧版 [`0059972c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/005996f4.md#insn-0059972c) · [`00599774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/005996f4.md#insn-00599774) · [`00599718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/005996f4.md#insn-00599718)
- 新版 [`00599a4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599a14.md#insn-00599a4c) · [`00599a94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599a14.md#insn-00599a94) · [`00599a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599a14.md#insn-00599a38)

~~~diff
- 0059972c ["INT_ADD", "register:40f0:8", ["const:59972c:8", "const:4:8"]]
- 0059972c ["CALL", null, ["callee:004413ec:8"]]
+ 00599a4c ["INT_ADD", "register:40f0:8", ["const:599a4c:8", "const:4:8"]]
+ 00599a4c ["CALL", null, ["callee:004413ec:8"]]
- 0059972c bytes 689efa97
+ 00599a4c bytes 689efa97
- 00599774 ["INT_ADD", "register:40f0:8", ["const:599774:8", "const:4:8"]]
- 00599774 ["CALL", null, ["ram:76911c:8"]]
+ 00599a94 ["INT_ADD", "register:40f0:8", ["const:599a94:8", "const:4:8"]]
+ 00599a94 ["CALL", null, ["ram:7694f8:8"]]
- 00599774 bytes 6a3e0794
+ 00599a94 bytes 993e0794
- 00599718 ["COPY", "register:4008:8", ["const:ca6000:8"]]
+ 00599a38 ["COPY", "register:4008:8", ["const:ca7000:8"]]
- 00599718 bytes 613800b0
+ 00599a38 bytes 613800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-987f6efd103da398d5d3c62412ad7f3a"></a>

### [`00599844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599844.md) → [`00599b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599b64.md) FUN_00599b64

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005996f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/005996f4.md) · 呼出先 12件 [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`00452c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md) [`0059b380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b380.md) [`0059b3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b3d0.md) [`007643dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007643dc.md)
- 新版 呼出元 1件 [`00599a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599a14.md) · 呼出先 12件 [`0044fc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044f/0044fc40.md) [`00452fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00452/00452fb4.md) [`0059b6a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059b/0059b6a0.md) [`0059b6f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059b/0059b6f0.md) [`007647b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/007647b8.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 95.05% / 新版 95.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00599c04",
      "incomplete_value": false,
      "site": "00599c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005998e4",
      "incomplete_value": false,
      "site": "005998e4",
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
            "const:a50:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00599b90",
      "value": [
        "leaf",
        "ram:7647b8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00599870",
      "value": [
        "leaf",
        "ram:7643dc:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00599874"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00599b90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007643dc"
      ]
    ],
    [
      "unmatched:00599874",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ],
    [
      "00599b9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007685fc"
      ]
    ]
  ],
  "added": [
    [
      "00599b90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007647b8"
      ]
    ],
    [
      "00599b94",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ],
    [
      "00599b9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007689d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00599870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599844.md#insn-00599870) · [`00599874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599844.md#insn-00599874) · [`0059987c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599844.md#insn-0059987c)
- 新版 [`00599b90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599b64.md#insn-00599b90) · [`00599b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599b64.md#insn-00599b9c)

~~~diff
- 00599870 ["INT_ADD", "register:40f0:8", ["const:599870:8", "const:4:8"]]
- 00599870 ["CALL", null, ["ram:7643dc:8"]]
+ 00599b90 ["INT_ADD", "register:40f0:8", ["const:599b90:8", "const:4:8"]]
+ 00599b90 ["CALL", null, ["ram:7647b8:8"]]
- 00599870 bytes db2a0794
+ 00599b90 bytes 0a2b0794
- 00599874 ["INT_ADD", "register:40f0:8", ["const:599874:8", "const:4:8"]]
- 00599874 ["CALL", null, ["callee:008524fc:8"]]
- 00599874 bytes 37df0a94
- 0059987c ["INT_ADD", "register:40f0:8", ["const:59987c:8", "const:4:8"]]
- 0059987c ["CALL", null, ["ram:7685fc:8"]]
+ 00599b9c ["INT_ADD", "register:40f0:8", ["const:599b9c:8", "const:4:8"]]
+ 00599b9c ["CALL", null, ["ram:7689d8:8"]]
- 0059987c bytes 603b0794
+ 00599b9c bytes 8f3b0794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a947fa5f794dd1634db469f8af875175"></a>

### [`00599ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599ab4.md) → [`00599dd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599dd4.md) FUN_00599dd4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0059a748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a748.md) [`0059ae58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059ae58.md) · 呼出先 4件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 2件 [`0059aa68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059aa68.md) [`0059b178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059b/0059b178.md) · 呼出先 4件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.28% / 新版 98.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00599e08",
      "incomplete_value": false,
      "site": "00599e18",
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
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599ae8",
      "incomplete_value": false,
      "site": "00599af8",
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
            "const:688:8"
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
      "definition_site": "00599e7c",
      "incomplete_value": false,
      "site": "00599e84",
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
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599b5c",
      "incomplete_value": false,
      "site": "00599b64",
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
            "const:670:8"
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
      "00599e08",
      "PARAM",
      [
        "storage",
        "00ca6688",
        null,
        "undefined1"
      ]
    ],
    [
      "00599e7c",
      "PARAM",
      [
        "storage",
        "00ca6670",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00599e08",
      "PARAM",
      [
        "storage",
        "00ca7648",
        null,
        "undefined1"
      ]
    ],
    [
      "00599e7c",
      "PARAM",
      [
        "storage",
        "00ca7630",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00599af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599ab4.md#insn-00599af8) · [`00599b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599ab4.md#insn-00599b64) · [`00599ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599ab4.md#insn-00599ae4)
- 新版 [`00599e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599dd4.md#insn-00599e18) · [`00599e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599dd4.md#insn-00599e84) · [`00599e04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599dd4.md#insn-00599e04)

~~~diff
- 00599af8 ["INT_ADD", "register:40f0:8", ["const:599af8:8", "const:4:8"]]
- 00599af8 ["CALL", null, ["callee:004413ec:8"]]
+ 00599e18 ["INT_ADD", "register:40f0:8", ["const:599e18:8", "const:4:8"]]
+ 00599e18 ["CALL", null, ["callee:004413ec:8"]]
- 00599af8 bytes 759dfa97
+ 00599e18 bytes 759dfa97
- 00599b64 ["INT_ADD", "register:40f0:8", ["const:599b64:8", "const:4:8"]]
- 00599b64 ["CALL", null, ["callee:004413ec:8"]]
+ 00599e84 ["INT_ADD", "register:40f0:8", ["const:599e84:8", "const:4:8"]]
+ 00599e84 ["CALL", null, ["callee:004413ec:8"]]
- 00599b64 bytes 5a9dfa97
+ 00599e84 bytes 5a9dfa97
- 00599ae4 ["COPY", "register:4008:8", ["const:ca6000:8"]]
+ 00599e04 ["COPY", "register:4008:8", ["const:ca7000:8"]]
- 00599ae4 bytes 613800b0
+ 00599e04 bytes 613800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdff8c2e65492ad7d8d1a963015f8649"></a>

### [`00599e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599e94.md) → [`0059a1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a1b4.md) FUN_0059a1b4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00599f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599f78.md) [`005ad4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad4c4.md) [`005ad550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad550.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 3件 [`0059a298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a298.md) [`005ad874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ad/005ad874.md) [`005ad900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ad/005ad900.md) · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.49% / 新版 96.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059a1cc",
      "incomplete_value": false,
      "site": "0059a1d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599eac",
      "incomplete_value": false,
      "site": "00599eb0",
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
            "const:7f8:8"
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
      "0059a1d0",
      "DATA",
      [
        "storage",
        "00c6d7f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a1d0",
      "DATA",
      [
        "storage",
        "00c6e7c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00599ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599e94.md#insn-00599ea8) · [`00599eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599e94.md#insn-00599eac) · [`00599ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599e94.md#insn-00599ec0)
- 新版 [`0059a1c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a1b4.md#insn-0059a1c8) · [`0059a1cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a1b4.md#insn-0059a1cc) · [`0059a1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a1b4.md#insn-0059a1e0)

~~~diff
- 00599ea8 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059a1c8 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00599ea8 bytes a8360090
+ 0059a1c8 bytes a8360090
- 00599eac ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 00599eac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00599eac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00599eac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059a1cc ["COPY", "tmp:0:8", ["const:7c8:8"]]
+ 0059a1cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059a1cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059a1cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00599eac bytes 08e11f91
+ 0059a1cc bytes 08211f91
- 00599ec0 ["INT_ADD", "register:40f0:8", ["const:599ec0:8", "const:4:8"]]
- 00599ec0 ["CALL", null, ["callee:00c54d90:8"]]
+ 0059a1e0 ["INT_ADD", "register:40f0:8", ["const:59a1e0:8", "const:4:8"]]
+ 0059a1e0 ["CALL", null, ["callee:00c54d90:8"]]
- 00599ec0 bytes b8e71a94
+ 0059a1e0 bytes ecea1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce79781d88c89ad6dad23989316c6385"></a>

### [`00599f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599f9c.md) → [`0059a2bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a2bc.md) FUN_0059a2bc

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
      "definition_site": "0059a2c8",
      "incomplete_value": false,
      "site": "0059a2d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599fa8",
      "incomplete_value": false,
      "site": "00599fb4",
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
            "const:860:8"
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
      "0059a2d4",
      "DATA",
      [
        "storage",
        "00c6d860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a2d4",
      "DATA",
      [
        "storage",
        "00c6e830",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00599fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599f9c.md#insn-00599fa4) · [`00599fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599f9c.md#insn-00599fa8)
- 新版 [`0059a2c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a2bc.md#insn-0059a2c4) · [`0059a2c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a2bc.md#insn-0059a2c8)

~~~diff
- 00599fa4 ["COPY", "register:4050:8", ["const:c6d000:8"]]
+ 0059a2c4 ["COPY", "register:4050:8", ["const:c6e000:8"]]
- 00599fa4 bytes aa360090
+ 0059a2c4 bytes aa360090
- 00599fa8 ["COPY", "tmp:0:8", ["const:860:8"]]
- 00599fa8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00599fa8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00599fa8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059a2c8 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 0059a2c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059a2c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059a2c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00599fa8 bytes 4a812191
+ 0059a2c8 bytes 4ac12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cea1bfa1bd7859514e8a846e149ba12f"></a>

### [`00599fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599fe0.md) → [`0059a300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a300.md) FUN_0059a300

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
      "definition_site": "0059a318",
      "incomplete_value": false,
      "site": "0059a324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599ff8",
      "incomplete_value": false,
      "site": "0059a004",
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
            "const:860:8"
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
      "0059a324",
      "DATA",
      [
        "storage",
        "00c6d860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a324",
      "DATA",
      [
        "storage",
        "00c6e830",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00599ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599fe0.md#insn-00599ff4) · [`00599ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599fe0.md#insn-00599ff8) · [`0059a028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599fe0.md#insn-0059a028)
- 新版 [`0059a314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a300.md#insn-0059a314) · [`0059a318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a300.md#insn-0059a318) · [`0059a348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a300.md#insn-0059a348)

~~~diff
- 00599ff4 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059a314 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 00599ff4 bytes a8360090
+ 0059a314 bytes a8360090
- 00599ff8 ["COPY", "tmp:0:8", ["const:860:8"]]
- 00599ff8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00599ff8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00599ff8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059a318 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 0059a318 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059a318 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059a318 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00599ff8 bytes 08812191
+ 0059a318 bytes 08c12091
- 0059a028 ["COPY", "register:0:8", ["register:4040:8"]]
- 0059a028 ["INT_ADD", "register:40f0:8", ["const:59a028:8", "const:4:8"]]
- 0059a028 ["CALLIND", null, ["register:0:8"]]
+ 0059a348 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a348 ["INT_ADD", "register:40f0:8", ["const:59a348:8", "const:4:8"]]
+ 0059a348 ["CALLIND", null, ["register:0:8"]]
- 0059a028 bytes 00013fd6
+ 0059a348 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4003a5c2c9cbcf278cff3c4ceb5e0bb5"></a>

### [`0059a03c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a03c.md) → [`0059a35c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a35c.md) FUN_0059a35c

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
      "definition_site": "0059a388",
      "incomplete_value": false,
      "site": "0059a388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a068",
      "incomplete_value": false,
      "site": "0059a068",
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
            "const:860:8"
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
      "0059a388",
      "DATA",
      [
        "storage",
        "00c6d860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a388",
      "DATA",
      [
        "storage",
        "00c6e830",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059a050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a03c.md#insn-0059a050) · [`0059a05c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a03c.md#insn-0059a05c) · [`0059a060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a03c.md#insn-0059a060)
- 新版 [`0059a370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a35c.md#insn-0059a370) · [`0059a37c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a35c.md#insn-0059a37c) · [`0059a380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a35c.md#insn-0059a380)

~~~diff
- 0059a050 ["INT_ADD", "register:40f0:8", ["const:59a050:8", "const:4:8"]]
- 0059a050 ["CALL", null, ["callee:00c58f30:8"]]
+ 0059a370 ["INT_ADD", "register:40f0:8", ["const:59a370:8", "const:4:8"]]
+ 0059a370 ["CALL", null, ["callee:00c58f30:8"]]
- 0059a050 bytes c4f71a94
+ 0059a370 bytes f0fa1a94
- 0059a05c ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0059a37c ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0059a05c bytes 883600f0
+ 0059a37c bytes a8360090
- 0059a060 ["COPY", "tmp:0:8", ["const:860:8"]]
- 0059a060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059a060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059a060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059a380 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 0059a380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059a380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059a380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059a060 bytes 08812191
+ 0059a380 bytes 08c12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba42e9905481a561d521c8a292c49841"></a>

### [`0059a0c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a0c4.md) → [`0059a3e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a3e4.md) FUN_0059a3e4

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
      "definition_site": "0059a400",
      "incomplete_value": false,
      "site": "0059a400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a0e0",
      "incomplete_value": false,
      "site": "0059a0e0",
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
            "const:860:8"
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
      "0059a400",
      "DATA",
      [
        "storage",
        "00c6d860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a400",
      "DATA",
      [
        "storage",
        "00c6e830",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059a0d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a0c4.md#insn-0059a0d8) · [`0059a0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a0c4.md#insn-0059a0dc) · [`0059a100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a0c4.md#insn-0059a100)
- 新版 [`0059a3f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a3e4.md#insn-0059a3f8) · [`0059a3fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a3e4.md#insn-0059a3fc) · [`0059a420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a3e4.md#insn-0059a420)

~~~diff
- 0059a0d8 ["COPY", "register:4048:8", ["const:c6d000:8"]]
+ 0059a3f8 ["COPY", "register:4048:8", ["const:c6e000:8"]]
- 0059a0d8 bytes 893600f0
+ 0059a3f8 bytes a9360090
- 0059a0dc ["COPY", "tmp:0:8", ["const:860:8"]]
- 0059a0dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059a0dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059a0dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059a3fc ["COPY", "tmp:0:8", ["const:830:8"]]
+ 0059a3fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a3fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a3fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059a0dc bytes 29812191
+ 0059a3fc bytes 29c12091
- 0059a100 ["COPY", "register:0:8", ["register:4048:8"]]
- 0059a100 ["INT_ADD", "register:40f0:8", ["const:59a100:8", "const:4:8"]]
- 0059a100 ["CALLIND", null, ["register:0:8"]]
+ 0059a420 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0059a420 ["INT_ADD", "register:40f0:8", ["const:59a420:8", "const:4:8"]]
+ 0059a420 ["CALLIND", null, ["register:0:8"]]
- 0059a100 bytes 20013fd6
+ 0059a420 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-932f7a832b60c8489ed1e03b73d16cad"></a>

### [`0059a4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a4d8.md) → [`0059a7f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a7f8.md) FUN_0059a7f8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00598e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598e00.md) [`005aca84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005aca84.md) · 呼出先 3件 [`00bf0470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0470.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 2件 [`00599120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599120.md) [`005ace34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ac/005ace34.md) · 呼出先 3件 [`00bf1464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1464.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059a818",
      "incomplete_value": true,
      "site": "0059a81c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0059a4f8",
      "incomplete_value": true,
      "site": "0059a4fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0059a820",
      "incomplete_value": true,
      "site": "0059a828",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a500",
      "incomplete_value": true,
      "site": "0059a508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3e0:8"
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
      "definition_site": "0059a824",
      "incomplete_value": true,
      "site": "0059a828",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a504",
      "incomplete_value": true,
      "site": "0059a508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3e8:8"
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
      "0059a814",
      "READ",
      [
        "storage",
        "00c9b3d8",
        null,
        "pointer"
      ]
    ],
    [
      "0059a81c",
      "DATA",
      [
        "storage",
        "00c92ad8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "0059a820",
      "READ",
      [
        "storage",
        "00c9b3e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059a814",
      "READ",
      [
        "storage",
        "00c9c3a8",
        null,
        "pointer"
      ]
    ],
    [
      "0059a81c",
      "DATA",
      [
        "storage",
        "00c93aa8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "0059a820",
      "READ",
      [
        "storage",
        "00c9c3b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059a508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a4d8.md#insn-0059a508) · [`0059a4e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a4d8.md#insn-0059a4e4) · [`0059a4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a4d8.md#insn-0059a4e8)
- 新版 [`0059a828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a7f8.md#insn-0059a828) · [`0059a804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a7f8.md#insn-0059a804) · [`0059a808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a7f8.md#insn-0059a808)

~~~diff
- 0059a508 ["INT_ADD", "register:40f0:8", ["const:59a508:8", "const:4:8"]]
- 0059a508 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0059a828 ["INT_ADD", "register:40f0:8", ["const:59a828:8", "const:4:8"]]
+ 0059a828 ["CALL", null, ["callee:00c58fb0:8"]]
- 0059a508 bytes b6f61a94
+ 0059a828 bytes e2f91a94
- 0059a4e4 ["INT_ADD", "register:40f0:8", ["const:59a4e4:8", "const:4:8"]]
- 0059a4e4 ["CALL", null, ["callee:00c58f90:8"]]
+ 0059a804 ["INT_ADD", "register:40f0:8", ["const:59a804:8", "const:4:8"]]
+ 0059a804 ["CALL", null, ["callee:00c58f90:8"]]
- 0059a4e4 bytes b7f61a94
+ 0059a804 bytes e3f91a94
- 0059a4e8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 0059a808 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 0059a4e8 bytes 083800b0
+ 0059a808 bytes 083800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8248a8f6bbef089fd225da1b1da0eb0d"></a>

### [`0059a50c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a50c.md) → [`0059a82c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a82c.md) FUN_0059a82c

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "0059a844",
      "incomplete_value": false,
      "site": "0059a848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a524",
      "incomplete_value": false,
      "site": "0059a528",
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
            "const:950:8"
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
      "0059a848",
      "DATA",
      [
        "storage",
        "00c6d950",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a848",
      "DATA",
      [
        "storage",
        "00c6e920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059a520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a50c.md#insn-0059a520) · [`0059a524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a50c.md#insn-0059a524) · [`0059a534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a50c.md#insn-0059a534)
- 新版 [`0059a840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a82c.md#insn-0059a840) · [`0059a844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a82c.md#insn-0059a844) · [`0059a854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a82c.md#insn-0059a854)

~~~diff
- 0059a520 ["COPY", "register:4048:8", ["const:c6d000:8"]]
+ 0059a840 ["COPY", "register:4048:8", ["const:c6e000:8"]]
- 0059a520 bytes 893600f0
+ 0059a840 bytes a9360090
- 0059a524 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0059a524 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059a524 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059a524 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059a844 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 0059a844 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a844 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a844 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059a524 bytes 29412591
+ 0059a844 bytes 29812491
- 0059a534 ["INT_ADD", "register:40f0:8", ["const:59a534:8", "const:4:8"]]
- 0059a534 ["CALL", null, ["callee:00c58f50:8"]]
+ 0059a854 ["INT_ADD", "register:40f0:8", ["const:59a854:8", "const:4:8"]]
+ 0059a854 ["CALL", null, ["callee:00c58f50:8"]]
- 0059a534 bytes 93f61a94
+ 0059a854 bytes bff91a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05d2f4d77edffb26d29b20ebf3fddae4"></a>

### [`0059a558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a558.md) → [`0059a878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a878.md) FUN_0059a878

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059a890",
      "incomplete_value": false,
      "site": "0059a894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a570",
      "incomplete_value": false,
      "site": "0059a574",
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
            "const:950:8"
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
      "0059a894",
      "DATA",
      [
        "storage",
        "00c6d950",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a894",
      "DATA",
      [
        "storage",
        "00c6e920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059a56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a558.md#insn-0059a56c) · [`0059a570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a558.md#insn-0059a570) · [`0059a580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a558.md#insn-0059a580)
- 新版 [`0059a88c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a878.md#insn-0059a88c) · [`0059a890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a878.md#insn-0059a890) · [`0059a8a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a878.md#insn-0059a8a0)

~~~diff
- 0059a56c ["COPY", "register:4048:8", ["const:c6d000:8"]]
+ 0059a88c ["COPY", "register:4048:8", ["const:c6e000:8"]]
- 0059a56c bytes 893600f0
+ 0059a88c bytes a9360090
- 0059a570 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0059a570 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059a570 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059a570 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059a890 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 0059a890 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a890 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a890 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059a570 bytes 29412591
+ 0059a890 bytes 29812491
- 0059a580 ["INT_ADD", "register:40f0:8", ["const:59a580:8", "const:4:8"]]
- 0059a580 ["CALL", null, ["callee:00c58f50:8"]]
+ 0059a8a0 ["INT_ADD", "register:40f0:8", ["const:59a8a0:8", "const:4:8"]]
+ 0059a8a0 ["CALL", null, ["callee:00c58f50:8"]]
- 0059a580 bytes 80f61a94
+ 0059a8a0 bytes acf91a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a49f6e5d5581630a08c28e5df1478a6b"></a>

### [`0059a5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a5a0.md) → [`0059a8c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a8c0.md) FUN_0059a8c0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0059a8e8",
      "incomplete_value": false,
      "site": "0059a8e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a5c8",
      "incomplete_value": false,
      "site": "0059a5c8",
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
            "const:950:8"
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
      "0059a8e8",
      "DATA",
      [
        "storage",
        "00c6d950",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a8e8",
      "DATA",
      [
        "storage",
        "00c6e920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059a5b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a5a0.md#insn-0059a5b4) · [`0059a5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a5a0.md#insn-0059a5c0) · [`0059a5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a5a0.md#insn-0059a5c4)
- 新版 [`0059a8d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a8c0.md#insn-0059a8d4) · [`0059a8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a8c0.md#insn-0059a8e0) · [`0059a8e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a8c0.md#insn-0059a8e4)

~~~diff
- 0059a5b4 ["INT_ADD", "register:40f0:8", ["const:59a5b4:8", "const:4:8"]]
- 0059a5b4 ["CALL", null, ["callee:00c58f30:8"]]
+ 0059a8d4 ["INT_ADD", "register:40f0:8", ["const:59a8d4:8", "const:4:8"]]
+ 0059a8d4 ["CALL", null, ["callee:00c58f30:8"]]
- 0059a5b4 bytes 6bf61a94
+ 0059a8d4 bytes 97f91a94
- 0059a5c0 ["COPY", "register:4048:8", ["const:c6d000:8"]]
+ 0059a8e0 ["COPY", "register:4048:8", ["const:c6e000:8"]]
- 0059a5c0 bytes 893600f0
+ 0059a8e0 bytes a9360090
- 0059a5c4 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0059a5c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059a5c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059a5c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059a8e4 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 0059a8e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a8e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a8e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059a5c4 bytes 29412591
+ 0059a8e4 bytes 29812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daed4ce5a8d0973a621236746a3c299c"></a>

### [`0059a640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a640.md) → [`0059a960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a960.md) FUN_0059a960

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059a980",
      "incomplete_value": false,
      "site": "0059a980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a660",
      "incomplete_value": false,
      "site": "0059a660",
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
            "const:950:8"
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
      "0059a980",
      "DATA",
      [
        "storage",
        "00c6d950",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059a980",
      "DATA",
      [
        "storage",
        "00c6e920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059a658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a640.md#insn-0059a658) · [`0059a65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a640.md#insn-0059a65c) · [`0059a674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a640.md#insn-0059a674)
- 新版 [`0059a978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a960.md#insn-0059a978) · [`0059a97c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a960.md#insn-0059a97c) · [`0059a994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059a960.md#insn-0059a994)

~~~diff
- 0059a658 ["COPY", "register:4048:8", ["const:c6d000:8"]]
+ 0059a978 ["COPY", "register:4048:8", ["const:c6e000:8"]]
- 0059a658 bytes 893600f0
+ 0059a978 bytes a9360090
- 0059a65c ["COPY", "tmp:0:8", ["const:950:8"]]
- 0059a65c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059a65c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059a65c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059a97c ["COPY", "tmp:0:8", ["const:920:8"]]
+ 0059a97c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a97c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059a97c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059a65c bytes 29412591
+ 0059a97c bytes 29812491
- 0059a674 ["INT_ADD", "register:40f0:8", ["const:59a674:8", "const:4:8"]]
- 0059a674 ["CALL", null, ["callee:00c54d60:8"]]
+ 0059a994 ["INT_ADD", "register:40f0:8", ["const:59a994:8", "const:4:8"]]
+ 0059a994 ["CALL", null, ["callee:00c54d60:8"]]
- 0059a674 bytes bfe51a94
+ 0059a994 bytes f3e81a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc77b50f9bab8cab825fdb090d034a6a"></a>

### [`0059ab78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059ab78.md) → [`0059ae98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059ae98.md) FUN_0059ae98

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059aeb0",
      "incomplete_value": false,
      "site": "0059aeb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059ab90",
      "incomplete_value": false,
      "site": "0059ab94",
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
            "const:9d0:8"
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
      "0059aeb4",
      "DATA",
      [
        "storage",
        "00c6d9d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059aeb4",
      "DATA",
      [
        "storage",
        "00c6e9a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059ab8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059ab78.md#insn-0059ab8c) · [`0059ab90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059ab78.md#insn-0059ab90) · [`0059aba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059ab78.md#insn-0059aba0)
- 新版 [`0059aeac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059ae98.md#insn-0059aeac) · [`0059aeb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059ae98.md#insn-0059aeb0) · [`0059aec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059ae98.md#insn-0059aec0)

~~~diff
- 0059ab8c ["COPY", "register:4048:8", ["const:c6d000:8"]]
+ 0059aeac ["COPY", "register:4048:8", ["const:c6e000:8"]]
- 0059ab8c bytes 893600f0
+ 0059aeac bytes a9360090
- 0059ab90 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 0059ab90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059ab90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059ab90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059aeb0 ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 0059aeb0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059aeb0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059aeb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059ab90 bytes 29412791
+ 0059aeb0 bytes 29812691
- 0059aba0 ["INT_ADD", "register:40f0:8", ["const:59aba0:8", "const:4:8"]]
- 0059aba0 ["CALL", null, ["callee:00c58f50:8"]]
+ 0059aec0 ["INT_ADD", "register:40f0:8", ["const:59aec0:8", "const:4:8"]]
+ 0059aec0 ["CALL", null, ["callee:00c58f50:8"]]
- 0059aba0 bytes f8f41a94
+ 0059aec0 bytes 24f81a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

