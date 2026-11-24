# v16.0.2 → v16.0.3 · 命令位置の検査未完了 (8)

[一覧の目次](README.md)

<a id="compare-396c4fafb8322631f6755923acc77a13"></a>

### [`0086ac08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ac08.md) → [`0086bbb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086bbb4.md) FUN_0086bbb4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0086ab90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ab90.md) [`009e12cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e12cc.md) [`009e23e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e2/009e23e0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`0086bb3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086bb3c.md) [`009e2278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e2/009e2278.md) [`009e338c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e3/009e338c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 40.00% / 新版 51.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086ad6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0086bd18"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0086ac90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0086ac90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086bc4c"
      ]
    ],
    [
      "unmatched:0086acc0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086bc44"
      ]
    ],
    [
      "unmatched:0086acf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086bcc4"
      ]
    ]
  ],
  "added": [
    [
      "0086bc3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086bc4c"
      ]
    ],
    [
      "0086bc6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086bc44"
      ]
    ],
    [
      "0086bc9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086bcc4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086ac90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ac08.md#insn-0086ac90) · [`0086acc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ac08.md#insn-0086acc0) · [`0086acf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ac08.md#insn-0086acf0)

~~~diff
- 0086ac90 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0086ac90 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 0086ac90 bytes 81000054
- 0086acc0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0086acc0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 0086acc0 bytes c1feff54
- 0086acf0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0086acf0 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 0086acf0 bytes 43010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d164c6635371b8533f5d3ec2fc6dec8a"></a>

### [`0086ada8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ada8.md) → [`0086bd54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086bd54.md) FUN_0086bd54

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00849c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00849/00849c68.md) [`0086ada8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ada8.md) [`009e03d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e03d0.md) · 呼出先 2件 [`0086ada8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ada8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 4件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) [`0084ac14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084a/0084ac14.md) [`0086bd54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086bd54.md) [`009e137c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e1/009e137c.md) · 呼出先 2件 [`0086bd54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086bd54.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 77.27% / 新版 85.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086adac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086adac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086adb0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0086adac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0086adb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0086adb4",
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
      "0086bd58",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0086bd5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0086bd60",
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

- 旧版 [`0086adac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ada8.md#insn-0086adac) · [`0086adb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ada8.md#insn-0086adb0) · [`0086adb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ada8.md#insn-0086adb4)

~~~diff
- 0086adac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0086adac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0086adac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 0086adac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0086adac bytes fd7bbda9
- 0086adb0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0086adb0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0086adb0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0086adb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0086adb0 bytes f65701a9
- 0086adb4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0086adb4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0086adb4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0086adb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0086adb4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fec16ed0585fe601d72e6b643c09e61"></a>

### [`0086ae7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ae7c.md) → [`0086be28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086be28.md) FUN_0086be28

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086ae88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086ae90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086ae90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0086ae88",
      "DATA",
      [
        "storage",
        "00c7f0a0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0086ae8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086be60"
      ]
    ],
    [
      "unmatched:0086ae90",
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
      "0086be34",
      "DATA",
      [
        "storage",
        "00c80070",
        null,
        "undefined *"
      ]
    ],
    [
      "0086be38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086be60"
      ]
    ],
    [
      "0086be3c",
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

- 旧版 [`0086ae88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ae7c.md#insn-0086ae88) · [`0086ae8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ae7c.md#insn-0086ae8c) · [`0086ae90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ae7c.md#insn-0086ae90)

~~~diff
- 0086ae88 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0086ae88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0086ae88 bytes 090000f9
- 0086ae8c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0086ae8c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 0086ae8c bytes 480100b4
- 0086ae90 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0086ae90 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0086ae90 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0086ae90 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0086ae90 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4455432779f46e031aacd32276e6fbde"></a>

### [`0086af08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086af08.md) → [`0086beb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086b/0086beb4.md) FUN_0086beb4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086af14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086af14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086af18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0086af14",
      "DATA",
      [
        "storage",
        "00c7f0a0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0086af1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086bee4"
      ]
    ],
    [
      "unmatched:0086af20",
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
      "0086bec0",
      "DATA",
      [
        "storage",
        "00c80070",
        null,
        "undefined *"
      ]
    ],
    [
      "0086bec8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086bee4"
      ]
    ],
    [
      "0086becc",
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

- 旧版 [`0086af14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086af08.md#insn-0086af14) · [`0086af18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086af08.md#insn-0086af18) · [`0086af1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086af08.md#insn-0086af1c)

~~~diff
- 0086af14 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0086af14 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 0086af14 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 0086af14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0086af14 bytes 292800a9
- 0086af18 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:10:8"]]
- 0086af18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0086af18 bytes 280800f9
- 0086af1c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0086af1c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0086af1c bytes e80000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-083b8738f0c0030a27180dfa310b35e3"></a>

### [`0086b138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b138.md) → [`0086c0e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086c/0086c0e4.md) FUN_0086c0e4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

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
      "site": "0086b15c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086b15c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0086c108"
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
      "unmatched:0086b15c",
      "DATA",
      [
        "storage",
        "00c7f120",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086c108",
      "DATA",
      [
        "storage",
        "00c800f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086b15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b138.md#insn-0086b15c) · [`0086b14c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b138.md#insn-0086b14c)
- 新版 [`0086c108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086c/0086c0e4.md#insn-0086c108) · [`0086c0f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086c/0086c0e4.md#insn-0086c0f8)

~~~diff
- 0086b15c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0086b15c ["COPY", "tmp:1:8", ["register:4050:8"]]
- 0086b15c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0086b15c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0086b15c bytes 092800a9
+ 0086c108 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0086c108 ["COPY", "tmp:1:8", ["register:4050:8"]]
+ 0086c108 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 0086c108 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0086c108 bytes 092800a9
- 0086b14c ["INT_ADD", "register:40f0:8", ["const:86b14c:8", "const:4:8"]]
- 0086b14c ["CALL", null, ["callee:00c58f30:8"]]
+ 0086c0f8 ["INT_ADD", "register:40f0:8", ["const:86c0f8:8", "const:4:8"]]
+ 0086c0f8 ["CALL", null, ["callee:00c58f30:8"]]
- 0086b14c bytes 85b30f94
+ 0086c0f8 bytes 8eb30f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-147a9752c2884c191f478b16ab6c8d17"></a>

### [`0086b22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b22c.md) → [`0086c1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086c/0086c1d8.md) FUN_0086c1d8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0086b1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b1fc.md) · 呼出先 7件 [`0048aa90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048aa90.md) [`00498724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00498/00498724.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`0086c1a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086c/0086c1a8.md) · 呼出先 7件 [`0048adb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048adb0.md) [`00498a44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00498/00498a44.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 23.81% / 新版 26.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086b230"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086b230"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086b234"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0086b230",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0086b234",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0086b238",
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
      "0086c1dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0086c1e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0086c1e4",
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

- 旧版 [`0086b230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b22c.md#insn-0086b230) · [`0086b234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b22c.md#insn-0086b234) · [`0086b238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086b/0086b22c.md#insn-0086b238)

~~~diff
- 0086b230 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0086b230 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0086b230 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0086b230 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0086b230 bytes fd7b03a9
- 0086b234 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0086b234 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0086b234 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0086b234 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0086b234 bytes f65704a9
- 0086b238 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0086b238 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0086b238 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 0086b238 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0086b238 bytes f44f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a16ea338e7b56301452d5ad95bd15dc"></a>

### [`0086d2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d2fc.md) → [`0086e2a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e2a8.md) FUN_0086e2a8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 75.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0086d320"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "0086e2cc"
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
      "unmatched:0086d320",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "0086e2cc",
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

- 旧版 [`0086d320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d2fc.md#insn-0086d320) · [`0086d304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d2fc.md#insn-0086d304)
- 新版 [`0086e2cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e2a8.md#insn-0086e2cc) · [`0086e2b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e2a8.md#insn-0086e2b0)

~~~diff
- 0086d320 ["INT_ADD", "register:40f0:8", ["const:86d320:8", "const:4:8"]]
- 0086d320 ["CALL", null, ["ram:47ad34:8"]]
- 0086d320 bytes 8536f097
+ 0086e2cc ["INT_ADD", "register:40f0:8", ["const:86e2cc:8", "const:4:8"]]
+ 0086e2cc ["CALL", null, ["ram:47b054:8"]]
+ 0086e2cc bytes 6233f097
- 0086d304 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0086d304 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0086e2b0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0086e2b0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0086d304 bytes e1010054
+ 0086e2b0 bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11e119ec9debfed3fc7747358518a6d0"></a>

### [`0086d4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d4f8.md) → [`0086e4a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e4a4.md) FUN_0086e4a4

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
      "site": "0086d51c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086d51c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0086e4c8"
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
      "unmatched:0086d51c",
      "DATA",
      [
        "storage",
        "00c7f420",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0086d520",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0086d524",
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
      "0086e4c8",
      "DATA",
      [
        "storage",
        "00c803f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0086e4cc",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0086e4d0",
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

- 旧版 [`0086d51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d4f8.md#insn-0086d51c) · [`0086d528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d4f8.md#insn-0086d528)
- 新版 [`0086e4c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e4a4.md#insn-0086e4c8)

~~~diff
- 0086d51c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0086d51c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0086d51c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0086d51c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0086d51c bytes 082400a9
- 0086d528 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0086d528 ["RETURN", null, ["register:0:8"]]
- 0086d528 bytes c0035fd6
+ 0086e4c8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0086e4c8 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 0086e4c8 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 0086e4c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0086e4c8 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ad1c1fee9482adb754227f2568e31f4"></a>

### [`0086d52c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d52c.md) → [`0086e4d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e4d8.md) FUN_0086e4d8

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
      "site": "0086d538"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086d538"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0086e4e4"
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
      "unmatched:0086d538",
      "DATA",
      [
        "storage",
        "00c7f420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086e4e4",
      "DATA",
      [
        "storage",
        "00c803f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d52c.md#insn-0086d538) · [`0086d53c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d52c.md#insn-0086d53c)
- 新版 [`0086e4e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e4d8.md#insn-0086e4e4)

~~~diff
- 0086d538 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0086d538 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0086d538 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 0086d538 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0086d538 bytes 292000a9
- 0086d53c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0086d53c ["RETURN", null, ["register:0:8"]]
- 0086d53c bytes c0035fd6
+ 0086e4e4 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0086e4e4 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 0086e4e4 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 0086e4e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0086e4e4 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2154cd1ec2862236b8b2f696be5c5df9"></a>

### [`0086d548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d548.md) → [`0086e4f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e4f4.md) FUN_0086e4f4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 75.00% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0086d56c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "0086e518"
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
      "unmatched:0086d56c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "0086e518",
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

- 旧版 [`0086d56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d548.md#insn-0086d56c) · [`0086d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d548.md#insn-0086d550)
- 新版 [`0086e518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e4f4.md#insn-0086e518) · [`0086e4fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e4f4.md#insn-0086e4fc)

~~~diff
- 0086d56c ["INT_ADD", "register:40f0:8", ["const:86d56c:8", "const:4:8"]]
- 0086d56c ["CALL", null, ["ram:47ad34:8"]]
- 0086d56c bytes f235f097
+ 0086e518 ["INT_ADD", "register:40f0:8", ["const:86e518:8", "const:4:8"]]
+ 0086e518 ["CALL", null, ["ram:47b054:8"]]
+ 0086e518 bytes cf32f097
- 0086d550 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0086d550 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0086e4fc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0086e4fc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 0086d550 bytes e1010054
+ 0086e4fc bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73b405928e3fa9ba37f590ee4cc55566"></a>

### [`0086d5bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d5bc.md) → [`0086e568`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e568.md) FUN_0086e568

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
      "site": "0086d5bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086d5bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086d5c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0086d5bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0086d5c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0086d5e0",
      "DATA",
      [
        "storage",
        "00c7f4a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086e568",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0086e56c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0086e58c",
      "DATA",
      [
        "storage",
        "00c80470",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d5bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d5bc.md#insn-0086d5bc) · [`0086d5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d5bc.md#insn-0086d5c0) · [`0086d5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d5bc.md#insn-0086d5e0)

~~~diff
- 0086d5bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0086d5bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0086d5bc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0086d5bc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0086d5bc bytes fd7bbea9
- 0086d5c0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0086d5c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0086d5c0 bytes f30b00f9
- 0086d5e0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0086d5e0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0086d5e0 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0086d5e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0086d5e0 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f2cb8016d9273c4f69bb57f86c9d793"></a>

### [`0086d5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d5f0.md) → [`0086e59c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e59c.md) FUN_0086e59c

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
      "site": "0086d5fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086d5fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0086e5a8"
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
      "unmatched:0086d5fc",
      "DATA",
      [
        "storage",
        "00c7f4a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086e5a8",
      "DATA",
      [
        "storage",
        "00c80470",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d5f0.md#insn-0086d5fc) · [`0086d600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d5f0.md#insn-0086d600)
- 新版 [`0086e5a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e59c.md#insn-0086e5a8)

~~~diff
- 0086d5fc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0086d5fc ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0086d5fc ["COPY", "tmp:2:8", ["register:4008:8"]]
- 0086d5fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0086d5fc bytes 292000a9
- 0086d600 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0086d600 ["RETURN", null, ["register:0:8"]]
- 0086d600 bytes c0035fd6
+ 0086e5a8 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0086e5a8 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 0086e5a8 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 0086e5a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0086e5a8 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98ca55367ff4e37c1c3a04a089210cb9"></a>

### [`0086d60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d60c.md) → [`0086e5b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e5b8.md) FUN_0086e5b8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 20.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0086d614"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0086e5c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0086d630"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0086d614",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086e5fc"
      ]
    ],
    [
      "unmatched:0086d630",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "0086e5c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0086e5fc"
      ]
    ],
    [
      "0086e5dc",
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

- 旧版 [`0086d614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d60c.md#insn-0086d614) · [`0086d630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d60c.md#insn-0086d630)
- 新版 [`0086e5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e5b8.md#insn-0086e5c0)

~~~diff
- 0086d614 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0086d614 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0086d614 bytes e1010054
- 0086d630 ["INT_ADD", "register:40f0:8", ["const:86d630:8", "const:4:8"]]
- 0086d630 ["CALL", null, ["ram:47ad34:8"]]
- 0086d630 bytes c135f097
+ 0086e5c0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0086e5c0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 0086e5c0 bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-555d203987b0e25f58a36cbe01a01005"></a>

### [`0086d684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d684.md) → [`0086e630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e630.md) FUN_0086e630

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
      "site": "0086d6a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086d6a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0086e654"
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
      "unmatched:0086d6a8",
      "DATA",
      [
        "storage",
        "00c7f520",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0086d6ac",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0086d6b0",
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
      "0086e654",
      "DATA",
      [
        "storage",
        "00c804f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0086e658",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0086e65c",
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

- 旧版 [`0086d6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d684.md#insn-0086d6a8) · [`0086d6b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d684.md#insn-0086d6b4)
- 新版 [`0086e654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e630.md#insn-0086e654)

~~~diff
- 0086d6a8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0086d6a8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0086d6a8 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0086d6a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0086d6a8 bytes 082400a9
- 0086d6b4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0086d6b4 ["RETURN", null, ["register:0:8"]]
- 0086d6b4 bytes c0035fd6
+ 0086e654 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0086e654 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 0086e654 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 0086e654 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0086e654 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01f21d76384b620c334d66a542aed96c"></a>

### [`0086d6b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d6b8.md) → [`0086e664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e664.md) FUN_0086e664

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
      "site": "0086d6c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086d6c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0086e670"
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
      "unmatched:0086d6c4",
      "DATA",
      [
        "storage",
        "00c7f520",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086e670",
      "DATA",
      [
        "storage",
        "00c804f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086d6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d6b8.md#insn-0086d6c4) · [`0086d6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d6b8.md#insn-0086d6c8)
- 新版 [`0086e670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086e664.md#insn-0086e670)

~~~diff
- 0086d6c4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0086d6c4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0086d6c4 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 0086d6c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0086d6c4 bytes 292000a9
- 0086d6c8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0086d6c8 ["RETURN", null, ["register:0:8"]]
- 0086d6c8 bytes c0035fd6
+ 0086e670 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0086e670 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 0086e670 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 0086e670 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0086e670 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-512abbe6857dc9f20bed86981509e6bf"></a>

### [`0086dcbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086dcbc.md) → [`0086ec68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086ec68.md) FUN_0086ec68

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`004647dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/004647dc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00464afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00464/00464afc.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

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
      "site": "0086dcc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0086ec74"
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
      "unmatched:0086dcc8",
      "DATA",
      [
        "storage",
        "00c7f620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0086ec74",
      "DATA",
      [
        "storage",
        "00c805f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086dcc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086dcbc.md#insn-0086dcc8) · [`0086dcbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086dcbc.md#insn-0086dcbc)
- 新版 [`0086ec74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086e/0086ec68.md#insn-0086ec74)

~~~diff
- 0086dcc8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0086dcc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0086dcc8 bytes 090000f9
+ 0086ec74 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 0086ec74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0086ec74 bytes 090000f9
- 0086dcbc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d0:8"]]
- 0086dcbc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 0086dcbc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 0086dcbc bytes 08404339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06ad282786987484a71aebff6385bafc"></a>

### [`0086f924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086f/0086f924.md) → [`008708d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00870/008708d0.md) FUN_008708d0

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
      "site": "0086f948"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086f948"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008708f4"
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
      "unmatched:0086f948",
      "DATA",
      [
        "storage",
        "00c7f6c0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0086f94c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0086f950",
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
      "008708f4",
      "DATA",
      [
        "storage",
        "00c80690",
        null,
        "undefined *"
      ]
    ],
    [
      "008708f8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008708fc",
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

- 旧版 [`0086f948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086f/0086f924.md#insn-0086f948) · [`0086f954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086f/0086f924.md#insn-0086f954)
- 新版 [`008708f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00870/008708d0.md#insn-008708f4)

~~~diff
- 0086f948 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0086f948 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0086f948 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0086f948 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0086f948 bytes 082400a9
- 0086f954 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0086f954 ["RETURN", null, ["register:0:8"]]
- 0086f954 bytes c0035fd6
+ 008708f4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008708f4 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 008708f4 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 008708f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008708f4 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7989eb5ffaae8fee7d095163bf360ce9"></a>

### [`0086f958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086f/0086f958.md) → [`00870904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00870/00870904.md) FUN_00870904

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "0086f964"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0086f964"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00870910"
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
      "unmatched:0086f964",
      "DATA",
      [
        "storage",
        "00c7f6c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00870910",
      "DATA",
      [
        "storage",
        "00c80690",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0086f964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086f/0086f958.md#insn-0086f964) · [`0086f968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086f/0086f958.md#insn-0086f968)
- 新版 [`00870910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00870/00870904.md#insn-00870910)

~~~diff
- 0086f964 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0086f964 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0086f964 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 0086f964 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0086f964 bytes 292000a9
- 0086f968 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0086f968 ["RETURN", null, ["register:0:8"]]
- 0086f968 bytes c0035fd6
+ 00870910 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00870910 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00870910 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00870910 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00870910 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c29e16133c67eb1b2df0c3c7221e31c"></a>

### [`00870d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/00870d00.md) → [`00871cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00871/00871cac.md) FUN_00871cac

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0085d54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085d/0085d54c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`0085e4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085e/0085e4f8.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "site": "00870d00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00870d00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00871cac"
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
      "unmatched:00870d00",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00870d0c",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00870d10",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043bad8"
      ]
    ]
  ],
  "added": [
    [
      "00871cac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00871cb8",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ],
    [
      "00871cbc",
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

- 旧版 [`00870d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/00870d00.md#insn-00870d00) · [`00870d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00870/00870d00.md#insn-00870d10)
- 新版 [`00871cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00871/00871cac.md#insn-00871cac)

~~~diff
- 00870d00 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00870d00 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00870d00 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00870d00 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00870d00 bytes fd7bbfa9
- 00870d10 ["INT_ADD", "register:40f0:8", ["const:870d10:8", "const:4:8"]]
- 00870d10 ["CALL", null, ["callee:0043bad8:8"]]
- 00870d10 bytes aa2aef97
+ 00871cac ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00871cac ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00871cac ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00871cac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00871cac bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb2b6e3ebf4fa67dffde6e8a4c01524c"></a>

### [`00871990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871990.md) → [`0087293c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00872/0087293c.md) FUN_0087293c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "008719b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008719b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00872960"
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
      "unmatched:008719b4",
      "DATA",
      [
        "storage",
        "00c7fa10",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008719b8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008719bc",
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
      "00872960",
      "DATA",
      [
        "storage",
        "00c809e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00872964",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00872968",
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

- 旧版 [`008719b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871990.md#insn-008719b4) · [`008719c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871990.md#insn-008719c0)
- 新版 [`00872960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00872/0087293c.md#insn-00872960)

~~~diff
- 008719b4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008719b4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008719b4 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008719b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008719b4 bytes 082400a9
- 008719c0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008719c0 ["RETURN", null, ["register:0:8"]]
- 008719c0 bytes c0035fd6
+ 00872960 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00872960 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00872960 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00872960 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00872960 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d56ba68815401d1b55a76ff4de770353"></a>

### [`00871bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871bc8.md) → [`00872b74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00872/00872b74.md) FUN_00872b74

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00871bd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00871bd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00872b80"
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
      "unmatched:00871bd4",
      "DATA",
      [
        "storage",
        "00c7faa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872b80",
      "DATA",
      [
        "storage",
        "00c80a70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871bc8.md#insn-00871bd4) · [`00871bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871bc8.md#insn-00871bd8)
- 新版 [`00872b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00872/00872b74.md#insn-00872b80)

~~~diff
- 00871bd4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00871bd4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00871bd4 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00871bd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00871bd4 bytes 292000a9
- 00871bd8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00871bd8 ["RETURN", null, ["register:0:8"]]
- 00871bd8 bytes c0035fd6
+ 00872b80 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00872b80 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00872b80 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00872b80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00872b80 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6493fef8830fca87d8c91ec7b2d54cf1"></a>

### [`00871ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871ff4.md) → [`00872fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00872/00872fa0.md) FUN_00872fa0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 50.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00871ffc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00872fa8"
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
      "unmatched:00871ffc",
      "DATA",
      [
        "storage",
        "00c7fb30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00872fa8",
      "DATA",
      [
        "storage",
        "00c80b00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00871ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871ff4.md#insn-00871ffc) · [`00871ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871ff4.md#insn-00871ff4)
- 新版 [`00872fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00872/00872fa0.md#insn-00872fa8)

~~~diff
- 00871ffc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00871ffc ["COPY", "tmp:1:8", ["register:4008:8"]]
- 00871ffc ["INT_ADD", "register:4008:8", ["register:4008:8", "const:8:8"]]
- 00871ffc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00871ffc bytes 288400f8
+ 00872fa8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00872fa8 ["COPY", "tmp:1:8", ["register:4008:8"]]
+ 00872fa8 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:8:8"]]
+ 00872fa8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00872fa8 bytes 288400f8
- 00871ff4 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00871ff4 bytes 682000d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f12ef181fafd1b7072568b28714c3a3c"></a>

### [`00872150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872150.md) → [`008730fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/008730fc.md) FUN_008730fc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

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
      "site": "0087215c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00873108"
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
      "unmatched:0087215c",
      "DATA",
      [
        "storage",
        "00c7fbb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00873108",
      "DATA",
      [
        "storage",
        "00c80b80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087215c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872150.md#insn-0087215c) · [`00872150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872150.md#insn-00872150)
- 新版 [`00873108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/008730fc.md#insn-00873108)

~~~diff
- 0087215c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0087215c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0087215c bytes 090000f9
+ 00873108 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00873108 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00873108 bytes 090000f9
- 00872150 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00872150 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00872150 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00872150 bytes 08204039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94b8adb25c56f326e4924862db668703"></a>

### [`00872390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872390.md) → [`0087333c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/0087333c.md) FUN_0087333c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 41.67% / 新版 41.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00872390"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00872390"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00872394"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00872390",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00872394",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008723a8",
      "DATA",
      [
        "storage",
        "00c7fc48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0087333c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00873340",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00873354",
      "DATA",
      [
        "storage",
        "00c80c18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00872390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872390.md#insn-00872390) · [`00872394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872390.md#insn-00872394) · [`008723a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872390.md#insn-008723a8)

~~~diff
- 00872390 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00872390 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00872390 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00872390 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00872390 bytes fd7bbea9
- 00872394 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00872394 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00872394 bytes f30b00f9
- 008723a8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008723a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008723a8 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3962afbbb5ea9e8bc2510b5894708e7"></a>

### [`008730a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008730a0.md) → [`0087404c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/0087404c.md) FUN_0087404c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008730a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00874054"
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
      "unmatched:008730a8",
      "DATA",
      [
        "storage",
        "00c7fce0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:008730ac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58f40"
      ]
    ]
  ],
  "added": [
    [
      "00874054",
      "DATA",
      [
        "storage",
        "00c80cb0",
        null,
        "pointer"
      ]
    ],
    [
      "00874058",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58f40"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008730a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008730a0.md#insn-008730a8) · [`008730a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008730a0.md#insn-008730a0)
- 新版 [`00874054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/0087404c.md#insn-00874054)

~~~diff
- 008730a8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008730a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008730a8 bytes 080000f9
+ 00874054 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00874054 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00874054 bytes 080000f9
- 008730a0 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 008730a0 bytes 68200090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f392fccfb326b41ab0dacccd91ff5f6"></a>

### [`00875048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875048.md) → [`00875ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875ff4.md) FUN_00875ff4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00875064"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00876010"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00875068"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00875064",
      "DATA",
      [
        "storage",
        "00c7ff10",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00875068",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00876040"
      ]
    ]
  ],
  "added": [
    [
      "00876010",
      "DATA",
      [
        "storage",
        "00c80ee0",
        null,
        "undefined *"
      ]
    ],
    [
      "00876014",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00876040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875048.md#insn-00875064) · [`00875068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875048.md#insn-00875068)
- 新版 [`00876010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875ff4.md#insn-00876010)

~~~diff
- 00875064 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00875064 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00875064 bytes 080000f9
- 00875068 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00875068 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00875068 bytes 740100b4
+ 00876010 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00876010 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00876010 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d46387acb4a57d6cc33b143f60d57bff"></a>

### [`00875674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875674.md) → [`00876620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876620.md) FUN_00876620

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00875434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875434.md) · 呼出先 2件 [`00875910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875910.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`008763e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008763e0.md) · 呼出先 2件 [`008768bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008768bc.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 84.43% / 新版 84.43%

CFGの説明率　旧版 72.09% / 新版 60.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008756e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008756f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008757d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008756fc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c590f0"
      ]
    ],
    [
      "unmatched:00875888",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c590f0"
      ]
    ],
    [
      "unmatched:008758f0",
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
      "008766a8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c590f0"
      ]
    ],
    [
      "00876834",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c590f0"
      ]
    ],
    [
      "0087689c",
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

- 旧版 [`008756e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875674.md#insn-008756e8) · [`008756f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875674.md#insn-008756f4) · [`008756fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875674.md#insn-008756fc)

~~~diff
- 008756e8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008756e8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 008756e8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 008756e8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:1:8"]]
- 008756e8 bytes 1815959a
- 008756f4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 008756f4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008756f4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 008756f4 ["COPY", "tmp:1:8", ["register:40e0:8"]]
- 008756f4 bytes 7a329c9a
- 008756fc ["INT_ADD", "register:40f0:8", ["const:8756fc:8", "const:4:8"]]
- 008756fc ["CALL", null, ["callee:00c590f0:8"]]
- 008756fc bytes 898a0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-859d50f8b33c0c49cd0b92744579f8b5"></a>

### [`00875910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875910.md) → [`008768bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008768bc.md) FUN_008768bc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00875674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875674.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00876620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876620.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 71.43% / 新版 76.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0087595c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00876908"
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
      "unmatched:0087595c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008769a0"
      ]
    ]
  ],
  "added": [
    [
      "00876908",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008769a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087595c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875910.md#insn-0087595c) · [`00875934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875910.md#insn-00875934)
- 新版 [`00876908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008768bc.md#insn-00876908) · [`008768e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008768bc.md#insn-008768e0)

~~~diff
- 0087595c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0087595c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 0087595c bytes c80400b4
+ 00876908 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00876908 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00876908 bytes c80400b4
- 00875934 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00875934 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 008768e0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 008768e0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00875934 bytes e80500b4
+ 008768e0 bytes e80500b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dc2877da25fe8d19b83f50ea852138d"></a>

### [`00875a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875a4c.md) → [`008769f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008769f8.md) FUN_008769f8

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
      "site": "00875a58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00875a58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00876a04"
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
      "unmatched:00875a58",
      "DATA",
      [
        "storage",
        "00c7ff90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00876a04",
      "DATA",
      [
        "storage",
        "00c80f60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875a4c.md#insn-00875a58) · [`00875a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875a4c.md#insn-00875a5c)
- 新版 [`00876a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008769f8.md#insn-00876a04)

~~~diff
- 00875a58 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00875a58 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00875a58 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00875a58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00875a58 bytes 292000a9
- 00875a5c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00875a5c ["RETURN", null, ["register:0:8"]]
- 00875a5c bytes c0035fd6
+ 00876a04 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00876a04 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00876a04 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00876a04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00876a04 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b39141d97861a21b67ba15c1c823e24a"></a>

### [`00875fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875fd4.md) → [`00876f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876f80.md) FUN_00876f80

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00875fe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00875fe4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00876f8c"
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
      "unmatched:00875fe0",
      "DATA",
      [
        "storage",
        "00c80080",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00876f8c",
      "DATA",
      [
        "storage",
        "00c81050",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875fd4.md#insn-00875fe0) · [`00875fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875fd4.md#insn-00875fe4)
- 新版 [`00876f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876f80.md#insn-00876f8c)

~~~diff
- 00875fe0 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00875fe0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00875fe0 bytes 290000f9
- 00875fe4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 00875fe4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00875fe4 bytes 2080803c
+ 00876f8c ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00876f8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00876f8c bytes 290000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b07d47b70f4781d2fc3e5c2dfc5e80e9"></a>

### [`00878310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878310.md) → [`008792bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00879/008792bc.md) FUN_008792bc

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0076820c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/0076820c.md) [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) [`00881dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/00881dd4.md) · 呼出先 8件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00b3c760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c760.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 4件 [`007685e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007685e8.md) [`00852508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852508.md) [`0088036c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/0088036c.md) [`00882d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/00882d80.md) · 呼出先 8件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00b3d754`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3d754.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.52% / 新版 95.52%

CFGの説明率　旧版 52.63% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087839c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00879348"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008783e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087839c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008783e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008793f0"
      ]
    ]
  ],
  "added": [
    [
      "00879348",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00879390",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008793f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087839c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878310.md#insn-0087839c) · [`008783e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878310.md#insn-008783e4)
- 新版 [`00879348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00879/008792bc.md#insn-00879348)

~~~diff
- 0087839c ["COPY", "tmp:0:8", ["register:8:8"]]
- 0087839c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0087839c bytes e80300f9
- 008783e4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008783e4 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 008783e4 bytes 01030054
+ 00879348 ["COPY", "tmp:0:8", ["register:8:8"]]
+ 00879348 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00879348 bytes e80300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc0ce8de06a483b226b425c23f0f248e"></a>

### [`0087b5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b5fc.md) → [`0087c5a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c5a8.md) FUN_0087c5a8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 52.94% / 新版 52.94%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087b614"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0087c5c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0087b618"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087b614",
      "DATA",
      [
        "storage",
        "00c80338",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0087b618",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087c5d4"
      ]
    ]
  ],
  "added": [
    [
      "0087c5c0",
      "DATA",
      [
        "storage",
        "00c81308",
        null,
        "undefined *"
      ]
    ],
    [
      "0087c5c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087c5d4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b5fc.md#insn-0087b614) · [`0087b618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b5fc.md#insn-0087b618)
- 新版 [`0087c5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c5a8.md#insn-0087c5c0)

~~~diff
- 0087b614 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0087b614 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 0087b614 bytes 0a0100f9
- 0087b618 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 0087b618 bytes 80000054
+ 0087c5c0 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0087c5c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 0087c5c0 bytes 0a0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79035d779170ebff541b0c64de5433ff"></a>

### [`0087b868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b868.md) → [`0087c814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c814.md) FUN_0087c814

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 66.67% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087b868"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087b868"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087b86c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087b868",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087b86c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087b890",
      "DATA",
      [
        "storage",
        "00c803c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c814",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0087c818",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0087c83c",
      "DATA",
      [
        "storage",
        "00c81398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b868.md#insn-0087b868) · [`0087b86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b868.md#insn-0087b86c) · [`0087b890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b868.md#insn-0087b890)

~~~diff
- 0087b868 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087b868 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087b868 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0087b868 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0087b868 bytes fd7bbea9
- 0087b86c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0087b86c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0087b86c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0087b86c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087b86c bytes f44f01a9
- 0087b890 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0087b890 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0087b890 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3d6eb899312a3a3904059b2b5fca9e7"></a>

### [`0087c1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c1d0.md) → [`0087d17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d17c.md) FUN_0087d17c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0087aa68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087aa68.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0087ba14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087b/0087ba14.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0087c1ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0087d198"
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
      "unmatched:0087c1ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087d1a8"
      ]
    ]
  ],
  "added": [
    [
      "0087d198",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087d1a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c1d0.md#insn-0087c1ec) · [`0087c1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c1d0.md#insn-0087c1e8)
- 新版 [`0087d198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d17c.md#insn-0087d198)

~~~diff
- 0087c1ec ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 0087c1ec bytes 80000054
+ 0087d198 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 0087d198 bytes 80000054
- 0087c1e8 ["INT_LESSEQUAL", "register:105:1", ["register:4048:8", "register:4000:8"]]
- 0087c1e8 ["INT_SBORROW", "register:106:1", ["register:4000:8", "register:4048:8"]]
- 0087c1e8 ["INT_SUB", "tmp:0:8", ["register:4000:8", "register:4048:8"]]
- 0087c1e8 ["INT_SLESS", "register:107:1", ["tmp:0:8", "const:0:8"]]
- 0087c1e8 bytes 1f0009eb
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16b7dc00f2201a184f2da26eba61ad76"></a>

### [`0087c220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c220.md) → [`0087d1cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d1cc.md) FUN_0087d1cc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087c224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c220.md#insn-0087c224) · [`0087c230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c220.md#insn-0087c230) · [`0087c23c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c220.md#insn-0087c23c)
- 新版 [`0087d1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d1cc.md#insn-0087d1d0) · [`0087d1e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d1cc.md#insn-0087d1e8)

~~~diff
- 0087c224 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0087c224 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 0087d1d0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 0087d1d0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 0087c224 bytes 800000b4
+ 0087d1d0 bytes 800000b4
- 0087c230 ["COPY", "register:0:8", ["register:4010:8"]]
- 0087c230 ["BRANCHIND", null, ["register:0:8"]]
- 0087c230 bytes 40001fd6
- 0087c23c ["INT_ADD", "register:40f0:8", ["const:87c23c:8", "const:4:8"]]
- 0087c23c ["CALL", null, ["callee:0045a0d4:8"]]
+ 0087d1e8 ["INT_ADD", "register:40f0:8", ["const:87d1e8:8", "const:4:8"]]
+ 0087d1e8 ["CALL", null, ["callee:0045a0d4:8"]]
- 0087c23c bytes de76ef97
+ 0087d1e8 bytes bb73ef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-553adb716f49e441861ca0abda5114dc"></a>

### [`0087c838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c838.md) → [`0087d7e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d7e4.md) FUN_0087d7e4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0087b148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b148.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0087c0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c0f4.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087c838"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087c838"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087c83c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087c838",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087c83c",
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
      "0087d7e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0087d7e8",
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

- 旧版 [`0087c838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c838.md#insn-0087c838) · [`0087c83c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c838.md#insn-0087c83c)
- 新版 [`0087d7e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d7e4.md#insn-0087d7e4)

~~~diff
- 0087c838 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087c838 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087c838 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0087c838 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0087c838 bytes fd7bbea9
- 0087c83c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0087c83c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0087c83c bytes f30b00f9
+ 0087d7e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0087d7e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0087d7e4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 0087d7e4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0087d7e4 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e57970f2d3b4fc3b32ce175505b239b2"></a>

### [`0087c8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c8d0.md) → [`0087d87c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d87c.md) FUN_0087d87c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 36.11% / 新版 36.11%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087c8d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087c8d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087c8d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087c8d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087c8d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087c8f8",
      "DATA",
      [
        "storage",
        "00c805e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087d87c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0087d880",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0087d8a4",
      "DATA",
      [
        "storage",
        "00c815b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c8d0.md#insn-0087c8d0) · [`0087c8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c8d0.md#insn-0087c8d4) · [`0087c8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c8d0.md#insn-0087c8f8)

~~~diff
- 0087c8d0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087c8d0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087c8d0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0087c8d0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0087c8d0 bytes fd7bbea9
- 0087c8d4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0087c8d4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0087c8d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0087c8d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087c8d4 bytes f44f01a9
- 0087c8f8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0087c8f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0087c8f8 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9fb536a2c0321b906b95de8dac3c5cf"></a>

### [`0087c960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c960.md) → [`0087d90c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d90c.md) FUN_0087d90c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 31.25% / 新版 29.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087c960"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087c960"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087c964"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087c960",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087c964",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087c988",
      "DATA",
      [
        "storage",
        "00c805e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087d90c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0087d910",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0087d934",
      "DATA",
      [
        "storage",
        "00c815b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c960.md#insn-0087c960) · [`0087c964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c960.md#insn-0087c964) · [`0087c988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c960.md#insn-0087c988)

~~~diff
- 0087c960 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087c960 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087c960 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0087c960 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0087c960 bytes fd7bbea9
- 0087c964 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0087c964 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0087c964 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0087c964 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087c964 bytes f44f01a9
- 0087c988 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0087c988 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0087c988 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec289e08dfcca5afa929453d16694d06"></a>

### [`0087cc84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087cc84.md) → [`0087dc30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087dc30.md) FUN_0087dc30

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0087acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087acb0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0087bc5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087b/0087bc5c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 85.71% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087cc84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087cc84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087cc88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087cc84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087cc88",
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
      "0087dc30",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0087dc34",
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

- 旧版 [`0087cc84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087cc84.md#insn-0087cc84) · [`0087cc88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087cc84.md#insn-0087cc88)
- 新版 [`0087dc30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087dc30.md#insn-0087dc30)

~~~diff
- 0087cc84 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087cc84 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087cc84 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0087cc84 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0087cc84 bytes fd7bbea9
- 0087cc88 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0087cc88 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0087cc88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0087cc88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087cc88 bytes f44f01a9
+ 0087dc30 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0087dc30 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0087dc30 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 0087dc30 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0087dc30 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b708d3edc25178e9df9c7b5a796cf60"></a>

### [`0087d2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d2f8.md) → [`0087e2a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087e/0087e2a4.md) FUN_0087e2a4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00493e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493e08.md) [`00575d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00575/00575d54.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00494128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494128.md) [`00576074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576074.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.22% / 新版 82.22%

CFGの説明率　旧版 50.00% / 新版 46.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087d2fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087d2fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087d300"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087d2fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087d300",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087d304",
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
      "0087e2a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0087e2ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0087e2b0",
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

- 旧版 [`0087d2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d2f8.md#insn-0087d2fc) · [`0087d300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d2f8.md#insn-0087d300) · [`0087d304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d2f8.md#insn-0087d304)

~~~diff
- 0087d2fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087d2fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087d2fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0087d2fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087d2fc bytes fd7b02a9
- 0087d300 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 0087d300 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0087d300 bytes f51b00f9
- 0087d304 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0087d304 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0087d304 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0087d304 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087d304 bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9ca314d1d859b5649ec1c0683f82a18"></a>

### [`0087d564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d564.md) → [`0087e510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087e/0087e510.md) FUN_0087e510

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008613e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00861/008613e0.md) · 呼出先 6件 [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5aa20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa20.md)
- 新版 呼出元 1件 [`0086238c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00862/0086238c.md) · 呼出先 6件 [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5b9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b9f0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "0087d5a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0087e554"
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
      "unmatched:0087d5a8",
      "DATA",
      [
        "storage",
        "00c80678",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0087d5ac",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087d5b0",
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
      "0087e554",
      "DATA",
      [
        "storage",
        "00c81648",
        null,
        "undefined *"
      ]
    ],
    [
      "0087e558",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0087e55c",
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

- 旧版 [`0087d5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d564.md#insn-0087d5a8) · [`0087d570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d564.md#insn-0087d570)
- 新版 [`0087e554`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087e/0087e510.md#insn-0087e554) · [`0087e51c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087e/0087e510.md#insn-0087e51c)

~~~diff
- 0087d5a8 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 0087d5a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0087d5a8 bytes 280000f9
+ 0087e554 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 0087e554 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0087e554 bytes 280000f9
- 0087d570 ["INT_ADD", "register:40f0:8", ["const:87d570:8", "const:4:8"]]
- 0087d570 ["CALL", null, ["callee:005891cc:8"]]
+ 0087e51c ["INT_ADD", "register:40f0:8", ["const:87e51c:8", "const:4:8"]]
+ 0087e51c ["CALL", null, ["callee:005891cc:8"]]
- 0087d570 bytes 4f2ef497
+ 0087e51c bytes 2c2bf497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-049e95e9bbb28177dd348b03c68c0c27"></a>

### [`0087d948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d948.md) → [`0087e8f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087e/0087e8f4.md) FUN_0087e8f4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0087eb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eb18.md) · 呼出先 5件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58300.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5abc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5abc0.md) [`00c5abd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5abd0.md)
- 新版 呼出元 1件 [`0087fac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fac4.md) · 呼出先 5件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c592d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c592d0.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5bb90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb90.md) [`00c5bba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bba0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 16.67% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0087d968"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0087e914"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0087d9c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087d968",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087e970"
      ]
    ]
  ],
  "added": [
    [
      "0087e914",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087e970"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087d968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d948.md#insn-0087d968) · [`0087d9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d948.md#insn-0087d9c0)
- 新版 [`0087e914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087e/0087e8f4.md#insn-0087e914)

~~~diff
- 0087d968 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 0087d968 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 0087d968 bytes e90200b4
- 0087d9c0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0087d9c0 ["RETURN", null, ["register:0:8"]]
- 0087d9c0 bytes c0035fd6
+ 0087e914 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 0087e914 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 0087e914 bytes e90200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4bdcb0630c0598c9aa2ea723eb9d666"></a>

### [`0087dc7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087dc7c.md) → [`0087ec28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087e/0087ec28.md) FUN_0087ec28

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0087dd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087dd68.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0087ed14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087e/0087ed14.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 28.81% / 新版 28.81%

CFGの説明率　旧版 10.00% / 新版 10.34%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0087dca4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0087dcbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0087dcd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0087ec34",
      "READ",
      [
        "storage",
        "01123928",
        null,
        "undefined1"
      ]
    ],
    [
      "0087ec38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0087dc9c"
      ]
    ],
    [
      "unmatched:0087dc94",
      "READ",
      [
        "storage",
        "01123938",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0087ec34",
      "READ",
      [
        "storage",
        "011248e8",
        null,
        "undefined1"
      ]
    ],
    [
      "0087ec38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087ec48"
      ]
    ],
    [
      "0087ec40",
      "READ",
      [
        "storage",
        "011248f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087dc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087dc7c.md#insn-0087dc98) · [`0087dca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087dc7c.md#insn-0087dca4) · [`0087dcb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087dc7c.md#insn-0087dcb0)

~~~diff
- 0087dc98 ["INT_ADD", "register:40f0:8", ["const:87dc98:8", "const:4:8"]]
- 0087dc98 ["CALL", null, ["callee:00c58f50:8"]]
- 0087dc98 bytes ba680f94
- 0087dca4 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 0087dca4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0087dca4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0087dca4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 0087dca4 bytes 88000036
- 0087dcb0 ["INT_ADD", "register:40f0:8", ["const:87dcb0:8", "const:4:8"]]
- 0087dcb0 ["CALL", null, ["callee:00c58f50:8"]]
- 0087dcb0 bytes b4680f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f268e93c65f211abdbea3e066bab77f0"></a>

### [`0087e62c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e62c.md) → [`0087f5d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087f5d8.md) FUN_0087f5d8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 7件 [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md) [`00879ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879ce0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00852508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852508.md) · 呼出先 7件 [`005891cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005891cc.md) [`005894bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/005894bc.md) [`00589bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589bb0.md) [`0087ac8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087a/0087ac8c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.84% / 新版 91.84%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087e65c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0087f608"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0087e6d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087e65c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087e6d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087f6d0"
      ]
    ]
  ],
  "added": [
    [
      "0087f608",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "0087f67c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087f6d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087e65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e62c.md#insn-0087e65c) · [`0087e6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087e62c.md#insn-0087e6d0)
- 新版 [`0087f608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087f5d8.md#insn-0087f608)

~~~diff
- 0087e65c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0087e65c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0087e65c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0087e65c bytes a8831ff8
- 0087e6d0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0087e6d0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0087e6d0 bytes a1020054
+ 0087f608 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0087f608 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
+ 0087f608 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 0087f608 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69372cfb6362dea5e6132096f47e2b94"></a>

### [`0087ebc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087ebc4.md) → [`0087fb70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fb70.md) FUN_0087fb70

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087ebc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087ebc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087ebc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087ebc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087ebc8",
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
      "0087fb70",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0087fb74",
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

- 旧版 [`0087ebc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087ebc4.md#insn-0087ebc4) · [`0087ebc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087ebc4.md#insn-0087ebc8)
- 新版 [`0087fb70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087fb70.md#insn-0087fb70)

~~~diff
- 0087ebc4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087ebc4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087ebc4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0087ebc4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0087ebc4 bytes fd7bbea9
- 0087ebc8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0087ebc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0087ebc8 bytes f30b00f9
+ 0087fb70 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0087fb70 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0087fb70 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 0087fb70 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0087fb70 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46933e3bd4f96cb532919eded8f9940f"></a>

### [`0087efd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087efd4.md) → [`0087ff80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087f/0087ff80.md) FUN_0087ff80

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 87.10% / 新版 87.10%

CFGの説明率　旧版 35.71% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0087efe8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0087ff94"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0087f018"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087efe8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087fff0"
      ]
    ],
    [
      "unmatched:0087f018",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0087ff94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087fff0"
      ]
    ],
    [
      "0087ffc4",
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

- 旧版 [`0087efe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087efd4.md#insn-0087efe8) · [`0087f018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087efd4.md#insn-0087f018) · [`0087f04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087efd4.md#insn-0087f04c)

~~~diff
- 0087efe8 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 0087efe8 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 0087efe8 bytes f30200b4
- 0087f018 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087f018 ["INT_ADD", "register:40f0:8", ["const:87f018:8", "const:4:8"]]
- 0087f018 ["CALLIND", null, ["register:0:8"]]
- 0087f018 bytes 00013fd6
- 0087f04c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0087f04c ["RETURN", null, ["register:0:8"]]
- 0087f04c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf94e8a0e3415d896b155d8dd7b9f91b"></a>

### [`0087f060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f060.md) → [`0088000c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00880/0088000c.md) FUN_0088000c

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
      "site": "0087f060"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087f060"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087f064"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087f060",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087f064",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087f078",
      "DATA",
      [
        "storage",
        "00c806d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0088000c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00880010",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00880024",
      "DATA",
      [
        "storage",
        "00c816a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087f060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f060.md#insn-0087f060) · [`0087f064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f060.md#insn-0087f064) · [`0087f078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f060.md#insn-0087f078)

~~~diff
- 0087f060 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087f060 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087f060 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0087f060 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0087f060 bytes fd7bbea9
- 0087f064 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0087f064 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0087f064 bytes f30b00f9
- 0087f078 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0087f078 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0087f078 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54c1b09652dd77a9ba19d66e0f419495"></a>

### [`0088106c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/0088106c.md) → [`00882018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/00882018.md) FUN_00882018

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 75.00% / 新版 81.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008810a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "0088204c"
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
      "unmatched:008810a0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0088204c",
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

- 旧版 [`008810a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/0088106c.md#insn-008810a0) · [`00881080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/0088106c.md#insn-00881080)
- 新版 [`0088204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/00882018.md#insn-0088204c) · [`0088202c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/00882018.md#insn-0088202c)

~~~diff
- 008810a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008810a0 ["INT_ADD", "register:40f0:8", ["const:8810a0:8", "const:4:8"]]
- 008810a0 ["CALLIND", null, ["register:0:8"]]
- 008810a0 bytes 00013fd6
+ 0088204c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088204c ["INT_ADD", "register:40f0:8", ["const:88204c:8", "const:4:8"]]
+ 0088204c ["CALLIND", null, ["register:0:8"]]
+ 0088204c bytes 00013fd6
- 00881080 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00881080 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 0088202c ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 0088202c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00881080 bytes 740100b4
+ 0088202c bytes 740100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b0e554987950e81c08a86d70c43c316"></a>

### [`008813a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008813a4.md) → [`00882350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/00882350.md) FUN_00882350

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 54.55% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008813a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008813a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008813a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008813a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008813a8",
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
      "00882350",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00882354",
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

- 旧版 [`008813a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008813a4.md#insn-008813a4) · [`008813a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008813a4.md#insn-008813a8)
- 新版 [`00882350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/00882350.md#insn-00882350)

~~~diff
- 008813a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008813a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008813a4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008813a4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008813a4 bytes fd7bbea9
- 008813a8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008813a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008813a8 bytes f30b00f9
+ 00882350 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00882350 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00882350 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00882350 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00882350 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5369d744ecfe2d1db34c16d105def9b6"></a>

### [`0088218c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/0088218c.md) → [`00883138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883138.md) FUN_00883138

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 1件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 60.00% / 新版 60.00%

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
      "site": "008821b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0088315c"
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
      "unmatched:008821b0",
      "DATA",
      [
        "storage",
        "003c7788",
        null,
        "dword"
      ]
    ],
    [
      "unmatched:008821bc",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008821c0",
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
      "0088315c",
      "DATA",
      [
        "storage",
        "003c7788",
        null,
        "dword"
      ]
    ],
    [
      "00883168",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0088316c",
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

- 旧版 [`008821b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/0088218c.md#insn-008821b0) · [`0088219c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/0088218c.md#insn-0088219c)
- 新版 [`0088315c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883138.md#insn-0088315c) · [`00883148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883138.md#insn-00883148)

~~~diff
- 008821b0 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 008821b0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 008821b0 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 008821b0 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 008821b0 bytes 0a6828b8
+ 0088315c ["COPY", "tmp:0:4", ["register:4050:4"]]
+ 0088315c ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 0088315c ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 0088315c ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 0088315c bytes 0a6828b8
- 0088219c ["INT_ADD", "register:40f0:8", ["const:88219c:8", "const:4:8"]]
- 0088219c ["CALL", null, ["callee:008524fc:8"]]
+ 00883148 ["INT_ADD", "register:40f0:8", ["const:883148:8", "const:4:8"]]
+ 00883148 ["CALL", null, ["callee:008524fc:8"]]
- 0088219c bytes ed3cff97
+ 00883148 bytes ed3cff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-339ee022d0e5af3f40638e360d93798f"></a>

### [`00882538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882538.md) → [`008834e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/008834e4.md) FUN_008834e4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.21% / 新版 86.21%

CFGの説明率　旧版 33.33% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00882564"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00883510"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008825a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00882564",
      "DATA",
      [
        "storage",
        "00c807e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883510",
      "DATA",
      [
        "storage",
        "00c817b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882538.md#insn-00882564) · [`008825a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882538.md#insn-008825a8)
- 新版 [`00883510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/008834e4.md#insn-00883510)

~~~diff
- 00882564 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00882564 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 00882564 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 00882564 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00882564 bytes 280401f8
- 008825a8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008825a8 ["RETURN", null, ["register:0:8"]]
- 008825a8 bytes c0035fd6
+ 00883510 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00883510 ["COPY", "tmp:1:8", ["register:4008:8"]]
+ 00883510 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
+ 00883510 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00883510 bytes 280401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f021ae9bdbfb42d764a9c8f383fb78cb"></a>

### [`00882700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882700.md) → [`008836ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/008836ac.md) FUN_008836ac

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00882718"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008836c4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00882720"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00882718",
      "DATA",
      [
        "storage",
        "00c80868",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0088271c",
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
      "008836c4",
      "DATA",
      [
        "storage",
        "00c81838",
        null,
        "undefined *"
      ]
    ],
    [
      "008836c8",
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

- 旧版 [`00882718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882700.md#insn-00882718) · [`00882720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882700.md#insn-00882720)
- 新版 [`008836c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/008836ac.md#insn-008836c4)

~~~diff
- 00882718 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00882718 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00882718 bytes 080000f9
- 00882720 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00882720 ["RETURN", null, ["register:0:8"]]
- 00882720 bytes c0035fd6
+ 008836c4 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008836c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008836c4 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8344ba5cbecfa3b06102e15c55783a22"></a>

### [`00882724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882724.md) → [`008836d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/008836d0.md) FUN_008836d0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

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
      "site": "0088272c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008836d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00882730"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088272c",
      "DATA",
      [
        "storage",
        "00c80868",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008836d8",
      "DATA",
      [
        "storage",
        "00c81838",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088272c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882724.md#insn-0088272c) · [`00882730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882724.md#insn-00882730)
- 新版 [`008836d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/008836d0.md#insn-008836d8)

~~~diff
- 0088272c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 0088272c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0088272c bytes 280000f9
- 00882730 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00882730 ["RETURN", null, ["register:0:8"]]
- 00882730 bytes c0035fd6
+ 008836d8 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 008836d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008836d8 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eedf1f184bac4053c66a288038671fb5"></a>

### [`008829f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008829f8.md) → [`008839a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/008839a4.md) FUN_008839a4

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00442e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442e98.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`00493288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493288.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 88.57% / 新版 91.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00882a10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00882a38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00882a3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00882a10",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00882a14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "unmatched:00882a30",
      "READ",
      [
        "storage",
        "002b94fd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008839bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "008839c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048d058"
      ]
    ],
    [
      "008839dc",
      "READ",
      [
        "storage",
        "002b95cc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008829f8.md#insn-00882a10) · [`00882a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008829f8.md#insn-00882a14) · [`00882a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/008829f8.md#insn-00882a38)

~~~diff
- 00882a10 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00882a10 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00882a10 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00882a10 bytes a8831ff8
- 00882a14 ["INT_ADD", "register:40f0:8", ["const:882a14:8", "const:4:8"]]
- 00882a14 ["CALL", null, ["ram:48cd38:8"]]
- 00882a14 bytes c928f097
- 00882a38 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00882a38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00882a38 bytes e02300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b737416267618761a2d6f0819dbab369"></a>

### [`00882c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882c74.md) → [`00883c20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883c20.md) FUN_00883c20

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

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
      "site": "00882c80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00883c2c"
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
      "unmatched:00882c80",
      "DATA",
      [
        "storage",
        "00c80968",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883c2c",
      "DATA",
      [
        "storage",
        "00c81938",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882c74.md#insn-00882c80) · [`00882c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882c74.md#insn-00882c74)
- 新版 [`00883c2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883c20.md#insn-00883c2c)

~~~diff
- 00882c80 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00882c80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00882c80 bytes 090000f9
+ 00883c2c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00883c2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00883c2c bytes 090000f9
- 00882c74 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00882c74 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00882c74 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00882c74 bytes 08204039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a0e5e2f096aa08792d0b0aab3db66a6"></a>

### [`00882d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882d48.md) → [`00883cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883cf4.md) FUN_00883cf4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

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
      "site": "00882d50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00883cfc"
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
      "unmatched:00882d50",
      "DATA",
      [
        "storage",
        "00c80968",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883cfc",
      "DATA",
      [
        "storage",
        "00c81938",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00882d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882d48.md#insn-00882d50) · [`00882d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882d48.md#insn-00882d48)
- 新版 [`00883cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883cf4.md#insn-00883cfc)

~~~diff
- 00882d50 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00882d50 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 00882d50 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:8:8"]]
- 00882d50 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00882d50 bytes 288400f8
+ 00883cfc ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00883cfc ["COPY", "tmp:1:8", ["register:4008:8"]]
+ 00883cfc ["INT_ADD", "register:4008:8", ["register:4008:8", "const:8:8"]]
+ 00883cfc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00883cfc bytes 288400f8
- 00882d48 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00882d48 bytes e81f00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82ff2766fe179ceaf09c026265e342af"></a>

### [`00882dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882dcc.md) → [`00883d78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00883/00883d78.md) FUN_00883d78

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`00493288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493288.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.74% / 新版 67.74%

CFGの説明率　旧版 60.00% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00882dd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00882dd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00882dd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00882dd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00882dd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00882dd8",
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
      "00883d7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00883d80",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00883d84",
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

- 旧版 [`00882dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882dcc.md#insn-00882dd0) · [`00882dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882dcc.md#insn-00882dd4) · [`00882dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00882/00882dcc.md#insn-00882dd8)

~~~diff
- 00882dd0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00882dd0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00882dd0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00882dd0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00882dd0 bytes fd7b02a9
- 00882dd4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00882dd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00882dd4 bytes f51b00f9
- 00882dd8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00882dd8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00882dd8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00882dd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00882dd8 bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d3c0eb4d8fc27e96ca0632554c92251"></a>

### [`00883670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883670.md) → [`0088461c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/0088461c.md) FUN_0088461c

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
      "site": "00883688"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00884634"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00883690"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00883688",
      "DATA",
      [
        "storage",
        "00c80ad8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0088368c",
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
      "00884634",
      "DATA",
      [
        "storage",
        "00c81aa8",
        null,
        "undefined *"
      ]
    ],
    [
      "00884638",
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

- 旧版 [`00883688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883670.md#insn-00883688) · [`00883690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883670.md#insn-00883690)
- 新版 [`00884634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/0088461c.md#insn-00884634)

~~~diff
- 00883688 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00883688 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00883688 bytes 080000f9
- 00883690 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00883690 ["RETURN", null, ["register:0:8"]]
- 00883690 bytes c0035fd6
+ 00884634 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00884634 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00884634 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63bfcc4838c46c67457fbd0fe4fc3d44"></a>

### [`00883a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883a28.md) → [`008849d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/008849d4.md) FUN_008849d4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00883a44"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008849f0"
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
      "unmatched:00883a44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00884a00"
      ]
    ]
  ],
  "added": [
    [
      "008849f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00884a00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00883a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883a28.md#insn-00883a44) · [`00883a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883a28.md#insn-00883a40)
- 新版 [`008849f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/008849d4.md#insn-008849f0)

~~~diff
- 00883a44 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00883a44 bytes 80000054
+ 008849f0 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 008849f0 bytes 80000054
- 00883a40 ["INT_LESSEQUAL", "register:105:1", ["register:4048:8", "register:4000:8"]]
- 00883a40 ["INT_SBORROW", "register:106:1", ["register:4000:8", "register:4048:8"]]
- 00883a40 ["INT_SUB", "tmp:0:8", ["register:4000:8", "register:4048:8"]]
- 00883a40 ["INT_SLESS", "register:107:1", ["tmp:0:8", "const:0:8"]]
- 00883a40 bytes 1f0009eb
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-221758dbd25f377f39d798b80d363aad"></a>

### [`00883aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883aac.md) → [`00884a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884a58.md) FUN_00884a58

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00880700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880700.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008816ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/008816ac.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 75.00% / 新版 69.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00883ae8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00884a94"
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
      "unmatched:00883ae8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00884a94",
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

- 旧版 [`00883ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883aac.md#insn-00883ae8) · [`00883acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00883/00883aac.md#insn-00883acc)
- 新版 [`00884a94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884a58.md#insn-00884a94) · [`00884a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00884/00884a58.md#insn-00884a78)

~~~diff
- 00883ae8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00883ae8 ["INT_ADD", "register:40f0:8", ["const:883ae8:8", "const:4:8"]]
- 00883ae8 ["CALLIND", null, ["register:0:8"]]
- 00883ae8 bytes 00013fd6
+ 00884a94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00884a94 ["INT_ADD", "register:40f0:8", ["const:884a94:8", "const:4:8"]]
+ 00884a94 ["CALLIND", null, ["register:0:8"]]
+ 00884a94 bytes 00013fd6
- 00883acc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00883acc ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00884a78 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00884a78 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00883acc bytes 000100b4
+ 00884a78 bytes 000100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-880dd71027a9f594696c905856556c21"></a>

### [`0088471c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/0088471c.md) → [`008856c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008856c8.md) FUN_008856c8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 66.67% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00884758"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00885704"
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
      "unmatched:00884758",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00885704",
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

- 旧版 [`00884758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/0088471c.md#insn-00884758) · [`0088473c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/0088471c.md#insn-0088473c)
- 新版 [`00885704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008856c8.md#insn-00885704) · [`008856e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/008856c8.md#insn-008856e8)

~~~diff
- 00884758 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884758 ["INT_ADD", "register:40f0:8", ["const:884758:8", "const:4:8"]]
- 00884758 ["CALLIND", null, ["register:0:8"]]
- 00884758 bytes 00013fd6
+ 00885704 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885704 ["INT_ADD", "register:40f0:8", ["const:885704:8", "const:4:8"]]
+ 00885704 ["CALLIND", null, ["register:0:8"]]
+ 00885704 bytes 00013fd6
- 0088473c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0088473c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 008856e8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 008856e8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 0088473c bytes 000100b4
+ 008856e8 bytes 000100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb392103c1e81f9e03fbe4bdc79e6abe"></a>

### [`008847a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008847a0.md) → [`0088574c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088574c.md) FUN_0088574c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 61.54% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008847e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00885790"
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
      "unmatched:008847e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008857bc"
      ]
    ]
  ],
  "added": [
    [
      "00885790",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008857bc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008847e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008847a0.md#insn-008847e4) · [`008847dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008847a0.md#insn-008847dc)
- 新版 [`00885790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088574c.md#insn-00885790) · [`00885788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/0088574c.md#insn-00885788)

~~~diff
- 008847e4 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 008847e4 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 008847e4 bytes 740100b4
+ 00885790 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00885790 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00885790 bytes 740100b4
- 008847dc ["COPY", "register:0:8", ["register:4040:8"]]
- 008847dc ["INT_ADD", "register:40f0:8", ["const:8847dc:8", "const:4:8"]]
- 008847dc ["CALLIND", null, ["register:0:8"]]
+ 00885788 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885788 ["INT_ADD", "register:40f0:8", ["const:885788:8", "const:4:8"]]
+ 00885788 ["CALLIND", null, ["register:0:8"]]
- 008847dc bytes 00013fd6
+ 00885788 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18d648ae9c85ab67aed7179ba0ca8a07"></a>

### [`008848ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008848ec.md) → [`00885898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885898.md) FUN_00885898

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.86% / 新版 82.86%

CFGの説明率　旧版 26.67% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00884910"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008858bc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00884934"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00884910",
      "DATA",
      [
        "storage",
        "00c80cf8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00884934",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "008858bc",
      "DATA",
      [
        "storage",
        "00c81cc8",
        null,
        "undefined *"
      ]
    ],
    [
      "008858e0",
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

- 旧版 [`00884910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008848ec.md#insn-00884910) · [`00884934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/008848ec.md#insn-00884934)
- 新版 [`008858bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885898.md#insn-008858bc)

~~~diff
- 00884910 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00884910 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00884910 bytes 680200f9
- 00884934 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884934 ["INT_ADD", "register:40f0:8", ["const:884934:8", "const:4:8"]]
- 00884934 ["CALLIND", null, ["register:0:8"]]
- 00884934 bytes 00013fd6
+ 008858bc ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 008858bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008858bc bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c90e438a697f2e795015dddeca6f7373"></a>

### [`00884ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884ac8.md) → [`00885a74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885a74.md) FUN_00885a74

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 58.33% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00884b0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00885ab8"
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
      "unmatched:00884b0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00885acc"
      ]
    ]
  ],
  "added": [
    [
      "00885ab8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00885acc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00884b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884ac8.md#insn-00884b0c) · [`00884b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884ac8.md#insn-00884b04)
- 新版 [`00885ab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885a74.md#insn-00885ab8) · [`00885ab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885a74.md#insn-00885ab0)

~~~diff
- 00884b0c ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00884b0c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00884b0c bytes b30000b4
+ 00885ab8 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00885ab8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00885ab8 bytes b30000b4
- 00884b04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884b04 ["INT_ADD", "register:40f0:8", ["const:884b04:8", "const:4:8"]]
- 00884b04 ["CALLIND", null, ["register:0:8"]]
+ 00885ab0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885ab0 ["INT_ADD", "register:40f0:8", ["const:885ab0:8", "const:4:8"]]
+ 00885ab0 ["CALLIND", null, ["register:0:8"]]
- 00884b04 bytes 00013fd6
+ 00885ab0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79e27a32847c3d00511b28fa88c20cdd"></a>

### [`00884b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884b4c.md) → [`00885af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885af8.md) FUN_00885af8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00880700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880700.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008816ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/008816ac.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 76.92% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00884bb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00885b5c"
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
      "unmatched:00884bb0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00885b5c",
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

- 旧版 [`00884bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884b4c.md#insn-00884bb0) · [`00884b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00884/00884b4c.md#insn-00884b88)
- 新版 [`00885b5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885af8.md#insn-00885b5c) · [`00885b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00885/00885af8.md#insn-00885b34)

~~~diff
- 00884bb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884bb0 ["INT_ADD", "register:40f0:8", ["const:884bb0:8", "const:4:8"]]
- 00884bb0 ["CALLIND", null, ["register:0:8"]]
- 00884bb0 bytes 00013fd6
+ 00885b5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885b5c ["INT_ADD", "register:40f0:8", ["const:885b5c:8", "const:4:8"]]
+ 00885b5c ["CALLIND", null, ["register:0:8"]]
+ 00885b5c bytes 00013fd6
- 00884b88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00884b88 ["INT_ADD", "register:40f0:8", ["const:884b88:8", "const:4:8"]]
- 00884b88 ["CALLIND", null, ["register:0:8"]]
+ 00885b34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885b34 ["INT_ADD", "register:40f0:8", ["const:885b34:8", "const:4:8"]]
+ 00885b34 ["CALLIND", null, ["register:0:8"]]
- 00884b88 bytes 00013fd6
+ 00885b34 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6925335edb0818daf3fc371cadc04d01"></a>

### [`008850e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008850e0.md) → [`0088608c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/0088608c.md) FUN_0088608c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 83.33% / 新版 76.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00885104"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008860b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00885108"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00885104",
      "DATA",
      [
        "storage",
        "00c80d68",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00885108",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008860c4"
      ]
    ]
  ],
  "added": [
    [
      "008860b0",
      "DATA",
      [
        "storage",
        "00c81d38",
        null,
        "undefined *"
      ]
    ],
    [
      "008860b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008860c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008850e0.md#insn-00885104) · [`00885108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/008850e0.md#insn-00885108)
- 新版 [`008860b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/0088608c.md#insn-008860b0)

~~~diff
- 00885104 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00885104 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00885104 bytes 680200f9
- 00885108 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00885108 bytes 80000054
+ 008860b0 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 008860b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008860b0 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3de3b4f181259ebbddc22ca70ac52f77"></a>

### [`00885b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885b6c.md) → [`00886b18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886b18.md) FUN_00886b18

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 81.82% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00885b90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00886b3c"
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
      "unmatched:00885b90",
      "DATA",
      [
        "storage",
        "00c80e68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886b3c",
      "DATA",
      [
        "storage",
        "00c81e38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885b6c.md#insn-00885b90) · [`00885b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885b6c.md#insn-00885b80)
- 新版 [`00886b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886b18.md#insn-00886b3c) · [`00886b2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886b18.md#insn-00886b2c)

~~~diff
- 00885b90 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00885b90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00885b90 bytes 680200f9
+ 00886b3c ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 00886b3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00886b3c bytes 680200f9
- 00885b80 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00886b2c ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00885b80 bytes c81f00f0
+ 00886b2c bytes c81f00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4724f93bd16a5ed555843d3e5bfff5b8"></a>

### [`00885dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885dd8.md) → [`00886d84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886d84.md) FUN_00886d84

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 41.67% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00885e1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00886dc8"
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
      "unmatched:00885e1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00886ddc"
      ]
    ]
  ],
  "added": [
    [
      "00886dc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00886ddc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00885e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885dd8.md#insn-00885e1c) · [`00885e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885dd8.md#insn-00885e14)
- 新版 [`00886dc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886d84.md#insn-00886dc8) · [`00886dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886d84.md#insn-00886dc0)

~~~diff
- 00885e1c ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00885e1c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00885e1c bytes b30000b4
+ 00886dc8 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00886dc8 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00886dc8 bytes b30000b4
- 00885e14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885e14 ["INT_ADD", "register:40f0:8", ["const:885e14:8", "const:4:8"]]
- 00885e14 ["CALLIND", null, ["register:0:8"]]
+ 00886dc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886dc0 ["INT_ADD", "register:40f0:8", ["const:886dc0:8", "const:4:8"]]
+ 00886dc0 ["CALLIND", null, ["register:0:8"]]
- 00885e14 bytes 00013fd6
+ 00886dc0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26e7944273c4a1f9feef550fab0fb27f"></a>

### [`00885e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885e5c.md) → [`00886e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886e08.md) FUN_00886e08

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0088577c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/0088577c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00886728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886728.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 58.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00885e5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00885e5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00885e60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00885e5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00885e60",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00885e98",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00886e08",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00886e0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00886e44",
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

- 旧版 [`00885e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885e5c.md#insn-00885e5c) · [`00885e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885e5c.md#insn-00885e60) · [`00885e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885e5c.md#insn-00885e98)

~~~diff
- 00885e5c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00885e5c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00885e5c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00885e5c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00885e5c bytes fd7bbea9
- 00885e60 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00885e60 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00885e60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00885e60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00885e60 bytes f44f01a9
- 00885e98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00885e98 ["INT_ADD", "register:40f0:8", ["const:885e98:8", "const:4:8"]]
- 00885e98 ["CALLIND", null, ["register:0:8"]]
- 00885e98 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43c95e8320b9589ed86db1b870b565b9"></a>

### [`00885ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885ff4.md) → [`00886fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00886/00886fa0.md) FUN_00886fa0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.40% / 新版 81.40%

CFGの説明率　旧版 81.82% / 新版 64.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00885ff4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00885ff4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00885ff8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00885ff4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00885ff8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00885ffc",
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
      "00886fa0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00886fa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00886fa8",
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

- 旧版 [`00885ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885ff4.md#insn-00885ff4) · [`00885ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885ff4.md#insn-00885ff8) · [`00885ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00885/00885ff4.md#insn-00885ffc)

~~~diff
- 00885ff4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00885ff4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00885ff4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00885ff4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00885ff4 bytes fd7bbda9
- 00885ff8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00885ff8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00885ff8 bytes f50b00f9
- 00885ffc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00885ffc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00885ffc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00885ffc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00885ffc bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7af4c3420783fdb17d35be9bbeea9124"></a>

### [`008861f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008861f8.md) → [`008871a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/008871a4.md) FUN_008871a4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008810f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008810f0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0088209c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/0088209c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 60.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008861f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008861f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008861fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008861f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008861fc",
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
      "008871a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008871a8",
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

- 旧版 [`008861f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008861f8.md#insn-008861f8) · [`008861fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008861f8.md#insn-008861fc)
- 新版 [`008871a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/008871a4.md#insn-008871a4)

~~~diff
- 008861f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008861f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008861f8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008861f8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008861f8 bytes fd7bbea9
- 008861fc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008861fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008861fc bytes f30b00f9
+ 008871a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 008871a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 008871a4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 008871a4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 008871a4 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0bcdebfa1fffc1d2ffa114399c9255a"></a>

### [`0088652c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/0088652c.md) → [`008874d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/008874d8.md) FUN_008874d8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 41.18% / 新版 41.18%

CFGの説明率　旧版 28.57% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00886544"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008874f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00886548"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00886544",
      "DATA",
      [
        "storage",
        "00c80f68",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00886548",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00887504"
      ]
    ]
  ],
  "added": [
    [
      "008874f0",
      "DATA",
      [
        "storage",
        "00c81f38",
        null,
        "undefined *"
      ]
    ],
    [
      "008874f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00887504"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/0088652c.md#insn-00886544) · [`00886548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/0088652c.md#insn-00886548)
- 新版 [`008874f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/008874d8.md#insn-008874f0)

~~~diff
- 00886544 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00886544 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00886544 bytes 0a0100f9
- 00886548 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00886548 bytes 80000054
+ 008874f0 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008874f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 008874f0 bytes 0a0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3579c4e17f560a487e72d975a814c527"></a>

### [`00886570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886570.md) → [`0088751c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/0088751c.md) FUN_0088751c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.57% / 新版 69.57%

CFGの説明率　旧版 28.57% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00886594"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00887540"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00886598"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00886594",
      "DATA",
      [
        "storage",
        "00c80f68",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00886598",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00887554"
      ]
    ],
    [
      "unmatched:008865b8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00887540",
      "DATA",
      [
        "storage",
        "00c81f38",
        null,
        "undefined *"
      ]
    ],
    [
      "00887544",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00887554"
      ]
    ],
    [
      "00887564",
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

- 旧版 [`00886594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886570.md#insn-00886594) · [`00886598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886570.md#insn-00886598) · [`008865b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886570.md#insn-008865b8)

~~~diff
- 00886594 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00886594 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00886594 bytes 680200f9
- 00886598 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00886598 bytes 80000054
- 008865b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008865b8 ["INT_ADD", "register:40f0:8", ["const:8865b8:8", "const:4:8"]]
- 008865b8 ["CALLIND", null, ["register:0:8"]]
- 008865b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc6bc6e77b3479bdd7657736eb21d613"></a>

### [`008865cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008865cc.md) → [`00887578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887578.md) FUN_00887578

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.97% / 新版 68.97%

CFGの説明率　旧版 30.00% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008865cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008865cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008865d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008865cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008865d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008865f8",
      "DATA",
      [
        "storage",
        "00c80f68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00887578",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0088757c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008875a4",
      "DATA",
      [
        "storage",
        "00c81f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008865cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008865cc.md#insn-008865cc) · [`008865d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008865cc.md#insn-008865d0) · [`008865f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008865cc.md#insn-008865f8)

~~~diff
- 008865cc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008865cc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008865cc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008865cc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008865cc bytes fd7bbea9
- 008865d0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008865d0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008865d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 008865d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008865d0 bytes f44f01a9
- 008865f8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008865f8 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 008865f8 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 008865f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008865f8 bytes 280401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2de56d7f0ef66fdd99326a4269298ef3"></a>

### [`00886654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886654.md) → [`00887600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887600.md) FUN_00887600

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 42.86% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00886670"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0088761c"
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
      "unmatched:00886670",
      "DATA",
      [
        "storage",
        "00c80f68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088761c",
      "DATA",
      [
        "storage",
        "00c81f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886654.md#insn-00886670) · [`00886668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886654.md#insn-00886668)
- 新版 [`0088761c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887600.md#insn-0088761c) · [`00887614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887600.md#insn-00887614)

~~~diff
- 00886670 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00886670 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 00886670 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 00886670 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00886670 bytes 290401f8
+ 0088761c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0088761c ["COPY", "tmp:1:8", ["register:4008:8"]]
+ 0088761c ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
+ 0088761c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 0088761c bytes 290401f8
- 00886668 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 00887614 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 00886668 bytes c91f00d0
+ 00887614 bytes c91f00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ba2f90f05f434aaa6f41fde3425e002"></a>

### [`00886700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886700.md) → [`008876ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/008876ac.md) FUN_008876ac

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00886258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886258.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00887204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887204.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 11.11% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0088671c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008876c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0088673c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088671c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008876d8"
      ]
    ],
    [
      "unmatched:0088673c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "008876c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008876d8"
      ]
    ],
    [
      "008876e8",
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

- 旧版 [`0088671c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886700.md#insn-0088671c) · [`0088673c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886700.md#insn-0088673c)
- 新版 [`008876c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/008876ac.md#insn-008876c8)

~~~diff
- 0088671c ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 0088671c bytes 80000054
- 0088673c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088673c ["INT_ADD", "register:40f0:8", ["const:88673c:8", "const:4:8"]]
- 0088673c ["CALLIND", null, ["register:0:8"]]
- 0088673c bytes 00013fd6
+ 008876c8 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 008876c8 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83abab29afcfadabba781f9569b9a8d0"></a>

### [`00886910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886910.md) → [`008878bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/008878bc.md) FUN_008878bc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 69.57% / 新版 69.57%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00886910"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00886910"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00886914"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00886910",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00886914",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00886928",
      "DATA",
      [
        "storage",
        "00c81008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008878bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008878c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008878d4",
      "DATA",
      [
        "storage",
        "00c81fd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886910.md#insn-00886910) · [`00886914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886910.md#insn-00886914) · [`00886928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886910.md#insn-00886928)

~~~diff
- 00886910 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00886910 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00886910 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00886910 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00886910 bytes fd7bbea9
- 00886914 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00886914 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00886914 bytes f30b00f9
- 00886928 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00886928 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00886928 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa92f974458365fe2bd7b62dbc82d47a"></a>

### [`008869c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008869c8.md) → [`00887974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887974.md) FUN_00887974

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 77.27% / 新版 77.27%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008869f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008869f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008869f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008869f0",
      "DATA",
      [
        "storage",
        "00c81008",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008869fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008879c0"
      ]
    ]
  ],
  "added": [
    [
      "0088799c",
      "DATA",
      [
        "storage",
        "00c81fd8",
        null,
        "undefined *"
      ]
    ],
    [
      "008879a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008879c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008869f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008869c8.md#insn-008869f0) · [`008869f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008869c8.md#insn-008869f4) · [`008869f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008869c8.md#insn-008869f8)

~~~diff
- 008869f0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008869f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008869f0 bytes 090000f9
- 008869f4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 008869f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008869f4 bytes 0080803c
- 008869f8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:18:8"]]
- 008869f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008869f8 bytes 080c00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-847c8efeca9e12fb0dc4613b74b4b2d7"></a>

### [`00886a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886a20.md) → [`008879cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/008879cc.md) FUN_008879cc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 73.33% / 新版 73.33%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00886a2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008879d8"
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
      "unmatched:00886a2c",
      "DATA",
      [
        "storage",
        "00c81008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008879d8",
      "DATA",
      [
        "storage",
        "00c81fd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886a20.md#insn-00886a2c) · [`00886a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886a20.md#insn-00886a20)
- 新版 [`008879d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/008879cc.md#insn-008879d8)

~~~diff
- 00886a2c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00886a2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00886a2c bytes 290000f9
+ 008879d8 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 008879d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008879d8 bytes 290000f9
- 00886a20 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00886a20 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00886a20 ["COPY", "register:5010:8", ["const:0:8"]]
- 00886a20 ["COPY", "register:5018:8", ["const:0:8"]]
- 00886a20 bytes 0080c03c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-848515216d21265dbbfc36396278cfb0"></a>

### [`00886a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886a5c.md) → [`00887a08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887a08.md) FUN_00887a08

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008817b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008817b0.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`0088275c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00882/0088275c.md) · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 16.67% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00886a5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00886a5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00886a60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00886a5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00886a60",
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
      "00887a08",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00887a0c",
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

- 旧版 [`00886a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886a5c.md#insn-00886a5c) · [`00886a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886a5c.md#insn-00886a60)
- 新版 [`00887a08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887a08.md#insn-00887a08)

~~~diff
- 00886a5c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00886a5c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00886a5c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00886a5c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00886a5c bytes fd7bbea9
- 00886a60 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00886a60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00886a60 bytes f30b00f9
+ 00887a08 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00887a08 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00887a08 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00887a08 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00887a08 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa4e8c08637f8c5d7d2baa910347aee5"></a>

### [`00886e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886e98.md) → [`00887e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887e44.md) FUN_00887e44

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 16.67% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00886ec8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00886ec8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00887e74"
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
      "unmatched:00886ec8",
      "DATA",
      [
        "storage",
        "00c81078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00887e74",
      "DATA",
      [
        "storage",
        "00c82048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886e98.md#insn-00886ec8) · [`00886eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886e98.md#insn-00886eac)
- 新版 [`00887e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887e44.md#insn-00887e74) · [`00887e58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00887/00887e44.md#insn-00887e58)

~~~diff
- 00886ec8 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00886ec8 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00886ec8 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00886ec8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00886ec8 bytes 0b2800a9
+ 00887e74 ["COPY", "tmp:0:8", ["register:4058:8"]]
+ 00887e74 ["COPY", "tmp:1:8", ["register:4050:8"]]
+ 00887e74 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00887e74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00887e74 bytes 0b2800a9
- 00886eac ["INT_ADD", "register:40f0:8", ["const:886eac:8", "const:4:8"]]
- 00886eac ["CALL", null, ["callee:00c58f30:8"]]
+ 00887e58 ["INT_ADD", "register:40f0:8", ["const:887e58:8", "const:4:8"]]
+ 00887e58 ["CALL", null, ["callee:00c58f30:8"]]
- 00886eac bytes 2d440f94
+ 00887e58 bytes 36440f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b15eff1f345b41f8b5206fbc74368f28"></a>

### [`00888124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888124.md) → [`008890d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/008890d0.md) FUN_008890d0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00888134"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008890e0"
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
      "unmatched:00888134",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008890f4"
      ]
    ]
  ],
  "added": [
    [
      "008890e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008890f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888124.md#insn-00888134) · [`00888140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888124.md#insn-00888140)
- 新版 [`008890e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/008890d0.md#insn-008890e0) · [`008890ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/008890d0.md#insn-008890ec)

~~~diff
- 00888134 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00888134 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00888134 bytes b30000b4
+ 008890e0 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 008890e0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 008890e0 bytes b30000b4
- 00888140 ["INT_ADD", "register:40f0:8", ["const:888140:8", "const:4:8"]]
- 00888140 ["CALL", null, ["callee:00c54d90:8"]]
+ 008890ec ["INT_ADD", "register:40f0:8", ["const:8890ec:8", "const:4:8"]]
+ 008890ec ["CALL", null, ["callee:00c54d90:8"]]
- 00888140 bytes 182f0f94
+ 008890ec bytes 292f0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c90bb0bc5109a0b0e2848639cbb884e"></a>

### [`00888818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888818.md) → [`008897c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/008897c4.md) FUN_008897c4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00857e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00857/00857e30.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 26.67% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00888870"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0088981c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008888a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00888870",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008897ec"
      ]
    ],
    [
      "unmatched:008888a4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00889810"
      ]
    ],
    [
      "unmatched:008888a0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0088981c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008897ec"
      ]
    ],
    [
      "00889850",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00889810"
      ]
    ],
    [
      "0088984c",
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

- 旧版 [`00888870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888818.md#insn-00888870) · [`008888a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888818.md#insn-008888a0)
- 新版 [`0088981c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00889/008897c4.md#insn-0088981c)

~~~diff
- 00888870 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00888870 ["CBRANCH", null, ["local:b1:8", "tmp:0:1"]]
- 00888870 bytes 94feffb4
- 008888a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008888a0 ["INT_ADD", "register:40f0:8", ["const:8888a0:8", "const:4:8"]]
- 008888a0 ["CALLIND", null, ["register:0:8"]]
- 008888a0 bytes 00013fd6
+ 0088981c ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 0088981c ["CBRANCH", null, ["local:b1:8", "tmp:0:1"]]
+ 0088981c bytes 94feffb4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ae5136c320af09d4f6c8cef417ee7d5"></a>

### [`00889074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889074.md) → [`0088a020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a020.md) FUN_0088a020

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
      "site": "00889080"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00889080"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0088a02c"
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
      "unmatched:00889080",
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
      "0088a02c",
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

- 旧版 [`00889080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889074.md#insn-00889080) · [`00889084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889074.md#insn-00889084)
- 新版 [`0088a02c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a020.md#insn-0088a02c)

~~~diff
- 00889080 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00889080 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00889080 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00889080 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00889080 bytes 292000a9
- 00889084 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00889084 ["RETURN", null, ["register:0:8"]]
- 00889084 bytes c0035fd6
+ 0088a02c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0088a02c ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 0088a02c ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 0088a02c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0088a02c bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ff71e8f06fa709879ca0bea37b07e90"></a>

### [`00889730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889730.md) → [`0088a6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a6dc.md) FUN_0088a6dc

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
      "site": "00889754"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00889754"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0088a700"
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
      "unmatched:00889754",
      "DATA",
      [
        "storage",
        "00c81460",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00889758",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088975c",
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
      "0088a700",
      "DATA",
      [
        "storage",
        "00c82430",
        null,
        "undefined *"
      ]
    ],
    [
      "0088a704",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0088a708",
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

- 旧版 [`00889754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889730.md#insn-00889754) · [`00889760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889730.md#insn-00889760)
- 新版 [`0088a700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088a6dc.md#insn-0088a700)

~~~diff
- 00889754 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00889754 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00889754 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00889754 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00889754 bytes 082400a9
- 00889760 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00889760 ["RETURN", null, ["register:0:8"]]
- 00889760 bytes c0035fd6
+ 0088a700 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0088a700 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 0088a700 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 0088a700 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0088a700 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90b87a27c324bfb1c98f92a6b277be3c"></a>

### [`00889bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889bac.md) → [`0088ab58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088ab58.md) FUN_0088ab58

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

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
      "site": "00889bd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00889bd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0088ab7c"
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
      "unmatched:00889bd0",
      "DATA",
      [
        "storage",
        "00c814e0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00889bd4",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00889bd8",
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
      "0088ab7c",
      "DATA",
      [
        "storage",
        "00c824b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088ab80",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0088ab84",
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

- 旧版 [`00889bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889bac.md#insn-00889bd0) · [`00889bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889bac.md#insn-00889bdc)
- 新版 [`0088ab7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088a/0088ab58.md#insn-0088ab7c)

~~~diff
- 00889bd0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00889bd0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00889bd0 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00889bd0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00889bd0 bytes 082400a9
- 00889bdc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00889bdc ["RETURN", null, ["register:0:8"]]
- 00889bdc bytes c0035fd6
+ 0088ab7c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0088ab7c ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 0088ab7c ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 0088ab7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0088ab7c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d716d15d1ee85d643166bfe8349cf9b6"></a>

### [`0088a3c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a3c8.md) → [`0088b374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b374.md) FUN_0088b374

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "0088a3d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0088b37c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0088a3d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088a3d0",
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
      "0088b37c",
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

- 旧版 [`0088a3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a3c8.md#insn-0088a3d0) · [`0088a3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a3c8.md#insn-0088a3d4)
- 新版 [`0088b37c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b374.md#insn-0088b37c)

~~~diff
- 0088a3d0 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 0088a3d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0088a3d0 bytes 280000f9
- 0088a3d4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0088a3d4 ["RETURN", null, ["register:0:8"]]
- 0088a3d4 bytes c0035fd6
+ 0088b37c ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 0088b37c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0088b37c bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f212679ca87f6540414be5ef3883bc2"></a>

### [`0088a3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a3e0.md) → [`0088b38c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b38c.md) FUN_0088b38c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b37c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37c24.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b38c18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b38/00b38c18.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 70.59% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0088a47c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0088b428"
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
      "unmatched:0088a47c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088b4b8"
      ]
    ]
  ],
  "added": [
    [
      "0088b428",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088b4b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a47c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a3e0.md#insn-0088a47c) · [`0088a410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a3e0.md#insn-0088a410)
- 新版 [`0088b428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b38c.md#insn-0088b428) · [`0088b3bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b38c.md#insn-0088b3bc)

~~~diff
- 0088a47c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0088a47c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 0088a47c bytes 81040054
+ 0088b428 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0088b428 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 0088b428 bytes 81040054
- 0088a410 ["INT_ADD", "register:40f0:8", ["const:88a410:8", "const:4:8"]]
- 0088a410 ["CALL", null, ["callee:00b38c18:8"]]
+ 0088b3bc ["INT_ADD", "register:40f0:8", ["const:88b3bc:8", "const:4:8"]]
+ 0088b3bc ["CALL", null, ["callee:00b38c18:8"]]
- 0088a410 bytes 05b60a94
+ 0088b3bc bytes 17b60a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4de3a8f32d76f1117228085727928bce"></a>

### [`0088a538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a538.md) → [`0088b4e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b4e4.md) FUN_0088b4e4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 5件 [`0088a688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a688.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`008888dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00888/008888dc.md) · 呼出先 5件 [`0088b634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b634.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 98.81% / 新版 98.81%

CFGの説明率　旧版 85.37% / 新版 81.40%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0088a62c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "0088b5d8"
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
      "unmatched:0088a62c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0088a688"
      ]
    ]
  ],
  "added": [
    [
      "0088b5d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0088b634"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a62c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a538.md#insn-0088a62c) · [`0088a55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a538.md#insn-0088a55c)
- 新版 [`0088b5d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b4e4.md#insn-0088b5d8) · [`0088b508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088b4e4.md#insn-0088b508)

~~~diff
- 0088a62c ["INT_ADD", "register:40f0:8", ["const:88a62c:8", "const:4:8"]]
- 0088a62c ["CALL", null, ["ram:88a688:8"]]
- 0088a62c bytes 17000094
+ 0088b5d8 ["INT_ADD", "register:40f0:8", ["const:88b5d8:8", "const:4:8"]]
+ 0088b5d8 ["CALL", null, ["ram:88b634:8"]]
+ 0088b5d8 bytes 17000094
- 0088a55c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0088a55c ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
+ 0088b508 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 0088b508 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 0088a55c bytes 280500b4
+ 0088b508 bytes 280500b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f018914a28858031f3fac2a428c6859d"></a>

### [`0088aea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aea8.md) → [`0088be54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088be54.md) FUN_0088be54

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
      "site": "0088aea8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088aea8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088aeac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088aea8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088aeac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088aec0",
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
      "0088be54",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0088be58",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0088be6c",
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

- 旧版 [`0088aea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aea8.md#insn-0088aea8) · [`0088aeac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aea8.md#insn-0088aeac) · [`0088aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aea8.md#insn-0088aec0)

~~~diff
- 0088aea8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0088aea8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0088aea8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0088aea8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0088aea8 bytes fd7bbea9
- 0088aeac ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0088aeac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0088aeac bytes f30b00f9
- 0088aec0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0088aec0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0088aec0 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39a40df20138b3f7f0b3cbf22cf76ae2"></a>

### [`0088afbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088afbc.md) → [`0088bf68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088bf68.md) FUN_0088bf68

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

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
      "site": "0088afc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0088bf70"
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
      "unmatched:0088afc4",
      "DATA",
      [
        "storage",
        "00c81780",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0088afc8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58f40"
      ]
    ]
  ],
  "added": [
    [
      "0088bf70",
      "DATA",
      [
        "storage",
        "00c82750",
        null,
        "undefined *"
      ]
    ],
    [
      "0088bf74",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58f40"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088afc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088afbc.md#insn-0088afc4) · [`0088afbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088afbc.md#insn-0088afbc)
- 新版 [`0088bf70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088bf68.md#insn-0088bf70)

~~~diff
- 0088afc4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0088afc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0088afc4 bytes 080000f9
+ 0088bf70 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 0088bf70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0088bf70 bytes 080000f9
- 0088afbc ["COPY", "register:4040:8", ["const:c81000:8"]]
- 0088afbc bytes a81f00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bd4ab49cbd980f1443e112db5b2d868"></a>

### [`0088afcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088afcc.md) → [`0088bf78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088b/0088bf78.md) FUN_0088bf78

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
      "site": "0088afcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088afcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088afd0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088afcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088afd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088afe4",
      "DATA",
      [
        "storage",
        "00c81780",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088bf78",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0088bf7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0088bf90",
      "DATA",
      [
        "storage",
        "00c82750",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088afcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088afcc.md#insn-0088afcc) · [`0088afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088afcc.md#insn-0088afd0) · [`0088afe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088afcc.md#insn-0088afe4)

~~~diff
- 0088afcc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0088afcc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0088afcc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0088afcc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0088afcc bytes fd7bbea9
- 0088afd0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0088afd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0088afd0 bytes f30b00f9
- 0088afe4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0088afe4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0088afe4 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d83647fcb57e4861bfc5c0fabf0b6a5e"></a>

### [`0088b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b210.md) → [`0088c1bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c1bc.md) FUN_0088c1bc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b228"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0088c1d4"
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
      "unmatched:0088b228",
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
      "0088c1d4",
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

- 旧版 [`0088b228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b210.md#insn-0088b228) · [`0088b21c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b210.md#insn-0088b21c)
- 新版 [`0088c1d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c1bc.md#insn-0088c1d4) · [`0088c1c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c1bc.md#insn-0088c1c8)

~~~diff
- 0088b228 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0088b228 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0088b228 bytes 080000f9
+ 0088c1d4 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 0088c1d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0088c1d4 bytes 080000f9
- 0088b21c ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088c1c8 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 0088b21c bytes a81f00d0
+ 0088c1c8 bytes a81f00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1ce6080c7662d30f85b64ee2980afda"></a>

### [`0088b5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b5f0.md) → [`0088c59c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c59c.md) FUN_0088c59c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b608"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0088c5b4"
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
      "unmatched:0088b608",
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
      "0088c5b4",
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

- 旧版 [`0088b608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b5f0.md#insn-0088b608) · [`0088b5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b5f0.md#insn-0088b5fc)
- 新版 [`0088c5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c59c.md#insn-0088c5b4) · [`0088c5a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c59c.md#insn-0088c5a8)

~~~diff
- 0088b608 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0088b608 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0088b608 bytes 080000f9
+ 0088c5b4 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 0088c5b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0088c5b4 bytes 080000f9
- 0088b5fc ["COPY", "register:4040:8", ["const:c81000:8"]]
+ 0088c5a8 ["COPY", "register:4040:8", ["const:c82000:8"]]
- 0088b5fc bytes a81f00d0
+ 0088c5a8 bytes a81f00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a932c8e2361b4ebdec225effc4d8567"></a>

### [`0088b998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b998.md) → [`0088c944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088c944.md) FUN_0088c944

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 28.57% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b9c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b9c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088b9cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088b9c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088b9cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088b9d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088c9bc"
      ]
    ]
  ],
  "added": [
    [
      "0088c974",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0088c978",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0088c980",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088c9bc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b9c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b998.md#insn-0088b9c8) · [`0088b9cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b998.md#insn-0088b9cc) · [`0088b9d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b998.md#insn-0088b9d4)

~~~diff
- 0088b9c8 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 0088b9c8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0088b9c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:8:8"]]
- 0088b9c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088b9c8 bytes eaa700a9
- 0088b9cc ["COPY", "tmp:0:8", ["register:8:8"]]
- 0088b9cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:8"]]
- 0088b9cc bytes eb0300f9
- 0088b9d4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0088b9d4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0088b9d4 bytes e00100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5436c8ad202aa81fabd333c10a939aa3"></a>

### [`0088ba58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088ba58.md) → [`0088ca04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088ca04.md) FUN_0088ca04

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088ba58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088ba58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088ba5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088ba58",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088ba5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088ba7c",
      "DATA",
      [
        "storage",
        "00c81990",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088ca04",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0088ca08",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0088ca28",
      "DATA",
      [
        "storage",
        "00c82960",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088ba58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088ba58.md#insn-0088ba58) · [`0088ba5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088ba58.md#insn-0088ba5c) · [`0088ba7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088ba58.md#insn-0088ba7c)

~~~diff
- 0088ba58 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0088ba58 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0088ba58 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0088ba58 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0088ba58 bytes fd7bbea9
- 0088ba5c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0088ba5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0088ba5c bytes f30b00f9
- 0088ba7c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0088ba7c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0088ba7c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0088ba7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088ba7c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c55be1d8bc8d1cb6d1e5f86a079889b"></a>

### [`0088ba8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088ba8c.md) → [`0088ca38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088ca38.md) FUN_0088ca38

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "0088ba98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088ba98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0088ca44"
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
      "unmatched:0088ba98",
      "DATA",
      [
        "storage",
        "00c81990",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088ca44",
      "DATA",
      [
        "storage",
        "00c82960",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088ba98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088ba8c.md#insn-0088ba98) · [`0088ba9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088ba8c.md#insn-0088ba9c)
- 新版 [`0088ca44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088ca38.md#insn-0088ca44)

~~~diff
- 0088ba98 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0088ba98 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0088ba98 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 0088ba98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088ba98 bytes 292000a9
- 0088ba9c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0088ba9c ["RETURN", null, ["register:0:8"]]
- 0088ba9c bytes c0035fd6
+ 0088ca44 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0088ca44 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 0088ca44 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 0088ca44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0088ca44 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8d07745de1ee08dbcd36473750a083a"></a>

### [`0088baa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088baa8.md) → [`0088ca54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088ca54.md) FUN_0088ca54

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 87.10% / 新版 87.10%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0088bad8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0088baf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0088bb18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088bad8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088cab8"
      ]
    ],
    [
      "unmatched:0088baf8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088cacc"
      ]
    ],
    [
      "unmatched:0088bb18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088cacc"
      ]
    ]
  ],
  "added": [
    [
      "0088ca84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088cab8"
      ]
    ],
    [
      "0088caa4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088cacc"
      ]
    ],
    [
      "0088cac4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088cacc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088bad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088baa8.md#insn-0088bad8) · [`0088baf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088baa8.md#insn-0088baf8) · [`0088bb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088baa8.md#insn-0088bb18)

~~~diff
- 0088bad8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0088bad8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 0088bad8 bytes a00100b4
- 0088baf8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0088baf8 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 0088baf8 bytes 41010054
- 0088bb18 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0088bb18 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 0088bb18 bytes 41000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff42aea914691f607356b150cfd87340"></a>

### [`0088bb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088bb50.md) → [`0088cafc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088cafc.md) FUN_0088cafc

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
      "site": "0088bb74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088bb74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0088cb20"
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
      "unmatched:0088bb74",
      "DATA",
      [
        "storage",
        "00c81a10",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0088bb78",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0088bb7c",
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
      "0088cb20",
      "DATA",
      [
        "storage",
        "00c829e0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088cb24",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0088cb28",
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

- 旧版 [`0088bb74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088bb50.md#insn-0088bb74) · [`0088bb80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088bb50.md#insn-0088bb80)
- 新版 [`0088cb20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088cafc.md#insn-0088cb20)

~~~diff
- 0088bb74 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0088bb74 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0088bb74 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0088bb74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088bb74 bytes 082400a9
- 0088bb80 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0088bb80 ["RETURN", null, ["register:0:8"]]
- 0088bb80 bytes c0035fd6
+ 0088cb20 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0088cb20 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 0088cb20 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 0088cb20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0088cb20 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0be6cee172d23af7934cbfdbafe89f0d"></a>

### [`0088bb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088bb84.md) → [`0088cb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088cb30.md) FUN_0088cb30

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 40.00% / 新版 40.00%

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
      "site": "0088bb90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088bb90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0088cb3c"
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
      "unmatched:0088bb90",
      "DATA",
      [
        "storage",
        "00c81a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088cb3c",
      "DATA",
      [
        "storage",
        "00c829e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088bb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088bb84.md#insn-0088bb90) · [`0088bb88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088bb84.md#insn-0088bb88)
- 新版 [`0088cb3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088c/0088cb30.md#insn-0088cb3c)

~~~diff
- 0088bb90 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0088bb90 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0088bb90 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 0088bb90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0088bb90 bytes 292000a9
+ 0088cb3c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0088cb3c ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 0088cb3c ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 0088cb3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0088cb3c bytes 292000a9
- 0088bb88 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 0088bb88 bytes a91f00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

