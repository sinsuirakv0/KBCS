# v16.0.2 → v16.0.3 · 命令位置の検査未完了 (10)

[一覧の目次](README.md)

<a id="compare-a544d64df3140cdad43b14de887e1ecc"></a>

### [`008bc284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc284.md) → [`008bd230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bd/008bd230.md) FUN_008bd230

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008bbe2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bb/008bbe2c.md) [`00a8319c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a83/00a8319c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`008bcdd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bc/008bcdd8.md) [`00a84190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a84/00a84190.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008bc284"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008bc284"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008bd230"
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
      "unmatched:008bc284",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008bc290",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:008bc294",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043bad8"
      ]
    ]
  ],
  "added": [
    [
      "008bd230",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008bd23c",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ],
    [
      "008bd240",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043bad8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008bc284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc284.md#insn-008bc284) · [`008bc294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc284.md#insn-008bc294)
- 新版 [`008bd230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bd/008bd230.md#insn-008bd230)

~~~diff
- 008bc284 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008bc284 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008bc284 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 008bc284 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008bc284 bytes fd7bbfa9
- 008bc294 ["INT_ADD", "register:40f0:8", ["const:8bc294:8", "const:4:8"]]
- 008bc294 ["CALL", null, ["callee:0043bad8:8"]]
- 008bc294 bytes 49fded97
+ 008bd230 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 008bd230 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 008bd230 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 008bd230 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 008bd230 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6750d43f2a74bbf4cfe2ef39d4443eb"></a>

### [`008bc298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc298.md) → [`008bd244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bd/008bd244.md) FUN_008bd244

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008b9624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b9624.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`008ba5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba5d0.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 91.01% / 新版 91.01%

CFGの説明率　旧版 58.82% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008bc2d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008bd280"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008bc390"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008bc2d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008bd298"
      ]
    ],
    [
      "unmatched:008bc390",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:008bc3cc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "008bd280",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008bd298"
      ]
    ],
    [
      "008bd33c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "008bd378",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008bc2d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc298.md#insn-008bc2d4) · [`008bc390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc298.md#insn-008bc390) · [`008bc3cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bc/008bc298.md#insn-008bc3cc)

~~~diff
- 008bc2d4 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 008bc2d4 bytes c0000054
- 008bc390 ["COPY", "register:0:8", ["register:4040:8"]]
- 008bc390 ["INT_ADD", "register:40f0:8", ["const:8bc390:8", "const:4:8"]]
- 008bc390 ["CALLIND", null, ["register:0:8"]]
- 008bc390 bytes 00013fd6
- 008bc3cc ["COPY", "register:0:8", ["register:4040:8"]]
- 008bc3cc ["INT_ADD", "register:40f0:8", ["const:8bc3cc:8", "const:4:8"]]
- 008bc3cc ["CALLIND", null, ["register:0:8"]]
- 008bc3cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-936b0ba9a5a08bc31e1c2a5f24d9ce6d"></a>

### [`008c8934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c8/008c8934.md) → [`008c98e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c9/008c98e0.md) FUN_008c98e0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008c5df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c5/008c5df8.md) · 呼出先 4件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`009df650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df650.md) [`009e1014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e1014.md) [`009e2fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e2/009e2fe8.md)
- 新版 呼出元 1件 [`008c6da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c6/008c6da4.md) · 呼出先 4件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`009e05fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e05fc.md) [`009e1fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e1fc0.md) [`009e3f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e3/009e3f94.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 83.10% / 新版 83.10%

CFGの説明率　旧版 38.89% / 新版 35.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008c8a4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "008c99f8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008c8a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c8/008c8934.md#insn-008c8a4c) · [`008c8950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c8/008c8934.md#insn-008c8950)
- 新版 [`008c99f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c9/008c98e0.md#insn-008c99f8) · [`008c98fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c9/008c98e0.md#insn-008c98fc)

~~~diff
- 008c8a4c ["COPY", "register:0:8", ["register:40f0:8"]]
- 008c8a4c ["RETURN", null, ["register:0:8"]]
- 008c8a4c bytes c0035fd6
+ 008c99f8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 008c99f8 ["RETURN", null, ["register:0:8"]]
+ 008c99f8 bytes c0035fd6
- 008c8950 ["INT_ADD", "register:40f0:8", ["const:8c8950:8", "const:4:8"]]
- 008c8950 ["CALL", null, ["callee:008524fc:8"]]
+ 008c98fc ["INT_ADD", "register:40f0:8", ["const:8c98fc:8", "const:4:8"]]
+ 008c98fc ["CALL", null, ["callee:008524fc:8"]]
- 008c8950 bytes 0023fe97
+ 008c98fc bytes 0023fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0f42facd2decef4d1ebd6dac8233368"></a>

### [`008cb964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb964.md) → [`008cc910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cc/008cc910.md) FUN_008cc910

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cb96c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cb974"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008cc918"
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
      "unmatched:008cb96c",
      "DATA",
      [
        "storage",
        "00c83e38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cc918",
      "DATA",
      [
        "storage",
        "00c84e08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb964.md#insn-008cb96c) · [`008cb974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb964.md#insn-008cb974) · [`008cb978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb964.md#insn-008cb978)

~~~diff
- 008cb96c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008cb96c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008cb96c bytes 280000f9
- 008cb974 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 008cb974 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008cb974 bytes 2080803c
- 008cb978 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008cb978 ["RETURN", null, ["register:0:8"]]
- 008cb978 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a91e4902b45cfa99d4f11ede3df47a5"></a>

### [`008cbc44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbc44.md) → [`008ccbf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cc/008ccbf0.md) FUN_008ccbf0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008bdb58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bd/008bdb58.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`008beb04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008be/008beb04.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbc44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbc44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008ccbf0"
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
      "unmatched:008cbc44",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008cbc50",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:008cbc54",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043bad8"
      ]
    ]
  ],
  "added": [
    [
      "008ccbf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008ccbfc",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ],
    [
      "008ccc00",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043bad8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cbc44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbc44.md#insn-008cbc44) · [`008cbc54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbc44.md#insn-008cbc54)
- 新版 [`008ccbf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cc/008ccbf0.md#insn-008ccbf0)

~~~diff
- 008cbc44 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008cbc44 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008cbc44 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 008cbc44 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008cbc44 bytes fd7bbfa9
- 008cbc54 ["INT_ADD", "register:40f0:8", ["const:8cbc54:8", "const:4:8"]]
- 008cbc54 ["CALL", null, ["callee:0043bad8:8"]]
- 008cbc54 bytes d9beed97
+ 008ccbf0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 008ccbf0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 008ccbf0 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 008ccbf0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 008ccbf0 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77050fd7892d5f9626f96373e079dd80"></a>

### [`008cbc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbc5c.md) → [`008ccc08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cc/008ccc08.md) FUN_008ccc08

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbc80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbc80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008ccc2c"
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
      "unmatched:008cbc80",
      "DATA",
      [
        "storage",
        "00c83eb8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008cbc84",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008cbc88",
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
      "008ccc2c",
      "DATA",
      [
        "storage",
        "00c84e88",
        null,
        "undefined *"
      ]
    ],
    [
      "008ccc30",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008ccc34",
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

- 旧版 [`008cbc80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbc5c.md#insn-008cbc80) · [`008cbc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbc5c.md#insn-008cbc8c)
- 新版 [`008ccc2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cc/008ccc08.md#insn-008ccc2c)

~~~diff
- 008cbc80 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008cbc80 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008cbc80 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008cbc80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008cbc80 bytes 082400a9
- 008cbc8c ["COPY", "register:0:8", ["register:40f0:8"]]
- 008cbc8c ["RETURN", null, ["register:0:8"]]
- 008cbc8c bytes c0035fd6
+ 008ccc2c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008ccc2c ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 008ccc2c ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 008ccc2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008ccc2c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c11f70827e2f0eae4abe37a97b108cfa"></a>

### [`008cbc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbc90.md) → [`008ccc3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cc/008ccc3c.md) FUN_008ccc3c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbc9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbc9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008ccc48"
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
      "unmatched:008cbc9c",
      "DATA",
      [
        "storage",
        "00c83eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ccc48",
      "DATA",
      [
        "storage",
        "00c84e88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cbc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbc90.md#insn-008cbc9c) · [`008cbca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbc90.md#insn-008cbca0)
- 新版 [`008ccc48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cc/008ccc3c.md#insn-008ccc48)

~~~diff
- 008cbc9c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008cbc9c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 008cbc9c ["COPY", "tmp:2:8", ["register:4008:8"]]
- 008cbc9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008cbc9c bytes 292000a9
- 008cbca0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008cbca0 ["RETURN", null, ["register:0:8"]]
- 008cbca0 bytes c0035fd6
+ 008ccc48 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 008ccc48 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 008ccc48 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 008ccc48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008ccc48 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c281c71cdccd7692816ba457ac958d48"></a>

### [`008cbf88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbf88.md) → [`008ccf34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cc/008ccf34.md) FUN_008ccf34

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbfac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbfac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008ccf58"
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
      "unmatched:008cbfac",
      "DATA",
      [
        "storage",
        "00c83f38",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008cbfb0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008cbfb4",
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
      "008ccf58",
      "DATA",
      [
        "storage",
        "00c84f08",
        null,
        "undefined *"
      ]
    ],
    [
      "008ccf5c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008ccf60",
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

- 旧版 [`008cbfac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbf88.md#insn-008cbfac) · [`008cbfb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbf88.md#insn-008cbfb8)
- 新版 [`008ccf58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cc/008ccf34.md#insn-008ccf58)

~~~diff
- 008cbfac ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008cbfac ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008cbfac ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008cbfac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008cbfac bytes 082400a9
- 008cbfb8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008cbfb8 ["RETURN", null, ["register:0:8"]]
- 008cbfb8 bytes c0035fd6
+ 008ccf58 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008ccf58 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 008ccf58 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 008ccf58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008ccf58 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6506152bb43fadd9795a2f6c8fec2a99"></a>

### [`008cbfbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbfbc.md) → [`008ccf68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cc/008ccf68.md) FUN_008ccf68

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbfc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbfc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008ccf74"
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
      "unmatched:008cbfc8",
      "DATA",
      [
        "storage",
        "00c83f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ccf74",
      "DATA",
      [
        "storage",
        "00c84f08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cbfc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbfbc.md#insn-008cbfc8) · [`008cbfcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbfbc.md#insn-008cbfcc)
- 新版 [`008ccf74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cc/008ccf68.md#insn-008ccf74)

~~~diff
- 008cbfc8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008cbfc8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 008cbfc8 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 008cbfc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008cbfc8 bytes 292000a9
- 008cbfcc ["COPY", "register:0:8", ["register:40f0:8"]]
- 008cbfcc ["RETURN", null, ["register:0:8"]]
- 008cbfcc bytes c0035fd6
+ 008ccf74 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 008ccf74 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 008ccf74 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 008ccf74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008ccf74 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d19ad2dcb182decf05801148c2ecb667"></a>

### [`008cc400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc400.md) → [`008cd3ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cd/008cd3ac.md) FUN_008cd3ac

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc400"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc400"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc404"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008cc400",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008cc404",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008cc424",
      "DATA",
      [
        "storage",
        "00c83fb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cd3ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008cd3b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008cd3d0",
      "DATA",
      [
        "storage",
        "00c84f88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cc400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc400.md#insn-008cc400) · [`008cc404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc400.md#insn-008cc404) · [`008cc424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc400.md#insn-008cc424)

~~~diff
- 008cc400 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008cc400 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008cc400 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008cc400 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008cc400 bytes fd7bbea9
- 008cc404 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008cc404 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008cc404 bytes f30b00f9
- 008cc424 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008cc424 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008cc424 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008cc424 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008cc424 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edacc5030cb0e7c318d0465b94204255"></a>

### [`008cc434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc434.md) → [`008cd3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cd/008cd3e0.md) FUN_008cd3e0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc440"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc440"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008cd3ec"
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
      "unmatched:008cc440",
      "DATA",
      [
        "storage",
        "00c83fb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cd3ec",
      "DATA",
      [
        "storage",
        "00c84f88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cc440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc434.md#insn-008cc440) · [`008cc444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc434.md#insn-008cc444)
- 新版 [`008cd3ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cd/008cd3e0.md#insn-008cd3ec)

~~~diff
- 008cc440 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008cc440 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 008cc440 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 008cc440 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008cc440 bytes 292000a9
- 008cc444 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008cc444 ["RETURN", null, ["register:0:8"]]
- 008cc444 bytes c0035fd6
+ 008cd3ec ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 008cd3ec ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 008cd3ec ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 008cd3ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008cd3ec bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6aab70d38d534ae7ab04e93e81338a57"></a>

### [`008cc4dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc4dc.md) → [`008cd488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cd/008cd488.md) FUN_008cd488

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 41.67% / 新版 41.67%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc4dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc4dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc4e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008cc4dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008cc4e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008cc4f4",
      "DATA",
      [
        "storage",
        "00c84038",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008cd488",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008cd48c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008cd4a0",
      "DATA",
      [
        "storage",
        "00c85008",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cc4dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc4dc.md#insn-008cc4dc) · [`008cc4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc4dc.md#insn-008cc4e0) · [`008cc4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc4dc.md#insn-008cc4f4)

~~~diff
- 008cc4dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008cc4dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008cc4dc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008cc4dc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008cc4dc bytes fd7bbea9
- 008cc4e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008cc4e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008cc4e0 bytes f30b00f9
- 008cc4f4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008cc4f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008cc4f4 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fabae1866efefdad2da674797b634d6f"></a>

### [`008cce18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cce18.md) → [`008cddc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cd/008cddc4.md) FUN_008cddc4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 82.86% / 新版 82.86%

CFGの説明率　旧版 31.25% / 新版 35.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008cce3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008cce5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008cdde8"
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
      "unmatched:008cce3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cde40"
      ]
    ],
    [
      "unmatched:008cce5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cde40"
      ]
    ]
  ],
  "added": [
    [
      "008cdde8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cde40"
      ]
    ],
    [
      "008cde08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cde40"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cce3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cce18.md#insn-008cce3c) · [`008cce5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cce18.md#insn-008cce5c)
- 新版 [`008cdde8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cd/008cddc4.md#insn-008cdde8)

~~~diff
- 008cce3c ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 008cce3c ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 008cce3c bytes c90200b4
- 008cce5c ["CBRANCH", null, ["local:b10:8", "register:102:1"]]
- 008cce5c bytes c2010054
+ 008cdde8 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 008cdde8 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 008cdde8 bytes c90200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8260cb9d580505fe87cb8280307fa8e"></a>

### [`008ccea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008ccea4.md) → [`008cde50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cd/008cde50.md) FUN_008cde50

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008cc668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc668.md) [`008ccea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008ccea4.md) · 呼出先 3件 [`008ccea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008ccea4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 2件 [`008cd614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cd/008cd614.md) [`008cde50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cd/008cde50.md) · 呼出先 3件 [`008cde50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cd/008cde50.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 97.35% / 新版 97.35%

CFGの説明率　旧版 80.42% / 新版 79.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008cd46c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008cd498"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008ce418"
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
      "unmatched:008cd46c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ce464"
      ]
    ],
    [
      "unmatched:008cd498",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ce408"
      ]
    ],
    [
      "unmatched:008cd4a8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "008ce418",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ce464"
      ]
    ],
    [
      "008ce444",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ce408"
      ]
    ],
    [
      "008ce454",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cd46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008ccea4.md#insn-008cd46c) · [`008cd498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008ccea4.md#insn-008cd498) · [`008cd4a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008ccea4.md#insn-008cd4a8)

~~~diff
- 008cd46c ["CBRANCH", null, ["local:b83:8", "register:101:1"]]
- 008cd46c bytes 60020054
- 008cd498 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008cd498 ["CBRANCH", null, ["local:b77:8", "tmp:0:1"]]
- 008cd498 bytes 20feffb5
- 008cd4a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008cd4a8 ["INT_ADD", "register:40f0:8", ["const:8cd4a8:8", "const:4:8"]]
- 008cd4a8 ["CALLIND", null, ["register:0:8"]]
- 008cd4a8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e099b91872279d53def1a75aa7f102c2"></a>

### [`008cedc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008cedc8.md) → [`008cfd74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cf/008cfd74.md) FUN_008cfd74

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008ce618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008ce618.md) [`008cedc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008cedc8.md) · 呼出先 3件 [`008cedc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008cedc8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 2件 [`008cf5c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cf/008cf5c4.md) [`008cfd74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cf/008cfd74.md) · 呼出先 3件 [`008cfd74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cf/008cfd74.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.12% / 新版 90.12%

CFGの説明率　旧版 77.85% / 新版 77.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 10件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ceed4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ceedc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ceee0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008cee9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cfe24"
      ]
    ],
    [
      "unmatched:008ceee4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cfecc"
      ]
    ],
    [
      "unmatched:008cef70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cfee0"
      ]
    ]
  ],
  "added": [
    [
      "008cfe48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cfe24"
      ]
    ],
    [
      "008cfe90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cfecc"
      ]
    ],
    [
      "008cff1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cfee0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cee94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008cedc8.md#insn-008cee94) · [`008cee98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008cedc8.md#insn-008cee98) · [`008cee9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008cedc8.md#insn-008cee9c)

~~~diff
- 008cee94 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008cee94 ["COPY", "tmp:1:8", ["register:4068:8"]]
- 008cee94 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 008cee94 ["COPY", "tmp:1:8", ["register:4060:8"]]
- 008cee94 bytes acb18c9a
- 008cee98 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008cee98 ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 008cee98 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 008cee98 ["COPY", "tmp:1:8", ["register:4070:8"]]
- 008cee98 bytes d6b28e9a
- 008cee9c ["INT_NOTEQUAL", "tmp:0:1", ["register:4060:8", "const:0:8"]]
- 008cee9c ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 008cee9c bytes ecfeffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1245d30ccd435bb458cf652fb03fef4"></a>

### [`008d060c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d060c.md) → [`008d15b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d1/008d15b8.md) FUN_008d15b8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d0624"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008d15d0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008d062c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d0624",
      "DATA",
      [
        "storage",
        "00c84508",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008d0628",
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
      "008d15d0",
      "DATA",
      [
        "storage",
        "00c854d8",
        null,
        "undefined *"
      ]
    ],
    [
      "008d15d4",
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

- 旧版 [`008d0624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d060c.md#insn-008d0624) · [`008d062c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d060c.md#insn-008d062c)
- 新版 [`008d15d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d1/008d15b8.md#insn-008d15d0)

~~~diff
- 008d0624 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008d0624 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008d0624 bytes 080000f9
- 008d062c ["COPY", "register:0:8", ["register:40f0:8"]]
- 008d062c ["RETURN", null, ["register:0:8"]]
- 008d062c bytes c0035fd6
+ 008d15d0 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008d15d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008d15d0 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdeeb7b236fa463f5ee17251061b67ae"></a>

### [`008d0648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0648.md) → [`008d15f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d1/008d15f4.md) FUN_008d15f4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 1件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 84.44% / 新版 84.44%

CFGの説明率　旧版 33.33% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d0670"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008d161c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008d0674"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d0670",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d1688"
      ]
    ],
    [
      "unmatched:008d0674",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ]
  ],
  "added": [
    [
      "008d161c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d1688"
      ]
    ],
    [
      "008d1620",
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

- 旧版 [`008d0670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0648.md#insn-008d0670) · [`008d0674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0648.md#insn-008d0674)
- 新版 [`008d161c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d1/008d15f4.md#insn-008d161c)

~~~diff
- 008d0670 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 008d0670 bytes 60030054
- 008d0674 ["INT_ADD", "register:40f0:8", ["const:8d0674:8", "const:4:8"]]
- 008d0674 ["CALL", null, ["callee:008524fc:8"]]
- 008d0674 bytes b703fe97
+ 008d161c ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 008d161c bytes 60030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b74518e79642523a6c7ff78cdb360df"></a>

### [`008d0878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0878.md) → [`008d1824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d1/008d1824.md) FUN_008d1824

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d0878"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d0878"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d0890"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d0878",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d0884",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58f30"
      ]
    ],
    [
      "unmatched:008d0890",
      "DATA",
      [
        "storage",
        "00c845f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d1824",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008d1830",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58f30"
      ]
    ],
    [
      "008d183c",
      "DATA",
      [
        "storage",
        "00c855c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d0878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0878.md#insn-008d0878) · [`008d0884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0878.md#insn-008d0884) · [`008d0890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0878.md#insn-008d0890)

~~~diff
- 008d0878 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d0878 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d0878 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 008d0878 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008d0878 bytes fd7bbfa9
- 008d0884 ["INT_ADD", "register:40f0:8", ["const:8d0884:8", "const:4:8"]]
- 008d0884 ["CALL", null, ["callee:00c58f30:8"]]
- 008d0884 bytes b71d0e94
- 008d0890 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008d0890 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008d0890 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8228d42f95c2ce76dfedd441de9128e"></a>

### [`008d089c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d089c.md) → [`008d1848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d1/008d1848.md) FUN_008d1848

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d08a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008d1850"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008d08a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d08a4",
      "DATA",
      [
        "storage",
        "00c845f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d1850",
      "DATA",
      [
        "storage",
        "00c855c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d08a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d089c.md#insn-008d08a4) · [`008d08a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d089c.md#insn-008d08a8)
- 新版 [`008d1850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d1/008d1848.md#insn-008d1850)

~~~diff
- 008d08a4 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008d08a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008d08a4 bytes 280000f9
- 008d08a8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008d08a8 ["RETURN", null, ["register:0:8"]]
- 008d08a8 bytes c0035fd6
+ 008d1850 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 008d1850 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008d1850 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad150386cb3eeffead2f3f86551a2fe2"></a>

### [`008d5ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d5ad0.md) → [`008d6a7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d6/008d6a7c.md) FUN_008d6a7c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 3件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00865b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865b4c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0084f5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084f/0084f5a0.md) · 呼出先 3件 [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`00866af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/00866af8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.43% / 新版 80.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5ad4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5ad4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5ad8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d5ad4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d5ad8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d5adc",
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
      "008d6a80",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "008d6a84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008d6a88",
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

- 旧版 [`008d5ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d5ad0.md#insn-008d5ad4) · [`008d5ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d5ad0.md#insn-008d5ad8) · [`008d5adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d5ad0.md#insn-008d5adc)

~~~diff
- 008d5ad4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d5ad4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d5ad4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 008d5ad4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d5ad4 bytes fd7b01a9
- 008d5ad8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 008d5ad8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 008d5ad8 bytes f51300f9
- 008d5adc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008d5adc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008d5adc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 008d5adc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d5adc bytes f44f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa33d43fda3a11906329929e46eebbee"></a>

### [`008d6c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6c68.md) → [`008d7c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d7/008d7c14.md) FUN_008d7c14

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00476708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476708.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00476a28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00476/00476a28.md) · 呼出先 0件 

命令の説明率　旧版 58.06% / 新版 58.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-f482ef8de17e1f47c70b56845da70ee3"></a>

### [`008d6ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6ce4.md) → [`008d7c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d7/008d7c90.md) FUN_008d7c90

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 28.57% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d6cf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008d7ca0"
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
      "unmatched:008d6cf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d7cb4"
      ]
    ]
  ],
  "added": [
    [
      "008d7ca0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d7cb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d6cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6ce4.md#insn-008d6cf4) · [`008d6d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6ce4.md#insn-008d6d00)
- 新版 [`008d7ca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d7/008d7c90.md#insn-008d7ca0) · [`008d7cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d7/008d7c90.md#insn-008d7cac)

~~~diff
- 008d6cf4 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 008d6cf4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 008d6cf4 bytes b30000b4
+ 008d7ca0 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 008d7ca0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 008d7ca0 bytes b30000b4
- 008d6d00 ["INT_ADD", "register:40f0:8", ["const:8d6d00:8", "const:4:8"]]
- 008d6d00 ["CALL", null, ["callee:00c54d90:8"]]
+ 008d7cac ["INT_ADD", "register:40f0:8", ["const:8d7cac:8", "const:4:8"]]
+ 008d7cac ["CALL", null, ["callee:00c54d90:8"]]
- 008d6d00 bytes 28f40d94
+ 008d7cac bytes 39f40d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb4881b1f477071f77cd5a7becbb8cff"></a>

### [`008d8c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8c34.md) → [`008d9be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d9/008d9be0.md) FUN_008d9be0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8c34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8c34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8c38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d8c34",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d8c38",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d8c58",
      "DATA",
      [
        "storage",
        "00c849f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d9be0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008d9be4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008d9c04",
      "DATA",
      [
        "storage",
        "00c859c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8c34.md#insn-008d8c34) · [`008d8c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8c34.md#insn-008d8c38) · [`008d8c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8c34.md#insn-008d8c58)

~~~diff
- 008d8c34 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d8c34 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d8c34 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008d8c34 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008d8c34 bytes fd7bbea9
- 008d8c38 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008d8c38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008d8c38 bytes f30b00f9
- 008d8c58 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d8c58 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008d8c58 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008d8c58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d8c58 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4584bdae46b823939980bb90ef588032"></a>

### [`008d8e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8e58.md) → [`008d9e04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008d9/008d9e04.md) FUN_008d9e04

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8e80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8e84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8e88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d8e80",
      "DATA",
      [
        "storage",
        "00c84a68",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008d8e8c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d8e90",
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
      "008d9e2c",
      "DATA",
      [
        "storage",
        "00c85a38",
        null,
        "undefined *"
      ]
    ],
    [
      "008d9e38",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008d9e3c",
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

- 旧版 [`008d8e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8e58.md#insn-008d8e80) · [`008d8e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8e58.md#insn-008d8e84) · [`008d8e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8e58.md#insn-008d8e88)

~~~diff
- 008d8e80 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008d8e80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008d8e80 bytes 080000f9
- 008d8e84 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 008d8e84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008d8e84 bytes 0080803c
- 008d8e88 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:18:8"]]
- 008d8e88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008d8e88 bytes 090c00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b3b126f03e22b365bc688d0ee42ad70"></a>

### [`008d9460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9460.md) → [`008da40c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008da40c.md) FUN_008da40c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9484"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9488"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008da430"
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
      "unmatched:008d9484",
      "DATA",
      [
        "storage",
        "00c84ad8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008d948c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d9490",
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
      "008da430",
      "DATA",
      [
        "storage",
        "00c85aa8",
        null,
        "undefined *"
      ]
    ],
    [
      "008da438",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008da43c",
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

- 旧版 [`008d9484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9460.md#insn-008d9484) · [`008d9488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9460.md#insn-008d9488) · [`008d9494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9460.md#insn-008d9494)

~~~diff
- 008d9484 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008d9484 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008d9484 bytes 080000f9
- 008d9488 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 008d9488 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008d9488 bytes 0080803c
- 008d9494 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008d9494 ["RETURN", null, ["register:0:8"]]
- 008d9494 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76bbb62a7e9055817d07b3794daadd9f"></a>

### [`008d9498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9498.md) → [`008da444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008da444.md) FUN_008da444

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d94a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d94a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008da44c"
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
      "unmatched:008d94a0",
      "DATA",
      [
        "storage",
        "00c84ad8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008da44c",
      "DATA",
      [
        "storage",
        "00c85aa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d94a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9498.md#insn-008d94a0) · [`008d94a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9498.md#insn-008d94a8) · [`008d94ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9498.md#insn-008d94ac)

~~~diff
- 008d94a0 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008d94a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008d94a0 bytes 280000f9
- 008d94a8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 008d94a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008d94a8 bytes 2080803c
- 008d94ac ["COPY", "register:0:8", ["register:40f0:8"]]
- 008d94ac ["RETURN", null, ["register:0:8"]]
- 008d94ac bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a52470391cef19934663b4907960e860"></a>

### [`008d94b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d94b8.md) → [`008da464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008da464.md) FUN_008da464

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0058fbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058fbc0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058fee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058fee0.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d94e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008da494"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008d94e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d94b8.md#insn-008d94e8) · [`008d94dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d94b8.md#insn-008d94dc)
- 新版 [`008da494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008da464.md#insn-008da494) · [`008da488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008da464.md#insn-008da488)

~~~diff
- 008d94e8 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 008d94e8 ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 008d94e8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 008d94e8 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 008d94e8 bytes 686a3438
+ 008da494 ["COPY", "tmp:0:4", ["register:4040:4"]]
+ 008da494 ["COPY", "tmp:1:8", ["register:40a0:8"]]
+ 008da494 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 008da494 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 008da494 bytes 686a3438
- 008d94dc ["INT_ADD", "register:40f0:8", ["const:8d94dc:8", "const:4:8"]]
- 008d94dc ["CALL", null, ["callee:0058fee0:8"]]
+ 008da488 ["INT_ADD", "register:40f0:8", ["const:8da488:8", "const:4:8"]]
+ 008da488 ["CALL", null, ["callee:0058fee0:8"]]
- 008d94dc bytes b9d9f297
+ 008da488 bytes 96d6f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9aaf2fafefab6b09e9cbb9e5c5ad380c"></a>

### [`008d9538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9538.md) → [`008da4e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008da4e4.md) FUN_008da4e4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d955c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d955c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008da508"
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
      "unmatched:008d955c",
      "DATA",
      [
        "storage",
        "00c84b78",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008d9560",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d9564",
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
      "008da508",
      "DATA",
      [
        "storage",
        "00c85b48",
        null,
        "undefined *"
      ]
    ],
    [
      "008da50c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008da510",
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

- 旧版 [`008d955c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9538.md#insn-008d955c) · [`008d9568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9538.md#insn-008d9568)
- 新版 [`008da508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008da4e4.md#insn-008da508)

~~~diff
- 008d955c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d955c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008d955c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008d955c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d955c bytes 082400a9
- 008d9568 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008d9568 ["RETURN", null, ["register:0:8"]]
- 008d9568 bytes c0035fd6
+ 008da508 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008da508 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 008da508 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 008da508 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008da508 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd93ff666c0fddf44ba5ee92b3042647"></a>

### [`008d9710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9710.md) → [`008da6bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008da6bc.md) FUN_008da6bc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9734"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9734"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008da6e0"
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
      "unmatched:008d9734",
      "DATA",
      [
        "storage",
        "00c84be8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008d9738",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d973c",
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
      "008da6e0",
      "DATA",
      [
        "storage",
        "00c85bb8",
        null,
        "undefined *"
      ]
    ],
    [
      "008da6e4",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008da6e8",
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

- 旧版 [`008d9734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9710.md#insn-008d9734) · [`008d9740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9710.md#insn-008d9740)
- 新版 [`008da6e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008da6bc.md#insn-008da6e0)

~~~diff
- 008d9734 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d9734 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008d9734 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008d9734 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d9734 bytes 082400a9
- 008d9740 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008d9740 ["RETURN", null, ["register:0:8"]]
- 008d9740 bytes c0035fd6
+ 008da6e0 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008da6e0 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 008da6e0 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 008da6e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008da6e0 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2ace74f4301a345079d6ae8fa890eb5"></a>

### [`008d9804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9804.md) → [`008da7b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008da/008da7b0.md) FUN_008da7b0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 11.11% / 新版 11.11%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9814"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d981c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008da7c0"
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
      "unmatched:008d9814",
      "DATA",
      [
        "storage",
        "00c84c78",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008d9818",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008da7d0"
      ]
    ],
    [
      "unmatched:008d9820",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58f50"
      ]
    ]
  ],
  "added": [
    [
      "008da7c0",
      "DATA",
      [
        "storage",
        "00c85c48",
        null,
        "undefined *"
      ]
    ],
    [
      "008da7c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008da7d0"
      ]
    ],
    [
      "008da7cc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58f50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d9814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9804.md#insn-008d9814) · [`008d9818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9804.md#insn-008d9818) · [`008d981c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9804.md#insn-008d981c)

~~~diff
- 008d9814 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d9814 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008d9814 bytes 090100f9
- 008d9818 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008d9818 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 008d9818 bytes 600000b4
- 008d981c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:28:8"]]
- 008d981c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 008d981c bytes 001500f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e24176be1d7b9e5c87ed51a55509054a"></a>

### [`008e9124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9124.md) → [`008ea0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea0d0.md) FUN_008ea0d0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 50.00% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e9164"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008ea110"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008e9164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9124.md#insn-008e9164) · [`008e9144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9124.md#insn-008e9144)
- 新版 [`008ea110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea0d0.md#insn-008ea110) · [`008ea0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea0d0.md#insn-008ea0f0)

~~~diff
- 008e9164 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 008e9164 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008e9164 bytes 690a00f9
+ 008ea110 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
+ 008ea110 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008ea110 bytes 690a00f9
- 008e9144 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008e9144 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 008ea0f0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 008ea0f0 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 008e9144 bytes e00100b4
+ 008ea0f0 bytes e00100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f36b5e597e326e60546425cb0f66a1e5"></a>

### [`008e92d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e92d4.md) → [`008ea280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea280.md) FUN_008ea280

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 55.56% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008e930c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008ea2b8"
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
      "unmatched:008e930c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ea29c"
      ]
    ]
  ],
  "added": [
    [
      "008ea2b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ea29c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e930c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e92d4.md#insn-008e930c) · [`008e92ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e92d4.md#insn-008e92ec)
- 新版 [`008ea2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea280.md#insn-008ea2b8) · [`008ea298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea280.md#insn-008ea298)

~~~diff
- 008e930c ["CBRANCH", null, ["local:b1:8", "register:101:1"]]
- 008e930c bytes 20ffff54
+ 008ea2b8 ["CBRANCH", null, ["local:b1:8", "register:101:1"]]
+ 008ea2b8 bytes 20ffff54
- 008e92ec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008e92ec ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 008ea298 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008ea298 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 008e92ec bytes 21010054
+ 008ea298 bytes 21010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2bbb252faa4c89703604aa00deee1e7"></a>

### [`008f2338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f2/008f2338.md) → [`008f32e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f3/008f32e4.md) FUN_008f32e4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f3098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f3/008f3098.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`008f4044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f4/008f4044.md) · 呼出先 1件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 83.78% / 新版 83.78%

CFGの説明率　旧版 50.00% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008f234c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f2/008f2338.md#insn-008f234c) · [`008f2354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f2/008f2338.md#insn-008f2354) · [`008f2358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f2/008f2338.md#insn-008f2358)
- 新版 [`008f32f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f3/008f32e4.md#insn-008f32f8) · [`008f3300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f3/008f32e4.md#insn-008f3300) · [`008f3304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f3/008f32e4.md#insn-008f3304)

~~~diff
- 008f234c ["INT_ADD", "register:40f0:8", ["const:8f234c:8", "const:4:8"]]
- 008f234c ["CALL", null, ["callee:008524fc:8"]]
+ 008f32f8 ["INT_ADD", "register:40f0:8", ["const:8f32f8:8", "const:4:8"]]
+ 008f32f8 ["CALL", null, ["callee:008524fc:8"]]
- 008f234c bytes 817cfd97
+ 008f32f8 bytes 817cfd97
- 008f2354 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008f2354 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 008f2354 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 008f2354 ["CBRANCH", null, ["local:b3:8", "tmp:2:1"]]
+ 008f3300 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008f3300 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 008f3300 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 008f3300 ["CBRANCH", null, ["local:b4:8", "tmp:2:1"]]
- 008f2354 bytes 4c030054
+ 008f3300 bytes 4c030054
- 008f2358 ["INT_ADD", "register:40f0:8", ["const:8f2358:8", "const:4:8"]]
- 008f2358 ["CALL", null, ["callee:008524fc:8"]]
+ 008f3304 ["INT_ADD", "register:40f0:8", ["const:8f3304:8", "const:4:8"]]
+ 008f3304 ["CALL", null, ["callee:008524fc:8"]]
- 008f2358 bytes 7e7cfd97
+ 008f3304 bytes 7e7cfd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86080c3be6cf221b360364b73afc9761"></a>

### [`008f8a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8a58.md) → [`008f9a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f9/008f9a04.md) FUN_008f9a04

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f8a58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f8a58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f8a5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008f8a58",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008f8a5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008f8a7c",
      "DATA",
      [
        "storage",
        "00c859c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f9a04",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008f9a08",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008f9a28",
      "DATA",
      [
        "storage",
        "00c86998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f8a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8a58.md#insn-008f8a58) · [`008f8a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8a58.md#insn-008f8a5c) · [`008f8a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8a58.md#insn-008f8a7c)

~~~diff
- 008f8a58 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008f8a58 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008f8a58 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008f8a58 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008f8a58 bytes fd7bbea9
- 008f8a5c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008f8a5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008f8a5c bytes f30b00f9
- 008f8a7c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008f8a7c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008f8a7c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008f8a7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008f8a7c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4cb9c20f087c9135e02a1d6280df843"></a>

### [`008f9c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9c68.md) → [`008fac14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fa/008fac14.md) FUN_008fac14

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 7件 [`008eb570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb570.md) [`008f39fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f3/008f39fc.md) [`008f5404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5404.md) [`008f5c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5c38.md) [`008f6338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f6338.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 7件 [`008ec51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ec51c.md) [`008f49a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f4/008f49a8.md) [`008f63b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f6/008f63b0.md) [`008f6be4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f6/008f6be4.md) [`008f72e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f7/008f72e4.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_store_alignment

命令の説明率　旧版 84.54% / 新版 84.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_destination` 3件, `store_value` 2件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f9d24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f9d2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f9d30"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008f9d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9c68.md#insn-008f9d24) · [`008f9d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9c68.md#insn-008f9d2c) · [`008f9d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9c68.md#insn-008f9d30)

~~~diff
- 008f9d24 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c8:8"]]
- 008f9d24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008f9d24 bytes 00808c3c
- 008f9d2c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:98:8"]]
- 008f9d2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008f9d2c bytes 0080893c
- 008f9d30 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008f9d30 ["COPY", "tmp:1:8", ["const:0:8"]]
- 008f9d30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 008f9d30 bytes 3f0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12dadee437afdf4adda4c1d197390fc8"></a>

### [`008f9e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9e5c.md) → [`008fae08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fa/008fae08.md) FUN_008fae08

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`008f5340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5340.md) [`008f9e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9e5c.md) [`008fa2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa2d0.md) · 呼出先 4件 [`008f9e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9e5c.md) [`008fa160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa160.md) [`008fa2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa2d0.md) [`008fa598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa598.md)
- 新版 呼出元 3件 [`008f62ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f6/008f62ec.md) [`008fae08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fa/008fae08.md) [`008fb27c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fb/008fb27c.md) · 呼出先 4件 [`008fae08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fa/008fae08.md) [`008fb10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fb/008fb10c.md) [`008fb27c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fb/008fb27c.md) [`008fb544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fb/008fb544.md)

変更の種類 branch_condition_or_target, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 97.93% / 新版 97.93%

CFGの説明率　旧版 89.06% / 新版 89.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f9e6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f9e6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008fae18"
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
      "unmatched:008f9e6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008fa158",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008fb0b0"
      ]
    ],
    [
      "unmatched:008fa15c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "008fae28"
      ]
    ]
  ],
  "added": [
    [
      "008fae18",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008fb104",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008fb0b0"
      ]
    ],
    [
      "008fb108",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "008fae28"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f9e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9e5c.md#insn-008f9e6c) · [`008fa158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9e5c.md#insn-008fa158)
- 新版 [`008fae18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fa/008fae08.md#insn-008fae18)

~~~diff
- 008f9e6c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008f9e6c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008f9e6c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 008f9e6c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008f9e6c bytes f44f04a9
- 008fa158 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008fa158 ["CBRANCH", null, ["local:b35:8", "tmp:0:1"]]
- 008fa158 bytes 61fdff54
+ 008fae18 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 008fae18 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 008fae18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
+ 008fae18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008fae18 bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2f3b289d31dc145b8a00a6275a583ee"></a>

### [`008fd234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fd/008fd234.md) → [`008fe1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fe/008fe1e0.md) FUN_008fe1e0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008fc644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fc/008fc644.md) [`008fd554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fd/008fd554.md) · 呼出先 9件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`005da5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005da/005da5c4.md) [`00691858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691858.md) [`0071ed58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071ed58.md)
- 新版 呼出元 2件 [`008fd5f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fd/008fd5f0.md) [`008fe500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fe/008fe500.md) · 呼出先 9件 [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`005da974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005da/005da974.md) [`00691c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00691/00691c08.md) [`0071f108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071f/0071f108.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 82.86% / 新版 82.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008fd3d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008fe380"
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
      "008fe288",
      "READ",
      [
        "storage",
        "0029f5e8",
        null,
        "string"
      ]
    ],
    [
      "008fe28c",
      "READ",
      [
        "storage",
        "0029f5ef",
        null,
        "string"
      ]
    ],
    [
      "unmatched:008fd3d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008fe378"
      ]
    ]
  ],
  "added": [
    [
      "008fe288",
      "READ",
      [
        "storage",
        "0029f628",
        null,
        "string"
      ]
    ],
    [
      "008fe28c",
      "READ",
      [
        "storage",
        "0029f62f",
        null,
        "string"
      ]
    ],
    [
      "008fe380",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008fe378"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fd3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fd/008fd234.md#insn-008fd3d4) · [`008fd26c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fd/008fd234.md#insn-008fd26c)
- 新版 [`008fe380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fe/008fe1e0.md#insn-008fe380) · [`008fe218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fe/008fe1e0.md#insn-008fe218)

~~~diff
- 008fd3d4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 008fd3d4 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 008fd3d4 bytes c9ffffb5
+ 008fe380 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 008fe380 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 008fe380 bytes c9ffffb5
- 008fd26c ["INT_ADD", "register:40f0:8", ["const:8fd26c:8", "const:4:8"]]
- 008fd26c ["CALL", null, ["callee:008ad384:8"]]
+ 008fe218 ["INT_ADD", "register:40f0:8", ["const:8fe218:8", "const:4:8"]]
+ 008fe218 ["CALL", null, ["callee:008ad384:8"]]
- 008fd26c bytes 5bbcfe97
+ 008fe218 bytes 5bbcfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c270bc0923a9860fb5af59c5d5766941"></a>

### [`008fe5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fe/008fe5d8.md) → [`008ff584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ff/008ff584.md) FUN_008ff584

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008fd554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fd/008fd554.md) · 呼出先 2件 [`008aca34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ac/008aca34.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`008fe500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fe/008fe500.md) · 呼出先 2件 [`008ad9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ad/008ad9e0.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008fe630"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "008ff5dc"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008fe630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fe/008fe5d8.md#insn-008fe630) · [`008fe5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fe/008fe5d8.md#insn-008fe5fc)
- 新版 [`008ff5dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ff/008ff584.md#insn-008ff5dc) · [`008ff5a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ff/008ff584.md#insn-008ff5a8)

~~~diff
- 008fe630 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008fe630 ["RETURN", null, ["register:0:8"]]
- 008fe630 bytes c0035fd6
+ 008ff5dc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 008ff5dc ["RETURN", null, ["register:0:8"]]
+ 008ff5dc bytes c0035fd6
- 008fe5fc ["INT_ADD", "register:40f0:8", ["const:8fe5fc:8", "const:4:8"]]
- 008fe5fc ["CALL", null, ["callee:008ad9e0:8"]]
+ 008ff5a8 ["INT_ADD", "register:40f0:8", ["const:8ff5a8:8", "const:4:8"]]
+ 008ff5a8 ["CALL", null, ["callee:008ad9e0:8"]]
- 008fe5fc bytes 0eb9fe97
+ 008ff5a8 bytes 0eb9fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1eb20d6a0c5647cc97af1f48f5f0adc4"></a>

### [`008ff318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff318.md) → [`009002c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00900/009002c4.md) FUN_009002c4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ff334"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009002e0"
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
      "unmatched:008ff334",
      "DATA",
      [
        "storage",
        "00c85c80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009002e0",
      "DATA",
      [
        "storage",
        "00c86c50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ff334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff318.md#insn-008ff334) · [`008ff328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff318.md#insn-008ff328)
- 新版 [`009002e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00900/009002c4.md#insn-009002e0) · [`009002d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00900/009002c4.md#insn-009002d4)

~~~diff
- 008ff334 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008ff334 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 008ff334 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:40:8"]]
- 008ff334 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008ff334 bytes 080404f8
+ 009002e0 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 009002e0 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 009002e0 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:40:8"]]
+ 009002e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 009002e0 bytes 080404f8
- 008ff328 ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 009002d4 ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008ff328 bytes 281c00d0
+ 009002d4 bytes 281c00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d0ff180f8b3aae9a7fb06dff697b17a"></a>

### [`008ff4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff4c0.md) → [`0090046c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00900/0090046c.md) FUN_0090046c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0071c4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c4b8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0071c868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c868.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 97.54% / 新版 97.54%

CFGの説明率　旧版 78.38% / 新版 78.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ff538"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009004e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008ff53c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ff4ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "unmatched:008ff538",
      "DATA",
      [
        "storage",
        "0039b1b8",
        null,
        "dword"
      ]
    ],
    [
      "unmatched:008ff53c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0090051c"
      ]
    ]
  ],
  "added": [
    [
      "00900498",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "009004e4",
      "DATA",
      [
        "storage",
        "0039b1b8",
        "fde_0039b1b8",
        "dword"
      ]
    ],
    [
      "009004e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0090051c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ff4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff4c0.md#insn-008ff4ec) · [`008ff538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff4c0.md#insn-008ff538) · [`008ff53c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff4c0.md#insn-008ff53c)

~~~diff
- 008ff4ec ["INT_ADD", "register:40f0:8", ["const:8ff4ec:8", "const:4:8"]]
- 008ff4ec ["CALL", null, ["ram:47ad34:8"]]
- 008ff4ec bytes 12eeed97
- 008ff538 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 008ff538 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 008ff538 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 008ff538 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 008ff538 bytes 096828b8
- 008ff53c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008ff53c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 008ff53c bytes a1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7296737bf36ab9ca57e0f749a67706e7"></a>

### [`008ff7c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff7c8.md) → [`00900774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00900/00900774.md) FUN_00900774

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ff7ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ff7ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00900798"
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
      "unmatched:008ff7ec",
      "DATA",
      [
        "storage",
        "00c85d00",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008ff7f0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ff7f4",
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
      "00900798",
      "DATA",
      [
        "storage",
        "00c86cd0",
        null,
        "undefined *"
      ]
    ],
    [
      "0090079c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009007a0",
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

- 旧版 [`008ff7ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff7c8.md#insn-008ff7ec) · [`008ff7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff7c8.md#insn-008ff7f8)
- 新版 [`00900798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00900/00900774.md#insn-00900798)

~~~diff
- 008ff7ec ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008ff7ec ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008ff7ec ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008ff7ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ff7ec bytes 082400a9
- 008ff7f8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008ff7f8 ["RETURN", null, ["register:0:8"]]
- 008ff7f8 bytes c0035fd6
+ 00900798 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00900798 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00900798 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00900798 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00900798 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c458a537a9a04657fd6955dbf02449d"></a>

### [`0090132c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/0090132c.md) → [`009022d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00902/009022d8.md) FUN_009022d8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008ff920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff920.md) [`00a3f3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3f/00a3f3a0.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) [`007f1b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1b10.md) [`007f1ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1ee8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`009008cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00900/009008cc.md) [`00a40394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a40/00a40394.md) · 呼出先 7件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0046ec04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ec04.md) [`007f2a74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007f2/007f2a74.md) [`007f2e4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007f2/007f2e4c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.31% / 新版 98.31%

CFGの説明率　旧版 81.48% / 新版 78.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00901480"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0090242c"
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
      "unmatched:00901480",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0090241c"
      ]
    ]
  ],
  "added": [
    [
      "0090242c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0090241c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00901480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/0090132c.md#insn-00901480) · [`00901394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/0090132c.md#insn-00901394)
- 新版 [`0090242c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00902/009022d8.md#insn-0090242c) · [`00902340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00902/009022d8.md#insn-00902340)

~~~diff
- 00901480 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00901480 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00901480 bytes 81ffff54
+ 0090242c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0090242c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 0090242c bytes 81ffff54
- 00901394 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00901394 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00901394 ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
+ 00902340 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00902340 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00902340 ["CBRANCH", null, ["local:b16:8", "tmp:1:1"]]
- 00901394 bytes 080a0054
+ 00902340 bytes 080a0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1714807a5715d029bd6b491f2b9e7cbf"></a>

### [`00901554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/00901554.md) → [`00902500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00902/00902500.md) FUN_00902500

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0090156c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00902518"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00901574"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0090156c",
      "DATA",
      [
        "storage",
        "00c85da0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00901570",
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
      "00902518",
      "DATA",
      [
        "storage",
        "00c86d70",
        null,
        "undefined *"
      ]
    ],
    [
      "0090251c",
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

- 旧版 [`0090156c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/00901554.md#insn-0090156c) · [`00901574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/00901554.md#insn-00901574)
- 新版 [`00902518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00902/00902500.md#insn-00902518)

~~~diff
- 0090156c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0090156c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0090156c bytes 080000f9
- 00901574 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00901574 ["RETURN", null, ["register:0:8"]]
- 00901574 bytes c0035fd6
+ 00902518 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00902518 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00902518 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32e7e1dfafb7319180ac1671aee86012"></a>

### [`00901614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/00901614.md) → [`009025c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00902/009025c0.md) FUN_009025c0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00901620"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00901620"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009025cc"
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
      "unmatched:00901620",
      "DATA",
      [
        "storage",
        "00c85e20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009025cc",
      "DATA",
      [
        "storage",
        "00c86df0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00901620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/00901614.md#insn-00901620) · [`00901618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/00901614.md#insn-00901618)
- 新版 [`009025cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00902/009025c0.md#insn-009025cc) · [`009025c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00902/009025c0.md#insn-009025c4)

~~~diff
- 00901620 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00901620 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00901620 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00901620 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00901620 bytes 292000a9
+ 009025cc ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 009025cc ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 009025cc ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 009025cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 009025cc bytes 292000a9
- 00901618 ["COPY", "register:4048:8", ["const:c85000:8"]]
+ 009025c4 ["COPY", "register:4048:8", ["const:c86000:8"]]
- 00901618 bytes 291c0090
+ 009025c4 bytes 291c0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0334da7c3a514a3a60014edf26a6db5a"></a>

### [`00901630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/00901630.md) → [`009025dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00902/009025dc.md) FUN_009025dc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00901798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/00901798.md) [`0090179c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/0090179c.md) [`00ac9604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9604.md) [`00acac44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aca/00acac44.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00902744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00902/00902744.md) [`00902748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00902/00902748.md) [`00aca5f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00aca5f8.md) [`00acbc38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acb/00acbc38.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 60.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00901670"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00901670"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0090261c"
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
      "unmatched:00901670",
      "DATA",
      [
        "storage",
        "00c85e90",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00901670",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00902654",
      "READ",
      [
        "storage",
        "00c85eb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0090261c",
      "DATA",
      [
        "storage",
        "00c86e60",
        null,
        "undefined *"
      ]
    ],
    [
      "0090261c",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00902654",
      "READ",
      [
        "storage",
        "00c86e80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00901670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/00901630.md#insn-00901670) · [`009016d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/00901630.md#insn-009016d0)
- 新版 [`0090261c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00902/009025dc.md#insn-0090261c)

~~~diff
- 00901670 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00901670 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00901670 ["COPY", "tmp:2:8", ["register:8:8"]]
- 00901670 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00901670 bytes e85700a9
- 009016d0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 009016d0 ["RETURN", null, ["register:0:8"]]
- 009016d0 bytes c0035fd6
+ 0090261c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0090261c ["COPY", "tmp:1:8", ["register:40a8:8"]]
+ 0090261c ["COPY", "tmp:2:8", ["register:8:8"]]
+ 0090261c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0090261c bytes e85700a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75446d721346ec0e4a16391fc08eaaa2"></a>

### [`009ccb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009ccb84.md) → [`009cdb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cdb30.md) FUN_009cdb30

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0087f164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f164.md) [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) [`00880494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880494.md) [`008acdac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ac/008acdac.md) · 呼出先 6件 [`0076846c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/0076846c.md) [`00768a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768a80.md) [`00768ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768ebc.md) [`0076911c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/0076911c.md) [`007692a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/007692a8.md)
- 新版 呼出元 4件 [`00880110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/00880110.md) [`0088036c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/0088036c.md) [`00881440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/00881440.md) [`008add58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ad/008add58.md) · 呼出先 6件 [`00768848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/00768848.md) [`00768e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/00768e5c.md) [`00769298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769298.md) [`007694f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/007694f8.md) [`00769684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/00769684.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 47.37% / 新版 47.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009cdb40",
      "value": [
        "leaf",
        "ram:84f5a0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009ccb94",
      "value": [
        "leaf",
        "ram:84e5f4:8"
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
      "site": "009cdb4c",
      "value": [
        "leaf",
        "ram:768e5c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009ccba0",
      "value": [
        "leaf",
        "ram:768a80:8"
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
      "site": "009cdb54",
      "value": [
        "leaf",
        "ram:769298:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009ccba8",
      "value": [
        "leaf",
        "ram:768ebc:8"
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
      "009cdb40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0084e5f4"
      ]
    ],
    [
      "009cdb4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768a80"
      ]
    ],
    [
      "009cdb54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768ebc"
      ]
    ]
  ],
  "added": [
    [
      "009cdb40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0084f5a0"
      ]
    ],
    [
      "009cdb4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768e5c"
      ]
    ],
    [
      "009cdb54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00769298"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ccb94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009ccb84.md#insn-009ccb94) · [`009ccba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009ccb84.md#insn-009ccba0) · [`009ccba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009ccb84.md#insn-009ccba8)
- 新版 [`009cdb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cdb30.md#insn-009cdb40) · [`009cdb4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cdb30.md#insn-009cdb4c) · [`009cdb54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009cd/009cdb30.md#insn-009cdb54)

~~~diff
- 009ccb94 ["INT_ADD", "register:40f0:8", ["const:9ccb94:8", "const:4:8"]]
- 009ccb94 ["CALL", null, ["ram:84e5f4:8"]]
+ 009cdb40 ["INT_ADD", "register:40f0:8", ["const:9cdb40:8", "const:4:8"]]
+ 009cdb40 ["CALL", null, ["ram:84f5a0:8"]]
- 009ccb94 bytes 9806fa97
+ 009cdb40 bytes 9806fa97
- 009ccba0 ["INT_ADD", "register:40f0:8", ["const:9ccba0:8", "const:4:8"]]
- 009ccba0 ["CALL", null, ["ram:768a80:8"]]
+ 009cdb4c ["INT_ADD", "register:40f0:8", ["const:9cdb4c:8", "const:4:8"]]
+ 009cdb4c ["CALL", null, ["ram:768e5c:8"]]
- 009ccba0 bytes b86ff697
+ 009cdb4c bytes c46cf697
- 009ccba8 ["INT_ADD", "register:40f0:8", ["const:9ccba8:8", "const:4:8"]]
- 009ccba8 ["CALL", null, ["ram:768ebc:8"]]
+ 009cdb54 ["INT_ADD", "register:40f0:8", ["const:9cdb54:8", "const:4:8"]]
+ 009cdb54 ["CALL", null, ["ram:769298:8"]]
- 009ccba8 bytes c570f697
+ 009cdb54 bytes d16df697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6741d352f1449db401500a97a9119f7b"></a>

### [`009f8670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f8/009f8670.md) → [`009f961c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f9/009f961c.md) FUN_009f961c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a01544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a01544.md) · 呼出先 15件 [`0046cac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cac4.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`005c3ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3ebc.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`006c5350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c5/006c5350.md)
- 新版 呼出元 1件 [`00a024f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a02/00a024f0.md) · 呼出先 15件 [`0046cde4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cde4.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`005c426c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c426c.md) [`00676e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676e50.md) [`006c5700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c5/006c5700.md)

変更の種類 call, call_target, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 99.16% / 新版 99.16%

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
      "site": "009f9754",
      "value": [
        "leaf",
        "ram:6cbe7c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f87a8",
      "value": [
        "leaf",
        "ram:6cbacc:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f9760",
      "value": [
        "leaf",
        "ram:6ccf80:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f87b4",
      "value": [
        "leaf",
        "ram:6ccbd0:8"
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
      "009f9688",
      "DATA",
      [
        "storage",
        "00436ba0",
        "fde_00436ba0",
        "dword"
      ]
    ],
    [
      "009f96a0",
      "DATA",
      [
        "storage",
        "00436b98",
        null,
        "byte[55]"
      ]
    ],
    [
      "009f96a8",
      "DATA",
      [
        "storage",
        "00436ba0",
        "fde_00436ba0",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "009f9688",
      "DATA",
      [
        "storage",
        "00436ba0",
        null,
        "byte[47]"
      ]
    ],
    [
      "009f96a0",
      "DATA",
      [
        "storage",
        "00436b98",
        null,
        "byte[47]"
      ]
    ],
    [
      "009f96a8",
      "DATA",
      [
        "storage",
        "00436ba0",
        null,
        "byte[47]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f87a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f8/009f8670.md#insn-009f87a8) · [`009f87b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f8/009f8670.md#insn-009f87b4) · [`009f86d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f8/009f8670.md#insn-009f86d0)
- 新版 [`009f9754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f9/009f961c.md#insn-009f9754) · [`009f9760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f9/009f961c.md#insn-009f9760) · [`009f967c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f9/009f961c.md#insn-009f967c)

~~~diff
- 009f87a8 ["INT_ADD", "register:40f0:8", ["const:9f87a8:8", "const:4:8"]]
- 009f87a8 ["CALL", null, ["ram:6cbacc:8"]]
+ 009f9754 ["INT_ADD", "register:40f0:8", ["const:9f9754:8", "const:4:8"]]
+ 009f9754 ["CALL", null, ["ram:6cbe7c:8"]]
- 009f87a8 bytes c94cf397
+ 009f9754 bytes ca49f397
- 009f87b4 ["INT_ADD", "register:40f0:8", ["const:9f87b4:8", "const:4:8"]]
- 009f87b4 ["CALL", null, ["ram:6ccbd0:8"]]
+ 009f9760 ["INT_ADD", "register:40f0:8", ["const:9f9760:8", "const:4:8"]]
+ 009f9760 ["CALL", null, ["ram:6ccf80:8"]]
- 009f87b4 bytes 0751f397
+ 009f9760 bytes 084ef397
- 009f86d0 ["INT_ADD", "register:40f0:8", ["const:9f86d0:8", "const:4:8"]]
- 009f86d0 ["CALL", null, ["callee:006c5700:8"]]
+ 009f967c ["INT_ADD", "register:40f0:8", ["const:9f967c:8", "const:4:8"]]
+ 009f967c ["CALL", null, ["callee:006c5700:8"]]
- 009f86d0 bytes 2033f397
+ 009f967c bytes 2130f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce350172288540216ee4f5b747aee24c"></a>

### [`00a2ea1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2ea1c.md) → [`00a2fa10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2f/00a2fa10.md) FUN_00a2fa10

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00a2eb48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2eb48.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00a2c310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2c/00a2c310.md) · 呼出先 4件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00a2fb3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2f/00a2fb3c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 83.33% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2eb14"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a2fb08"
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
      "unmatched:00a2eb14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2faf8"
      ]
    ]
  ],
  "added": [
    [
      "00a2fb08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a2faf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a2eb14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2ea1c.md#insn-00a2eb14) · [`00a2ea44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2ea1c.md#insn-00a2ea44)
- 新版 [`00a2fb08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2f/00a2fa10.md#insn-00a2fb08) · [`00a2fa38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2f/00a2fa10.md#insn-00a2fa38)

~~~diff
- 00a2eb14 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a2eb14 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00a2eb14 bytes 81ffff54
+ 00a2fb08 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a2fb08 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00a2fb08 bytes 81ffff54
- 00a2ea44 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
+ 00a2fa38 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00a2ea44 bytes c0060054
+ 00a2fa38 bytes c0060054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc5a87173e42edd5dc5960ea96db4c74"></a>

### [`00a2efbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2efbc.md) → [`00a2ffb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2f/00a2ffb0.md) FUN_00a2ffb0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0086c30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c30c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00a271bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a27/00a271bc.md) · 呼出先 3件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0086d2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086d/0086d2b8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.00% / 新版 87.00%

CFGの説明率　旧版 36.61% / 新版 37.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 10件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2f028"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a2f16c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a3001c"
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
      "unmatched:00a2f02c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a30068"
      ]
    ],
    [
      "unmatched:00a2f038",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a2f030"
      ]
    ],
    [
      "unmatched:00a2f040",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a2f030"
      ]
    ]
  ],
  "added": [
    [
      "00a30020",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a30068"
      ]
    ],
    [
      "00a3002c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a30024"
      ]
    ],
    [
      "00a30034",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a30024"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a2f028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2efbc.md#insn-00a2f028) · [`00a2f02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2efbc.md#insn-00a2f02c) · [`00a2f038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2efbc.md#insn-00a2f038)

~~~diff
- 00a2f028 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:8:8"]]
- 00a2f028 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a2f028 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00a2f028 bytes ff0600f9
- 00a2f02c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a2f02c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00a2f02c bytes 480200b4
- 00a2f038 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a2f038 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00a2f038 bytes c8ffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b552c20aea685643cecb666afe99d56"></a>

### [`00a31d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31d04.md) → [`00a32cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a32/00a32cf8.md) FUN_00a32cf8

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a31fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31fa8.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00a32f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a32/00a32f9c.md) · 呼出先 3件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00803b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803b14.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 95.27% / 新版 95.27%

CFGの説明率　旧版 71.62% / 新版 74.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a31db0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a31db4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a31db4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a31d44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a32e18"
      ]
    ],
    [
      "unmatched:00a31e88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a32e64"
      ]
    ]
  ],
  "added": [
    [
      "00a32d38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a32e18"
      ]
    ],
    [
      "00a32e7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a32e64"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a31d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31d04.md#insn-00a31d44) · [`00a31db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31d04.md#insn-00a31db0) · [`00a31db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31d04.md#insn-00a31db4)

~~~diff
- 00a31d44 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00a31d44 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 00a31d44 bytes 090700b4
- 00a31db0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:68:8"]]
- 00a31db0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a31db0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00a31db0 bytes 1f3400f9
- 00a31db4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00a31db4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a31db4 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00a31db4 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00a31db4 bytes 1f7c00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cba74d39daf5885d8ccdc19ab45242a9"></a>

### [`00a32a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a32a58.md) → [`00a33a4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a33/00a33a4c.md) FUN_00a33a4c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 12件 [`006bedb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006be/006bedb4.md) [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) [`007cb638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cb/007cb638.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) [`00802d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)
- 新版 呼出元 12件 [`006bf164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bf/006bf164.md) [`00773cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773cc8.md) [`007cc59c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cc/007cc59c.md) [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) [`007e00a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007e0/007e00a4.md) · 呼出先 5件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00803b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803b14.md) [`00803c64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803c64.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c594f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c594f0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 96.05% / 新版 96.05%

CFGの説明率　旧版 66.67% / 新版 64.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a32db4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a33da8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a32a8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a32a8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a33d54"
      ]
    ],
    [
      "unmatched:00a32a94",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00a33a94"
      ]
    ],
    [
      "unmatched:00a32ae8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a33b20"
      ]
    ]
  ],
  "added": [
    [
      "00a33a80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a33d54"
      ]
    ],
    [
      "00a33a88",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00a33a94"
      ]
    ],
    [
      "00a33adc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a33b20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a32a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a32a58.md#insn-00a32a8c) · [`00a32ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a32a58.md#insn-00a32ae8) · [`00a32b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a32a58.md#insn-00a32b78)

~~~diff
- 00a32a8c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a32a8c ["CBRANCH", null, ["local:b59:8", "tmp:0:1"]]
- 00a32a8c bytes a81600b4
- 00a32ae8 ["CBRANCH", null, ["local:b22:8", "register:101:1"]]
- 00a32ae8 bytes 20020054
- 00a32b78 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a32b78 ["CBRANCH", null, ["local:b36:8", "tmp:0:1"]]
- 00a32b78 bytes ca030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bc0d66f061577fa51b323e3ad09ffdd"></a>

### [`00a3574c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a35/00a3574c.md) → [`00a36740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a36/00a36740.md) FUN_00a36740

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009d3b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d3/009d3b48.md) · 呼出先 4件 [`00727a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727a28.md) [`00727d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727d74.md) [`00727ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727ec0.md) [`0072800c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00728/0072800c.md)
- 新版 呼出元 1件 [`009d4af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d4/009d4af4.md) · 呼出先 4件 [`00727dd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00727/00727dd8.md) [`00728124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00728/00728124.md) [`00728270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00728/00728270.md) [`007283bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00728/007283bc.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 85.00% / 新版 77.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a35814"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a36808"
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
      "unmatched:00a35814",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a36820"
      ]
    ]
  ],
  "added": [
    [
      "00a36808",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a36820"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a35814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a35/00a3574c.md#insn-00a35814) · [`00a35764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a35/00a3574c.md#insn-00a35764)
- 新版 [`00a36808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a36/00a36740.md#insn-00a36808) · [`00a36758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a36/00a36740.md#insn-00a36758)

~~~diff
- 00a35814 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a35814 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00a35814 bytes cb000054
+ 00a36808 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00a36808 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00a36808 bytes cb000054
- 00a35764 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a35764 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00a36758 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00a36758 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00a35764 bytes ab050054
+ 00a36758 bytes ab050054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13db8439846e9b118fea279add12ef0d"></a>

### [`00a35854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a35/00a35854.md) → [`00a36848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a36/00a36848.md) FUN_00a36848

採用 · 移動量 `+0xff4` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009d3b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d3/009d3b48.md) · 呼出先 0件 
- 新版 呼出元 1件 [`009d4af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d4/009d4af4.md) · 呼出先 0件 

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-8f8ed136d1ebc588277dfe84fab2f901"></a>

### [`00a380b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a380b8.md) → [`00a390ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a39/00a390ac.md) FUN_00a390ac

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00869280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869280.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0086a22c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086a22c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 37.50% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a380b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a380b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a380bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a380b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a380bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a380c0",
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
      "00a390ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a390b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a390b4",
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

- 旧版 [`00a380b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a380b8.md#insn-00a380b8) · [`00a380bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a380b8.md#insn-00a380bc) · [`00a380c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a380b8.md#insn-00a380c0)

~~~diff
- 00a380b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a380b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a380b8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00a380b8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a380b8 bytes fd7bbda9
- 00a380bc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a380bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00a380bc bytes f50b00f9
- 00a380c0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a380c0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a380c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a380c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a380c0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fca8fea4d0bd8769e961424fba77274b"></a>

### [`00a391f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a391f4.md) → [`00a3a1e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3a/00a3a1e8.md) FUN_00a3a1e8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.10% / 新版 87.10%

CFGの説明率　旧版 91.67% / 新版 84.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a391f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a391f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a391f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a391f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a391f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a391fc",
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
      "00a3a1e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a3a1ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a3a1f0",
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

- 旧版 [`00a391f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a391f4.md#insn-00a391f4) · [`00a391f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a391f4.md#insn-00a391f8) · [`00a391fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a391f4.md#insn-00a391fc)

~~~diff
- 00a391f4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a391f4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a391f4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00a391f4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a391f4 bytes fd7bbda9
- 00a391f8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a391f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00a391f8 bytes f50b00f9
- 00a391fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a391fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a391fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a391fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a391fc bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a78aa05c9daab506c90edd2f86012165"></a>

### [`00a39270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39270.md) → [`00a3a264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3a/00a3a264.md) FUN_00a3a264

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a36170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a36/00a36170.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00a39454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39454.md) [`00a3957c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a3957c.md) [`00a39724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39724.md) [`00a39738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39738.md)
- 新版 呼出元 1件 [`00a37164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a37/00a37164.md) · 呼出先 8件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00a3a448`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3a/00a3a448.md) [`00a3a570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3a/00a3a570.md) [`00a3a718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3a/00a3a718.md) [`00a3a72c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3a/00a3a72c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.04% / 新版 83.04%

CFGの説明率　旧版 54.17% / 新版 52.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39274"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39274"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39278"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a39274",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a39278",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a3927c",
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
      "00a3a268",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00a3a26c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a3a270",
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

- 旧版 [`00a39274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39270.md#insn-00a39274) · [`00a39278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39270.md#insn-00a39278) · [`00a3927c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39270.md#insn-00a3927c)

~~~diff
- 00a39274 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a39274 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a39274 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00a39274 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a39274 bytes fd7b03a9
- 00a39278 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00a39278 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00a39278 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00a39278 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a39278 bytes f85f04a9
- 00a3927c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a3927c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a3927c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00a3927c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a3927c bytes f65705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c603c0e2f37aa7e9dfaa195a1c772fe"></a>

### [`00a39a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39a24.md) → [`00a3aa18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3a/00a3aa18.md) FUN_00a3aa18

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a39894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39894.md) · 呼出先 2件 [`00a39be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39be8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00a3a888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3a/00a3a888.md) · 呼出先 2件 [`00a3abdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3a/00a3abdc.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.41% / 新版 89.41%

CFGの説明率　旧版 33.33% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39a6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39a6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39a70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a39a6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a39a70",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a39a74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a3aaf8"
      ]
    ]
  ],
  "added": [
    [
      "00a3aa60",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00a3aa64",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00a3aa68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a3aaf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a39a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39a24.md#insn-00a39a6c) · [`00a39a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39a24.md#insn-00a39a70) · [`00a39a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39a24.md#insn-00a39a74)

~~~diff
- 00a39a6c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a39a6c ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 00a39a6c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:8:8"]]
- 00a39a6c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a39a6c bytes f6db00a9
- 00a39a70 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00a39a70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a39a70 bytes e81700f9
- 00a39a74 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00a39a74 bytes 80040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9ae74a11b18d29e13d3e833f7964e39"></a>

### [`00a39cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39cc8.md) → [`00a3acbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3a/00a3acbc.md) FUN_00a3acbc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a39c90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39c90.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00a3ac84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3a/00a3ac84.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 76.92% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39cd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39cd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a3accc"
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
      "unmatched:00a39cd8",
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
      "00a3accc",
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

- 旧版 [`00a39cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39cc8.md#insn-00a39cd8) · [`00a39ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39cc8.md#insn-00a39ccc)
- 新版 [`00a3accc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3a/00a3acbc.md#insn-00a3accc) · [`00a3acc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3a/00a3acbc.md#insn-00a3acc0)

~~~diff
- 00a39cd8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a39cd8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a39cd8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a39cd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a39cd8 bytes f44f02a9
+ 00a3accc ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00a3accc ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00a3accc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
+ 00a3accc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a3accc bytes f44f02a9
- 00a39ccc ["CBRANCH", null, ["local:b18:8", "register:101:1"]]
+ 00a3acc0 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 00a39ccc bytes 00050054
+ 00a3acc0 bytes 00050054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e5b42442022150363d90eceecd0fd6e"></a>

### [`00a39e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39e2c.md) → [`00a3ae20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3a/00a3ae20.md) FUN_00a3ae20

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a3815c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a3815c.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00869280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869280.md) [`00a3a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a058.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00a39150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a39/00a39150.md) · 呼出先 6件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0086a22c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086a22c.md) [`00a3b04c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3b/00a3b04c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.81% / 新版 92.81%

CFGの説明率　旧版 71.43% / 新版 74.07%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39f90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39f90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39f94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a39e64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a3aed4"
      ]
    ]
  ],
  "added": [
    [
      "00a3ae58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a3aed4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a39e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39e2c.md#insn-00a39e64) · [`00a39f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39e2c.md#insn-00a39f90) · [`00a39f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a39/00a39e2c.md#insn-00a39f94)

~~~diff
- 00a39e64 ["CBRANCH", null, ["local:b6:8", "register:102:1"]]
- 00a39e64 bytes e2030054
- 00a39f90 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:10:8"]]
- 00a39f90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5040:16"]]
- 00a39f90 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00a39f90 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00a39f90 bytes 228100ad
- 00a39f94 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a39f94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00a39f94 bytes 2101803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25f1ecec6e1c219bc847ff49140f3a13"></a>

### [`00a3a06c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a06c.md) → [`00a3b060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3b/00a3b060.md) FUN_00a3b060

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a3815c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a38/00a3815c.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`008691e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/008691e0.md) [`00a3a2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a2bc.md) [`00a3a4b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a4b4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00a39150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a39/00a39150.md) · 呼出先 7件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0086a18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086a18c.md) [`00a3b2b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3b/00a3b2b0.md) [`00a3b4a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3b/00a3b4a8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.01% / 新版 71.01%

CFGの説明率　旧版 47.06% / 新版 43.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3a090"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3a0f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3a168"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a3a090",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a3a0bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a3b144"
      ]
    ],
    [
      "unmatched:00a3a0e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a3b25c"
      ]
    ]
  ],
  "added": [
    [
      "00a3b084",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00a3b0b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a3b144"
      ]
    ],
    [
      "00a3b0dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a3b25c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3a090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a06c.md#insn-00a3a090) · [`00a3a0bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a06c.md#insn-00a3a0bc) · [`00a3a0e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3a06c.md#insn-00a3a0e8)

~~~diff
- 00a3a090 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a3a090 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a3a090 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a3a090 bytes a8831ff8
- 00a3a0bc ["CBRANCH", null, ["local:b16:8", "register:102:1"]]
- 00a3a0bc bytes a2040054
- 00a3a0e8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a3a0e8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00a3a0e8 ["CBRANCH", null, ["local:b37:8", "tmp:1:1"]]
- 00a3a0e8 bytes 080c0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69c9990539e715a4859a58c9819c7925"></a>

### [`00a3b918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3b/00a3b918.md) → [`00a3c90c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3c/00a3c90c.md) FUN_00a3c90c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a3ab1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3a/00a3ab1c.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00a3bb10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3b/00a3bb10.md) · 呼出先 3件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 42.42% / 新版 41.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3b948"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3b94c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a3c93c"
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
      "unmatched:00a3b950",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a3ca34"
      ]
    ],
    [
      "unmatched:00a3b984",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a3c98c"
      ]
    ],
    [
      "unmatched:00a3b9a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a3c980"
      ]
    ]
  ],
  "added": [
    [
      "00a3c944",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a3ca34"
      ]
    ],
    [
      "00a3c978",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a3c98c"
      ]
    ],
    [
      "00a3c998",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a3c980"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3b948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3b/00a3b918.md#insn-00a3b948) · [`00a3b94c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3b/00a3b918.md#insn-00a3b94c) · [`00a3b950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3b/00a3b918.md#insn-00a3b950)

~~~diff
- 00a3b948 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:10:8"]]
- 00a3b948 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a3b948 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00a3b948 bytes 1f0900f9
- 00a3b94c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a3b94c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
- 00a3b94c bytes 160100f9
- 00a3b950 ["CBRANCH", null, ["local:b21:8", "register:101:1"]]
- 00a3b950 bytes 80070054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fb9274faac5d70cbc14bf734dece30f"></a>

### [`00a3da48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3d/00a3da48.md) → [`00a3ea3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3e/00a3ea3c.md) FUN_00a3ea3c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a3ce6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3c/00a3ce6c.md) · 呼出先 2件 [`008ab9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ab/008ab9c0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00a3de60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3d/00a3de60.md) · 呼出先 2件 [`008ac96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ac/008ac96c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3da84"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a3ea78"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a3da84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3d/00a3da48.md#insn-00a3da84) · [`00a3da6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3d/00a3da48.md#insn-00a3da6c)
- 新版 [`00a3ea78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3e/00a3ea3c.md#insn-00a3ea78) · [`00a3ea60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3e/00a3ea3c.md#insn-00a3ea60)

~~~diff
- 00a3da84 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00a3da84 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00a3da84 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00a3da84 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a3da84 bytes e903899a
+ 00a3ea78 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 00a3ea78 ["COPY", "tmp:1:8", ["tmp:0:8"]]
+ 00a3ea78 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00a3ea78 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a3ea78 bytes e903899a
- 00a3da6c ["INT_ADD", "register:40f0:8", ["const:a3da6c:8", "const:4:8"]]
- 00a3da6c ["CALL", null, ["callee:008ac96c:8"]]
+ 00a3ea60 ["INT_ADD", "register:40f0:8", ["const:a3ea60:8", "const:4:8"]]
+ 00a3ea60 ["CALL", null, ["callee:008ac96c:8"]]
- 00a3da6c bytes d5b7f997
+ 00a3ea60 bytes c3b7f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38fcf5f8f0b3abf6457a89871d42ed59"></a>

### [`00a3e79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e79c.md) → [`00a3f790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3f/00a3f790.md) FUN_00a3f790

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a3bd98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3b/00a3bd98.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 1件 [`00a3cd8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3c/00a3cd8c.md) · 呼出先 1件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3e79c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3e79c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a3f790"
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
      "unmatched:00a3e79c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a3e7a8",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a3e7ac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00442c90"
      ]
    ]
  ],
  "added": [
    [
      "00a3f790",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a3f79c",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ],
    [
      "00a3f7a0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00442c90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3e79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e79c.md#insn-00a3e79c) · [`00a3e7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e79c.md#insn-00a3e7ac)
- 新版 [`00a3f790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3f/00a3f790.md#insn-00a3f790)

~~~diff
- 00a3e79c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a3e79c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a3e79c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00a3e79c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a3e79c bytes fd7bbfa9
- 00a3e7ac ["INT_ADD", "register:40f0:8", ["const:a3e7ac:8", "const:4:8"]]
- 00a3e7ac ["CALL", null, ["callee:00442c90:8"]]
- 00a3e7ac bytes 7110e897
+ 00a3f790 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00a3f790 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00a3f790 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00a3f790 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00a3f790 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26bcf6f39102dd553e1f890c9c91d7bb"></a>

### [`00a3e7e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e7e8.md) → [`00a3f7dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3f/00a3f7dc.md) FUN_00a3f7dc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3e7f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3e7f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a3f7e8"
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
      "unmatched:00a3e7f4",
      "DATA",
      [
        "storage",
        "00c8b488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3f7e8",
      "DATA",
      [
        "storage",
        "00c8c458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3e7f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e7e8.md#insn-00a3e7f4) · [`00a3e7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e7e8.md#insn-00a3e7f8)
- 新版 [`00a3f7e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3f/00a3f7dc.md#insn-00a3f7e8)

~~~diff
- 00a3e7f4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a3e7f4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a3e7f4 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00a3e7f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a3e7f4 bytes 292000a9
- 00a3e7f8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a3e7f8 ["RETURN", null, ["register:0:8"]]
- 00a3e7f8 bytes c0035fd6
+ 00a3f7e8 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a3f7e8 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00a3f7e8 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00a3f7e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a3f7e8 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a683417aedc9781d0c2404be1144afc"></a>

### [`00a3e87c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e87c.md) → [`00a3f870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3f/00a3f870.md) FUN_00a3f870

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.95% / 新版 80.95%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3e898"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a3f88c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3e8bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a3e898",
      "DATA",
      [
        "storage",
        "00c8b508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3f88c",
      "DATA",
      [
        "storage",
        "00c8c4d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3e898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e87c.md#insn-00a3e898) · [`00a3e8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e87c.md#insn-00a3e8bc)
- 新版 [`00a3f88c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3f/00a3f870.md#insn-00a3f88c)

~~~diff
- 00a3e898 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a3e898 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00a3e898 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:40:8"]]
- 00a3e898 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a3e898 bytes 080404f8
- 00a3e8bc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a3e8bc ["RETURN", null, ["register:0:8"]]
- 00a3e8bc bytes c0035fd6
+ 00a3f88c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a3f88c ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00a3f88c ["INT_ADD", "register:4000:8", ["register:4000:8", "const:40:8"]]
+ 00a3f88c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00a3f88c bytes 080404f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02edd973d9dc1eb35f8e92b6eae5fe01"></a>

### [`00a3e974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e974.md) → [`00a3f968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3f/00a3f968.md) FUN_00a3f968

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00a3ecb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3ecb8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00a3fcac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3f/00a3fcac.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 14.29% / 新版 14.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3e980"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a3f974"
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
      "unmatched:00a3e980",
      "DATA",
      [
        "storage",
        "00c8b508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3f974",
      "DATA",
      [
        "storage",
        "00c8c4d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3e980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e974.md#insn-00a3e980) · [`00a3e974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e974.md#insn-00a3e974)
- 新版 [`00a3f974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3f/00a3f968.md#insn-00a3f974)

~~~diff
- 00a3e980 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a3e980 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a3e980 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:8:8"]]
- 00a3e980 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a3e980 bytes 098500f8
+ 00a3f974 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a3f974 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00a3f974 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:8:8"]]
+ 00a3f974 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00a3f974 bytes 098500f8
- 00a3e974 ["COPY", "register:4040:8", ["register:4008:8"]]
- 00a3e974 bytes e80301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1138fa3f54a88a51fcd57b430385706e"></a>

### [`00a3e9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e9dc.md) → [`00a3f9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3f/00a3f9d0.md) FUN_00a3f9d0

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a3ce6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3c/00a3ce6c.md) · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00a3de60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3d/00a3de60.md) · 呼出先 2件 [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3e9dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3e9dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3e9e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a3e9dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a3e9e0",
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
      "00a3f9d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a3f9d4",
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

- 旧版 [`00a3e9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e9dc.md#insn-00a3e9dc) · [`00a3e9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e9dc.md#insn-00a3e9e0)
- 新版 [`00a3f9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3f/00a3f9d0.md#insn-00a3f9d0)

~~~diff
- 00a3e9dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a3e9dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a3e9dc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a3e9dc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a3e9dc bytes fd7bbea9
- 00a3e9e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a3e9e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00a3e9e0 bytes f30b00f9
+ 00a3f9d0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00a3f9d0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00a3f9d0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00a3f9d0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00a3f9d0 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1a419186268c62e078cd46df2e7eaa0"></a>

### [`00a3ee14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3ee14.md) → [`00a3fe08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3f/00a3fe08.md) FUN_00a3fe08

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3ee30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a3fe24"
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
      "unmatched:00a3ee30",
      "DATA",
      [
        "storage",
        "00c8b578",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3fe24",
      "DATA",
      [
        "storage",
        "00c8c548",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3ee30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3ee14.md#insn-00a3ee30) · [`00a3ee24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3ee14.md#insn-00a3ee24)
- 新版 [`00a3fe24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3f/00a3fe08.md#insn-00a3fe24) · [`00a3fe18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3f/00a3fe08.md#insn-00a3fe18)

~~~diff
- 00a3ee30 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a3ee30 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00a3ee30 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:28:8"]]
- 00a3ee30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a3ee30 bytes 088402f8
+ 00a3fe24 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a3fe24 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00a3fe24 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:28:8"]]
+ 00a3fe24 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00a3fe24 bytes 088402f8
- 00a3ee24 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a3fe18 ["COPY", "register:4040:8", ["const:c8c000:8"]]
- 00a3ee24 bytes 681200b0
+ 00a3fe18 bytes 681200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c0616244408d7069cb178cea05c94d1"></a>

### [`00a40de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a40/00a40de4.md) → [`00a41dd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a41/00a41dd8.md) FUN_00a41dd8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00a40f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a40/00a40f4c.md) [`00a40f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a40/00a40f50.md) [`00ac9604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac9/00ac9604.md) [`00acac44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aca/00acac44.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00a41f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a41/00a41f40.md) [`00a41f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a41/00a41f44.md) [`00aca5f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aca/00aca5f8.md) [`00acbc38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acb/00acbc38.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.95% / 新版 80.95%

CFGの説明率　旧版 27.27% / 新版 23.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a40e08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a40e24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a40e24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a40e08",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a40e24",
      "DATA",
      [
        "storage",
        "00c8b798",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a40e24",
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
      "00a41dfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a41e18",
      "DATA",
      [
        "storage",
        "00c8c768",
        null,
        "undefined *"
      ]
    ],
    [
      "00a41e18",
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

- 旧版 [`00a40e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a40/00a40de4.md#insn-00a40e08) · [`00a40e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a40/00a40de4.md#insn-00a40e24) · [`00a40e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a40/00a40de4.md#insn-00a40e40)

~~~diff
- 00a40e08 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a40e08 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a40e08 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a40e08 bytes a8831ff8
- 00a40e24 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a40e24 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a40e24 ["COPY", "tmp:2:8", ["register:8:8"]]
- 00a40e24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a40e24 bytes e85700a9
- 00a40e40 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00a40e40 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57b9f0c5a5e870735525938ad78fb037"></a>

### [`00a40f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a40/00a40f04.md) → [`00a41ef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a41/00a41ef8.md) FUN_00a41ef8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a40f28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a40f28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a41f1c"
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
      "unmatched:00a40f28",
      "DATA",
      [
        "storage",
        "00c8b798",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a40f2c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a40f30",
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
      "00a41f1c",
      "DATA",
      [
        "storage",
        "00c8c768",
        null,
        "undefined *"
      ]
    ],
    [
      "00a41f20",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a41f24",
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

- 旧版 [`00a40f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a40/00a40f04.md#insn-00a40f28) · [`00a40f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a40/00a40f04.md#insn-00a40f34)
- 新版 [`00a41f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a41/00a41ef8.md#insn-00a41f1c)

~~~diff
- 00a40f28 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a40f28 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a40f28 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a40f28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a40f28 bytes 082400a9
- 00a40f34 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a40f34 ["RETURN", null, ["register:0:8"]]
- 00a40f34 bytes c0035fd6
+ 00a41f1c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a41f1c ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a41f1c ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00a41f1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a41f1c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1234b0dbb14a90a1917b028f76e5ad0"></a>

### [`00a413d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a41/00a413d8.md) → [`00a423cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a42/00a423cc.md) FUN_00a423cc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a41600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a41/00a41600.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00a425f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a42/00a425f4.md) · 呼出先 8件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00487dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487dc4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 64.29% / 新版 62.07%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a41550"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a41584"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a415a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a424e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a41590"
      ]
    ],
    [
      "unmatched:00a41550",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a425f0"
      ]
    ],
    [
      "unmatched:00a41584",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a425f0"
      ]
    ]
  ],
  "added": [
    [
      "00a424e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a42584"
      ]
    ],
    [
      "00a42544",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a425f0"
      ]
    ],
    [
      "00a42578",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a425f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a41550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a41/00a413d8.md#insn-00a41550) · [`00a41584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a41/00a413d8.md#insn-00a41584) · [`00a415a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a41/00a413d8.md#insn-00a415a0)

~~~diff
- 00a41550 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a41550 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
- 00a41550 bytes 61050054
- 00a41584 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a41584 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
- 00a41584 bytes c1030054
- 00a415a0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a415a0 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
- 00a415a0 bytes e1020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a8e7c015bfa0873a68f2e5b3b30225f"></a>

### [`00a4203c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a42/00a4203c.md) → [`00a43030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a43/00a43030.md) FUN_00a43030

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008c1ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c1/008c1ef0.md) [`008c4974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c4/008c4974.md) · 呼出先 1件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)
- 新版 呼出元 2件 [`008c2e9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c2/008c2e9c.md) [`008c5920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c5/008c5920.md) · 呼出先 1件 [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 66.67% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a42054"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a43048"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a42054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a42/00a4203c.md#insn-00a42054) · [`00a42040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a42/00a4203c.md#insn-00a42040)
- 新版 [`00a43048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a43/00a43030.md#insn-00a43048) · [`00a43034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a43/00a43030.md#insn-00a43034)

~~~diff
- 00a42054 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a42054 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a42054 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00a42054 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00a42054 bytes 29b18a9a
+ 00a43048 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00a43048 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a43048 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00a43048 ["COPY", "tmp:1:8", ["register:4050:8"]]
+ 00a43048 bytes 29b18a9a
- 00a42040 ["INT_EQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00a42040 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00a43034 ["INT_EQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
+ 00a43034 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00a42040 bytes aa0100b4
+ 00a43034 bytes aa0100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1666bb82e5a15bf14786b590179ab850"></a>

### [`00a42110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a42/00a42110.md) → [`00a43104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a43/00a43104.md) FUN_00a43104

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 16件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`005e1660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1660.md) [`005f57d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f5/005f57d0.md) [`006d02fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d0/006d02fc.md) [`00759634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00759/00759634.md) · 呼出先 2件 [`0066a448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066a/0066a448.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 16件 [`005bcbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bcbbc.md) [`005e1a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e1a10.md) [`005f5b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005f5/005f5b80.md) [`006d06ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d0/006d06ac.md) [`007599e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00759/007599e4.md) · 呼出先 2件 [`0066a7f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0066a/0066a7f8.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 47.06% / 新版 36.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a421c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a421d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a431b8"
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
      "unmatched:00a421c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a431d0"
      ]
    ]
  ],
  "added": [
    [
      "00a431b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a431d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a421c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a42/00a42110.md#insn-00a421c4) · [`00a421d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a42/00a42110.md#insn-00a421d0)
- 新版 [`00a431b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a43/00a43104.md#insn-00a431b8)

~~~diff
- 00a421c4 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00a421c4 bytes c0000054
- 00a421d0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a421d0 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00a421d0 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00a421d0 ["COPY", "tmp:3:8", ["register:4098:8"]]
- 00a421d0 bytes 69c2889a
+ 00a431b8 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
+ 00a431b8 bytes c0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51b9377111f161ae0e274e633a75d6c4"></a>

### [`00a430ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a43/00a430ac.md) → [`00a440a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a44/00a440a0.md) FUN_00a440a0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005e1660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1660.md) [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) · 呼出先 5件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00853cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/00853cc8.md) [`00a42084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a42/00a42084.md) [`00a42110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a42/00a42110.md) [`00af398c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af398c.md)
- 新版 呼出元 2件 [`005e1a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e1/005e1a10.md) [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) · 呼出先 5件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00854c74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00854/00854c74.md) [`00a43078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a43/00a43078.md) [`00a43104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a43/00a43104.md) [`00af4980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af4/00af4980.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 61.54% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a430ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a430ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a430b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a430ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a430b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a430b4",
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
      "00a440a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a440a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a440a8",
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

- 旧版 [`00a430ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a43/00a430ac.md#insn-00a430ac) · [`00a430b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a43/00a430ac.md#insn-00a430b0) · [`00a430b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a43/00a430ac.md#insn-00a430b4)

~~~diff
- 00a430ac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a430ac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a430ac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00a430ac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a430ac bytes fd7bbda9
- 00a430b0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a430b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00a430b0 bytes f50b00f9
- 00a430b4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a430b4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a430b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a430b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a430b4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea602093f5aa05cb04bec02d602cfbaa"></a>

### [`00a46c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46c88.md) → [`00a47c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47c7c.md) FUN_00a47c7c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 30件 [`005c4998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c4998.md) [`005c69b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c69b8.md) [`005c8800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8800.md) [`005c8f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8f3c.md) [`006535e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/006535e0.md) · 呼出先 2件 [`00a46c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46c88.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md)
- 新版 呼出元 30件 [`005c4d48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c4d48.md) [`005c6d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c6d68.md) [`005c8bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c8/005c8bb0.md) [`005c92ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c9/005c92ec.md) [`00653990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653990.md) · 呼出先 2件 [`00a47c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47c7c.md) [`00c596b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a47ccc",
      "PARAM",
      [
        "storage",
        "00c8b848",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a47cd0",
      "PARAM",
      [
        "storage",
        "00c8b858",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a47ccc",
      "PARAM",
      [
        "storage",
        "00c8c818",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a47cd0",
      "PARAM",
      [
        "storage",
        "00c8c828",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a46cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46c88.md#insn-00a46cc4) · [`00a46cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46c88.md#insn-00a46cc8) · [`00a46ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46c88.md#insn-00a46ccc)
- 新版 [`00a47cb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47c7c.md#insn-00a47cb8) · [`00a47cbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47c7c.md#insn-00a47cbc)

~~~diff
- 00a46cc4 ["COPY", "register:40b8:8", ["const:c8b000:8"]]
+ 00a47cb8 ["COPY", "register:40b8:8", ["const:c8c000:8"]]
- 00a46cc4 bytes 371200b0
+ 00a47cb8 bytes 371200b0
- 00a46cc8 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00a46cc8 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 00a46cc8 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 00a46cc8 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 00a47cbc ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00a47cbc ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 00a47cbc ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 00a47cbc ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 00a46cc8 bytes f7222191
+ 00a47cbc bytes f7622091
- 00a46ccc ["COPY", "register:40c0:8", ["const:c8b000:8"]]
- 00a46ccc bytes 381200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19c3e1c99d1d020e63fa109ac600697c"></a>

### [`00a46e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46e3c.md) → [`00a47e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47e30.md) FUN_00a47e30

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008bdb58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bd/008bdb58.md) · 呼出先 5件 [`00a46a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46a78.md) [`00a46c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46c88.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`008beb04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008be/008beb04.md) · 呼出先 5件 [`00a47a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47a6c.md) [`00a47c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47c7c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.23% / 新版 91.23%

CFGの説明率　旧版 62.50% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a46eec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a46eec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a46ef8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a46ef4",
      "READ",
      [
        "storage",
        "Stack[-0x64]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a47ee8",
      "READ",
      [
        "storage",
        "Stack[-0x64]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a46eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46e3c.md#insn-00a46eec) · [`00a46ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46e3c.md#insn-00a46ef8) · [`00a46efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46e3c.md#insn-00a46efc)

~~~diff
- 00a46eec ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00a46eec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:4"]]
- 00a46eec ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:4:8"]]
- 00a46eec ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:4"]]
- 00a46eec bytes 0004012d
- 00a46ef8 ["COPY", "tmp:0:4", ["register:40a0:4"]]
- 00a46ef8 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00a46ef8 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:c0:8"]]
- 00a46ef8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:4"]]
- 00a46ef8 bytes 14201829
- 00a46efc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c8:8"]]
- 00a46efc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:8"]]
- 00a46efc bytes 006400fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f97ef23ab25a83be7e66c001a549f8d5"></a>

### [`00a46f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46f2c.md) → [`00a47f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47f20.md) FUN_00a47f20

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0082bec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082b/0082bec0.md) · 呼出先 5件 [`00a46a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46a78.md) [`00a46c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46c88.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`0082ce6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0082c/0082ce6c.md) · 呼出先 5件 [`00a47a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47a6c.md) [`00a47c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47c7c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 68.97% / 新版 68.97%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a46f30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a46f30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a46f34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a46f30",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a46f34",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a46f38",
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
      "00a47f24",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a47f28",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a47f2c",
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

- 旧版 [`00a46f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46f2c.md#insn-00a46f30) · [`00a46f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46f2c.md#insn-00a46f34) · [`00a46f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46f2c.md#insn-00a46f38)

~~~diff
- 00a46f30 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a46f30 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a46f30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a46f30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a46f30 bytes fd7b01a9
- 00a46f34 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a46f34 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a46f34 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a46f34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a46f34 bytes fc6f02a9
- 00a46f38 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a46f38 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a46f38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00a46f38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a46f38 bytes fa6703a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdb729729f933a115ebc6474338e0500"></a>

### [`00a47158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47158.md) → [`00a4814c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a48/00a4814c.md) FUN_00a4814c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`004676bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004676bc.md) [`00467720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467720.md) [`00467758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467758.md) [`00467864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467864.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004679dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/004679dc.md) [`00467a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467a40.md) [`00467a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467a78.md) [`00467b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467b84.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.94% / 新版 98.94%

CFGの説明率　旧版 79.63% / 新版 81.13%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a471b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47158.md#insn-00a471b8) · [`00a471d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47158.md#insn-00a471d4) · [`00a471dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47158.md#insn-00a471dc)
- 新版 [`00a481c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a48/00a4814c.md#insn-00a481c8) · [`00a481d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a48/00a4814c.md#insn-00a481d0)

~~~diff
- 00a471b8 ["INT_XOR", "tmp:0:8", ["register:5040:8", "register:5060:8"]]
- 00a471b8 ["INT_AND", "tmp:1:8", ["tmp:0:8", "register:5020:8"]]
- 00a471b8 ["INT_XOR", "register:5020:8", ["register:5040:8", "tmp:1:8"]]
- 00a471b8 bytes 611c622e
- 00a471d4 ["CBRANCH", null, ["local:b28:8", "register:101:1"]]
+ 00a481c8 ["CBRANCH", null, ["local:b27:8", "register:101:1"]]
- 00a471d4 bytes c0070054
+ 00a481c8 bytes c0070054
- 00a471dc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a471dc ["CBRANCH", null, ["local:b30:8", "tmp:0:1"]]
+ 00a481d0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a481d0 ["CBRANCH", null, ["local:b29:8", "tmp:0:1"]]
- 00a471dc bytes a1080054
+ 00a481d0 bytes a1080054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bccbe9b1869f0beb2b21a86212df3753"></a>

### [`00a47688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47688.md) → [`00a4867c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a48/00a4867c.md) FUN_00a4867c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`004676bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004676bc.md) [`00467720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467720.md) [`00467758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467758.md) [`00467864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467864.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004679dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/004679dc.md) [`00467a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467a40.md) [`00467a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467a78.md) [`00467b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467b84.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 96.02% / 新版 96.02%

CFGの説明率　旧版 67.92% / 新版 64.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a47824"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a47824"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a47828"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a47904",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a48914"
      ]
    ],
    [
      "unmatched:00a4791c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a488fc"
      ]
    ]
  ],
  "added": [
    [
      "00a488f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a48914"
      ]
    ],
    [
      "00a48910",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a488fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a477dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47688.md#insn-00a477dc) · [`00a47824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47688.md#insn-00a47824) · [`00a47828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47688.md#insn-00a47828)

~~~diff
- 00a477dc ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a477dc ["COPY", "tmp:1:4", ["register:4050:4"]]
- 00a477dc ["BOOL_NEGATE", "tmp:2:1", ["tmp:0:1"]]
- 00a477dc ["CBRANCH", null, ["const:2:4", "tmp:2:1"]]
- 00a477dc bytes 4ba58a1a
- 00a47824 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:98:8"]]
- 00a47824 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5060:4"]]
- 00a47824 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:4:8"]]
- 00a47824 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:4"]]
- 00a47824 bytes 6306132d
- 00a47828 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:90:8"]]
- 00a47828 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5040:4"]]
- 00a47828 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:4:8"]]
- 00a47828 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:4"]]
- 00a47828 bytes 6206122d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d79086091aa1c10c6e4b7fe987020a99"></a>

### [`00a4f21c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f21c.md) → [`00a50210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a50/00a50210.md) FUN_00a50210

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 1件 [`00a48f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a48/00a48f48.md) · 呼出先 4件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.79% / 新版 90.79%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4f298"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4f310"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a5028c"
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
      "00a502b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a50330"
      ]
    ],
    [
      "00a502c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a50260"
      ]
    ],
    [
      "unmatched:00a4f2a8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58fe0"
      ]
    ]
  ],
  "added": [
    [
      "00a5023c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a50330"
      ]
    ],
    [
      "00a50248",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a50260"
      ]
    ],
    [
      "00a502b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a50338"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a4f27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f21c.md#insn-00a4f27c) · [`00a4f298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f21c.md#insn-00a4f298) · [`00a4f2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f21c.md#insn-00a4f2a8)

~~~diff
- 00a4f27c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a4f27c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00a4f27c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a4f27c ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00a4f27c bytes 0801899a
- 00a4f298 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00a4f298 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a4f298 bytes 680200f9
- 00a4f2a8 ["INT_ADD", "register:40f0:8", ["const:a4f2a8:8", "const:4:8"]]
- 00a4f2a8 ["CALL", null, ["callee:00c58fe0:8"]]
- 00a4f2a8 bytes 5a230894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29748ce6ad30031bea82e214f55ef7b2"></a>

### [`00a60320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a60/00a60320.md) → [`00a61314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a61/00a61314.md) FUN_00a61314

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a60624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a60/00a60624.md) · 呼出先 3件 [`008003d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/008003d0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a65e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a65/00a65e5c.md)
- 新版 呼出元 1件 [`00a61618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a61/00a61618.md) · 呼出先 3件 [`00801334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00801/00801334.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00a66e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a66/00a66e50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 89.52% / 新版 89.52%

CFGの説明率　旧版 12.50% / 新版 11.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a603ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a60458"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a613a0"
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
      "unmatched:00a603ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a613d4"
      ]
    ],
    [
      "00a6144c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6143c"
      ]
    ],
    [
      "unmatched:00a6042c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65e5c"
      ]
    ]
  ],
  "added": [
    [
      "00a613a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a613d4"
      ]
    ],
    [
      "00a613f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6143c"
      ]
    ],
    [
      "00a61420",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a66e50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a603ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a60/00a60320.md#insn-00a603ac) · [`00a6042c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a60/00a60320.md#insn-00a6042c) · [`00a60458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a60/00a60320.md#insn-00a60458)

~~~diff
- 00a603ac ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a603ac ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00a603ac ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
- 00a603ac bytes a8010054
- 00a6042c ["INT_ADD", "register:40f0:8", ["const:a6042c:8", "const:4:8"]]
- 00a6042c ["CALL", null, ["ram:a65e5c:8"]]
- 00a6042c bytes 8c160094
- 00a60458 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00a60458 bytes 00ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1b2901b713913d482ee85b58c9c7adf"></a>

### [`00a60624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a60/00a60624.md) → [`00a61618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a61/00a61618.md) FUN_00a61618

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) [`00a8e624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8e/00a8e624.md) [`00a91618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a91/00a91618.md) [`00a91824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a91/00a91824.md) [`00a9b02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a9b/00a9b02c.md) · 呼出先 3件 [`00a6014c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a60/00a6014c.md) [`00a60320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a60/00a60320.md) [`00a604c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a60/00a604c4.md)
- 新版 呼出元 6件 [`006bc0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md) [`00a8f618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a8f/00a8f618.md) [`00a9260c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a92/00a9260c.md) [`00a92818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a92/00a92818.md) [`00a9c020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a9c/00a9c020.md) · 呼出先 3件 [`00a61140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a61/00a61140.md) [`00a61314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a61/00a61314.md) [`00a614b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a61/00a614b8.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 63.27% / 新版 63.27%

CFGの説明率　旧版 3.12% / 新版 3.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a60624"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a60624"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a60628"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a60624",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a60628",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a6062c",
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
      "00a61618",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00a6161c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a61620",
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

- 旧版 [`00a60624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a60/00a60624.md#insn-00a60624) · [`00a60628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a60/00a60624.md#insn-00a60628) · [`00a6062c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a60/00a60624.md#insn-00a6062c)

~~~diff
- 00a60624 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a60624 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a60624 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00a60624 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a60624 bytes fd7bbca9
- 00a60628 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a60628 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00a60628 bytes f70b00f9
- 00a6062c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a6062c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a6062c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a6062c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6062c bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e3e878e56f1d6b4247447fdb8183046"></a>

### [`00a658d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a65/00a658d0.md) → [`00a668c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a66/00a668c4.md) FUN_00a668c4

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`007dd7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007dd/007dd7f8.md) [`00a65ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a65/00a65ad0.md) [`00a65cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a65/00a65cdc.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 3件 [`007de75c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007de/007de75c.md) [`00a66ac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a66/00a66ac4.md) [`00a66cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a66/00a66cd0.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 88.46% / 新版 86.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a658d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a658d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a658d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a658d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a658d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a658d8",
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
      "00a668c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a668c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00a668cc",
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

- 旧版 [`00a658d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a65/00a658d0.md#insn-00a658d0) · [`00a658d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a65/00a658d0.md#insn-00a658d4) · [`00a658d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a65/00a658d0.md#insn-00a658d8)

~~~diff
- 00a658d0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a658d0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a658d0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00a658d0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a658d0 bytes fd7bbba9
- 00a658d4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a658d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00a658d4 bytes f90b00f9
- 00a658d8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00a658d8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00a658d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a658d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a658d8 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92b371a2ab96e73f1ca293944f3f9101"></a>

### [`00a66ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a66/00a66ca4.md) → [`00a67c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a67/00a67c98.md) FUN_00a67c98

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00605294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/00605294.md) [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) · 呼出先 2件 [`00a65e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a65/00a65e5c.md) [`00a66524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a66/00a66524.md)
- 新版 呼出元 3件 [`005fea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fea5c.md) [`00605644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00605/00605644.md) [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) · 呼出先 2件 [`00a66e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a66/00a66e50.md) [`00a67518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a67/00a67518.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00a66cd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00a67cc8"
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
      "unmatched:00a66cd4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65e5c"
      ]
    ],
    [
      "unmatched:00a66d04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a66524"
      ]
    ]
  ],
  "added": [
    [
      "00a67cc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a66e50"
      ]
    ],
    [
      "00a67cf8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a67518"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a66cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a66/00a66ca4.md#insn-00a66cd4) · [`00a66d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a66/00a66ca4.md#insn-00a66d04)
- 新版 [`00a67cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a67/00a67c98.md#insn-00a67cc8)

~~~diff
- 00a66cd4 ["INT_ADD", "register:40f0:8", ["const:a66cd4:8", "const:4:8"]]
- 00a66cd4 ["CALL", null, ["ram:a65e5c:8"]]
- 00a66cd4 bytes 62fcff97
+ 00a67cc8 ["INT_ADD", "register:40f0:8", ["const:a67cc8:8", "const:4:8"]]
+ 00a67cc8 ["CALL", null, ["ram:a66e50:8"]]
+ 00a67cc8 bytes 62fcff97
- 00a66d04 ["BRANCH", null, ["ram:a66524:8"]]
- 00a66d04 bytes 08feff17
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d776d9d6e4d0acf9768ad7e104ac0f75"></a>

### [`00a68ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a68/00a68ff8.md) → [`00a69fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a69/00a69fec.md) FUN_00a69fec

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 2件 [`00a6c14c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6c/00a6c14c.md) [`00a6c4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6c/00a6c4f8.md)
- 新版 呼出元 1件 [`007e00a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007e0/007e00a4.md) · 呼出先 2件 [`00a6d140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a6d/00a6d140.md) [`00a6d4ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a6d/00a6d4ec.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00a69024"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00a6a018"
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
      "unmatched:00a69020",
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
      "00a6a014",
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

- 旧版 [`00a69024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a68/00a68ff8.md#insn-00a69024) · [`00a69010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a68/00a68ff8.md#insn-00a69010)
- 新版 [`00a6a018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a69/00a69fec.md#insn-00a6a018) · [`00a6a004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a69/00a69fec.md#insn-00a6a004)

~~~diff
- 00a69024 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a69024 ["RETURN", null, ["register:0:8"]]
- 00a69024 bytes c0035fd6
+ 00a6a018 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00a6a018 ["RETURN", null, ["register:0:8"]]
+ 00a6a018 bytes c0035fd6
- 00a69010 ["INT_ADD", "register:40f0:8", ["const:a69010:8", "const:4:8"]]
- 00a69010 ["CALL", null, ["callee:00a6d4ec:8"]]
+ 00a6a004 ["INT_ADD", "register:40f0:8", ["const:a6a004:8", "const:4:8"]]
+ 00a6a004 ["CALL", null, ["callee:00a6d4ec:8"]]
- 00a69010 bytes 3a0d0094
+ 00a6a004 bytes 3a0d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40dd6c9c535b180ac9328f303ad22c67"></a>

### [`00a69414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a69/00a69414.md) → [`00a6a408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a6a/00a6a408.md) FUN_00a6a408

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 75.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00a69450"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00a6a444"
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
      "unmatched:00a69450",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00a6a444",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a69450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a69/00a69414.md#insn-00a69450) · [`00a69430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a69/00a69414.md#insn-00a69430)
- 新版 [`00a6a444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a6a/00a6a408.md#insn-00a6a444) · [`00a6a424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a6a/00a6a408.md#insn-00a6a424)

~~~diff
- 00a69450 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a69450 ["INT_ADD", "register:40f0:8", ["const:a69450:8", "const:4:8"]]
- 00a69450 ["CALLIND", null, ["register:0:8"]]
- 00a69450 bytes 00013fd6
+ 00a6a444 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a6a444 ["INT_ADD", "register:40f0:8", ["const:a6a444:8", "const:4:8"]]
+ 00a6a444 ["CALLIND", null, ["register:0:8"]]
+ 00a6a444 bytes 00013fd6
- 00a69430 ["INT_ADD", "register:40f0:8", ["const:a69430:8", "const:4:8"]]
- 00a69430 ["CALL", null, ["callee:00c54d90:8"]]
+ 00a6a424 ["INT_ADD", "register:40f0:8", ["const:a6a424:8", "const:4:8"]]
+ 00a6a424 ["CALL", null, ["callee:00c54d90:8"]]
- 00a69430 bytes 5caa0794
+ 00a6a424 bytes 5baa0794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-075d1adda5d929a59259d92e1dba8b1d"></a>

### [`00a6b090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6b/00a6b090.md) → [`00a6c084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a6c/00a6c084.md) FUN_00a6c084

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a69520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a69/00a69520.md) · 呼出先 4件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00a6a514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a6a/00a6a514.md) · 呼出先 4件 [`00494970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494970.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 32.26% / 新版 30.30%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6b13c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a6c130"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6b0c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a6b11c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6c100"
      ]
    ]
  ],
  "added": [
    [
      "00a6c110",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6c100"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6b0c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6b/00a6b090.md#insn-00a6b0c4) · [`00a6b11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6b/00a6b090.md#insn-00a6b11c) · [`00a6b13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6b/00a6b090.md#insn-00a6b13c)

~~~diff
- 00a6b0c4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a6b0c4 ["COPY", "tmp:1:8", ["register:4058:8"]]
- 00a6b0c4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00a6b0c4 ["COPY", "tmp:1:8", ["register:4060:8"]]
- 00a6b0c4 bytes 6bb18c9a
- 00a6b11c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a6b11c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00a6b11c bytes 81ffff54
- 00a6b13c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:10:8"]]
- 00a6b13c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00a6b13c bytes 090900f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0a38e5956251933b403326b4f6bd3c4"></a>

### [`00a6c154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6c/00a6c154.md) → [`00a6d148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a6d/00a6d148.md) FUN_00a6d148

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a6ab3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6a/00a6ab3c.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)
- 新版 呼出元 1件 [`00a6bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a6b/00a6bb30.md) · 呼出先 1件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6c168"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a6d15c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a6c168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6c/00a6c154.md#insn-00a6c168) · [`00a6c15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6c/00a6c154.md#insn-00a6c15c)
- 新版 [`00a6d15c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a6d/00a6d148.md#insn-00a6d15c) · [`00a6d150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a6d/00a6d148.md#insn-00a6d150)

~~~diff
- 00a6c168 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a6c168 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a6c168 bytes 0001803d
+ 00a6d15c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a6d15c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 00a6d15c bytes 0001803d
- 00a6c15c ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
- 00a6c15c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00a6c15c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00a6c15c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00a6d150 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
+ 00a6d150 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00a6d150 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00a6d150 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00a6c15c bytes ca000037
+ 00a6d150 bytes ca000037
~~~


<a id="compare-199f6765bf99ffede93c9b90a532f454"></a>

### [`00a7bb94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7b/00a7bb94.md) → [`00a7cb88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7c/00a7cb88.md) FUN_00a7cb88

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7bbb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7bbb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a7cbac"
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
      "unmatched:00a7bbb8",
      "DATA",
      [
        "storage",
        "00c8bad0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a7bbbc",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7bbc0",
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
      "00a7cbac",
      "DATA",
      [
        "storage",
        "00c8caa0",
        null,
        "undefined *"
      ]
    ],
    [
      "00a7cbb0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a7cbb4",
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

- 旧版 [`00a7bbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7b/00a7bb94.md#insn-00a7bbb8) · [`00a7bbc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7b/00a7bb94.md#insn-00a7bbc4)
- 新版 [`00a7cbac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7c/00a7cb88.md#insn-00a7cbac)

~~~diff
- 00a7bbb8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a7bbb8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a7bbb8 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a7bbb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7bbb8 bytes 082400a9
- 00a7bbc4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a7bbc4 ["RETURN", null, ["register:0:8"]]
- 00a7bbc4 bytes c0035fd6
+ 00a7cbac ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a7cbac ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a7cbac ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00a7cbac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a7cbac bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0af65829e449a4eb6875e212b1e5d89"></a>

### [`00a7bbc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7b/00a7bbc8.md) → [`00a7cbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7c/00a7cbbc.md) FUN_00a7cbbc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7bbd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7bbd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a7cbc8"
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
      "unmatched:00a7bbd4",
      "DATA",
      [
        "storage",
        "00c8bad0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7cbc8",
      "DATA",
      [
        "storage",
        "00c8caa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7bbd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7b/00a7bbc8.md#insn-00a7bbd4) · [`00a7bbd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7b/00a7bbc8.md#insn-00a7bbd8)
- 新版 [`00a7cbc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7c/00a7cbbc.md#insn-00a7cbc8)

~~~diff
- 00a7bbd4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a7bbd4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a7bbd4 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00a7bbd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7bbd4 bytes 292000a9
- 00a7bbd8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a7bbd8 ["RETURN", null, ["register:0:8"]]
- 00a7bbd8 bytes c0035fd6
+ 00a7cbc8 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a7cbc8 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00a7cbc8 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00a7cbc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a7cbc8 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a93e0dc6f78bf174eaab14190068e939"></a>

### [`00a7be6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7b/00a7be6c.md) → [`00a7ce60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7c/00a7ce60.md) FUN_00a7ce60

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7be84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a7ce78"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7be8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a7be84",
      "DATA",
      [
        "storage",
        "00c8bb40",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a7be88",
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
      "00a7ce78",
      "DATA",
      [
        "storage",
        "00c8cb10",
        null,
        "undefined *"
      ]
    ],
    [
      "00a7ce7c",
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

- 旧版 [`00a7be84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7b/00a7be6c.md#insn-00a7be84) · [`00a7be8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7b/00a7be6c.md#insn-00a7be8c)
- 新版 [`00a7ce78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7c/00a7ce60.md#insn-00a7ce78)

~~~diff
- 00a7be84 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a7be84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a7be84 bytes 080000f9
- 00a7be8c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a7be8c ["RETURN", null, ["register:0:8"]]
- 00a7be8c bytes c0035fd6
+ 00a7ce78 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00a7ce78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00a7ce78 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92ce0f07c294886fc171a038d3963d45"></a>

### [`00a7be90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7b/00a7be90.md) → [`00a7ce84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7c/00a7ce84.md) FUN_00a7ce84

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7be98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a7ce8c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7be9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a7be98",
      "DATA",
      [
        "storage",
        "00c8bb40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7ce8c",
      "DATA",
      [
        "storage",
        "00c8cb10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7be98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7b/00a7be90.md#insn-00a7be98) · [`00a7be9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7b/00a7be90.md#insn-00a7be9c)
- 新版 [`00a7ce8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7c/00a7ce84.md#insn-00a7ce8c)

~~~diff
- 00a7be98 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00a7be98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a7be98 bytes 280000f9
- 00a7be9c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a7be9c ["RETURN", null, ["register:0:8"]]
- 00a7be9c bytes c0035fd6
+ 00a7ce8c ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00a7ce8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00a7ce8c bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-148bd22d996d21baa25cf64ff91dce43"></a>

### [`00a7c244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7c/00a7c244.md) → [`00a7d238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7d/00a7d238.md) FUN_00a7d238

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c268"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c268"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a7d25c"
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
      "unmatched:00a7c268",
      "DATA",
      [
        "storage",
        "00c8bcd0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a7c26c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7c270",
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
      "00a7d25c",
      "DATA",
      [
        "storage",
        "00c8cca0",
        null,
        "undefined *"
      ]
    ],
    [
      "00a7d260",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a7d264",
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

- 旧版 [`00a7c268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7c/00a7c244.md#insn-00a7c268) · [`00a7c258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7c/00a7c244.md#insn-00a7c258)
- 新版 [`00a7d25c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7d/00a7d238.md#insn-00a7d25c) · [`00a7d24c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7d/00a7d238.md#insn-00a7d24c)

~~~diff
- 00a7c268 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a7c268 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a7c268 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a7c268 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7c268 bytes 082400a9
+ 00a7d25c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a7d25c ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a7d25c ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00a7d25c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a7d25c bytes 082400a9
- 00a7c258 ["INT_ADD", "register:40f0:8", ["const:a7c258:8", "const:4:8"]]
- 00a7c258 ["CALL", null, ["callee:00c58f30:8"]]
+ 00a7d24c ["INT_ADD", "register:40f0:8", ["const:a7d24c:8", "const:4:8"]]
+ 00a7d24c ["CALL", null, ["callee:00c58f30:8"]]
- 00a7c258 bytes 426f0794
+ 00a7d24c bytes 396f0794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c1a9558054799df7044ac580ac9f1ee"></a>

### [`00a7c278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7c/00a7c278.md) → [`00a7d26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7d/00a7d26c.md) FUN_00a7d26c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c284"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c284"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a7d278"
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
      "unmatched:00a7c284",
      "DATA",
      [
        "storage",
        "00c8bcd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7d278",
      "DATA",
      [
        "storage",
        "00c8cca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7c284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7c/00a7c278.md#insn-00a7c284) · [`00a7c288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7c/00a7c278.md#insn-00a7c288)
- 新版 [`00a7d278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7d/00a7d26c.md#insn-00a7d278)

~~~diff
- 00a7c284 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a7c284 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a7c284 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00a7c284 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7c284 bytes 292000a9
- 00a7c288 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a7c288 ["RETURN", null, ["register:0:8"]]
- 00a7c288 bytes c0035fd6
+ 00a7d278 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a7d278 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00a7d278 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00a7d278 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a7d278 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f48bc37d1fabf6ee4cb2f7747fd1d4da"></a>

### [`00a7c38c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7c/00a7c38c.md) → [`00a7d380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7d/00a7d380.md) FUN_00a7d380

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 46.15% / 新版 46.15%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c38c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c38c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c390"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a7c38c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7c390",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7c3b0",
      "DATA",
      [
        "storage",
        "00c8bd50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7d380",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a7d384",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a7d3a4",
      "DATA",
      [
        "storage",
        "00c8cd20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7c38c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7c/00a7c38c.md#insn-00a7c38c) · [`00a7c390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7c/00a7c38c.md#insn-00a7c390) · [`00a7c3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7c/00a7c38c.md#insn-00a7c3b0)

~~~diff
- 00a7c38c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a7c38c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a7c38c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a7c38c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a7c38c bytes fd7bbea9
- 00a7c390 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a7c390 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00a7c390 bytes f30b00f9
- 00a7c3b0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a7c3b0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a7c3b0 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a7c3b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7c3b0 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-638b7883749b7b64148c7f837d21f6ad"></a>

### [`00a7c3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7c/00a7c3c0.md) → [`00a7d3b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7d/00a7d3b4.md) FUN_00a7d3b4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c3cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c3cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a7d3c0"
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
      "unmatched:00a7c3cc",
      "DATA",
      [
        "storage",
        "00c8bd50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7d3c0",
      "DATA",
      [
        "storage",
        "00c8cd20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7c3cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7c/00a7c3c0.md#insn-00a7c3cc) · [`00a7c3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7c/00a7c3c0.md#insn-00a7c3d0)
- 新版 [`00a7d3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7d/00a7d3b4.md#insn-00a7d3c0)

~~~diff
- 00a7c3cc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a7c3cc ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a7c3cc ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00a7c3cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7c3cc bytes 292000a9
- 00a7c3d0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a7c3d0 ["RETURN", null, ["register:0:8"]]
- 00a7c3d0 bytes c0035fd6
+ 00a7d3c0 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a7d3c0 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00a7d3c0 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00a7d3c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a7d3c0 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63f6cfbb115e21eca785a8df3096d84a"></a>

### [`00a7e8a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7e/00a7e8a4.md) → [`00a7f898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7f/00a7f898.md) FUN_00a7f898

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a79b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a79/00a79b04.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00a7aaf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7a/00a7aaf8.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 81.67% / 新版 80.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7e980"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7ea0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a7f974"
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
      "unmatched:00a7e980",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a7f984"
      ]
    ],
    [
      "unmatched:00a7ea0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a7fa28"
      ]
    ]
  ],
  "added": [
    [
      "00a7f974",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a7f984"
      ]
    ],
    [
      "00a7fa00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a7fa28"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7e980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7e/00a7e8a4.md#insn-00a7e980) · [`00a7ea0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7e/00a7e8a4.md#insn-00a7ea0c)
- 新版 [`00a7f974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7f/00a7f898.md#insn-00a7f974)

~~~diff
- 00a7e980 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a7e980 ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
- 00a7e980 bytes 8a000054
- 00a7ea0c ["INT_EQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
- 00a7ea0c ["CBRANCH", null, ["local:b40:8", "tmp:0:1"]]
- 00a7ea0c bytes 4b0100b4
+ 00a7f974 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00a7f974 ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
+ 00a7f974 bytes 8a000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d9ec3aaf6303dfcb00aec823518d072"></a>

### [`00a7ea94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7e/00a7ea94.md) → [`00a7fa88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7f/00a7fa88.md) FUN_00a7fa88

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7eaac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a7faa0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7eab4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a7eaac",
      "DATA",
      [
        "storage",
        "00c8c1f0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a7eab0",
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
      "00a7faa0",
      "DATA",
      [
        "storage",
        "00c8d1c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00a7faa4",
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

- 旧版 [`00a7eaac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7e/00a7ea94.md#insn-00a7eaac) · [`00a7eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7e/00a7ea94.md#insn-00a7eab4)
- 新版 [`00a7faa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7f/00a7fa88.md#insn-00a7faa0)

~~~diff
- 00a7eaac ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a7eaac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a7eaac bytes 080000f9
- 00a7eab4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a7eab4 ["RETURN", null, ["register:0:8"]]
- 00a7eab4 bytes c0035fd6
+ 00a7faa0 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00a7faa0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00a7faa0 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93fc801bffde1f7690a794d8f986b7a7"></a>

### [`00a7eb14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7e/00a7eb14.md) → [`00a7fb08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7f/00a7fb08.md) FUN_00a7fb08

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7eb2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a7fb20"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7eb34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a7eb2c",
      "DATA",
      [
        "storage",
        "00c8c270",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a7eb30",
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
      "00a7fb20",
      "DATA",
      [
        "storage",
        "00c8d240",
        null,
        "undefined *"
      ]
    ],
    [
      "00a7fb24",
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

- 旧版 [`00a7eb2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7e/00a7eb14.md#insn-00a7eb2c) · [`00a7eb34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7e/00a7eb14.md#insn-00a7eb34)
- 新版 [`00a7fb20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a7f/00a7fb08.md#insn-00a7fb20)

~~~diff
- 00a7eb2c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a7eb2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a7eb2c bytes 080000f9
- 00a7eb34 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a7eb34 ["RETURN", null, ["register:0:8"]]
- 00a7eb34 bytes c0035fd6
+ 00a7fb20 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00a7fb20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00a7fb20 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-484dc483a09eeb8808107836a9fe9b53"></a>

### [`00a806a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a80/00a806a4.md) → [`00a81698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a81/00a81698.md) FUN_00a81698

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00a72604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a72/00a72604.md) [`00a806a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a80/00a806a4.md) [`00a80984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a80/00a80984.md) · 呼出先 3件 [`00a806a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a80/00a806a4.md) [`00a80984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a80/00a80984.md) [`00a80c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a80/00a80c2c.md)
- 新版 呼出元 3件 [`00a735f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a73/00a735f8.md) [`00a81698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a81/00a81698.md) [`00a81978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a81/00a81978.md) · 呼出先 3件 [`00a81698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a81/00a81698.md) [`00a81978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a81/00a81978.md) [`00a81c20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a81/00a81c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.28% / 新版 97.28%

CFGの説明率　旧版 59.70% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a806c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a80874"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a816b4"
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
      "unmatched:00a806c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a816d0"
      ]
    ],
    [
      "unmatched:00a806c4",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a806c8",
      "READ",
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
      "00a816b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a816d0"
      ]
    ],
    [
      "00a816b8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a816bc",
      "READ",
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

- 旧版 [`00a806c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a80/00a806a4.md#insn-00a806c0) · [`00a80874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a80/00a806a4.md#insn-00a80874)
- 新版 [`00a816b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a81/00a81698.md#insn-00a816b4)

~~~diff
- 00a806c0 ["CBRANCH", null, ["local:b3:8", "register:102:1"]]
- 00a806c0 bytes e2000054
- 00a80874 ["CBRANCH", null, ["local:b1:8", "register:101:1"]]
- 00a80874 bytes 80f2ff54
+ 00a816b4 ["CBRANCH", null, ["local:b3:8", "register:102:1"]]
+ 00a816b4 bytes e2000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

