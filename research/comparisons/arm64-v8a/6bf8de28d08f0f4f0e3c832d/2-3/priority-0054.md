# v16.0.2 → v16.0.3 · 最優先の変更候補 (54)

[一覧の目次](README.md)

<a id="compare-0654315b9db036d2169d782b397bdc80"></a>

### [`008ddd08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dd/008ddd08.md) → [`008decb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008de/008decb4.md) FUN_008decb4

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 13件 [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043f478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f478.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0066d11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066d/0066d11c.md) [`008dd148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dd/008dd148.md)
- 新版 呼出元 1件 [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) · 呼出先 13件 [`0043ecac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043ecac.md) [`0043f798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043f/0043f798.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0066d4cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0066d/0066d4cc.md) [`008de0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008de/008de0f4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.66% / 新版 90.66%

CFGの説明率　旧版 30.00% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ddd3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ddd40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ddd88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ddd30",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:008ddd34",
      "READ",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:008ddd3c",
      "WRITE",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008decdc",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "008dece0",
      "READ",
      [
        "storage",
        "00ca5a28",
        null,
        "undefined8"
      ]
    ],
    [
      "008dece8",
      "WRITE",
      [
        "storage",
        "00ca5a28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ddd3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dd/008ddd08.md#insn-008ddd3c) · [`008ddd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dd/008ddd08.md#insn-008ddd40) · [`008ddd88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dd/008ddd08.md#insn-008ddd88)

~~~diff
- 008ddd3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 008ddd3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008ddd3c bytes 093505f9
- 008ddd40 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:a78:8"]]
- 008ddd40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 008ddd40 bytes 6a3f05f9
- 008ddd88 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:a78:8"]]
- 008ddd88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 008ddd88 bytes 743f05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6485a665ef71b530e407edd355b3815b"></a>

### [`008ddff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dd/008ddff4.md) → [`008defa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008de/008defa0.md) FUN_008defa0

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 24件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0047d1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d1fc.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md)
- 新版 呼出元 1件 [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) · 呼出先 25件 [`0044deb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044d/0044deb0.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0047d51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d51c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.19% / 新版 88.19%

CFGの説明率　旧版 57.97% / 新版 59.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 4件, `store_condition` 13件, `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008de0b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008dea28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008dea2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008df028",
      "READ",
      [
        "storage",
        "002c4198",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:008de0b4",
      "DATA",
      [
        "storage",
        "00332098",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "unmatched:008de0b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008df0a4"
      ]
    ]
  ],
  "added": [
    [
      "008df028",
      "READ",
      [
        "storage",
        "002c41e8",
        null,
        "undefined8"
      ]
    ],
    [
      "008df060",
      "DATA",
      [
        "storage",
        "00332098",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "008df064",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008df0a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008de0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dd/008ddff4.md#insn-008de0b4) · [`008de0b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dd/008ddff4.md#insn-008de0b8) · [`008de298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dd/008ddff4.md#insn-008de298)

~~~diff
- 008de0b4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:38:8"]]
- 008de0b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4070:4"]]
- 008de0b4 bytes ee3a00b9
- 008de0b8 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008de0b8 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 008de0b8 bytes 0a020054
- 008de298 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008de298 ["COPY", "tmp:1:4", ["register:4050:4"]]
- 008de298 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 008de298 ["COPY", "tmp:1:4", ["register:4058:4"]]
- 008de298 bytes 4ab18b1a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-143750f4f190383c46bcfdc05a4f316d"></a>

### [`008deaac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008de/008deaac.md) → [`008dfa58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008df/008dfa58.md) FUN_008dfa58

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00859bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859bb0.md) · 呼出先 25件 [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00468c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468c1c.md) [`00468ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468ca0.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md)
- 新版 呼出元 1件 [`0085ab5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085a/0085ab5c.md) · 呼出先 25件 [`00467ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467ec0.md) [`00468f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468f3c.md) [`00468fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468fc0.md) [`004692e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692e8.md) [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.26% / 新版 64.26%

CFGの説明率　旧版 27.35% / 新版 27.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 24件, `unresolved_branch_alignment` 18件, `unresolved_call_alignment` 20件, `unresolved_store_alignment` 14件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008df3e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008df3e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008df3f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008deaec",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "008dfaa4",
      "READ",
      [
        "storage",
        "00ca5030",
        null,
        "undefined8"
      ]
    ],
    [
      "008dfab8",
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
      "008dfa98",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ],
    [
      "008dfaa4",
      "READ",
      [
        "storage",
        "00ca5ff0",
        null,
        "undefined8"
      ]
    ],
    [
      "008dfab8",
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

- 旧版 [`008deb7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008de/008deaac.md#insn-008deb7c) · [`008dee10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008de/008deaac.md#insn-008dee10) · [`008df3e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008de/008deaac.md#insn-008df3e4)

~~~diff
- 008deb7c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008deb7c ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 008deb7c bytes 600000b4
- 008dee10 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 008dee10 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 008dee10 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 008dee10 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 008dee10 bytes e8030037
- 008df3e4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 008df3e4 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 008df3e4 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:8:8"]]
- 008df3e4 ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:1:8"]]
- 008df3e4 bytes 1f8d00f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-275e5679a9651902eb401a3e05777d1c"></a>

### [`008e0a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0a80.md) → [`008e1a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e1a2c.md) FUN_008e1a2c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008e0648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0648.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`008e15f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e15f4.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "008e1a38",
      "incomplete_value": false,
      "site": "008e1a3c",
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
      "definition_site": "008e0a8c",
      "incomplete_value": false,
      "site": "008e0a90",
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
      "008e1a38",
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
      "008e1a38",
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

- 旧版 [`008e0a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0a80.md#insn-008e0a90) · [`008e0a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0a80.md#insn-008e0a88) · [`008e0a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0a80.md#insn-008e0a8c)
- 新版 [`008e1a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e1a2c.md#insn-008e1a3c) · [`008e1a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e1a2c.md#insn-008e1a34) · [`008e1a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e1a2c.md#insn-008e1a38)

~~~diff
- 008e0a90 ["INT_ADD", "register:40f0:8", ["const:8e0a90:8", "const:4:8"]]
- 008e0a90 ["CALL", null, ["callee:0043bad8:8"]]
+ 008e1a3c ["INT_ADD", "register:40f0:8", ["const:8e1a3c:8", "const:4:8"]]
+ 008e1a3c ["CALL", null, ["callee:0043bad8:8"]]
- 008e0a90 bytes 4a6bed97
+ 008e1a3c bytes 2768ed97
- 008e0a88 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 008e1a34 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 008e0a88 bytes a0cefff0
+ 008e1a34 bytes a0cefff0
- 008e0a8c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 008e0a8c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008e0a8c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008e0a8c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e1a38 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 008e1a38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e1a38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e1a38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008e0a8c bytes 00303e91
+ 008e1a38 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c994ed41c8df2845146fb6bf280abe36"></a>

### [`008e0c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0c84.md) → [`008e1c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e1c30.md) FUN_008e1c30

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008ddd08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008dd/008ddd08.md) · 呼出先 13件 [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`006333b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00633/006333b4.md) [`00758228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00758/00758228.md) [`00863734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00863/00863734.md)
- 新版 呼出元 1件 [`008decb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008de/008decb4.md) · 呼出先 13件 [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`00633764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00633/00633764.md) [`007585d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00758/007585d8.md) [`008646e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00864/008646e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.69% / 新版 82.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 36件, `store_destination` 7件, `store_value` 27件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008e1c68",
      "incomplete_value": false,
      "site": "008e1c74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e0cbc",
      "incomplete_value": false,
      "site": "008e0cc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:190:8"
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
      "definition_site": "008e1cb0",
      "incomplete_value": true,
      "site": "008e1cb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:49d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e0d04",
      "incomplete_value": true,
      "site": "008e0d04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3ce:8"
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
      "definition_site": "008e1cc8",
      "incomplete_value": true,
      "site": "008e1cc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f91:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e0d1c",
      "incomplete_value": true,
      "site": "008e0d1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f47:8"
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
      "008e1c74",
      "DATA",
      [
        "storage",
        "00c85190",
        null,
        "pointer"
      ]
    ],
    [
      "008e1c80",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "008e1ca0",
      "READ",
      [
        "storage",
        "002b63ce",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008e1c74",
      "DATA",
      [
        "storage",
        "00c86160",
        null,
        "pointer"
      ]
    ],
    [
      "008e1c80",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ],
    [
      "008e1ca0",
      "READ",
      [
        "storage",
        "002b649d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e0cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0c84.md#insn-008e0cb4) · [`008e0cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0c84.md#insn-008e0cb8) · [`008e0cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0c84.md#insn-008e0cbc)
- 新版 [`008e1c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e1c30.md#insn-008e1c60) · [`008e1c64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e1c30.md#insn-008e1c64) · [`008e1c68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e1/008e1c30.md#insn-008e1c68)

~~~diff
- 008e0cb4 ["INT_ADD", "register:40f0:8", ["const:8e0cb4:8", "const:4:8"]]
- 008e0cb4 ["CALL", null, ["callee:007585d8:8"]]
+ 008e1c60 ["INT_ADD", "register:40f0:8", ["const:8e1c60:8", "const:4:8"]]
+ 008e1c60 ["CALL", null, ["callee:007585d8:8"]]
- 008e0cb4 bytes 5dddf997
+ 008e1c60 bytes 5edaf997
- 008e0cb8 ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008e1c64 ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008e0cb8 bytes 281d00b0
+ 008e1c64 bytes 281d00b0
- 008e0cbc ["COPY", "tmp:0:8", ["const:190:8"]]
- 008e0cbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e0cbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e0cbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e1c68 ["COPY", "tmp:0:8", ["const:160:8"]]
+ 008e1c68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e1c68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e1c68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e0cbc bytes 08410691
+ 008e1c68 bytes 08810591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2017f1a807bf27487368069a1b28639"></a>

### [`008e1968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e1/008e1968.md) → [`008e2914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e2/008e2914.md) FUN_008e2914

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00682364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682364.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00682714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00682/00682714.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008e292c",
      "incomplete_value": false,
      "site": "008e2930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e1980",
      "incomplete_value": false,
      "site": "008e1984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:400:8"
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
      "definition_site": "008e2968",
      "incomplete_value": false,
      "site": "008e296c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e19bc",
      "incomplete_value": false,
      "site": "008e19c0",
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
            "const:8e0:8"
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
      "008e2930",
      "DATA",
      [
        "storage",
        "00c78400",
        null,
        "pointer"
      ]
    ],
    [
      "008e296c",
      "DATA",
      [
        "storage",
        "00c748e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008e2930",
      "DATA",
      [
        "storage",
        "00c793d0",
        null,
        "pointer"
      ]
    ],
    [
      "008e296c",
      "DATA",
      [
        "storage",
        "00c758b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e197c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e1/008e1968.md#insn-008e197c) · [`008e1980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e1/008e1968.md#insn-008e1980) · [`008e1994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e1/008e1968.md#insn-008e1994)
- 新版 [`008e2928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e2/008e2914.md#insn-008e2928) · [`008e292c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e2/008e2914.md#insn-008e292c) · [`008e2940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e2/008e2914.md#insn-008e2940)

~~~diff
- 008e197c ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 008e2928 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 008e197c bytes a81c00f0
+ 008e2928 bytes a81c00f0
- 008e1980 ["COPY", "tmp:0:8", ["const:400:8"]]
- 008e1980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e1980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e1980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e292c ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 008e292c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e292c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e292c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e1980 bytes 08011091
+ 008e292c bytes 08410f91
- 008e1994 ["INT_ADD", "register:40f0:8", ["const:8e1994:8", "const:4:8"]]
- 008e1994 ["CALL", null, ["callee:00c54d90:8"]]
+ 008e2940 ["INT_ADD", "register:40f0:8", ["const:8e2940:8", "const:4:8"]]
+ 008e2940 ["CALL", null, ["callee:00c54d90:8"]]
- 008e1994 bytes 03c90d94
+ 008e2940 bytes 14c90d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7d61d35556203c518d0cce01953ce39"></a>

### [`008e1a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e1/008e1a08.md) → [`008e29b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e2/008e29b4.md) _INIT_173

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "008e29f0",
      "incomplete_value": true,
      "site": "008e2a0c",
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
      "definition_site": "008e1a44",
      "incomplete_value": true,
      "site": "008e1a60",
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
      "definition_site": "008e2a14",
      "incomplete_value": true,
      "site": "008e2a30",
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
      "definition_site": "008e1a68",
      "incomplete_value": true,
      "site": "008e1a84",
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
      "definition_site": "008e2a34",
      "incomplete_value": true,
      "site": "008e2a50",
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
      "definition_site": "008e1a88",
      "incomplete_value": true,
      "site": "008e1aa4",
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
      "008e29f0",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "008e2a14",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "008e2a34",
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
      "008e29f0",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "008e2a14",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "008e2a34",
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

- 旧版 [`008e1b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e1/008e1a08.md#insn-008e1b68) · [`008e1c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e1/008e1a08.md#insn-008e1c3c) · [`008e1a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e1/008e1a08.md#insn-008e1a30)
- 新版 [`008e2b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e2/008e29b4.md#insn-008e2b14) · [`008e2be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e2/008e29b4.md#insn-008e2be8) · [`008e29dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e2/008e29b4.md#insn-008e29dc)

~~~diff
- 008e1b68 ["INT_ADD", "register:40f0:8", ["const:8e1b68:8", "const:4:8"]]
- 008e1b68 ["CALL", null, ["callee:0043bb58:8"]]
+ 008e2b14 ["INT_ADD", "register:40f0:8", ["const:8e2b14:8", "const:4:8"]]
+ 008e2b14 ["CALL", null, ["callee:0043bb58:8"]]
- 008e1b68 bytes 3467ed97
+ 008e2b14 bytes 1164ed97
- 008e1c3c ["INT_ADD", "register:40f0:8", ["const:8e1c3c:8", "const:4:8"]]
- 008e1c3c ["CALL", null, ["callee:00c58ed0:8"]]
+ 008e2be8 ["INT_ADD", "register:40f0:8", ["const:8e2be8:8", "const:4:8"]]
+ 008e2be8 ["CALL", null, ["callee:00c58ed0:8"]]
- 008e1c3c bytes b1d80d94
+ 008e2be8 bytes bad80d94
- 008e1a30 ["COPY", "register:4098:8", ["const:1123000:8"]]
+ 008e29dc ["COPY", "register:4098:8", ["const:1124000:8"]]
- 008e1a30 bytes 134200d0
+ 008e29dc bytes 134200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd64fce3199c359cb0af68095a8fbed6"></a>

### [`008e1d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e1/008e1d98.md) → [`008e2d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e2/008e2d44.md) FUN_008e2d44

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008e5fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5fd0.md) · 呼出先 13件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)
- 新版 呼出元 1件 [`008e6f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e6/008e6f7c.md) · 呼出先 13件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`004889b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004889b8.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.55% / 新版 88.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008e2d90",
      "incomplete_value": false,
      "site": "008e2d98",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e1de4",
      "incomplete_value": false,
      "site": "008e1dec",
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
            "const:e08:8"
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
      "definition_site": "008e2dbc",
      "incomplete_value": true,
      "site": "008e2dcc",
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
                "const:375:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e1e10",
      "incomplete_value": true,
      "site": "008e1e20",
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
                "const:297:8"
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
      "definition_site": "008e2dd0",
      "incomplete_value": true,
      "site": "008e2dd0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008e1e24",
      "incomplete_value": true,
      "site": "008e1e24",
      "value": [
        "LOAD",
        "8",
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
      "008e2d98",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "008e2dbc",
      "READ",
      [
        "storage",
        "002b4297",
        null,
        "string"
      ]
    ],
    [
      "008e2dc0",
      "READ",
      [
        "storage",
        "002b42a6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008e2d98",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "008e2dbc",
      "READ",
      [
        "storage",
        "002b4375",
        null,
        "string"
      ]
    ],
    [
      "008e2dc0",
      "READ",
      [
        "storage",
        "002b4384",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e1dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e1/008e1d98.md#insn-008e1dd0) · [`008e1de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e1/008e1d98.md#insn-008e1de0) · [`008e1de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e1/008e1d98.md#insn-008e1de4)
- 新版 [`008e2d7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e2/008e2d44.md#insn-008e2d7c) · [`008e2d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e2/008e2d44.md#insn-008e2d8c) · [`008e2d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e2/008e2d44.md#insn-008e2d90)

~~~diff
- 008e1dd0 ["INT_ADD", "register:40f0:8", ["const:8e1dd0:8", "const:4:8"]]
- 008e1dd0 ["CALL", null, ["callee:00488180:8"]]
+ 008e2d7c ["INT_ADD", "register:40f0:8", ["const:8e2d7c:8", "const:4:8"]]
+ 008e2d7c ["CALL", null, ["callee:00488180:8"]]
- 008e1dd0 bytes 2498ee97
+ 008e2d7c bytes 0195ee97
- 008e1de0 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 008e2d8c ["COPY", "register:4040:8", ["const:c65000:8"]]
- 008e1de0 bytes 081c00f0
+ 008e2d8c bytes 081c00f0
- 008e1de4 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 008e1de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e1de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e1de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e2d90 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 008e2d90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e2d90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e2d90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e1de4 bytes 08213891
+ 008e2d90 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53799e6c77fcc444afafe24c30c54c9d"></a>

### [`008e2910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2910.md) → [`008e38bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e38bc.md) FUN_008e38bc

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008e5fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5fd0.md) · 呼出先 23件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048796c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md)
- 新版 呼出元 1件 [`008e6f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e6/008e6f7c.md) · 呼出先 23件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c8c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00487dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487dc4.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.70% / 新版 93.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008e3900",
      "incomplete_value": false,
      "site": "008e3908",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e2954",
      "incomplete_value": false,
      "site": "008e295c",
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
            "const:e08:8"
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
      "definition_site": "008e3920",
      "incomplete_value": true,
      "site": "008e392c",
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
                "const:832:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e2974",
      "incomplete_value": true,
      "site": "008e2980",
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
                "const:763:8"
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
      "definition_site": "008e3a4c",
      "incomplete_value": true,
      "site": "008e3a4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c9e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e2aa0",
      "incomplete_value": true,
      "site": "008e2aa0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008e3908",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "008e3920",
      "READ",
      [
        "storage",
        "002b8763",
        null,
        "string"
      ]
    ],
    [
      "008e3a3c",
      "READ",
      [
        "storage",
        "002abbd1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008e3908",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "008e3920",
      "READ",
      [
        "storage",
        "002b8832",
        null,
        "string"
      ]
    ],
    [
      "008e3a3c",
      "READ",
      [
        "storage",
        "002abc9e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e2948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2910.md#insn-008e2948) · [`008e2950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2910.md#insn-008e2950) · [`008e2954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2910.md#insn-008e2954)
- 新版 [`008e38f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e38bc.md#insn-008e38f4) · [`008e38fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e38bc.md#insn-008e38fc) · [`008e3900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e38bc.md#insn-008e3900)

~~~diff
- 008e2948 ["INT_ADD", "register:40f0:8", ["const:8e2948:8", "const:4:8"]]
- 008e2948 ["CALL", null, ["callee:00488180:8"]]
+ 008e38f4 ["INT_ADD", "register:40f0:8", ["const:8e38f4:8", "const:4:8"]]
+ 008e38f4 ["CALL", null, ["callee:00488180:8"]]
- 008e2948 bytes 4695ee97
+ 008e38f4 bytes 2392ee97
- 008e2950 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 008e38fc ["COPY", "register:4040:8", ["const:c65000:8"]]
- 008e2950 bytes 081c00d0
+ 008e38fc bytes 081c00d0
- 008e2954 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 008e2954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e2954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e2954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008e3900 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 008e3900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008e3900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008e3900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e2954 bytes 08213891
+ 008e3900 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dfefd244fa07c56baa40f2fd5592da3"></a>

### [`008e3400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3400.md) → [`008e43ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e43ac.md) FUN_008e43ac

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008e6700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e6/008e6700.md) · 呼出先 22件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f88.md) [`008b7044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7044.md)
- 新版 呼出元 1件 [`008e76ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e7/008e76ac.md) · 呼出先 22件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`005d8fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d8fb8.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f34.md) [`008b7ff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ff0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.25% / 新版 84.25%

CFGの説明率　旧版 73.33% / 新版 74.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e3550"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e3560"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e357c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008e3444",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:008e3448",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e4418"
      ]
    ],
    [
      "unmatched:008e3450",
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
      "008e43f0",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "008e43f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e4418"
      ]
    ],
    [
      "008e43fc",
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

- 旧版 [`008e3448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3400.md#insn-008e3448) · [`008e3550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3400.md#insn-008e3550) · [`008e3554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3400.md#insn-008e3554)

~~~diff
- 008e3448 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008e3448 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 008e3448 bytes 200100b4
- 008e3550 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 008e3550 ["COPY", "tmp:1:8", ["const:0:8"]]
- 008e3550 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 008e3550 bytes ff1300f9
- 008e3554 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 008e3554 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 008e3554 bytes f60000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-293f08f1113b30e549c3e06b5206d7d4"></a>

### [`008e3da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3da4.md) → [`008e4d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e4d50.md) FUN_008e4d50

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006b34d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b34d8.md) · 呼出先 21件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a290.md)
- 新版 呼出元 1件 [`006b3888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3888.md) · 呼出先 21件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`004682b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/004682b4.md) [`004692e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692e8.md) [`0046a5b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046a/0046a5b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.53% / 新版 99.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008e4d9c",
      "incomplete_value": true,
      "site": "008e4d9c",
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
      "definition_site": "008e3df0",
      "incomplete_value": true,
      "site": "008e3df0",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008e4da4",
      "incomplete_value": false,
      "site": "008e4db4",
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
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e3df8",
      "incomplete_value": false,
      "site": "008e3e08",
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
            "const:f28:8"
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
      "definition_site": "008e4dac",
      "incomplete_value": false,
      "site": "008e4db4",
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
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e3e00",
      "incomplete_value": false,
      "site": "008e3e08",
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
            "const:8e0:8"
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
      "008e4d98",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008e4da4",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008e4dac",
      "PARAM",
      [
        "storage",
        "00c738e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008e4d98",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "008e4da4",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008e4dac",
      "PARAM",
      [
        "storage",
        "00c748b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e3e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3da4.md#insn-008e3e08) · [`008e3de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3da4.md#insn-008e3de8) · [`008e3dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3da4.md#insn-008e3dec)
- 新版 [`008e4db4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e4d50.md#insn-008e4db4) · [`008e4d94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e4d50.md#insn-008e4d94) · [`008e4d98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e4d50.md#insn-008e4d98)

~~~diff
- 008e3e08 ["INT_ADD", "register:40f0:8", ["const:8e3e08:8", "const:4:8"]]
- 008e3e08 ["CALL", null, ["callee:00c596b0:8"]]
+ 008e4db4 ["INT_ADD", "register:40f0:8", ["const:8e4db4:8", "const:4:8"]]
+ 008e4db4 ["CALL", null, ["callee:00c596b0:8"]]
- 008e3e08 bytes 36d20d94
+ 008e4db4 bytes 3fd20d94
- 008e3de8 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 008e4d94 ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 008e3de8 bytes 081e00b0
+ 008e4d94 bytes 081e00b0
- 008e3dec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 008e3dec ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008e4d98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a38:8"]]
+ 008e4d98 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008e3dec bytes 003d45f9
+ 008e4d98 bytes 001d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ba3e80eeebff35195528b458b79e163"></a>

### [`008e484c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e484c.md) → [`008e57f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e57f8.md) FUN_008e57f8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006b2a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b2a00.md) · 呼出先 11件 [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00597e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597e48.md) [`00597e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597e88.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`006b2db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b2/006b2db0.md) · 呼出先 11件 [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`00598168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598168.md) [`005981a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/005981a8.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

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
      "site": "008e588c",
      "value": [
        "leaf",
        "ram:a85cac:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008e48e0",
      "value": [
        "leaf",
        "ram:a84cb8:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008e58c4",
      "value": [
        "leaf",
        "ram:a85ccc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008e4918",
      "value": [
        "leaf",
        "ram:a84cd8:8"
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
      "008e588c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84cb8"
      ]
    ],
    [
      "008e58c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84cd8"
      ]
    ]
  ],
  "added": [
    [
      "008e588c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a85cac"
      ]
    ],
    [
      "008e58c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a85ccc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e48e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e484c.md#insn-008e48e0) · [`008e4918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e484c.md#insn-008e4918) · [`008e4874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e484c.md#insn-008e4874)
- 新版 [`008e588c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e57f8.md#insn-008e588c) · [`008e58c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e57f8.md#insn-008e58c4) · [`008e5820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e57f8.md#insn-008e5820)

~~~diff
- 008e48e0 ["INT_ADD", "register:40f0:8", ["const:8e48e0:8", "const:4:8"]]
- 008e48e0 ["CALL", null, ["ram:a84cb8:8"]]
+ 008e588c ["INT_ADD", "register:40f0:8", ["const:8e588c:8", "const:4:8"]]
+ 008e588c ["CALL", null, ["ram:a85cac:8"]]
- 008e48e0 bytes f6800694
+ 008e588c bytes 08810694
- 008e4918 ["INT_ADD", "register:40f0:8", ["const:8e4918:8", "const:4:8"]]
- 008e4918 ["CALL", null, ["ram:a84cd8:8"]]
+ 008e58c4 ["INT_ADD", "register:40f0:8", ["const:8e58c4:8", "const:4:8"]]
+ 008e58c4 ["CALL", null, ["ram:a85ccc:8"]]
- 008e4918 bytes f0800694
+ 008e58c4 bytes 02810694
- 008e4874 ["INT_ADD", "register:40f0:8", ["const:8e4874:8", "const:4:8"]]
- 008e4874 ["CALL", null, ["callee:008524fc:8"]]
+ 008e5820 ["INT_ADD", "register:40f0:8", ["const:8e5820:8", "const:4:8"]]
+ 008e5820 ["CALL", null, ["callee:008524fc:8"]]
- 008e4874 bytes 37b3fd97
+ 008e5820 bytes 37b3fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92631c0e35aa0313ee7d15ae5c1297db"></a>

### [`008e49f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e49f4.md) → [`008e59a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e59a0.md) FUN_008e59a0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008e9ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9ce0.md) · 呼出先 26件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)
- 新版 呼出元 1件 [`008eac8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eac8c.md) · 呼出先 26件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.62% / 新版 94.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e5b28",
      "incomplete_value": true,
      "site": "008e5b3c",
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
                "const:b8f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e4b7c",
      "incomplete_value": true,
      "site": "008e4b90",
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
                "const:ab8:8"
              ]
            ]
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
      "definition_site": "008e5b40",
      "incomplete_value": true,
      "site": "008e5b40",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008e4b94",
      "incomplete_value": true,
      "site": "008e4b94",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008e5f8c",
      "incomplete_value": false,
      "site": "008e5f8c",
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
                "const:fc0:8"
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
      "definition_site": "008e4fe0",
      "incomplete_value": false,
      "site": "008e4fe0",
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
                "const:0:8"
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
    "ordinal": 53,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008e5b14",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "008e5b28",
      "READ",
      [
        "storage",
        "002aeab8",
        null,
        "string"
      ]
    ],
    [
      "008e5b2c",
      "READ",
      [
        "storage",
        "002aeac5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008e5b14",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ],
    [
      "008e5b28",
      "READ",
      [
        "storage",
        "002aeb8f",
        null,
        "string"
      ]
    ],
    [
      "008e5b2c",
      "READ",
      [
        "storage",
        "002aeb9c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e4bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e49f4.md#insn-008e4bdc) · [`008e4fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e49f4.md#insn-008e4fbc) · [`008e4ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e49f4.md#insn-008e4ff8)
- 新版 [`008e5b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e59a0.md#insn-008e5b88) · [`008e5f68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e59a0.md#insn-008e5f68) · [`008e5fa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e59a0.md#insn-008e5fa4)

~~~diff
- 008e4bdc ["INT_ADD", "register:40f0:8", ["const:8e4bdc:8", "const:4:8"]]
- 008e4bdc ["CALL", null, ["callee:0047e96c:8"]]
+ 008e5b88 ["INT_ADD", "register:40f0:8", ["const:8e5b88:8", "const:4:8"]]
+ 008e5b88 ["CALL", null, ["callee:0047e96c:8"]]
- 008e4bdc bytes 9c66ee97
+ 008e5b88 bytes 7963ee97
- 008e4fbc ["INT_ADD", "register:40f0:8", ["const:8e4fbc:8", "const:4:8"]]
- 008e4fbc ["CALL", null, ["callee:00c58ef0:8"]]
+ 008e5f68 ["INT_ADD", "register:40f0:8", ["const:8e5f68:8", "const:4:8"]]
+ 008e5f68 ["CALL", null, ["callee:00c58ef0:8"]]
- 008e4fbc bytes d9cb0d94
+ 008e5f68 bytes e2cb0d94
- 008e4ff8 ["INT_ADD", "register:40f0:8", ["const:8e4ff8:8", "const:4:8"]]
- 008e4ff8 ["CALL", null, ["callee:00c58ed0:8"]]
+ 008e5fa4 ["INT_ADD", "register:40f0:8", ["const:8e5fa4:8", "const:4:8"]]
+ 008e5fa4 ["CALL", null, ["callee:00c58ed0:8"]]
- 008e4ff8 bytes c2cb0d94
+ 008e5fa4 bytes cbcb0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a8e81d5d745871fa63254801fae785f"></a>

### [`008e5238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5238.md) → [`008e61e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e6/008e61e4.md) FUN_008e61e4

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008ea310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea310.md) · 呼出先 20件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`006df59c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006df59c.md)
- 新版 呼出元 1件 [`008eb2bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb2bc.md) · 呼出先 20件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`006df94c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006df/006df94c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 69.23% / 新版 69.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件, `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e6254",
      "incomplete_value": true,
      "site": "008e6264",
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
                "const:2f9000:8"
              ],
              [
                "leaf",
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e52a8",
      "incomplete_value": true,
      "site": "008e52b8",
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
                "const:2f9000:8"
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e6254",
      "incomplete_value": true,
      "site": "008e6264",
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
      "definition_site": "008e52a8",
      "incomplete_value": true,
      "site": "008e52b8",
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e54c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008e6254",
      "READ",
      [
        "storage",
        "002f9ad0",
        null,
        null
      ]
    ],
    [
      "008e6254",
      "READ",
      [
        "storage",
        "002f9ae0",
        null,
        null
      ]
    ],
    [
      "unmatched:008e53c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e6444"
      ]
    ]
  ],
  "added": [
    [
      "008e6254",
      "READ",
      [
        "storage",
        "002f9b10",
        null,
        null
      ]
    ],
    [
      "008e6254",
      "READ",
      [
        "storage",
        "002f9b20",
        null,
        null
      ]
    ],
    [
      "008e6370",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e6444"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e53c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5238.md#insn-008e53c4) · [`008e53d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5238.md#insn-008e53d8) · [`008e54c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5238.md#insn-008e54c8)

~~~diff
- 008e53c4 ["CBRANCH", null, ["local:b31:8", "register:101:1"]]
- 008e53c4 bytes a0060054
- 008e53d8 ["CBRANCH", null, ["local:b31:8", "register:101:1"]]
- 008e53d8 bytes 00060054
- 008e54c8 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 008e54c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008e54c8 bytes 2003803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb290d307ecadfbea1f8deab0e9f5d01"></a>

### [`008e5fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5fd0.md) → [`008e6f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e6/008e6f7c.md) FUN_008e6f7c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006b2a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b2a00.md) · 呼出先 24件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00447734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447734.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md)
- 新版 呼出元 1件 [`006b2db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b2/006b2db0.md) · 呼出先 24件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00447a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00447/00447a54.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046ecd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ecd0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.96% / 新版 80.96%

CFGの説明率　旧版 51.26% / 新版 52.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_condition` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e6078"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e607c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e6080"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008e601c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e6fe8"
      ]
    ],
    [
      "unmatched:008e6058",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:008e605c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e759c"
      ]
    ]
  ],
  "added": [
    [
      "008e6fc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e6fe8"
      ]
    ],
    [
      "008e7004",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ],
    [
      "008e7008",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e759c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e6078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5fd0.md#insn-008e6078) · [`008e607c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5fd0.md#insn-008e607c) · [`008e6080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e5/008e5fd0.md#insn-008e6080)

~~~diff
- 008e6078 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 008e6078 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:58:8"]]
- 008e6078 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 008e6078 bytes e8630139
- 008e607c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 008e607c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:59:8"]]
- 008e607c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008e607c bytes ea9305f8
- 008e6080 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008e6080 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:5f:8"]]
- 008e6080 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008e6080 bytes e9f305f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb86cf8b024a8d901860fad5ce6f5292"></a>

### [`008e6700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e6/008e6700.md) → [`008e76ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e7/008e76ac.md) FUN_008e76ac

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006b2bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b2bb4.md) · 呼出先 42件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0044e9c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e9c8.md) [`0044fcfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fcfc.md) [`0046d9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d9b4.md)
- 新版 呼出元 1件 [`006b2f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b2/006b2f64.md) · 呼出先 42件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0044ece8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044e/0044ece8.md) [`0045001c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00450/0045001c.md) [`0046dcd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046dcd4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.76% / 新版 94.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 10件, `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008e77a4",
      "incomplete_value": true,
      "site": "008e77a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2ed:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e67f8",
      "incomplete_value": true,
      "site": "008e67f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:20f:8"
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
      "definition_site": "008e7848",
      "incomplete_value": true,
      "site": "008e7848",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b9e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e689c",
      "incomplete_value": true,
      "site": "008e689c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ac0:8"
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
      "definition_site": "008e7860",
      "incomplete_value": false,
      "site": "008e7860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e68b4",
      "incomplete_value": false,
      "site": "008e68b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "008e7724",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ],
    [
      "008e773c",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "qword"
      ]
    ],
    [
      "008e7754",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "008e7724",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ],
    [
      "008e773c",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "dword"
      ]
    ],
    [
      "008e7754",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e67cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e6/008e6700.md#insn-008e67cc) · [`008e68f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e6/008e6700.md#insn-008e68f8) · [`008e6954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e6/008e6700.md#insn-008e6954)
- 新版 [`008e7778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e7/008e76ac.md#insn-008e7778) · [`008e78a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e7/008e76ac.md#insn-008e78a4) · [`008e7900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e7/008e76ac.md#insn-008e7900)

~~~diff
- 008e67cc ["INT_ADD", "register:40f0:8", ["const:8e67cc:8", "const:4:8"]]
- 008e67cc ["CALL", null, ["ram:48cd38:8"]]
+ 008e7778 ["INT_ADD", "register:40f0:8", ["const:8e7778:8", "const:4:8"]]
+ 008e7778 ["CALL", null, ["ram:48d058:8"]]
- 008e67cc bytes 5b99ee97
+ 008e7778 bytes 3896ee97
- 008e68f8 ["INT_ADD", "register:40f0:8", ["const:8e68f8:8", "const:4:8"]]
- 008e68f8 ["CALL", null, ["ram:48cd38:8"]]
+ 008e78a4 ["INT_ADD", "register:40f0:8", ["const:8e78a4:8", "const:4:8"]]
+ 008e78a4 ["CALL", null, ["ram:48d058:8"]]
- 008e68f8 bytes 1099ee97
+ 008e78a4 bytes ed95ee97
- 008e6954 ["INT_ADD", "register:40f0:8", ["const:8e6954:8", "const:4:8"]]
- 008e6954 ["CALL", null, ["ram:47ad34:8"]]
+ 008e7900 ["INT_ADD", "register:40f0:8", ["const:8e7900:8", "const:4:8"]]
+ 008e7900 ["CALL", null, ["ram:47b054:8"]]
- 008e6954 bytes f850ee97
+ 008e7900 bytes d54dee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1be289565e3de16ced624a929052e8ab"></a>

### [`008e7424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e7/008e7424.md) → [`008e83d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e8/008e83d0.md) FUN_008e83d0

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006b34d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b34d8.md) · 呼出先 15件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00468f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468f8c.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046af4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046af4c.md)
- 新版 呼出元 1件 [`006b3888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3888.md) · 呼出先 15件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467ec0.md) [`004692ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692ac.md) [`004692e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692e8.md) [`0046b26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046b/0046b26c.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 81.52% / 新版 81.52%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 15件, `call_target` 2件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 13件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008e8414",
      "incomplete_value": true,
      "site": "008e8414",
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
      "definition_site": "008e7468",
      "incomplete_value": true,
      "site": "008e7468",
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
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008e77a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008e7848"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008e8410",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008e841c",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008e8424",
      "PARAM",
      [
        "storage",
        "00c738e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008e8410",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "008e841c",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008e8424",
      "PARAM",
      [
        "storage",
        "00c748b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e7480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e7/008e7424.md#insn-008e7480) · [`008e7660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e7/008e7424.md#insn-008e7660) · [`008e76f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e7/008e7424.md#insn-008e76f0)
- 新版 [`008e842c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e8/008e83d0.md#insn-008e842c) · [`008e860c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e8/008e83d0.md#insn-008e860c) · [`008e869c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e8/008e83d0.md#insn-008e869c)

~~~diff
- 008e7480 ["INT_ADD", "register:40f0:8", ["const:8e7480:8", "const:4:8"]]
- 008e7480 ["CALL", null, ["callee:00c596b0:8"]]
+ 008e842c ["INT_ADD", "register:40f0:8", ["const:8e842c:8", "const:4:8"]]
+ 008e842c ["CALL", null, ["callee:00c596b0:8"]]
- 008e7480 bytes 98c40d94
+ 008e842c bytes a1c40d94
- 008e7660 ["INT_ADD", "register:40f0:8", ["const:8e7660:8", "const:4:8"]]
- 008e7660 ["CALL", null, ["ram:46e7fc:8"]]
+ 008e860c ["INT_ADD", "register:40f0:8", ["const:8e860c:8", "const:4:8"]]
+ 008e860c ["CALL", null, ["ram:46eb1c:8"]]
- 008e7660 bytes 671cee97
+ 008e860c bytes 4419ee97
- 008e76f0 ["INT_ADD", "register:40f0:8", ["const:8e76f0:8", "const:4:8"]]
- 008e76f0 ["CALL", null, ["ram:46e7fc:8"]]
+ 008e869c ["INT_ADD", "register:40f0:8", ["const:8e869c:8", "const:4:8"]]
+ 008e869c ["CALL", null, ["ram:46eb1c:8"]]
- 008e76f0 bytes 431cee97
+ 008e869c bytes 2019ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-253ba9329e17f89dc2c674ea918421be"></a>

### [`008e7abc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e7/008e7abc.md) → [`008e8a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e8/008e8a68.md) FUN_008e8a68

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006b34d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b34d8.md) · 呼出先 15件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046a928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a928.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md)
- 新版 呼出元 1件 [`006b3888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3888.md) · 呼出先 15件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md) [`0046ac48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046a/0046ac48.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.95% / 新版 74.95%

CFGの説明率　旧版 42.86% / 新版 43.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 23件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 15件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e7c4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e7de4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e7dec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008e7bf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e9260"
      ]
    ],
    [
      "unmatched:008e7cf8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e8cc0"
      ]
    ],
    [
      "unmatched:008e7d00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e925c"
      ]
    ]
  ],
  "added": [
    [
      "008e8ba0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e9260"
      ]
    ],
    [
      "008e8ca4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e8cc0"
      ]
    ],
    [
      "008e8cac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008e925c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e7bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e7/008e7abc.md#insn-008e7bf4) · [`008e7c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e7/008e7abc.md#insn-008e7c4c) · [`008e7cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e7/008e7abc.md#insn-008e7cf8)

~~~diff
- 008e7bf4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 008e7bf4 ["CBRANCH", null, ["local:b106:8", "tmp:0:1"]]
- 008e7bf4 bytes 0a3600b5
- 008e7c4c ["COPY", "tmp:0:4", ["const:0:4"]]
- 008e7c4c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 008e7c4c ["COPY", "tmp:2:8", ["register:40b8:8"]]
- 008e7c4c ["INT_ADD", "register:40b8:8", ["register:40b8:8", "const:4:8"]]
- 008e7c4c bytes ff4600b8
- 008e7cf8 ["INT_EQUAL", "tmp:0:1", ["register:40d0:8", "const:0:8"]]
- 008e7cf8 ["CBRANCH", null, ["local:b35:8", "tmp:0:1"]]
- 008e7cf8 bytes fa0000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b82de2eeacd076ebe36d25fdbb8b0d8e"></a>

### [`008e82b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e82b8.md) → [`008e9264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9264.md) FUN_008e9264

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`008e3148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3148.md) [`008e49f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e49f4.md) [`008e86a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e86a4.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 3件 [`008e40f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e40f4.md) [`008e59a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e59a0.md) [`008e9650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9650.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "008e9270",
      "incomplete_value": false,
      "site": "008e9274",
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
      "definition_site": "008e82c4",
      "incomplete_value": false,
      "site": "008e82c8",
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
      "008e9270",
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
      "008e9270",
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

- 旧版 [`008e82c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e82b8.md#insn-008e82c8) · [`008e82c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e82b8.md#insn-008e82c0) · [`008e82c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e82b8.md#insn-008e82c4)
- 新版 [`008e9274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9264.md#insn-008e9274) · [`008e926c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9264.md#insn-008e926c) · [`008e9270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9264.md#insn-008e9270)

~~~diff
- 008e82c8 ["INT_ADD", "register:40f0:8", ["const:8e82c8:8", "const:4:8"]]
- 008e82c8 ["CALL", null, ["callee:0043bad8:8"]]
+ 008e9274 ["INT_ADD", "register:40f0:8", ["const:8e9274:8", "const:4:8"]]
+ 008e9274 ["CALL", null, ["callee:0043bad8:8"]]
- 008e82c8 bytes 3c4ded97
+ 008e9274 bytes 194aed97
- 008e82c0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 008e926c ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 008e82c0 bytes 60cefff0
+ 008e926c bytes 60cefff0
- 008e82c4 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 008e82c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008e82c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008e82c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e9270 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 008e9270 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e9270 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e9270 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008e82c4 bytes 00303e91
+ 008e9270 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd7449c47dbfa1f11ba5fead4d9c2559"></a>

### [`008e85a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e85a0.md) → [`008e954c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e954c.md) FUN_008e954c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008e83bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e83bc.md) [`008e8e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8e94.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`008e9368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9368.md) [`008e9e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9e40.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "008e9558",
      "incomplete_value": false,
      "site": "008e955c",
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
      "definition_site": "008e85ac",
      "incomplete_value": false,
      "site": "008e85b0",
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
      "008e9558",
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
      "008e9558",
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

- 旧版 [`008e85b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e85a0.md#insn-008e85b0) · [`008e85a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e85a0.md#insn-008e85a8) · [`008e85ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e85a0.md#insn-008e85ac)
- 新版 [`008e955c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e954c.md#insn-008e955c) · [`008e9554`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e954c.md#insn-008e9554) · [`008e9558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e954c.md#insn-008e9558)

~~~diff
- 008e85b0 ["INT_ADD", "register:40f0:8", ["const:8e85b0:8", "const:4:8"]]
- 008e85b0 ["CALL", null, ["callee:0043bad8:8"]]
+ 008e955c ["INT_ADD", "register:40f0:8", ["const:8e955c:8", "const:4:8"]]
+ 008e955c ["CALL", null, ["callee:0043bad8:8"]]
- 008e85b0 bytes 824ced97
+ 008e955c bytes 5f49ed97
- 008e85a8 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 008e9554 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 008e85a8 bytes 60cefff0
+ 008e9554 bytes 60cefff0
- 008e85ac ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 008e85ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008e85ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008e85ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e9558 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 008e9558 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e9558 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e9558 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008e85ac bytes 00303e91
+ 008e9558 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4708260c2f4cd2413de8287fc8f120fd"></a>

### [`008e8690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8690.md) → [`008e963c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e963c.md) FUN_008e963c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008e45e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45e4.md) [`008e8d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8d0c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`008e5590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e5590.md) [`008e9cb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9cb8.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "008e9648",
      "incomplete_value": false,
      "site": "008e964c",
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
      "definition_site": "008e869c",
      "incomplete_value": false,
      "site": "008e86a0",
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
      "008e9648",
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
      "008e9648",
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

- 旧版 [`008e86a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8690.md#insn-008e86a0) · [`008e8698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8690.md#insn-008e8698) · [`008e869c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8690.md#insn-008e869c)
- 新版 [`008e964c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e963c.md#insn-008e964c) · [`008e9644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e963c.md#insn-008e9644) · [`008e9648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e963c.md#insn-008e9648)

~~~diff
- 008e86a0 ["INT_ADD", "register:40f0:8", ["const:8e86a0:8", "const:4:8"]]
- 008e86a0 ["CALL", null, ["callee:0043bad8:8"]]
+ 008e964c ["INT_ADD", "register:40f0:8", ["const:8e964c:8", "const:4:8"]]
+ 008e964c ["CALL", null, ["callee:0043bad8:8"]]
- 008e86a0 bytes 464ced97
+ 008e964c bytes 2349ed97
- 008e8698 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 008e9644 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 008e8698 bytes 60cefff0
+ 008e9644 bytes 60cefff0
- 008e869c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 008e869c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008e869c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008e869c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e9648 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 008e9648 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e9648 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e9648 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008e869c bytes 00303e91
+ 008e9648 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2cc62abfc03fe1fee0aa7b7780de63a"></a>

### [`008e8860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8860.md) → [`008e980c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e980c.md) FUN_008e980c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008e2910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2910.md) [`008e45e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e4/008e45e4.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`008e38bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e38bc.md) [`008e5590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e5/008e5590.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "008e9818",
      "incomplete_value": false,
      "site": "008e981c",
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
      "definition_site": "008e886c",
      "incomplete_value": false,
      "site": "008e8870",
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
      "008e9818",
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
      "008e9818",
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

- 旧版 [`008e8870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8860.md#insn-008e8870) · [`008e8868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8860.md#insn-008e8868) · [`008e886c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8860.md#insn-008e886c)
- 新版 [`008e981c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e980c.md#insn-008e981c) · [`008e9814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e980c.md#insn-008e9814) · [`008e9818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e980c.md#insn-008e9818)

~~~diff
- 008e8870 ["INT_ADD", "register:40f0:8", ["const:8e8870:8", "const:4:8"]]
- 008e8870 ["CALL", null, ["callee:0043bad8:8"]]
+ 008e981c ["INT_ADD", "register:40f0:8", ["const:8e981c:8", "const:4:8"]]
+ 008e981c ["CALL", null, ["callee:0043bad8:8"]]
- 008e8870 bytes d24bed97
+ 008e981c bytes af48ed97
- 008e8868 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 008e9814 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 008e8868 bytes 60cefff0
+ 008e9814 bytes 60cefff0
- 008e886c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 008e886c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008e886c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008e886c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e9818 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 008e9818 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e9818 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e9818 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008e886c bytes 00303e91
+ 008e9818 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-595e6e9ac79d2064e7e1d4e37ff0145b"></a>

### [`008e8a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8a58.md) → [`008e9a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9a04.md) FUN_008e9a04

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`008e8874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8874.md) [`008e8fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8fdc.md) [`008ea5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea5ec.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 3件 [`008e9820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9820.md) [`008e9f88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9f88.md) [`008eb598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb598.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "008e9a10",
      "incomplete_value": false,
      "site": "008e9a14",
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
      "definition_site": "008e8a64",
      "incomplete_value": false,
      "site": "008e8a68",
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
      "008e9a10",
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
      "008e9a10",
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

- 旧版 [`008e8a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8a58.md#insn-008e8a68) · [`008e8a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8a58.md#insn-008e8a60) · [`008e8a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8a58.md#insn-008e8a64)
- 新版 [`008e9a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9a04.md#insn-008e9a14) · [`008e9a0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9a04.md#insn-008e9a0c) · [`008e9a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9a04.md#insn-008e9a10)

~~~diff
- 008e8a68 ["INT_ADD", "register:40f0:8", ["const:8e8a68:8", "const:4:8"]]
- 008e8a68 ["CALL", null, ["callee:0043bad8:8"]]
+ 008e9a14 ["INT_ADD", "register:40f0:8", ["const:8e9a14:8", "const:4:8"]]
+ 008e9a14 ["CALL", null, ["callee:0043bad8:8"]]
- 008e8a68 bytes 544bed97
+ 008e9a14 bytes 3148ed97
- 008e8a60 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 008e9a0c ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 008e8a60 bytes 60cefff0
+ 008e9a0c bytes 60cefff0
- 008e8a64 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 008e8a64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008e8a64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008e8a64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e9a10 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 008e9a10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e9a10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e9a10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008e8a64 bytes 00303e91
+ 008e9a10 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11f6099d81050a661cd87af9ed7ecfba"></a>

### [`008e8ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8ca4.md) → [`008e9c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9c50.md) FUN_008e9c50

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`008e8ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8ac0.md) [`008e918c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e918c.md) [`008ea3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea3f0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 3件 [`008e9a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9a6c.md) [`008ea138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea138.md) [`008eb39c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb39c.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "008e9c5c",
      "incomplete_value": false,
      "site": "008e9c60",
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
      "definition_site": "008e8cb0",
      "incomplete_value": false,
      "site": "008e8cb4",
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
      "008e9c5c",
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
      "008e9c5c",
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

- 旧版 [`008e8cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8ca4.md#insn-008e8cb4) · [`008e8cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8ca4.md#insn-008e8cac) · [`008e8cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8ca4.md#insn-008e8cb0)
- 新版 [`008e9c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9c50.md#insn-008e9c60) · [`008e9c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9c50.md#insn-008e9c58) · [`008e9c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9c50.md#insn-008e9c5c)

~~~diff
- 008e8cb4 ["INT_ADD", "register:40f0:8", ["const:8e8cb4:8", "const:4:8"]]
- 008e8cb4 ["CALL", null, ["callee:0043bad8:8"]]
+ 008e9c60 ["INT_ADD", "register:40f0:8", ["const:8e9c60:8", "const:4:8"]]
+ 008e9c60 ["CALL", null, ["callee:0043bad8:8"]]
- 008e8cb4 bytes c14aed97
+ 008e9c60 bytes 9e47ed97
- 008e8cac ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 008e9c58 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 008e8cac bytes 60cefff0
+ 008e9c58 bytes 60cefff0
- 008e8cb0 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 008e8cb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008e8cb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008e8cb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008e9c5c ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 008e9c5c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008e9c5c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008e9c5c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008e8cb0 bytes 00303e91
+ 008e9c5c bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-323ff2bbfc59ac8b8bf8e6097b42360d"></a>

### [`008e8fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8fdc.md) → [`008e9f88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9f88.md) FUN_008e9f88

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008e2910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2910.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`008e8a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8a58.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008e38bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e38bc.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`008e9a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9a04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.78% / 新版 98.78%

CFGの説明率　旧版 75.00% / 新版 69.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008e90d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008ea07c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "008e9118",
      "incomplete_value": true,
      "site": "008e911c",
      "value": [
        "live",
        "register:4098:8"
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
      "unmatched:008e90d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ea094"
      ]
    ]
  ],
  "added": [
    [
      "008ea07c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ea094"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e90d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8fdc.md#insn-008e90d0) · [`008e911c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8fdc.md#insn-008e911c)
- 新版 [`008ea0c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9f88.md#insn-008ea0c8) · [`008ea07c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9f88.md#insn-008ea07c)

~~~diff
- 008e90d0 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 008e90d0 bytes c0000054
- 008e911c ["INT_ADD", "register:40f0:8", ["const:8e911c:8", "const:4:8"]]
- 008e911c ["CALL", null, ["callee:008e9a04:8"]]
+ 008ea0c8 ["INT_ADD", "register:40f0:8", ["const:8ea0c8:8", "const:4:8"]]
+ 008ea0c8 ["CALL", null, ["callee:008e9a04:8"]]
- 008e911c bytes 4ffeff97
+ 008ea0c8 bytes 4ffeff97
+ 008ea07c ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
+ 008ea07c bytes c0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fe4ae5357435ef930dcea5d81169975"></a>

### [`008e918c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e918c.md) → [`008ea138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea138.md) FUN_008ea138

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008e2910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e2/008e2910.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`008e8ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e8/008e8ca4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008e38bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e3/008e38bc.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`008e9c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e9/008e9c50.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 91.46% / 新版 91.46%

CFGの説明率　旧版 60.71% / 新版 60.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008e91b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008e91d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008e91e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008e91b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ea274"
      ]
    ]
  ],
  "added": [
    [
      "008ea164",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ea274"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e91b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e918c.md#insn-008e91b8) · [`008e91d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e918c.md#insn-008e91d4) · [`008e91e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e918c.md#insn-008e91e0)

~~~diff
- 008e91b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 008e91b8 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 008e91b8 bytes 8a0800b5
- 008e91d4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008e91d4 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 008e91d4 ["COPY", "tmp:2:8", ["register:4050:8"]]
- 008e91d4 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 008e91d4 bytes 4881889a
- 008e91e0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 008e91e0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 008e91e0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 008e91e0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008e91e0 bytes 1631899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7326a533f51bd9ff2ca50a9d77c0464e"></a>

### [`008e9340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9340.md) → [`008ea2ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea2ec.md) FUN_008ea2ec

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
      "definition_site": "008ea310",
      "incomplete_value": false,
      "site": "008ea310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9364",
      "incomplete_value": false,
      "site": "008e9364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
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
      "008ea310",
      "DATA",
      [
        "storage",
        "00c851b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea310",
      "DATA",
      [
        "storage",
        "00c86180",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9340.md#insn-008e9354) · [`008e935c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9340.md#insn-008e935c) · [`008e9360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9340.md#insn-008e9360)
- 新版 [`008ea300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea2ec.md#insn-008ea300) · [`008ea308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea2ec.md#insn-008ea308) · [`008ea30c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea2ec.md#insn-008ea30c)

~~~diff
- 008e9354 ["INT_ADD", "register:40f0:8", ["const:8e9354:8", "const:4:8"]]
- 008e9354 ["CALL", null, ["callee:00c58f30:8"]]
+ 008ea300 ["INT_ADD", "register:40f0:8", ["const:8ea300:8", "const:4:8"]]
+ 008ea300 ["CALL", null, ["callee:00c58f30:8"]]
- 008e9354 bytes 03bb0d94
+ 008ea300 bytes 0cbb0d94
- 008e935c ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008ea308 ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008e935c bytes e81c0090
+ 008ea308 bytes e81c0090
- 008e9360 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 008e9360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e9360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e9360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ea30c ["COPY", "tmp:0:8", ["const:180:8"]]
+ 008ea30c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea30c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea30c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e9360 bytes 08c10691
+ 008ea30c bytes 08010691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac77aadabd23b355882156acdc136781"></a>

### [`008e9374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9374.md) → [`008ea320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea320.md) FUN_008ea320

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
      "definition_site": "008ea32c",
      "incomplete_value": false,
      "site": "008ea32c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9380",
      "incomplete_value": false,
      "site": "008e9380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
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
      "008ea32c",
      "DATA",
      [
        "storage",
        "00c851b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea32c",
      "DATA",
      [
        "storage",
        "00c86180",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9374.md#insn-008e9378) · [`008e937c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9374.md#insn-008e937c)
- 新版 [`008ea324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea320.md#insn-008ea324) · [`008ea328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea320.md#insn-008ea328)

~~~diff
- 008e9378 ["COPY", "register:4048:8", ["const:c85000:8"]]
+ 008ea324 ["COPY", "register:4048:8", ["const:c86000:8"]]
- 008e9378 bytes e91c0090
+ 008ea324 bytes e91c0090
- 008e937c ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 008e937c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008e937c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008e937c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ea328 ["COPY", "tmp:0:8", ["const:180:8"]]
+ 008ea328 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea328 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea328 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008e937c bytes 29c10691
+ 008ea328 bytes 29010691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2733e4d2a2cd3fb535fd198e0ee7e1e"></a>

### [`008e9390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9390.md) → [`008ea33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea33c.md) FUN_008ea33c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md) [`008e3ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e3/008e3ce0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ea8.md) [`008e4c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008e4/008e4c8c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e9390"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e9390"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e9394"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008e9390",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:008e9394",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008e9398",
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
      "008ea33c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "008ea340",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008ea344",
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

- 旧版 [`008e9390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9390.md#insn-008e9390) · [`008e9394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9390.md#insn-008e9394) · [`008e9398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9390.md#insn-008e9398)

~~~diff
- 008e9390 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008e9390 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008e9390 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 008e9390 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008e9390 bytes fd7bbda9
- 008e9394 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008e9394 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 008e9394 bytes f50b00f9
- 008e9398 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008e9398 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008e9398 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008e9398 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008e9398 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c428a0a9c64878aaefa5a0531673798d"></a>

### [`008e94c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e94c0.md) → [`008ea46c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea46c.md) FUN_008ea46c

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
      "definition_site": "008ea490",
      "incomplete_value": false,
      "site": "008ea490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:200:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e94e4",
      "incomplete_value": false,
      "site": "008e94e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "008ea490",
      "DATA",
      [
        "storage",
        "00c85230",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea490",
      "DATA",
      [
        "storage",
        "00c86200",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e94d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e94c0.md#insn-008e94d4) · [`008e94dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e94c0.md#insn-008e94dc) · [`008e94e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e94c0.md#insn-008e94e0)
- 新版 [`008ea480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea46c.md#insn-008ea480) · [`008ea488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea46c.md#insn-008ea488) · [`008ea48c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea46c.md#insn-008ea48c)

~~~diff
- 008e94d4 ["INT_ADD", "register:40f0:8", ["const:8e94d4:8", "const:4:8"]]
- 008e94d4 ["CALL", null, ["callee:00c58f30:8"]]
+ 008ea480 ["INT_ADD", "register:40f0:8", ["const:8ea480:8", "const:4:8"]]
+ 008ea480 ["CALL", null, ["callee:00c58f30:8"]]
- 008e94d4 bytes a3ba0d94
+ 008ea480 bytes acba0d94
- 008e94dc ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008ea488 ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008e94dc bytes e81c0090
+ 008ea488 bytes e81c0090
- 008e94e0 ["COPY", "tmp:0:8", ["const:230:8"]]
- 008e94e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e94e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e94e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ea48c ["COPY", "tmp:0:8", ["const:200:8"]]
+ 008ea48c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea48c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea48c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e94e0 bytes 08c10891
+ 008ea48c bytes 08010891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d183341fc172d161a0bb2e80a00cc9b"></a>

### [`008e94f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e94f4.md) → [`008ea4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea4a0.md) FUN_008ea4a0

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
      "definition_site": "008ea4ac",
      "incomplete_value": false,
      "site": "008ea4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:200:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9500",
      "incomplete_value": false,
      "site": "008e9500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      "008ea4ac",
      "DATA",
      [
        "storage",
        "00c85230",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea4ac",
      "DATA",
      [
        "storage",
        "00c86200",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e94f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e94f4.md#insn-008e94f8) · [`008e94fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e94f4.md#insn-008e94fc)
- 新版 [`008ea4a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea4a0.md#insn-008ea4a4) · [`008ea4a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea4a0.md#insn-008ea4a8)

~~~diff
- 008e94f8 ["COPY", "register:4048:8", ["const:c85000:8"]]
+ 008ea4a4 ["COPY", "register:4048:8", ["const:c86000:8"]]
- 008e94f8 bytes e91c0090
+ 008ea4a4 bytes e91c0090
- 008e94fc ["COPY", "tmp:0:8", ["const:230:8"]]
- 008e94fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008e94fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008e94fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ea4a8 ["COPY", "tmp:0:8", ["const:200:8"]]
+ 008ea4a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea4a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ea4a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008e94fc bytes 29c10891
+ 008ea4a8 bytes 29010891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adbd623d17e859a671f5e4d8e67a9eed"></a>

### [`008e9510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9510.md) → [`008ea4bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea4bc.md) FUN_008ea4bc

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b7a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a68.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b8a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b8a14.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "008ea4dc",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008e9530",
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
      "site": "008ea4e8",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008e953c",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "008ea4dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008ea4e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008ea50c",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "008ea4dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "008ea4e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "008ea50c",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9510.md#insn-008e9530) · [`008e953c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9510.md#insn-008e953c) · [`008e9550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9510.md#insn-008e9550)
- 新版 [`008ea4dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea4bc.md#insn-008ea4dc) · [`008ea4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea4bc.md#insn-008ea4e8) · [`008ea4fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea4bc.md#insn-008ea4fc)

~~~diff
- 008e9530 ["INT_ADD", "register:40f0:8", ["const:8e9530:8", "const:4:8"]]
- 008e9530 ["CALL", null, ["ram:47ad34:8"]]
+ 008ea4dc ["INT_ADD", "register:40f0:8", ["const:8ea4dc:8", "const:4:8"]]
+ 008ea4dc ["CALL", null, ["ram:47b054:8"]]
- 008e9530 bytes 0146ee97
+ 008ea4dc bytes de42ee97
- 008e953c ["INT_ADD", "register:40f0:8", ["const:8e953c:8", "const:4:8"]]
- 008e953c ["CALL", null, ["ram:47ad34:8"]]
+ 008ea4e8 ["INT_ADD", "register:40f0:8", ["const:8ea4e8:8", "const:4:8"]]
+ 008ea4e8 ["CALL", null, ["ram:47b054:8"]]
- 008e953c bytes fe45ee97
+ 008ea4e8 bytes db42ee97
- 008e9550 ["INT_ADD", "register:40f0:8", ["const:8e9550:8", "const:4:8"]]
- 008e9550 ["CALL", null, ["callee:008524fc:8"]]
+ 008ea4fc ["INT_ADD", "register:40f0:8", ["const:8ea4fc:8", "const:4:8"]]
+ 008ea4fc ["CALL", null, ["callee:008524fc:8"]]
- 008e9550 bytes 00a0fd97
+ 008ea4fc bytes 00a0fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e788b8fb56ccb9d9f451dce07f3363c1"></a>

### [`008e95bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e95bc.md) → [`008ea568`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea568.md) FUN_008ea568

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008ea588",
      "incomplete_value": false,
      "site": "008ea58c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e95dc",
      "incomplete_value": false,
      "site": "008e95e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
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
      "008ea58c",
      "DATA",
      [
        "storage",
        "00c852b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea58c",
      "DATA",
      [
        "storage",
        "00c86280",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e95d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e95bc.md#insn-008e95d0) · [`008e95d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e95bc.md#insn-008e95d8) · [`008e95dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e95bc.md#insn-008e95dc)
- 新版 [`008ea57c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea568.md#insn-008ea57c) · [`008ea584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea568.md#insn-008ea584) · [`008ea588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea568.md#insn-008ea588)

~~~diff
- 008e95d0 ["INT_ADD", "register:40f0:8", ["const:8e95d0:8", "const:4:8"]]
- 008e95d0 ["CALL", null, ["callee:00c58f30:8"]]
+ 008ea57c ["INT_ADD", "register:40f0:8", ["const:8ea57c:8", "const:4:8"]]
+ 008ea57c ["CALL", null, ["callee:00c58f30:8"]]
- 008e95d0 bytes 64ba0d94
+ 008ea57c bytes 6dba0d94
- 008e95d8 ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008ea584 ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008e95d8 bytes e81c0090
+ 008ea584 bytes e81c0090
- 008e95dc ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 008e95dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e95dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e95dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ea588 ["COPY", "tmp:0:8", ["const:280:8"]]
+ 008ea588 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea588 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea588 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e95dc bytes 08c10a91
+ 008ea588 bytes 08010a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87f6a1748b93a76dd3260f3c0af255e3"></a>

### [`008e95f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e95f4.md) → [`008ea5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea5a0.md) FUN_008ea5a0

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
      "definition_site": "008ea5a4",
      "incomplete_value": false,
      "site": "008ea5a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e95f8",
      "incomplete_value": false,
      "site": "008e95fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
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
      "008ea5a8",
      "DATA",
      [
        "storage",
        "00c852b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ea5a8",
      "DATA",
      [
        "storage",
        "00c86280",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e95f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e95f4.md#insn-008e95f4) · [`008e95f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e95f4.md#insn-008e95f8)
- 新版 [`008ea5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea5a0.md#insn-008ea5a0) · [`008ea5a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea5a0.md#insn-008ea5a4)

~~~diff
- 008e95f4 ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008ea5a0 ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008e95f4 bytes e81c0090
+ 008ea5a0 bytes e81c0090
- 008e95f8 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 008e95f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e95f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e95f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ea5a4 ["COPY", "tmp:0:8", ["const:280:8"]]
+ 008ea5a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea5a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ea5a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e95f8 bytes 08c10a91
+ 008ea5a4 bytes 08010a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdaaeb42dce1d0b7ee7f3137375622ee"></a>

### [`008e9614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9614.md) → [`008ea5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea5c0.md) FUN_008ea5c0

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 17件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.07% / 新版 92.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008ea6f0",
      "incomplete_value": true,
      "site": "008ea6f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:857:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9744",
      "incomplete_value": true,
      "site": "008e9744",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:788:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "008ea714",
      "incomplete_value": false,
      "site": "008ea714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9768",
      "incomplete_value": false,
      "site": "008e9768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
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
      "definition_site": "008ea774",
      "incomplete_value": true,
      "site": "008ea774",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:666:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e97c8",
      "incomplete_value": true,
      "site": "008e97c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:59b:8"
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
      "008ea5fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008ea618",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008ea68c",
      "DATA",
      [
        "storage",
        "004362dc",
        "fde_004362dc",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "008ea5fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "008ea618",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "008ea68c",
      "DATA",
      [
        "storage",
        "004362dc",
        null,
        "byte[51]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9614.md#insn-008e9650) · [`008e966c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9614.md#insn-008e966c) · [`008e96a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9614.md#insn-008e96a8)
- 新版 [`008ea5fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea5c0.md#insn-008ea5fc) · [`008ea618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea5c0.md#insn-008ea618) · [`008ea654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ea5c0.md#insn-008ea654)

~~~diff
- 008e9650 ["INT_ADD", "register:40f0:8", ["const:8e9650:8", "const:4:8"]]
- 008e9650 ["CALL", null, ["ram:47ad34:8"]]
+ 008ea5fc ["INT_ADD", "register:40f0:8", ["const:8ea5fc:8", "const:4:8"]]
+ 008ea5fc ["CALL", null, ["ram:47b054:8"]]
- 008e9650 bytes b945ee97
+ 008ea5fc bytes 9642ee97
- 008e966c ["INT_ADD", "register:40f0:8", ["const:8e966c:8", "const:4:8"]]
- 008e966c ["CALL", null, ["ram:47ad34:8"]]
+ 008ea618 ["INT_ADD", "register:40f0:8", ["const:8ea618:8", "const:4:8"]]
+ 008ea618 ["CALL", null, ["ram:47b054:8"]]
- 008e966c bytes b245ee97
+ 008ea618 bytes 8f42ee97
- 008e96a8 ["INT_ADD", "register:40f0:8", ["const:8e96a8:8", "const:4:8"]]
- 008e96a8 ["CALL", null, ["callee:008524fc:8"]]
+ 008ea654 ["INT_ADD", "register:40f0:8", ["const:8ea654:8", "const:4:8"]]
+ 008ea654 ["CALL", null, ["callee:008524fc:8"]]
- 008e96a8 bytes aa9ffd97
+ 008ea654 bytes aa9ffd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d69fdc66594d40179e5a3d21957cdcd"></a>

### [`008e9b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9b00.md) → [`008eaaac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eaaac.md) FUN_008eaaac

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008eaacc",
      "incomplete_value": false,
      "site": "008eaad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9b20",
      "incomplete_value": false,
      "site": "008e9b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:320:8"
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
      "008eaad0",
      "DATA",
      [
        "storage",
        "00c85320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eaad0",
      "DATA",
      [
        "storage",
        "00c862f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9b00.md#insn-008e9b14) · [`008e9b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9b00.md#insn-008e9b1c) · [`008e9b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9b00.md#insn-008e9b20)
- 新版 [`008eaac0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eaaac.md#insn-008eaac0) · [`008eaac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eaaac.md#insn-008eaac8) · [`008eaacc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eaaac.md#insn-008eaacc)

~~~diff
- 008e9b14 ["INT_ADD", "register:40f0:8", ["const:8e9b14:8", "const:4:8"]]
- 008e9b14 ["CALL", null, ["callee:00c58f30:8"]]
+ 008eaac0 ["INT_ADD", "register:40f0:8", ["const:8eaac0:8", "const:4:8"]]
+ 008eaac0 ["CALL", null, ["callee:00c58f30:8"]]
- 008e9b14 bytes 13b90d94
+ 008eaac0 bytes 1cb90d94
- 008e9b1c ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008eaac8 ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008e9b1c bytes e81c0090
+ 008eaac8 bytes e81c0090
- 008e9b20 ["COPY", "tmp:0:8", ["const:320:8"]]
- 008e9b20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e9b20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e9b20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008eaacc ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 008eaacc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008eaacc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008eaacc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e9b20 bytes 08810c91
+ 008eaacc bytes 08c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60c9dae1a5072b4f798eb74783016c90"></a>

### [`008e9b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9b38.md) → [`008eaae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eaae4.md) FUN_008eaae4

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
      "definition_site": "008eaae8",
      "incomplete_value": false,
      "site": "008eaaec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9b3c",
      "incomplete_value": false,
      "site": "008e9b40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:320:8"
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
      "008eaaec",
      "DATA",
      [
        "storage",
        "00c85320",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eaaec",
      "DATA",
      [
        "storage",
        "00c862f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9b38.md#insn-008e9b38) · [`008e9b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9b38.md#insn-008e9b3c)
- 新版 [`008eaae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eaae4.md#insn-008eaae4) · [`008eaae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eaae4.md#insn-008eaae8)

~~~diff
- 008e9b38 ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008eaae4 ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008e9b38 bytes e81c0090
+ 008eaae4 bytes e81c0090
- 008e9b3c ["COPY", "tmp:0:8", ["const:320:8"]]
- 008e9b3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e9b3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e9b3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008eaae8 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 008eaae8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008eaae8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008eaae8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e9b3c bytes 08810c91
+ 008eaae8 bytes 08c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e49831a0d778b4d9bcd5cb3fc39b93f4"></a>

### [`008e9b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9b58.md) → [`008eab04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eab04.md) FUN_008eab04

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "008eab2c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008e9b80",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "008eab2c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "008eab2c",
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

- 旧版 [`008e9b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9b58.md#insn-008e9b80) · [`008e9b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9b58.md#insn-008e9b7c)
- 新版 [`008eab2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eab04.md#insn-008eab2c) · [`008eab28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eab04.md#insn-008eab28)

~~~diff
- 008e9b80 ["INT_ADD", "register:40f0:8", ["const:8e9b80:8", "const:4:8"]]
- 008e9b80 ["CALL", null, ["ram:47ad34:8"]]
+ 008eab2c ["INT_ADD", "register:40f0:8", ["const:8eab2c:8", "const:4:8"]]
+ 008eab2c ["CALL", null, ["ram:47b054:8"]]
- 008e9b80 bytes 6d44ee97
+ 008eab2c bytes 4a41ee97
- 008e9b7c ["INT_ADD", "register:40f0:8", ["const:8e9b7c:8", "const:4:8"]]
- 008e9b7c ["CALL", null, ["callee:008ba17c:8"]]
+ 008eab28 ["INT_ADD", "register:40f0:8", ["const:8eab28:8", "const:4:8"]]
+ 008eab28 ["CALL", null, ["callee:008ba17c:8"]]
- 008e9b7c bytes 953dff97
+ 008eab28 bytes 953dff97
~~~


<a id="compare-2974db5dbd39b68207921216bdfa11bf"></a>

### [`008e9bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9bc4.md) → [`008eab70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eab70.md) FUN_008eab70

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008eab90",
      "incomplete_value": false,
      "site": "008eab94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9be4",
      "incomplete_value": false,
      "site": "008e9be8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
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
      "008eab94",
      "DATA",
      [
        "storage",
        "00c853a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eab94",
      "DATA",
      [
        "storage",
        "00c86370",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9bc4.md#insn-008e9bd8) · [`008e9be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9bc4.md#insn-008e9be0) · [`008e9be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9bc4.md#insn-008e9be4)
- 新版 [`008eab84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eab70.md#insn-008eab84) · [`008eab8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eab70.md#insn-008eab8c) · [`008eab90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eab70.md#insn-008eab90)

~~~diff
- 008e9bd8 ["INT_ADD", "register:40f0:8", ["const:8e9bd8:8", "const:4:8"]]
- 008e9bd8 ["CALL", null, ["callee:00c58f30:8"]]
+ 008eab84 ["INT_ADD", "register:40f0:8", ["const:8eab84:8", "const:4:8"]]
+ 008eab84 ["CALL", null, ["callee:00c58f30:8"]]
- 008e9bd8 bytes e2b80d94
+ 008eab84 bytes ebb80d94
- 008e9be0 ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008eab8c ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008e9be0 bytes e81c0090
+ 008eab8c bytes e81c0090
- 008e9be4 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 008e9be4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e9be4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e9be4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008eab90 ["COPY", "tmp:0:8", ["const:370:8"]]
+ 008eab90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008eab90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008eab90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e9be4 bytes 08810e91
+ 008eab90 bytes 08c10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16f41e75d55911968e921d5c62f7b2ef"></a>

### [`008e9bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9bfc.md) → [`008eaba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eaba8.md) FUN_008eaba8

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
      "definition_site": "008eabac",
      "incomplete_value": false,
      "site": "008eabb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9c00",
      "incomplete_value": false,
      "site": "008e9c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
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
      "008eabb0",
      "DATA",
      [
        "storage",
        "00c853a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eabb0",
      "DATA",
      [
        "storage",
        "00c86370",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9bfc.md#insn-008e9bfc) · [`008e9c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9bfc.md#insn-008e9c00)
- 新版 [`008eaba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eaba8.md#insn-008eaba8) · [`008eabac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eaba8.md#insn-008eabac)

~~~diff
- 008e9bfc ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008eaba8 ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008e9bfc bytes e81c0090
+ 008eaba8 bytes e81c0090
- 008e9c00 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 008e9c00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e9c00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e9c00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008eabac ["COPY", "tmp:0:8", ["const:370:8"]]
+ 008eabac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008eabac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008eabac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e9c00 bytes 08810e91
+ 008eabac bytes 08c10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82dc0de3cac754783114979cdb62b505"></a>

### [`008e9c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9c1c.md) → [`008eabc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eabc8.md) FUN_008eabc8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "008eabf0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008e9c44",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "008eabf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "008eabf0",
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

- 旧版 [`008e9c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9c1c.md#insn-008e9c44) · [`008e9c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9c1c.md#insn-008e9c40)
- 新版 [`008eabf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eabc8.md#insn-008eabf0) · [`008eabec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eabc8.md#insn-008eabec)

~~~diff
- 008e9c44 ["INT_ADD", "register:40f0:8", ["const:8e9c44:8", "const:4:8"]]
- 008e9c44 ["CALL", null, ["ram:47ad34:8"]]
+ 008eabf0 ["INT_ADD", "register:40f0:8", ["const:8eabf0:8", "const:4:8"]]
+ 008eabf0 ["CALL", null, ["ram:47b054:8"]]
- 008e9c44 bytes 3c44ee97
+ 008eabf0 bytes 1941ee97
- 008e9c40 ["INT_ADD", "register:40f0:8", ["const:8e9c40:8", "const:4:8"]]
- 008e9c40 ["CALL", null, ["callee:008ba17c:8"]]
+ 008eabec ["INT_ADD", "register:40f0:8", ["const:8eabec:8", "const:4:8"]]
+ 008eabec ["CALL", null, ["callee:008ba17c:8"]]
- 008e9c40 bytes 643dff97
+ 008eabec bytes 643dff97
~~~


<a id="compare-436e53de1d6a4864dc363a7414c5d99d"></a>

### [`008e9c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9c88.md) → [`008eac34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eac34.md) FUN_008eac34

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008eac54",
      "incomplete_value": false,
      "site": "008eac58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9ca8",
      "incomplete_value": false,
      "site": "008e9cac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
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
      "008eac58",
      "DATA",
      [
        "storage",
        "00c85420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eac58",
      "DATA",
      [
        "storage",
        "00c863f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9c88.md#insn-008e9c9c) · [`008e9ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9c88.md#insn-008e9ca4) · [`008e9ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9c88.md#insn-008e9ca8)
- 新版 [`008eac48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eac34.md#insn-008eac48) · [`008eac50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eac34.md#insn-008eac50) · [`008eac54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eac34.md#insn-008eac54)

~~~diff
- 008e9c9c ["INT_ADD", "register:40f0:8", ["const:8e9c9c:8", "const:4:8"]]
- 008e9c9c ["CALL", null, ["callee:00c58f30:8"]]
+ 008eac48 ["INT_ADD", "register:40f0:8", ["const:8eac48:8", "const:4:8"]]
+ 008eac48 ["CALL", null, ["callee:00c58f30:8"]]
- 008e9c9c bytes b1b80d94
+ 008eac48 bytes bab80d94
- 008e9ca4 ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008eac50 ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008e9ca4 bytes e81c0090
+ 008eac50 bytes e81c0090
- 008e9ca8 ["COPY", "tmp:0:8", ["const:420:8"]]
- 008e9ca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e9ca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e9ca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008eac54 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 008eac54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008eac54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008eac54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e9ca8 bytes 08811091
+ 008eac54 bytes 08c10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4aa525973b99bd6d20bdc99ff6caadf"></a>

### [`008e9cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9cc0.md) → [`008eac6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eac6c.md) FUN_008eac6c

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
      "definition_site": "008eac70",
      "incomplete_value": false,
      "site": "008eac74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9cc4",
      "incomplete_value": false,
      "site": "008e9cc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
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
      "008eac74",
      "DATA",
      [
        "storage",
        "00c85420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eac74",
      "DATA",
      [
        "storage",
        "00c863f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9cc0.md#insn-008e9cc0) · [`008e9cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9cc0.md#insn-008e9cc4)
- 新版 [`008eac6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eac6c.md#insn-008eac6c) · [`008eac70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eac6c.md#insn-008eac70)

~~~diff
- 008e9cc0 ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008eac6c ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008e9cc0 bytes e81c0090
+ 008eac6c bytes e81c0090
- 008e9cc4 ["COPY", "tmp:0:8", ["const:420:8"]]
- 008e9cc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e9cc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e9cc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008eac70 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 008eac70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008eac70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008eac70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e9cc4 bytes 08811091
+ 008eac70 bytes 08c10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d5c7278aba0d82c5449abfa4048c76a"></a>

### [`008e9dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9dac.md) → [`008ead58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ead58.md) FUN_008ead58

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
      "definition_site": "008ead7c",
      "incomplete_value": false,
      "site": "008ead7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9dd0",
      "incomplete_value": false,
      "site": "008e9dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
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
      "008ead7c",
      "DATA",
      [
        "storage",
        "00c854b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ead7c",
      "DATA",
      [
        "storage",
        "00c86480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9dac.md#insn-008e9dc0) · [`008e9dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9dac.md#insn-008e9dc8) · [`008e9dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9dac.md#insn-008e9dcc)
- 新版 [`008ead6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ead58.md#insn-008ead6c) · [`008ead74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ead58.md#insn-008ead74) · [`008ead78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ead58.md#insn-008ead78)

~~~diff
- 008e9dc0 ["INT_ADD", "register:40f0:8", ["const:8e9dc0:8", "const:4:8"]]
- 008e9dc0 ["CALL", null, ["callee:00c58f30:8"]]
+ 008ead6c ["INT_ADD", "register:40f0:8", ["const:8ead6c:8", "const:4:8"]]
+ 008ead6c ["CALL", null, ["callee:00c58f30:8"]]
- 008e9dc0 bytes 68b80d94
+ 008ead6c bytes 71b80d94
- 008e9dc8 ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008ead74 ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008e9dc8 bytes e81c0090
+ 008ead74 bytes e81c0090
- 008e9dcc ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 008e9dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008e9dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008e9dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ead78 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 008ead78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ead78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ead78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008e9dcc bytes 08c11291
+ 008ead78 bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92afe24f461d03a39c4da11734a464e4"></a>

### [`008e9de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9de0.md) → [`008ead8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ead8c.md) FUN_008ead8c

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
      "definition_site": "008ead98",
      "incomplete_value": false,
      "site": "008ead98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9dec",
      "incomplete_value": false,
      "site": "008e9dec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
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
      "008ead98",
      "DATA",
      [
        "storage",
        "00c854b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ead98",
      "DATA",
      [
        "storage",
        "00c86480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9de0.md#insn-008e9de4) · [`008e9de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9de0.md#insn-008e9de8)
- 新版 [`008ead90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ead8c.md#insn-008ead90) · [`008ead94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008ead8c.md#insn-008ead94)

~~~diff
- 008e9de4 ["COPY", "register:4048:8", ["const:c85000:8"]]
+ 008ead90 ["COPY", "register:4048:8", ["const:c86000:8"]]
- 008e9de4 bytes e91c0090
+ 008ead90 bytes e91c0090
- 008e9de8 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 008e9de8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008e9de8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008e9de8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ead94 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 008ead94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ead94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ead94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008e9de8 bytes 29c11291
+ 008ead94 bytes 29011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adffd9629556802a7bb7355c02ccc3a9"></a>

### [`008e9dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9dfc.md) → [`008eada8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eada8.md) FUN_008eada8

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b98b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b98b0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008ba85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba85c.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.57% / 新版 84.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008eae84",
      "incomplete_value": true,
      "site": "008eae84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9df:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9ed8",
      "incomplete_value": true,
      "site": "008e9ed8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:901:8"
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
      "definition_site": "008eae88",
      "incomplete_value": true,
      "site": "008eae88",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008e9edc",
      "incomplete_value": true,
      "site": "008e9edc",
      "value": [
        "LOAD",
        "8",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008eaea0",
      "incomplete_value": false,
      "site": "008eaea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008e9ef4",
      "incomplete_value": false,
      "site": "008e9ef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
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
      "008eade0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008eadfc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008eae44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008e9f2c"
      ]
    ]
  ],
  "added": [
    [
      "008eade0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "008eadfc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "008eae44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008eaed8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e9e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9dfc.md#insn-008e9e34) · [`008e9e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9dfc.md#insn-008e9e50) · [`008e9e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e9/008e9dfc.md#insn-008e9e84)
- 新版 [`008eade0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eada8.md#insn-008eade0) · [`008eadfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eada8.md#insn-008eadfc) · [`008eae30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ea/008eada8.md#insn-008eae30)

~~~diff
- 008e9e34 ["INT_ADD", "register:40f0:8", ["const:8e9e34:8", "const:4:8"]]
- 008e9e34 ["CALL", null, ["ram:47ad34:8"]]
+ 008eade0 ["INT_ADD", "register:40f0:8", ["const:8eade0:8", "const:4:8"]]
+ 008eade0 ["CALL", null, ["ram:47b054:8"]]
- 008e9e34 bytes c043ee97
+ 008eade0 bytes 9d40ee97
- 008e9e50 ["INT_ADD", "register:40f0:8", ["const:8e9e50:8", "const:4:8"]]
- 008e9e50 ["CALL", null, ["ram:47ad34:8"]]
+ 008eadfc ["INT_ADD", "register:40f0:8", ["const:8eadfc:8", "const:4:8"]]
+ 008eadfc ["CALL", null, ["ram:47b054:8"]]
- 008e9e50 bytes b943ee97
+ 008eadfc bytes 9640ee97
- 008e9e84 ["INT_ADD", "register:40f0:8", ["const:8e9e84:8", "const:4:8"]]
- 008e9e84 ["CALL", null, ["callee:008524fc:8"]]
+ 008eae30 ["INT_ADD", "register:40f0:8", ["const:8eae30:8", "const:4:8"]]
+ 008eae30 ["CALL", null, ["callee:008524fc:8"]]
- 008e9e84 bytes b39dfd97
+ 008eae30 bytes b39dfd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-861650af15bf94330f9e1fe8c81bc15f"></a>

### [`008ea148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea148.md) → [`008eb0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb0f4.md) FUN_008eb0f4

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
      "definition_site": "008eb118",
      "incomplete_value": false,
      "site": "008eb118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea16c",
      "incomplete_value": false,
      "site": "008ea16c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:520:8"
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
      "008eb118",
      "DATA",
      [
        "storage",
        "00c85520",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eb118",
      "DATA",
      [
        "storage",
        "00c864f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea148.md#insn-008ea15c) · [`008ea164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea148.md#insn-008ea164) · [`008ea168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea148.md#insn-008ea168)
- 新版 [`008eb108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb0f4.md#insn-008eb108) · [`008eb110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb0f4.md#insn-008eb110) · [`008eb114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb0f4.md#insn-008eb114)

~~~diff
- 008ea15c ["INT_ADD", "register:40f0:8", ["const:8ea15c:8", "const:4:8"]]
- 008ea15c ["CALL", null, ["callee:00c58f30:8"]]
+ 008eb108 ["INT_ADD", "register:40f0:8", ["const:8eb108:8", "const:4:8"]]
+ 008eb108 ["CALL", null, ["callee:00c58f30:8"]]
- 008ea15c bytes 81b70d94
+ 008eb108 bytes 8ab70d94
- 008ea164 ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008eb110 ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008ea164 bytes c81c00f0
+ 008eb110 bytes c81c00f0
- 008ea168 ["COPY", "tmp:0:8", ["const:520:8"]]
- 008ea168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ea168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ea168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008eb114 ["COPY", "tmp:0:8", ["const:4f0:8"]]
+ 008eb114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008eb114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008eb114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ea168 bytes 08811491
+ 008eb114 bytes 08c11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9489267669e5145eab1563dae720611d"></a>

### [`008ea17c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea17c.md) → [`008eb128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb128.md) FUN_008eb128

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
      "definition_site": "008eb134",
      "incomplete_value": false,
      "site": "008eb134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea188",
      "incomplete_value": false,
      "site": "008ea188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:520:8"
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
      "008eb134",
      "DATA",
      [
        "storage",
        "00c85520",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eb134",
      "DATA",
      [
        "storage",
        "00c864f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea17c.md#insn-008ea180) · [`008ea184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea17c.md#insn-008ea184)
- 新版 [`008eb12c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb128.md#insn-008eb12c) · [`008eb130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb128.md#insn-008eb130)

~~~diff
- 008ea180 ["COPY", "register:4048:8", ["const:c85000:8"]]
+ 008eb12c ["COPY", "register:4048:8", ["const:c86000:8"]]
- 008ea180 bytes c91c00f0
+ 008eb12c bytes c91c00f0
- 008ea184 ["COPY", "tmp:0:8", ["const:520:8"]]
- 008ea184 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ea184 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ea184 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008eb130 ["COPY", "tmp:0:8", ["const:4f0:8"]]
+ 008eb130 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008eb130 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008eb130 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ea184 bytes 29811491
+ 008eb130 bytes 29c11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c863f0e7b846d82f0b731585105f2eae"></a>

### [`008ea198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea198.md) → [`008eb144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb144.md) FUN_008eb144

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "008eb16c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008ea1c0",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "008eb16c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "008eb16c",
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

- 旧版 [`008ea1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea198.md#insn-008ea1c0) · [`008ea1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea198.md#insn-008ea1bc)
- 新版 [`008eb16c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb144.md#insn-008eb16c) · [`008eb168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb144.md#insn-008eb168)

~~~diff
- 008ea1c0 ["INT_ADD", "register:40f0:8", ["const:8ea1c0:8", "const:4:8"]]
- 008ea1c0 ["CALL", null, ["ram:47ad34:8"]]
+ 008eb16c ["INT_ADD", "register:40f0:8", ["const:8eb16c:8", "const:4:8"]]
+ 008eb16c ["CALL", null, ["ram:47b054:8"]]
- 008ea1c0 bytes dd42ee97
+ 008eb16c bytes ba3fee97
- 008ea1bc ["INT_ADD", "register:40f0:8", ["const:8ea1bc:8", "const:4:8"]]
- 008ea1bc ["CALL", null, ["callee:008ba17c:8"]]
+ 008eb168 ["INT_ADD", "register:40f0:8", ["const:8eb168:8", "const:4:8"]]
+ 008eb168 ["CALL", null, ["callee:008ba17c:8"]]
- 008ea1bc bytes 053cff97
+ 008eb168 bytes 053cff97
~~~


<a id="compare-9aaaba0769a0e840f7a0528c03bc2299"></a>

### [`008ea204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea204.md) → [`008eb1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb1b0.md) FUN_008eb1b0

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
      "definition_site": "008eb1d4",
      "incomplete_value": false,
      "site": "008eb1d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea228",
      "incomplete_value": false,
      "site": "008ea228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
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
      "008eb1d4",
      "DATA",
      [
        "storage",
        "00c855a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eb1d4",
      "DATA",
      [
        "storage",
        "00c86570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea204.md#insn-008ea218) · [`008ea220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea204.md#insn-008ea220) · [`008ea224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea204.md#insn-008ea224)
- 新版 [`008eb1c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb1b0.md#insn-008eb1c4) · [`008eb1cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb1b0.md#insn-008eb1cc) · [`008eb1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb1b0.md#insn-008eb1d0)

~~~diff
- 008ea218 ["INT_ADD", "register:40f0:8", ["const:8ea218:8", "const:4:8"]]
- 008ea218 ["CALL", null, ["callee:00c58f30:8"]]
+ 008eb1c4 ["INT_ADD", "register:40f0:8", ["const:8eb1c4:8", "const:4:8"]]
+ 008eb1c4 ["CALL", null, ["callee:00c58f30:8"]]
- 008ea218 bytes 52b70d94
+ 008eb1c4 bytes 5bb70d94
- 008ea220 ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008eb1cc ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008ea220 bytes c81c00f0
+ 008eb1cc bytes c81c00f0
- 008ea224 ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 008ea224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ea224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ea224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008eb1d0 ["COPY", "tmp:0:8", ["const:570:8"]]
+ 008eb1d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008eb1d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008eb1d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ea224 bytes 08811691
+ 008eb1d0 bytes 08c11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79fd71d331e193b77ef0ddc8a398c35e"></a>

### [`008ea238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea238.md) → [`008eb1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb1e4.md) FUN_008eb1e4

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
      "definition_site": "008eb1f0",
      "incomplete_value": false,
      "site": "008eb1f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea244",
      "incomplete_value": false,
      "site": "008ea244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
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
      "008eb1f0",
      "DATA",
      [
        "storage",
        "00c855a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eb1f0",
      "DATA",
      [
        "storage",
        "00c86570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea23c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea238.md#insn-008ea23c) · [`008ea240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea238.md#insn-008ea240)
- 新版 [`008eb1e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb1e4.md#insn-008eb1e8) · [`008eb1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb1e4.md#insn-008eb1ec)

~~~diff
- 008ea23c ["COPY", "register:4048:8", ["const:c85000:8"]]
+ 008eb1e8 ["COPY", "register:4048:8", ["const:c86000:8"]]
- 008ea23c bytes c91c00f0
+ 008eb1e8 bytes c91c00f0
- 008ea240 ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 008ea240 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ea240 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ea240 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008eb1ec ["COPY", "tmp:0:8", ["const:570:8"]]
+ 008eb1ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008eb1ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008eb1ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ea240 bytes 29811691
+ 008eb1ec bytes 29c11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19a6ee4f16832c44c1f877d23ae655bd"></a>

### [`008ea254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea254.md) → [`008eb200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb200.md) FUN_008eb200

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "008eb228",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008ea27c",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "008eb228",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "008eb228",
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

- 旧版 [`008ea27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea254.md#insn-008ea27c) · [`008ea278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea254.md#insn-008ea278)
- 新版 [`008eb228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb200.md#insn-008eb228) · [`008eb224`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb200.md#insn-008eb224)

~~~diff
- 008ea27c ["INT_ADD", "register:40f0:8", ["const:8ea27c:8", "const:4:8"]]
- 008ea27c ["CALL", null, ["ram:47ad34:8"]]
+ 008eb228 ["INT_ADD", "register:40f0:8", ["const:8eb228:8", "const:4:8"]]
+ 008eb228 ["CALL", null, ["ram:47b054:8"]]
- 008ea27c bytes ae42ee97
+ 008eb228 bytes 8b3fee97
- 008ea278 ["INT_ADD", "register:40f0:8", ["const:8ea278:8", "const:4:8"]]
- 008ea278 ["CALL", null, ["callee:008ba17c:8"]]
+ 008eb224 ["INT_ADD", "register:40f0:8", ["const:8eb224:8", "const:4:8"]]
+ 008eb224 ["CALL", null, ["callee:008ba17c:8"]]
- 008ea278 bytes d63bff97
+ 008eb224 bytes d63bff97
~~~


<a id="compare-513e29276b19d4daa417d528457275d7"></a>

### [`008ea2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea2c0.md) → [`008eb26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb26c.md) FUN_008eb26c

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
      "definition_site": "008eb290",
      "incomplete_value": false,
      "site": "008eb290",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea2e4",
      "incomplete_value": false,
      "site": "008ea2e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "008eb290",
      "DATA",
      [
        "storage",
        "00c85620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eb290",
      "DATA",
      [
        "storage",
        "00c865f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea2d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea2c0.md#insn-008ea2d4) · [`008ea2dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea2c0.md#insn-008ea2dc) · [`008ea2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea2c0.md#insn-008ea2e0)
- 新版 [`008eb280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb26c.md#insn-008eb280) · [`008eb288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb26c.md#insn-008eb288) · [`008eb28c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb26c.md#insn-008eb28c)

~~~diff
- 008ea2d4 ["INT_ADD", "register:40f0:8", ["const:8ea2d4:8", "const:4:8"]]
- 008ea2d4 ["CALL", null, ["callee:00c58f30:8"]]
+ 008eb280 ["INT_ADD", "register:40f0:8", ["const:8eb280:8", "const:4:8"]]
+ 008eb280 ["CALL", null, ["callee:00c58f30:8"]]
- 008ea2d4 bytes 23b70d94
+ 008eb280 bytes 2cb70d94
- 008ea2dc ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008eb288 ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008ea2dc bytes c81c00f0
+ 008eb288 bytes c81c00f0
- 008ea2e0 ["COPY", "tmp:0:8", ["const:620:8"]]
- 008ea2e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ea2e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ea2e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008eb28c ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 008eb28c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008eb28c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008eb28c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ea2e0 bytes 08811891
+ 008eb28c bytes 08c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c719f33a6e5aab507d80b6244d91344"></a>

### [`008ea2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea2f4.md) → [`008eb2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb2a0.md) FUN_008eb2a0

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
      "definition_site": "008eb2ac",
      "incomplete_value": false,
      "site": "008eb2ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea300",
      "incomplete_value": false,
      "site": "008ea300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "008eb2ac",
      "DATA",
      [
        "storage",
        "00c85620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eb2ac",
      "DATA",
      [
        "storage",
        "00c865f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea2f4.md#insn-008ea2f8) · [`008ea2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea2f4.md#insn-008ea2fc)
- 新版 [`008eb2a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb2a0.md#insn-008eb2a4) · [`008eb2a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb2a0.md#insn-008eb2a8)

~~~diff
- 008ea2f8 ["COPY", "register:4048:8", ["const:c85000:8"]]
+ 008eb2a4 ["COPY", "register:4048:8", ["const:c86000:8"]]
- 008ea2f8 bytes c91c00f0
+ 008eb2a4 bytes c91c00f0
- 008ea2fc ["COPY", "tmp:0:8", ["const:620:8"]]
- 008ea2fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ea2fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ea2fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008eb2a8 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 008eb2a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008eb2a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008eb2a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ea2fc bytes 29811891
+ 008eb2a8 bytes 29c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29a5c1b0c014e5220577452a41280179"></a>

### [`008ea7e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea7e4.md) → [`008eb790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb790.md) FUN_008eb790

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
      "definition_site": "008eb7b4",
      "incomplete_value": false,
      "site": "008eb7b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea808",
      "incomplete_value": false,
      "site": "008ea808",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "008eb7b4",
      "DATA",
      [
        "storage",
        "00c856b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eb7b4",
      "DATA",
      [
        "storage",
        "00c86680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea7e4.md#insn-008ea7f8) · [`008ea800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea7e4.md#insn-008ea800) · [`008ea804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea7e4.md#insn-008ea804)
- 新版 [`008eb7a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb790.md#insn-008eb7a4) · [`008eb7ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb790.md#insn-008eb7ac) · [`008eb7b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb790.md#insn-008eb7b0)

~~~diff
- 008ea7f8 ["INT_ADD", "register:40f0:8", ["const:8ea7f8:8", "const:4:8"]]
- 008ea7f8 ["CALL", null, ["callee:00c58f30:8"]]
+ 008eb7a4 ["INT_ADD", "register:40f0:8", ["const:8eb7a4:8", "const:4:8"]]
+ 008eb7a4 ["CALL", null, ["callee:00c58f30:8"]]
- 008ea7f8 bytes dab50d94
+ 008eb7a4 bytes e3b50d94
- 008ea800 ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008eb7ac ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008ea800 bytes c81c00f0
+ 008eb7ac bytes c81c00f0
- 008ea804 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 008ea804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ea804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ea804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008eb7b0 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 008eb7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008eb7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008eb7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ea804 bytes 08c11a91
+ 008eb7b0 bytes 08011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-236446463e4e7c7e50f3e4f83619be54"></a>

### [`008ea818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea818.md) → [`008eb7c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb7c4.md) FUN_008eb7c4

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
      "definition_site": "008eb7d0",
      "incomplete_value": false,
      "site": "008eb7d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea824",
      "incomplete_value": false,
      "site": "008ea824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "008eb7d0",
      "DATA",
      [
        "storage",
        "00c856b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eb7d0",
      "DATA",
      [
        "storage",
        "00c86680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea81c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea818.md#insn-008ea81c) · [`008ea820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea818.md#insn-008ea820)
- 新版 [`008eb7c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb7c4.md#insn-008eb7c8) · [`008eb7cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb7c4.md#insn-008eb7cc)

~~~diff
- 008ea81c ["COPY", "register:4048:8", ["const:c85000:8"]]
+ 008eb7c8 ["COPY", "register:4048:8", ["const:c86000:8"]]
- 008ea81c bytes c91c00f0
+ 008eb7c8 bytes c91c00f0
- 008ea820 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 008ea820 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ea820 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ea820 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008eb7cc ["COPY", "tmp:0:8", ["const:680:8"]]
+ 008eb7cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008eb7cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008eb7cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ea820 bytes 29c11a91
+ 008eb7cc bytes 29011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ac529d75777a947cbc55528280e1af0"></a>

### [`008ea834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea834.md) → [`008eb7e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb7e0.md) FUN_008eb7e0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "008eb804",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008ea858",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "008eb804",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "008eb804",
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

- 旧版 [`008ea858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea834.md#insn-008ea858) · [`008ea854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea834.md#insn-008ea854)
- 新版 [`008eb804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb7e0.md#insn-008eb804) · [`008eb800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb7e0.md#insn-008eb800)

~~~diff
- 008ea858 ["INT_ADD", "register:40f0:8", ["const:8ea858:8", "const:4:8"]]
- 008ea858 ["CALL", null, ["ram:47ad34:8"]]
+ 008eb804 ["INT_ADD", "register:40f0:8", ["const:8eb804:8", "const:4:8"]]
+ 008eb804 ["CALL", null, ["ram:47b054:8"]]
- 008ea858 bytes 3741ee97
+ 008eb804 bytes 143eee97
- 008ea854 ["INT_ADD", "register:40f0:8", ["const:8ea854:8", "const:4:8"]]
- 008ea854 ["CALL", null, ["callee:008ba17c:8"]]
+ 008eb800 ["INT_ADD", "register:40f0:8", ["const:8eb800:8", "const:4:8"]]
+ 008eb800 ["CALL", null, ["callee:008ba17c:8"]]
- 008ea854 bytes 5f3aff97
+ 008eb800 bytes 5f3aff97
~~~


<a id="compare-aabe8b7862bcd54a6a7818dfb7eac625"></a>

### [`008ea8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea8a8.md) → [`008eb854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb854.md) FUN_008eb854

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
      "definition_site": "008eb878",
      "incomplete_value": false,
      "site": "008eb878",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea8cc",
      "incomplete_value": false,
      "site": "008ea8cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:730:8"
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
      "008eb878",
      "DATA",
      [
        "storage",
        "00c85730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eb878",
      "DATA",
      [
        "storage",
        "00c86700",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea8a8.md#insn-008ea8bc) · [`008ea8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea8a8.md#insn-008ea8c4) · [`008ea8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea8a8.md#insn-008ea8c8)
- 新版 [`008eb868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb854.md#insn-008eb868) · [`008eb870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb854.md#insn-008eb870) · [`008eb874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb854.md#insn-008eb874)

~~~diff
- 008ea8bc ["INT_ADD", "register:40f0:8", ["const:8ea8bc:8", "const:4:8"]]
- 008ea8bc ["CALL", null, ["callee:00c58f30:8"]]
+ 008eb868 ["INT_ADD", "register:40f0:8", ["const:8eb868:8", "const:4:8"]]
+ 008eb868 ["CALL", null, ["callee:00c58f30:8"]]
- 008ea8bc bytes a9b50d94
+ 008eb868 bytes b2b50d94
- 008ea8c4 ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008eb870 ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008ea8c4 bytes c81c00f0
+ 008eb870 bytes c81c00f0
- 008ea8c8 ["COPY", "tmp:0:8", ["const:730:8"]]
- 008ea8c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ea8c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ea8c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008eb874 ["COPY", "tmp:0:8", ["const:700:8"]]
+ 008eb874 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008eb874 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008eb874 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ea8c8 bytes 08c11c91
+ 008eb874 bytes 08011c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e369a99e452fb83121ec8a86de28ca5"></a>

### [`008ea8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea8dc.md) → [`008eb888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb888.md) FUN_008eb888

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
      "definition_site": "008eb894",
      "incomplete_value": false,
      "site": "008eb894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea8e8",
      "incomplete_value": false,
      "site": "008ea8e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
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
      "008eb894",
      "DATA",
      [
        "storage",
        "00c85730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eb894",
      "DATA",
      [
        "storage",
        "00c86700",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea8dc.md#insn-008ea8e0) · [`008ea8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea8dc.md#insn-008ea8e4)
- 新版 [`008eb88c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb888.md#insn-008eb88c) · [`008eb890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb888.md#insn-008eb890)

~~~diff
- 008ea8e0 ["COPY", "register:4048:8", ["const:c85000:8"]]
+ 008eb88c ["COPY", "register:4048:8", ["const:c86000:8"]]
- 008ea8e0 bytes c91c00f0
+ 008eb88c bytes c91c00f0
- 008ea8e4 ["COPY", "tmp:0:8", ["const:730:8"]]
- 008ea8e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ea8e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ea8e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008eb890 ["COPY", "tmp:0:8", ["const:700:8"]]
+ 008eb890 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008eb890 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008eb890 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ea8e4 bytes 29c11c91
+ 008eb890 bytes 29011c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ace0df33272413a0155aac284c6e63f3"></a>

### [`008ea8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea8f8.md) → [`008eb8a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb8a4.md) FUN_008eb8a4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

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
      "site": "008eb8c8",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008ea91c",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "008eb8c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "008eb8c8",
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

- 旧版 [`008ea91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea8f8.md#insn-008ea91c) · [`008ea918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea8f8.md#insn-008ea918)
- 新版 [`008eb8c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb8a4.md#insn-008eb8c8) · [`008eb8c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb8a4.md#insn-008eb8c4)

~~~diff
- 008ea91c ["INT_ADD", "register:40f0:8", ["const:8ea91c:8", "const:4:8"]]
- 008ea91c ["CALL", null, ["ram:47ad34:8"]]
+ 008eb8c8 ["INT_ADD", "register:40f0:8", ["const:8eb8c8:8", "const:4:8"]]
+ 008eb8c8 ["CALL", null, ["ram:47b054:8"]]
- 008ea91c bytes 0641ee97
+ 008eb8c8 bytes e33dee97
- 008ea918 ["INT_ADD", "register:40f0:8", ["const:8ea918:8", "const:4:8"]]
- 008ea918 ["CALL", null, ["callee:008ba17c:8"]]
+ 008eb8c4 ["INT_ADD", "register:40f0:8", ["const:8eb8c4:8", "const:4:8"]]
+ 008eb8c4 ["CALL", null, ["callee:008ba17c:8"]]
- 008ea918 bytes 2e3aff97
+ 008eb8c4 bytes 2e3aff97
~~~


<a id="compare-54e7706f322d60bc1168b138588dbfd8"></a>

### [`008ea99c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea99c.md) → [`008eb948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb948.md) FUN_008eb948

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
      "definition_site": "008eb96c",
      "incomplete_value": false,
      "site": "008eb96c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea9c0",
      "incomplete_value": false,
      "site": "008ea9c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
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
      "008eb96c",
      "DATA",
      [
        "storage",
        "00c857b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eb96c",
      "DATA",
      [
        "storage",
        "00c86780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea99c.md#insn-008ea9b0) · [`008ea9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea99c.md#insn-008ea9b8) · [`008ea9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea99c.md#insn-008ea9bc)
- 新版 [`008eb95c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb948.md#insn-008eb95c) · [`008eb964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb948.md#insn-008eb964) · [`008eb968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb948.md#insn-008eb968)

~~~diff
- 008ea9b0 ["INT_ADD", "register:40f0:8", ["const:8ea9b0:8", "const:4:8"]]
- 008ea9b0 ["CALL", null, ["callee:00c58f30:8"]]
+ 008eb95c ["INT_ADD", "register:40f0:8", ["const:8eb95c:8", "const:4:8"]]
+ 008eb95c ["CALL", null, ["callee:00c58f30:8"]]
- 008ea9b0 bytes 6cb50d94
+ 008eb95c bytes 75b50d94
- 008ea9b8 ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008eb964 ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008ea9b8 bytes c81c00f0
+ 008eb964 bytes c81c00f0
- 008ea9bc ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 008ea9bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ea9bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ea9bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008eb968 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 008eb968 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008eb968 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008eb968 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ea9bc bytes 08c11e91
+ 008eb968 bytes 08011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-befc9a8f961f94f148477134e5e90315"></a>

### [`008ea9d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea9d0.md) → [`008eb97c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb97c.md) FUN_008eb97c

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
      "definition_site": "008eb988",
      "incomplete_value": false,
      "site": "008eb988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ea9dc",
      "incomplete_value": false,
      "site": "008ea9dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
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
      "008eb988",
      "DATA",
      [
        "storage",
        "00c857b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eb988",
      "DATA",
      [
        "storage",
        "00c86780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ea9d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea9d0.md#insn-008ea9d4) · [`008ea9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea9d0.md#insn-008ea9d8)
- 新版 [`008eb980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb97c.md#insn-008eb980) · [`008eb984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb97c.md#insn-008eb984)

~~~diff
- 008ea9d4 ["COPY", "register:4048:8", ["const:c85000:8"]]
+ 008eb980 ["COPY", "register:4048:8", ["const:c86000:8"]]
- 008ea9d4 bytes c91c00f0
+ 008eb980 bytes c91c00f0
- 008ea9d8 ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 008ea9d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ea9d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ea9d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008eb984 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 008eb984 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008eb984 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008eb984 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ea9d8 bytes 29c11e91
+ 008eb984 bytes 29011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2af3dc580d7074b2ed5dd380c439888d"></a>

### [`008ea9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea9ec.md) → [`008eb998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb998.md) FUN_008eb998

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

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
      "site": "008eb9b4",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008eaa08",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "008eb9b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "008eb9b4",
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

- 旧版 [`008eaa08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea9ec.md#insn-008eaa08) · [`008eaa04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008ea9ec.md#insn-008eaa04)
- 新版 [`008eb9b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb998.md#insn-008eb9b4) · [`008eb9b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb998.md#insn-008eb9b0)

~~~diff
- 008eaa08 ["INT_ADD", "register:40f0:8", ["const:8eaa08:8", "const:4:8"]]
- 008eaa08 ["CALL", null, ["ram:47ad34:8"]]
+ 008eb9b4 ["INT_ADD", "register:40f0:8", ["const:8eb9b4:8", "const:4:8"]]
+ 008eb9b4 ["CALL", null, ["ram:47b054:8"]]
- 008eaa08 bytes cb40ee97
+ 008eb9b4 bytes a83dee97
- 008eaa04 ["INT_ADD", "register:40f0:8", ["const:8eaa04:8", "const:4:8"]]
- 008eaa04 ["CALL", null, ["callee:008ba17c:8"]]
+ 008eb9b0 ["INT_ADD", "register:40f0:8", ["const:8eb9b0:8", "const:4:8"]]
+ 008eb9b0 ["CALL", null, ["callee:008ba17c:8"]]
- 008eaa04 bytes f339ff97
+ 008eb9b0 bytes f339ff97
~~~


<a id="compare-eeed4a5e3f2f342e825c5da24db8bce3"></a>

### [`008eaa4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaa4c.md) → [`008eb9f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb9f8.md) FUN_008eb9f8

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
      "definition_site": "008eba1c",
      "incomplete_value": false,
      "site": "008eba1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008eaa70",
      "incomplete_value": false,
      "site": "008eaa70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "008eba1c",
      "DATA",
      [
        "storage",
        "00c85830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eba1c",
      "DATA",
      [
        "storage",
        "00c86800",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008eaa60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaa4c.md#insn-008eaa60) · [`008eaa68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaa4c.md#insn-008eaa68) · [`008eaa6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaa4c.md#insn-008eaa6c)
- 新版 [`008eba0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb9f8.md#insn-008eba0c) · [`008eba14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb9f8.md#insn-008eba14) · [`008eba18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eb9f8.md#insn-008eba18)

~~~diff
- 008eaa60 ["INT_ADD", "register:40f0:8", ["const:8eaa60:8", "const:4:8"]]
- 008eaa60 ["CALL", null, ["callee:00c58f30:8"]]
+ 008eba0c ["INT_ADD", "register:40f0:8", ["const:8eba0c:8", "const:4:8"]]
+ 008eba0c ["CALL", null, ["callee:00c58f30:8"]]
- 008eaa60 bytes 40b50d94
+ 008eba0c bytes 49b50d94
- 008eaa68 ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008eba14 ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008eaa68 bytes c81c00f0
+ 008eba14 bytes c81c00f0
- 008eaa6c ["COPY", "tmp:0:8", ["const:830:8"]]
- 008eaa6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008eaa6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008eaa6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008eba18 ["COPY", "tmp:0:8", ["const:800:8"]]
+ 008eba18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008eba18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008eba18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008eaa6c bytes 08c12091
+ 008eba18 bytes 08012091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a63765cd43fdacbf7a9d692d4fba5521"></a>

### [`008eaa80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaa80.md) → [`008eba2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eba2c.md) FUN_008eba2c

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
      "definition_site": "008eba38",
      "incomplete_value": false,
      "site": "008eba38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008eaa8c",
      "incomplete_value": false,
      "site": "008eaa8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "008eba38",
      "DATA",
      [
        "storage",
        "00c85830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008eba38",
      "DATA",
      [
        "storage",
        "00c86800",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008eaa84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaa80.md#insn-008eaa84) · [`008eaa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaa80.md#insn-008eaa88)
- 新版 [`008eba30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eba2c.md#insn-008eba30) · [`008eba34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eba2c.md#insn-008eba34)

~~~diff
- 008eaa84 ["COPY", "register:4048:8", ["const:c85000:8"]]
+ 008eba30 ["COPY", "register:4048:8", ["const:c86000:8"]]
- 008eaa84 bytes c91c00f0
+ 008eba30 bytes c91c00f0
- 008eaa88 ["COPY", "tmp:0:8", ["const:830:8"]]
- 008eaa88 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008eaa88 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008eaa88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008eba34 ["COPY", "tmp:0:8", ["const:800:8"]]
+ 008eba34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008eba34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008eba34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008eaa88 bytes 29c12091
+ 008eba34 bytes 29012091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72eb6794dd3b4b97830f5559440fc3d5"></a>

### [`008eaa9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaa9c.md) → [`008eba48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eba48.md) FUN_008eba48

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 15件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0052dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`0052e060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e060.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment

命令の説明率　旧版 94.69% / 新版 94.69%

CFGの説明率　旧版 87.10% / 新版 83.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008ebb30",
      "incomplete_value": true,
      "site": "008ebb48",
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
                "const:6b3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008eab84",
      "incomplete_value": true,
      "site": "008eab9c",
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
                "const:5e4:8"
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
      "definition_site": "008ebc20",
      "incomplete_value": false,
      "site": "008ebc20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008eac74",
      "incomplete_value": false,
      "site": "008eac74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "site": "008eba8c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008eaae0",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "008eba8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008ebb10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008ebb30",
      "READ",
      [
        "storage",
        "002b95e4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008eba8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "008ebb10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "008ebb30",
      "READ",
      [
        "storage",
        "002b96b3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008eaae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaa9c.md#insn-008eaae0) · [`008eab64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaa9c.md#insn-008eab64) · [`008ead5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaa9c.md#insn-008ead5c)
- 新版 [`008eba8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eba48.md#insn-008eba8c) · [`008ebb10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008eba48.md#insn-008ebb10)

~~~diff
- 008eaae0 ["INT_ADD", "register:40f0:8", ["const:8eaae0:8", "const:4:8"]]
- 008eaae0 ["CALL", null, ["ram:47ad34:8"]]
+ 008eba8c ["INT_ADD", "register:40f0:8", ["const:8eba8c:8", "const:4:8"]]
+ 008eba8c ["CALL", null, ["ram:47b054:8"]]
- 008eaae0 bytes 9540ee97
+ 008eba8c bytes 723dee97
- 008eab64 ["INT_ADD", "register:40f0:8", ["const:8eab64:8", "const:4:8"]]
- 008eab64 ["CALL", null, ["ram:47ad34:8"]]
+ 008ebb10 ["INT_ADD", "register:40f0:8", ["const:8ebb10:8", "const:4:8"]]
+ 008ebb10 ["CALL", null, ["ram:47b054:8"]]
- 008eab64 bytes 7440ee97
+ 008ebb10 bytes 513dee97
- 008ead5c ["COPY", "register:0:8", ["register:40f0:8"]]
- 008ead5c ["RETURN", null, ["register:0:8"]]
- 008ead5c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17e9cd20ebf42fc55d314a473e6c1f0d"></a>

### [`008eaf20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaf20.md) → [`008ebecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebecc.md) FUN_008ebecc

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
      "definition_site": "008ebef0",
      "incomplete_value": false,
      "site": "008ebef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008eaf44",
      "incomplete_value": false,
      "site": "008eaf44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "008ebef0",
      "DATA",
      [
        "storage",
        "00c858a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ebef0",
      "DATA",
      [
        "storage",
        "00c86870",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008eaf34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaf20.md#insn-008eaf34) · [`008eaf3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaf20.md#insn-008eaf3c) · [`008eaf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaf20.md#insn-008eaf40)
- 新版 [`008ebee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebecc.md#insn-008ebee0) · [`008ebee8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebecc.md#insn-008ebee8) · [`008ebeec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebecc.md#insn-008ebeec)

~~~diff
- 008eaf34 ["INT_ADD", "register:40f0:8", ["const:8eaf34:8", "const:4:8"]]
- 008eaf34 ["CALL", null, ["callee:00c58f30:8"]]
+ 008ebee0 ["INT_ADD", "register:40f0:8", ["const:8ebee0:8", "const:4:8"]]
+ 008ebee0 ["CALL", null, ["callee:00c58f30:8"]]
- 008eaf34 bytes 0bb40d94
+ 008ebee0 bytes 14b40d94
- 008eaf3c ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008ebee8 ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008eaf3c bytes c81c00f0
+ 008ebee8 bytes c81c00f0
- 008eaf40 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 008eaf40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008eaf40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008eaf40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ebeec ["COPY", "tmp:0:8", ["const:870:8"]]
+ 008ebeec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ebeec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ebeec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008eaf40 bytes 08812291
+ 008ebeec bytes 08c12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4ced70f996059e2bd58ef9321c6e3c7"></a>

### [`008eaf54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaf54.md) → [`008ebf00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebf00.md) FUN_008ebf00

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
      "definition_site": "008ebf0c",
      "incomplete_value": false,
      "site": "008ebf0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008eaf60",
      "incomplete_value": false,
      "site": "008eaf60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "008ebf0c",
      "DATA",
      [
        "storage",
        "00c858a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ebf0c",
      "DATA",
      [
        "storage",
        "00c86870",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008eaf58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaf54.md#insn-008eaf58) · [`008eaf5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaf54.md#insn-008eaf5c)
- 新版 [`008ebf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebf00.md#insn-008ebf04) · [`008ebf08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebf00.md#insn-008ebf08)

~~~diff
- 008eaf58 ["COPY", "register:4048:8", ["const:c85000:8"]]
+ 008ebf04 ["COPY", "register:4048:8", ["const:c86000:8"]]
- 008eaf58 bytes c91c00f0
+ 008ebf04 bytes c91c00f0
- 008eaf5c ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 008eaf5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008eaf5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008eaf5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ebf08 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 008ebf08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ebf08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ebf08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008eaf5c bytes 29812291
+ 008ebf08 bytes 29c12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a52129c0ddac0112120ec214f2cfc11d"></a>

### [`008eaf70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaf70.md) → [`008ebf1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebf1c.md) FUN_008ebf1c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

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
      "site": "008ebf38",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008eaf8c",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "008ebf38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "008ebf38",
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

- 旧版 [`008eaf8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaf70.md#insn-008eaf8c) · [`008eaf88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eaf70.md#insn-008eaf88)
- 新版 [`008ebf38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebf1c.md#insn-008ebf38) · [`008ebf34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebf1c.md#insn-008ebf34)

~~~diff
- 008eaf8c ["INT_ADD", "register:40f0:8", ["const:8eaf8c:8", "const:4:8"]]
- 008eaf8c ["CALL", null, ["ram:47ad34:8"]]
+ 008ebf38 ["INT_ADD", "register:40f0:8", ["const:8ebf38:8", "const:4:8"]]
+ 008ebf38 ["CALL", null, ["ram:47b054:8"]]
- 008eaf8c bytes 6a3fee97
+ 008ebf38 bytes 473cee97
- 008eaf88 ["INT_ADD", "register:40f0:8", ["const:8eaf88:8", "const:4:8"]]
- 008eaf88 ["CALL", null, ["callee:008ba17c:8"]]
+ 008ebf34 ["INT_ADD", "register:40f0:8", ["const:8ebf34:8", "const:4:8"]]
+ 008ebf34 ["CALL", null, ["callee:008ba17c:8"]]
- 008eaf88 bytes 9238ff97
+ 008ebf34 bytes 9238ff97
~~~


<a id="compare-45390f9f5f49be500822504ea7ca6d01"></a>

### [`008eafd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eafd0.md) → [`008ebf7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebf7c.md) FUN_008ebf7c

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
      "definition_site": "008ebfa0",
      "incomplete_value": false,
      "site": "008ebfa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008eaff4",
      "incomplete_value": false,
      "site": "008eaff4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "008ebfa0",
      "DATA",
      [
        "storage",
        "00c85930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ebfa0",
      "DATA",
      [
        "storage",
        "00c86900",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008eafe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eafd0.md#insn-008eafe4) · [`008eafec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eafd0.md#insn-008eafec) · [`008eaff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ea/008eafd0.md#insn-008eaff0)
- 新版 [`008ebf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebf7c.md#insn-008ebf90) · [`008ebf98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebf7c.md#insn-008ebf98) · [`008ebf9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebf7c.md#insn-008ebf9c)

~~~diff
- 008eafe4 ["INT_ADD", "register:40f0:8", ["const:8eafe4:8", "const:4:8"]]
- 008eafe4 ["CALL", null, ["callee:00c58f30:8"]]
+ 008ebf90 ["INT_ADD", "register:40f0:8", ["const:8ebf90:8", "const:4:8"]]
+ 008ebf90 ["CALL", null, ["callee:00c58f30:8"]]
- 008eafe4 bytes dfb30d94
+ 008ebf90 bytes e8b30d94
- 008eafec ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008ebf98 ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008eafec bytes c81c00f0
+ 008ebf98 bytes c81c00f0
- 008eaff0 ["COPY", "tmp:0:8", ["const:930:8"]]
- 008eaff0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008eaff0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008eaff0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ebf9c ["COPY", "tmp:0:8", ["const:900:8"]]
+ 008ebf9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ebf9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ebf9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008eaff0 bytes 08c12491
+ 008ebf9c bytes 08012491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54ec793d34c9521dc233fe8de58ae9bf"></a>

### [`008eb004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb004.md) → [`008ebfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebfb0.md) FUN_008ebfb0

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
      "definition_site": "008ebfbc",
      "incomplete_value": false,
      "site": "008ebfbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008eb010",
      "incomplete_value": false,
      "site": "008eb010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "008ebfbc",
      "DATA",
      [
        "storage",
        "00c85930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ebfbc",
      "DATA",
      [
        "storage",
        "00c86900",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008eb008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb004.md#insn-008eb008) · [`008eb00c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb004.md#insn-008eb00c)
- 新版 [`008ebfb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebfb0.md#insn-008ebfb4) · [`008ebfb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebfb0.md#insn-008ebfb8)

~~~diff
- 008eb008 ["COPY", "register:4048:8", ["const:c85000:8"]]
+ 008ebfb4 ["COPY", "register:4048:8", ["const:c86000:8"]]
- 008eb008 bytes c91c00d0
+ 008ebfb4 bytes c91c00f0
- 008eb00c ["COPY", "tmp:0:8", ["const:930:8"]]
- 008eb00c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008eb00c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008eb00c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ebfb8 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 008ebfb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ebfb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ebfb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008eb00c bytes 29c12491
+ 008ebfb8 bytes 29012491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9466c44992792aa6d43c5ff20204879"></a>

### [`008eb020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb020.md) → [`008ebfcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebfcc.md) FUN_008ebfcc

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b92e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92e8.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`004692e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692e8.md) [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008ba294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba294.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.77% / 新版 90.77%

CFGの説明率　旧版 11.11% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008eb058"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008ec004"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008ec00c",
      "incomplete_value": false,
      "site": "008ec020",
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
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008eb060",
      "incomplete_value": false,
      "site": "008eb074",
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
            "const:f28:8"
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
      "unmatched:008eb054",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:008eb058",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ec03c"
      ]
    ],
    [
      "unmatched:008eb060",
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
      "008ec000",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "008ec004",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ec03c"
      ]
    ],
    [
      "008ec00c",
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

- 旧版 [`008eb058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb020.md#insn-008eb058) · [`008eb074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb020.md#insn-008eb074) · [`008eb0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb020.md#insn-008eb0ac)
- 新版 [`008ec020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebfcc.md#insn-008ec020) · [`008ec058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008eb/008ebfcc.md#insn-008ec058)

~~~diff
- 008eb058 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008eb058 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 008eb058 bytes c80100b4
- 008eb074 ["INT_ADD", "register:40f0:8", ["const:8eb074:8", "const:4:8"]]
- 008eb074 ["CALL", null, ["callee:00c596b0:8"]]
+ 008ec020 ["INT_ADD", "register:40f0:8", ["const:8ec020:8", "const:4:8"]]
+ 008ec020 ["CALL", null, ["callee:00c596b0:8"]]
- 008eb074 bytes 9bb50d94
+ 008ec020 bytes a4b50d94
- 008eb0ac ["INT_ADD", "register:40f0:8", ["const:8eb0ac:8", "const:4:8"]]
- 008eb0ac ["CALL", null, ["callee:004692e8:8"]]
+ 008ec058 ["INT_ADD", "register:40f0:8", ["const:8ec058:8", "const:4:8"]]
+ 008ec058 ["CALL", null, ["callee:004692e8:8"]]
- 008eb0ac bytes c7f7ed97
+ 008ec058 bytes a4f4ed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a351e10d4bbc24526ed33fdb46866ac"></a>

### [`008eb14c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb14c.md) → [`008ec0f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ec0f8.md) _INIT_174

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.23% / 新版 80.23%

CFGの説明率　旧版 33.33% / 新版 35.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eb17c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eb1a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eb1c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008eb17c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008eb188",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "unmatched:008eb1a4",
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
      "008ec128",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008ec134",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "008ec150",
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

- 旧版 [`008eb17c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb14c.md#insn-008eb17c) · [`008eb1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb14c.md#insn-008eb1a4) · [`008eb1c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb14c.md#insn-008eb1c8)

~~~diff
- 008eb17c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008eb17c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008eb17c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008eb17c bytes a9831ff8
- 008eb1a4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 008eb1a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008eb1a4 bytes e013813c
- 008eb1c8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 008eb1c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008eb1c8 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-939d307a317ac1372de1d38ffc1b2d0d"></a>

### [`008eb4dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb4dc.md) → [`008ec488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ec488.md) FUN_008ec488

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006d87c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d8/006d87c0.md) · 呼出先 2件 [`008eb570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb570.md) [`008eb9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb9dc.md)
- 新版 呼出元 1件 [`006d8b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d8/006d8b70.md) · 呼出先 2件 [`008ec51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ec51c.md) [`008ec988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ec988.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008ec4e4",
      "incomplete_value": true,
      "site": "008ec4e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008eb538",
      "incomplete_value": true,
      "site": "008eb538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008ec50c",
      "incomplete_value": true,
      "site": "008ec50c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6b4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008eb560",
      "incomplete_value": true,
      "site": "008eb560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6e4:8"
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
      "008ec4c4",
      "READ",
      [
        "storage",
        "00ca46e0",
        null,
        "undefined4"
      ]
    ],
    [
      "008ec4e4",
      "WRITE",
      [
        "storage",
        "00ca46e0",
        null,
        "undefined4"
      ]
    ],
    [
      "008ec4ec",
      "READ",
      [
        "storage",
        "00ca46e4",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "008ec4c4",
      "READ",
      [
        "storage",
        "00ca56b0",
        null,
        "undefined4"
      ]
    ],
    [
      "008ec4e4",
      "WRITE",
      [
        "storage",
        "00ca56b0",
        null,
        "undefined4"
      ]
    ],
    [
      "008ec4ec",
      "READ",
      [
        "storage",
        "00ca56b4",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008eb538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb4dc.md#insn-008eb538) · [`008eb560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb4dc.md#insn-008eb560) · [`008eb4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb4dc.md#insn-008eb4f8)
- 新版 [`008ec4e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ec488.md#insn-008ec4e4) · [`008ec50c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ec488.md#insn-008ec50c) · [`008ec4a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ec488.md#insn-008ec4a4)

~~~diff
- 008eb538 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 008eb538 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008ec4e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6b0:8"]]
+ 008ec4e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008eb538 bytes 68e206b9
+ 008ec4e4 bytes 68b206b9
- 008eb560 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e4:8"]]
- 008eb560 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008ec50c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6b4:8"]]
+ 008ec50c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008eb560 bytes 68e606b9
+ 008ec50c bytes 68b606b9
- 008eb4f8 ["COPY", "register:4098:8", ["const:ca4000:8"]]
+ 008ec4a4 ["COPY", "register:4098:8", ["const:ca5000:8"]]
- 008eb4f8 bytes d31d00b0
+ 008ec4a4 bytes d31d00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2716006e9128ce347591d07fdc02fc7"></a>

### [`008eb570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb570.md) → [`008ec51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ec51c.md) FUN_008ec51c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`008eb4dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb4dc.md) [`008ec2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008ec2f4.md) [`008f5404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5404.md) [`008f6b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f6b3c.md) · 呼出先 13件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00633824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00633/00633824.md) [`008f23cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f2/008f23cc.md)
- 新版 呼出元 5件 [`008ec488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ec488.md) [`008ed2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ed/008ed2a0.md) [`008f63b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f6/008f63b0.md) [`008f7ae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f7/008f7ae8.md) [`008f8008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f8/008f8008.md) · 呼出先 13件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`00633bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00633/00633bd4.md) [`008f3378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f3/008f3378.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.60% / 新版 87.60%

CFGの説明率　旧版 79.55% / 新版 78.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eb7b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eb7b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eb7b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008ec5c8",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "008ec608",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "008ec744",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "008ec5c8",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ],
    [
      "008ec608",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ],
    [
      "008ec744",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008eb7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb570.md#insn-008eb7b0) · [`008eb7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb570.md#insn-008eb7b4) · [`008eb7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb570.md#insn-008eb7b8)

~~~diff
- 008eb7b0 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 008eb7b0 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:18:8"]]
- 008eb7b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 008eb7b0 bytes e8630039
- 008eb7b4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 008eb7b4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 008eb7b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:29:8"]]
- 008eb7b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 008eb7b4 bytes ffa70039
- 008eb7b8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:19:8"]]
- 008eb7b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008eb7b8 bytes e093813c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff3884a6707a3dabeb8c35551ccda984"></a>

### [`008eb9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb9dc.md) → [`008ec988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ec988.md) FUN_008ec988

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`008eb4dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb4dc.md) [`008ec2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008ec2f4.md) [`008f5404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5404.md) [`008f6b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f6b3c.md) · 呼出先 3件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008c4974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c4/008c4974.md) [`008cac10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ca/008cac10.md)
- 新版 呼出元 4件 [`008ec488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ec488.md) [`008ed2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ed/008ed2a0.md) [`008f63b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f6/008f63b0.md) [`008f8008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f8/008f8008.md) · 呼出先 3件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008c5920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c5/008c5920.md) [`008cbbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cb/008cbbbc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 87.90% / 新版 87.90%

CFGの説明率　旧版 17.65% / 新版 21.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008eba68"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008eca14"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008eba6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008eba68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008eca78"
      ]
    ],
    [
      "unmatched:008eba6c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ],
    [
      "unmatched:008ebb00",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ]
  ],
  "added": [
    [
      "008eca14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008eca78"
      ]
    ],
    [
      "008eca18",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ],
    [
      "008ecaac",
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

- 旧版 [`008eba68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb9dc.md#insn-008eba68) · [`008eba6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb9dc.md#insn-008eba6c) · [`008ebac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb9dc.md#insn-008ebac4)
- 新版 [`008eca70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ec988.md#insn-008eca70)

~~~diff
- 008eba68 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008eba68 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 008eba68 bytes 2a030054
- 008eba6c ["INT_ADD", "register:40f0:8", ["const:8eba6c:8", "const:4:8"]]
- 008eba6c ["CALL", null, ["callee:008524fc:8"]]
- 008eba6c bytes b996fd97
- 008ebac4 ["INT_ADD", "register:40f0:8", ["const:8ebac4:8", "const:4:8"]]
- 008ebac4 ["CALL", null, ["callee:008c5920:8"]]
+ 008eca70 ["INT_ADD", "register:40f0:8", ["const:8eca70:8", "const:4:8"]]
+ 008eca70 ["CALL", null, ["callee:008c5920:8"]]
- 008ebac4 bytes ac63ff97
+ 008eca70 bytes ac63ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52913e3280d9453dd27f52e5d3fc6df1"></a>

### [`008ebbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008ebbcc.md) → [`008ecb78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ecb78.md) FUN_008ecb78

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f67b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f67b8.md) · 呼出先 14件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)
- 新版 呼出元 1件 [`008f7764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f7/008f7764.md) · 呼出先 14件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`004889b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004889b8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 53.19% / 新版 54.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 10件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ebbf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ebc28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ebc50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ebbf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ebc28",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008ebc28",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008ecba0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "008ecbd4",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "008ecbd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ebbf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008ebbcc.md#insn-008ebbf4) · [`008ebc28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008ebbcc.md#insn-008ebc28) · [`008ebc34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008ebbcc.md#insn-008ebc34)
- 新版 [`008ecbe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ecb78.md#insn-008ecbe0)

~~~diff
- 008ebbf4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008ebbf4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 008ebbf4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008ebbf4 bytes a8031ff8
- 008ebc28 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 008ebc28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008ebc28 bytes e91700f9
- 008ebc34 ["INT_ADD", "register:40f0:8", ["const:8ebc34:8", "const:4:8"]]
- 008ebc34 ["CALL", null, ["callee:00c58f30:8"]]
+ 008ecbe0 ["INT_ADD", "register:40f0:8", ["const:8ecbe0:8", "const:4:8"]]
+ 008ecbe0 ["CALL", null, ["callee:00c58f30:8"]]
- 008ebc34 bytes cbb00d94
+ 008ecbe0 bytes d4b00d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc6f3e50586004245f316b0090f17966"></a>

### [`008ebec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008ebec8.md) → [`008ece74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ece74.md) FUN_008ece74

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f67b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f67b8.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`008003d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/008003d0.md) [`00800684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800684.md) [`008040cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00804/008040cc.md) [`008f8a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8a40.md)
- 新版 呼出元 1件 [`008f7764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f7/008f7764.md) · 呼出先 8件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00801334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00801/00801334.md) [`008015e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00801/008015e8.md) [`00805030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00805/00805030.md) [`008f99ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f9/008f99ec.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 94.94% / 新版 94.94%

CFGの説明率　旧版 66.67% / 新版 64.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008ebf4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008ecef8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008ecee8",
      "value": [
        "leaf",
        "ram:805030:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008ebf3c",
      "value": [
        "leaf",
        "ram:8040cc:8"
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
      "008ecee8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008040cc"
      ]
    ],
    [
      "unmatched:008ebf4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008eceb0"
      ]
    ]
  ],
  "added": [
    [
      "008ecee8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00805030"
      ]
    ],
    [
      "008ecef8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008eceb0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ebf3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008ebec8.md#insn-008ebf3c) · [`008ebf4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008ebec8.md#insn-008ebf4c)
- 新版 [`008ecee8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ece74.md#insn-008ecee8) · [`008ecef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ece74.md#insn-008ecef8)

~~~diff
- 008ebf3c ["INT_ADD", "register:40f0:8", ["const:8ebf3c:8", "const:4:8"]]
- 008ebf3c ["CALL", null, ["ram:8040cc:8"]]
+ 008ecee8 ["INT_ADD", "register:40f0:8", ["const:8ecee8:8", "const:4:8"]]
+ 008ecee8 ["CALL", null, ["ram:805030:8"]]
- 008ebf3c bytes 6460fc97
+ 008ecee8 bytes 5260fc97
- 008ebf4c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 008ebf4c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 008ebf4c bytes c3fdff54
+ 008ecef8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 008ecef8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 008ecef8 bytes c3fdff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-300dc6ce03a53515d484af3e2f4216da"></a>

### [`008ec004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008ec004.md) → [`008ecfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ecfb0.md) FUN_008ecfb0

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008efa48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ef/008efa48.md) · 呼出先 8件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0052dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md) [`005cd130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd130.md) [`006648e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/006648e0.md)
- 新版 呼出元 1件 [`008f09f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f0/008f09f4.md) · 呼出先 8件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`0052e060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e060.md) [`005cd4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cd4e0.md) [`00664c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664c90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 86.96% / 新版 90.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ec04c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ec050"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ec054"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ec040",
      "READ",
      [
        "storage",
        "002a5bfb",
        null,
        "string"
      ]
    ],
    [
      "unmatched:008ec044",
      "READ",
      [
        "storage",
        "002a5c0a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:008ec048",
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
      "008ecfec",
      "READ",
      [
        "storage",
        "002a5d53",
        null,
        "string"
      ]
    ],
    [
      "008ecff0",
      "READ",
      [
        "storage",
        "002a5d62",
        null,
        "string"
      ]
    ],
    [
      "008ecff4",
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

- 旧版 [`008ec030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008ec004.md#insn-008ec030) · [`008ec04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008ec004.md#insn-008ec04c) · [`008ec050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008ec004.md#insn-008ec050)
- 新版 [`008ecfdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ecfb0.md#insn-008ecfdc)

~~~diff
- 008ec030 ["INT_ADD", "register:40f0:8", ["const:8ec030:8", "const:4:8"]]
- 008ec030 ["CALL", null, ["callee:00c58f30:8"]]
+ 008ecfdc ["INT_ADD", "register:40f0:8", ["const:8ecfdc:8", "const:4:8"]]
+ 008ecfdc ["CALL", null, ["callee:00c58f30:8"]]
- 008ec030 bytes ccaf0d94
+ 008ecfdc bytes d5af0d94
- 008ec04c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 008ec04c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 008ec04c bytes e02b00f9
- 008ec050 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008ec050 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008ec050 bytes 0000803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95e430fa239253848eb553a162d16d00"></a>

### [`008ec2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008ec2f4.md) → [`008ed2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ed/008ed2a0.md) FUN_008ed2a0

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008efa48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ef/008efa48.md) · 呼出先 18件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md)
- 新版 呼出元 1件 [`008f09f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f0/008f09f4.md) · 呼出先 18件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0047ec3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047ec3c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`00493168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493168.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_destination` 7件, `store_value` 4件

アドレスに依存する影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008ed38c",
      "incomplete_value": true,
      "site": "008ed38c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ec3e0",
      "incomplete_value": true,
      "site": "008ec3e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be1:8"
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
      "definition_site": "008ed524",
      "incomplete_value": true,
      "site": "008ed524",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cbb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ec578",
      "incomplete_value": true,
      "site": "008ec578",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bee:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008ed840",
      "incomplete_value": false,
      "site": "008ed840",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ec894",
      "incomplete_value": false,
      "site": "008ec894",
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
            "const:6e0:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008ed364",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "008ed378",
      "READ",
      [
        "storage",
        "002abbe1",
        null,
        "string"
      ]
    ],
    [
      "008ed400",
      "READ",
      [
        "storage",
        "00c9ad70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008ed364",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ],
    [
      "008ed378",
      "READ",
      [
        "storage",
        "002abcae",
        null,
        "string"
      ]
    ],
    [
      "008ed400",
      "READ",
      [
        "storage",
        "00c9bd40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ec474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008ec2f4.md#insn-008ec474) · [`008ec5b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008ec2f4.md#insn-008ec5b4) · [`008ec894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008ec2f4.md#insn-008ec894)
- 新版 [`008ed420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ed/008ed2a0.md#insn-008ed420) · [`008ed560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ed/008ed2a0.md#insn-008ed560) · [`008ed840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ed/008ed2a0.md#insn-008ed840)

~~~diff
- 008ec474 ["INT_ADD", "register:40f0:8", ["const:8ec474:8", "const:4:8"]]
- 008ec474 ["CALL", null, ["callee:0047ec3c:8"]]
+ 008ed420 ["INT_ADD", "register:40f0:8", ["const:8ed420:8", "const:4:8"]]
+ 008ed420 ["CALL", null, ["callee:0047ec3c:8"]]
- 008ec474 bytes 2a49ee97
+ 008ed420 bytes 0746ee97
- 008ec5b4 ["INT_ADD", "register:40f0:8", ["const:8ec5b4:8", "const:4:8"]]
- 008ec5b4 ["CALL", null, ["callee:0047ec3c:8"]]
+ 008ed560 ["INT_ADD", "register:40f0:8", ["const:8ed560:8", "const:4:8"]]
+ 008ed560 ["CALL", null, ["callee:0047ec3c:8"]]
- 008ec5b4 bytes da48ee97
+ 008ed560 bytes b745ee97
- 008ec894 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6e0:8"]]
- 008ec894 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008ed840 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6b0:8"]]
+ 008ed840 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008ec894 bytes 28e106b9
+ 008ed840 bytes 28b106b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46f6a2ab7621c86bba9c2328c4b25781"></a>

### [`008eca90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008eca90.md) → [`008eda3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ed/008eda3c.md) FUN_008eda3c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f7ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f7/008f7ecc.md) · 呼出先 7件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00468844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468844.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`008f8e78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f8/008f8e78.md) · 呼出先 7件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00468b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468b64.md) [`004692e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692e8.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 91.32% / 新版 91.32%

CFGの説明率　旧版 54.84% / 新版 54.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 2件, `unresolved_call_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008eda58",
      "incomplete_value": true,
      "site": "008eda58",
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
      "definition_site": "008ecaac",
      "incomplete_value": true,
      "site": "008ecaac",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008eda60",
      "incomplete_value": false,
      "site": "008eda74",
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
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ecab4",
      "incomplete_value": false,
      "site": "008ecac8",
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
            "const:f28:8"
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
      "definition_site": "008eda68",
      "incomplete_value": false,
      "site": "008eda74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ecabc",
      "incomplete_value": false,
      "site": "008ecac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
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
      "008eda54",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008eda60",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008eda68",
      "PARAM",
      [
        "storage",
        "00c859a0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008eda54",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "008eda60",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008eda68",
      "PARAM",
      [
        "storage",
        "00c86970",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ecac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008eca90.md#insn-008ecac8) · [`008ecc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008eca90.md#insn-008ecc5c) · [`008ecca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008eca90.md#insn-008ecca8)
- 新版 [`008eda74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ed/008eda3c.md#insn-008eda74) · [`008edc08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ed/008eda3c.md#insn-008edc08)

~~~diff
- 008ecac8 ["INT_ADD", "register:40f0:8", ["const:8ecac8:8", "const:4:8"]]
- 008ecac8 ["CALL", null, ["callee:00c596b0:8"]]
+ 008eda74 ["INT_ADD", "register:40f0:8", ["const:8eda74:8", "const:4:8"]]
+ 008eda74 ["CALL", null, ["callee:00c596b0:8"]]
- 008ecac8 bytes 06af0d94
+ 008eda74 bytes 0faf0d94
- 008ecc5c ["INT_ADD", "register:40f0:8", ["const:8ecc5c:8", "const:4:8"]]
- 008ecc5c ["CALL", null, ["ram:8c9dfc:8"]]
+ 008edc08 ["INT_ADD", "register:40f0:8", ["const:8edc08:8", "const:4:8"]]
+ 008edc08 ["CALL", null, ["ram:8cada8:8"]]
- 008ecc5c bytes 6874ff97
+ 008edc08 bytes 6874ff97
- 008ecca8 ["INT_ADD", "register:40f0:8", ["const:8ecca8:8", "const:4:8"]]
- 008ecca8 ["CALL", null, ["ram:8c9dfc:8"]]
- 008ecca8 bytes 5574ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eedbc6fa2348a0bb2a48bac9863c13af"></a>

### [`008eceb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008eceb4.md) → [`008ede60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ed/008ede60.md) FUN_008ede60

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f6b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f6b3c.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`008f7ae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f7/008f7ae8.md) · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 82.71% / 新版 82.71%

CFGの説明率　旧版 57.69% / 新版 57.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008ecf94"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008ecfbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008ecfcc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ecf94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008edf60"
      ]
    ],
    [
      "unmatched:008ecfbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008edf94"
      ]
    ],
    [
      "unmatched:008ecfc8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c54d90"
      ]
    ]
  ],
  "added": [
    [
      "008edf40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008edf60"
      ]
    ],
    [
      "008edf68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008edf94"
      ]
    ],
    [
      "008edf74",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c54d90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ecef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008eceb4.md#insn-008ecef4) · [`008ecf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008eceb4.md#insn-008ecf30) · [`008ecf68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ec/008eceb4.md#insn-008ecf68)

~~~diff
- 008ecef4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008ecef4 ["INT_ADD", "register:40f0:8", ["const:8ecef4:8", "const:4:8"]]
- 008ecef4 ["CALLIND", null, ["register:0:8"]]
- 008ecef4 bytes 00013fd6
- 008ecf30 ["COPY", "register:0:8", ["register:4040:8"]]
- 008ecf30 ["INT_ADD", "register:40f0:8", ["const:8ecf30:8", "const:4:8"]]
- 008ecf30 ["CALLIND", null, ["register:0:8"]]
- 008ecf30 bytes 00013fd6
- 008ecf68 ["COPY", "register:0:8", ["register:4040:8"]]
- 008ecf68 ["INT_ADD", "register:40f0:8", ["const:8ecf68:8", "const:4:8"]]
- 008ecf68 ["CALLIND", null, ["register:0:8"]]
- 008ecf68 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6967b65762f1937f785c4e93eeb12853"></a>

### [`008ed20c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ed/008ed20c.md) → [`008ee1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ee/008ee1b8.md) FUN_008ee1b8

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`008efa48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ef/008efa48.md) [`008f3098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f3/008f3098.md) [`008f66e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f66e8.md) · 呼出先 53件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046e7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e7b0.md) [`0046e7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e7c0.md) [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md)
- 新版 呼出元 3件 [`008f09f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f0/008f09f4.md) [`008f4044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f4/008f4044.md) [`008f7694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f7/008f7694.md) · 呼出先 53件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0046ead0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ead0.md) [`0046eae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046eae0.md) [`0046ecd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ecd0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.36% / 新版 83.36%

CFGの説明率　旧版 57.46% / 新版 57.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 33件, `call_target` 6件, `store_condition` 1件, `store_value` 4件, `unresolved_branch_alignment` 32件, `unresolved_call_alignment` 36件, `unresolved_store_alignment` 74件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ed20c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ed20c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ed210"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ed20c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ed210",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ed214",
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
      "008ee1b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008ee1bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008ee1c0",
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

- 旧版 [`008ed20c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ed/008ed20c.md#insn-008ed20c) · [`008ed210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ed/008ed20c.md#insn-008ed210) · [`008ed214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ed/008ed20c.md#insn-008ed214)

~~~diff
- 008ed20c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008ed20c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008ed20c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 008ed20c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008ed20c bytes fd7bbaa9
- 008ed210 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008ed210 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008ed210 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 008ed210 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ed210 bytes fc6f01a9
- 008ed214 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 008ed214 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 008ed214 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008ed214 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ed214 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3aaf8e6f348b315727e9a9adb9724dbf"></a>

### [`008ef95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ef/008ef95c.md) → [`008f0908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f0/008f0908.md) FUN_008f0908

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008f66e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f66e8.md) · 呼出先 5件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`006c0f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0f84.md) [`006c1f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c1/006c1f88.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md)
- 新版 呼出元 1件 [`008f7694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f7/008f7694.md) · 呼出先 5件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`006c1334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c1/006c1334.md) [`006c2338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c2/006c2338.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00c596b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.22% / 新版 93.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008f0928",
      "incomplete_value": true,
      "site": "008f0928",
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
      "definition_site": "008ef97c",
      "incomplete_value": true,
      "site": "008ef97c",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008f0930",
      "incomplete_value": false,
      "site": "008f0944",
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
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ef984",
      "incomplete_value": false,
      "site": "008ef998",
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
            "const:f28:8"
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
      "definition_site": "008f0938",
      "incomplete_value": false,
      "site": "008f0944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ef98c",
      "incomplete_value": false,
      "site": "008ef998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
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
      "008f0924",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008f0930",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f0938",
      "PARAM",
      [
        "storage",
        "00c859a0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008f0924",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "008f0930",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f0938",
      "PARAM",
      [
        "storage",
        "00c86970",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ef998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ef/008ef95c.md#insn-008ef998) · [`008ef970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ef/008ef95c.md#insn-008ef970) · [`008ef978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ef/008ef95c.md#insn-008ef978)
- 新版 [`008f0944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f0/008f0908.md#insn-008f0944) · [`008f091c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f0/008f0908.md#insn-008f091c) · [`008f0924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f0/008f0908.md#insn-008f0924)

~~~diff
- 008ef998 ["INT_ADD", "register:40f0:8", ["const:8ef998:8", "const:4:8"]]
- 008ef998 ["CALL", null, ["callee:00c596b0:8"]]
+ 008f0944 ["INT_ADD", "register:40f0:8", ["const:8f0944:8", "const:4:8"]]
+ 008f0944 ["CALL", null, ["callee:00c596b0:8"]]
- 008ef998 bytes 52a30d94
+ 008f0944 bytes 5ba30d94
- 008ef970 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 008f091c ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 008ef970 bytes a81d00b0
+ 008f091c bytes a81d00b0
- 008ef978 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 008ef978 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008f0924 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a38:8"]]
+ 008f0924 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008ef978 bytes 083d45f9
+ 008f0924 bytes 081d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-708154943f3925b8129fb69723947af5"></a>

### [`008efa48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ef/008efa48.md) → [`008f09f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f0/008f09f4.md) FUN_008f09f4

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f6794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f6794.md) · 呼出先 41件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046edcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046edcc.md) [`0046ee44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ee44.md)
- 新版 呼出元 1件 [`008f7740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f7/008f7740.md) · 呼出先 41件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046f0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f0ec.md) [`0046f164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f164.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.05% / 新版 90.05%

CFGの説明率　旧版 50.90% / 新版 51.20%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 22件, `call_target` 4件, `store_condition` 1件, `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008f0cf4",
      "incomplete_value": true,
      "site": "008f0cf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:110:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008efd48",
      "incomplete_value": true,
      "site": "008efd4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008efdc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008efe04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008efa98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f0d0c"
      ]
    ],
    [
      "unmatched:008efb50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f0bc8"
      ]
    ],
    [
      "unmatched:008efbac",
      "READ",
      [
        "storage",
        "00c9b5f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008f0a44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f0d0c"
      ]
    ],
    [
      "008f0afc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f0bc8"
      ]
    ],
    [
      "008f0b58",
      "READ",
      [
        "storage",
        "00c9c5c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008efa98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ef/008efa48.md#insn-008efa98) · [`008efb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ef/008efa48.md#insn-008efb50) · [`008efc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ef/008efa48.md#insn-008efc08)

~~~diff
- 008efa98 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008efa98 ["CBRANCH", null, ["local:b54:8", "tmp:0:1"]]
- 008efa98 bytes 4a160054
- 008efb50 ["CBRANCH", null, ["local:b29:8", "register:101:1"]]
- 008efb50 bytes 60060054
- 008efc08 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008efc08 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 008efc08 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 008efc08 ["CBRANCH", null, ["local:b31:8", "tmp:2:1"]]
- 008efc08 bytes 2c010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f48f58fc67b0898f98172b079d2b102"></a>

### [`008f0a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f0/008f0a28.md) → [`008f19d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f1/008f19d4.md) FUN_008f19d4

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f7ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f7/008f7ecc.md) · 呼出先 41件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md)
- 新版 呼出元 1件 [`008f8e78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f8/008f8e78.md) · 呼出先 41件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`00467ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467ec0.md) [`004682b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/004682b4.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.52% / 新版 78.52%

CFGの説明率　旧版 23.77% / 新版 23.40%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 69件, `call_target` 3件, `unresolved_branch_alignment` 18件, `unresolved_call_alignment` 46件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f0ee4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f0eec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f0ef0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008f1a14",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008f1a20",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f1a28",
      "PARAM",
      [
        "storage",
        "00c859a0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008f1a14",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "008f1a20",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f1a28",
      "PARAM",
      [
        "storage",
        "00c86970",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f0ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f0/008f0a28.md#insn-008f0ee4) · [`008f0eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f0/008f0a28.md#insn-008f0eec) · [`008f0ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f0/008f0a28.md#insn-008f0ef0)

~~~diff
- 008f0ee4 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 008f0ee4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:48:8"]]
- 008f0ee4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 008f0ee4 bytes e8230139
- 008f0eec ["COPY", "tmp:0:4", ["const:0:4"]]
- 008f0eec ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 008f0eec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:58:8"]]
- 008f0eec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 008f0eec bytes ff630139
- 008f0ef0 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 008f0ef0 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:49:8"]]
- 008f0ef0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008f0ef0 bytes ea9304f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7be398b5cf7e2d0434c9c31be82a360"></a>

### [`008f23cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f2/008f23cc.md) → [`008f3378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f3/008f3378.md) FUN_008f3378

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008eb570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008eb570.md) · 呼出先 12件 [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`006333b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00633/006333b4.md) [`00666360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00666/00666360.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008f8b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8b18.md)
- 新版 呼出元 1件 [`008ec51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ec51c.md) · 呼出先 12件 [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`00633764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00633/00633764.md) [`00666710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00666/00666710.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008f9ac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f9/008f9ac4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 59.65% / 新版 59.65%

CFGの説明率　旧版 23.33% / 新版 22.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f2504"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f2508"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f253c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008f2480",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f3448"
      ]
    ],
    [
      "008f3450",
      "DATA",
      [
        "storage",
        "003c92d0",
        null,
        "uleb128"
      ]
    ],
    [
      "008f3454",
      "DATA",
      [
        "storage",
        "003c92d8",
        null,
        "byte[11]"
      ]
    ]
  ],
  "added": [
    [
      "008f342c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f3448"
      ]
    ],
    [
      "008f3450",
      "DATA",
      [
        "storage",
        "003c92d0",
        null,
        "byte[11]"
      ]
    ],
    [
      "008f3454",
      "DATA",
      [
        "storage",
        "003c92d8",
        "fde_003c92d8",
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f2480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f2/008f23cc.md#insn-008f2480) · [`008f24b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f2/008f23cc.md#insn-008f24b0) · [`008f24c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f2/008f23cc.md#insn-008f24c0)

~~~diff
- 008f2480 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008f2480 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 008f2480 bytes e00000b5
- 008f24b0 ["CBRANCH", null, ["local:b1:8", "register:101:1"]]
- 008f24b0 bytes 20faff54
- 008f24c0 ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
- 008f24c0 bytes a0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b6a19fc07da56601b6ba1873ed9f669"></a>

### [`008f26e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f2/008f26e8.md) → [`008f3694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f3/008f3694.md) FUN_008f3694

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f5404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5404.md) · 呼出先 14件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00664800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664800.md) [`00664870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664870.md) [`00665cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00665/00665cbc.md) [`00665cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00665/00665cf8.md)
- 新版 呼出元 1件 [`008f63b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f6/008f63b0.md) · 呼出先 14件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00664bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664bb0.md) [`00664c20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664c20.md) [`0066606c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00666/0066606c.md) [`006660a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00666/006660a8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.80% / 新版 64.80%

CFGの説明率　旧版 14.20% / 新版 14.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_condition` 7件, `unresolved_branch_alignment` 29件, `unresolved_call_alignment` 13件, `unresolved_store_alignment` 44件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f26ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f26ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f26f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008f26ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008f26f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008f26f4",
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
      "008f3698",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008f369c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008f36a0",
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

- 旧版 [`008f26ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f2/008f26e8.md#insn-008f26ec) · [`008f26f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f2/008f26e8.md#insn-008f26f0) · [`008f26f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f2/008f26e8.md#insn-008f26f4)

~~~diff
- 008f26ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008f26ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008f26ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 008f26ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008f26ec bytes fd7b0ca9
- 008f26f0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008f26f0 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008f26f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 008f26f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008f26f0 bytes fc6f0da9
- 008f26f4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 008f26f4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 008f26f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 008f26f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008f26f4 bytes fa670ea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe9119dcd12ee2af3bf80e3071e8b7bf"></a>

### [`008f32b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f3/008f32b4.md) → [`008f4260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f4/008f4260.md) FUN_008f4260

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f6338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f6338.md) · 呼出先 16件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) [`00468d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468d48.md)
- 新版 呼出元 1件 [`008f72e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f7/008f72e4.md) · 呼出先 16件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`004682b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/004682b4.md) [`00469068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469068.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.20% / 新版 73.20%

CFGの説明率　旧版 26.60% / 新版 25.51%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 8件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f35a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f35a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f35b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008f428c",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008f429c",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f42a4",
      "PARAM",
      [
        "storage",
        "00c859a0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008f428c",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "008f429c",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f42a4",
      "PARAM",
      [
        "storage",
        "00c86970",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f3340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f3/008f32b4.md#insn-008f3340) · [`008f3558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f3/008f32b4.md#insn-008f3558) · [`008f3570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f3/008f32b4.md#insn-008f3570)

~~~diff
- 008f3340 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008f3340 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 008f3340 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 008f3340 ["CBRANCH", null, ["local:b13:8", "tmp:2:1"]]
- 008f3340 bytes ac080054
- 008f3558 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008f3558 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
- 008f3558 bytes e80000b5
- 008f3570 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008f3570 ["CBRANCH", null, ["local:b31:8", "tmp:0:1"]]
- 008f3570 bytes 480100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-086b771827da8484ed2604d53df34800"></a>

### [`008f5404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5404.md) → [`008f63b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f6/008f63b0.md) FUN_008f63b0

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008f66e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f66e8.md) · 呼出先 27件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00664800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664800.md)
- 新版 呼出元 1件 [`008f7694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f7/008f7694.md) · 呼出先 27件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00664bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664bb0.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008f69c0",
      "incomplete_value": false,
      "site": "008f69c0",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5a14",
      "incomplete_value": false,
      "site": "008f5a14",
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
            "const:6e0:8"
          ]
        ]
      ]
    },
    "ordinal": 109,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008f69e0",
      "incomplete_value": false,
      "site": "008f69e0",
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
            "const:6b4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5a34",
      "incomplete_value": false,
      "site": "008f5a34",
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
            "const:6e4:8"
          ]
        ]
      ]
    },
    "ordinal": 110,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008f63ec",
      "incomplete_value": true,
      "site": "008f63ec",
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
      "definition_site": "008f5440",
      "incomplete_value": true,
      "site": "008f5440",
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
      "008f63e8",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008f63f4",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f63fc",
      "PARAM",
      [
        "storage",
        "00c859a0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008f63e8",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "008f63f4",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f63fc",
      "PARAM",
      [
        "storage",
        "00c86970",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f545c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5404.md#insn-008f545c) · [`008f5784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5404.md#insn-008f5784) · [`008f57d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f5/008f5404.md#insn-008f57d4)
- 新版 [`008f6408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f6/008f63b0.md#insn-008f6408) · [`008f6730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f6/008f63b0.md#insn-008f6730) · [`008f6780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f6/008f63b0.md#insn-008f6780)

~~~diff
- 008f545c ["INT_ADD", "register:40f0:8", ["const:8f545c:8", "const:4:8"]]
- 008f545c ["CALL", null, ["callee:00c596b0:8"]]
+ 008f6408 ["INT_ADD", "register:40f0:8", ["const:8f6408:8", "const:4:8"]]
+ 008f6408 ["CALL", null, ["callee:00c596b0:8"]]
- 008f545c bytes a18c0d94
+ 008f6408 bytes aa8c0d94
- 008f5784 ["INT_ADD", "register:40f0:8", ["const:8f5784:8", "const:4:8"]]
- 008f5784 ["CALL", null, ["ram:665cbc:8"]]
+ 008f6730 ["INT_ADD", "register:40f0:8", ["const:8f6730:8", "const:4:8"]]
+ 008f6730 ["CALL", null, ["ram:66606c:8"]]
- 008f5784 bytes 4ec1f597
+ 008f6730 bytes 4fbef597
- 008f57d4 ["INT_ADD", "register:40f0:8", ["const:8f57d4:8", "const:4:8"]]
- 008f57d4 ["CALL", null, ["callee:008fac14:8"]]
+ 008f6780 ["INT_ADD", "register:40f0:8", ["const:8f6780:8", "const:4:8"]]
+ 008f6780 ["CALL", null, ["callee:008fac14:8"]]
- 008f57d4 bytes 25110094
+ 008f6780 bytes 25110094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71bc67a13dfeae103f4fb4bd3609cd63"></a>

### [`008f6338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f6338.md) → [`008f72e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f7/008f72e4.md) FUN_008f72e4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f7ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f7/008f7ecc.md) · 呼出先 14件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00468844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468844.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046969c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/0046969c.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md)
- 新版 呼出元 1件 [`008f8e78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f8/008f8e78.md) · 呼出先 14件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00468b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468b64.md) [`004692e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692e8.md) [`004699bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004699bc.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.78% / 新版 81.78%

CFGの説明率　旧版 43.64% / 新版 43.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 14件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f633c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f633c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f6340"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008f633c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008f6340",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008f6344",
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
      "008f72e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008f72ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008f72f0",
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

- 旧版 [`008f633c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f6338.md#insn-008f633c) · [`008f6340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f6338.md#insn-008f6340) · [`008f6344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f6338.md#insn-008f6344)

~~~diff
- 008f633c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 008f633c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5120:8"]]
- 008f633c ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:8:8"]]
- 008f633c ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5100:8"]]
- 008f633c bytes e923026d
- 008f6340 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008f6340 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008f6340 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 008f6340 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008f6340 bytes fd7b03a9
- 008f6344 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 008f6344 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 008f6344 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 008f6344 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008f6344 bytes fa6704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0651ba1f17d8247f821c78e824579c45"></a>

### [`008f66e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f66e8.md) → [`008f7694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f7/008f7694.md) FUN_008f7694

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f67b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f67b8.md) · 呼出先 7件 [`0066d11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066d/0066d11c.md) [`006c4214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c4/006c4214.md) [`006d18a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d1/006d18a0.md) [`008ed20c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ed/008ed20c.md) [`008ef95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ef/008ef95c.md)
- 新版 呼出元 1件 [`008f7764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f7/008f7764.md) · 呼出先 7件 [`0066d4cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0066d/0066d4cc.md) [`006c45c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c4/006c45c4.md) [`006d1c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d1/006d1c50.md) [`008ee1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ee/008ee1b8.md) [`008f0908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f0/008f0908.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 88.37% / 新版 88.37%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008f6700"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008f76ac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008f76b4",
      "incomplete_value": false,
      "site": "008f76c8",
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
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f6708",
      "incomplete_value": false,
      "site": "008f671c",
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
            "const:f28:8"
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
      "unmatched:008f66fc",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:008f6700",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f76d4"
      ]
    ],
    [
      "008f76b4",
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
      "008f76a8",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "008f76ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f76d4"
      ]
    ],
    [
      "008f76b4",
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

- 旧版 [`008f6700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f66e8.md#insn-008f6700) · [`008f671c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f66e8.md#insn-008f671c) · [`008f6778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f66e8.md#insn-008f6778)
- 新版 [`008f76c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f7/008f7694.md#insn-008f76c8) · [`008f7724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f7/008f7694.md#insn-008f7724)

~~~diff
- 008f6700 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008f6700 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 008f6700 bytes 480100b4
- 008f671c ["INT_ADD", "register:40f0:8", ["const:8f671c:8", "const:4:8"]]
- 008f671c ["CALL", null, ["callee:00c596b0:8"]]
+ 008f76c8 ["INT_ADD", "register:40f0:8", ["const:8f76c8:8", "const:4:8"]]
+ 008f76c8 ["CALL", null, ["callee:00c596b0:8"]]
- 008f671c bytes f1870d94
+ 008f76c8 bytes fa870d94
- 008f6778 ["INT_ADD", "register:40f0:8", ["const:8f6778:8", "const:4:8"]]
- 008f6778 ["CALL", null, ["ram:6d18a0:8"]]
+ 008f7724 ["INT_ADD", "register:40f0:8", ["const:8f7724:8", "const:4:8"]]
+ 008f7724 ["CALL", null, ["ram:6d1c50:8"]]
- 008f6778 bytes 4a6cf797
+ 008f7724 bytes 4b69f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23e62f02e5848cd462240edeb5a24674"></a>

### [`008f8a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8a40.md) → [`008f99ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f9/008f99ec.md) FUN_008f99ec

採用 · 移動量 `+0xfac` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008ebbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008ebbcc.md) [`008ebec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008eb/008ebec8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`008ecb78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ecb78.md) [`008ece74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ec/008ece74.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "008f99f8",
      "incomplete_value": false,
      "site": "008f99fc",
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
      "definition_site": "008f8a4c",
      "incomplete_value": false,
      "site": "008f8a50",
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
      "008f99f8",
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
      "008f99f8",
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

- 旧版 [`008f8a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8a40.md#insn-008f8a50) · [`008f8a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8a40.md#insn-008f8a48) · [`008f8a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8a40.md#insn-008f8a4c)
- 新版 [`008f99fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f9/008f99ec.md#insn-008f99fc) · [`008f99f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f9/008f99ec.md#insn-008f99f4) · [`008f99f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f9/008f99ec.md#insn-008f99f8)

~~~diff
- 008f8a50 ["INT_ADD", "register:40f0:8", ["const:8f8a50:8", "const:4:8"]]
- 008f8a50 ["CALL", null, ["callee:0043bad8:8"]]
+ 008f99fc ["INT_ADD", "register:40f0:8", ["const:8f99fc:8", "const:4:8"]]
+ 008f99fc ["CALL", null, ["callee:0043bad8:8"]]
- 008f8a50 bytes 5a0bed97
+ 008f99fc bytes 3708ed97
- 008f8a48 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 008f99f4 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 008f8a48 bytes e0cdfff0
+ 008f99f4 bytes e0cdfff0
- 008f8a4c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 008f8a4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008f8a4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008f8a4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008f99f8 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 008f99f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008f99f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008f99f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008f8a4c bytes 00303e91
+ 008f99f8 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ee93ae0b65588fe1634197f9c24c0c8"></a>

### [`008f8a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8a8c.md) → [`008f9a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f9/008f9a38.md) FUN_008f9a38

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
      "definition_site": "008f9a44",
      "incomplete_value": false,
      "site": "008f9a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f8a98",
      "incomplete_value": false,
      "site": "008f8a98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
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
      "008f9a44",
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
      "008f9a44",
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

- 旧版 [`008f8a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8a8c.md#insn-008f8a90) · [`008f8a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8a8c.md#insn-008f8a94)
- 新版 [`008f9a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f9/008f9a38.md#insn-008f9a3c) · [`008f9a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f9/008f9a38.md#insn-008f9a40)

~~~diff
- 008f8a90 ["COPY", "register:4048:8", ["const:c85000:8"]]
+ 008f9a3c ["COPY", "register:4048:8", ["const:c86000:8"]]
- 008f8a90 bytes 691c00b0
+ 008f9a3c bytes 691c00b0
- 008f8a94 ["COPY", "tmp:0:8", ["const:9c8:8"]]
- 008f8a94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008f8a94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008f8a94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008f9a40 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 008f9a40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008f9a40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008f9a40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008f8a94 bytes 29212791
+ 008f9a40 bytes 29612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d16d12c1223d559b3656b239037e2a9f"></a>

### [`008f8aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8aa8.md) → [`008f9a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f9/008f9a54.md) FUN_008f9a54

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
      "site": "008f9a78",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008f8acc",
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
      "008f9a78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "008f9a78",
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

- 旧版 [`008f8acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8aa8.md#insn-008f8acc) · [`008f8ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8aa8.md#insn-008f8ad8)
- 新版 [`008f9a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f9/008f9a54.md#insn-008f9a78) · [`008f9a84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f9/008f9a54.md#insn-008f9a84)

~~~diff
- 008f8acc ["INT_ADD", "register:40f0:8", ["const:8f8acc:8", "const:4:8"]]
- 008f8acc ["CALL", null, ["ram:47ad34:8"]]
+ 008f9a78 ["INT_ADD", "register:40f0:8", ["const:8f9a78:8", "const:4:8"]]
+ 008f9a78 ["CALL", null, ["ram:47b054:8"]]
- 008f8acc bytes 9a08ee97
+ 008f9a78 bytes 7705ee97
- 008f8ad8 ["INT_ADD", "register:40f0:8", ["const:8f8ad8:8", "const:4:8"]]
- 008f8ad8 ["CALL", null, ["callee:0047d134:8"]]
+ 008f9a84 ["INT_ADD", "register:40f0:8", ["const:8f9a84:8", "const:4:8"]]
+ 008f9a84 ["CALL", null, ["callee:0047d134:8"]]
- 008f8ad8 bytes cf10ee97
+ 008f9a84 bytes ac0dee97
~~~


<a id="compare-87473e08c6d1ddb5c462f9eaf3fbd4cc"></a>

### [`008f8b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8b18.md) → [`008f9ac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f9/008f9ac4.md) FUN_008f9ac4

採用 · 移動量 `+0xfac` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008f23cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f2/008f23cc.md) [`008f8b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8b18.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 2件 [`008f3378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f3/008f3378.md) [`008f9ac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f9/008f9ac4.md) · 呼出先 22件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.50% / 新版 95.50%

CFGの説明率　旧版 78.68% / 新版 78.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f8b44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f8b50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f90d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008f8b44",
      "WRITE",
      [
        "storage",
        "Stack[-0xe0]",
        null,
        null
      ]
    ],
    [
      "unmatched:008f8b50",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:008f8b70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f9cf4"
      ]
    ]
  ],
  "added": [
    [
      "008f9af0",
      "WRITE",
      [
        "storage",
        "Stack[-0xe0]",
        null,
        null
      ]
    ],
    [
      "008f9afc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "008f9b1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008f9cf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f8b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8b18.md#insn-008f8b44) · [`008f8b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8b18.md#insn-008f8b50) · [`008f8b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8b18.md#insn-008f8b70)

~~~diff
- 008f8b44 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008f8b44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4018:8"]]
- 008f8b44 bytes e30b00f9
- 008f8b50 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008f8b50 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008f8b50 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008f8b50 bytes a9831ff8
- 008f8b70 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 008f8b70 ["CBRANCH", null, ["local:b29:8", "tmp:0:1"]]
- 008f8b70 bytes c30e0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-052022230683147878c108fa8c110c82"></a>

### [`008f9330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9330.md) → [`008fa2dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fa/008fa2dc.md) FUN_008fa2dc

採用 · 移動量 `+0xfac` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008f8b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f8/008f8b18.md) [`008f9330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9330.md) · 呼出先 23件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 2件 [`008f9ac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008f9/008f9ac4.md) [`008fa2dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fa/008fa2dc.md) · 呼出先 23件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008fa434",
      "incomplete_value": false,
      "site": "008fa43c",
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
            "const:62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f9488",
      "incomplete_value": false,
      "site": "008f9490",
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
            "const:f93:8"
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
      "definition_site": "008fa4f0",
      "incomplete_value": false,
      "site": "008fa4f8",
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
            "const:ef6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f9544",
      "incomplete_value": false,
      "site": "008f954c",
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
            "const:e27:8"
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
      "definition_site": "008fa508",
      "incomplete_value": false,
      "site": "008fa514",
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
            "const:f73:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f955c",
      "incomplete_value": false,
      "site": "008f9568",
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
            "const:f29:8"
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
      "008fa434",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "008fa4f0",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "008fa508",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008fa434",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "008fa4f0",
      "PARAM",
      [
        "storage",
        "002b5ef6",
        null,
        null
      ]
    ],
    [
      "008fa508",
      "PARAM",
      [
        "storage",
        "002c0f73",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f9490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9330.md#insn-008f9490) · [`008f954c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9330.md#insn-008f954c) · [`008f9568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9330.md#insn-008f9568)
- 新版 [`008fa43c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fa/008fa2dc.md#insn-008fa43c) · [`008fa4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fa/008fa2dc.md#insn-008fa4f8) · [`008fa514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fa/008fa2dc.md#insn-008fa514)

~~~diff
- 008f9490 ["INT_ADD", "register:40f0:8", ["const:8f9490:8", "const:4:8"]]
- 008f9490 ["CALL", null, ["callee:004421f4:8"]]
+ 008fa43c ["INT_ADD", "register:40f0:8", ["const:8fa43c:8", "const:4:8"]]
+ 008fa43c ["CALL", null, ["callee:004421f4:8"]]
- 008f9490 bytes 9122ed97
+ 008fa43c bytes 6e1fed97
- 008f954c ["INT_ADD", "register:40f0:8", ["const:8f954c:8", "const:4:8"]]
- 008f954c ["CALL", null, ["callee:004421f4:8"]]
+ 008fa4f8 ["INT_ADD", "register:40f0:8", ["const:8fa4f8:8", "const:4:8"]]
+ 008fa4f8 ["CALL", null, ["callee:004421f4:8"]]
- 008f954c bytes 6222ed97
+ 008fa4f8 bytes 3f1fed97
- 008f9568 ["INT_ADD", "register:40f0:8", ["const:8f9568:8", "const:4:8"]]
- 008f9568 ["CALL", null, ["callee:00442b54:8"]]
+ 008fa514 ["INT_ADD", "register:40f0:8", ["const:8fa514:8", "const:4:8"]]
+ 008fa514 ["CALL", null, ["callee:00442b54:8"]]
- 008f9568 bytes b324ed97
+ 008fa514 bytes 9021ed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-066514c286475c750497eaa1afe8f426"></a>

### [`008f9df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9df0.md) → [`008fad9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fa/008fad9c.md) FUN_008fad9c

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
      "definition_site": "008fadb0",
      "incomplete_value": false,
      "site": "008fadb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c86000:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f9e04",
      "incomplete_value": false,
      "site": "008f9e08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c85000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "008fadb4",
      "DATA",
      [
        "storage",
        "00c85a48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fadb4",
      "DATA",
      [
        "storage",
        "00c86a18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f9dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9df0.md#insn-008f9dfc) · [`008f9e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9df0.md#insn-008f9e00) · [`008f9e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9df0.md#insn-008f9e04)
- 新版 [`008fada8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fa/008fad9c.md#insn-008fada8) · [`008fadac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fa/008fad9c.md#insn-008fadac) · [`008fadb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fa/008fad9c.md#insn-008fadb0)

~~~diff
- 008f9dfc ["INT_ADD", "register:40f0:8", ["const:8f9dfc:8", "const:4:8"]]
- 008f9dfc ["CALL", null, ["callee:00c58f30:8"]]
+ 008fada8 ["INT_ADD", "register:40f0:8", ["const:8fada8:8", "const:4:8"]]
+ 008fada8 ["CALL", null, ["callee:00c58f30:8"]]
- 008f9dfc bytes 59780d94
+ 008fada8 bytes 62780d94
- 008f9e00 ["COPY", "register:4040:8", ["const:c85000:8"]]
+ 008fadac ["COPY", "register:4040:8", ["const:c86000:8"]]
- 008f9e00 bytes 681c0090
+ 008fadac bytes 681c0090
- 008f9e04 ["COPY", "tmp:0:8", ["const:a48:8"]]
- 008f9e04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f9e04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f9e04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fadb0 ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 008fadb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fadb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fadb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f9e04 bytes 08212991
+ 008fadb0 bytes 08612891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b027dccc42996d30d1eafe7831d8c5b7"></a>

### [`008fa160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa160.md) → [`008fb10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fb/008fb10c.md) FUN_008fb10c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`008f9e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9e5c.md) [`008fa2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa2d0.md) [`008fa598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa598.md) · 呼出先 3件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008f9c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9c68.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 3件 [`008fae08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fa/008fae08.md) [`008fb27c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fb/008fb27c.md) [`008fb544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fb/008fb544.md) · 呼出先 3件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008fac14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fa/008fac14.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 69.57% / 新版 69.57%

CFGの説明率　旧版 14.29% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008fa1b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008fa264"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008fb160"
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
      "unmatched:008fa1b0",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "unmatched:008fa1b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008fb184",
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
      "008fb15c",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ],
    [
      "008fb160",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008fb184",
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

- 旧版 [`008fa1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa160.md#insn-008fa1b4) · [`008fa1b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa160.md#insn-008fa1b8) · [`008fa214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa160.md#insn-008fa214)
- 新版 [`008fb164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fb/008fb10c.md#insn-008fb164) · [`008fb1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fb/008fb10c.md#insn-008fb1c0)

~~~diff
- 008fa1b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008fa1b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 008fa1b4 bytes f70b00f9
- 008fa1b8 ["INT_ADD", "register:40f0:8", ["const:8fa1b8:8", "const:4:8"]]
- 008fa1b8 ["CALL", null, ["callee:008fac14:8"]]
+ 008fb164 ["INT_ADD", "register:40f0:8", ["const:8fb164:8", "const:4:8"]]
+ 008fb164 ["CALL", null, ["callee:008fac14:8"]]
- 008fa1b8 bytes acfeff97
+ 008fb164 bytes acfeff97
- 008fa214 ["INT_ADD", "register:40f0:8", ["const:8fa214:8", "const:4:8"]]
- 008fa214 ["CALL", null, ["callee:008fac14:8"]]
+ 008fb1c0 ["INT_ADD", "register:40f0:8", ["const:8fb1c0:8", "const:4:8"]]
+ 008fb1c0 ["CALL", null, ["callee:008fac14:8"]]
- 008fa214 bytes 95feff97
+ 008fb1c0 bytes 95feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc18ea30f570a4804b9167948e91c3f4"></a>

### [`008fa2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa2d0.md) → [`008fb27c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fb/008fb27c.md) FUN_008fb27c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f9e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9e5c.md) · 呼出先 2件 [`008f9e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f9/008f9e5c.md) [`008fa160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa160.md)
- 新版 呼出元 1件 [`008fae08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fa/008fae08.md) · 呼出先 2件 [`008fae08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fa/008fae08.md) [`008fb10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fb/008fb10c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.89% / 新版 89.89%

CFGの説明率　旧版 31.08% / 新版 32.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_condition` 1件, `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008fa2d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008fa2d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008fa2d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008fa2d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008fa2d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008fa2dc",
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
      "008fb280",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008fb284",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008fb288",
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

- 旧版 [`008fa2d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa2d0.md#insn-008fa2d4) · [`008fa2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa2d0.md#insn-008fa2d8) · [`008fa2dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fa/008fa2d0.md#insn-008fa2dc)

~~~diff
- 008fa2d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008fa2d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008fa2d4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 008fa2d4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008fa2d4 bytes fd7bbaa9
- 008fa2d8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008fa2d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 008fa2d8 bytes fb0b00f9
- 008fa2dc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 008fa2dc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 008fa2dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008fa2dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008fa2dc bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

