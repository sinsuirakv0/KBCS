# v16.0.2 → v16.0.3 · 最優先の変更候補 (50)

[一覧の目次](README.md)

<a id="compare-9b94afa99fd6bab1c7ae9bf31fe7d1f4"></a>

### [`00888e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888e74.md) → [`00889e20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889e20.md) FUN_00889e20

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00889e2c",
      "incomplete_value": false,
      "site": "00889e2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888e80",
      "incomplete_value": false,
      "site": "00888e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
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
      "00889e2c",
      "DATA",
      [
        "storage",
        "00c812c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00889e2c",
      "DATA",
      [
        "storage",
        "00c82290",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888e74.md#insn-00888e78) · [`00888e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888e74.md#insn-00888e7c)
- 新版 [`00889e24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889e20.md#insn-00889e24) · [`00889e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889e20.md#insn-00889e28)

~~~diff
- 00888e78 ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 00889e24 ["COPY", "register:4048:8", ["const:c82000:8"]]
- 00888e78 bytes c91f00b0
+ 00889e24 bytes c91f00b0
- 00888e7c ["COPY", "tmp:0:8", ["const:2c0:8"]]
- 00888e7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00888e7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00888e7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00889e28 ["COPY", "tmp:0:8", ["const:290:8"]]
+ 00889e28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00889e28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00889e28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00888e7c bytes 29010b91
+ 00889e28 bytes 29410a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20d0e19b236a5f91a4de3158af0c8ba0"></a>

### [`00889040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889040.md) → [`00889fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889fec.md) FUN_00889fec

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00889040"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00889040"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00889044"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00889040",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00889044",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00889064",
      "DATA",
      [
        "storage",
        "00c81350",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00889fec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00889ff0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0088a010",
      "DATA",
      [
        "storage",
        "00c82320",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889040.md#insn-00889040) · [`00889044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889040.md#insn-00889044) · [`00889054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889040.md#insn-00889054)
- 新版 [`0088a000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/00889fec.md#insn-0088a000)

~~~diff
- 00889040 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00889040 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00889040 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00889040 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00889040 bytes fd7bbea9
- 00889044 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00889044 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00889044 bytes f30b00f9
- 00889054 ["INT_ADD", "register:40f0:8", ["const:889054:8", "const:4:8"]]
- 00889054 ["CALL", null, ["callee:00c58f30:8"]]
+ 0088a000 ["INT_ADD", "register:40f0:8", ["const:88a000:8", "const:4:8"]]
+ 0088a000 ["CALL", null, ["callee:00c58f30:8"]]
- 00889054 bytes c33b0f94
+ 0088a000 bytes cc3b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-017d9171b45af12ca082280f3a69392a"></a>

### [`00889234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889234.md) → [`0088a1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a1e0.md) FUN_0088a1e0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088a1f4",
      "incomplete_value": false,
      "site": "0088a1f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889248",
      "incomplete_value": false,
      "site": "0088924c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
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
      "0088a1f8",
      "DATA",
      [
        "storage",
        "00c813e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088a1f8",
      "DATA",
      [
        "storage",
        "00c823b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889234.md#insn-00889240) · [`00889244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889234.md#insn-00889244) · [`00889248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889234.md#insn-00889248)
- 新版 [`0088a1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a1e0.md#insn-0088a1ec) · [`0088a1f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a1e0.md#insn-0088a1f0) · [`0088a1f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a1e0.md#insn-0088a1f4)

~~~diff
- 00889240 ["INT_ADD", "register:40f0:8", ["const:889240:8", "const:4:8"]]
- 00889240 ["CALL", null, ["callee:00c58f30:8"]]
+ 0088a1ec ["INT_ADD", "register:40f0:8", ["const:88a1ec:8", "const:4:8"]]
+ 0088a1ec ["CALL", null, ["callee:00c58f30:8"]]
- 00889240 bytes 483b0f94
+ 0088a1ec bytes 513b0f94
- 00889244 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088a1f0 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 00889244 bytes c81f0090
+ 0088a1f0 bytes c81f0090
- 00889248 ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 00889248 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00889248 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00889248 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088a1f4 ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 0088a1f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a1f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a1f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00889248 bytes 08810f91
+ 0088a1f4 bytes 08c10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-809d119e7bac00c2969c0d722d1ce53e"></a>

### [`00889258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889258.md) → [`0088a204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a204.md) FUN_0088a204

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088a208",
      "incomplete_value": false,
      "site": "0088a20c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088925c",
      "incomplete_value": false,
      "site": "00889260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
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
      "0088a20c",
      "DATA",
      [
        "storage",
        "00c813e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088a20c",
      "DATA",
      [
        "storage",
        "00c823b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889258.md#insn-00889258) · [`0088925c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889258.md#insn-0088925c)
- 新版 [`0088a204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a204.md#insn-0088a204) · [`0088a208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a204.md#insn-0088a208)

~~~diff
- 00889258 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088a204 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 00889258 bytes c81f0090
+ 0088a204 bytes c81f0090
- 0088925c ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 0088925c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088925c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088925c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088a208 ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 0088a208 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a208 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a208 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088925c bytes 08810f91
+ 0088a208 bytes 08c10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a69b3ce13d753265e6cb108013bb9f5"></a>

### [`00889270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889270.md) → [`0088a21c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a21c.md) FUN_0088a21c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0052dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md) [`0066d13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066d/0066d13c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0052e060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e060.md) [`0066d4ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0066d/0066d4ec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 90.67% / 新版 90.67%

CFGの説明率　旧版 68.75% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00889354"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008893a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008893ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0088a258",
      "READ",
      [
        "storage",
        "002a0662",
        null,
        "string"
      ]
    ],
    [
      "0088a2ac",
      "READ",
      [
        "storage",
        "002a0662",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00889340",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088a334"
      ]
    ]
  ],
  "added": [
    [
      "0088a258",
      "READ",
      [
        "storage",
        "002a06a2",
        null,
        "string"
      ]
    ],
    [
      "0088a2ac",
      "READ",
      [
        "storage",
        "002a06a2",
        null,
        "string"
      ]
    ],
    [
      "0088a2ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088a334"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889270.md#insn-00889340) · [`00889354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889270.md#insn-00889354) · [`0088936c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889270.md#insn-0088936c)

~~~diff
- 00889340 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00889340 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00889340 bytes 570200b4
- 00889354 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00889354 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:11:8"]]
- 00889354 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00889354 bytes e91301f8
- 0088936c ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 0088936c bytes e0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c36f0b85d5f24d64ba948329c2671dd3"></a>

### [`00889764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889764.md) → [`0088a710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a710.md) FUN_0088a710

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088a71c",
      "incomplete_value": false,
      "site": "0088a71c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889770",
      "incomplete_value": false,
      "site": "00889770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:460:8"
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
      "0088a71c",
      "DATA",
      [
        "storage",
        "00c81460",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088a71c",
      "DATA",
      [
        "storage",
        "00c82430",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889764.md#insn-00889768) · [`0088976c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889764.md#insn-0088976c)
- 新版 [`0088a714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a710.md#insn-0088a714) · [`0088a718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a710.md#insn-0088a718)

~~~diff
- 00889768 ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 0088a714 ["COPY", "register:4048:8", ["const:c82000:8"]]
- 00889768 bytes c91f0090
+ 0088a714 bytes c91f0090
- 0088976c ["COPY", "tmp:0:8", ["const:460:8"]]
- 0088976c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088976c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088976c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088a718 ["COPY", "tmp:0:8", ["const:430:8"]]
+ 0088a718 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088a718 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088a718 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088976c bytes 29811191
+ 0088a718 bytes 29c11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c38da30e32236a00523e21783575414"></a>

### [`00889780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889780.md) → [`0088a72c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a72c.md) FUN_0088a72c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0052dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md) [`0066d13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066d/0066d13c.md) [`00aa34d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aa3/00aa34d0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0052e060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e060.md) [`0066d4ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0066d/0066d4ec.md) [`00aa44c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aa4/00aa44c4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 96.84% / 新版 96.84%

CFGの説明率　旧版 49.32% / 新版 53.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008897a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00889904"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0088a750"
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
      "unmatched:008897a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "0088a784",
      "READ",
      [
        "storage",
        "002a0662",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00889804",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088a7cc"
      ]
    ]
  ],
  "added": [
    [
      "0088a750",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "0088a784",
      "READ",
      [
        "storage",
        "002a06a2",
        null,
        "string"
      ]
    ],
    [
      "0088a7b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088a7cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008897a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889780.md#insn-008897a4) · [`00889804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889780.md#insn-00889804) · [`0088988c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889780.md#insn-0088988c)

~~~diff
- 008897a4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008897a4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008897a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008897a4 bytes a8831ff8
- 00889804 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00889804 bytes e0000054
- 0088988c ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 0088988c bytes e0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1c32c93582b524f9c131325436d1123"></a>

### [`00889be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889be0.md) → [`0088ab8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088ab8c.md) FUN_0088ab8c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088ab98",
      "incomplete_value": false,
      "site": "0088ab98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889bec",
      "incomplete_value": false,
      "site": "00889bec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
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
      "0088ab98",
      "DATA",
      [
        "storage",
        "00c814e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088ab98",
      "DATA",
      [
        "storage",
        "00c824b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889be0.md#insn-00889be4) · [`00889be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889be0.md#insn-00889be8)
- 新版 [`0088ab90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088ab8c.md#insn-0088ab90) · [`0088ab94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088ab8c.md#insn-0088ab94)

~~~diff
- 00889be4 ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 0088ab90 ["COPY", "register:4048:8", ["const:c82000:8"]]
- 00889be4 bytes c91f0090
+ 0088ab90 bytes c91f0090
- 00889be8 ["COPY", "tmp:0:8", ["const:4e0:8"]]
- 00889be8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00889be8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00889be8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088ab94 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 0088ab94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088ab94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088ab94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00889be8 bytes 29811391
+ 0088ab94 bytes 29c11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e18f379571e42afb0a3c5395626ecbd"></a>

### [`00889bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889bfc.md) → [`0088aba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088aba8.md) FUN_0088aba8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00889dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889dc0.md) [`00889dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889dc4.md) [`0088a1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a1bc.md) [`0088a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a1c0.md) [`00b37c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37c24.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0088ad6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088ad6c.md) [`0088ad70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088ad70.md) [`0088b168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b168.md) [`0088b16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b16c.md) [`00b38c18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b38/00b38c18.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 66.04% / 新版 66.04%

CFGの説明率　旧版 57.14% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00889c00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00889c00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00889c04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00889c00",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00889c04",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00889c20",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088abac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0088abb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0088abcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889bfc.md#insn-00889c00) · [`00889c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889bfc.md#insn-00889c04) · [`00889c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889bfc.md#insn-00889c20)

~~~diff
- 00889c00 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00889c00 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00889c00 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00889c00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00889c00 bytes fd7b07a9
- 00889c04 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00889c04 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00889c04 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00889c04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00889c04 bytes f44f08a9
- 00889c20 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00889c20 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00889c20 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00889c20 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-088993c3fb79fb8e6c168c1787fadf94"></a>

### [`00889d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889d78.md) → [`0088ad24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088ad24.md) FUN_0088ad24

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088ad48",
      "incomplete_value": false,
      "site": "0088ad48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889d9c",
      "incomplete_value": false,
      "site": "00889d9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:550:8"
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
      "0088ad48",
      "DATA",
      [
        "storage",
        "00c81550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088ad48",
      "DATA",
      [
        "storage",
        "00c82520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889d78.md#insn-00889d8c) · [`00889d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889d78.md#insn-00889d94) · [`00889d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889d78.md#insn-00889d98)
- 新版 [`0088ad38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088ad24.md#insn-0088ad38) · [`0088ad40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088ad24.md#insn-0088ad40) · [`0088ad44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088ad24.md#insn-0088ad44)

~~~diff
- 00889d8c ["INT_ADD", "register:40f0:8", ["const:889d8c:8", "const:4:8"]]
- 00889d8c ["CALL", null, ["callee:00c58f30:8"]]
+ 0088ad38 ["INT_ADD", "register:40f0:8", ["const:88ad38:8", "const:4:8"]]
+ 0088ad38 ["CALL", null, ["callee:00c58f30:8"]]
- 00889d8c bytes 75380f94
+ 0088ad38 bytes 7e380f94
- 00889d94 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088ad40 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 00889d94 bytes c81f0090
+ 0088ad40 bytes c81f0090
- 00889d98 ["COPY", "tmp:0:8", ["const:550:8"]]
- 00889d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00889d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00889d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088ad44 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 0088ad44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088ad44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088ad44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00889d98 bytes 08411591
+ 0088ad44 bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5135bc6b152160d6af6cd94e2f4ac69a"></a>

### [`00889dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889dac.md) → [`0088ad58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088ad58.md) FUN_0088ad58

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088ad64",
      "incomplete_value": false,
      "site": "0088ad64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889db8",
      "incomplete_value": false,
      "site": "00889db8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:550:8"
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
      "0088ad64",
      "DATA",
      [
        "storage",
        "00c81550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088ad64",
      "DATA",
      [
        "storage",
        "00c82520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889dac.md#insn-00889db0) · [`00889db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889dac.md#insn-00889db4)
- 新版 [`0088ad5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088ad58.md#insn-0088ad5c) · [`0088ad60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088ad58.md#insn-0088ad60)

~~~diff
- 00889db0 ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 0088ad5c ["COPY", "register:4048:8", ["const:c82000:8"]]
- 00889db0 bytes c91f0090
+ 0088ad5c bytes c91f0090
- 00889db4 ["COPY", "tmp:0:8", ["const:550:8"]]
- 00889db4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00889db4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00889db4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088ad60 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 0088ad60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088ad60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088ad60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00889db4 bytes 29411591
+ 0088ad60 bytes 29811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f91b6e4ec573346d00e15fec506f3da3"></a>

### [`00889dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889dc8.md) → [`0088ad74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088ad74.md) FUN_0088ad74

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0052dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md) [`0066d13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066d/0066d13c.md) [`006a2bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2bd0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0052e060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e060.md) [`0066d4ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0066d/0066d4ec.md) [`006a2f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a2/006a2f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.02% / 新版 91.02%

CFGの説明率　旧版 57.89% / 新版 62.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088ae0c",
      "incomplete_value": true,
      "site": "0088ae0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6a2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889e60",
      "incomplete_value": true,
      "site": "00889e60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:662:8"
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
      "definition_site": "0088ae94",
      "incomplete_value": true,
      "site": "0088ae94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889ee8",
      "incomplete_value": true,
      "site": "00889ee8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:942:8"
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
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00889f40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0088adfc",
      "READ",
      [
        "storage",
        "002a0662",
        null,
        "string"
      ]
    ],
    [
      "0088ae70",
      "READ",
      [
        "storage",
        "002bb942",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00889f40",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088adfc",
      "READ",
      [
        "storage",
        "002a06a2",
        null,
        "string"
      ]
    ],
    [
      "0088ae70",
      "READ",
      [
        "storage",
        "002bba20",
        null,
        "string"
      ]
    ],
    [
      "0088aeec",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889dc8.md#insn-00889e8c) · [`00889f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889dc8.md#insn-00889f18) · [`00889f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889dc8.md#insn-00889f40)

~~~diff
- 00889e8c ["COPY", "register:0:8", ["register:4048:8"]]
- 00889e8c ["INT_ADD", "register:40f0:8", ["const:889e8c:8", "const:4:8"]]
- 00889e8c ["CALLIND", null, ["register:0:8"]]
- 00889e8c bytes 20013fd6
- 00889f18 ["COPY", "register:0:8", ["register:4048:8"]]
- 00889f18 ["INT_ADD", "register:40f0:8", ["const:889f18:8", "const:4:8"]]
- 00889f18 ["CALLIND", null, ["register:0:8"]]
- 00889f18 bytes 20013fd6
- 00889f40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:48:8"]]
- 00889f40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00889f40 bytes 8082843c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f2317d2cfb292cc9193130c53ba995e"></a>

### [`0088a174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a174.md) → [`0088b120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b120.md) FUN_0088b120

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088b144",
      "incomplete_value": false,
      "site": "0088b144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a198",
      "incomplete_value": false,
      "site": "0088a198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:5d0:8"
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
      "0088b144",
      "DATA",
      [
        "storage",
        "00c815d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b144",
      "DATA",
      [
        "storage",
        "00c825a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a174.md#insn-0088a188) · [`0088a190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a174.md#insn-0088a190) · [`0088a194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a174.md#insn-0088a194)
- 新版 [`0088b134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b120.md#insn-0088b134) · [`0088b13c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b120.md#insn-0088b13c) · [`0088b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b120.md#insn-0088b140)

~~~diff
- 0088a188 ["INT_ADD", "register:40f0:8", ["const:88a188:8", "const:4:8"]]
- 0088a188 ["CALL", null, ["callee:00c58f30:8"]]
+ 0088b134 ["INT_ADD", "register:40f0:8", ["const:88b134:8", "const:4:8"]]
+ 0088b134 ["CALL", null, ["callee:00c58f30:8"]]
- 0088a188 bytes 76370f94
+ 0088b134 bytes 7f370f94
- 0088a190 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088b13c ["COPY", "register:4040:8", ["const:c82000:8"]]
- 0088a190 bytes a81f00f0
+ 0088b13c bytes a81f00f0
- 0088a194 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 0088a194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088a194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088a194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b140 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 0088b140 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b140 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b140 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088a194 bytes 08411791
+ 0088b140 bytes 08811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8b10f8da9295851fea2976627ada18d"></a>

### [`0088a1a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a1a8.md) → [`0088b154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b154.md) FUN_0088b154

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088b160",
      "incomplete_value": false,
      "site": "0088b160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a1b4",
      "incomplete_value": false,
      "site": "0088a1b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:5d0:8"
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
      "0088b160",
      "DATA",
      [
        "storage",
        "00c815d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b160",
      "DATA",
      [
        "storage",
        "00c825a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a1ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a1a8.md#insn-0088a1ac) · [`0088a1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a1a8.md#insn-0088a1b0)
- 新版 [`0088b158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b154.md#insn-0088b158) · [`0088b15c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b154.md#insn-0088b15c)

~~~diff
- 0088a1ac ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 0088b158 ["COPY", "register:4048:8", ["const:c82000:8"]]
- 0088a1ac bytes a91f00f0
+ 0088b158 bytes a91f00f0
- 0088a1b0 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 0088a1b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088a1b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088a1b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088b15c ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 0088b15c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088b15c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088b15c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088a1b0 bytes 29411791
+ 0088b15c bytes 29811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb45bd2844f6600ee215ba6c2ab18219"></a>

### [`0088a1c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a1c4.md) → [`0088b170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b170.md) FUN_0088b170

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`0048ce90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce90.md) [`0069ef6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069ef6c.md) [`006a2bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2bd0.md) [`006a2da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2da0.md) [`006a2da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2da4.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0048d1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b0.md) [`0069f31c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0069f/0069f31c.md) [`006a2f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a2/006a2f80.md) [`006a3150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a3/006a3150.md) [`006a3154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a3/006a3154.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment

命令の説明率　旧版 94.94% / 新版 94.94%

CFGの説明率　旧版 72.22% / 新版 72.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088b20c",
      "incomplete_value": false,
      "site": "0088b218",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a260",
      "incomplete_value": false,
      "site": "0088a26c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0088b1cc",
      "incomplete_value": false,
      "site": "0088b1d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:6a3000:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a220",
      "incomplete_value": false,
      "site": "0088a22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:6a2000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0088a2f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088a220",
      "PARAM",
      [
        "storage",
        "006a2da0",
        null,
        null
      ]
    ],
    [
      "0088b218",
      "DATA",
      [
        "storage",
        "00c81640",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b264",
      "READ",
      [
        "storage",
        "00c81660",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0088b1cc",
      "PARAM",
      [
        "storage",
        "006a3150",
        null,
        null
      ]
    ],
    [
      "0088b218",
      "DATA",
      [
        "storage",
        "00c82610",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b264",
      "READ",
      [
        "storage",
        "00c82630",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a1c4.md#insn-0088a22c) · [`0088a2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a1c4.md#insn-0088a2f8)
- 新版 [`0088b1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b170.md#insn-0088b1d8) · [`0088b2a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b170.md#insn-0088b2a4)

~~~diff
- 0088a22c ["INT_ADD", "register:40f0:8", ["const:88a22c:8", "const:4:8"]]
- 0088a22c ["CALL", null, ["callee:006a3154:8"]]
+ 0088b1d8 ["INT_ADD", "register:40f0:8", ["const:88b1d8:8", "const:4:8"]]
+ 0088b1d8 ["CALL", null, ["callee:006a3154:8"]]
- 0088a22c bytes de62f897
+ 0088b1d8 bytes df5ff897
- 0088a2f8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0088a2f8 ["RETURN", null, ["register:0:8"]]
- 0088a2f8 bytes c0035fd6
+ 0088b2a4 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 0088b2a4 ["RETURN", null, ["register:0:8"]]
+ 0088b2a4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-818593b63309b3b7aaa2ec24ad236e43"></a>

### [`0088a3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a3a4.md) → [`0088b350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b350.md) FUN_0088b350

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088b364",
      "incomplete_value": false,
      "site": "0088b368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a3b8",
      "incomplete_value": false,
      "site": "0088a3bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "0088b368",
      "DATA",
      [
        "storage",
        "00c81640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b368",
      "DATA",
      [
        "storage",
        "00c82610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a3a4.md#insn-0088a3b0) · [`0088a3b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a3a4.md#insn-0088a3b4) · [`0088a3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a3a4.md#insn-0088a3b8)
- 新版 [`0088b35c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b350.md#insn-0088b35c) · [`0088b360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b350.md#insn-0088b360) · [`0088b364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b350.md#insn-0088b364)

~~~diff
- 0088a3b0 ["INT_ADD", "register:40f0:8", ["const:88a3b0:8", "const:4:8"]]
- 0088a3b0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0088b35c ["INT_ADD", "register:40f0:8", ["const:88b35c:8", "const:4:8"]]
+ 0088b35c ["CALL", null, ["callee:00c58f30:8"]]
- 0088a3b0 bytes ec360f94
+ 0088b35c bytes f5360f94
- 0088a3b4 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088b360 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 0088a3b4 bytes a81f00f0
+ 0088b360 bytes a81f00f0
- 0088a3b8 ["COPY", "tmp:0:8", ["const:640:8"]]
- 0088a3b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088a3b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088a3b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b364 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 0088b364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088a3b8 bytes 08011991
+ 0088b364 bytes 08411891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3440f65ee599dde3b0f4297a55cb4af"></a>

### [`0088a828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a828.md) → [`0088b7d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b7d4.md) FUN_0088b7d4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)
- 新版 呼出元 1件 [`008888dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008888dc.md) · 呼出先 3件 [`0088847c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/0088847c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59230.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.81% / 新版 73.81%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088a868"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088a868"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088a86c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088a86c",
      "DATA",
      [
        "storage",
        "00c816e0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0088a884",
      "DATA",
      [
        "storage",
        "00c81128",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0088a89c",
      "PARAM",
      [
        "storage",
        "002b3035",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088b818",
      "DATA",
      [
        "storage",
        "00c826b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b830",
      "DATA",
      [
        "storage",
        "00c820f8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b848",
      "PARAM",
      [
        "storage",
        "002b307f",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a828.md#insn-0088a84c) · [`0088a868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a828.md#insn-0088a868) · [`0088a86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a828.md#insn-0088a86c)
- 新版 [`0088b7f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b7d4.md#insn-0088b7f8)

~~~diff
- 0088a84c ["INT_ADD", "register:40f0:8", ["const:88a84c:8", "const:4:8"]]
- 0088a84c ["CALL", null, ["callee:00c58f30:8"]]
+ 0088b7f8 ["INT_ADD", "register:40f0:8", ["const:88b7f8:8", "const:4:8"]]
+ 0088b7f8 ["CALL", null, ["callee:00c58f30:8"]]
- 0088a84c bytes c5350f94
+ 0088b7f8 bytes ce350f94
- 0088a868 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0088a868 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0088a868 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0088a868 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0088a868 bytes 1ffc00a9
- 0088a86c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0088a86c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0088a86c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-708db9a3c97aaab3cde4549f4747dc9f"></a>

### [`0088a8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a8fc.md) → [`0088b8a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b8a8.md) FUN_0088b8a8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088b8ac",
      "incomplete_value": false,
      "site": "0088b8b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a900",
      "incomplete_value": false,
      "site": "0088a904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "0088b8b0",
      "DATA",
      [
        "storage",
        "00c816e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b8b0",
      "DATA",
      [
        "storage",
        "00c826b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a8fc.md#insn-0088a8fc) · [`0088a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a8fc.md#insn-0088a900)
- 新版 [`0088b8a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b8a8.md#insn-0088b8a8) · [`0088b8ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b8a8.md#insn-0088b8ac)

~~~diff
- 0088a8fc ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088b8a8 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 0088a8fc bytes a81f00f0
+ 0088b8a8 bytes a81f00f0
- 0088a900 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 0088a900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088a900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088a900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b8ac ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 0088b8ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b8ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b8ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088a900 bytes 08811b91
+ 0088b8ac bytes 08c11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d666d409d506f241e0ad61dd9abba45"></a>

### [`0088a90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a90c.md) → [`0088b8b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b8b8.md) FUN_0088b8b8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088b8c8",
      "incomplete_value": false,
      "site": "0088b8d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a91c",
      "incomplete_value": false,
      "site": "0088a924",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "0088b8d0",
      "DATA",
      [
        "storage",
        "00c816e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b8d0",
      "DATA",
      [
        "storage",
        "00c826b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a90c.md#insn-0088a918) · [`0088a91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a90c.md#insn-0088a91c) · [`0088a928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a90c.md#insn-0088a928)
- 新版 [`0088b8c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b8b8.md#insn-0088b8c4) · [`0088b8c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b8b8.md#insn-0088b8c8) · [`0088b8d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b8b8.md#insn-0088b8d4)

~~~diff
- 0088a918 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088b8c4 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 0088a918 bytes a81f00f0
+ 0088b8c4 bytes a81f00f0
- 0088a91c ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 0088a91c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088a91c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088a91c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b8c8 ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 0088b8c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b8c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b8c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088a91c bytes 08811b91
+ 0088b8c8 bytes 08c11a91
- 0088a928 ["INT_ADD", "register:40f0:8", ["const:88a928:8", "const:4:8"]]
- 0088a928 ["CALL", null, ["callee:00c58f40:8"]]
+ 0088b8d4 ["INT_ADD", "register:40f0:8", ["const:88b8d4:8", "const:4:8"]]
+ 0088b8d4 ["CALL", null, ["callee:00c58f40:8"]]
- 0088a928 bytes 92350f94
+ 0088b8d4 bytes 9b350f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01ee49256bf6bc5d681270de682d6127"></a>

### [`0088a948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a948.md) → [`0088b8f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b8f4.md) FUN_0088b8f4

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 4件 [`0088ac64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088ac64.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8f0.md)
- 新版 呼出元 1件 [`008888dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008888dc.md) · 呼出先 4件 [`0088bc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088bc10.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 96.32% / 新版 96.32%

CFGの説明率　旧版 77.78% / 新版 76.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088a974"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088aa54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088aa54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088a974",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088abd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088bb8c"
      ]
    ]
  ],
  "added": [
    [
      "0088b920",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "0088bb80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088bb8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a948.md#insn-0088a974) · [`0088aa2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a948.md#insn-0088aa2c) · [`0088aa54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a948.md#insn-0088aa54)
- 新版 [`0088b9d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b8f4.md#insn-0088b9d8)

~~~diff
- 0088a974 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0088a974 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0088a974 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0088a974 bytes a8831ff8
- 0088aa2c ["INT_ADD", "register:40f0:8", ["const:88aa2c:8", "const:4:8"]]
- 0088aa2c ["CALL", null, ["callee:00c58f30:8"]]
+ 0088b9d8 ["INT_ADD", "register:40f0:8", ["const:88b9d8:8", "const:4:8"]]
+ 0088b9d8 ["CALL", null, ["callee:00c58f30:8"]]
- 0088aa2c bytes 4d350f94
+ 0088b9d8 bytes 56350f94
- 0088aa54 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0088aa54 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 0088aa54 ["COPY", "tmp:2:8", ["register:40b8:8"]]
- 0088aa54 ["COPY", "tmp:3:8", ["register:4000:8"]]
- 0088aa54 bytes 1f5c00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f815c9a21c69760f629ba6ee0022401b"></a>

### [`0088ac64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088ac64.md) → [`0088bc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088bc10.md) FUN_0088bc10

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0088a948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a948.md) · 呼出先 3件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0088b8f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b8f4.md) · 呼出先 3件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 87.50% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0088ac80"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0088ac94"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0088bc2c"
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
      "unmatched:0088ac80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088bd68"
      ]
    ],
    [
      "unmatched:0088ac94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088bc4c"
      ]
    ]
  ],
  "added": [
    [
      "0088bc2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088bd68"
      ]
    ],
    [
      "0088bc40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088bc4c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088ac80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088ac64.md#insn-0088ac80) · [`0088ac94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088ac64.md#insn-0088ac94)
- 新版 [`0088bc2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088bc10.md#insn-0088bc2c)

~~~diff
- 0088ac80 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0088ac80 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
- 0088ac80 bytes e80900b5
- 0088ac94 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0088ac94 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0088ac94 bytes 680000b4
+ 0088bc2c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 0088bc2c ["CBRANCH", null, ["local:b29:8", "tmp:0:1"]]
+ 0088bc2c bytes e80900b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00136ee514dc57c21527377a933d0f79"></a>

### [`0088adc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088adc0.md) → [`0088bd6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088bd6c.md) FUN_0088bd6c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)
- 新版 呼出元 1件 [`008888dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008888dc.md) · 呼出先 3件 [`0088847c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/0088847c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59230.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.77% / 新版 69.77%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088ae00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088ae00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088ae04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088ae04",
      "DATA",
      [
        "storage",
        "00c81730",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0088ae1c",
      "DATA",
      [
        "storage",
        "00c81148",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0088ae38",
      "PARAM",
      [
        "storage",
        "002a7dd9",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088bdb0",
      "DATA",
      [
        "storage",
        "00c82700",
        null,
        "undefined *"
      ]
    ],
    [
      "0088bdc8",
      "DATA",
      [
        "storage",
        "00c82118",
        null,
        "pointer"
      ]
    ],
    [
      "0088bde4",
      "PARAM",
      [
        "storage",
        "002a7f31",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088ae00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088adc0.md#insn-0088ae00) · [`0088ae04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088adc0.md#insn-0088ae04) · [`0088ae1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088adc0.md#insn-0088ae1c)

~~~diff
- 0088ae00 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0088ae00 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0088ae00 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0088ae00 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0088ae00 bytes 1ffc00a9
- 0088ae04 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0088ae04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0088ae04 bytes 080000f9
- 0088ae1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:20:8"]]
- 0088ae1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0088ae1c bytes 681200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af5971360a4248ee4b1c9425833af6f8"></a>

### [`0088ae98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088ae98.md) → [`0088be44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088be44.md) FUN_0088be44

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088be48",
      "incomplete_value": false,
      "site": "0088be4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088ae9c",
      "incomplete_value": false,
      "site": "0088aea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:730:8"
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
      "0088be4c",
      "DATA",
      [
        "storage",
        "00c81730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088be4c",
      "DATA",
      [
        "storage",
        "00c82700",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088ae98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088ae98.md#insn-0088ae98) · [`0088ae9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088ae98.md#insn-0088ae9c)
- 新版 [`0088be44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088be44.md#insn-0088be44) · [`0088be48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088be44.md#insn-0088be48)

~~~diff
- 0088ae98 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088be44 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 0088ae98 bytes a81f00f0
+ 0088be44 bytes a81f00f0
- 0088ae9c ["COPY", "tmp:0:8", ["const:730:8"]]
- 0088ae9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088ae9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088ae9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088be48 ["COPY", "tmp:0:8", ["const:700:8"]]
+ 0088be48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088be48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088be48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088ae9c bytes 08c11c91
+ 0088be48 bytes 08011c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24a746d70a58b82a766b7fcb41d9a60e"></a>

### [`0088aee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aee4.md) → [`0088be90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088be90.md) FUN_0088be90

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)
- 新版 呼出元 1件 [`008888dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008888dc.md) · 呼出先 3件 [`0088847c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/0088847c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59230.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 48.84% / 新版 48.84%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088aee4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088aee8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088aee8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088aee4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088aee8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088aeec",
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
      "0088be90",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0088be94",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0088be98",
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

- 旧版 [`0088aee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aee4.md#insn-0088aee4) · [`0088aee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aee4.md#insn-0088aee8) · [`0088aeec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aee4.md#insn-0088aeec)

~~~diff
- 0088aee4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 0088aee4 ["STORE", null, ["const:1b1:8", "register:8:8", "register:5100:8"]]
- 0088aee4 bytes e80f1cfc
- 0088aee8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0088aee8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0088aee8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0088aee8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088aee8 bytes fd7b01a9
- 0088aeec ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0088aeec ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0088aeec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0088aeec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088aeec bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e63569b2b19b5cca77751126ec99215"></a>

### [`0088affc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088affc.md) → [`0088bfa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088bfa8.md) FUN_0088bfa8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`0088b36c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b36c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0088c318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c318.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088b000",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0088c318"
      ]
    ]
  ],
  "added": [
    [
      "0088bfac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0088c318"
      ]
    ]
  ]
}
~~~


<a id="compare-f4a0e2bb0bbc87b9c1c91bda5a2d19b5"></a>

### [`0088b008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b008.md) → [`0088bfb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088bfb4.md) FUN_0088bfb4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)
- 新版 呼出元 1件 [`008888dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008888dc.md) · 呼出先 3件 [`0088847c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/0088847c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59230.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 39.53% / 新版 39.53%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b008"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b00c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b00c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088b008",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088b00c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088b010",
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
      "0088bfb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0088bfb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0088bfbc",
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

- 旧版 [`0088b008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b008.md#insn-0088b008) · [`0088b00c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b008.md#insn-0088b00c) · [`0088b010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b008.md#insn-0088b010)

~~~diff
- 0088b008 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 0088b008 ["STORE", null, ["const:1b1:8", "register:8:8", "register:5100:8"]]
- 0088b008 bytes e80f1cfc
- 0088b00c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0088b00c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0088b00c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0088b00c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088b00c bytes fd7b01a9
- 0088b010 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0088b010 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0088b010 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0088b010 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088b010 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f88133dabf5670fbd44865d1530f3aef"></a>

### [`0088b0e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b0e0.md) → [`0088c08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c08c.md) FUN_0088c08c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088c090",
      "incomplete_value": false,
      "site": "0088c094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b0e4",
      "incomplete_value": false,
      "site": "0088b0e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
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
      "0088c094",
      "DATA",
      [
        "storage",
        "00c817d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088c094",
      "DATA",
      [
        "storage",
        "00c827a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b0e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b0e0.md#insn-0088b0e0) · [`0088b0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b0e0.md#insn-0088b0e4)
- 新版 [`0088c08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c08c.md#insn-0088c08c) · [`0088c090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c08c.md#insn-0088c090)

~~~diff
- 0088b0e0 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088c08c ["COPY", "register:4040:8", ["const:c82000:8"]]
- 0088b0e0 bytes a81f00d0
+ 0088c08c bytes a81f00d0
- 0088b0e4 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 0088b0e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b0e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b0e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088c090 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 0088c090 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088c090 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088c090 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b0e4 bytes 08411f91
+ 0088c090 bytes 08811e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbb9f8769db4071260b5fcacec7b2ab0"></a>

### [`0088b0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b0f0.md) → [`0088c09c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c09c.md) FUN_0088c09c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088c0ac",
      "incomplete_value": false,
      "site": "0088c0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b100",
      "incomplete_value": false,
      "site": "0088b108",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
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
      "0088c0b4",
      "DATA",
      [
        "storage",
        "00c817d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088c0b4",
      "DATA",
      [
        "storage",
        "00c827a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b0fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b0f0.md#insn-0088b0fc) · [`0088b100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b0f0.md#insn-0088b100) · [`0088b10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b0f0.md#insn-0088b10c)
- 新版 [`0088c0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c09c.md#insn-0088c0a8) · [`0088c0ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c09c.md#insn-0088c0ac) · [`0088c0b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c09c.md#insn-0088c0b8)

~~~diff
- 0088b0fc ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088c0a8 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 0088b0fc bytes a81f00d0
+ 0088c0a8 bytes a81f00d0
- 0088b100 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 0088b100 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b100 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b100 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088c0ac ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 0088c0ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088c0ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088c0ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b100 bytes 08411f91
+ 0088c0ac bytes 08811e91
- 0088b10c ["INT_ADD", "register:40f0:8", ["const:88b10c:8", "const:4:8"]]
- 0088b10c ["CALL", null, ["callee:00c58f40:8"]]
+ 0088c0b8 ["INT_ADD", "register:40f0:8", ["const:88c0b8:8", "const:4:8"]]
+ 0088c0b8 ["CALL", null, ["callee:00c58f40:8"]]
- 0088b10c bytes 99330f94
+ 0088c0b8 bytes a2330f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73285c08fc8272c9365443e72363dbb7"></a>

### [`0088b12c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b12c.md) → [`0088c0d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c0d8.md) FUN_0088c0d8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)
- 新版 呼出元 1件 [`008888dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008888dc.md) · 呼出先 3件 [`0088847c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/0088847c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59230.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b134"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b134"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b138"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088b134",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088b138",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0088c11c",
      "DATA",
      [
        "storage",
        "00c81820",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088c0e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0088c0e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0088c11c",
      "DATA",
      [
        "storage",
        "00c827f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b12c.md#insn-0088b134) · [`0088b138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b12c.md#insn-0088b138) · [`0088b1a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b12c.md#insn-0088b1a8)
- 新版 [`0088c154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c0d8.md#insn-0088c154)

~~~diff
- 0088b134 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0088b134 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0088b134 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0088b134 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088b134 bytes f65702a9
- 0088b138 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0088b138 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0088b138 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0088b138 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088b138 bytes f44f03a9
- 0088b1a8 ["INT_ADD", "register:40f0:8", ["const:88b1a8:8", "const:4:8"]]
- 0088b1a8 ["CALL", null, ["callee:00c59230:8"]]
+ 0088c154 ["INT_ADD", "register:40f0:8", ["const:88c154:8", "const:4:8"]]
+ 0088c154 ["CALL", null, ["callee:00c59230:8"]]
- 0088b1a8 bytes 2e340f94
+ 0088c154 bytes 37340f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0e8748231f09c7f60de4174f5fc1bb5"></a>

### [`0088b200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b200.md) → [`0088c1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c1ac.md) FUN_0088c1ac

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088c1b0",
      "incomplete_value": false,
      "site": "0088c1b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b204",
      "incomplete_value": false,
      "site": "0088b208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:820:8"
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
      "0088c1b4",
      "DATA",
      [
        "storage",
        "00c81820",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088c1b4",
      "DATA",
      [
        "storage",
        "00c827f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b200.md#insn-0088b200) · [`0088b204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b200.md#insn-0088b204)
- 新版 [`0088c1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c1ac.md#insn-0088c1ac) · [`0088c1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c1ac.md#insn-0088c1b0)

~~~diff
- 0088b200 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088c1ac ["COPY", "register:4040:8", ["const:c82000:8"]]
- 0088b200 bytes a81f00d0
+ 0088c1ac bytes a81f00d0
- 0088b204 ["COPY", "tmp:0:8", ["const:820:8"]]
- 0088b204 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b204 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b204 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088c1b0 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 0088c1b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088c1b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088c1b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b204 bytes 08812091
+ 0088c1b0 bytes 08c11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44d0ededa4faf31fdd9b207c969a46c8"></a>

### [`0088b24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b24c.md) → [`0088c1f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c1f8.md) FUN_0088c1f8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)
- 新版 呼出元 1件 [`008888dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008888dc.md) · 呼出先 3件 [`0088847c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/0088847c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59230.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 59.52% / 新版 59.52%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b24c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b24c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b250"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088b24c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088b250",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088b254",
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
      "0088c1f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0088c1fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0088c200",
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

- 旧版 [`0088b24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b24c.md#insn-0088b24c) · [`0088b250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b24c.md#insn-0088b250) · [`0088b254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b24c.md#insn-0088b254)

~~~diff
- 0088b24c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0088b24c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0088b24c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 0088b24c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0088b24c bytes fd7bbca9
- 0088b250 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0088b250 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 0088b250 bytes f70b00f9
- 0088b254 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0088b254 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0088b254 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0088b254 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088b254 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d1c702fba3a156808961cb0e8094d45"></a>

### [`0088b320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b320.md) → [`0088c2cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c2cc.md) FUN_0088c2cc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088c2d0",
      "incomplete_value": false,
      "site": "0088c2d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b324",
      "incomplete_value": false,
      "site": "0088b328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "0088c2d4",
      "DATA",
      [
        "storage",
        "00c81870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088c2d4",
      "DATA",
      [
        "storage",
        "00c82840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b320.md#insn-0088b320) · [`0088b324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b320.md#insn-0088b324)
- 新版 [`0088c2cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c2cc.md#insn-0088c2cc) · [`0088c2d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c2cc.md#insn-0088c2d0)

~~~diff
- 0088b320 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088c2cc ["COPY", "register:4040:8", ["const:c82000:8"]]
- 0088b320 bytes a81f00d0
+ 0088c2cc bytes a81f00d0
- 0088b324 ["COPY", "tmp:0:8", ["const:870:8"]]
- 0088b324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088c2d0 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 0088c2d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088c2d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088c2d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b324 bytes 08c12191
+ 0088c2d0 bytes 08012191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68c47a4e3435e477ce0cea105745d755"></a>

### [`0088b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b330.md) → [`0088c2dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c2dc.md) FUN_0088c2dc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088c2ec",
      "incomplete_value": false,
      "site": "0088c2f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b340",
      "incomplete_value": false,
      "site": "0088b348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "0088c2f4",
      "DATA",
      [
        "storage",
        "00c81870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088c2f4",
      "DATA",
      [
        "storage",
        "00c82840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b330.md#insn-0088b33c) · [`0088b340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b330.md#insn-0088b340) · [`0088b34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b330.md#insn-0088b34c)
- 新版 [`0088c2e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c2dc.md#insn-0088c2e8) · [`0088c2ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c2dc.md#insn-0088c2ec) · [`0088c2f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c2dc.md#insn-0088c2f8)

~~~diff
- 0088b33c ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088c2e8 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 0088b33c bytes a81f00d0
+ 0088c2e8 bytes a81f00d0
- 0088b340 ["COPY", "tmp:0:8", ["const:870:8"]]
- 0088b340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088c2ec ["COPY", "tmp:0:8", ["const:840:8"]]
+ 0088c2ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088c2ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088c2ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b340 bytes 08c12191
+ 0088c2ec bytes 08012191
- 0088b34c ["INT_ADD", "register:40f0:8", ["const:88b34c:8", "const:4:8"]]
- 0088b34c ["CALL", null, ["callee:00c58f40:8"]]
+ 0088c2f8 ["INT_ADD", "register:40f0:8", ["const:88c2f8:8", "const:4:8"]]
+ 0088c2f8 ["CALL", null, ["callee:00c58f40:8"]]
- 0088b34c bytes 09330f94
+ 0088c2f8 bytes 12330f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aadc96714f708da09f428490a41916b5"></a>

### [`0088b36c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b36c.md) → [`0088c318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c318.md) FUN_0088c318

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`0088a93c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a93c.md) [`0088aed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aed8.md) [`0088affc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088affc.md) [`0088b120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b120.md) [`0088b240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b240.md) · 呼出先 3件 [`00597f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f0c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 7件 [`0088b8e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b8e8.md) [`0088be84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088be84.md) [`0088bfa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088bfa8.md) [`0088c0cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c0cc.md) [`0088c1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c1ec.md) · 呼出先 3件 [`0059822c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/0059822c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment

命令の説明率　旧版 69.79% / 新版 69.79%

CFGの説明率　旧版 8.70% / 新版 7.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件, `unresolved_branch_alignment` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088c33c",
      "incomplete_value": false,
      "site": "0088c340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b390",
      "incomplete_value": false,
      "site": "0088b394",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b3c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b3c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0088c340",
      "DATA",
      [
        "storage",
        "00c81108",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0088b3c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0088b3d4"
      ]
    ],
    [
      "unmatched:0088b3c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088c394"
      ]
    ]
  ],
  "added": [
    [
      "0088c340",
      "DATA",
      [
        "storage",
        "00c820d8",
        null,
        "pointer"
      ]
    ],
    [
      "0088c370",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088c380"
      ]
    ],
    [
      "0088c374",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088c394"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b3c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b36c.md#insn-0088b3c4) · [`0088b3c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b36c.md#insn-0088b3c8) · [`0088b424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b36c.md#insn-0088b424)

~~~diff
- 0088b3c4 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 0088b3c4 bytes 80000054
- 0088b3c8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0088b3c8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 0088b3c8 bytes 000100b4
- 0088b424 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 0088b424 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-272f841a65c896cd987f3b070af3c8e5"></a>

### [`0088b4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b4f0.md) → [`0088c49c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c49c.md) FUN_0088c49c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)
- 新版 呼出元 1件 [`008888dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008888dc.md) · 呼出先 3件 [`0088847c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/0088847c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59230.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.39% / 新版 69.39%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b544"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b544"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b548"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088b548",
      "DATA",
      [
        "storage",
        "00c818c0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0088b550",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0088847c"
      ]
    ],
    [
      "unmatched:0088b560",
      "DATA",
      [
        "storage",
        "00c811e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0088c4f4",
      "DATA",
      [
        "storage",
        "00c82890",
        null,
        "undefined *"
      ]
    ],
    [
      "0088c4fc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0088847c"
      ]
    ],
    [
      "0088c50c",
      "DATA",
      [
        "storage",
        "00c821b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b4f0.md#insn-0088b520) · [`0088b544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b4f0.md#insn-0088b544) · [`0088b548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b4f0.md#insn-0088b548)
- 新版 [`0088c4cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c49c.md#insn-0088c4cc)

~~~diff
- 0088b520 ["INT_ADD", "register:40f0:8", ["const:88b520:8", "const:4:8"]]
- 0088b520 ["CALL", null, ["callee:00c58f30:8"]]
+ 0088c4cc ["INT_ADD", "register:40f0:8", ["const:88c4cc:8", "const:4:8"]]
+ 0088c4cc ["CALL", null, ["callee:00c58f30:8"]]
- 0088b520 bytes 90320f94
+ 0088c4cc bytes 99320f94
- 0088b544 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0088b544 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0088b544 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0088b544 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0088b544 bytes 1ffc00a9
- 0088b548 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0088b548 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0088b548 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0956f0b12bc8976eaecd6724a81be85"></a>

### [`0088b5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b5e0.md) → [`0088c58c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c58c.md) FUN_0088c58c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088c590",
      "incomplete_value": false,
      "site": "0088c594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b5e4",
      "incomplete_value": false,
      "site": "0088b5e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "0088c594",
      "DATA",
      [
        "storage",
        "00c818c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088c594",
      "DATA",
      [
        "storage",
        "00c82890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b5e0.md#insn-0088b5e0) · [`0088b5e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b5e0.md#insn-0088b5e4)
- 新版 [`0088c58c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c58c.md#insn-0088c58c) · [`0088c590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c58c.md#insn-0088c590)

~~~diff
- 0088b5e0 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088c58c ["COPY", "register:4040:8", ["const:c82000:8"]]
- 0088b5e0 bytes a81f00d0
+ 0088c58c bytes a81f00d0
- 0088b5e4 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 0088b5e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b5e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b5e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088c590 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 0088c590 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088c590 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088c590 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b5e4 bytes 08012391
+ 0088c590 bytes 08412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e8eeb43a6c7d04f0cc319fca62af11e"></a>

### [`0088b620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b620.md) → [`0088c5cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c5cc.md) FUN_0088c5cc

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00597f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f0c.md) [`0088b36c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b36c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0059822c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/0059822c.md) [`0088c318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c318.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 56.67% / 新版 56.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b624"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b624"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b628"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088b624",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088b628",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088b644",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088c5d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0088c5d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0088c5f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b620.md#insn-0088b624) · [`0088b628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b620.md#insn-0088b628) · [`0088b644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b620.md#insn-0088b644)

~~~diff
- 0088b624 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0088b624 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0088b624 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0088b624 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088b624 bytes fd7b02a9
- 0088b628 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0088b628 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0088b628 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0088b628 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088b628 bytes f44f03a9
- 0088b644 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0088b644 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0088b644 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0088b644 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1e506a7bd42eec05f0dae242833ea3f"></a>

### [`0088b6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b6a0.md) → [`0088c64c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c64c.md) FUN_0088c64c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)
- 新版 呼出元 1件 [`008888dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008888dc.md) · 呼出先 3件 [`0088847c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/0088847c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59230.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 48.84% / 新版 48.84%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b6a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b6a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b6a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088b6a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088b6a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088b6a8",
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
      "0088c64c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0088c650",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0088c654",
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

- 旧版 [`0088b6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b6a0.md#insn-0088b6a0) · [`0088b6a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b6a0.md#insn-0088b6a4) · [`0088b6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b6a0.md#insn-0088b6a8)

~~~diff
- 0088b6a0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 0088b6a0 ["STORE", null, ["const:1b1:8", "register:8:8", "register:5100:8"]]
- 0088b6a0 bytes e80f1cfc
- 0088b6a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0088b6a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0088b6a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0088b6a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088b6a4 bytes fd7b01a9
- 0088b6a8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0088b6a8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0088b6a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0088b6a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088b6a8 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05002475dfcbff45674b0d818fcdbd3a"></a>

### [`0088b778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b778.md) → [`0088c724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c724.md) FUN_0088c724

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)
- 新版 呼出元 1件 [`008888dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008888dc.md) · 呼出先 3件 [`0088847c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/0088847c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59230.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.42% / 新版 74.42%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b7b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b7b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b7bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088b7bc",
      "DATA",
      [
        "storage",
        "00c81870",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0088b7d4",
      "DATA",
      [
        "storage",
        "00c811a8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0088b7f0",
      "PARAM",
      [
        "storage",
        "002b86a3",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088c768",
      "DATA",
      [
        "storage",
        "00c82840",
        null,
        "undefined *"
      ]
    ],
    [
      "0088c780",
      "DATA",
      [
        "storage",
        "00c82178",
        null,
        "pointer"
      ]
    ],
    [
      "0088c79c",
      "PARAM",
      [
        "storage",
        "002b8772",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b778.md#insn-0088b79c) · [`0088b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b778.md#insn-0088b7b8) · [`0088b7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b778.md#insn-0088b7bc)
- 新版 [`0088c748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c724.md#insn-0088c748)

~~~diff
- 0088b79c ["INT_ADD", "register:40f0:8", ["const:88b79c:8", "const:4:8"]]
- 0088b79c ["CALL", null, ["callee:00c58f30:8"]]
+ 0088c748 ["INT_ADD", "register:40f0:8", ["const:88c748:8", "const:4:8"]]
+ 0088c748 ["CALL", null, ["callee:00c58f30:8"]]
- 0088b79c bytes f1310f94
+ 0088c748 bytes fa310f94
- 0088b7b8 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0088b7b8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0088b7b8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0088b7b8 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0088b7b8 bytes 1ffc00a9
- 0088b7bc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0088b7bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0088b7bc bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bb086b17d12a0d56b70abf6a222d81c"></a>

### [`0088b850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b850.md) → [`0088c7fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c7fc.md) FUN_0088c7fc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)
- 新版 呼出元 1件 [`008888dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008888dc.md) · 呼出先 3件 [`0088847c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/0088847c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59230.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.35% / 新版 67.35%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b860"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b860"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b8a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088b860",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088b8a8",
      "DATA",
      [
        "storage",
        "00c818c0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0088b8b0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0088847c"
      ]
    ]
  ],
  "added": [
    [
      "0088c80c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0088c854",
      "DATA",
      [
        "storage",
        "00c82890",
        null,
        "undefined *"
      ]
    ],
    [
      "0088c85c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0088847c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b850.md#insn-0088b860) · [`0088b880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b850.md#insn-0088b880) · [`0088b8a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b850.md#insn-0088b8a4)
- 新版 [`0088c82c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c7fc.md#insn-0088c82c)

~~~diff
- 0088b860 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0088b860 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0088b860 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0088b860 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088b860 bytes f44f04a9
- 0088b880 ["INT_ADD", "register:40f0:8", ["const:88b880:8", "const:4:8"]]
- 0088b880 ["CALL", null, ["callee:00c58f30:8"]]
+ 0088c82c ["INT_ADD", "register:40f0:8", ["const:88c82c:8", "const:4:8"]]
+ 0088c82c ["CALL", null, ["callee:00c58f30:8"]]
- 0088b880 bytes b8310f94
+ 0088c82c bytes c1310f94
- 0088b8a4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0088b8a4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0088b8a4 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0088b8a4 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0088b8a4 bytes 1ffc00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8fe5b6b1f8f03af4639ebe2996f9b31"></a>

### [`0088b948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b948.md) → [`0088c8f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c8f4.md) FUN_0088c8f4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088c918",
      "incomplete_value": false,
      "site": "0088c918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b96c",
      "incomplete_value": false,
      "site": "0088b96c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:910:8"
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
      "0088c918",
      "DATA",
      [
        "storage",
        "00c81910",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088c918",
      "DATA",
      [
        "storage",
        "00c828e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b948.md#insn-0088b95c) · [`0088b964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b948.md#insn-0088b964) · [`0088b968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b948.md#insn-0088b968)
- 新版 [`0088c908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c8f4.md#insn-0088c908) · [`0088c910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c8f4.md#insn-0088c910) · [`0088c914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c8f4.md#insn-0088c914)

~~~diff
- 0088b95c ["INT_ADD", "register:40f0:8", ["const:88b95c:8", "const:4:8"]]
- 0088b95c ["CALL", null, ["callee:00c58f30:8"]]
+ 0088c908 ["INT_ADD", "register:40f0:8", ["const:88c908:8", "const:4:8"]]
+ 0088c908 ["CALL", null, ["callee:00c58f30:8"]]
- 0088b95c bytes 81310f94
+ 0088c908 bytes 8a310f94
- 0088b964 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088c910 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 0088b964 bytes a81f00d0
+ 0088c910 bytes a81f00d0
- 0088b968 ["COPY", "tmp:0:8", ["const:910:8"]]
- 0088b968 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b968 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b968 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088c914 ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 0088c914 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088c914 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088c914 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b968 bytes 08412491
+ 0088c914 bytes 08812391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2983d647b385578c50c9dd71b143d00"></a>

### [`0088b97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b97c.md) → [`0088c928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c928.md) FUN_0088c928

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088c934",
      "incomplete_value": false,
      "site": "0088c934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b988",
      "incomplete_value": false,
      "site": "0088b988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "0088c934",
      "DATA",
      [
        "storage",
        "00c81910",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088c934",
      "DATA",
      [
        "storage",
        "00c828e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b97c.md#insn-0088b980) · [`0088b984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b97c.md#insn-0088b984)
- 新版 [`0088c92c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c928.md#insn-0088c92c) · [`0088c930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c928.md#insn-0088c930)

~~~diff
- 0088b980 ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 0088c92c ["COPY", "register:4048:8", ["const:c82000:8"]]
- 0088b980 bytes a91f00d0
+ 0088c92c bytes a91f00d0
- 0088b984 ["COPY", "tmp:0:8", ["const:910:8"]]
- 0088b984 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088b984 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088b984 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088c930 ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 0088c930 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088c930 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088c930 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088b984 bytes 29412491
+ 0088c930 bytes 29812391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5acdd1344385f484f341f2985ca3180c"></a>

### [`0088bde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088bde8.md) → [`0088cd94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088cd94.md) _INIT_165

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 77.40% / 新版 77.40%

CFGの説明率　旧版 30.77% / 新版 31.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088be18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088be2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088be30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088be18",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088be24",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0088be2c",
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
      "0088cdc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0088cdd0",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0088cdd8",
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

- 旧版 [`0088be18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088bde8.md#insn-0088be18) · [`0088be2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088bde8.md#insn-0088be2c) · [`0088be30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088bde8.md#insn-0088be30)

~~~diff
- 0088be18 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0088be18 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0088be18 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0088be18 bytes a9831ff8
- 0088be2c ["COPY", "tmp:0:4", ["register:4050:4"]]
- 0088be2c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 0088be2c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 0088be2c bytes ea130278
- 0088be30 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 0088be30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 0088be30 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41b8e4189f8bd283ff25ed5f64776968"></a>

### [`0088c178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md) → [`0088d124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d124.md) FUN_0088d124

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 25件 [`00472b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472b38.md) [`00472bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472bec.md) [`00472bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472bfc.md) [`00472de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472de4.md) [`004737bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004737bc.md)
- 新版 呼出元 0件  · 呼出先 25件 [`00472e58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00472/00472e58.md) [`00472f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00472/00472f0c.md) [`00472f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00472/00472f1c.md) [`00473104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00473/00473104.md) [`00473adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00473/00473adc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.68% / 新版 79.68%

CFGの説明率　旧版 19.74% / 新版 20.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088c2c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088c388"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088c38c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0088d144",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0088c2b8"
      ]
    ],
    [
      "unmatched:0088c1c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00472bec"
      ]
    ],
    [
      "0088d174",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0088c2b8"
      ]
    ]
  ],
  "added": [
    [
      "0088d144",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088d264"
      ]
    ],
    [
      "0088d16c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00472f0c"
      ]
    ],
    [
      "0088d174",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088d264"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088c1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md#insn-0088c1c0) · [`0088c1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md#insn-0088c1f4) · [`0088c244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md#insn-0088c244)

~~~diff
- 0088c1c0 ["INT_ADD", "register:40f0:8", ["const:88c1c0:8", "const:4:8"]]
- 0088c1c0 ["CALL", null, ["ram:472bec:8"]]
- 0088c1c0 bytes 8b9aef97
- 0088c1f4 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 0088c1f4 bytes a0020054
- 0088c244 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0088c244 ["CBRANCH", null, ["local:b47:8", "tmp:0:1"]]
- 0088c244 bytes 410f0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01d2977fa5cd0aa0407a8dd1c1626c65"></a>

### [`0088c504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c504.md) → [`0088d4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d4b0.md) FUN_0088d4b0

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0088c178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md) [`0088f4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f4f4.md) [`0088f6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f6cc.md) · 呼出先 9件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044c814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c814.md) [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md)
- 新版 呼出元 3件 [`0088d124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d124.md) [`008904a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/008904a0.md) [`00890678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890678.md) · 呼出先 9件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0044cb34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044c/0044cb34.md) [`004738a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00473/004738a0.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048eb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048eb40.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.60% / 新版 75.60%

CFGの説明率　旧版 50.77% / 新版 49.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088c580"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088c58c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088c5a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088c528",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "unmatched:0088c52c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0048eb40"
      ]
    ],
    [
      "unmatched:0088c530",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ],
  "added": [
    [
      "0088d4d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048d058"
      ]
    ],
    [
      "0088d4d8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0048eb40"
      ]
    ],
    [
      "0088d4dc",
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

- 旧版 [`0088c528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c504.md#insn-0088c528) · [`0088c52c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c504.md#insn-0088c52c) · [`0088c580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c504.md#insn-0088c580)

~~~diff
- 0088c528 ["INT_ADD", "register:40f0:8", ["const:88c528:8", "const:4:8"]]
- 0088c528 ["CALL", null, ["ram:48cd38:8"]]
- 0088c528 bytes 0402f097
- 0088c52c ["INT_ADD", "register:40f0:8", ["const:88c52c:8", "const:4:8"]]
- 0088c52c ["CALL", null, ["callee:0048eb40:8"]]
- 0088c52c bytes bd08f097
- 0088c580 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0088c580 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:48:8"]]
- 0088c580 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0088c580 bytes e9230139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68b4f32673a6db41dfbd7f62fe6f721e"></a>

### [`0088ef18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088e/0088ef18.md) → [`0088fec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088f/0088fec4.md) FUN_0088fec4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 2件 [`0088d874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d874.md) [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) · 呼出先 5件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004412bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412bc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 73.75% / 新版 73.75%

CFGの説明率　旧版 47.06% / 新版 53.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088efec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088eff0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088eff0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088ef84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088fff8"
      ]
    ]
  ],
  "added": [
    [
      "0088ff30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088fff8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088ef84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088e/0088ef18.md#insn-0088ef84) · [`0088efec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088e/0088ef18.md#insn-0088efec) · [`0088eff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088e/0088ef18.md#insn-0088eff0)

~~~diff
- 0088ef84 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0088ef84 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 0088ef84 ["CBRANCH", null, ["local:b12:8", "tmp:1:1"]]
- 0088ef84 bytes 48060054
- 0088efec ["COPY", "tmp:0:8", ["register:4008:8"]]
- 0088efec ["COPY", "tmp:1:8", ["const:0:8"]]
- 0088efec ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 0088efec bytes 3f0000f9
- 0088eff0 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0088eff0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0088eff0 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0088eff0 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0088eff0 bytes 3ffc00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8364f4c8920fb704e505c5d423eb36d6"></a>

### [`0088f2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f2d8.md) → [`00890284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890284.md) FUN_00890284

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 3件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0046d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d5e8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0088d874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d874.md) · 呼出先 3件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`0046d908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d908.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008902ec",
      "incomplete_value": false,
      "site": "008902f0",
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
      "definition_site": "0088f340",
      "incomplete_value": false,
      "site": "0088f344",
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
      "008902ec",
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
      "008902ec",
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

- 旧版 [`0088f344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f2d8.md#insn-0088f344) · [`0088f2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f2d8.md#insn-0088f2fc) · [`0088f340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f2d8.md#insn-0088f340)
- 新版 [`008902f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890284.md#insn-008902f0) · [`008902a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890284.md#insn-008902a8) · [`008902ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890284.md#insn-008902ec)

~~~diff
- 0088f344 ["INT_ADD", "register:40f0:8", ["const:88f344:8", "const:4:8"]]
- 0088f344 ["CALL", null, ["callee:00442c90:8"]]
+ 008902f0 ["INT_ADD", "register:40f0:8", ["const:8902f0:8", "const:4:8"]]
+ 008902f0 ["CALL", null, ["callee:00442c90:8"]]
- 0088f344 bytes 8bcdee97
+ 008902f0 bytes 68caee97
- 0088f2fc ["INT_ADD", "register:40f0:8", ["const:88f2fc:8", "const:4:8"]]
- 0088f2fc ["CALL", null, ["callee:0046d908:8"]]
+ 008902a8 ["INT_ADD", "register:40f0:8", ["const:8902a8:8", "const:4:8"]]
+ 008902a8 ["CALL", null, ["callee:0046d908:8"]]
- 0088f2fc bytes bb78ef97
+ 008902a8 bytes 9875ef97
- 0088f340 ["COPY", "tmp:0:8", ["const:170:8"]]
- 0088f340 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0088f340 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0088f340 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008902ec ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 008902ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008902ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008902ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0088f340 bytes 00c00591
+ 008902ec bytes 00c00691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f06c575ac732e52bd670bd4552227a44"></a>

### [`0088f34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f34c.md) → [`008902f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/008902f8.md) FUN_008902f8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 2件 [`0046d6ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d6ec.md) [`00564320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/00564320.md)
- 新版 呼出元 1件 [`0088d874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d874.md) · 呼出先 2件 [`0046da0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046da0c.md) [`00564640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00564/00564640.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088f35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f34c.md#insn-0088f35c) · [`0088f368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f34c.md#insn-0088f368) · [`0088f374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f34c.md#insn-0088f374)
- 新版 [`00890308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/008902f8.md#insn-00890308) · [`00890314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/008902f8.md#insn-00890314) · [`00890320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/008902f8.md#insn-00890320)

~~~diff
- 0088f35c ["INT_ADD", "register:40f0:8", ["const:88f35c:8", "const:4:8"]]
- 0088f35c ["CALL", null, ["callee:0046da0c:8"]]
+ 00890308 ["INT_ADD", "register:40f0:8", ["const:890308:8", "const:4:8"]]
+ 00890308 ["CALL", null, ["callee:0046da0c:8"]]
- 0088f35c bytes e478ef97
+ 00890308 bytes c175ef97
- 0088f368 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
+ 00890314 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 0088f368 bytes c0000054
+ 00890314 bytes c0000054
- 0088f374 ["INT_ADD", "register:40f0:8", ["const:88f374:8", "const:4:8"]]
- 0088f374 ["CALL", null, ["callee:00564640:8"]]
+ 00890320 ["INT_ADD", "register:40f0:8", ["const:890320:8", "const:4:8"]]
+ 00890320 ["CALL", null, ["callee:00564640:8"]]
- 0088f374 bytes eb53f397
+ 00890320 bytes c850f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b86871c9dba1bb250634b12f19f54fe0"></a>

### [`0088f390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f390.md) → [`0089033c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/0089033c.md) FUN_0089033c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) [`00aa3e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aa3/00aa3e94.md) · 呼出先 1件 [`00c5a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9c0.md)
- 新版 呼出元 2件 [`0088d874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d874.md) [`00aa4e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aa4/00aa4e88.md) · 呼出先 1件 [`00c5b990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b990.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0088f3b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f390.md#insn-0088f3b4)
- 新版 [`00890360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/0089033c.md#insn-00890360)

~~~diff
- 0088f3b4 ["INT_ADD", "register:40f0:8", ["const:88f3b4:8", "const:4:8"]]
- 0088f3b4 ["CALL", null, ["callee:00c5b990:8"]]
+ 00890360 ["INT_ADD", "register:40f0:8", ["const:890360:8", "const:4:8"]]
+ 00890360 ["CALL", null, ["callee:00c5b990:8"]]
- 0088f3b4 bytes 832d0f94
+ 00890360 bytes 8c2d0f94
~~~


<a id="compare-ab88909ad5ab2966f31e8083d6ae6d92"></a>

### [`0088f3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f3d8.md) → [`00890384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890384.md) FUN_00890384

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md)
- 新版 呼出元 1件 [`0088d874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d874.md) · 呼出先 3件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.56% / 新版 80.56%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088f400"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088f404"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088f408"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088f400",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088f410",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008903ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008903bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088f400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f3d8.md#insn-0088f400) · [`0088f404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f3d8.md#insn-0088f404) · [`0088f408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f3d8.md#insn-0088f408)

~~~diff
- 0088f400 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0088f400 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 0088f400 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0088f400 bytes a8031ff8
- 0088f404 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0088f404 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 0088f404 bytes 010000f9
- 0088f408 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 0088f408 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0088f408 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 0088f408 bytes 1f0800f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7f46f06dc995c5a387a97f2f4a548ae"></a>

### [`0088f6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f6b0.md) → [`0089065c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/0089065c.md) FUN_0089065c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00890668",
      "incomplete_value": false,
      "site": "00890668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088f6bc",
      "incomplete_value": false,
      "site": "0088f6bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "00890668",
      "DATA",
      [
        "storage",
        "00c81be8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00890668",
      "DATA",
      [
        "storage",
        "00c82bb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088f6b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f6b0.md#insn-0088f6b4) · [`0088f6b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f6b0.md#insn-0088f6b8)
- 新版 [`00890660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/0089065c.md#insn-00890660) · [`00890664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/0089065c.md#insn-00890664)

~~~diff
- 0088f6b4 ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 00890660 ["COPY", "register:4048:8", ["const:c82000:8"]]
- 0088f6b4 bytes 891f00d0
+ 00890660 bytes 891f00d0
- 0088f6b8 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 0088f6b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088f6b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088f6b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00890664 ["COPY", "tmp:0:8", ["const:bb8:8"]]
+ 00890664 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00890664 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00890664 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088f6b8 bytes 29a12f91
+ 00890664 bytes 29e12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dde3fc752c45a260e4db589ade6551e9"></a>

### [`0088fb80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fb80.md) → [`00890b2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890b2c.md) FUN_00890b2c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00890b40",
      "incomplete_value": false,
      "site": "00890b44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088fb94",
      "incomplete_value": false,
      "site": "0088fb98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
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
      "00890b44",
      "DATA",
      [
        "storage",
        "00c81cd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00890b44",
      "DATA",
      [
        "storage",
        "00c82ca8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088fb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fb80.md#insn-0088fb90) · [`0088fb94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fb80.md#insn-0088fb94) · [`0088fba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fb80.md#insn-0088fba8)
- 新版 [`00890b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890b2c.md#insn-00890b3c) · [`00890b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890b2c.md#insn-00890b40) · [`00890b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890b2c.md#insn-00890b54)

~~~diff
- 0088fb90 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00890b3c ["COPY", "register:4040:8", ["const:c82000:8"]]
- 0088fb90 bytes 881f00d0
+ 00890b3c bytes 881f00d0
- 0088fb94 ["COPY", "tmp:0:8", ["const:cd8:8"]]
- 0088fb94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088fb94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088fb94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00890b40 ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 00890b40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00890b40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00890b40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088fb94 bytes 08613391
+ 00890b40 bytes 08a13291
- 0088fba8 ["INT_ADD", "register:40f0:8", ["const:88fba8:8", "const:4:8"]]
- 0088fba8 ["CALL", null, ["callee:00c54d90:8"]]
+ 00890b54 ["INT_ADD", "register:40f0:8", ["const:890b54:8", "const:4:8"]]
+ 00890b54 ["CALL", null, ["callee:00c54d90:8"]]
- 0088fba8 bytes 7e100f94
+ 00890b54 bytes 8f100f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-484e56ec557e60b64569db2509d78daf"></a>

### [`0088fbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fbdc.md) → [`00890b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890b88.md) FUN_00890b88

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088fbf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00890ba4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0088fc20",
      "incomplete_value": true,
      "site": "0088fc24",
      "value": [
        "live",
        "register:40a0:8"
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
      "unmatched:0088fbf8",
      "DATA",
      [
        "storage",
        "00c81cd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00890ba4",
      "DATA",
      [
        "storage",
        "00c82ca8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088fbf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fbdc.md#insn-0088fbf8) · [`0088fc24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fbdc.md#insn-0088fc24)
- 新版 [`00890bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890b88.md#insn-00890bd0) · [`00890ba4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890b88.md#insn-00890ba4)

~~~diff
- 0088fbf8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0088fbf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0088fbf8 bytes 080000f9
- 0088fc24 ["INT_ADD", "register:40f0:8", ["const:88fc24:8", "const:4:8"]]
- 0088fc24 ["CALL", null, ["callee:00c58f20:8"]]
+ 00890bd0 ["INT_ADD", "register:40f0:8", ["const:890bd0:8", "const:4:8"]]
+ 00890bd0 ["CALL", null, ["callee:00c58f20:8"]]
- 0088fc24 bytes cb200f94
+ 00890bd0 bytes d4200f94
+ 00890ba4 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00890ba4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00890ba4 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25d7891c4ba266406a90ef5ed2256d11"></a>

### [`0088fc88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fc88.md) → [`00890c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890c34.md) FUN_00890c34

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00890c40",
      "incomplete_value": false,
      "site": "00890c40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088fc94",
      "incomplete_value": false,
      "site": "0088fc94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
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
      "00890c40",
      "DATA",
      [
        "storage",
        "00c81cd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00890c40",
      "DATA",
      [
        "storage",
        "00c82ca8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088fc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fc88.md#insn-0088fc8c) · [`0088fc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fc88.md#insn-0088fc90) · [`0088fcb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fc88.md#insn-0088fcb0)
- 新版 [`00890c38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890c34.md#insn-00890c38) · [`00890c3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890c34.md#insn-00890c3c) · [`00890c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890c34.md#insn-00890c5c)

~~~diff
- 0088fc8c ["COPY", "register:4048:8", ["const:c81000:8"]]
+ 00890c38 ["COPY", "register:4048:8", ["const:c82000:8"]]
- 0088fc8c bytes 891f00d0
+ 00890c38 bytes 891f00d0
- 0088fc90 ["COPY", "tmp:0:8", ["const:cd8:8"]]
- 0088fc90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088fc90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088fc90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00890c3c ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 00890c3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00890c3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00890c3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088fc90 bytes 29613391
+ 00890c3c bytes 29a13291
- 0088fcb0 ["INT_ADD", "register:40f0:8", ["const:88fcb0:8", "const:4:8"]]
- 0088fcb0 ["CALL", null, ["callee:00c54d60:8"]]
+ 00890c5c ["INT_ADD", "register:40f0:8", ["const:890c5c:8", "const:4:8"]]
+ 00890c5c ["CALL", null, ["callee:00c54d60:8"]]
- 0088fcb0 bytes 30100f94
+ 00890c5c bytes 41100f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-affa8cf00ea98a657168335eba04002e"></a>

### [`0088fd5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fd5c.md) → [`00890d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890d08.md) FUN_00890d08

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048dc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048dc8c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048dfac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048dfac.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

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
      "site": "00890d10",
      "value": [
        "leaf",
        "ram:48d058:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0088fd64",
      "value": [
        "leaf",
        "ram:48cd38:8"
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
      "00890d10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ],
  "added": [
    [
      "00890d10",
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

- 旧版 [`0088fd64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fd5c.md#insn-0088fd64) · [`0088fd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fd5c.md#insn-0088fd68) · [`0088fd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fd5c.md#insn-0088fd70)
- 新版 [`00890d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890d08.md#insn-00890d10) · [`00890d14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890d08.md#insn-00890d14) · [`00890d1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890d08.md#insn-00890d1c)

~~~diff
- 0088fd64 ["INT_ADD", "register:40f0:8", ["const:88fd64:8", "const:4:8"]]
- 0088fd64 ["CALL", null, ["ram:48cd38:8"]]
+ 00890d10 ["INT_ADD", "register:40f0:8", ["const:890d10:8", "const:4:8"]]
+ 00890d10 ["CALL", null, ["ram:48d058:8"]]
- 0088fd64 bytes f5f3ef97
+ 00890d10 bytes d2f0ef97
- 0088fd68 ["INT_ADD", "register:40f0:8", ["const:88fd68:8", "const:4:8"]]
- 0088fd68 ["CALL", null, ["callee:0048dfac:8"]]
+ 00890d14 ["INT_ADD", "register:40f0:8", ["const:890d14:8", "const:4:8"]]
+ 00890d14 ["CALL", null, ["callee:0048dfac:8"]]
- 0088fd68 bytes c9f7ef97
+ 00890d14 bytes a6f4ef97
- 0088fd70 ["INT_ADD", "register:40f0:8", ["const:88fd70:8", "const:4:8"]]
- 0088fd70 ["CALL", null, ["callee:008524fc:8"]]
+ 00890d1c ["INT_ADD", "register:40f0:8", ["const:890d1c:8", "const:4:8"]]
+ 00890d1c ["CALL", null, ["callee:008524fc:8"]]
- 0088fd70 bytes f805ff97
+ 00890d1c bytes f805ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68b1bfcadd79e6238e355c32e05ccbce"></a>

### [`0088fdb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fdb8.md) → [`00890d64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890d64.md) FUN_00890d64

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00890d78",
      "incomplete_value": false,
      "site": "00890d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088fdcc",
      "incomplete_value": false,
      "site": "0088fdd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "00890d7c",
      "DATA",
      [
        "storage",
        "00c81d68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00890d7c",
      "DATA",
      [
        "storage",
        "00c82d38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088fdc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fdb8.md#insn-0088fdc4) · [`0088fdc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fdb8.md#insn-0088fdc8) · [`0088fdcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fdb8.md#insn-0088fdcc)
- 新版 [`00890d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890d64.md#insn-00890d70) · [`00890d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890d64.md#insn-00890d74) · [`00890d78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890d64.md#insn-00890d78)

~~~diff
- 0088fdc4 ["INT_ADD", "register:40f0:8", ["const:88fdc4:8", "const:4:8"]]
- 0088fdc4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00890d70 ["INT_ADD", "register:40f0:8", ["const:890d70:8", "const:4:8"]]
+ 00890d70 ["CALL", null, ["callee:00c58f30:8"]]
- 0088fdc4 bytes 67200f94
+ 00890d70 bytes 70200f94
- 0088fdc8 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00890d74 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 0088fdc8 bytes 881f00d0
+ 00890d74 bytes 881f00d0
- 0088fdcc ["COPY", "tmp:0:8", ["const:d68:8"]]
- 0088fdcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088fdcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088fdcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00890d78 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00890d78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00890d78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00890d78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088fdcc bytes 08a13591
+ 00890d78 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-359cea324c1cf1fc444a18447c6e516d"></a>

### [`0088fdf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fdf4.md) → [`00890da0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00890/00890da0.md) FUN_00890da0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00550a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a54.md) [`0089020c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/0089020c.md) [`0089025c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/0089025c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`00550d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550d74.md) [`008911b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/008911b8.md) [`00891208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891208.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.91% / 新版 84.91%

CFGの説明率　旧版 58.06% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088fe20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088fe28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088fe2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088fe18",
      "READ",
      [
        "storage",
        "002b790e",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0088fe20",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088fe24",
      "READ",
      [
        "storage",
        "002b7915",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00890dc4",
      "READ",
      [
        "storage",
        "002b79dd",
        null,
        "string"
      ]
    ],
    [
      "00890dcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00890dd0",
      "READ",
      [
        "storage",
        "002b79e4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088fe20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fdf4.md#insn-0088fe20) · [`0088fe28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fdf4.md#insn-0088fe28) · [`0088fe2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fdf4.md#insn-0088fe2c)

~~~diff
- 0088fe20 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0088fe20 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0088fe20 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0088fe20 bytes a8831ff8
- 0088fe28 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 0088fe28 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:28:8"]]
- 0088fe28 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0088fe28 bytes eaa30039
- 0088fe2c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 0088fe2c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:29:8"]]
- 0088fe2c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0088fe2c bytes eb9302f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba37a2bd91aa4c58b55b4227d2760973"></a>

### [`0089012c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/0089012c.md) → [`008910d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/008910d8.md) FUN_008910d8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "008910f0",
      "incomplete_value": false,
      "site": "008910f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00890144",
      "incomplete_value": false,
      "site": "00890148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
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
      "008910f4",
      "DATA",
      [
        "storage",
        "00c81dd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008910f4",
      "DATA",
      [
        "storage",
        "00c82da8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00890140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/0089012c.md#insn-00890140) · [`00890144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/0089012c.md#insn-00890144) · [`00890158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/0089012c.md#insn-00890158)
- 新版 [`008910ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/008910d8.md#insn-008910ec) · [`008910f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/008910d8.md#insn-008910f0) · [`00891104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/008910d8.md#insn-00891104)

~~~diff
- 00890140 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 008910ec ["COPY", "register:4040:8", ["const:c82000:8"]]
- 00890140 bytes 881f00b0
+ 008910ec bytes 881f00b0
- 00890144 ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 00890144 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00890144 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00890144 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008910f0 ["COPY", "tmp:0:8", ["const:da8:8"]]
+ 008910f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008910f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008910f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00890144 bytes 08613791
+ 008910f0 bytes 08a13691
- 00890158 ["INT_ADD", "register:40f0:8", ["const:890158:8", "const:4:8"]]
- 00890158 ["CALL", null, ["callee:00c54d90:8"]]
+ 00891104 ["INT_ADD", "register:40f0:8", ["const:891104:8", "const:4:8"]]
+ 00891104 ["CALL", null, ["callee:00c54d90:8"]]
- 00890158 bytes 120f0f94
+ 00891104 bytes 230f0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7d5f85378baac95c76406b06b27c684"></a>

### [`008902d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008902d8.md) → [`00891284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891284.md) _INIT_166

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 72.88% / 新版 72.88%

CFGの説明率　旧版 12.20% / 新版 10.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00890308"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00890330"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00890354"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00890308",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00890314",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00890330",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008912b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008912c0",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "008912dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00890308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008902d8.md#insn-00890308) · [`00890330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008902d8.md#insn-00890330) · [`00890354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008902d8.md#insn-00890354)

~~~diff
- 00890308 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00890308 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00890308 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00890308 bytes a9831ff8
- 00890330 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00890330 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00890330 bytes e013813c
- 00890354 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00890354 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00890354 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-371098e27b4d63b7414cb0fa8cccec20"></a>

### [`00890668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890668.md) → [`00891614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891614.md) FUN_00891614

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00890c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890c28.md) [`00891e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891e20.md) · 呼出先 3件 [`0058f474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f474.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58500.md)
- 新版 呼出元 2件 [`00891bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891bd4.md) [`00892dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892dcc.md) · 呼出先 3件 [`0058f794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f794.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c594d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c594d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.21% / 新版 86.21%

CFGの説明率　旧版 45.00% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0089066c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0089066c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00890670"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0089066c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00890670",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00890690",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00891618",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0089161c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0089163c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0089066c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890668.md#insn-0089066c) · [`00890670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890668.md#insn-00890670) · [`00890690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890668.md#insn-00890690)

~~~diff
- 0089066c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0089066c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0089066c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0089066c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0089066c bytes fd7b04a9
- 00890670 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00890670 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00890670 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00890670 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00890670 bytes f65705a9
- 00890690 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00890690 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00890690 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00890690 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b650ece5190f7765621fbbc8a7b1175c"></a>

### [`008907ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008907ac.md) → [`00891758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891758.md) FUN_00891758

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00890c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890c28.md) [`00890de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890de4.md) [`0089261c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/0089261c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00852508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852508.md) · 呼出先 8件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00891bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891bd4.md) [`00891d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891d90.md) [`008935c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/008935c8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 54.81% / 新版 54.81%

CFGの説明率　旧版 62.50% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 47件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008907f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00890804"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00890810"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008907f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00890800",
      "READ",
      [
        "storage",
        "002f323f",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00890804",
      "WRITE",
      [
        "storage",
        "Stack[-0x1e8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008917a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "008917ac",
      "READ",
      [
        "storage",
        "002f327f",
        null,
        "string"
      ]
    ],
    [
      "008917b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x1e8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008907f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008907ac.md#insn-008907f4) · [`00890804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008907ac.md#insn-00890804) · [`00890810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008907ac.md#insn-00890810)

~~~diff
- 008907f4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008907f4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 008907f4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008907f4 bytes a8031ff8
- 00890804 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00890804 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00890804 bytes e92b00b9
- 00890810 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00890810 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00890810 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00890810 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00890810 bytes 1f7c00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be6eb5d3935b9f5e55c66bab5fa36460"></a>

### [`00890c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890c28.md) → [`00891bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891bd4.md) FUN_00891bd4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008907ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008907ac.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00890668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890668.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00891758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891758.md) · 呼出先 5件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00891614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891614.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.27% / 新版 87.27%

CFGの説明率　旧版 47.37% / 新版 40.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00890c2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00890c2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00890c30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00890c2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00890c30",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00890c34",
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
      "00891bd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00891bdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00891be0",
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

- 旧版 [`00890c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890c28.md#insn-00890c2c) · [`00890c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890c28.md#insn-00890c30) · [`00890c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890c28.md#insn-00890c34)

~~~diff
- 00890c2c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00890c2c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00890c2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00890c2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00890c2c bytes fd7b06a9
- 00890c30 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00890c30 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00890c30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00890c30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00890c30 bytes f65707a9
- 00890c34 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00890c34 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00890c34 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00890c34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00890c34 bytes f44f08a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47439e56fc656810647a63e7130a440a"></a>

### [`00890de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890de4.md) → [`00891d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891d90.md) FUN_00891d90

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`008907ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008907ac.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00891758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891758.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 59.70% / 新版 63.49%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00891e6c",
      "incomplete_value": true,
      "site": "00891e70",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:118:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00890ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890de4.md#insn-00890ec4) · [`00890df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890de4.md#insn-00890df8) · [`00890e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890de4.md#insn-00890e00)
- 新版 [`00891e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891d90.md#insn-00891e70) · [`00891da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891d90.md#insn-00891da4) · [`00891dac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891d90.md#insn-00891dac)

~~~diff
- 00890ec4 ["INT_ADD", "register:40f0:8", ["const:890ec4:8", "const:4:8"]]
- 00890ec4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00891e70 ["INT_ADD", "register:40f0:8", ["const:891e70:8", "const:4:8"]]
+ 00891e70 ["CALL", null, ["callee:00c58f50:8"]]
- 00890ec4 bytes 2f1c0f94
+ 00891e70 bytes 381c0f94
- 00890df8 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00890df8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00890df8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00890df8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00891da4 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00891da4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00891da4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00891da4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00890df8 bytes 48040037
+ 00891da4 bytes 48040037
- 00890e00 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00890e00 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00890e00 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00890e00 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00891dac ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00891dac ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00891dac ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00891dac ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00890e00 bytes 88040037
+ 00891dac bytes 88040037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d3243231ad5286556fc9966720d7b9c"></a>

### [`00891038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891038.md) → [`00891fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891fe4.md) FUN_00891fe4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0084876c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/0084876c.md) [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) [`00854944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00854/00854944.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 4件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) [`00849718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00849/00849718.md) [`00852508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852508.md) [`008558f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00855/008558f0.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 57.33% / 新版 57.33%

CFGの説明率　旧版 5.66% / 新版 6.98%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00891038"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00891038"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0089103c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00891038",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0089103c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00891040",
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
      "00891fe4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00891fe8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00891fec",
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

- 旧版 [`00891038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891038.md#insn-00891038) · [`0089103c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891038.md#insn-0089103c) · [`00891040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891038.md#insn-00891040)

~~~diff
- 00891038 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00891038 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00891038 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00891038 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00891038 bytes fd7bbda9
- 0089103c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0089103c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0089103c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0089103c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0089103c bytes f65701a9
- 00891040 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00891040 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00891040 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00891040 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00891040 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c6b553b365f80db14ea5cf4e32326e6"></a>

### [`0089135c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/0089135c.md) → [`00892308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892308.md) FUN_00892308

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00891fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891fb8.md) · 呼出先 23件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`00892f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892f64.md) · 呼出先 23件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 55.32% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00891394"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00891600"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00891604"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00891394",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00891398",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b3a1a4"
      ]
    ],
    [
      "unmatched:0089139c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089243c"
      ]
    ]
  ],
  "added": [
    [
      "00892340",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00892344",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b3a1a4"
      ]
    ],
    [
      "00892348",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089243c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00891394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/0089135c.md#insn-00891394) · [`00891600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/0089135c.md#insn-00891600) · [`00891604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/0089135c.md#insn-00891604)

~~~diff
- 00891394 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00891394 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00891394 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00891394 bytes a8031ff8
- 00891600 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:18:8"]]
- 00891600 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:8"]]
- 00891600 bytes 000d00fd
- 00891604 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00891604 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:28:8"]]
- 00891604 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00891604 bytes 09a10039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08c2af6919faf4f27361ac9fc76cbcb3"></a>

### [`00891a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891a64.md) → [`00892a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892a10.md) FUN_00892a10

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00891fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891fb8.md) [`00893e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893e14.md) [`0089d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089d/0089d520.md) · 呼出先 3件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b391b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b39/00b391b0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 3件 [`00892f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892f64.md) [`00894dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894dc0.md) [`0089e4cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089e/0089e4cc.md) · 呼出先 3件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00b3a1a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3a/00b3a1a4.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 72.41% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00891b68"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00892b14"
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
      "00892b08",
      "DATA",
      [
        "storage",
        "00436b50",
        "fde_00436b50",
        "dword"
      ]
    ],
    [
      "00892b0c",
      "READ",
      [
        "storage",
        "002f32f8",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00891b68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00892b20"
      ]
    ]
  ],
  "added": [
    [
      "00892b08",
      "DATA",
      [
        "storage",
        "00436b50",
        null,
        "byte[47]"
      ]
    ],
    [
      "00892b0c",
      "READ",
      [
        "storage",
        "002f3338",
        null,
        "undefined4"
      ]
    ],
    [
      "00892b14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00892b20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00891b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891a64.md#insn-00891b68) · [`00891a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891a64.md#insn-00891a80)
- 新版 [`00892b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892a10.md#insn-00892b14) · [`00892a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892a10.md#insn-00892a2c)

~~~diff
- 00891b68 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00891b68 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00891b68 bytes 6a000054
+ 00892b14 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00892b14 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
+ 00892b14 bytes 6a000054
- 00891a80 ["INT_ADD", "register:40f0:8", ["const:891a80:8", "const:4:8"]]
- 00891a80 ["CALL", null, ["callee:00b3a1a4:8"]]
+ 00892a2c ["INT_ADD", "register:40f0:8", ["const:892a2c:8", "const:4:8"]]
+ 00892a2c ["CALL", null, ["callee:00b3a1a4:8"]]
- 00891a80 bytes cc9d0a94
+ 00892a2c bytes de9d0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-659063c587b93e30007ec6eb677e3fb0"></a>

### [`00891bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891bc4.md) → [`00892b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892b70.md) FUN_00892b70

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00891fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891fb8.md) [`00892494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892494.md) [`008931a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008931a4.md) [`008932f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008932f4.md) · 呼出先 9件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00892ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892ce8.md) [`00892cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892cec.md) [`008b98b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b98b0.md)
- 新版 呼出元 4件 [`00892f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892f64.md) [`00893440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893440.md) [`00894150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894150.md) [`008942a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/008942a0.md) · 呼出先 9件 [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00893c94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893c94.md) [`00893c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893c98.md) [`008ba85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba85c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 60.34% / 新版 60.34%

CFGの説明率　旧版 30.30% / 新版 32.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00891c1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00891c20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00891c24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00892b9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00892c20"
      ]
    ],
    [
      "unmatched:00891bf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00892bec"
      ]
    ],
    [
      "unmatched:00891bf8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00892c84"
      ]
    ]
  ],
  "added": [
    [
      "00892b94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00892c20"
      ]
    ],
    [
      "00892b9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00892bec"
      ]
    ],
    [
      "00892ba4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00892c84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00891bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891bc4.md#insn-00891bf0) · [`00891bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891bc4.md#insn-00891bf8) · [`00891c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891bc4.md#insn-00891c1c)

~~~diff
- 00891bf0 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00891bf0 bytes 80020054
- 00891bf8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00891bf8 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00891bf8 bytes 01070054
- 00891c1c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00891c1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00891c1c bytes e00b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e391094fc8e9e148379a7b5c044189ec"></a>

### [`00891e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891e20.md) → [`00892dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892dcc.md) FUN_00892dcc

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0089135c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/0089135c.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00890668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890668.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00892308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892308.md) · 呼出先 5件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00891614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891614.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.78% / 新版 91.78%

CFGの説明率　旧版 33.33% / 新版 38.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00891e6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00891e70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00892e18"
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
      "unmatched:00891e6c",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00891e70",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ],
    [
      "00892e50",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00892e30"
      ]
    ]
  ],
  "added": [
    [
      "00892e18",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "00892e1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ],
    [
      "00892e20",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00892e30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00891e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891e20.md#insn-00891e6c) · [`00891e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891e20.md#insn-00891e70) · [`00891ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891e20.md#insn-00891ec0)

~~~diff
- 00891e6c ["COPY", "tmp:0:8", ["register:8:8"]]
- 00891e6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00891e6c bytes e003803d
- 00891e70 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00891e70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00891e70 bytes e80b00f9
- 00891ec0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00891ec0 ["INT_ADD", "register:40f0:8", ["const:891ec0:8", "const:4:8"]]
- 00891ec0 ["CALLIND", null, ["register:0:8"]]
- 00891ec0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4df7d4aef65f5bf5a763b49f17993141"></a>

### [`00891fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891fb8.md) → [`00892f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892f64.md) FUN_00892f64

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00892f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892f04.md) [`00893e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893e14.md) [`0089d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089d/0089d520.md) · 呼出先 16件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce60.md) [`0047ce68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce68.md) [`0058f474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f474.md)
- 新版 呼出元 3件 [`00893eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893eb0.md) [`00894dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894dc0.md) [`0089e4cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089e/0089e4cc.md) · 呼出先 16件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d180.md) [`0047d188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d188.md) [`0058f794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f794.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 94.46% / 新版 94.46%

CFGの説明率　旧版 72.22% / 新版 72.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 2件, `store_value` 2件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00893294",
      "incomplete_value": false,
      "site": "0089329c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008922e8",
      "incomplete_value": false,
      "site": "008922f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "definition_site": "008932a8",
      "incomplete_value": false,
      "site": "008932a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:348:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008922fc",
      "incomplete_value": false,
      "site": "008922fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008920b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008920b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00893164"
      ]
    ],
    [
      "unmatched:0089211c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00893164"
      ]
    ],
    [
      "unmatched:0089218c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008923cc"
      ]
    ]
  ],
  "added": [
    [
      "00893060",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00893164"
      ]
    ],
    [
      "008930c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00893164"
      ]
    ],
    [
      "00893138",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00893378"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008920b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891fb8.md#insn-008920b4) · [`0089210c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891fb8.md#insn-0089210c) · [`0089211c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891fb8.md#insn-0089211c)
- 新版 [`008930b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892f64.md#insn-008930b8)

~~~diff
- 008920b4 ["CBRANCH", null, ["local:b31:8", "register:101:1"]]
- 008920b4 bytes 20080054
- 0089210c ["INT_ADD", "register:40f0:8", ["const:89210c:8", "const:4:8"]]
- 0089210c ["CALL", null, ["callee:00c590f0:8"]]
+ 008930b8 ["INT_ADD", "register:40f0:8", ["const:8930b8:8", "const:4:8"]]
+ 008930b8 ["CALL", null, ["callee:00c590f0:8"]]
- 0089210c bytes 05180f94
+ 008930b8 bytes 0e180f94
- 0089211c ["CBRANCH", null, ["local:b31:8", "register:101:1"]]
- 0089211c bytes e0040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15af3a5d666207ea38dd1ae61ddff50a"></a>

### [`0089261c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/0089261c.md) → [`008935c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/008935c8.md) FUN_008935c8

採用 · 移動量 `+0xfac` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008907ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008907ac.md) [`0089135c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/0089135c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`00891758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00891/00891758.md) [`00892308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892308.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "008935d4",
      "incomplete_value": false,
      "site": "008935d8",
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
      "definition_site": "00892628",
      "incomplete_value": false,
      "site": "0089262c",
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
      "008935d4",
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
      "008935d4",
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

- 旧版 [`0089262c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/0089261c.md#insn-0089262c) · [`00892624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/0089261c.md#insn-00892624) · [`00892628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/0089261c.md#insn-00892628)
- 新版 [`008935d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/008935c8.md#insn-008935d8) · [`008935d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/008935c8.md#insn-008935d0) · [`008935d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/008935c8.md#insn-008935d4)

~~~diff
- 0089262c ["INT_ADD", "register:40f0:8", ["const:89262c:8", "const:4:8"]]
- 0089262c ["CALL", null, ["callee:0043bad8:8"]]
+ 008935d8 ["INT_ADD", "register:40f0:8", ["const:8935d8:8", "const:4:8"]]
+ 008935d8 ["CALL", null, ["callee:0043bad8:8"]]
- 0089262c bytes 63a4ee97
+ 008935d8 bytes 40a1ee97
- 00892624 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 008935d0 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00892624 bytes 20d1ffb0
+ 008935d0 bytes 20d1ffb0
- 00892628 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00892628 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00892628 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00892628 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008935d4 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 008935d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008935d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008935d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00892628 bytes 00303e91
+ 008935d4 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e45d99569e708be54e8aa37aeff9d0a"></a>

### [`00892670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892670.md) → [`0089361c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/0089361c.md) FUN_0089361c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`008927b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/008927b4.md) [`008927b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/008927b8.md) [`00b3a654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3a/00b3a654.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00893760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893760.md) [`00893764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893764.md) [`00b3b648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3b/00b3b648.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.27% / 新版 70.27%

CFGの説明率　旧版 25.00% / 新版 23.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00892674"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00892674"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00892678"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00892674",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00892678",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00892688",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00893620",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00893624",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00893634",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892670.md#insn-00892674) · [`00892678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892670.md#insn-00892678) · [`00892688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892670.md#insn-00892688)

~~~diff
- 00892674 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00892674 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00892674 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00892674 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00892674 bytes fd7b04a9
- 00892678 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00892678 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00892678 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00892678 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00892678 bytes f44f05a9
- 00892688 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00892688 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00892688 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00892688 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fa129e3bd95019ee0098db2eae1b16c"></a>

### [`008927a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/008927a4.md) → [`00893750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893750.md) FUN_00893750

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00893754",
      "incomplete_value": false,
      "site": "00893758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008927a8",
      "incomplete_value": false,
      "site": "008927ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
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
      "00893758",
      "DATA",
      [
        "storage",
        "00c81ee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00893758",
      "DATA",
      [
        "storage",
        "00c82eb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008927a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/008927a4.md#insn-008927a4) · [`008927a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/008927a4.md#insn-008927a8)
- 新版 [`00893750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893750.md#insn-00893750) · [`00893754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893750.md#insn-00893754)

~~~diff
- 008927a4 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00893750 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 008927a4 bytes 681f00f0
+ 00893750 bytes 681f00f0
- 008927a8 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 008927a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008927a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008927a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00893754 ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 00893754 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00893754 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00893754 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008927a8 bytes 08a13b91
+ 00893754 bytes 08e13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58c444edd3e7a91704fdb07357c1615a"></a>

### [`008927bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/008927bc.md) → [`00893768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893768.md) FUN_00893768

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0071c4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c4b8.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00442e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442e98.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`0071c868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c868.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.31% / 新版 84.31%

CFGの説明率　旧版 42.37% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008927c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008927c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008927c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008927c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:008927c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008927c8",
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
      "0089376c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00893770",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00893774",
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

- 旧版 [`008927c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/008927bc.md#insn-008927c0) · [`008927c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/008927bc.md#insn-008927c4) · [`008927c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/008927bc.md#insn-008927c8)

~~~diff
- 008927c0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008927c0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008927c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 008927c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008927c0 bytes fd7b0da9
- 008927c4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:e0:8"]]
- 008927c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 008927c4 bytes f57300f9
- 008927c8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008927c8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008927c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 008927c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008927c8 bytes f44f0fa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75b9f7299333b7b20a0e6e5738ce769e"></a>

### [`00892b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892b64.md) → [`00893b10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893b10.md) FUN_00893b10

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00892b7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00893b28"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00892b6c",
      "incomplete_value": false,
      "site": "00892b70",
      "value": [
        "leaf",
        "const:10:8"
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
      "unmatched:00892b7c",
      "DATA",
      [
        "storage",
        "00c81f58",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00892b80",
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
      "00893b28",
      "DATA",
      [
        "storage",
        "00c82f28",
        null,
        "undefined *"
      ]
    ],
    [
      "00893b2c",
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

- 旧版 [`00892b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892b64.md#insn-00892b70) · [`00892b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892b64.md#insn-00892b7c) · [`00892b84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892b64.md#insn-00892b84)
- 新版 [`00893b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893b10.md#insn-00893b1c)

~~~diff
- 00892b70 ["INT_ADD", "register:40f0:8", ["const:892b70:8", "const:4:8"]]
- 00892b70 ["CALL", null, ["callee:00c58f30:8"]]
+ 00893b1c ["INT_ADD", "register:40f0:8", ["const:893b1c:8", "const:4:8"]]
+ 00893b1c ["CALL", null, ["callee:00c58f30:8"]]
- 00892b70 bytes fc140f94
+ 00893b1c bytes 05150f94
- 00892b7c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00892b7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00892b7c bytes 080000f9
- 00892b84 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00892b84 ["RETURN", null, ["register:0:8"]]
- 00892b84 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2ec7a10698362f56ddcb70da1f06943"></a>

### [`00892b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892b88.md) → [`00893b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893b34.md) FUN_00893b34

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00893b38",
      "incomplete_value": false,
      "site": "00893b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892b8c",
      "incomplete_value": false,
      "site": "00892b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      "00893b3c",
      "DATA",
      [
        "storage",
        "00c81f58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00893b3c",
      "DATA",
      [
        "storage",
        "00c82f28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892b88.md#insn-00892b88) · [`00892b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892b88.md#insn-00892b8c)
- 新版 [`00893b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893b34.md#insn-00893b34) · [`00893b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893b34.md#insn-00893b38)

~~~diff
- 00892b88 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00893b34 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 00892b88 bytes 681f00f0
+ 00893b34 bytes 681f00f0
- 00892b8c ["COPY", "tmp:0:8", ["const:f58:8"]]
- 00892b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00892b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00892b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00893b38 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 00893b38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00893b38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00893b38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00892b8c bytes 08613d91
+ 00893b38 bytes 08a13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c5db9f6af4fdd2b1cd5c3c017d8e07f"></a>

### [`00892ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892ba0.md) → [`00893b4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893b4c.md) FUN_00893b4c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "00893b70",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00892bc4",
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
      "00893b70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00893b70",
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

- 旧版 [`00892bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892ba0.md#insn-00892bc4) · [`00892bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892ba0.md#insn-00892bd0)
- 新版 [`00893b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893b4c.md#insn-00893b70) · [`00893b7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893b4c.md#insn-00893b7c)

~~~diff
- 00892bc4 ["INT_ADD", "register:40f0:8", ["const:892bc4:8", "const:4:8"]]
- 00892bc4 ["CALL", null, ["ram:47ad34:8"]]
+ 00893b70 ["INT_ADD", "register:40f0:8", ["const:893b70:8", "const:4:8"]]
+ 00893b70 ["CALL", null, ["ram:47b054:8"]]
- 00892bc4 bytes 5ca0ef97
+ 00893b70 bytes 399def97
- 00892bd0 ["INT_ADD", "register:40f0:8", ["const:892bd0:8", "const:4:8"]]
- 00892bd0 ["CALL", null, ["callee:0047d134:8"]]
+ 00893b7c ["INT_ADD", "register:40f0:8", ["const:893b7c:8", "const:4:8"]]
+ 00893b7c ["CALL", null, ["callee:0047d134:8"]]
- 00892bd0 bytes 91a8ef97
+ 00893b7c bytes 6ea5ef97
~~~


<a id="compare-af79b26b5e79e751d6dc6e970c3d74e3"></a>

### [`00892c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892c14.md) → [`00893bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893bc0.md) FUN_00893bc0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00893bd4",
      "incomplete_value": false,
      "site": "00893bd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892c28",
      "incomplete_value": false,
      "site": "00892c2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
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
      "00893bd8",
      "DATA",
      [
        "storage",
        "00c81ff8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00893bd8",
      "DATA",
      [
        "storage",
        "00c82fc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892c14.md#insn-00892c20) · [`00892c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892c14.md#insn-00892c24) · [`00892c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892c14.md#insn-00892c28)
- 新版 [`00893bcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893bc0.md#insn-00893bcc) · [`00893bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893bc0.md#insn-00893bd0) · [`00893bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893bc0.md#insn-00893bd4)

~~~diff
- 00892c20 ["INT_ADD", "register:40f0:8", ["const:892c20:8", "const:4:8"]]
- 00892c20 ["CALL", null, ["callee:00c58f30:8"]]
+ 00893bcc ["INT_ADD", "register:40f0:8", ["const:893bcc:8", "const:4:8"]]
+ 00893bcc ["CALL", null, ["callee:00c58f30:8"]]
- 00892c20 bytes d0140f94
+ 00893bcc bytes d9140f94
- 00892c24 ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 00893bd0 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 00892c24 bytes 681f00f0
+ 00893bd0 bytes 681f00f0
- 00892c28 ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 00892c28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00892c28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00892c28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00893bd4 ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 00893bd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00893bd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00893bd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00892c28 bytes 08e13f91
+ 00893bd4 bytes 08213f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18244c72b5a01a85fcbcecb21e77a9bf"></a>

### [`00892cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892cf0.md) → [`00893c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893c9c.md) FUN_00893c9c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "00893cc0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00892d14",
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
      "00893cc0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00893cc0",
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

- 旧版 [`00892d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892cf0.md#insn-00892d14) · [`00892d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892cf0.md#insn-00892d20)
- 新版 [`00893cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893c9c.md#insn-00893cc0) · [`00893ccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893c9c.md#insn-00893ccc)

~~~diff
- 00892d14 ["INT_ADD", "register:40f0:8", ["const:892d14:8", "const:4:8"]]
- 00892d14 ["CALL", null, ["ram:47ad34:8"]]
+ 00893cc0 ["INT_ADD", "register:40f0:8", ["const:893cc0:8", "const:4:8"]]
+ 00893cc0 ["CALL", null, ["ram:47b054:8"]]
- 00892d14 bytes 08a0ef97
+ 00893cc0 bytes e59cef97
- 00892d20 ["INT_ADD", "register:40f0:8", ["const:892d20:8", "const:4:8"]]
- 00892d20 ["CALL", null, ["callee:0047d134:8"]]
+ 00893ccc ["INT_ADD", "register:40f0:8", ["const:893ccc:8", "const:4:8"]]
+ 00893ccc ["CALL", null, ["callee:0047d134:8"]]
- 00892d20 bytes 3da8ef97
+ 00893ccc bytes 1aa5ef97
~~~


<a id="compare-63087f385abc7d484fa8d8ae6479b594"></a>

### [`00892d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892d60.md) → [`00893d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d0c.md) FUN_00893d0c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0089135c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/0089135c.md) [`00891fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891fb8.md) [`00892f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892f04.md) [`008931a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008931a4.md) [`008932f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008932f4.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 7件 [`00892308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892308.md) [`00892f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892f64.md) [`00893eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893eb0.md) [`00894150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894150.md) [`008942a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/008942a0.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

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
      "definition_site": "00893d18",
      "incomplete_value": false,
      "site": "00893d1c",
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
      "definition_site": "00892d6c",
      "incomplete_value": false,
      "site": "00892d70",
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
      "00893d18",
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
      "00893d18",
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

- 旧版 [`00892d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892d60.md#insn-00892d70) · [`00892d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892d60.md#insn-00892d68) · [`00892d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892d60.md#insn-00892d6c)
- 新版 [`00893d1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d0c.md#insn-00893d1c) · [`00893d14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d0c.md#insn-00893d14) · [`00893d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d0c.md#insn-00893d18)

~~~diff
- 00892d70 ["INT_ADD", "register:40f0:8", ["const:892d70:8", "const:4:8"]]
- 00892d70 ["CALL", null, ["callee:00442c90:8"]]
+ 00893d1c ["INT_ADD", "register:40f0:8", ["const:893d1c:8", "const:4:8"]]
+ 00893d1c ["CALL", null, ["callee:00442c90:8"]]
- 00892d70 bytes 00bfee97
+ 00893d1c bytes ddbbee97
- 00892d68 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00893d14 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00892d68 bytes 20d1ffb0
+ 00893d14 bytes 20d1ffb0
- 00892d6c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00892d6c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00892d6c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00892d6c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00893d18 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00893d18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00893d18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00893d18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00892d6c bytes 00303e91
+ 00893d18 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d66bc6933c139923d2aacbd760b9180"></a>

### [`00892d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892d74.md) → [`00893d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d20.md) FUN_00893d20

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00893d28",
      "incomplete_value": false,
      "site": "00893d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892d7c",
      "incomplete_value": false,
      "site": "00892d80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:f8:8"
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
      "00893d2c",
      "DATA",
      [
        "storage",
        "00c820f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00893d2c",
      "DATA",
      [
        "storage",
        "00c830c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892d74.md#insn-00892d78) · [`00892d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892d74.md#insn-00892d7c)
- 新版 [`00893d24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d20.md#insn-00893d24) · [`00893d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d20.md#insn-00893d28)

~~~diff
- 00892d78 ["COPY", "register:4048:8", ["const:c82000:8"]]
+ 00893d24 ["COPY", "register:4048:8", ["const:c83000:8"]]
- 00892d78 bytes 891f0090
+ 00893d24 bytes 891f0090
- 00892d7c ["COPY", "tmp:0:8", ["const:f8:8"]]
- 00892d7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00892d7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00892d7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00893d28 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 00893d28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00893d28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00893d28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00892d7c bytes 29e10391
+ 00893d28 bytes 29210391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95c573570639fe652e9bdc9be255c2f3"></a>

### [`00892d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892d94.md) → [`00893d40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d40.md) FUN_00893d40

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00893d48",
      "incomplete_value": false,
      "site": "00893d4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892d9c",
      "incomplete_value": false,
      "site": "00892da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:f8:8"
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
      "00893d4c",
      "DATA",
      [
        "storage",
        "00c820f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00893d4c",
      "DATA",
      [
        "storage",
        "00c830c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892d94.md#insn-00892d98) · [`00892d9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892d94.md#insn-00892d9c) · [`00892dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892d94.md#insn-00892dc0)
- 新版 [`00893d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d40.md#insn-00893d44) · [`00893d48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d40.md#insn-00893d48) · [`00893d6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d40.md#insn-00893d6c)

~~~diff
- 00892d98 ["COPY", "register:4048:8", ["const:c82000:8"]]
+ 00893d44 ["COPY", "register:4048:8", ["const:c83000:8"]]
- 00892d98 bytes 891f0090
+ 00893d44 bytes 891f0090
- 00892d9c ["COPY", "tmp:0:8", ["const:f8:8"]]
- 00892d9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00892d9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00892d9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00893d48 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 00893d48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00893d48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00893d48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00892d9c bytes 29e10391
+ 00893d48 bytes 29210391
- 00892dc0 ["INT_ADD", "register:40f0:8", ["const:892dc0:8", "const:4:8"]]
- 00892dc0 ["CALL", null, ["callee:00c58f50:8"]]
+ 00893d6c ["INT_ADD", "register:40f0:8", ["const:893d6c:8", "const:4:8"]]
+ 00893d6c ["CALL", null, ["callee:00c58f50:8"]]
- 00892dc0 bytes 70140f94
+ 00893d6c bytes 79140f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d4e2446d427f62b50bc54a8ad74eebe"></a>

### [`00892dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892dd4.md) → [`00893d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d80.md) FUN_00893d80

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00893db0",
      "incomplete_value": false,
      "site": "00893db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892e04",
      "incomplete_value": false,
      "site": "00892e04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:f8:8"
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
      "00893db0",
      "DATA",
      [
        "storage",
        "00c820f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00893db0",
      "DATA",
      [
        "storage",
        "00c830c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892dd4.md#insn-00892de8) · [`00892df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892dd4.md#insn-00892df4) · [`00892df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892dd4.md#insn-00892df8)
- 新版 [`00893d94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d80.md#insn-00893d94) · [`00893da0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d80.md#insn-00893da0) · [`00893da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d80.md#insn-00893da4)

~~~diff
- 00892de8 ["INT_ADD", "register:40f0:8", ["const:892de8:8", "const:4:8"]]
- 00892de8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00893d94 ["INT_ADD", "register:40f0:8", ["const:893d94:8", "const:4:8"]]
+ 00893d94 ["CALL", null, ["callee:00c58f30:8"]]
- 00892de8 bytes 5e140f94
+ 00893d94 bytes 67140f94
- 00892df4 ["COPY", "register:4058:8", ["const:c82000:8"]]
+ 00893da0 ["COPY", "register:4058:8", ["const:c83000:8"]]
- 00892df4 bytes 8b1f0090
+ 00893da0 bytes 8b1f0090
- 00892df8 ["COPY", "tmp:0:8", ["const:f8:8"]]
- 00892df8 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00892df8 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00892df8 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00893da4 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 00893da4 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00893da4 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00893da4 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00892df8 bytes 6be10391
+ 00893da4 bytes 6b210391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4810b404bae557c513c3e0de2fb861bd"></a>

### [`00892e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892e58.md) → [`00893e04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893e04.md) FUN_00893e04

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00893e24",
      "incomplete_value": false,
      "site": "00893e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892e78",
      "incomplete_value": false,
      "site": "00892e78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:f8:8"
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
      "00893e24",
      "DATA",
      [
        "storage",
        "00c820f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00893e24",
      "DATA",
      [
        "storage",
        "00c830c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892e58.md#insn-00892e68) · [`00892e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892e58.md#insn-00892e6c) · [`00892e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892e58.md#insn-00892e74)
- 新版 [`00893e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893e04.md#insn-00893e14) · [`00893e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893e04.md#insn-00893e18)

~~~diff
- 00892e68 ["COPY", "register:4048:8", ["const:c82000:8"]]
+ 00893e14 ["COPY", "register:4048:8", ["const:c83000:8"]]
- 00892e68 bytes 891f0090
+ 00893e14 bytes 891f0090
- 00892e6c ["COPY", "tmp:0:8", ["const:f8:8"]]
- 00892e6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00892e6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00892e6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00893e18 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 00893e18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00893e18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00893e18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00892e6c bytes 29e10391
+ 00893e18 bytes 29210391
- 00892e74 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00892e74 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65aecc8753b6b34f4df333fb059d5cb7"></a>

### [`008931a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008931a4.md) → [`00894150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894150.md) FUN_00894150

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00891bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891bc4.md) [`00892d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892d60.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00892b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892b70.md) [`00893d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d0c.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 53.33% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893254"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00894200"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008941b0",
      "incomplete_value": false,
      "site": "008941b4",
      "value": [
        "leaf",
        "const:2:8"
      ]
    },
    "old": null,
    "ordinal": 7,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00893208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008931a4.md#insn-00893208) · [`00893254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008931a4.md#insn-00893254)
- 新版 [`008941b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894150.md#insn-008941b4) · [`00894200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894150.md#insn-00894200)

~~~diff
- 00893208 ["INT_ADD", "register:40f0:8", ["const:893208:8", "const:4:8"]]
- 00893208 ["CALL", null, ["callee:00892b70:8"]]
+ 008941b4 ["INT_ADD", "register:40f0:8", ["const:8941b4:8", "const:4:8"]]
+ 008941b4 ["CALL", null, ["callee:00892b70:8"]]
- 00893208 bytes 6ffaff97
+ 008941b4 bytes 6ffaff97
- 00893254 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:20:8"]]
- 00893254 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:8"]]
- 00893254 bytes 001100fd
+ 00894200 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:20:8"]]
+ 00894200 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:8"]]
+ 00894200 bytes 001100fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-330d22abc07dfb09f12ce12591fa2345"></a>

### [`008932d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008932d4.md) → [`00894280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894280.md) FUN_00894280

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00894284",
      "incomplete_value": false,
      "site": "00894288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008932d8",
      "incomplete_value": false,
      "site": "008932dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
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
      "00894288",
      "DATA",
      [
        "storage",
        "00c821f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00894288",
      "DATA",
      [
        "storage",
        "00c831c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008932d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008932d4.md#insn-008932d4) · [`008932d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008932d4.md#insn-008932d8)
- 新版 [`00894280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894280.md#insn-00894280) · [`00894284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894280.md#insn-00894284)

~~~diff
- 008932d4 ["COPY", "register:4040:8", ["const:c82000:8"]]
+ 00894280 ["COPY", "register:4040:8", ["const:c83000:8"]]
- 008932d4 bytes 681f00f0
+ 00894280 bytes 681f00f0
- 008932d8 ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 008932d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008932d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008932d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00894284 ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 00894284 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00894284 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00894284 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008932d8 bytes 08e10791
+ 00894284 bytes 08210791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2eceedf94bfb384fe9c483a93fc6cc56"></a>

### [`008932f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008932f4.md) → [`008942a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/008942a0.md) FUN_008942a0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00891bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891bc4.md) [`00892d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892d60.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00892b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00892/00892b70.md) [`00893d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d0c.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 42.86% / 新版 46.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0089330c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008932f4.md#insn-0089330c) · [`00893314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008932f4.md#insn-00893314) · [`00893318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008932f4.md#insn-00893318)
- 新版 [`008942b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/008942a0.md#insn-008942b8) · [`008942c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/008942a0.md#insn-008942c0) · [`008942c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/008942a0.md#insn-008942c4)

~~~diff
- 0089330c ["INT_ADD", "register:40f0:8", ["const:89330c:8", "const:4:8"]]
- 0089330c ["CALL", null, ["callee:00b3a880:8"]]
+ 008942b8 ["INT_ADD", "register:40f0:8", ["const:8942b8:8", "const:4:8"]]
+ 008942b8 ["CALL", null, ["callee:00b3a880:8"]]
- 0089330c bytes 60990a94
+ 008942b8 bytes 72990a94
- 00893314 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00893314 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 008942c0 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 008942c0 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00893314 bytes 88020034
+ 008942c0 bytes 88020034
- 00893318 ["INT_ADD", "register:40f0:8", ["const:893318:8", "const:4:8"]]
- 00893318 ["CALL", null, ["callee:008524fc:8"]]
+ 008942c4 ["INT_ADD", "register:40f0:8", ["const:8942c4:8", "const:4:8"]]
+ 008942c4 ["CALL", null, ["callee:008524fc:8"]]
- 00893318 bytes 8ef8fe97
+ 008942c4 bytes 8ef8fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37bd76333464c4fb474bcdb09447e9b2"></a>

### [`008934e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008934e4.md) → [`00894490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894490.md) FUN_00894490

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008944a4",
      "incomplete_value": false,
      "site": "008944a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008934f8",
      "incomplete_value": false,
      "site": "008934fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "008944a8",
      "DATA",
      [
        "storage",
        "00c822f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008944a8",
      "DATA",
      [
        "storage",
        "00c832c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008934f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008934e4.md#insn-008934f0) · [`008934f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008934e4.md#insn-008934f4) · [`008934f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008934e4.md#insn-008934f8)
- 新版 [`0089449c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894490.md#insn-0089449c) · [`008944a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894490.md#insn-008944a0) · [`008944a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894490.md#insn-008944a4)

~~~diff
- 008934f0 ["INT_ADD", "register:40f0:8", ["const:8934f0:8", "const:4:8"]]
- 008934f0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0089449c ["INT_ADD", "register:40f0:8", ["const:89449c:8", "const:4:8"]]
+ 0089449c ["CALL", null, ["callee:00c58f30:8"]]
- 008934f0 bytes 9c120f94
+ 0089449c bytes a5120f94
- 008934f4 ["COPY", "register:4040:8", ["const:c82000:8"]]
+ 008944a0 ["COPY", "register:4040:8", ["const:c83000:8"]]
- 008934f4 bytes 681f00f0
+ 008944a0 bytes 681f00f0
- 008934f8 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 008934f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008934f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008934f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008944a4 ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 008944a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008944a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008944a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008934f8 bytes 08e10b91
+ 008944a4 bytes 08210b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f748c9b4f5b35a69d81c31d7e05094a"></a>

### [`00893550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893550.md) → [`008944fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/008944fc.md) FUN_008944fc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 35.71% / 新版 35.71%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893550"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893550"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893554"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00893550",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00893554",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00893574",
      "DATA",
      [
        "storage",
        "00c82378",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008944fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00894500",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00894520",
      "DATA",
      [
        "storage",
        "00c83348",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00893550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893550.md#insn-00893550) · [`00893554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893550.md#insn-00893554) · [`00893564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893550.md#insn-00893564)
- 新版 [`00894510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/008944fc.md#insn-00894510)

~~~diff
- 00893550 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00893550 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00893550 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00893550 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00893550 bytes fd7bbea9
- 00893554 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00893554 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00893554 bytes f30b00f9
- 00893564 ["INT_ADD", "register:40f0:8", ["const:893564:8", "const:4:8"]]
- 00893564 ["CALL", null, ["callee:00c58f30:8"]]
+ 00894510 ["INT_ADD", "register:40f0:8", ["const:894510:8", "const:4:8"]]
+ 00894510 ["CALL", null, ["callee:00c58f30:8"]]
- 00893564 bytes 7f120f94
+ 00894510 bytes 88120f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31dbf29603d9db5087da450a5513be1e"></a>

### [`008935a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008935a8.md) → [`00894554`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894554.md) FUN_00894554

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce60.md) [`0047cf48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cf48.md) [`00892d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892d60.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d180.md) [`0047d268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d268.md) [`00893d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00893/00893d0c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.48% / 新版 90.48%

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
      "site": "00894584",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008935d8",
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
      "site": "00894590",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008935e4",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "00894584",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00894590",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00894584",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00894590",
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

- 旧版 [`008935d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008935a8.md#insn-008935d8) · [`008935e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008935a8.md#insn-008935e4) · [`008935dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008935a8.md#insn-008935dc)
- 新版 [`00894584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894554.md#insn-00894584) · [`00894590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894554.md#insn-00894590) · [`00894588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894554.md#insn-00894588)

~~~diff
- 008935d8 ["INT_ADD", "register:40f0:8", ["const:8935d8:8", "const:4:8"]]
- 008935d8 ["CALL", null, ["ram:47ad34:8"]]
+ 00894584 ["INT_ADD", "register:40f0:8", ["const:894584:8", "const:4:8"]]
+ 00894584 ["CALL", null, ["ram:47b054:8"]]
- 008935d8 bytes d79def97
+ 00894584 bytes b49aef97
- 008935e4 ["INT_ADD", "register:40f0:8", ["const:8935e4:8", "const:4:8"]]
- 008935e4 ["CALL", null, ["ram:47ad34:8"]]
+ 00894590 ["INT_ADD", "register:40f0:8", ["const:894590:8", "const:4:8"]]
+ 00894590 ["CALL", null, ["ram:47b054:8"]]
- 008935e4 bytes d49def97
+ 00894590 bytes b19aef97
- 008935dc ["INT_ADD", "register:40f0:8", ["const:8935dc:8", "const:4:8"]]
- 008935dc ["CALL", null, ["callee:0047d180:8"]]
+ 00894588 ["INT_ADD", "register:40f0:8", ["const:894588:8", "const:4:8"]]
+ 00894588 ["CALL", null, ["callee:0047d180:8"]]
- 008935dc bytes 21a6ef97
+ 00894588 bytes fea2ef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4018ba0c42d5647d283bbd5a9450bc2d"></a>

### [`00893624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893624.md) → [`008945d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/008945d0.md) _INIT_167

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.53% / 新版 78.53%

CFGの説明率　旧版 45.65% / 新版 58.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893654"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893668"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0089366c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00893654",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00893660",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00893668",
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
      "00894600",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0089460c",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "00894614",
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

- 旧版 [`00893654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893624.md#insn-00893654) · [`00893668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893624.md#insn-00893668) · [`0089366c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893624.md#insn-0089366c)

~~~diff
- 00893654 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00893654 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00893654 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00893654 bytes a9831ff8
- 00893668 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00893668 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00893668 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00893668 bytes ea130278
- 0089366c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 0089366c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 0089366c bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4063cbd4bc120685bc64d5be4f16740"></a>

### [`008939b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008939b4.md) → [`00894960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894960.md) FUN_00894960

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce60.md) [`0047cf48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cf48.md) [`0083f2dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f2dc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d180.md) [`0047d268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d268.md) [`00840288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00840/00840288.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.10% / 新版 93.10%

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
      "site": "008949b4",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00893a08",
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
      "site": "008949c0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00893a14",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "008949b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008949c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "008949b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "008949c0",
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

- 旧版 [`00893a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008939b4.md#insn-00893a08) · [`00893a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008939b4.md#insn-00893a14) · [`008939bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008939b4.md#insn-008939bc)
- 新版 [`008949b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894960.md#insn-008949b4) · [`008949c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894960.md#insn-008949c0) · [`00894968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894960.md#insn-00894968)

~~~diff
- 00893a08 ["INT_ADD", "register:40f0:8", ["const:893a08:8", "const:4:8"]]
- 00893a08 ["CALL", null, ["ram:47ad34:8"]]
+ 008949b4 ["INT_ADD", "register:40f0:8", ["const:8949b4:8", "const:4:8"]]
+ 008949b4 ["CALL", null, ["ram:47b054:8"]]
- 00893a08 bytes cb9cef97
+ 008949b4 bytes a899ef97
- 00893a14 ["INT_ADD", "register:40f0:8", ["const:893a14:8", "const:4:8"]]
- 00893a14 ["CALL", null, ["ram:47ad34:8"]]
+ 008949c0 ["INT_ADD", "register:40f0:8", ["const:8949c0:8", "const:4:8"]]
+ 008949c0 ["CALL", null, ["ram:47b054:8"]]
- 00893a14 bytes c89cef97
+ 008949c0 bytes a599ef97
- 008939bc ["INT_ADD", "register:40f0:8", ["const:8939bc:8", "const:4:8"]]
- 008939bc ["CALL", null, ["callee:008524fc:8"]]
+ 00894968 ["INT_ADD", "register:40f0:8", ["const:894968:8", "const:4:8"]]
+ 00894968 ["CALL", null, ["callee:008524fc:8"]]
- 008939bc bytes e5f6fe97
+ 00894968 bytes e5f6fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd06a6634b2ab934dfbbb30c18d93696"></a>

### [`00893a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893a28.md) → [`008949d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/008949d4.md) FUN_008949d4

採用 · 移動量 `+0xfac` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048f3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048f/0048f3d8.md) [`00492c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492c40.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048f6f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f6f8.md) [`00492f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00492/00492f60.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.51% / 新版 75.51%

CFGの説明率　旧版 59.26% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893b24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893b28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893b30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00893a68",
      "DATA",
      [
        "storage",
        "002f3e32",
        "switchD_00893a70::switchdataD_002f3e32",
        "byte"
      ]
    ],
    [
      "00894a1c",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00893a98"
      ]
    ],
    [
      "00894a1c",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00893ac4"
      ]
    ]
  ],
  "added": [
    [
      "00894a14",
      "DATA",
      [
        "storage",
        "002f3e72",
        "switchD_00894a1c::switchdataD_002f3e72",
        "byte"
      ]
    ],
    [
      "00894a1c",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00894a44"
      ]
    ],
    [
      "00894a1c",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00894a70"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00893a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893a28.md#insn-00893a74) · [`00893a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893a28.md#insn-00893a98) · [`00893aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893a28.md#insn-00893aac)
- 新版 [`00894a20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/008949d4.md#insn-00894a20)

~~~diff
- 00893a74 ["INT_ADD", "register:40f0:8", ["const:893a74:8", "const:4:8"]]
- 00893a74 ["CALL", null, ["ram:48cd38:8"]]
+ 00894a20 ["INT_ADD", "register:40f0:8", ["const:894a20:8", "const:4:8"]]
+ 00894a20 ["CALL", null, ["ram:48d058:8"]]
- 00893a74 bytes b1e4ef97
+ 00894a20 bytes 8ee1ef97
- 00893a98 ["INT_ADD", "register:40f0:8", ["const:893a98:8", "const:4:8"]]
- 00893a98 ["CALL", null, ["ram:48cd38:8"]]
- 00893a98 bytes a8e4ef97
- 00893aac ["INT_ADD", "register:40f0:8", ["const:893aac:8", "const:4:8"]]
- 00893aac ["CALL", null, ["ram:48cd38:8"]]
- 00893aac bytes a3e4ef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-817fa5d154d50c37577ba93e82051dac"></a>

### [`00893bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893bdc.md) → [`00894b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894b88.md) FUN_00894b88

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0089d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089d/0089d520.md) · 呼出先 14件 [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f46c.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047cacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cacc.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md)
- 新版 呼出元 1件 [`0089e4cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089e/0089e4cc.md) · 呼出先 14件 [`0043ecac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043ecac.md) [`0043f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f78c.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047cdec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047c/0047cdec.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.39% / 新版 82.39%

CFGの説明率　旧版 77.50% / 新版 79.49%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 13件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893d30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00894cdc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00893d4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00894bc0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "00894bcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00894bdc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ],
  "added": [
    [
      "00894bc0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048d058"
      ]
    ],
    [
      "00894bcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00894bdc",
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

- 旧版 [`00893c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893bdc.md#insn-00893c14) · [`00893c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893bdc.md#insn-00893c20) · [`00893c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893bdc.md#insn-00893c30)
- 新版 [`00894bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894b88.md#insn-00894bc0) · [`00894bcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894b88.md#insn-00894bcc) · [`00894bdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894b88.md#insn-00894bdc)

~~~diff
- 00893c14 ["INT_ADD", "register:40f0:8", ["const:893c14:8", "const:4:8"]]
- 00893c14 ["CALL", null, ["ram:48cd38:8"]]
+ 00894bc0 ["INT_ADD", "register:40f0:8", ["const:894bc0:8", "const:4:8"]]
+ 00894bc0 ["CALL", null, ["ram:48d058:8"]]
- 00893c14 bytes 49e4ef97
+ 00894bc0 bytes 26e1ef97
- 00893c20 ["INT_ADD", "register:40f0:8", ["const:893c20:8", "const:4:8"]]
- 00893c20 ["CALL", null, ["ram:47ad34:8"]]
+ 00894bcc ["INT_ADD", "register:40f0:8", ["const:894bcc:8", "const:4:8"]]
+ 00894bcc ["CALL", null, ["ram:47b054:8"]]
- 00893c20 bytes 459cef97
+ 00894bcc bytes 2299ef97
- 00893c30 ["INT_ADD", "register:40f0:8", ["const:893c30:8", "const:4:8"]]
- 00893c30 ["CALL", null, ["ram:48cd38:8"]]
+ 00894bdc ["INT_ADD", "register:40f0:8", ["const:894bdc:8", "const:4:8"]]
+ 00894bdc ["CALL", null, ["ram:48d058:8"]]
- 00893c30 bytes 42e4ef97
+ 00894bdc bytes 1fe1ef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c889706b2db6e45945a490fa64ad84e"></a>

### [`00893e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893e14.md) → [`00894dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00894/00894dc0.md) FUN_00894dc0

採用 · 移動量 `+0xfac` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 53件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043f414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f414.md) [`0043f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f46c.md) [`0043f478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f478.md)
- 新版 呼出元 0件  · 呼出先 53件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`0043ecac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043ecac.md) [`0043f734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f734.md) [`0043f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f78c.md) [`0043f798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f798.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 54.12% / 新版 54.12%

CFGの説明率　旧版 24.95% / 新版 25.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 31件, `call_target` 5件, `store_value` 9件, `unresolved_branch_alignment` 67件, `unresolved_call_alignment` 174件, `unresolved_store_alignment` 24件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893e18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893e18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893e1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00893e18",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00893e1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00893e20",
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
      "00894dc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00894dc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00894dcc",
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

- 旧版 [`00893e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893e14.md#insn-00893e18) · [`00893e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893e14.md#insn-00893e1c) · [`00893e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893e14.md#insn-00893e20)

~~~diff
- 00893e18 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00893e18 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00893e18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00893e18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00893e18 bytes fd7b0ea9
- 00893e1c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:f0:8"]]
- 00893e1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00893e1c bytes f57b00f9
- 00893e20 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00893e20 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00893e20 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00893e20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00893e20 bytes f44f10a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd144543d953dd5221779f136b6b3f22"></a>

### [`00895a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md) → [`008969d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00896/008969d4.md) FUN_008969d4

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 99件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md) [`0043f7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f7cc.md)
- 新版 呼出元 0件  · 呼出先 99件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`0043ecac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043ecac.md) [`0043efc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043efc0.md) [`0043faec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043faec.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 47.99% / 新版 47.99%

CFGの説明率　旧版 17.80% / 新版 17.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 37件, `call_target` 3件, `store_condition` 1件, `unresolved_branch_alignment` 90件, `unresolved_call_alignment` 154件, `unresolved_store_alignment` 68件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00895a80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00895a84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00895a88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00895a78",
      "READ",
      [
        "storage",
        "002a066c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00895a7c",
      "READ",
      [
        "storage",
        "002a0671",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00895a80",
      "WRITE",
      [
        "storage",
        "Stack[-0x110]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00896a24",
      "READ",
      [
        "storage",
        "002a06ac",
        null,
        "string"
      ]
    ],
    [
      "00896a28",
      "READ",
      [
        "storage",
        "002a06b1",
        null,
        "string"
      ]
    ],
    [
      "00896a2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x110]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00895a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md#insn-00895a80) · [`00895a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md#insn-00895a84) · [`00895a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md#insn-00895a88)

~~~diff
- 00895a80 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00895a80 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:a0:8"]]
- 00895a80 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00895a80 bytes e8830239
- 00895a84 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00895a84 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00895a84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:ae:8"]]
- 00895a84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00895a84 bytes ffbb0239
- 00895a88 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00895a88 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:1:8"]]
- 00895a88 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00895a88 bytes aa1200f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bdad1c567b8d7f59f41588629335f99"></a>

### [`00897748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00897/00897748.md) → [`008986f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00898/008986f4.md) FUN_008986f4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00895a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`008969d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00896/008969d4.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 56.25% / 新版 47.37%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "008977a8",
      "incomplete_value": false,
      "site": "008977b0",
      "value": [
        "leaf",
        "const:48:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008977b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00897/00897748.md#insn-008977b0) · [`00897758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00897/00897748.md#insn-00897758) · [`0089776c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00897/00897748.md#insn-0089776c)
- 新版 [`0089875c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00898/008986f4.md#insn-0089875c) · [`00898718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00898/008986f4.md#insn-00898718)

~~~diff
- 008977b0 ["INT_ADD", "register:40f0:8", ["const:8977b0:8", "const:4:8"]]
- 008977b0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0089875c ["INT_ADD", "register:40f0:8", ["const:89875c:8", "const:4:8"]]
+ 0089875c ["CALL", null, ["callee:00c58f30:8"]]
- 008977b0 bytes ec010f94
+ 0089875c bytes f5010f94
- 00897758 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00897758 bytes fd030091
- 0089776c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0089776c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00898718 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00898718 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0089776c bytes c80000b5
+ 00898718 bytes c80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff122c2fa0fb9b1bc53a6ca2b3fead07"></a>

### [`0089b29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089b29c.md) → [`0089c248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089c/0089c248.md) FUN_0089c248

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 2件 [`008978e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00897/008978e4.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00898890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00898/00898890.md) [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-5a18804fbb886388715760e8b67d279d"></a>

### [`0089bce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md) → [`0089cc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089c/0089cc90.md) FUN_0089cc90

採用 · 移動量 `+0xfac` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 69件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md)
- 新版 呼出元 0件  · 呼出先 69件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00442e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442e98.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.33% / 新版 69.33%

CFGの説明率　旧版 22.43% / 新版 24.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 33件, `call_target` 2件, `store_condition` 2件, `store_value` 2件, `unresolved_branch_alignment` 36件, `unresolved_call_alignment` 57件, `unresolved_store_alignment` 52件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0089bce8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0089bce8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0089bcec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0089bce8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0089bcec",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0089bcf0",
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
      "0089cc94",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0089cc98",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0089cc9c",
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

- 旧版 [`0089bce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md#insn-0089bce8) · [`0089bcec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md#insn-0089bcec) · [`0089bcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md#insn-0089bcf0)

~~~diff
- 0089bce8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0089bce8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0089bce8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:180:8"]]
- 0089bce8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0089bce8 bytes fd7b18a9
- 0089bcec ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0089bcec ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0089bcec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:190:8"]]
- 0089bcec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0089bcec bytes fc6f19a9
- 0089bcf0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0089bcf0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0089bcf0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1a0:8"]]
- 0089bcf0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0089bcf0 bytes fa671aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9866fba836cc72e689089a072650acf"></a>

### [`0089d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089d/0089d520.md) → [`0089e4cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089e/0089e4cc.md) FUN_0089e4cc

採用 · 移動量 `+0xfac` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 52件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00472bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472bec.md) [`00472bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472bfc.md) [`00472d9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472d9c.md)
- 新版 呼出元 0件  · 呼出先 52件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00472f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00472/00472f0c.md) [`00472f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00472/00472f1c.md) [`004730bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00473/004730bc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.17% / 新版 70.17%

CFGの説明率　旧版 39.20% / 新版 37.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `call_target` 6件, `store_condition` 3件, `store_value` 3件, `unresolved_branch_alignment` 25件, `unresolved_call_alignment` 47件, `unresolved_store_alignment` 40件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0089d5dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0089d5e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0089d5e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0089d578",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089e578"
      ]
    ],
    [
      "unmatched:0089d5dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x100]",
        null,
        null
      ]
    ],
    [
      "unmatched:0089d5e4",
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
      "0089e524",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089e578"
      ]
    ],
    [
      "0089e588",
      "WRITE",
      [
        "storage",
        "Stack[-0x100]",
        null,
        null
      ]
    ],
    [
      "0089e590",
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

- 旧版 [`0089d5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089d/0089d520.md#insn-0089d5dc) · [`0089d5e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089d/0089d520.md#insn-0089d5e4) · [`0089d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089d/0089d520.md#insn-0089d5e8)

~~~diff
- 0089d5dc ["COPY", "tmp:0:4", ["register:4040:4"]]
- 0089d5dc ["INT_ADD", "tmp:1:8", ["register:8:8", "const:30:8"]]
- 0089d5dc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0089d5dc bytes e8c30039
- 0089d5e4 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0089d5e4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:31:8"]]
- 0089d5e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 0089d5e4 bytes e91303b8
- 0089d5e8 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 0089d5e8 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:35:8"]]
- 0089d5e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 0089d5e8 bytes e8530378
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6610f91a4f526df94b6ef9f070468d72"></a>

### [`008a3dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a3/008a3dc0.md) → [`008a4d6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008a4/008a4d6c.md) FUN_008a4d6c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 45.00% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008a3df8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008a3e54"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008a4da4"
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
      "unmatched:008a3df8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008a4dcc"
      ]
    ],
    [
      "unmatched:008a3e54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008a4e0c"
      ]
    ]
  ],
  "added": [
    [
      "008a4da4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008a4dcc"
      ]
    ],
    [
      "008a4e00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008a4e0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a3df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a3/008a3dc0.md#insn-008a3df8) · [`008a3e54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a3/008a3dc0.md#insn-008a3e54)
- 新版 [`008a4da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008a4/008a4d6c.md#insn-008a4da4)

~~~diff
- 008a3df8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008a3df8 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 008a3df8 bytes 480100b4
- 008a3e54 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008a3e54 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 008a3e54 bytes 680000b4
+ 008a4da4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 008a4da4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 008a4da4 bytes 480100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

