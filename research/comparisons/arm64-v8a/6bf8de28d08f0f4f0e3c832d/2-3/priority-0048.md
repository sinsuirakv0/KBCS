# v16.0.2 → v16.0.3 · 最優先の変更候補 (48)

[一覧の目次](README.md)

<a id="compare-6fb967d9d0c35b0fab0c31edadee7e23"></a>

### [`008723c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008723c0.md) → [`0087336c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/0087336c.md) FUN_0087336c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`0085b488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b488.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0085c434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c434.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-c1f7a310d7cb97807e3c8cdea2b49c0a"></a>

### [`008723d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008723d0.md) → [`0087337c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/0087337c.md) FUN_0087337c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0085b488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b488.md) · 呼出先 6件 [`00444120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444120.md) [`004446c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/004446c0.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0085c434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c434.md) · 呼出先 6件 [`00444440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444440.md) [`004449e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/004449e0.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 54.05% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008723d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008723d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008723d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008723d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008723d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008723dc",
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
      "00873380",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00873384",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00873388",
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

- 旧版 [`008723d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008723d0.md#insn-008723d4) · [`008723d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008723d0.md#insn-008723d8) · [`008723dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008723d0.md#insn-008723dc)

~~~diff
- 008723d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008723d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008723d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 008723d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008723d4 bytes fd7b05a9
- 008723d8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008723d8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008723d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 008723d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008723d8 bytes fc6f06a9
- 008723dc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 008723dc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 008723dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 008723dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008723dc bytes fa6707a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b644e3d95c7cbb05e1df52ed3cf21a0"></a>

### [`008725f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008725f8.md) → [`008735a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/008735a4.md) FUN_008735a4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00872a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872a44.md) · 呼出先 5件 [`00484800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/00484800.md) [`004939d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004939d8.md) [`00851a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`008739f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/008739f0.md) · 呼出先 5件 [`00484b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00484/00484b20.md) [`00493cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493cf8.md) [`00852a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852a10.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 22.88% / 新版 22.88%

CFGの説明率　旧版 10.34% / 新版 9.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 27件, `unresolved_call_alignment` 41件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008725fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008725fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00872600"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008725fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00872600",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00872604",
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
      "008735a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008735ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008735b0",
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

- 旧版 [`008725fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008725f8.md#insn-008725fc) · [`00872600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008725f8.md#insn-00872600) · [`00872604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008725f8.md#insn-00872604)

~~~diff
- 008725fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008725fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008725fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008725fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008725fc bytes fd7b02a9
- 00872600 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00872600 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00872600 bytes f91b00f9
- 00872604 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00872604 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00872604 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00872604 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00872604 bytes f85f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a580c98410813c9d7c28aaa10549aa1e"></a>

### [`00872a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872a44.md) → [`008739f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/008739f0.md) FUN_008739f0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`008725f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008725f8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008735a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/008735a4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00872a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872a44.md#insn-00872a54)
- 新版 [`00873a00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/008739f0.md#insn-00873a00)

~~~diff
- 00872a54 ["INT_ADD", "register:40f0:8", ["const:872a54:8", "const:4:8"]]
- 00872a54 ["CALL", null, ["callee:008735a4:8"]]
+ 00873a00 ["INT_ADD", "register:40f0:8", ["const:873a00:8", "const:4:8"]]
+ 00873a00 ["CALL", null, ["callee:008735a4:8"]]
- 00872a54 bytes e9feff97
+ 00873a00 bytes e9feff97
~~~


<a id="compare-58bb86ee237d3ae37bf86920c08d0a51"></a>

### [`00872a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872a68.md) → [`00873a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/00873a14.md) FUN_00873a14

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 17件 [`00444120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444120.md) [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00444440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444440.md) [`00445180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00445/00445180.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0047ec3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047ec3c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.53% / 新版 68.53%

CFGの説明率　旧版 35.53% / 新版 38.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00872a78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00872a78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00872a7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00872a78",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00872a7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00872a80",
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
      "00873a24",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00873a28",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00873a2c",
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

- 旧版 [`00872a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872a68.md#insn-00872a78) · [`00872a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872a68.md#insn-00872a7c) · [`00872a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872a68.md#insn-00872a80)

~~~diff
- 00872a78 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00872a78 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00872a78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 00872a78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00872a78 bytes f85f0ca9
- 00872a7c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00872a7c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00872a7c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00872a7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00872a7c bytes f6570da9
- 00872a80 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00872a80 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00872a80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00872a80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00872a80 bytes f44f0ea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2db33f57b827c7a2f8b5dd947dd11b2b"></a>

### [`008730b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008730b0.md) → [`0087405c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/0087405c.md) FUN_0087405c

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
      "definition_site": "0087406c",
      "incomplete_value": false,
      "site": "00874074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008730c0",
      "incomplete_value": false,
      "site": "008730c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "00874074",
      "DATA",
      [
        "storage",
        "00c7fce0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00874074",
      "DATA",
      [
        "storage",
        "00c80cb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008730bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008730b0.md#insn-008730bc) · [`008730c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008730b0.md#insn-008730c0) · [`008730cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008730b0.md#insn-008730cc)
- 新版 [`00874068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/0087405c.md#insn-00874068) · [`0087406c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/0087405c.md#insn-0087406c) · [`00874078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/0087405c.md#insn-00874078)

~~~diff
- 008730bc ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 00874068 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 008730bc bytes 68200090
+ 00874068 bytes 68200090
- 008730c0 ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 008730c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008730c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008730c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087406c ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 0087406c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087406c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087406c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008730c0 bytes 08813391
+ 0087406c bytes 08c13291
- 008730cc ["INT_ADD", "register:40f0:8", ["const:8730cc:8", "const:4:8"]]
- 008730cc ["CALL", null, ["callee:00c58f40:8"]]
+ 00874078 ["INT_ADD", "register:40f0:8", ["const:874078:8", "const:4:8"]]
+ 00874078 ["CALL", null, ["callee:00c58f40:8"]]
- 008730cc bytes a9930f94
+ 00874078 bytes b2930f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa914e0c049731c49900384f988293ea"></a>

### [`008730f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008730f0.md) → [`0087409c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/0087409c.md) FUN_0087409c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0085b488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b488.md) [`0087674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/0087674c.md) · 呼出先 12件 [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`00597f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f08.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 2件 [`0085c434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c434.md) [`008776f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008776f8.md) · 呼出先 12件 [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047ec3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047ec3c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`00598228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598228.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.32% / 新版 70.32%

CFGの説明率　旧版 24.66% / 新版 36.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00873134"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00873134"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087319c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00873134",
      "DATA",
      [
        "storage",
        "00c7fd30",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00873154",
      "PARAM",
      [
        "storage",
        "002eee70",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0087315c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59230"
      ]
    ]
  ],
  "added": [
    [
      "008740e0",
      "DATA",
      [
        "storage",
        "00c80d00",
        null,
        "undefined *"
      ]
    ],
    [
      "00874100",
      "PARAM",
      [
        "storage",
        "002eeeb0",
        null,
        "string"
      ]
    ],
    [
      "00874108",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59230"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008730f0.md#insn-00873134) · [`0087319c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008730f0.md#insn-0087319c) · [`008731a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008730f0.md#insn-008731a8)

~~~diff
- 00873134 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00873134 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 00873134 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00873134 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00873134 bytes 080400a9
- 0087319c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0087319c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:19:8"]]
- 0087319c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0087319c bytes e89301f8
- 008731a8 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 008731a8 ["COPY", "tmp:1:8", ["register:8:8"]]
- 008731a8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 008731a8 bytes e9030039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49fb7b9baabc1a19042cee16b752bf82"></a>

### [`008734ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008734ec.md) → [`00874498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874498.md) FUN_00874498

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.40% / 新版 81.40%

CFGの説明率　旧版 56.25% / 新版 64.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008734ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008734ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008734f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008734ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008734f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00873508",
      "DATA",
      [
        "storage",
        "00c7fd30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874498",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0087449c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008744b4",
      "DATA",
      [
        "storage",
        "00c80d00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008734ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008734ec.md#insn-008734ec) · [`008734f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008734ec.md#insn-008734f0) · [`00873508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008734ec.md#insn-00873508)

~~~diff
- 008734ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008734ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008734ec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008734ec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008734ec bytes fd7bbea9
- 008734f0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008734f0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008734f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 008734f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008734f0 bytes f44f01a9
- 00873508 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00873508 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00873508 bytes 090000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bef86aacea9b1c5acfb286b19590cf7c"></a>

### [`00873598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873598.md) → [`00874544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874544.md) FUN_00874544

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.18% / 新版 87.18%

CFGの説明率　旧版 78.57% / 新版 84.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087455c",
      "incomplete_value": false,
      "site": "00874560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008735b0",
      "incomplete_value": false,
      "site": "008735b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
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
      "00874560",
      "DATA",
      [
        "storage",
        "00c7fd30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00874560",
      "DATA",
      [
        "storage",
        "00c80d00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008735ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873598.md#insn-008735ac) · [`008735b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873598.md#insn-008735b0) · [`008735c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873598.md#insn-008735c0)
- 新版 [`00874558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874544.md#insn-00874558) · [`0087455c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874544.md#insn-0087455c) · [`0087456c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874544.md#insn-0087456c)

~~~diff
- 008735ac ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 00874558 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 008735ac bytes 69200090
+ 00874558 bytes 69200090
- 008735b0 ["COPY", "tmp:0:8", ["const:d30:8"]]
- 008735b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008735b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008735b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087455c ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 0087455c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087455c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087455c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008735b0 bytes 29c13491
+ 0087455c bytes 29013491
- 008735c0 ["INT_ADD", "register:40f0:8", ["const:8735c0:8", "const:4:8"]]
- 008735c0 ["CALL", null, ["callee:00c58f50:8"]]
+ 0087456c ["INT_ADD", "register:40f0:8", ["const:87456c:8", "const:4:8"]]
+ 0087456c ["CALL", null, ["callee:00c58f50:8"]]
- 008735c0 bytes 70920f94
+ 0087456c bytes 79920f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f32dac0ba03ad178a316d2b1dc11d047"></a>

### [`00873634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873634.md) → [`008745e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/008745e0.md) FUN_008745e0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 17件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00560b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560b48.md) [`00764f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764f38.md)
- 新版 呼出元 0件  · 呼出先 17件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00442e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442e98.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`00560e68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00560/00560e68.md) [`00765314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00765/00765314.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.30% / 新版 82.30%

CFGの説明率　旧版 49.46% / 新版 54.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087368c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00873694"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00873698"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087365c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768430"
      ]
    ],
    [
      "unmatched:00873688",
      "READ",
      [
        "storage",
        "002b4bdb",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0087368c",
      "WRITE",
      [
        "storage",
        "Stack[-0x9c]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00874608",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0076880c"
      ]
    ],
    [
      "00874634",
      "READ",
      [
        "storage",
        "002b4cb9",
        null,
        "string"
      ]
    ],
    [
      "00874638",
      "WRITE",
      [
        "storage",
        "Stack[-0x9c]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087368c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873634.md#insn-0087368c) · [`00873694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873634.md#insn-00873694) · [`00873698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873634.md#insn-00873698)

~~~diff
- 0087368c ["COPY", "tmp:0:4", ["const:0:4"]]
- 0087368c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0087368c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:64:8"]]
- 0087368c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0087368c bytes ff930139
- 00873694 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00873694 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00873694 bytes e96300b9
- 00873698 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:51:8"]]
- 00873698 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00873698 bytes e013853c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-039311bdfb4b3c3ff430b11c3e96808a"></a>

### [`00873b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873b00.md) → [`00874aac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874aac.md) FUN_00874aac

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00873634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873634.md) [`00874b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874b2c.md) · 呼出先 9件 [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`0044f988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f988.md) [`008745d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/008745d0.md) [`00874620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874620.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 2件 [`008745e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/008745e0.md) [`00875ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875ad8.md) · 呼出先 9件 [`0044fc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044f/0044fc40.md) [`0044fca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044f/0044fca8.md) [`0087557c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/0087557c.md) [`008755cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008755cc.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.06% / 新版 95.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00874b14",
      "incomplete_value": false,
      "site": "00874b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873b68",
      "incomplete_value": false,
      "site": "00873b68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00874b34",
      "incomplete_value": false,
      "site": "00874b34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873b88",
      "incomplete_value": false,
      "site": "00873b88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "00874b14",
      "DATA",
      [
        "storage",
        "00c7fd90",
        null,
        "undefined *"
      ]
    ],
    [
      "00874b34",
      "DATA",
      [
        "storage",
        "00c7fd90",
        null,
        "undefined *"
      ]
    ],
    [
      "00874b74",
      "READ",
      [
        "storage",
        "00c7fdb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00874b14",
      "DATA",
      [
        "storage",
        "00c80d60",
        null,
        "undefined *"
      ]
    ],
    [
      "00874b34",
      "DATA",
      [
        "storage",
        "00c80d60",
        null,
        "undefined *"
      ]
    ],
    [
      "00874b74",
      "READ",
      [
        "storage",
        "00c80d80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873b00.md#insn-00873b2c) · [`00873b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873b00.md#insn-00873b50) · [`00873b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873b00.md#insn-00873b54)
- 新版 [`00874ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874aac.md#insn-00874ad8) · [`00874afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874aac.md#insn-00874afc) · [`00874b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874aac.md#insn-00874b00)

~~~diff
- 00873b2c ["INT_ADD", "register:40f0:8", ["const:873b2c:8", "const:4:8"]]
- 00873b2c ["CALL", null, ["callee:0044fc40:8"]]
+ 00874ad8 ["INT_ADD", "register:40f0:8", ["const:874ad8:8", "const:4:8"]]
+ 00874ad8 ["CALL", null, ["callee:0044fc40:8"]]
- 00873b2c bytes 7d6fef97
+ 00874ad8 bytes 5a6cef97
- 00873b50 ["INT_ADD", "register:40f0:8", ["const:873b50:8", "const:4:8"]]
- 00873b50 ["CALL", null, ["callee:00c54d60:8"]]
+ 00874afc ["INT_ADD", "register:40f0:8", ["const:874afc:8", "const:4:8"]]
+ 00874afc ["CALL", null, ["callee:00c54d60:8"]]
- 00873b50 bytes 88800f94
+ 00874afc bytes 99800f94
- 00873b54 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 00874b00 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00873b54 bytes 68200090
+ 00874b00 bytes 68200090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1a307db313a3090316a30c594b3c92c"></a>

### [`00873ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873ca8.md) → [`00874c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874c54.md) FUN_00874c54

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00873634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873634.md) [`00874740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874740.md) · 呼出先 7件 [`00874d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874d00.md) [`00874d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874d50.md) [`00880700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880700.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 2件 [`008745e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/008745e0.md) [`008756ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008756ec.md) · 呼出先 7件 [`00875cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875cac.md) [`00875cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875cfc.md) [`008816ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/008816ac.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.15% / 新版 93.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00874cb4",
      "incomplete_value": false,
      "site": "00874cb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873d08",
      "incomplete_value": false,
      "site": "00873d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00874cd4",
      "incomplete_value": false,
      "site": "00874cd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873d28",
      "incomplete_value": false,
      "site": "00873d28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "00874cf0",
      "value": [
        "leaf",
        "ram:8816ac:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00873d44",
      "value": [
        "leaf",
        "ram:880700:8"
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
      "00874cb4",
      "DATA",
      [
        "storage",
        "00c7fe90",
        null,
        "undefined *"
      ]
    ],
    [
      "00874cd4",
      "DATA",
      [
        "storage",
        "00c7fe90",
        null,
        "undefined *"
      ]
    ],
    [
      "00874cf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00880700"
      ]
    ]
  ],
  "added": [
    [
      "00874cb4",
      "DATA",
      [
        "storage",
        "00c80e60",
        null,
        "undefined *"
      ]
    ],
    [
      "00874cd4",
      "DATA",
      [
        "storage",
        "00c80e60",
        null,
        "undefined *"
      ]
    ],
    [
      "00874cf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008816ac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873ca8.md#insn-00873d44) · [`00873cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873ca8.md#insn-00873cf0) · [`00873cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873ca8.md#insn-00873cf4)
- 新版 [`00874cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874c54.md#insn-00874cf0) · [`00874c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874c54.md#insn-00874c9c) · [`00874ca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874c54.md#insn-00874ca0)

~~~diff
- 00873d44 ["INT_ADD", "register:40f0:8", ["const:873d44:8", "const:4:8"]]
- 00873d44 ["CALL", null, ["ram:880700:8"]]
+ 00874cf0 ["INT_ADD", "register:40f0:8", ["const:874cf0:8", "const:4:8"]]
+ 00874cf0 ["CALL", null, ["ram:8816ac:8"]]
- 00873d44 bytes 6f320094
+ 00874cf0 bytes 6f320094
- 00873cf0 ["INT_ADD", "register:40f0:8", ["const:873cf0:8", "const:4:8"]]
- 00873cf0 ["CALL", null, ["callee:00c54d60:8"]]
+ 00874c9c ["INT_ADD", "register:40f0:8", ["const:874c9c:8", "const:4:8"]]
+ 00874c9c ["CALL", null, ["callee:00c54d60:8"]]
- 00873cf0 bytes 20800f94
+ 00874c9c bytes 31800f94
- 00873cf4 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 00874ca0 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00873cf4 bytes 68200090
+ 00874ca0 bytes 68200090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49946503bbc81921bd078e91d33a3aa9"></a>

### [`00873e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873e20.md) → [`00874dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874dcc.md) FUN_00874dcc

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873634.md) · 呼出先 7件 [`00875138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875138.md) [`00875188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875188.md) [`00880d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880d4c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`008745e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/008745e0.md) · 呼出先 7件 [`008760e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008760e4.md) [`00876134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876134.md) [`00881cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00881/00881cf8.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.52% / 新版 94.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00874e2c",
      "incomplete_value": false,
      "site": "00874e2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873e80",
      "incomplete_value": false,
      "site": "00873e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00874e4c",
      "incomplete_value": false,
      "site": "00874e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00873ea0",
      "incomplete_value": false,
      "site": "00873ea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f10:8"
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
      "00874e2c",
      "DATA",
      [
        "storage",
        "00c7ff10",
        null,
        "undefined *"
      ]
    ],
    [
      "00874e4c",
      "DATA",
      [
        "storage",
        "00c7ff10",
        null,
        "undefined *"
      ]
    ],
    [
      "00874e90",
      "READ",
      [
        "storage",
        "00c7ff30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00874e2c",
      "DATA",
      [
        "storage",
        "00c80ee0",
        null,
        "undefined *"
      ]
    ],
    [
      "00874e4c",
      "DATA",
      [
        "storage",
        "00c80ee0",
        null,
        "undefined *"
      ]
    ],
    [
      "00874e90",
      "READ",
      [
        "storage",
        "00c80f00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00873e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873e20.md#insn-00873e68) · [`00873e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873e20.md#insn-00873e6c) · [`00873e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873e20.md#insn-00873e70)
- 新版 [`00874e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874dcc.md#insn-00874e14) · [`00874e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874dcc.md#insn-00874e18) · [`00874e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874dcc.md#insn-00874e1c)

~~~diff
- 00873e68 ["INT_ADD", "register:40f0:8", ["const:873e68:8", "const:4:8"]]
- 00873e68 ["CALL", null, ["callee:00c54d60:8"]]
+ 00874e14 ["INT_ADD", "register:40f0:8", ["const:874e14:8", "const:4:8"]]
+ 00874e14 ["CALL", null, ["callee:00c54d60:8"]]
- 00873e68 bytes c27f0f94
+ 00874e14 bytes d37f0f94
- 00873e6c ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 00874e18 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00873e6c bytes 68200090
+ 00874e18 bytes 68200090
- 00873e70 ["COPY", "tmp:0:8", ["const:f10:8"]]
- 00873e70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873e70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873e70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874e1c ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00874e1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874e1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874e1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873e70 bytes 08413c91
+ 00874e1c bytes 08813b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60026eb22464a8f6e295a94e0752bffe"></a>

### [`00873f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873f98.md) → [`00874f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874f44.md) FUN_00874f44

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00873634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873634.md) [`00874dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874dd4.md) [`0087520c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/0087520c.md) [`008760b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/008760b0.md) · 呼出先 16件 [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`00453cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453cf0.md) [`007643dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007643dc.md) [`00764f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764f38.md) [`00875434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875434.md)
- 新版 呼出元 4件 [`008745e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/008745e0.md) [`00875d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875d80.md) [`008761b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008761b8.md) [`0087705c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/0087705c.md) · 呼出先 16件 [`0044fc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044f/0044fc40.md) [`00454010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00454/00454010.md) [`007647b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/007647b8.md) [`00765314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00765/00765314.md) [`008763e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008763e0.md)

変更の種類 call, call_target, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.05% / 新版 89.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00874fa0",
      "incomplete_value": true,
      "site": "00874fa0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
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
    "old": {
      "definition_site": "00873ff4",
      "incomplete_value": true,
      "site": "00873ff4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:dcb:8"
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
      "definition_site": "00874fa8",
      "incomplete_value": true,
      "site": "00874fa8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00873ffc",
      "incomplete_value": true,
      "site": "00873ffc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00874fec",
      "incomplete_value": true,
      "site": "00874ffc",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:6e6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874040",
      "incomplete_value": true,
      "site": "00874050",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:61b:8"
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
      "00874f94",
      "READ",
      [
        "storage",
        "002a7dcb",
        null,
        "string"
      ]
    ],
    [
      "00874f98",
      "READ",
      [
        "storage",
        "002a7dd0",
        null,
        "string"
      ]
    ],
    [
      "00874fec",
      "READ",
      [
        "storage",
        "002a361b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00874f94",
      "READ",
      [
        "storage",
        "002a7f23",
        null,
        "string"
      ]
    ],
    [
      "00874f98",
      "READ",
      [
        "storage",
        "002a7f28",
        null,
        "string"
      ]
    ],
    [
      "00874fec",
      "READ",
      [
        "storage",
        "002a36e6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873f98.md#insn-00874148) · [`00874154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873f98.md#insn-00874154) · [`00873fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873f98.md#insn-00873fe0)
- 新版 [`008750f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874f44.md#insn-008750f4) · [`00875100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874f44.md#insn-00875100) · [`00874f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874f44.md#insn-00874f8c)

~~~diff
- 00874148 ["INT_ADD", "register:40f0:8", ["const:874148:8", "const:4:8"]]
- 00874148 ["CALL", null, ["ram:7643dc:8"]]
+ 008750f4 ["INT_ADD", "register:40f0:8", ["const:8750f4:8", "const:4:8"]]
+ 008750f4 ["CALL", null, ["ram:7647b8:8"]]
- 00874148 bytes a5c0fb97
+ 008750f4 bytes b1bdfb97
- 00874154 ["INT_ADD", "register:40f0:8", ["const:874154:8", "const:4:8"]]
- 00874154 ["CALL", null, ["ram:764f38:8"]]
+ 00875100 ["INT_ADD", "register:40f0:8", ["const:875100:8", "const:4:8"]]
+ 00875100 ["CALL", null, ["ram:765314:8"]]
- 00874154 bytes 79c3fb97
+ 00875100 bytes 85c0fb97
- 00873fe0 ["COPY", "tmp:0:8", ["const:dcb:8"]]
- 00873fe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00873fe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00873fe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00874f8c ["COPY", "tmp:0:8", ["const:f23:8"]]
+ 00874f8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00874f8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00874f8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00873fe0 bytes 082d3791
+ 00874f8c bytes 088d3c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e264a87f9d23c64f15c133a82982f61"></a>

### [`00874484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874484.md) → [`00875430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875430.md) FUN_00875430

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
      "definition_site": "00875444",
      "incomplete_value": false,
      "site": "00875448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874498",
      "incomplete_value": false,
      "site": "0087449c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "00875448",
      "DATA",
      [
        "storage",
        "00c7fd90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875448",
      "DATA",
      [
        "storage",
        "00c80d60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874484.md#insn-00874494) · [`00874498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874484.md#insn-00874498) · [`008744ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874484.md#insn-008744ac)
- 新版 [`00875440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875430.md#insn-00875440) · [`00875444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875430.md#insn-00875444) · [`00875458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875430.md#insn-00875458)

~~~diff
- 00874494 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 00875440 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00874494 bytes 482000f0
+ 00875440 bytes 482000f0
- 00874498 ["COPY", "tmp:0:8", ["const:d90:8"]]
- 00874498 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874498 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874498 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875444 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 00875444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874498 bytes 08413691
+ 00875444 bytes 08813591
- 008744ac ["INT_ADD", "register:40f0:8", ["const:8744ac:8", "const:4:8"]]
- 008744ac ["CALL", null, ["callee:00c54d90:8"]]
+ 00875458 ["INT_ADD", "register:40f0:8", ["const:875458:8", "const:4:8"]]
+ 00875458 ["CALL", null, ["callee:00c54d90:8"]]
- 008744ac bytes 3d7e0f94
+ 00875458 bytes 4e7e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11e12a6e308b892be910ae72e95f5a6d"></a>

### [`008744e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/008744e0.md) → [`0087548c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/0087548c.md) FUN_0087548c

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
      "definition_site": "008754a4",
      "incomplete_value": false,
      "site": "008754a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008744f8",
      "incomplete_value": false,
      "site": "008744fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "008754a8",
      "DATA",
      [
        "storage",
        "00c7fd90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008754a8",
      "DATA",
      [
        "storage",
        "00c80d60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008744f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/008744e0.md#insn-008744f4) · [`008744f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/008744e0.md#insn-008744f8) · [`0087450c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/008744e0.md#insn-0087450c)
- 新版 [`008754a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/0087548c.md#insn-008754a0) · [`008754a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/0087548c.md#insn-008754a4) · [`008754b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/0087548c.md#insn-008754b8)

~~~diff
- 008744f4 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 008754a0 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 008744f4 bytes 482000f0
+ 008754a0 bytes 482000f0
- 008744f8 ["COPY", "tmp:0:8", ["const:d90:8"]]
- 008744f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008744f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008744f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008754a4 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 008754a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008754a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008754a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008744f8 bytes 08413691
+ 008754a4 bytes 08813591
- 0087450c ["INT_ADD", "register:40f0:8", ["const:87450c:8", "const:4:8"]]
- 0087450c ["CALL", null, ["callee:00c54d90:8"]]
+ 008754b8 ["INT_ADD", "register:40f0:8", ["const:8754b8:8", "const:4:8"]]
+ 008754b8 ["CALL", null, ["callee:00c54d90:8"]]
- 0087450c bytes 257e0f94
+ 008754b8 bytes 367e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d3ae76ba196e5cbb88639f3efe0d6f8"></a>

### [`0087453c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/0087453c.md) → [`008754e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008754e8.md) FUN_008754e8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087550c",
      "incomplete_value": false,
      "site": "00875510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874560",
      "incomplete_value": false,
      "site": "00874564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "00875510",
      "DATA",
      [
        "storage",
        "00c7fd90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875510",
      "DATA",
      [
        "storage",
        "00c80d60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/0087453c.md#insn-00874550) · [`0087455c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/0087453c.md#insn-0087455c) · [`00874560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/0087453c.md#insn-00874560)
- 新版 [`008754fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008754e8.md#insn-008754fc) · [`00875508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008754e8.md#insn-00875508) · [`0087550c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008754e8.md#insn-0087550c)

~~~diff
- 00874550 ["INT_ADD", "register:40f0:8", ["const:874550:8", "const:4:8"]]
- 00874550 ["CALL", null, ["callee:00c58f30:8"]]
+ 008754fc ["INT_ADD", "register:40f0:8", ["const:8754fc:8", "const:4:8"]]
+ 008754fc ["CALL", null, ["callee:00c58f30:8"]]
- 00874550 bytes 848e0f94
+ 008754fc bytes 8d8e0f94
- 0087455c ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 00875508 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 0087455c bytes 492000f0
+ 00875508 bytes 492000f0
- 00874560 ["COPY", "tmp:0:8", ["const:d90:8"]]
- 00874560 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00874560 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00874560 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087550c ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 0087550c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087550c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087550c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00874560 bytes 29413691
+ 0087550c bytes 29813591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57cdcba217ed33645562f9d9525935a0"></a>

### [`00874594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874594.md) → [`00875540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875540.md) FUN_00875540

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00875548",
      "incomplete_value": false,
      "site": "0087554c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087459c",
      "incomplete_value": false,
      "site": "008745a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "0087554c",
      "DATA",
      [
        "storage",
        "00c7fd90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087554c",
      "DATA",
      [
        "storage",
        "00c80d60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874594.md#insn-00874598) · [`0087459c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874594.md#insn-0087459c) · [`008745c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874594.md#insn-008745c4)
- 新版 [`00875544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875540.md#insn-00875544) · [`00875548`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875540.md#insn-00875548) · [`00875570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875540.md#insn-00875570)

~~~diff
- 00874598 ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 00875544 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 00874598 bytes 492000f0
+ 00875544 bytes 492000f0
- 0087459c ["COPY", "tmp:0:8", ["const:d90:8"]]
- 0087459c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087459c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087459c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875548 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 00875548 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875548 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875548 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087459c bytes 29413691
+ 00875548 bytes 29813591
- 008745c4 ["INT_ADD", "register:40f0:8", ["const:8745c4:8", "const:4:8"]]
- 008745c4 ["CALL", null, ["callee:00c54d60:8"]]
+ 00875570 ["INT_ADD", "register:40f0:8", ["const:875570:8", "const:4:8"]]
+ 00875570 ["CALL", null, ["callee:00c54d60:8"]]
- 008745c4 bytes eb7d0f94
+ 00875570 bytes fc7d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb525a4aadad6588e485ce628e390236"></a>

### [`00874740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874740.md) → [`008756ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008756ec.md) FUN_008756ec

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00874670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874670.md) · 呼出先 7件 [`00873ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873ca8.md) [`00874a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874a8c.md) [`00874adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874adc.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`0087561c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/0087561c.md) · 呼出先 7件 [`00874c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874c54.md) [`00875a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875a38.md) [`00875a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875a88.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00875788",
      "incomplete_value": false,
      "site": "00875788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008747dc",
      "incomplete_value": false,
      "site": "008747dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
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
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008757a4",
      "incomplete_value": false,
      "site": "008757a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008747f8",
      "incomplete_value": false,
      "site": "008747f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "00875788",
      "DATA",
      [
        "storage",
        "00c7fe00",
        null,
        "undefined *"
      ]
    ],
    [
      "008757a4",
      "DATA",
      [
        "storage",
        "00c7fe00",
        null,
        "undefined *"
      ]
    ],
    [
      "008757ec",
      "READ",
      [
        "storage",
        "00c7fe20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00875788",
      "DATA",
      [
        "storage",
        "00c80dd0",
        null,
        "undefined *"
      ]
    ],
    [
      "008757a4",
      "DATA",
      [
        "storage",
        "00c80dd0",
        null,
        "undefined *"
      ]
    ],
    [
      "008757ec",
      "READ",
      [
        "storage",
        "00c80df0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008747c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874740.md#insn-008747c4) · [`008747c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874740.md#insn-008747c8) · [`008747cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874740.md#insn-008747cc)
- 新版 [`00875770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008756ec.md#insn-00875770) · [`00875774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008756ec.md#insn-00875774) · [`00875778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008756ec.md#insn-00875778)

~~~diff
- 008747c4 ["INT_ADD", "register:40f0:8", ["const:8747c4:8", "const:4:8"]]
- 008747c4 ["CALL", null, ["callee:00c54d60:8"]]
+ 00875770 ["INT_ADD", "register:40f0:8", ["const:875770:8", "const:4:8"]]
+ 00875770 ["CALL", null, ["callee:00c54d60:8"]]
- 008747c4 bytes 6b7d0f94
+ 00875770 bytes 7c7d0f94
- 008747c8 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 00875774 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 008747c8 bytes 482000f0
+ 00875774 bytes 482000f0
- 008747cc ["COPY", "tmp:0:8", ["const:e00:8"]]
- 008747cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008747cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008747cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875778 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 00875778 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875778 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875778 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008747cc bytes 08013891
+ 00875778 bytes 08413791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d081509055ced88fdaf333e95e2d861b"></a>

### [`00874940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874940.md) → [`008758ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008758ec.md) FUN_008758ec

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
      "definition_site": "00875900",
      "incomplete_value": false,
      "site": "00875904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874954",
      "incomplete_value": false,
      "site": "00874958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "00875904",
      "DATA",
      [
        "storage",
        "00c7fe00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875904",
      "DATA",
      [
        "storage",
        "00c80dd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874940.md#insn-00874950) · [`00874954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874940.md#insn-00874954) · [`00874968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874940.md#insn-00874968)
- 新版 [`008758fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008758ec.md#insn-008758fc) · [`00875900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008758ec.md#insn-00875900) · [`00875914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008758ec.md#insn-00875914)

~~~diff
- 00874950 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 008758fc ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00874950 bytes 482000f0
+ 008758fc bytes 482000f0
- 00874954 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 00874954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875900 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 00875900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874954 bytes 08013891
+ 00875900 bytes 08413791
- 00874968 ["INT_ADD", "register:40f0:8", ["const:874968:8", "const:4:8"]]
- 00874968 ["CALL", null, ["callee:00c54d90:8"]]
+ 00875914 ["INT_ADD", "register:40f0:8", ["const:875914:8", "const:4:8"]]
+ 00875914 ["CALL", null, ["callee:00c54d90:8"]]
- 00874968 bytes 0e7d0f94
+ 00875914 bytes 1f7d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-143b4e8234b3e8a3b7341ec79f0f835a"></a>

### [`0087499c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/0087499c.md) → [`00875948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875948.md) FUN_00875948

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
      "definition_site": "00875960",
      "incomplete_value": false,
      "site": "00875964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008749b4",
      "incomplete_value": false,
      "site": "008749b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "00875964",
      "DATA",
      [
        "storage",
        "00c7fe00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875964",
      "DATA",
      [
        "storage",
        "00c80dd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008749b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/0087499c.md#insn-008749b0) · [`008749b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/0087499c.md#insn-008749b4) · [`008749c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/0087499c.md#insn-008749c8)
- 新版 [`0087595c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875948.md#insn-0087595c) · [`00875960`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875948.md#insn-00875960) · [`00875974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875948.md#insn-00875974)

~~~diff
- 008749b0 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 0087595c ["COPY", "register:4040:8", ["const:c80000:8"]]
- 008749b0 bytes 482000f0
+ 0087595c bytes 482000f0
- 008749b4 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 008749b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008749b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008749b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875960 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 00875960 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875960 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875960 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008749b4 bytes 08013891
+ 00875960 bytes 08413791
- 008749c8 ["INT_ADD", "register:40f0:8", ["const:8749c8:8", "const:4:8"]]
- 008749c8 ["CALL", null, ["callee:00c54d90:8"]]
+ 00875974 ["INT_ADD", "register:40f0:8", ["const:875974:8", "const:4:8"]]
+ 00875974 ["CALL", null, ["callee:00c54d90:8"]]
- 008749c8 bytes f67c0f94
+ 00875974 bytes 077d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ff7817d4f014fadd3e106d9b19d519d"></a>

### [`008749f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/008749f8.md) → [`008759a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008759a4.md) FUN_008759a4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008759c8",
      "incomplete_value": false,
      "site": "008759cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874a1c",
      "incomplete_value": false,
      "site": "00874a20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "008759cc",
      "DATA",
      [
        "storage",
        "00c7fe00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008759cc",
      "DATA",
      [
        "storage",
        "00c80dd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/008749f8.md#insn-00874a0c) · [`00874a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/008749f8.md#insn-00874a18) · [`00874a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/008749f8.md#insn-00874a1c)
- 新版 [`008759b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008759a4.md#insn-008759b8) · [`008759c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008759a4.md#insn-008759c4) · [`008759c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008759a4.md#insn-008759c8)

~~~diff
- 00874a0c ["INT_ADD", "register:40f0:8", ["const:874a0c:8", "const:4:8"]]
- 00874a0c ["CALL", null, ["callee:00c58f30:8"]]
+ 008759b8 ["INT_ADD", "register:40f0:8", ["const:8759b8:8", "const:4:8"]]
+ 008759b8 ["CALL", null, ["callee:00c58f30:8"]]
- 00874a0c bytes 558d0f94
+ 008759b8 bytes 5e8d0f94
- 00874a18 ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 008759c4 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 00874a18 bytes 492000f0
+ 008759c4 bytes 492000f0
- 00874a1c ["COPY", "tmp:0:8", ["const:e00:8"]]
- 00874a1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00874a1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00874a1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008759c8 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 008759c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008759c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008759c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00874a1c bytes 29013891
+ 008759c8 bytes 29413791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b21f7a73f7f1f5ef09d9ca233d30f371"></a>

### [`00874a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874a50.md) → [`008759fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008759fc.md) FUN_008759fc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00875a04",
      "incomplete_value": false,
      "site": "00875a08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874a58",
      "incomplete_value": false,
      "site": "00874a5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "00875a08",
      "DATA",
      [
        "storage",
        "00c7fe00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875a08",
      "DATA",
      [
        "storage",
        "00c80dd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874a50.md#insn-00874a54) · [`00874a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874a50.md#insn-00874a58) · [`00874a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874a50.md#insn-00874a80)
- 新版 [`00875a00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008759fc.md#insn-00875a00) · [`00875a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008759fc.md#insn-00875a04) · [`00875a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/008759fc.md#insn-00875a2c)

~~~diff
- 00874a54 ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 00875a00 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 00874a54 bytes 492000f0
+ 00875a00 bytes 492000f0
- 00874a58 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 00874a58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00874a58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00874a58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875a04 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 00875a04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875a04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875a04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00874a58 bytes 29013891
+ 00875a04 bytes 29413791
- 00874a80 ["INT_ADD", "register:40f0:8", ["const:874a80:8", "const:4:8"]]
- 00874a80 ["CALL", null, ["callee:00c54d60:8"]]
+ 00875a2c ["INT_ADD", "register:40f0:8", ["const:875a2c:8", "const:4:8"]]
+ 00875a2c ["CALL", null, ["callee:00c54d60:8"]]
- 00874a80 bytes bc7c0f94
+ 00875a2c bytes cd7c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c153c3f2309dc3e25e401dce65268bd5"></a>

### [`00874bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874bb4.md) → [`00875b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875b60.md) FUN_00875b60

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
      "definition_site": "00875b74",
      "incomplete_value": false,
      "site": "00875b78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874bc8",
      "incomplete_value": false,
      "site": "00874bcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      "00875b78",
      "DATA",
      [
        "storage",
        "00c7fe90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875b78",
      "DATA",
      [
        "storage",
        "00c80e60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874bb4.md#insn-00874bc4) · [`00874bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874bb4.md#insn-00874bc8) · [`00874bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874bb4.md#insn-00874bdc)
- 新版 [`00875b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875b60.md#insn-00875b70) · [`00875b74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875b60.md#insn-00875b74) · [`00875b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875b60.md#insn-00875b88)

~~~diff
- 00874bc4 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 00875b70 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00874bc4 bytes 482000f0
+ 00875b70 bytes 482000f0
- 00874bc8 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 00874bc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874bc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874bc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875b74 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 00875b74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875b74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875b74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874bc8 bytes 08413a91
+ 00875b74 bytes 08813991
- 00874bdc ["INT_ADD", "register:40f0:8", ["const:874bdc:8", "const:4:8"]]
- 00874bdc ["CALL", null, ["callee:00c54d90:8"]]
+ 00875b88 ["INT_ADD", "register:40f0:8", ["const:875b88:8", "const:4:8"]]
+ 00875b88 ["CALL", null, ["callee:00c54d90:8"]]
- 00874bdc bytes 717c0f94
+ 00875b88 bytes 827c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca97e07aa1735055ed614e07a8670112"></a>

### [`00874c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874c10.md) → [`00875bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875bbc.md) FUN_00875bbc

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
      "definition_site": "00875bd4",
      "incomplete_value": false,
      "site": "00875bd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874c28",
      "incomplete_value": false,
      "site": "00874c2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      "00875bd8",
      "DATA",
      [
        "storage",
        "00c7fe90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875bd8",
      "DATA",
      [
        "storage",
        "00c80e60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874c10.md#insn-00874c24) · [`00874c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874c10.md#insn-00874c28) · [`00874c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874c10.md#insn-00874c3c)
- 新版 [`00875bd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875bbc.md#insn-00875bd0) · [`00875bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875bbc.md#insn-00875bd4) · [`00875be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875bbc.md#insn-00875be8)

~~~diff
- 00874c24 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 00875bd0 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00874c24 bytes 482000f0
+ 00875bd0 bytes 482000f0
- 00874c28 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 00874c28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00874c28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00874c28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875bd4 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 00875bd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875bd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875bd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00874c28 bytes 08413a91
+ 00875bd4 bytes 08813991
- 00874c3c ["INT_ADD", "register:40f0:8", ["const:874c3c:8", "const:4:8"]]
- 00874c3c ["CALL", null, ["callee:00c54d90:8"]]
+ 00875be8 ["INT_ADD", "register:40f0:8", ["const:875be8:8", "const:4:8"]]
+ 00875be8 ["CALL", null, ["callee:00c54d90:8"]]
- 00874c3c bytes 597c0f94
+ 00875be8 bytes 6a7c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-650724b996a44f30f8079a1869c21e58"></a>

### [`00874c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874c6c.md) → [`00875c18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875c18.md) FUN_00875c18

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00875c3c",
      "incomplete_value": false,
      "site": "00875c40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874c90",
      "incomplete_value": false,
      "site": "00874c94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      "00875c40",
      "DATA",
      [
        "storage",
        "00c7fe90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875c40",
      "DATA",
      [
        "storage",
        "00c80e60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874c6c.md#insn-00874c80) · [`00874c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874c6c.md#insn-00874c8c) · [`00874c90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874c6c.md#insn-00874c90)
- 新版 [`00875c2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875c18.md#insn-00875c2c) · [`00875c38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875c18.md#insn-00875c38) · [`00875c3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875c18.md#insn-00875c3c)

~~~diff
- 00874c80 ["INT_ADD", "register:40f0:8", ["const:874c80:8", "const:4:8"]]
- 00874c80 ["CALL", null, ["callee:00c58f30:8"]]
+ 00875c2c ["INT_ADD", "register:40f0:8", ["const:875c2c:8", "const:4:8"]]
+ 00875c2c ["CALL", null, ["callee:00c58f30:8"]]
- 00874c80 bytes b88c0f94
+ 00875c2c bytes c18c0f94
- 00874c8c ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 00875c38 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 00874c8c bytes 492000f0
+ 00875c38 bytes 492000f0
- 00874c90 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 00874c90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00874c90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00874c90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875c3c ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 00875c3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875c3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875c3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00874c90 bytes 29413a91
+ 00875c3c bytes 29813991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed0abe0b88e856264203a1d34741dabe"></a>

### [`00874cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874cc4.md) → [`00875c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875c70.md) FUN_00875c70

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00875c78",
      "incomplete_value": false,
      "site": "00875c7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00874ccc",
      "incomplete_value": false,
      "site": "00874cd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      "00875c7c",
      "DATA",
      [
        "storage",
        "00c7fe90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875c7c",
      "DATA",
      [
        "storage",
        "00c80e60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874cc4.md#insn-00874cc8) · [`00874ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874cc4.md#insn-00874ccc) · [`00874cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874cc4.md#insn-00874cf4)
- 新版 [`00875c74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875c70.md#insn-00875c74) · [`00875c78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875c70.md#insn-00875c78) · [`00875ca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875c70.md#insn-00875ca0)

~~~diff
- 00874cc8 ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 00875c74 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 00874cc8 bytes 492000f0
+ 00875c74 bytes 492000f0
- 00874ccc ["COPY", "tmp:0:8", ["const:e90:8"]]
- 00874ccc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00874ccc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00874ccc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875c78 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 00875c78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875c78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875c78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00874ccc bytes 29413a91
+ 00875c78 bytes 29813991
- 00874cf4 ["INT_ADD", "register:40f0:8", ["const:874cf4:8", "const:4:8"]]
- 00874cf4 ["CALL", null, ["callee:00c54d60:8"]]
+ 00875ca0 ["INT_ADD", "register:40f0:8", ["const:875ca0:8", "const:4:8"]]
+ 00875ca0 ["CALL", null, ["callee:00c54d60:8"]]
- 00874cf4 bytes 1f7c0f94
+ 00875ca0 bytes 307c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75a71f291926df43587ba01ede66cf17"></a>

### [`00874d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874d50.md) → [`00875cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875cfc.md) FUN_00875cfc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00873ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873ca8.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00874c54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874c54.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 60.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00874d88",
      "incomplete_value": true,
      "site": "00874d8c",
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


#### 変更候補の命令位置

- 旧版 [`00874d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874d50.md#insn-00874d8c) · [`00874d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874d50.md#insn-00874d64) · [`00874d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874d50.md#insn-00874d70)
- 新版 [`00875d38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875cfc.md#insn-00875d38) · [`00875d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875cfc.md#insn-00875d10) · [`00875d1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875cfc.md#insn-00875d1c)

~~~diff
- 00874d8c ["INT_ADD", "register:40f0:8", ["const:874d8c:8", "const:4:8"]]
- 00874d8c ["CALL", null, ["callee:00c58f20:8"]]
+ 00875d38 ["INT_ADD", "register:40f0:8", ["const:875d38:8", "const:4:8"]]
+ 00875d38 ["CALL", null, ["callee:00c58f20:8"]]
- 00874d8c bytes 718c0f94
+ 00875d38 bytes 7a8c0f94
- 00874d64 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00874d64 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00875d10 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00875d10 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00874d64 bytes 740100b4
+ 00875d10 bytes 740100b4
- 00874d70 ["INT_ADD", "register:40f0:8", ["const:874d70:8", "const:4:8"]]
- 00874d70 ["CALL", null, ["callee:00c54d90:8"]]
+ 00875d1c ["INT_ADD", "register:40f0:8", ["const:875d1c:8", "const:4:8"]]
+ 00875d1c ["CALL", null, ["callee:00c54d90:8"]]
- 00874d70 bytes 0c7c0f94
+ 00875d1c bytes 1d7c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d6c4e61cc95044386da974cf810a383"></a>

### [`00874dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874dd4.md) → [`00875d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875d80.md) FUN_00875d80

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00874da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874da0.md) · 呼出先 6件 [`00597f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f0c.md) [`00873f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873f98.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00875d4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875d4c.md) · 呼出先 6件 [`0059822c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/0059822c.md) [`00874f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874f44.md) [`00a1b6a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a1b/00a1b6a4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 56.44% / 新版 56.44%

CFGの説明率　旧版 31.25% / 新版 23.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00874df4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00874e2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00874e30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00874df4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00874e24",
      "READ",
      [
        "storage",
        "002a485f",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00874e24",
      "READ",
      [
        "storage",
        "002a486f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00875da0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00875dd0",
      "READ",
      [
        "storage",
        "002a492a",
        null,
        "string"
      ]
    ],
    [
      "00875dd0",
      "READ",
      [
        "storage",
        "002a493a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874dd4.md#insn-00874df4) · [`00874e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874dd4.md#insn-00874e2c) · [`00874e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874dd4.md#insn-00874e30)

~~~diff
- 00874df4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00874df4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00874df4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00874df4 bytes a8831ff8
- 00874e2c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00874e2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00874e2c bytes e00b00f9
- 00874e30 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00874e30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5040:16"]]
- 00874e30 bytes e203803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8441b515755adfe7de832127cba3a10"></a>

### [`00874fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874fec.md) → [`00875f98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875f98.md) FUN_00875f98

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 75.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00875fac",
      "incomplete_value": false,
      "site": "00875fb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875000",
      "incomplete_value": false,
      "site": "00875004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f10:8"
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
      "00875fb0",
      "DATA",
      [
        "storage",
        "00c7ff10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875fb0",
      "DATA",
      [
        "storage",
        "00c80ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00874ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874fec.md#insn-00874ffc) · [`00875000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874fec.md#insn-00875000) · [`00875014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00874/00874fec.md#insn-00875014)
- 新版 [`00875fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875f98.md#insn-00875fa8) · [`00875fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875f98.md#insn-00875fac) · [`00875fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00875/00875f98.md#insn-00875fc0)

~~~diff
- 00874ffc ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 00875fa8 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00874ffc bytes 482000f0
+ 00875fa8 bytes 482000f0
- 00875000 ["COPY", "tmp:0:8", ["const:f10:8"]]
- 00875000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00875000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00875000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00875fac ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00875fac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00875fac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00875fac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00875000 bytes 08413c91
+ 00875fac bytes 08813b91
- 00875014 ["INT_ADD", "register:40f0:8", ["const:875014:8", "const:4:8"]]
- 00875014 ["CALL", null, ["callee:00c54d90:8"]]
+ 00875fc0 ["INT_ADD", "register:40f0:8", ["const:875fc0:8", "const:4:8"]]
+ 00875fc0 ["CALL", null, ["callee:00c54d90:8"]]
- 00875014 bytes 637b0f94
+ 00875fc0 bytes 747b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a487535efd7d02fe8d9829a6fb778f7f"></a>

### [`008750a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/008750a4.md) → [`00876050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876050.md) FUN_00876050

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 33.33% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008750a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008750a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008750a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008750a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008750a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008750cc",
      "DATA",
      [
        "storage",
        "00c7ff10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00876050",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00876054",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00876078",
      "DATA",
      [
        "storage",
        "00c80ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008750a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/008750a4.md#insn-008750a4) · [`008750a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/008750a4.md#insn-008750a8) · [`008750b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/008750a4.md#insn-008750b8)
- 新版 [`00876064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876050.md#insn-00876064)

~~~diff
- 008750a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008750a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008750a4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008750a4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008750a4 bytes fd7bbea9
- 008750a8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008750a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008750a8 bytes f30b00f9
- 008750b8 ["INT_ADD", "register:40f0:8", ["const:8750b8:8", "const:4:8"]]
- 008750b8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00876064 ["INT_ADD", "register:40f0:8", ["const:876064:8", "const:4:8"]]
+ 00876064 ["CALL", null, ["callee:00c58f30:8"]]
- 008750b8 bytes aa8b0f94
+ 00876064 bytes b38b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e692f721053ab7d566aef31c6dcdb79c"></a>

### [`008750fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/008750fc.md) → [`008760a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008760a8.md) FUN_008760a8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008760b0",
      "incomplete_value": false,
      "site": "008760b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875104",
      "incomplete_value": false,
      "site": "00875108",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f10:8"
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
      "008760b4",
      "DATA",
      [
        "storage",
        "00c7ff10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008760b4",
      "DATA",
      [
        "storage",
        "00c80ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/008750fc.md#insn-00875100) · [`00875104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/008750fc.md#insn-00875104) · [`0087512c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/008750fc.md#insn-0087512c)
- 新版 [`008760ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008760a8.md#insn-008760ac) · [`008760b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008760a8.md#insn-008760b0) · [`008760d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008760a8.md#insn-008760d8)

~~~diff
- 00875100 ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 008760ac ["COPY", "register:4048:8", ["const:c80000:8"]]
- 00875100 bytes 492000d0
+ 008760ac bytes 492000d0
- 00875104 ["COPY", "tmp:0:8", ["const:f10:8"]]
- 00875104 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00875104 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00875104 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008760b0 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 008760b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008760b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008760b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00875104 bytes 29413c91
+ 008760b0 bytes 29813b91
- 0087512c ["INT_ADD", "register:40f0:8", ["const:87512c:8", "const:4:8"]]
- 0087512c ["CALL", null, ["callee:00c54d60:8"]]
+ 008760d8 ["INT_ADD", "register:40f0:8", ["const:8760d8:8", "const:4:8"]]
+ 008760d8 ["CALL", null, ["callee:00c54d60:8"]]
- 0087512c bytes 117b0f94
+ 008760d8 bytes 227b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25faed62c0502833f17ccf67c7beea09"></a>

### [`00875138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875138.md) → [`008760e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008760e4.md) FUN_008760e4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00873e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873e20.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`00874dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874dcc.md) · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00875148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875138.md#insn-00875148) · [`00875154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875138.md#insn-00875154) · [`00875158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875138.md#insn-00875158)
- 新版 [`008760f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008760e4.md#insn-008760f4) · [`00876100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008760e4.md#insn-00876100) · [`00876104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008760e4.md#insn-00876104)

~~~diff
- 00875148 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00875148 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 008760f4 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 008760f4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00875148 bytes b30000b4
+ 008760f4 bytes b30000b4
- 00875154 ["INT_ADD", "register:40f0:8", ["const:875154:8", "const:4:8"]]
- 00875154 ["CALL", null, ["callee:00c54d90:8"]]
+ 00876100 ["INT_ADD", "register:40f0:8", ["const:876100:8", "const:4:8"]]
+ 00876100 ["CALL", null, ["callee:00c54d90:8"]]
- 00875154 bytes 137b0f94
+ 00876100 bytes 247b0f94
- 00875158 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00875158 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00876104 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00876104 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00875158 bytes 800000b4
+ 00876104 bytes 800000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-480bc7a27b0ee25aa07b412baba0d926"></a>

### [`0087520c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/0087520c.md) → [`008761b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008761b8.md) FUN_008761b8

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008751d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/008751d8.md) · 呼出先 6件 [`00597f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f0c.md) [`00873f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873f98.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00876184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876184.md) · 呼出先 6件 [`0059822c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/0059822c.md) [`00874f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874f44.md) [`00a1b6a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a1b/00a1b6a4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_store_alignment

命令の説明率　旧版 63.71% / 新版 63.71%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 4件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087620c",
      "incomplete_value": true,
      "site": "00876214",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "leaf",
            "const:2c3000:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875260",
      "incomplete_value": true,
      "site": "00875268",
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
                "const:fb0:8"
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
      "definition_site": "00876208",
      "incomplete_value": true,
      "site": "00876218",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:6b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087525c",
      "incomplete_value": true,
      "site": "0087526c",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:5ed:8"
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
      "definition_site": "00876208",
      "incomplete_value": true,
      "site": "00876218",
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
      "definition_site": "0087525c",
      "incomplete_value": true,
      "site": "0087526c",
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
      "00876208",
      "READ",
      [
        "storage",
        "002a35ed",
        null,
        "string"
      ]
    ],
    [
      "00876208",
      "READ",
      [
        "storage",
        "002a35fd",
        null,
        "string"
      ]
    ],
    [
      "0087620c",
      "READ",
      [
        "storage",
        "002c2fb0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00876208",
      "READ",
      [
        "storage",
        "002a36b8",
        null,
        "string"
      ]
    ],
    [
      "00876208",
      "READ",
      [
        "storage",
        "002a36c8",
        null,
        "string"
      ]
    ],
    [
      "0087620c",
      "READ",
      [
        "storage",
        "002c3000",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008752b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/0087520c.md#insn-008752b8) · [`008752bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/0087520c.md#insn-008752bc) · [`008752c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/0087520c.md#insn-008752c0)

~~~diff
- 008752b8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008752b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 008752b8 bytes e00b00f9
- 008752bc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:20:8"]]
- 008752bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5040:16"]]
- 008752bc bytes 0208803d
- 008752c0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008752c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008752c0 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 008752c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 008752c0 bytes 000400ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9528d4f8912e813690414080de8fd91"></a>

### [`00875434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875434.md) → [`008763e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008763e0.md) FUN_008763e0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00873f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873f98.md) · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00875674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875674.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00874f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874f44.md) · 呼出先 5件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00876620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876620.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 85.71% / 新版 81.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00875474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875434.md#insn-00875474) · [`008754c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875434.md#insn-008754c4) · [`008754f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875434.md#insn-008754f4)
- 新版 [`00876420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008763e0.md#insn-00876420) · [`00876470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008763e0.md#insn-00876470) · [`008764a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008763e0.md#insn-008764a0)

~~~diff
- 00875474 ["INT_EQUAL", "tmp:0:1", ["register:40d8:8", "const:0:8"]]
- 00875474 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00876420 ["INT_EQUAL", "tmp:0:1", ["register:40d8:8", "const:0:8"]]
+ 00876420 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00875474 bytes fb0600b4
+ 00876420 bytes fb0600b4
- 008754c4 ["INT_ADD", "register:40f0:8", ["const:8754c4:8", "const:4:8"]]
- 008754c4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00876470 ["INT_ADD", "register:40f0:8", ["const:876470:8", "const:4:8"]]
+ 00876470 ["CALL", null, ["callee:00c590f0:8"]]
- 008754c4 bytes 178b0f94
+ 00876470 bytes 208b0f94
- 008754f4 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
+ 008764a0 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 008754f4 bytes 20030054
+ 008764a0 bytes 20030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffef0e7fa24707460172c2ddc1adc3cb"></a>

### [`00875a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875a18.md) → [`008769c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008769c4.md) FUN_008769c4

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
      "definition_site": "008769e8",
      "incomplete_value": false,
      "site": "008769e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875a3c",
      "incomplete_value": false,
      "site": "00875a3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:f90:8"
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
      "008769e8",
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
      "008769e8",
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

- 旧版 [`00875a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875a18.md#insn-00875a2c) · [`00875a34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875a18.md#insn-00875a34) · [`00875a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875a18.md#insn-00875a38)
- 新版 [`008769d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008769c4.md#insn-008769d8) · [`008769e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008769c4.md#insn-008769e0) · [`008769e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/008769c4.md#insn-008769e4)

~~~diff
- 00875a2c ["INT_ADD", "register:40f0:8", ["const:875a2c:8", "const:4:8"]]
- 00875a2c ["CALL", null, ["callee:00c58f30:8"]]
+ 008769d8 ["INT_ADD", "register:40f0:8", ["const:8769d8:8", "const:4:8"]]
+ 008769d8 ["CALL", null, ["callee:00c58f30:8"]]
- 00875a2c bytes 4d890f94
+ 008769d8 bytes 56890f94
- 00875a34 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 008769e0 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00875a34 bytes 482000d0
+ 008769e0 bytes 482000d0
- 00875a38 ["COPY", "tmp:0:8", ["const:f90:8"]]
- 00875a38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00875a38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00875a38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008769e4 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 008769e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008769e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008769e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00875a38 bytes 08413e91
+ 008769e4 bytes 08813d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a4bc0fc0e8d637222c7f5aa680489f3"></a>

### [`00875ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875ab0.md) → [`00876a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876a5c.md) FUN_00876a5c

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
      "definition_site": "00876a70",
      "incomplete_value": false,
      "site": "00876a74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:fe0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875ac4",
      "incomplete_value": false,
      "site": "00875ac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:10:8"
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
      "00876a74",
      "DATA",
      [
        "storage",
        "00c80010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00876a74",
      "DATA",
      [
        "storage",
        "00c80fe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875ab0.md#insn-00875ac4) · [`00875ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875ab0.md#insn-00875ad8) · [`00875af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875ab0.md#insn-00875af8)
- 新版 [`00876a70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876a5c.md#insn-00876a70) · [`00876a84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876a5c.md#insn-00876a84) · [`00876aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876a5c.md#insn-00876aa4)

~~~diff
- 00875ac4 ["COPY", "tmp:0:8", ["const:10:8"]]
- 00875ac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00875ac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00875ac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00876a70 ["COPY", "tmp:0:8", ["const:fe0:8"]]
+ 00876a70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00876a70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00876a70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00875ac4 bytes 08410091
+ 00876a70 bytes 08813f91
- 00875ad8 ["INT_ADD", "register:40f0:8", ["const:875ad8:8", "const:4:8"]]
- 00875ad8 ["CALL", null, ["callee:00c54d90:8"]]
+ 00876a84 ["INT_ADD", "register:40f0:8", ["const:876a84:8", "const:4:8"]]
+ 00876a84 ["CALL", null, ["callee:00c54d90:8"]]
- 00875ad8 bytes b2780f94
+ 00876a84 bytes c3780f94
- 00875af8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875af8 ["INT_ADD", "register:40f0:8", ["const:875af8:8", "const:4:8"]]
- 00875af8 ["CALLIND", null, ["register:0:8"]]
+ 00876aa4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00876aa4 ["INT_ADD", "register:40f0:8", ["const:876aa4:8", "const:4:8"]]
+ 00876aa4 ["CALLIND", null, ["register:0:8"]]
- 00875af8 bytes 00013fd6
+ 00876aa4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d46ff8750a13a1432ea7cdb768579742"></a>

### [`00875b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875b0c.md) → [`00876ab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876ab8.md) FUN_00876ab8

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
      "definition_site": "00876ad0",
      "incomplete_value": false,
      "site": "00876ad4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:fe0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875b24",
      "incomplete_value": false,
      "site": "00875b28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
      "00876ad4",
      "DATA",
      [
        "storage",
        "00c80010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00876ad4",
      "DATA",
      [
        "storage",
        "00c80fe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875b0c.md#insn-00875b24) · [`00875b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875b0c.md#insn-00875b38) · [`00875b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875b0c.md#insn-00875b4c)
- 新版 [`00876ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876ab8.md#insn-00876ad0) · [`00876ae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876ab8.md#insn-00876ae4) · [`00876af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876ab8.md#insn-00876af8)

~~~diff
- 00875b24 ["COPY", "tmp:0:8", ["const:10:8"]]
- 00875b24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00875b24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00875b24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00876ad0 ["COPY", "tmp:0:8", ["const:fe0:8"]]
+ 00876ad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00876ad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00876ad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00875b24 bytes 08410091
+ 00876ad0 bytes 08813f91
- 00875b38 ["INT_ADD", "register:40f0:8", ["const:875b38:8", "const:4:8"]]
- 00875b38 ["CALL", null, ["callee:00c54d90:8"]]
+ 00876ae4 ["INT_ADD", "register:40f0:8", ["const:876ae4:8", "const:4:8"]]
+ 00876ae4 ["CALL", null, ["callee:00c54d90:8"]]
- 00875b38 bytes 9a780f94
+ 00876ae4 bytes ab780f94
- 00875b4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00875b4c ["INT_ADD", "register:40f0:8", ["const:875b4c:8", "const:4:8"]]
- 00875b4c ["CALLIND", null, ["register:0:8"]]
+ 00876af8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00876af8 ["INT_ADD", "register:40f0:8", ["const:876af8:8", "const:4:8"]]
+ 00876af8 ["CALLIND", null, ["register:0:8"]]
- 00875b4c bytes 00013fd6
+ 00876af8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ad140ee44224807b5f1a0e89f82fa58"></a>

### [`00875b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875b68.md) → [`00876b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876b14.md) FUN_00876b14

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00876b38",
      "incomplete_value": false,
      "site": "00876b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:fe0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875b8c",
      "incomplete_value": false,
      "site": "00875b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:10:8"
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
      "00876b3c",
      "DATA",
      [
        "storage",
        "00c80010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00876b3c",
      "DATA",
      [
        "storage",
        "00c80fe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875b68.md#insn-00875b7c) · [`00875b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875b68.md#insn-00875b8c) · [`00875bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875b68.md#insn-00875bac)
- 新版 [`00876b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876b14.md#insn-00876b28) · [`00876b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876b14.md#insn-00876b38) · [`00876b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876b14.md#insn-00876b58)

~~~diff
- 00875b7c ["INT_ADD", "register:40f0:8", ["const:875b7c:8", "const:4:8"]]
- 00875b7c ["CALL", null, ["callee:00c58f30:8"]]
+ 00876b28 ["INT_ADD", "register:40f0:8", ["const:876b28:8", "const:4:8"]]
+ 00876b28 ["CALL", null, ["callee:00c58f30:8"]]
- 00875b7c bytes f9880f94
+ 00876b28 bytes 02890f94
- 00875b8c ["COPY", "tmp:0:8", ["const:10:8"]]
- 00875b8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00875b8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00875b8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00876b38 ["COPY", "tmp:0:8", ["const:fe0:8"]]
+ 00876b38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00876b38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00876b38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00875b8c bytes 29410091
+ 00876b38 bytes 29813f91
- 00875bac ["INT_ADD", "register:40f0:8", ["const:875bac:8", "const:4:8"]]
- 00875bac ["CALL", null, ["callee:00c54d60:8"]]
+ 00876b58 ["INT_ADD", "register:40f0:8", ["const:876b58:8", "const:4:8"]]
+ 00876b58 ["CALL", null, ["callee:00c54d60:8"]]
- 00875bac bytes 71780f94
+ 00876b58 bytes 82780f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ee228e8afc8c728e454270bb4a2cd97"></a>

### [`00875bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875bc0.md) → [`00876b6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876b6c.md) FUN_00876b6c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00876b74",
      "incomplete_value": false,
      "site": "00876b78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:fe0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875bc8",
      "incomplete_value": false,
      "site": "00875bcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:10:8"
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
      "00876b78",
      "DATA",
      [
        "storage",
        "00c80010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00876b78",
      "DATA",
      [
        "storage",
        "00c80fe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00875bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875bc0.md#insn-00875bc8) · [`00875bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875bc0.md#insn-00875bf0)
- 新版 [`00876b74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876b6c.md#insn-00876b74) · [`00876b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876b6c.md#insn-00876b9c)

~~~diff
- 00875bc8 ["COPY", "tmp:0:8", ["const:10:8"]]
- 00875bc8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00875bc8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00875bc8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00876b74 ["COPY", "tmp:0:8", ["const:fe0:8"]]
+ 00876b74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00876b74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00876b74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00875bc8 bytes 29410091
+ 00876b74 bytes 29813f91
- 00875bf0 ["INT_ADD", "register:40f0:8", ["const:875bf0:8", "const:4:8"]]
- 00875bf0 ["CALL", null, ["callee:00c54d60:8"]]
+ 00876b9c ["INT_ADD", "register:40f0:8", ["const:876b9c:8", "const:4:8"]]
+ 00876b9c ["CALL", null, ["callee:00c54d60:8"]]
- 00875bf0 bytes 60780f94
+ 00876b9c bytes 71780f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82dd54507507301a03c6db136f44ab2c"></a>

### [`00875bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875bfc.md) → [`00876ba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876ba8.md) FUN_00876ba8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00873f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873f98.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`00874f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874f44.md) · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 16.67% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00876bbc",
      "incomplete_value": true,
      "site": "00876bc4",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00875c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875bfc.md#insn-00875c18) · [`00875c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875bfc.md#insn-00875c0c) · [`00875c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875bfc.md#insn-00875c1c)
- 新版 [`00876bc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876ba8.md#insn-00876bc4) · [`00876bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876ba8.md#insn-00876bb8) · [`00876bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876ba8.md#insn-00876bc8)

~~~diff
- 00875c18 ["INT_ADD", "register:40f0:8", ["const:875c18:8", "const:4:8"]]
- 00875c18 ["CALL", null, ["callee:00c54d90:8"]]
+ 00876bc4 ["INT_ADD", "register:40f0:8", ["const:876bc4:8", "const:4:8"]]
+ 00876bc4 ["CALL", null, ["callee:00c54d90:8"]]
- 00875c18 bytes 62780f94
+ 00876bc4 bytes 73780f94
- 00875c0c ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00875c0c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00876bb8 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00876bb8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00875c0c bytes b30000b4
+ 00876bb8 bytes b30000b4
- 00875c1c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00875c1c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00876bc8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00876bc8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00875c1c bytes 800000b4
+ 00876bc8 bytes 800000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42d945b64f0543ddcf84099e63ff551f"></a>

### [`00875c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875c4c.md) → [`00876bf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876bf8.md) FUN_00876bf8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00873f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873f98.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00874f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/00874f44.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00875c60"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00876c0c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00876c14",
      "incomplete_value": false,
      "site": "00876c18",
      "value": [
        "leaf",
        "const:ffffffffffffffff:8"
      ]
    },
    "old": null,
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
      "unmatched:00875c60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00876c38"
      ]
    ],
    [
      "unmatched:00875c80",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00876c0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00876c38"
      ]
    ],
    [
      "00876c2c",
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

- 旧版 [`00875c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875c4c.md#insn-00875c60) · [`00875c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875c4c.md#insn-00875c6c) · [`00875c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875c4c.md#insn-00875c80)
- 新版 [`00876c18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876bf8.md#insn-00876c18)

~~~diff
- 00875c60 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00875c60 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00875c60 bytes 740100b4
- 00875c6c ["INT_ADD", "register:40f0:8", ["const:875c6c:8", "const:4:8"]]
- 00875c6c ["CALL", null, ["callee:00c54d90:8"]]
+ 00876c18 ["INT_ADD", "register:40f0:8", ["const:876c18:8", "const:4:8"]]
+ 00876c18 ["CALL", null, ["callee:00c54d90:8"]]
- 00875c6c bytes 4d780f94
+ 00876c18 bytes 5e780f94
- 00875c80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875c80 ["INT_ADD", "register:40f0:8", ["const:875c80:8", "const:4:8"]]
- 00875c80 ["CALLIND", null, ["register:0:8"]]
- 00875c80 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d5e2e52f70283f7d038bf3e61e54b2f"></a>

### [`00875cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875cd0.md) → [`00876c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876c7c.md) FUN_00876c7c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00875c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875c9c.md) · 呼出先 6件 [`00876010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876010.md) [`00876060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876060.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`00876c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876c48.md) · 呼出先 6件 [`00876fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876fbc.md) [`0087700c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/0087700c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 70.83% / 新版 73.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00875d5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00875d5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00875d60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00876cbc",
      "DATA",
      [
        "storage",
        "003c7780",
        null,
        "dword"
      ]
    ],
    [
      "unmatched:00875d5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00875d60",
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
      "00876cbc",
      "DATA",
      [
        "storage",
        "003c7780",
        null,
        "byte[11]"
      ]
    ],
    [
      "00876d08",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00876d0c",
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

- 旧版 [`00875d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875cd0.md#insn-00875d5c) · [`00875d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875cd0.md#insn-00875d60) · [`00875d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875cd0.md#insn-00875d78)

~~~diff
- 00875d5c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00875d5c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00875d5c ["COPY", "tmp:2:8", ["tmp:0:8"]]
- 00875d5c ["INT_ADD", "tmp:3:8", ["register:8:8", "const:38:8"]]
- 00875d5c bytes f3ff03a9
- 00875d60 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00875d60 ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 00875d60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00875d60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00875d60 bytes e85b02a9
- 00875d78 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00875d78 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00875d78 ["COPY", "tmp:2:8", ["tmp:0:8"]]
- 00875d78 ["INT_ADD", "tmp:3:8", ["register:8:8", "const:38:8"]]
- 00875d78 bytes f3ff03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2888a4b7827c596e760824852fd92f1f"></a>

### [`00875e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875e74.md) → [`00876e20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876e20.md) FUN_00876e20

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00875e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875e74.md#insn-00875e90) · [`00875e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875e74.md#insn-00875e94) · [`00875eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875e74.md#insn-00875eb0)
- 新版 [`00876e3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876e20.md#insn-00876e3c) · [`00876e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876e20.md#insn-00876e40) · [`00876e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876e20.md#insn-00876e5c)

~~~diff
- 00875e90 ["INT_ADD", "register:40f0:8", ["const:875e90:8", "const:4:8"]]
- 00875e90 ["CALL", null, ["callee:00c54d90:8"]]
+ 00876e3c ["INT_ADD", "register:40f0:8", ["const:876e3c:8", "const:4:8"]]
+ 00876e3c ["CALL", null, ["callee:00c54d90:8"]]
- 00875e90 bytes c4770f94
+ 00876e3c bytes d5770f94
- 00875e94 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00875e94 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00876e40 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00876e40 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00875e94 bytes 800000b4
+ 00876e40 bytes 800000b4
- 00875eb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00875eb0 ["INT_ADD", "register:40f0:8", ["const:875eb0:8", "const:4:8"]]
- 00875eb0 ["CALLIND", null, ["register:0:8"]]
+ 00876e5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00876e5c ["INT_ADD", "register:40f0:8", ["const:876e5c:8", "const:4:8"]]
+ 00876e5c ["CALLIND", null, ["register:0:8"]]
- 00875eb0 bytes 00013fd6
+ 00876e5c bytes 00013fd6
~~~


<a id="compare-287a12eb94cfe99429af07340269f57a"></a>

### [`00875ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875ec4.md) → [`00876e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876e70.md) FUN_00876e70

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
      "definition_site": "00876e84",
      "incomplete_value": false,
      "site": "00876e88",
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
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875ed8",
      "incomplete_value": false,
      "site": "00875edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:80:8"
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
      "00876e88",
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
      "00876e88",
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

- 旧版 [`00875ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875ec4.md#insn-00875ed4) · [`00875ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875ec4.md#insn-00875ed8) · [`00875eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875ec4.md#insn-00875eec)
- 新版 [`00876e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876e70.md#insn-00876e80) · [`00876e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876e70.md#insn-00876e84) · [`00876e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876e70.md#insn-00876e98)

~~~diff
- 00875ed4 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00876e80 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00875ed4 bytes 482000f0
+ 00876e80 bytes 482000f0
- 00875ed8 ["COPY", "tmp:0:8", ["const:80:8"]]
- 00875ed8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00875ed8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00875ed8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00876e84 ["COPY", "tmp:0:8", ["const:50:8"]]
+ 00876e84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00876e84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00876e84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00875ed8 bytes 08010291
+ 00876e84 bytes 08410191
- 00875eec ["INT_ADD", "register:40f0:8", ["const:875eec:8", "const:4:8"]]
- 00875eec ["CALL", null, ["callee:00c54d90:8"]]
+ 00876e98 ["INT_ADD", "register:40f0:8", ["const:876e98:8", "const:4:8"]]
+ 00876e98 ["CALL", null, ["callee:00c54d90:8"]]
- 00875eec bytes ad770f94
+ 00876e98 bytes be770f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d28d055f507118e1628639fdfa9a1601"></a>

### [`00875f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875f20.md) → [`00876ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876ecc.md) FUN_00876ecc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 65.22% / 新版 65.22%

CFGの説明率　旧版 14.29% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00875f20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00875f20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00875f24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00875f20",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00875f24",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00875f3c",
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
      "00876ecc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00876ed0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00876ee8",
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

- 旧版 [`00875f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875f20.md#insn-00875f20) · [`00875f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875f20.md#insn-00875f24) · [`00875f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875f20.md#insn-00875f3c)

~~~diff
- 00875f20 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00875f20 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00875f20 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00875f20 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00875f20 bytes fd7bbea9
- 00875f24 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00875f24 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00875f24 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00875f24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00875f24 bytes f44f01a9
- 00875f3c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00875f3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00875f3c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-288d2ada3ce52065636cf9faa88e7c09"></a>

### [`00875f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875f7c.md) → [`00876f28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876f28.md) FUN_00876f28

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00876f4c",
      "incomplete_value": false,
      "site": "00876f50",
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
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00875fa0",
      "incomplete_value": false,
      "site": "00875fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:80:8"
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
      "00876f50",
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
      "00876f50",
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

- 旧版 [`00875f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875f7c.md#insn-00875f90) · [`00875f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875f7c.md#insn-00875f9c) · [`00875fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875f7c.md#insn-00875fa0)
- 新版 [`00876f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876f28.md#insn-00876f3c) · [`00876f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876f28.md#insn-00876f48) · [`00876f4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876f28.md#insn-00876f4c)

~~~diff
- 00875f90 ["INT_ADD", "register:40f0:8", ["const:875f90:8", "const:4:8"]]
- 00875f90 ["CALL", null, ["callee:00c58f30:8"]]
+ 00876f3c ["INT_ADD", "register:40f0:8", ["const:876f3c:8", "const:4:8"]]
+ 00876f3c ["CALL", null, ["callee:00c58f30:8"]]
- 00875f90 bytes f4870f94
+ 00876f3c bytes fd870f94
- 00875f9c ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 00876f48 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 00875f9c bytes 492000f0
+ 00876f48 bytes 492000f0
- 00875fa0 ["COPY", "tmp:0:8", ["const:80:8"]]
- 00875fa0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00875fa0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00875fa0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00876f4c ["COPY", "tmp:0:8", ["const:50:8"]]
+ 00876f4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00876f4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00876f4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00875fa0 bytes 29010291
+ 00876f4c bytes 29410191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70edbd30f296695da3a48021ce2cb5fc"></a>

### [`00876060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876060.md) → [`0087700c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/0087700c.md) FUN_0087700c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00875cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00875/00875cd0.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00876c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00876/00876c7c.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00876074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876060.md#insn-00876074) · [`00876080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876060.md#insn-00876080) · [`00876084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876060.md#insn-00876084)
- 新版 [`00877020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/0087700c.md#insn-00877020) · [`0087702c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/0087700c.md#insn-0087702c) · [`00877030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/0087700c.md#insn-00877030)

~~~diff
- 00876074 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00876074 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00877020 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00877020 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00876074 bytes 740100b4
+ 00877020 bytes 740100b4
- 00876080 ["INT_ADD", "register:40f0:8", ["const:876080:8", "const:4:8"]]
- 00876080 ["CALL", null, ["callee:00c54d90:8"]]
+ 0087702c ["INT_ADD", "register:40f0:8", ["const:87702c:8", "const:4:8"]]
+ 0087702c ["CALL", null, ["callee:00c54d90:8"]]
- 00876080 bytes 48770f94
+ 0087702c bytes 59770f94
- 00876084 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00876084 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00877030 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00877030 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00876084 bytes e00000b5
+ 00877030 bytes e00000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6726a966cca5433c7f2795f5559d82c5"></a>

### [`00876138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876138.md) → [`008770e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008770e4.md) FUN_008770e4

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
      "definition_site": "008770e8",
      "incomplete_value": false,
      "site": "008770ec",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087613c",
      "incomplete_value": false,
      "site": "00876140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:110:8"
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
      "008770ec",
      "DATA",
      [
        "storage",
        "00c80110",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008770ec",
      "DATA",
      [
        "storage",
        "00c810e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00876138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876138.md#insn-00876138) · [`0087613c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876138.md#insn-0087613c)
- 新版 [`008770e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008770e4.md#insn-008770e4) · [`008770e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008770e4.md#insn-008770e8)

~~~diff
- 00876138 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 008770e4 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00876138 bytes 482000d0
+ 008770e4 bytes 482000d0
- 0087613c ["COPY", "tmp:0:8", ["const:110:8"]]
- 0087613c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087613c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087613c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008770e8 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 008770e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008770e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008770e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087613c bytes 08410491
+ 008770e8 bytes 08810391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a666430309d79f1c00346b6051149683"></a>

### [`00876148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876148.md) → [`008770f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008770f4.md) FUN_008770f4

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
      "definition_site": "00877104",
      "incomplete_value": false,
      "site": "0087710c",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876158",
      "incomplete_value": false,
      "site": "00876160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:110:8"
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
      "0087710c",
      "DATA",
      [
        "storage",
        "00c80110",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0087710c",
      "DATA",
      [
        "storage",
        "00c810e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00876154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876148.md#insn-00876154) · [`00876158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876148.md#insn-00876158) · [`00876164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876148.md#insn-00876164)
- 新版 [`00877100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008770f4.md#insn-00877100) · [`00877104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008770f4.md#insn-00877104) · [`00877110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008770f4.md#insn-00877110)

~~~diff
- 00876154 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00877100 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00876154 bytes 482000d0
+ 00877100 bytes 482000d0
- 00876158 ["COPY", "tmp:0:8", ["const:110:8"]]
- 00876158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00876158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00876158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00877104 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 00877104 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00877104 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00877104 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00876158 bytes 08410491
+ 00877104 bytes 08810391
- 00876164 ["INT_ADD", "register:40f0:8", ["const:876164:8", "const:4:8"]]
- 00876164 ["CALL", null, ["callee:00c58f40:8"]]
+ 00877110 ["INT_ADD", "register:40f0:8", ["const:877110:8", "const:4:8"]]
+ 00877110 ["CALL", null, ["callee:00c58f40:8"]]
- 00876164 bytes 83870f94
+ 00877110 bytes 8c870f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35143a59d18753a88b70841bfebc0118"></a>

### [`00876188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876188.md) → [`00877134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877134.md) FUN_00877134

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0085b488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b488.md) [`0087674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/0087674c.md) · 呼出先 12件 [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`00597f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f08.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 2件 [`0085c434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c434.md) [`008776f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008776f8.md) · 呼出先 12件 [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047ec3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047ec3c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`00598228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598228.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.06% / 新版 73.06%

CFGの説明率　旧版 53.45% / 新版 62.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008761c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008761cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008761cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008761c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:008761cc",
      "DATA",
      [
        "storage",
        "00c80160",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008761ec",
      "PARAM",
      [
        "storage",
        "002ef79a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0087716c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00877178",
      "DATA",
      [
        "storage",
        "00c81130",
        null,
        "undefined *"
      ]
    ],
    [
      "00877198",
      "PARAM",
      [
        "storage",
        "002ef7da",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008761c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876188.md#insn-008761c0) · [`008761cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876188.md#insn-008761cc) · [`008761d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876188.md#insn-008761d0)

~~~diff
- 008761c0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008761c0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008761c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008761c0 bytes a8831ff8
- 008761cc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008761cc ["COPY", "tmp:1:8", ["register:4008:8"]]
- 008761cc ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008761cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008761cc bytes 080400a9
- 008761d0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 008761d0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 008761d0 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:10:8"]]
- 008761d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 008761d0 bytes 1f400039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bcf82554f56709072d07595fd25061b"></a>

### [`00876584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876584.md) → [`00877530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877530.md) FUN_00877530

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00877548",
      "incomplete_value": false,
      "site": "0087754c",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087659c",
      "incomplete_value": false,
      "site": "008765a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:160:8"
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
      "0087754c",
      "DATA",
      [
        "storage",
        "00c80160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087754c",
      "DATA",
      [
        "storage",
        "00c81130",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00876598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876584.md#insn-00876598) · [`0087659c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876584.md#insn-0087659c) · [`008765ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876584.md#insn-008765ac)
- 新版 [`00877544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877530.md#insn-00877544) · [`00877548`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877530.md#insn-00877548) · [`00877558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877530.md#insn-00877558)

~~~diff
- 00876598 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 00877544 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 00876598 bytes 492000d0
+ 00877544 bytes 492000d0
- 0087659c ["COPY", "tmp:0:8", ["const:160:8"]]
- 0087659c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087659c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087659c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00877548 ["COPY", "tmp:0:8", ["const:130:8"]]
+ 00877548 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00877548 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00877548 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087659c bytes 29810591
+ 00877548 bytes 29c10491
- 008765ac ["INT_ADD", "register:40f0:8", ["const:8765ac:8", "const:4:8"]]
- 008765ac ["CALL", null, ["callee:00c58f50:8"]]
+ 00877558 ["INT_ADD", "register:40f0:8", ["const:877558:8", "const:4:8"]]
+ 00877558 ["CALL", null, ["callee:00c58f50:8"]]
- 008765ac bytes 75860f94
+ 00877558 bytes 7e860f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7172dc4cc68a3c9e4e8aa042ae241a1f"></a>

### [`00876630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876630.md) → [`008775dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008775dc.md) FUN_008775dc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "008775f4",
      "incomplete_value": false,
      "site": "008775f8",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876648",
      "incomplete_value": false,
      "site": "0087664c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:160:8"
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
      "008775f8",
      "DATA",
      [
        "storage",
        "00c80160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008775f8",
      "DATA",
      [
        "storage",
        "00c81130",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00876644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876630.md#insn-00876644) · [`00876648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876630.md#insn-00876648) · [`00876658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876630.md#insn-00876658)
- 新版 [`008775f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008775dc.md#insn-008775f0) · [`008775f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008775dc.md#insn-008775f4) · [`00877604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008775dc.md#insn-00877604)

~~~diff
- 00876644 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 008775f0 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 00876644 bytes 492000d0
+ 008775f0 bytes 492000d0
- 00876648 ["COPY", "tmp:0:8", ["const:160:8"]]
- 00876648 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00876648 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00876648 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008775f4 ["COPY", "tmp:0:8", ["const:130:8"]]
+ 008775f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008775f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008775f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00876648 bytes 29810591
+ 008775f4 bytes 29c10491
- 00876658 ["INT_ADD", "register:40f0:8", ["const:876658:8", "const:4:8"]]
- 00876658 ["CALL", null, ["callee:00c58f50:8"]]
+ 00877604 ["INT_ADD", "register:40f0:8", ["const:877604:8", "const:4:8"]]
+ 00877604 ["CALL", null, ["callee:00c58f50:8"]]
- 00876658 bytes 4a860f94
+ 00877604 bytes 53860f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-789c8ff491d09cb0f334c11c008c03bc"></a>

### [`008766fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/008766fc.md) → [`008776a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008776a8.md) FUN_008776a8

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
      "definition_site": "008776cc",
      "incomplete_value": false,
      "site": "008776cc",
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
            "const:190:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876720",
      "incomplete_value": false,
      "site": "00876720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
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
      "008776cc",
      "DATA",
      [
        "storage",
        "00c801c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008776cc",
      "DATA",
      [
        "storage",
        "00c81190",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00876710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/008766fc.md#insn-00876710) · [`00876718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/008766fc.md#insn-00876718) · [`0087671c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/008766fc.md#insn-0087671c)
- 新版 [`008776bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008776a8.md#insn-008776bc) · [`008776c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008776a8.md#insn-008776c4) · [`008776c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008776a8.md#insn-008776c8)

~~~diff
- 00876710 ["INT_ADD", "register:40f0:8", ["const:876710:8", "const:4:8"]]
- 00876710 ["CALL", null, ["callee:00c58f30:8"]]
+ 008776bc ["INT_ADD", "register:40f0:8", ["const:8776bc:8", "const:4:8"]]
+ 008776bc ["CALL", null, ["callee:00c58f30:8"]]
- 00876710 bytes 14860f94
+ 008776bc bytes 1d860f94
- 00876718 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 008776c4 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00876718 bytes 482000d0
+ 008776c4 bytes 482000d0
- 0087671c ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 0087671c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087671c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087671c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008776c8 ["COPY", "tmp:0:8", ["const:190:8"]]
+ 008776c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008776c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008776c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087671c bytes 08010791
+ 008776c8 bytes 08410691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4738300056a4bdd68f2d9343f51e8dc0"></a>

### [`00876730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876730.md) → [`008776dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008776dc.md) FUN_008776dc

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
      "definition_site": "008776e8",
      "incomplete_value": false,
      "site": "008776e8",
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
            "const:190:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087673c",
      "incomplete_value": false,
      "site": "0087673c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
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
      "008776e8",
      "DATA",
      [
        "storage",
        "00c801c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008776e8",
      "DATA",
      [
        "storage",
        "00c81190",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00876734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876730.md#insn-00876734) · [`00876738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876730.md#insn-00876738)
- 新版 [`008776e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008776dc.md#insn-008776e0) · [`008776e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008776dc.md#insn-008776e4)

~~~diff
- 00876734 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 008776e0 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 00876734 bytes 492000d0
+ 008776e0 bytes 492000d0
- 00876738 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 00876738 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00876738 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00876738 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008776e4 ["COPY", "tmp:0:8", ["const:190:8"]]
+ 008776e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008776e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008776e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00876738 bytes 29010791
+ 008776e4 bytes 29410691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5e45a0773dcd1789633784a5cb370ae"></a>

### [`0087674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/0087674c.md) → [`008776f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008776f8.md) FUN_008776f8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00495414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495414.md) [`008730e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008730e0.md) [`008730f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/008730f0.md) [`00876178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876178.md) [`00876188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876188.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00495734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00495/00495734.md) [`0087408c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/0087408c.md) [`0087409c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00874/0087409c.md) [`00877124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877124.md) [`00877134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877134.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.99% / 新版 96.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008777a4",
      "incomplete_value": false,
      "site": "008777b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008767f8",
      "incomplete_value": false,
      "site": "00876804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "definition_site": "0087781c",
      "incomplete_value": false,
      "site": "00877828",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876870",
      "incomplete_value": false,
      "site": "0087687c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:110:8"
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
      "008777b0",
      "DATA",
      [
        "storage",
        "00c7fce0",
        null,
        "pointer"
      ]
    ],
    [
      "008777fc",
      "READ",
      [
        "storage",
        "00c7fcf0",
        null,
        "undefined *"
      ]
    ],
    [
      "00877828",
      "DATA",
      [
        "storage",
        "00c80110",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008777b0",
      "DATA",
      [
        "storage",
        "00c80cb0",
        null,
        "pointer"
      ]
    ],
    [
      "008777fc",
      "READ",
      [
        "storage",
        "00c80cc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00877828",
      "DATA",
      [
        "storage",
        "00c810e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/0087674c.md#insn-0087678c) · [`008767ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/0087674c.md#insn-008767ac) · [`008767b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/0087674c.md#insn-008767b4)
- 新版 [`00877738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008776f8.md#insn-00877738) · [`00877758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008776f8.md#insn-00877758) · [`00877760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008776f8.md#insn-00877760)

~~~diff
- 0087678c ["INT_ADD", "register:40f0:8", ["const:87678c:8", "const:4:8"]]
- 0087678c ["CALL", null, ["callee:008ba17c:8"]]
+ 00877738 ["INT_ADD", "register:40f0:8", ["const:877738:8", "const:4:8"]]
+ 00877738 ["CALL", null, ["callee:008ba17c:8"]]
- 0087678c bytes 910a0194
+ 00877738 bytes 910a0194
- 008767ac ["INT_ADD", "register:40f0:8", ["const:8767ac:8", "const:4:8"]]
- 008767ac ["CALL", null, ["callee:00c54d60:8"]]
+ 00877758 ["INT_ADD", "register:40f0:8", ["const:877758:8", "const:4:8"]]
+ 00877758 ["CALL", null, ["callee:00c54d60:8"]]
- 008767ac bytes 71750f94
+ 00877758 bytes 82750f94
- 008767b4 ["INT_ADD", "register:40f0:8", ["const:8767b4:8", "const:4:8"]]
- 008767b4 ["CALL", null, ["callee:00495734:8"]]
+ 00877760 ["INT_ADD", "register:40f0:8", ["const:877760:8", "const:4:8"]]
+ 00877760 ["CALL", null, ["callee:00495734:8"]]
- 008767b4 bytes 187bf097
+ 00877760 bytes f577f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b024de0bed66eb13c8355bc397b28992"></a>

### [`00876a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876a18.md) → [`008779c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008779c4.md) FUN_008779c4

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
      "definition_site": "008779e8",
      "incomplete_value": false,
      "site": "008779e8",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876a3c",
      "incomplete_value": false,
      "site": "00876a3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:240:8"
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
      "008779e8",
      "DATA",
      [
        "storage",
        "00c80240",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008779e8",
      "DATA",
      [
        "storage",
        "00c81210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00876a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876a18.md#insn-00876a2c) · [`00876a34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876a18.md#insn-00876a34) · [`00876a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876a18.md#insn-00876a38)
- 新版 [`008779d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008779c4.md#insn-008779d8) · [`008779e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008779c4.md#insn-008779e0) · [`008779e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008779c4.md#insn-008779e4)

~~~diff
- 00876a2c ["INT_ADD", "register:40f0:8", ["const:876a2c:8", "const:4:8"]]
- 00876a2c ["CALL", null, ["callee:00c58f30:8"]]
+ 008779d8 ["INT_ADD", "register:40f0:8", ["const:8779d8:8", "const:4:8"]]
+ 008779d8 ["CALL", null, ["callee:00c58f30:8"]]
- 00876a2c bytes 4d850f94
+ 008779d8 bytes 56850f94
- 00876a34 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 008779e0 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00876a34 bytes 482000d0
+ 008779e0 bytes 482000d0
- 00876a38 ["COPY", "tmp:0:8", ["const:240:8"]]
- 00876a38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00876a38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00876a38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008779e4 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 008779e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008779e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008779e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00876a38 bytes 08010991
+ 008779e4 bytes 08410891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ce41e7ed2bdb8a35c338fbaa5a028d1"></a>

### [`00876a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876a4c.md) → [`008779f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008779f8.md) FUN_008779f8

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
      "definition_site": "00877a04",
      "incomplete_value": false,
      "site": "00877a04",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876a58",
      "incomplete_value": false,
      "site": "00876a58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00877a04",
      "DATA",
      [
        "storage",
        "00c80240",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00877a04",
      "DATA",
      [
        "storage",
        "00c81210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00876a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876a4c.md#insn-00876a50) · [`00876a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876a4c.md#insn-00876a54)
- 新版 [`008779fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008779f8.md#insn-008779fc) · [`00877a00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/008779f8.md#insn-00877a00)

~~~diff
- 00876a50 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 008779fc ["COPY", "register:4048:8", ["const:c81000:8"]]
- 00876a50 bytes 492000d0
+ 008779fc bytes 492000d0
- 00876a54 ["COPY", "tmp:0:8", ["const:240:8"]]
- 00876a54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00876a54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00876a54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00877a00 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 00877a00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00877a00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00877a00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00876a54 bytes 29010991
+ 00877a00 bytes 29410891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-681fb7c43c800c02147ff10aa112dd21"></a>

### [`00876a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876a68.md) → [`00877a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877a14.md) FUN_00877a14

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0044f3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f3d0.md) [`0044f47c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f47c.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0044f6f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044f/0044f6f0.md) [`0044f79c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044f/0044f79c.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

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
      "site": "00877a5c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00876ab0",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "site": "00877ad0",
      "value": [
        "leaf",
        "ram:48d058:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00876b24",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00877a5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00877ad0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ],
  "added": [
    [
      "00877a5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00877ad0",
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

- 旧版 [`00876ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876a68.md#insn-00876ab0) · [`00876b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876a68.md#insn-00876b24) · [`00876aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876a68.md#insn-00876aac)
- 新版 [`00877a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877a14.md#insn-00877a5c) · [`00877ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877a14.md#insn-00877ad0) · [`00877a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877a14.md#insn-00877a58)

~~~diff
- 00876ab0 ["INT_ADD", "register:40f0:8", ["const:876ab0:8", "const:4:8"]]
- 00876ab0 ["CALL", null, ["ram:47ad34:8"]]
+ 00877a5c ["INT_ADD", "register:40f0:8", ["const:877a5c:8", "const:4:8"]]
+ 00877a5c ["CALL", null, ["ram:47b054:8"]]
- 00876ab0 bytes a110f097
+ 00877a5c bytes 7e0df097
- 00876b24 ["INT_ADD", "register:40f0:8", ["const:876b24:8", "const:4:8"]]
- 00876b24 ["CALL", null, ["ram:48cd38:8"]]
+ 00877ad0 ["INT_ADD", "register:40f0:8", ["const:877ad0:8", "const:4:8"]]
+ 00877ad0 ["CALL", null, ["ram:48d058:8"]]
- 00876b24 bytes 8558f097
+ 00877ad0 bytes 6255f097
- 00876aac ["INT_ADD", "register:40f0:8", ["const:876aac:8", "const:4:8"]]
- 00876aac ["CALL", null, ["callee:008ba17c:8"]]
+ 00877a58 ["INT_ADD", "register:40f0:8", ["const:877a58:8", "const:4:8"]]
+ 00877a58 ["CALL", null, ["callee:008ba17c:8"]]
- 00876aac bytes c9090194
+ 00877a58 bytes c9090194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfc7f4b5c0d8790b1b9df50e953176dc"></a>

### [`00876bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876bcc.md) → [`00877b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877b78.md) _INIT_157

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
      "definition_site": "00877bb4",
      "incomplete_value": true,
      "site": "00877bd0",
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
      "definition_site": "00876c08",
      "incomplete_value": true,
      "site": "00876c24",
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
      "definition_site": "00877bd8",
      "incomplete_value": true,
      "site": "00877bf4",
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
      "definition_site": "00876c2c",
      "incomplete_value": true,
      "site": "00876c48",
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
      "definition_site": "00877bf8",
      "incomplete_value": true,
      "site": "00877c14",
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
      "definition_site": "00876c4c",
      "incomplete_value": true,
      "site": "00876c68",
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
      "00877bb4",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00877bd8",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00877bf8",
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
      "00877bb4",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "00877bd8",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "00877bf8",
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

- 旧版 [`00876d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876bcc.md#insn-00876d2c) · [`00876e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876bcc.md#insn-00876e00) · [`00876bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876bcc.md#insn-00876bf4)
- 新版 [`00877cd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877b78.md#insn-00877cd8) · [`00877dac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877b78.md#insn-00877dac) · [`00877ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877b78.md#insn-00877ba0)

~~~diff
- 00876d2c ["INT_ADD", "register:40f0:8", ["const:876d2c:8", "const:4:8"]]
- 00876d2c ["CALL", null, ["callee:0043bb58:8"]]
+ 00877cd8 ["INT_ADD", "register:40f0:8", ["const:877cd8:8", "const:4:8"]]
+ 00877cd8 ["CALL", null, ["callee:0043bb58:8"]]
- 00876d2c bytes c312ef97
+ 00877cd8 bytes a00fef97
- 00876e00 ["INT_ADD", "register:40f0:8", ["const:876e00:8", "const:4:8"]]
- 00876e00 ["CALL", null, ["callee:00c58ed0:8"]]
+ 00877dac ["INT_ADD", "register:40f0:8", ["const:877dac:8", "const:4:8"]]
+ 00877dac ["CALL", null, ["callee:00c58ed0:8"]]
- 00876e00 bytes 40840f94
+ 00877dac bytes 49840f94
- 00876bf4 ["COPY", "register:4098:8", ["const:1123000:8"]]
+ 00877ba0 ["COPY", "register:4098:8", ["const:1124000:8"]]
- 00876bf4 bytes 734500b0
+ 00877ba0 bytes 734500b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd86159af52d5cd4f6ef6c72e48b5b8f"></a>

### [`00876f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876f5c.md) → [`00877f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877f08.md) FUN_00877f08

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00872a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/00872a68.md) · 呼出先 26件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`00444120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444120.md) [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md)
- 新版 呼出元 1件 [`00873a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00873/00873a14.md) · 呼出先 26件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00442e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442e98.md) [`00444440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00444/00444440.md) [`00445180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00445/00445180.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 76.60% / 新版 73.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 11件, `store_destination` 2件, `store_value` 10件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00877f84",
      "incomplete_value": true,
      "site": "00877f94",
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
                "const:998:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876fd8",
      "incomplete_value": true,
      "site": "00876fe8",
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
                "const:8c9:8"
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
      "definition_site": "00877f88",
      "incomplete_value": true,
      "site": "00877f98",
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00876fdc",
      "incomplete_value": true,
      "site": "00876fec",
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
                "const:f:8"
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
      "definition_site": "00877f8c",
      "incomplete_value": true,
      "site": "00877f9c",
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
      "definition_site": "00876fe0",
      "incomplete_value": true,
      "site": "00876ff0",
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
      "00877f68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "00877f84",
      "READ",
      [
        "storage",
        "002b78c9",
        null,
        "string"
      ]
    ],
    [
      "00877f88",
      "READ",
      [
        "storage",
        "002b78d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00877f68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048d058"
      ]
    ],
    [
      "00877f84",
      "READ",
      [
        "storage",
        "002b7998",
        null,
        "string"
      ]
    ],
    [
      "00877f88",
      "READ",
      [
        "storage",
        "002b79a7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00876fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876f5c.md#insn-00876fbc) · [`00877150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876f5c.md#insn-00877150) · [`008771dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876f5c.md#insn-008771dc)
- 新版 [`00877f68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877f08.md#insn-00877f68) · [`008780fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877f08.md#insn-008780fc) · [`00878188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877f08.md#insn-00878188)

~~~diff
- 00876fbc ["INT_ADD", "register:40f0:8", ["const:876fbc:8", "const:4:8"]]
- 00876fbc ["CALL", null, ["ram:48cd38:8"]]
+ 00877f68 ["INT_ADD", "register:40f0:8", ["const:877f68:8", "const:4:8"]]
+ 00877f68 ["CALL", null, ["ram:48d058:8"]]
- 00876fbc bytes 5f57f097
+ 00877f68 bytes 3c54f097
- 00877150 ["INT_ADD", "register:40f0:8", ["const:877150:8", "const:4:8"]]
- 00877150 ["CALL", null, ["ram:48cd38:8"]]
+ 008780fc ["INT_ADD", "register:40f0:8", ["const:8780fc:8", "const:4:8"]]
+ 008780fc ["CALL", null, ["ram:48d058:8"]]
- 00877150 bytes fa56f097
+ 008780fc bytes d753f097
- 008771dc ["INT_ADD", "register:40f0:8", ["const:8771dc:8", "const:4:8"]]
- 008771dc ["CALL", null, ["ram:48cd38:8"]]
+ 00878188 ["INT_ADD", "register:40f0:8", ["const:878188:8", "const:4:8"]]
+ 00878188 ["CALL", null, ["ram:48d058:8"]]
- 008771dc bytes d756f097
+ 00878188 bytes b453f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d083763d171c6e6fe1612d217a27215b"></a>

### [`00877918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877918.md) → [`008788c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00878/008788c4.md) FUN_008788c4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00876f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876f5c.md) · 呼出先 5件 [`00877c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877c78.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c58500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58500.md)
- 新版 呼出元 1件 [`00877f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877f08.md) · 呼出先 5件 [`00878c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00878/00878c24.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c594d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c594d0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 86.90% / 新版 86.90%

CFGの説明率　旧版 62.96% / 新版 58.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00877a14"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00877a24"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008789c0"
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
      "unmatched:00877a14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008789ec"
      ]
    ],
    [
      "unmatched:00877a20",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c54d90"
      ]
    ],
    [
      "unmatched:00877a24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008789ec"
      ]
    ]
  ],
  "added": [
    [
      "008789c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008789ec"
      ]
    ],
    [
      "008789cc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c54d90"
      ]
    ],
    [
      "008789d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008789ec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00877990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877918.md#insn-00877990) · [`00877a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877918.md#insn-00877a14) · [`00877a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877918.md#insn-00877a20)
- 新版 [`0087893c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00878/008788c4.md#insn-0087893c)

~~~diff
- 00877990 ["INT_ADD", "register:40f0:8", ["const:877990:8", "const:4:8"]]
- 00877990 ["CALL", null, ["callee:00c58f20:8"]]
+ 0087893c ["INT_ADD", "register:40f0:8", ["const:87893c:8", "const:4:8"]]
+ 0087893c ["CALL", null, ["callee:00c58f20:8"]]
- 00877990 bytes 70810f94
+ 0087893c bytes 79810f94
- 00877a14 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00877a14 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00877a14 bytes 750100b4
- 00877a20 ["INT_ADD", "register:40f0:8", ["const:877a20:8", "const:4:8"]]
- 00877a20 ["CALL", null, ["callee:00c54d90:8"]]
- 00877a20 bytes e0700f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68f24ca58b2b1a40a66aba6359d61f9c"></a>

### [`00877a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877a68.md) → [`00878a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00878/00878a14.md) FUN_00878a14

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00876f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876f5c.md) · 呼出先 6件 [`00446a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446a88.md) [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c58240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58240.md)
- 新版 呼出元 1件 [`00877f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00877/00877f08.md) · 呼出先 6件 [`00446da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00446/00446da8.md) [`00c58f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f00.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59170.md) [`00c59210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59210.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00877a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877a68.md#insn-00877a7c) · [`00877a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877a68.md#insn-00877a84) · [`00877a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877a68.md#insn-00877a8c)
- 新版 [`00878a28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00878/00878a14.md#insn-00878a28) · [`00878a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00878/00878a14.md#insn-00878a30) · [`00878a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00878/00878a14.md#insn-00878a38)

~~~diff
- 00877a7c ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00877a7c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00878a28 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00878a28 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00877a7c bytes f30100b4
+ 00878a28 bytes f30100b4
- 00877a84 ["INT_ADD", "register:40f0:8", ["const:877a84:8", "const:4:8"]]
- 00877a84 ["CALL", null, ["callee:00446da8:8"]]
+ 00878a30 ["INT_ADD", "register:40f0:8", ["const:878a30:8", "const:4:8"]]
+ 00878a30 ["CALL", null, ["callee:00446da8:8"]]
- 00877a84 bytes 013cef97
+ 00878a30 bytes de38ef97
- 00877a8c ["INT_ADD", "register:40f0:8", ["const:877a8c:8", "const:4:8"]]
- 00877a8c ["CALL", null, ["callee:00c59210:8"]]
+ 00878a38 ["INT_ADD", "register:40f0:8", ["const:878a38:8", "const:4:8"]]
+ 00878a38 ["CALL", null, ["callee:00c59210:8"]]
- 00877a8c bytes ed810f94
+ 00878a38 bytes f6810f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-184914336ff0db109c0ddf11ccf4b758"></a>

### [`00877ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877ac8.md) → [`00878a74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00878/00878a74.md) FUN_00878a74

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`00597e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597e88.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0085b488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b488.md) [`00877da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877da8.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00597dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/00597dec.md) [`005981a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/005981a8.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`0085c434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c434.md) [`00878d54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00878/00878d54.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 64.00% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00877aec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00878a98"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00877af0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00877aec",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00877af0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00878b80"
      ]
    ],
    [
      "00878b2c",
      "PARAM",
      [
        "storage",
        "00877da8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00878a98",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00878a9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00878b80"
      ]
    ],
    [
      "00878b2c",
      "PARAM",
      [
        "storage",
        "00878d54",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00877aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877ac8.md#insn-00877aec) · [`00877af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877ac8.md#insn-00877af0) · [`00877b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877ac8.md#insn-00877b68)
- 新版 [`00878b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00878/00878a74.md#insn-00878b14)

~~~diff
- 00877aec ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00877aec ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00877aec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00877aec bytes a8831ff8
- 00877af0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00877af0 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00877af0 bytes 23070054
- 00877b68 ["INT_ADD", "register:40f0:8", ["const:877b68:8", "const:4:8"]]
- 00877b68 ["CALL", null, ["callee:00c58f30:8"]]
+ 00878b14 ["INT_ADD", "register:40f0:8", ["const:878b14:8", "const:4:8"]]
+ 00878b14 ["CALL", null, ["callee:00c58f30:8"]]
- 00877b68 bytes fe800f94
+ 00878b14 bytes 07810f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8b624cf1437652c30770fce229355a4"></a>

### [`00877ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877ef0.md) → [`00878e9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00878/00878e9c.md) _INIT_158

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.71% / 新版 75.71%

CFGの説明率　旧版 87.50% / 新版 93.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00877f20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00877f48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00877f6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00877f20",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00877f2c",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00877f48",
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
      "00878ecc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00878ed8",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "00878ef4",
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

- 旧版 [`00877f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877ef0.md#insn-00877f20) · [`00877f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877ef0.md#insn-00877f48) · [`00877f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877ef0.md#insn-00877f6c)

~~~diff
- 00877f20 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00877f20 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00877f20 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00877f20 bytes a9831ff8
- 00877f48 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00877f48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00877f48 bytes e013813c
- 00877f6c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00877f6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00877f6c bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c58b7b43b68813f2617ec9a172f9e460"></a>

### [`00878448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878448.md) → [`008793f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00879/008793f4.md) FUN_008793f4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 19件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`006eed04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ee/006eed04.md) [`006ff698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff698.md) [`0070d410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070d/0070d410.md) [`0075ba1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075ba1c.md) · 呼出先 6件 [`0071bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bf30.md) [`008787b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/008787b0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md)
- 新版 呼出元 19件 [`005fea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fea5c.md) [`006ef0b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ef/006ef0b4.md) [`006ffa48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ff/006ffa48.md) [`0070d7c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0070d/0070d7c0.md) [`0075bdcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075b/0075bdcc.md) · 呼出先 6件 [`0071c2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c2e0.md) [`0087975c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00879/0087975c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 63.74% / 新版 63.74%

CFGの説明率　旧版 25.93% / 新版 29.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_call_alignment` 8件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087848c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00878508"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087850c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087848c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00878508",
      "DATA",
      [
        "storage",
        "002affcb",
        null,
        null
      ]
    ],
    [
      "unmatched:00878508",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00879438",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "008794b4",
      "DATA",
      [
        "storage",
        "002b00a2",
        null,
        null
      ]
    ],
    [
      "008794b4",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087848c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878448.md#insn-0087848c) · [`00878508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878448.md#insn-00878508) · [`0087850c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878448.md#insn-0087850c)

~~~diff
- 0087848c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0087848c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0087848c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0087848c bytes a8831ff8
- 00878508 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00878508 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 00878508 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00878508 bytes a8031cf8
- 0087850c ["COPY", "tmp:0:4", ["const:0:4"]]
- 0087850c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0087850c ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 0087850c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 0087850c bytes bf831cb8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9e84cf9f429f05360c330a6e921214a"></a>

### [`008787b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/008787b0.md) → [`0087975c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00879/0087975c.md) FUN_0087975c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00878448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878448.md) [`00878c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878c44.md) [`00878f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878f30.md) [`00878f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878f48.md) [`008792f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/008792f4.md) · 呼出先 11件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`007522d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/007522d8.md) [`007842d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00784/007842d8.md) [`00b3c978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c978.md)
- 新版 呼出元 5件 [`008793f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00879/008793f4.md) [`00879bf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00879/00879bf0.md) [`00879edc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00879/00879edc.md) [`00879ef4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00879/00879ef4.md) [`0087a2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087a/0087a2a0.md) · 呼出先 11件 [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`00752688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/00752688.md) [`007846b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00784/007846b4.md) [`00b3d96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3d96c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.74% / 新版 79.74%

CFGの説明率　旧版 44.00% / 新版 30.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00878848"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008788b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008788b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00878848",
      "DATA",
      [
        "storage",
        "002b3031",
        null,
        null
      ]
    ],
    [
      "unmatched:00878848",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "00879818",
      "DATA",
      [
        "storage",
        "002b3031",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008797f4",
      "DATA",
      [
        "storage",
        "002b307b",
        null,
        null
      ]
    ],
    [
      "008797f4",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "00879818",
      "DATA",
      [
        "storage",
        "002b307b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00878848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/008787b0.md#insn-00878848) · [`008788b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/008787b0.md#insn-008788b0) · [`008788b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/008787b0.md#insn-008788b4)

~~~diff
- 00878848 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00878848 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 00878848 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00878848 bytes a8831bf8
- 008788b0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008788b0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 008788b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008788b0 bytes a8831bf8
- 008788b4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 008788b4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 008788b4 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 008788b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 008788b4 bytes bf031cb8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6666fa8a717151e46905825baa0c37f9"></a>

### [`00878c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878c44.md) → [`00879bf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00879/00879bf0.md) FUN_00879bf0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`00611ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00611/00611ea0.md) [`00696e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e7c.md) [`007200e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00720/007200e8.md) [`0090dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090d/0090dd50.md) [`009472c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00947/009472c0.md) · 呼出先 6件 [`0071bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bf30.md) [`008787b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/008787b0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md)
- 新版 呼出元 5件 [`00612250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00612/00612250.md) [`0069722c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/0069722c.md) [`00720498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00720/00720498.md) [`0090ecfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0090e/0090ecfc.md) [`0094826c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00948/0094826c.md) · 呼出先 6件 [`0071c2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c2e0.md) [`0087975c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00879/0087975c.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5b8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8e0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.20% / 新版 90.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00879ca0",
      "incomplete_value": false,
      "site": "00879ca0",
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
            "const:a2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878cf4",
      "incomplete_value": false,
      "site": "00878cf4",
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
            "const:fcb:8"
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
      "definition_site": "00879d14",
      "incomplete_value": false,
      "site": "00879d14",
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
            "const:31f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878d68",
      "incomplete_value": false,
      "site": "00878d68",
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
            "const:252:8"
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
      "definition_site": "00879d84",
      "incomplete_value": false,
      "site": "00879d84",
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
            "const:225:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878dd8",
      "incomplete_value": false,
      "site": "00878dd8",
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
            "const:14e:8"
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
      "00879ca0",
      "DATA",
      [
        "storage",
        "002affcb",
        null,
        null
      ]
    ],
    [
      "00879ce8",
      "DATA",
      [
        "storage",
        "002affcb",
        null,
        null
      ]
    ],
    [
      "00879d00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ]
  ],
  "added": [
    [
      "00879ca0",
      "DATA",
      [
        "storage",
        "002b00a2",
        null,
        null
      ]
    ],
    [
      "00879ce8",
      "DATA",
      [
        "storage",
        "002b00a2",
        null,
        null
      ]
    ],
    [
      "00879d00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c2e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00878d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878c44.md#insn-00878d54) · [`00878dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878c44.md#insn-00878dc8) · [`00878e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878c44.md#insn-00878e50)
- 新版 [`00879d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00879/00879bf0.md#insn-00879d00) · [`00879d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00879/00879bf0.md#insn-00879d74) · [`00879dfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00879/00879bf0.md#insn-00879dfc)

~~~diff
- 00878d54 ["INT_ADD", "register:40f0:8", ["const:878d54:8", "const:4:8"]]
- 00878d54 ["CALL", null, ["ram:71bf30:8"]]
+ 00879d00 ["INT_ADD", "register:40f0:8", ["const:879d00:8", "const:4:8"]]
+ 00879d00 ["CALL", null, ["ram:71c2e0:8"]]
- 00878d54 bytes 778cfa97
+ 00879d00 bytes 7889fa97
- 00878dc8 ["INT_ADD", "register:40f0:8", ["const:878dc8:8", "const:4:8"]]
- 00878dc8 ["CALL", null, ["ram:71bf30:8"]]
+ 00879d74 ["INT_ADD", "register:40f0:8", ["const:879d74:8", "const:4:8"]]
+ 00879d74 ["CALL", null, ["ram:71c2e0:8"]]
- 00878dc8 bytes 5a8cfa97
+ 00879d74 bytes 5b89fa97
- 00878e50 ["INT_ADD", "register:40f0:8", ["const:878e50:8", "const:4:8"]]
- 00878e50 ["CALL", null, ["callee:0087975c:8"]]
+ 00879dfc ["INT_ADD", "register:40f0:8", ["const:879dfc:8", "const:4:8"]]
+ 00879dfc ["CALL", null, ["callee:0087975c:8"]]
- 00878e50 bytes 58feff97
+ 00879dfc bytes 58feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-345581ee67dcda55a7c8d8234a3e5cc6"></a>

### [`00878f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878f60.md) → [`00879f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00879/00879f0c.md) FUN_00879f0c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0075d7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075d/0075d7b4.md) · 呼出先 11件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`007522d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/007522d8.md) [`007842d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00784/007842d8.md) [`00b3c978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3c978.md)
- 新版 呼出元 1件 [`0075db64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075d/0075db64.md) · 呼出先 11件 [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`00752688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/00752688.md) [`007846b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00784/007846b4.md) [`00b3d96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3d/00b3d96c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 61.54% / 新版 64.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00879f94",
      "incomplete_value": false,
      "site": "00879f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:7b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00878fe8",
      "incomplete_value": false,
      "site": "00878fe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:31:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00879050"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008790b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00879f94",
      "DATA",
      [
        "storage",
        "002b3031",
        null,
        null
      ]
    ],
    [
      "00879fb8",
      "DATA",
      [
        "storage",
        "002b3031",
        null,
        null
      ]
    ],
    [
      "00879fdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0087903c"
      ]
    ]
  ],
  "added": [
    [
      "00879f94",
      "DATA",
      [
        "storage",
        "002b307b",
        null,
        null
      ]
    ],
    [
      "00879fb8",
      "DATA",
      [
        "storage",
        "002b307b",
        null,
        null
      ]
    ],
    [
      "00879fdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00879fe8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878f60.md#insn-00879038) · [`0087903c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878f60.md#insn-0087903c) · [`00879040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878f60.md#insn-00879040)

~~~diff
- 00879038 ["INT_ADD", "register:40f0:8", ["const:879038:8", "const:4:8"]]
- 00879038 ["CALL", null, ["callee:00c58f50:8"]]
- 00879038 bytes d27b0f94
- 0087903c ["INT_ADD", "register:40f0:8", ["const:87903c:8", "const:4:8"]]
- 0087903c ["CALL", null, ["ram:48cd38:8"]]
- 0087903c bytes 3f4ff097
- 00879040 ["INT_ADD", "register:40f0:8", ["const:879040:8", "const:4:8"]]
- 00879040 ["CALL", null, ["callee:0048d1e4:8"]]
- 00879040 bytes a14ff097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1d983f7bb4a7ae1a32f1a1439cae2b1"></a>

### [`0087930c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/0087930c.md) → [`0087a2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087a/0087a2b8.md) _INIT_159

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 48.02% / 新版 48.02%

CFGの説明率　旧版 56.76% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 45件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00879310"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00879310"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00879314"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00879310",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00879314",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00879318",
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
      "0087a2bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0087a2c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0087a2c4",
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

- 旧版 [`00879310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/0087930c.md#insn-00879310) · [`00879314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/0087930c.md#insn-00879314) · [`00879318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/0087930c.md#insn-00879318)

~~~diff
- 00879310 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00879310 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00879310 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00879310 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00879310 bytes fd7b0fa9
- 00879314 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00879314 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00879314 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00879314 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00879314 bytes fc5710a9
- 00879318 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00879318 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00879318 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00879318 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00879318 bytes f44f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b5d9d4f70a3785c37149cb39b457064"></a>

### [`0087969c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/0087969c.md) → [`0087a648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087a/0087a648.md) FUN_0087a648

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0087bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087bc9c.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004939d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004939d8.md) [`00562734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00562/00562734.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0087cc48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087cc48.md) · 呼出先 6件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00493cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493cf8.md) [`00562a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/00562a54.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.42% / 新版 84.42%

CFGの説明率　旧版 29.03% / 新版 20.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008796b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00879710"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0087a664"
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
      "unmatched:008796b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008796d8",
      "PARAM",
      [
        "storage",
        "011236f8",
        null,
        "undefined2"
      ]
    ],
    [
      "unmatched:008796f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087a70c"
      ]
    ]
  ],
  "added": [
    [
      "0087a664",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0087a684",
      "PARAM",
      [
        "storage",
        "011246b8",
        null,
        "undefined2"
      ]
    ],
    [
      "0087a6a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087a70c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008796b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/0087969c.md#insn-008796b8) · [`008796e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/0087969c.md#insn-008796e4) · [`008796f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/0087969c.md#insn-008796f4)
- 新版 [`0087a690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087a/0087a648.md#insn-0087a690)

~~~diff
- 008796b8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008796b8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008796b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008796b8 bytes a8831ff8
- 008796e4 ["INT_ADD", "register:40f0:8", ["const:8796e4:8", "const:4:8"]]
- 008796e4 ["CALL", null, ["callee:00562a54:8"]]
+ 0087a690 ["INT_ADD", "register:40f0:8", ["const:87a690:8", "const:4:8"]]
+ 0087a690 ["CALL", null, ["callee:00562a54:8"]]
- 008796e4 bytes 14a4f397
+ 0087a690 bytes f1a0f397
- 008796f4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008796f4 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 008796f4 bytes 61030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-608c299af430b20d6644bc3d702260ad"></a>

### [`0087980c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/0087980c.md) → [`0087a7b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087a/0087a7b8.md) _INIT_160

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00bc5880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5880.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_store_alignment

命令の説明率　旧版 46.12% / 新版 46.12%

CFGの説明率　旧版 93.33% / 新版 65.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 4件, `store_value` 3件, `unresolved_store_alignment` 45件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00879810"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00879810"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00879814"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00879810",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00879814",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00879818",
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
      "0087a7bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0087a7c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0087a7c4",
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

- 旧版 [`00879810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/0087980c.md#insn-00879810) · [`00879814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/0087980c.md#insn-00879814) · [`00879818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/0087980c.md#insn-00879818)

~~~diff
- 00879810 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00879810 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00879810 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00879810 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00879810 bytes fd7b0fa9
- 00879814 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00879814 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00879814 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00879814 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00879814 bytes fc5710a9
- 00879818 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00879818 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00879818 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00879818 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00879818 bytes f44f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94a0ab20203cc3fdd4bad77f62fae186"></a>

### [`00879de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879de0.md) → [`0087ad8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087a/0087ad8c.md) FUN_0087ad8c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005b1910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1910.md) · 呼出先 10件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0087a360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087a360.md) [`0087b414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b414.md) [`0087bc1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087bc1c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`005b1cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b1/005b1cc0.md) · 呼出先 10件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0087b30c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087b/0087b30c.md) [`0087c3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c3c0.md) [`0087cbc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087cbc8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.44% / 新版 95.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087ae14",
      "incomplete_value": true,
      "site": "0087ae20",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879e68",
      "incomplete_value": true,
      "site": "00879e74",
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
                "const:20:8"
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
      "definition_site": "0087ae10",
      "incomplete_value": true,
      "site": "0087ae24",
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
                "const:d67:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00879e64",
      "incomplete_value": true,
      "site": "00879e78",
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
                "const:c0f:8"
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
      "definition_site": "0087ae10",
      "incomplete_value": true,
      "site": "0087ae24",
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
      "definition_site": "00879e64",
      "incomplete_value": true,
      "site": "00879e78",
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
      "0087ae10",
      "READ",
      [
        "storage",
        "002a6c0f",
        null,
        null
      ]
    ],
    [
      "0087ae10",
      "READ",
      [
        "storage",
        "002a6c1f",
        null,
        null
      ]
    ],
    [
      "0087ae14",
      "READ",
      [
        "storage",
        "002a6c2f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0087ae10",
      "READ",
      [
        "storage",
        "002a6d67",
        null,
        null
      ]
    ],
    [
      "0087ae10",
      "READ",
      [
        "storage",
        "002a6d77",
        null,
        null
      ]
    ],
    [
      "0087ae14",
      "READ",
      [
        "storage",
        "002a6d87",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00879e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879de0.md#insn-00879e44) · [`00879e54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879de0.md#insn-00879e54) · [`00879e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879de0.md#insn-00879e5c)
- 新版 [`0087adf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087a/0087ad8c.md#insn-0087adf0) · [`0087ae00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087a/0087ad8c.md#insn-0087ae00) · [`0087ae08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087a/0087ad8c.md#insn-0087ae08)

~~~diff
- 00879e44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00879e44 ["INT_ADD", "register:40f0:8", ["const:879e44:8", "const:4:8"]]
- 00879e44 ["CALLIND", null, ["register:0:8"]]
+ 0087adf0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087adf0 ["INT_ADD", "register:40f0:8", ["const:87adf0:8", "const:4:8"]]
+ 0087adf0 ["CALLIND", null, ["register:0:8"]]
- 00879e44 bytes 00013fd6
+ 0087adf0 bytes 00013fd6
- 00879e54 ["INT_ADD", "register:40f0:8", ["const:879e54:8", "const:4:8"]]
- 00879e54 ["CALL", null, ["callee:00c58f30:8"]]
+ 0087ae00 ["INT_ADD", "register:40f0:8", ["const:87ae00:8", "const:4:8"]]
+ 0087ae00 ["CALL", null, ["callee:00c58f30:8"]]
- 00879e54 bytes 43780f94
+ 0087ae00 bytes 4c780f94
- 00879e5c ["COPY", "tmp:0:8", ["const:c0f:8"]]
- 00879e5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00879e5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00879e5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087ae08 ["COPY", "tmp:0:8", ["const:d67:8"]]
+ 0087ae08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087ae08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087ae08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00879e5c bytes 293d3091
+ 0087ae08 bytes 299d3591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc11e1ba4a723167a52c9bcd29979a28"></a>

### [`0087a360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087a360.md) → [`0087b30c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087b/0087b30c.md) FUN_0087b30c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00879de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879de0.md) [`00b344ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b344ac.md) · 呼出先 7件 [`0087b4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b4a0.md) [`0087b5f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b5f8.md) [`0087b7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b7d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`0087ad8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087a/0087ad8c.md) [`00b354a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b354a0.md) · 呼出先 7件 [`0087c44c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c44c.md) [`0087c5a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c5a4.md) [`0087c77c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c77c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.53% / 新版 74.53%

CFGの説明率　旧版 11.86% / 新版 18.42%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 2件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087a364"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087a364"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087a368"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087a364",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087a368",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087a36c",
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
      "0087b310",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0087b314",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0087b318",
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

- 旧版 [`0087a364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087a360.md#insn-0087a364) · [`0087a368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087a360.md#insn-0087a368) · [`0087a36c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087a360.md#insn-0087a36c)

~~~diff
- 0087a364 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087a364 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087a364 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 0087a364 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087a364 bytes fd7b09a9
- 0087a368 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:a0:8"]]
- 0087a368 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0087a368 bytes f55300f9
- 0087a36c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0087a36c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0087a36c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 0087a36c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087a36c bytes f44f0ba9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fb75bce337d932014d7699d8f866f62"></a>

### [`0087aa68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087aa68.md) → [`0087ba14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087b/0087ba14.md) FUN_0087ba14

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0087a7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087a7a0.md) [`00b34f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b34/00b34f40.md) · 呼出先 7件 [`0087b4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b4a0.md) [`0087bff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087bff8.md) [`0087c1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c1d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`0087b74c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087b/0087b74c.md) [`00b35f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b35/00b35f34.md) · 呼出先 7件 [`0087c44c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c44c.md) [`0087cfa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087cfa4.md) [`0087d17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d17c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 94.34% / 新版 94.34%

CFGの説明率　旧版 73.53% / 新版 67.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_call_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087badc",
      "incomplete_value": false,
      "site": "0087badc",
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
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087ab30",
      "incomplete_value": false,
      "site": "0087ab30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:458:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0087aaa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0087ba7c",
      "incomplete_value": false,
      "site": "0087ba94",
      "value": [
        "leaf",
        "const:87cfa4:8"
      ]
    },
    "old": {
      "definition_site": "0087aad0",
      "incomplete_value": false,
      "site": "0087aae8",
      "value": [
        "leaf",
        "const:87bff8:8"
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
      "0087ba7c",
      "PARAM",
      [
        "storage",
        "0087bff8",
        null,
        null
      ]
    ],
    [
      "0087badc",
      "DATA",
      [
        "storage",
        "00c80458",
        null,
        "undefined *"
      ]
    ],
    [
      "0087bb5c",
      "READ",
      [
        "storage",
        "00c80480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087ba7c",
      "PARAM",
      [
        "storage",
        "0087cfa4",
        null,
        null
      ]
    ],
    [
      "0087badc",
      "DATA",
      [
        "storage",
        "00c81428",
        null,
        "undefined *"
      ]
    ],
    [
      "0087bb5c",
      "READ",
      [
        "storage",
        "00c81450",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087aaa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087aa68.md#insn-0087aaa8) · [`0087aae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087aa68.md#insn-0087aae8) · [`0087abe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087aa68.md#insn-0087abe4)
- 新版 [`0087ba94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087b/0087ba14.md#insn-0087ba94)

~~~diff
- 0087aaa8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087aaa8 ["INT_ADD", "register:40f0:8", ["const:87aaa8:8", "const:4:8"]]
- 0087aaa8 ["CALLIND", null, ["register:0:8"]]
- 0087aaa8 bytes 20013fd6
- 0087aae8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087aae8 ["INT_ADD", "register:40f0:8", ["const:87aae8:8", "const:4:8"]]
- 0087aae8 ["CALLIND", null, ["register:0:8"]]
+ 0087ba94 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087ba94 ["INT_ADD", "register:40f0:8", ["const:87ba94:8", "const:4:8"]]
+ 0087ba94 ["CALLIND", null, ["register:0:8"]]
- 0087aae8 bytes 20013fd6
+ 0087ba94 bytes 20013fd6
- 0087abe4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087abe4 ["INT_ADD", "register:40f0:8", ["const:87abe4:8", "const:4:8"]]
- 0087abe4 ["CALLIND", null, ["register:0:8"]]
- 0087abe4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da91410b542d2428839692a0c4b8fc94"></a>

### [`0087b148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b148.md) → [`0087c0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c0f4.md) FUN_0087c0f4

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0087acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087acb0.md) · 呼出先 7件 [`0087b4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b4a0.md) [`0087c660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c660.md) [`0087c838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c838.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0087bc5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087b/0087bc5c.md) · 呼出先 7件 [`0087c44c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c44c.md) [`0087d60c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d60c.md) [`0087d7e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d7e4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 97.17% / 新版 97.17%

CFGの説明率　旧版 68.42% / 新版 76.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087b168"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087c1bc",
      "incomplete_value": false,
      "site": "0087c1bc",
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
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b210",
      "incomplete_value": false,
      "site": "0087b210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0087c114"
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
      "unmatched:0087b168",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0087c15c",
      "PARAM",
      [
        "storage",
        "0087c660",
        null,
        null
      ]
    ],
    [
      "0087c1bc",
      "DATA",
      [
        "storage",
        "00c80568",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c114",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0087c15c",
      "PARAM",
      [
        "storage",
        "0087d60c",
        null,
        null
      ]
    ],
    [
      "0087c1bc",
      "DATA",
      [
        "storage",
        "00c81538",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b148.md#insn-0087b168) · [`0087b1c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b148.md#insn-0087b1c8) · [`0087b268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b148.md#insn-0087b268)
- 新版 [`0087c174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c0f4.md#insn-0087c174) · [`0087c214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c0f4.md#insn-0087c214)

~~~diff
- 0087b168 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0087b168 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0087b168 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0087b168 bytes a8831ff8
- 0087b1c8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087b1c8 ["INT_ADD", "register:40f0:8", ["const:87b1c8:8", "const:4:8"]]
- 0087b1c8 ["CALLIND", null, ["register:0:8"]]
+ 0087c174 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087c174 ["INT_ADD", "register:40f0:8", ["const:87c174:8", "const:4:8"]]
+ 0087c174 ["CALLIND", null, ["register:0:8"]]
- 0087b1c8 bytes 20013fd6
+ 0087c174 bytes 20013fd6
- 0087b268 ["INT_ADD", "register:40f0:8", ["const:87b268:8", "const:4:8"]]
- 0087b268 ["CALL", null, ["callee:0087c44c:8"]]
+ 0087c214 ["INT_ADD", "register:40f0:8", ["const:87c214:8", "const:4:8"]]
+ 0087c214 ["CALL", null, ["callee:0087c44c:8"]]
- 0087b268 bytes 8e000094
+ 0087c214 bytes 8e000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecb925fb87820419cb4a402e27461b99"></a>

### [`0087b640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b640.md) → [`0087c5ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c5ec.md) FUN_0087c5ec

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c604",
      "incomplete_value": false,
      "site": "0087c610",
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
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b658",
      "incomplete_value": false,
      "site": "0087b664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:338:8"
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
      "0087c610",
      "DATA",
      [
        "storage",
        "00c80338",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c610",
      "DATA",
      [
        "storage",
        "00c81308",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b640.md#insn-0087b654) · [`0087b658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b640.md#insn-0087b658) · [`0087b688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b640.md#insn-0087b688)
- 新版 [`0087c600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c5ec.md#insn-0087c600) · [`0087c604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c5ec.md#insn-0087c604) · [`0087c634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c5ec.md#insn-0087c634)

~~~diff
- 0087b654 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 0087c600 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 0087b654 bytes 282000b0
+ 0087c600 bytes 282000b0
- 0087b658 ["COPY", "tmp:0:8", ["const:338:8"]]
- 0087b658 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087b658 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087b658 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c604 ["COPY", "tmp:0:8", ["const:308:8"]]
+ 0087c604 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c604 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c604 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087b658 bytes 08e10c91
+ 0087c604 bytes 08210c91
- 0087b688 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b688 ["INT_ADD", "register:40f0:8", ["const:87b688:8", "const:4:8"]]
- 0087b688 ["CALLIND", null, ["register:0:8"]]
+ 0087c634 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c634 ["INT_ADD", "register:40f0:8", ["const:87c634:8", "const:4:8"]]
+ 0087c634 ["CALLIND", null, ["register:0:8"]]
- 0087b688 bytes 00013fd6
+ 0087c634 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f38be8df7b4bb6735ebc1b46d304e70f"></a>

### [`0087b69c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b69c.md) → [`0087c648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c648.md) FUN_0087c648

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c674",
      "incomplete_value": false,
      "site": "0087c674",
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
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b6c8",
      "incomplete_value": false,
      "site": "0087b6c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:338:8"
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
      "0087c674",
      "DATA",
      [
        "storage",
        "00c80338",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c674",
      "DATA",
      [
        "storage",
        "00c81308",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b69c.md#insn-0087b6b0) · [`0087b6bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b69c.md#insn-0087b6bc) · [`0087b6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b69c.md#insn-0087b6c0)
- 新版 [`0087c65c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c648.md#insn-0087c65c) · [`0087c668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c648.md#insn-0087c668) · [`0087c66c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c648.md#insn-0087c66c)

~~~diff
- 0087b6b0 ["INT_ADD", "register:40f0:8", ["const:87b6b0:8", "const:4:8"]]
- 0087b6b0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0087c65c ["INT_ADD", "register:40f0:8", ["const:87c65c:8", "const:4:8"]]
+ 0087c65c ["CALL", null, ["callee:00c58f30:8"]]
- 0087b6b0 bytes 2c720f94
+ 0087c65c bytes 35720f94
- 0087b6bc ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 0087c668 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 0087b6bc bytes 282000b0
+ 0087c668 bytes 282000b0
- 0087b6c0 ["COPY", "tmp:0:8", ["const:338:8"]]
- 0087b6c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087b6c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087b6c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087c66c ["COPY", "tmp:0:8", ["const:308:8"]]
+ 0087c66c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c66c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087c66c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087b6c0 bytes 08e10c91
+ 0087c66c bytes 08210c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75358bffe2419742acebed9d4857b673"></a>

### [`0087b724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b724.md) → [`0087c6d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c6d0.md) FUN_0087c6d0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087c6ec",
      "incomplete_value": false,
      "site": "0087c6ec",
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
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b740",
      "incomplete_value": false,
      "site": "0087b740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:338:8"
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
      "0087c6ec",
      "DATA",
      [
        "storage",
        "00c80338",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087c6ec",
      "DATA",
      [
        "storage",
        "00c81308",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b724.md#insn-0087b738) · [`0087b73c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b724.md#insn-0087b73c) · [`0087b760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b724.md#insn-0087b760)
- 新版 [`0087c6e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c6d0.md#insn-0087c6e4) · [`0087c6e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c6d0.md#insn-0087c6e8) · [`0087c70c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c6d0.md#insn-0087c70c)

~~~diff
- 0087b738 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 0087c6e4 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 0087b738 bytes 292000b0
+ 0087c6e4 bytes 292000b0
- 0087b73c ["COPY", "tmp:0:8", ["const:338:8"]]
- 0087b73c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087b73c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087b73c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087c6e8 ["COPY", "tmp:0:8", ["const:308:8"]]
+ 0087c6e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087c6e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087c6e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087b73c bytes 29e10c91
+ 0087c6e8 bytes 29210c91
- 0087b760 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087b760 ["INT_ADD", "register:40f0:8", ["const:87b760:8", "const:4:8"]]
- 0087b760 ["CALLIND", null, ["register:0:8"]]
+ 0087c70c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087c70c ["INT_ADD", "register:40f0:8", ["const:87c70c:8", "const:4:8"]]
+ 0087c70c ["CALLIND", null, ["register:0:8"]]
- 0087b760 bytes 20013fd6
+ 0087c70c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dfc003a60c0d4905172d4f5da3c4cbd"></a>

### [`0087b8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b8f8.md) → [`0087c8a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c8a4.md) FUN_0087c8a4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 56.25% / 新版 64.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087c8bc",
      "incomplete_value": false,
      "site": "0087c8cc",
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
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087b910",
      "incomplete_value": false,
      "site": "0087b920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0087b970"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "0087c91c"
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
      "0087c8cc",
      "DATA",
      [
        "storage",
        "00c803c8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0087b970",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0087c8cc",
      "DATA",
      [
        "storage",
        "00c81398",
        null,
        "undefined *"
      ]
    ],
    [
      "0087c91c",
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

- 旧版 [`0087b970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b8f8.md#insn-0087b970) · [`0087b90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b8f8.md#insn-0087b90c)
- 新版 [`0087c91c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c8a4.md#insn-0087c91c) · [`0087c8b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c8a4.md#insn-0087c8b8)

~~~diff
- 0087b970 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087b970 ["INT_ADD", "register:40f0:8", ["const:87b970:8", "const:4:8"]]
- 0087b970 ["CALLIND", null, ["register:0:8"]]
- 0087b970 bytes 00013fd6
+ 0087c91c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087c91c ["INT_ADD", "register:40f0:8", ["const:87c91c:8", "const:4:8"]]
+ 0087c91c ["CALLIND", null, ["register:0:8"]]
+ 0087c91c bytes 00013fd6
- 0087b90c ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 0087c8b8 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 0087b90c bytes 282000b0
+ 0087c8b8 bytes 282000b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2c87a476a0bbf9be177677abd262f21"></a>

### [`0087b984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b984.md) → [`0087c930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c930.md) FUN_0087c930

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.84% / 新版 91.84%

CFGの説明率　旧版 58.82% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087b9b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0087c960"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0087b9b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087b9b4",
      "DATA",
      [
        "storage",
        "00c803c8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0087b9b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087c980"
      ]
    ]
  ],
  "added": [
    [
      "0087c960",
      "DATA",
      [
        "storage",
        "00c81398",
        null,
        "undefined *"
      ]
    ],
    [
      "0087c964",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087c980"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087b99c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b984.md#insn-0087b99c) · [`0087b9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b984.md#insn-0087b9b4) · [`0087b9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b984.md#insn-0087b9b8)
- 新版 [`0087c948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c930.md#insn-0087c948)

~~~diff
- 0087b99c ["INT_ADD", "register:40f0:8", ["const:87b99c:8", "const:4:8"]]
- 0087b99c ["CALL", null, ["callee:00c58f30:8"]]
+ 0087c948 ["INT_ADD", "register:40f0:8", ["const:87c948:8", "const:4:8"]]
+ 0087c948 ["CALL", null, ["callee:00c58f30:8"]]
- 0087b99c bytes 71710f94
+ 0087c948 bytes 7a710f94
- 0087b9b4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0087b9b4 ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 0087b9b4 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:10:8"]]
- 0087b9b4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0087b9b4 bytes 880601f8
- 0087b9b8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0087b9b8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 0087b9b8 bytes e00000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46c790d8d97859ac6c104070b526248c"></a>

### [`0087ba94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087ba94.md) → [`0087ca40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087ca40.md) FUN_0087ca40

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 54.55% / 新版 85.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087ba94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087ba94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087ba98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087ba94",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087ba98",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087ba9c",
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
      "0087ca40",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0087ca44",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0087ca48",
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

- 旧版 [`0087ba94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087ba94.md#insn-0087ba94) · [`0087ba98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087ba94.md#insn-0087ba98) · [`0087ba9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087ba94.md#insn-0087ba9c)

~~~diff
- 0087ba94 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087ba94 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087ba94 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 0087ba94 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0087ba94 bytes fd7bbda9
- 0087ba98 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0087ba98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0087ba98 bytes f50b00f9
- 0087ba9c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0087ba9c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0087ba9c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0087ba9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087ba9c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-940d68a19f5c095e895f8c5ae4f54bed"></a>

### [`0087bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087bc9c.md) → [`0087cc48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087cc48.md) FUN_0087cc48

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0087969c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/0087969c.md) [`0087a7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087a7a0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0087a648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087a/0087a648.md) [`0087b74c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087b/0087b74c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 75.00% / 新版 67.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087ccc0",
      "incomplete_value": true,
      "site": "0087ccd4",
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
      "definition_site": "0087bd14",
      "incomplete_value": true,
      "site": "0087bd28",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0087ccd8",
      "incomplete_value": true,
      "site": "0087cce8",
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
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:80b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087bd2c",
      "incomplete_value": true,
      "site": "0087bd3c",
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
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:7c1:8"
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
      "definition_site": "0087ccd8",
      "incomplete_value": true,
      "site": "0087cce8",
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
      "definition_site": "0087bd2c",
      "incomplete_value": true,
      "site": "0087bd3c",
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
      "0087ccc0",
      "READ",
      [
        "storage",
        "002c26a0",
        null,
        null
      ]
    ],
    [
      "0087ccd8",
      "READ",
      [
        "storage",
        "002c17c1",
        null,
        null
      ]
    ],
    [
      "0087ccd8",
      "READ",
      [
        "storage",
        "002c17d1",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0087ccc0",
      "READ",
      [
        "storage",
        "002c26f0",
        null,
        null
      ]
    ],
    [
      "0087ccd8",
      "READ",
      [
        "storage",
        "002c180b",
        null,
        null
      ]
    ],
    [
      "0087ccd8",
      "READ",
      [
        "storage",
        "002c181b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087be14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087bc9c.md#insn-0087be14) · [`0087bccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087bc9c.md#insn-0087bccc)
- 新版 [`0087cdc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087cc48.md#insn-0087cdc0) · [`0087cc78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087cc48.md#insn-0087cc78)

~~~diff
- 0087be14 ["INT_ADD", "register:40f0:8", ["const:87be14:8", "const:4:8"]]
- 0087be14 ["CALL", null, ["ram:87a7a0:8"]]
- 0087be14 bytes 63faff97
+ 0087cdc0 ["INT_ADD", "register:40f0:8", ["const:87cdc0:8", "const:4:8"]]
+ 0087cdc0 ["CALL", null, ["ram:87b74c:8"]]
+ 0087cdc0 bytes 63faff97
- 0087bccc ["INT_ADD", "register:40f0:8", ["const:87bccc:8", "const:4:8"]]
- 0087bccc ["CALL", null, ["callee:00c5baa0:8"]]
+ 0087cc78 ["INT_ADD", "register:40f0:8", ["const:87cc78:8", "const:4:8"]]
+ 0087cc78 ["CALL", null, ["callee:00c5baa0:8"]]
- 0087bccc bytes 817b0f94
+ 0087cc78 bytes 8a7b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdaf23b70800cbe1929731d519196cfe"></a>

### [`0087bffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087bffc.md) → [`0087cfa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087cfa8.md) FUN_0087cfa8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087cfb4",
      "incomplete_value": false,
      "site": "0087cfc0",
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
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c008",
      "incomplete_value": false,
      "site": "0087c014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:458:8"
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
      "0087cfc0",
      "DATA",
      [
        "storage",
        "00c80458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087cfc0",
      "DATA",
      [
        "storage",
        "00c81428",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087bffc.md#insn-0087c004) · [`0087c008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087bffc.md#insn-0087c008)
- 新版 [`0087cfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087cfa8.md#insn-0087cfb0) · [`0087cfb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087cfa8.md#insn-0087cfb4)

~~~diff
- 0087c004 ["COPY", "register:4050:8", ["const:c80000:8"]]
+ 0087cfb0 ["COPY", "register:4050:8", ["const:c81000:8"]]
- 0087c004 bytes 2a200090
+ 0087cfb0 bytes 2a2000b0
- 0087c008 ["COPY", "tmp:0:8", ["const:458:8"]]
- 0087c008 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0087c008 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0087c008 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087cfb4 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 0087cfb4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087cfb4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087cfb4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0087c008 bytes 4a611191
+ 0087cfb4 bytes 4aa11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a715203cd2fc77bc2e255065bdfac1b1"></a>

### [`0087c040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c040.md) → [`0087cfec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087cfec.md) FUN_0087cfec

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087d004",
      "incomplete_value": false,
      "site": "0087d010",
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
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c058",
      "incomplete_value": false,
      "site": "0087c064",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:458:8"
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
      "0087d010",
      "DATA",
      [
        "storage",
        "00c80458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087d010",
      "DATA",
      [
        "storage",
        "00c81428",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c040.md#insn-0087c054) · [`0087c058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c040.md#insn-0087c058) · [`0087c088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c040.md#insn-0087c088)
- 新版 [`0087d000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087cfec.md#insn-0087d000) · [`0087d004`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087cfec.md#insn-0087d004) · [`0087d034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087cfec.md#insn-0087d034)

~~~diff
- 0087c054 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 0087d000 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 0087c054 bytes 28200090
+ 0087d000 bytes 28200090
- 0087c058 ["COPY", "tmp:0:8", ["const:458:8"]]
- 0087c058 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c058 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c058 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087d004 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 0087d004 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087d004 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087d004 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c058 bytes 08611191
+ 0087d004 bytes 08a11091
- 0087c088 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c088 ["INT_ADD", "register:40f0:8", ["const:87c088:8", "const:4:8"]]
- 0087c088 ["CALLIND", null, ["register:0:8"]]
+ 0087d034 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087d034 ["INT_ADD", "register:40f0:8", ["const:87d034:8", "const:4:8"]]
+ 0087d034 ["CALLIND", null, ["register:0:8"]]
- 0087c088 bytes 00013fd6
+ 0087d034 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8581dd048b118dd4192c5709143edb54"></a>

### [`0087c09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c09c.md) → [`0087d048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d048.md) FUN_0087d048

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087d074",
      "incomplete_value": false,
      "site": "0087d074",
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
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c0c8",
      "incomplete_value": false,
      "site": "0087c0c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:458:8"
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
      "0087d074",
      "DATA",
      [
        "storage",
        "00c80458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087d074",
      "DATA",
      [
        "storage",
        "00c81428",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c09c.md#insn-0087c0b0) · [`0087c0bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c09c.md#insn-0087c0bc) · [`0087c0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c09c.md#insn-0087c0c0)
- 新版 [`0087d05c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d048.md#insn-0087d05c) · [`0087d068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d048.md#insn-0087d068) · [`0087d06c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d048.md#insn-0087d06c)

~~~diff
- 0087c0b0 ["INT_ADD", "register:40f0:8", ["const:87c0b0:8", "const:4:8"]]
- 0087c0b0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0087d05c ["INT_ADD", "register:40f0:8", ["const:87d05c:8", "const:4:8"]]
+ 0087d05c ["CALL", null, ["callee:00c58f30:8"]]
- 0087c0b0 bytes ac6f0f94
+ 0087d05c bytes b56f0f94
- 0087c0bc ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 0087d068 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 0087c0bc bytes 28200090
+ 0087d068 bytes 28200090
- 0087c0c0 ["COPY", "tmp:0:8", ["const:458:8"]]
- 0087c0c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c0c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c0c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087d06c ["COPY", "tmp:0:8", ["const:428:8"]]
+ 0087d06c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087d06c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087d06c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c0c0 bytes 08611191
+ 0087d06c bytes 08a11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23c0ee1f468878d2ec90b5bd05d5fc19"></a>

### [`0087c124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c124.md) → [`0087d0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d0d0.md) FUN_0087d0d0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087d0ec",
      "incomplete_value": false,
      "site": "0087d0ec",
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
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c140",
      "incomplete_value": false,
      "site": "0087c140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:458:8"
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
      "0087d0ec",
      "DATA",
      [
        "storage",
        "00c80458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087d0ec",
      "DATA",
      [
        "storage",
        "00c81428",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c124.md#insn-0087c138) · [`0087c13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c124.md#insn-0087c13c) · [`0087c160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c124.md#insn-0087c160)
- 新版 [`0087d0e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d0d0.md#insn-0087d0e4) · [`0087d0e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d0d0.md#insn-0087d0e8) · [`0087d10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d0d0.md#insn-0087d10c)

~~~diff
- 0087c138 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 0087d0e4 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 0087c138 bytes 29200090
+ 0087d0e4 bytes 29200090
- 0087c13c ["COPY", "tmp:0:8", ["const:458:8"]]
- 0087c13c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087c13c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087c13c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087d0e8 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 0087d0e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087d0e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087d0e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087c13c bytes 29611191
+ 0087d0e8 bytes 29a11091
- 0087c160 ["COPY", "register:0:8", ["register:4048:8"]]
- 0087c160 ["INT_ADD", "register:40f0:8", ["const:87c160:8", "const:4:8"]]
- 0087c160 ["CALLIND", null, ["register:0:8"]]
+ 0087d10c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087d10c ["INT_ADD", "register:40f0:8", ["const:87d10c:8", "const:4:8"]]
+ 0087d10c ["CALLIND", null, ["register:0:8"]]
- 0087c160 bytes 20013fd6
+ 0087d10c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73944f99d843ec0357bd76a1491432ce"></a>

### [`0087c268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c268.md) → [`0087d214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d214.md) FUN_0087d214

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087d220",
      "incomplete_value": false,
      "site": "0087d22c",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c274",
      "incomplete_value": false,
      "site": "0087c280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "0087d22c",
      "DATA",
      [
        "storage",
        "00c804d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087d22c",
      "DATA",
      [
        "storage",
        "00c814a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c268.md#insn-0087c270) · [`0087c274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c268.md#insn-0087c274)
- 新版 [`0087d21c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d214.md#insn-0087d21c) · [`0087d220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d214.md#insn-0087d220)

~~~diff
- 0087c270 ["COPY", "register:4050:8", ["const:c80000:8"]]
+ 0087d21c ["COPY", "register:4050:8", ["const:c81000:8"]]
- 0087c270 bytes 2a200090
+ 0087d21c bytes 2a200090
- 0087c274 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 0087c274 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0087c274 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0087c274 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087d220 ["COPY", "tmp:0:8", ["const:4a8:8"]]
+ 0087d220 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087d220 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087d220 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0087c274 bytes 4a611391
+ 0087d220 bytes 4aa11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5972c2929331319feb35466e0a1c7fec"></a>

### [`0087c2ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c2ac.md) → [`0087d258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d258.md) FUN_0087d258

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 42.86% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087d270",
      "incomplete_value": false,
      "site": "0087d27c",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c2c4",
      "incomplete_value": false,
      "site": "0087c2d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "0087d27c",
      "DATA",
      [
        "storage",
        "00c804d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087d27c",
      "DATA",
      [
        "storage",
        "00c814a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c2ac.md#insn-0087c2c0) · [`0087c2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c2ac.md#insn-0087c2c4) · [`0087c2d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c2ac.md#insn-0087c2d4)
- 新版 [`0087d26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d258.md#insn-0087d26c) · [`0087d270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d258.md#insn-0087d270) · [`0087d280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d258.md#insn-0087d280)

~~~diff
- 0087c2c0 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 0087d26c ["COPY", "register:4040:8", ["const:c81000:8"]]
- 0087c2c0 bytes 28200090
+ 0087d26c bytes 28200090
- 0087c2c4 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 0087c2c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0087c2c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0087c2c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0087d270 ["COPY", "tmp:0:8", ["const:4a8:8"]]
+ 0087d270 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0087d270 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0087d270 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0087c2c4 bytes 08611391
+ 0087d270 bytes 08a11291
- 0087c2d4 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 0087d280 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 0087c2d4 bytes 80000054
+ 0087d280 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5834aa490c3bbeb48ea229f852a70716"></a>

### [`0087c308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c308.md) → [`0087d2b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d2b4.md) FUN_0087d2b4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 79.31% / 新版 79.31%

CFGの説明率　旧版 42.86% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087c308"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087c308"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087c30c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087c308",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087c30c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087c334",
      "DATA",
      [
        "storage",
        "00c804d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087d2b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0087d2b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0087d2e0",
      "DATA",
      [
        "storage",
        "00c814a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c308.md#insn-0087c308) · [`0087c30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c308.md#insn-0087c30c) · [`0087c334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c308.md#insn-0087c334)

~~~diff
- 0087c308 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087c308 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087c308 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0087c308 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0087c308 bytes fd7bbea9
- 0087c30c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0087c30c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0087c30c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0087c30c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087c30c bytes f44f01a9
- 0087c334 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0087c334 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 0087c334 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 0087c334 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0087c334 bytes 280401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4108d96a76bb830f8eca29131714e09"></a>

### [`0087c390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c390.md) → [`0087d33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d33c.md) FUN_0087d33c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087d358",
      "incomplete_value": false,
      "site": "0087d358",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c3ac",
      "incomplete_value": false,
      "site": "0087c3ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "0087d358",
      "DATA",
      [
        "storage",
        "00c804d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087d358",
      "DATA",
      [
        "storage",
        "00c814a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c390.md#insn-0087c3a4) · [`0087c3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c390.md#insn-0087c3a8) · [`0087c3cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c390.md#insn-0087c3cc)
- 新版 [`0087d350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d33c.md#insn-0087d350) · [`0087d354`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d33c.md#insn-0087d354) · [`0087d378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d33c.md#insn-0087d378)

~~~diff
- 0087c3a4 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 0087d350 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 0087c3a4 bytes 29200090
+ 0087d350 bytes 29200090
- 0087c3a8 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 0087c3a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0087c3a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0087c3a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0087d354 ["COPY", "tmp:0:8", ["const:4a8:8"]]
+ 0087d354 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0087d354 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0087d354 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0087c3a8 bytes 29611391
+ 0087d354 bytes 29a11291
- 0087c3cc ["COPY", "register:0:8", ["register:4048:8"]]
- 0087c3cc ["INT_ADD", "register:40f0:8", ["const:87c3cc:8", "const:4:8"]]
- 0087c3cc ["CALLIND", null, ["register:0:8"]]
+ 0087d378 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0087d378 ["INT_ADD", "register:40f0:8", ["const:87d378:8", "const:4:8"]]
+ 0087d378 ["CALLIND", null, ["register:0:8"]]
- 0087c3cc bytes 20013fd6
+ 0087d378 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6da8f348744deee3e4bc79263de3246"></a>

### [`0087c43c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c43c.md) → [`0087d3e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d3e8.md) FUN_0087d3e8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0087a7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087a7a0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0087b74c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087b/0087b74c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0087c478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c43c.md#insn-0087c478)
- 新版 [`0087d424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d3e8.md#insn-0087d424)

~~~diff
- 0087c478 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c478 ["INT_ADD", "register:40f0:8", ["const:87c478:8", "const:4:8"]]
- 0087c478 ["CALLIND", null, ["register:0:8"]]
+ 0087d424 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087d424 ["INT_ADD", "register:40f0:8", ["const:87d424:8", "const:4:8"]]
+ 0087d424 ["CALLIND", null, ["register:0:8"]]
- 0087c478 bytes 00013fd6
+ 0087d424 bytes 00013fd6
~~~


<a id="compare-f519658b2735d3a9cca5ab82bb2533e9"></a>

### [`0087c48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c48c.md) → [`0087d438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d438.md) FUN_0087d438

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 29.63% / 新版 27.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087c4b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0087d464"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0087c5a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087c4b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087c5a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087d5e0"
      ]
    ],
    [
      "unmatched:0087c5e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087d5e0"
      ]
    ]
  ],
  "added": [
    [
      "0087d464",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "0087d554",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087d5e0"
      ]
    ],
    [
      "0087d594",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087d5e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c48c.md#insn-0087c4b8) · [`0087c4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c48c.md#insn-0087c4bc) · [`0087c588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c48c.md#insn-0087c588)
- 新版 [`0087d468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d438.md#insn-0087d468)

~~~diff
- 0087c4b8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0087c4b8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0087c4b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0087c4b8 bytes a8831ff8
- 0087c4bc ["INT_ADD", "register:40f0:8", ["const:87c4bc:8", "const:4:8"]]
- 0087c4bc ["CALL", null, ["callee:00c5baa0:8"]]
+ 0087d468 ["INT_ADD", "register:40f0:8", ["const:87d468:8", "const:4:8"]]
+ 0087d468 ["CALL", null, ["callee:00c5baa0:8"]]
- 0087c4bc bytes 85790f94
+ 0087d468 bytes 8e790f94
- 0087c588 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c588 ["INT_ADD", "register:40f0:8", ["const:87c588:8", "const:4:8"]]
- 0087c588 ["CALLIND", null, ["register:0:8"]]
- 0087c588 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad7f0cec72195bf887bc03daed5bf820"></a>

### [`0087c664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c664.md) → [`0087d610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d610.md) FUN_0087d610

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0087d61c",
      "incomplete_value": false,
      "site": "0087d628",
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
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c670",
      "incomplete_value": false,
      "site": "0087c67c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
      "0087d628",
      "DATA",
      [
        "storage",
        "00c80568",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0087d628",
      "DATA",
      [
        "storage",
        "00c81538",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c664.md#insn-0087c66c) · [`0087c670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c664.md#insn-0087c670)
- 新版 [`0087d618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d610.md#insn-0087d618) · [`0087d61c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d610.md#insn-0087d61c)

~~~diff
- 0087c66c ["COPY", "register:4050:8", ["const:c80000:8"]]
+ 0087d618 ["COPY", "register:4050:8", ["const:c81000:8"]]
- 0087c66c bytes 2a200090
+ 0087d618 bytes 2a200090
- 0087c670 ["COPY", "tmp:0:8", ["const:568:8"]]
- 0087c670 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0087c670 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0087c670 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0087d61c ["COPY", "tmp:0:8", ["const:538:8"]]
+ 0087d61c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0087d61c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0087d61c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0087c670 bytes 4aa11591
+ 0087d61c bytes 4ae11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-445276816af08e2c4ed43aa357fb414d"></a>

### [`0087c6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c6a8.md) → [`0087d654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d654.md) FUN_0087d654

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 42.86% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087d66c",
      "incomplete_value": false,
      "site": "0087d678",
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
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c6c0",
      "incomplete_value": false,
      "site": "0087c6cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0087c6f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "0087d69c"
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
      "0087d678",
      "DATA",
      [
        "storage",
        "00c80568",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0087c6f0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0087d678",
      "DATA",
      [
        "storage",
        "00c81538",
        null,
        "undefined *"
      ]
    ],
    [
      "0087d69c",
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

- 旧版 [`0087c6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c6a8.md#insn-0087c6f0) · [`0087c6bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c6a8.md#insn-0087c6bc)
- 新版 [`0087d69c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d654.md#insn-0087d69c) · [`0087d668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d654.md#insn-0087d668)

~~~diff
- 0087c6f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087c6f0 ["INT_ADD", "register:40f0:8", ["const:87c6f0:8", "const:4:8"]]
- 0087c6f0 ["CALLIND", null, ["register:0:8"]]
- 0087c6f0 bytes 00013fd6
+ 0087d69c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087d69c ["INT_ADD", "register:40f0:8", ["const:87d69c:8", "const:4:8"]]
+ 0087d69c ["CALLIND", null, ["register:0:8"]]
+ 0087d69c bytes 00013fd6
- 0087c6bc ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 0087d668 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 0087c6bc bytes 28200090
+ 0087d668 bytes 28200090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8749154999bf21da6900502cf89c470"></a>

### [`0087c704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c704.md) → [`0087d6b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d6b0.md) FUN_0087d6b0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 57.14% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `store_value` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087d6dc",
      "incomplete_value": false,
      "site": "0087d6dc",
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
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c730",
      "incomplete_value": false,
      "site": "0087c730",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0087c740"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0087d6ec"
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
      "0087d6dc",
      "DATA",
      [
        "storage",
        "00c80568",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0087c740",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087d704"
      ]
    ]
  ],
  "added": [
    [
      "0087d6dc",
      "DATA",
      [
        "storage",
        "00c81538",
        null,
        "undefined *"
      ]
    ],
    [
      "0087d6ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087d704"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c704.md#insn-0087c740) · [`0087c718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c704.md#insn-0087c718)
- 新版 [`0087d6ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d6b0.md#insn-0087d6ec) · [`0087d6c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d6b0.md#insn-0087d6c4)

~~~diff
- 0087c740 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 0087c740 bytes c0000054
+ 0087d6ec ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 0087d6ec bytes c0000054
- 0087c718 ["INT_ADD", "register:40f0:8", ["const:87c718:8", "const:4:8"]]
- 0087c718 ["CALL", null, ["callee:00c58f30:8"]]
+ 0087d6c4 ["INT_ADD", "register:40f0:8", ["const:87d6c4:8", "const:4:8"]]
+ 0087d6c4 ["CALL", null, ["callee:00c58f30:8"]]
- 0087c718 bytes 126e0f94
+ 0087d6c4 bytes 1b6e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4eaef704b0bc5e90e916a0ddc9bc254"></a>

### [`0087c78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c78c.md) → [`0087d738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d738.md) FUN_0087d738

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment

命令の説明率　旧版 79.31% / 新版 79.31%

CFGの説明率　旧版 50.00% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `store_value` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087d754",
      "incomplete_value": false,
      "site": "0087d754",
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
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087c7a8",
      "incomplete_value": false,
      "site": "0087c7a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0087c7b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0087d764"
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
      "0087d754",
      "DATA",
      [
        "storage",
        "00c80568",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0087c7b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087d790"
      ]
    ]
  ],
  "added": [
    [
      "0087d754",
      "DATA",
      [
        "storage",
        "00c81538",
        null,
        "undefined *"
      ]
    ],
    [
      "0087d764",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087d790"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087c7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c78c.md#insn-0087c7b8) · [`0087c7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c78c.md#insn-0087c7a0)
- 新版 [`0087d764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d738.md#insn-0087d764) · [`0087d74c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d738.md#insn-0087d74c)

~~~diff
- 0087c7b8 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 0087c7b8 bytes 60010054
+ 0087d764 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 0087d764 bytes 60010054
- 0087c7a0 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 0087d74c ["COPY", "register:4048:8", ["const:c81000:8"]]
- 0087c7a0 bytes 29200090
+ 0087d74c bytes 29200090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00474d74e73fde182fc0cc731153470a"></a>

### [`0087c9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c9ec.md) → [`0087d998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d998.md) FUN_0087d998

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.23% / 新版 87.23%

CFGの説明率　旧版 35.29% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087ca1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0087d9c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0087ca20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087ca1c",
      "DATA",
      [
        "storage",
        "00c805e8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0087ca20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087d9e8"
      ]
    ],
    [
      "unmatched:0087ca54",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0087d9c8",
      "DATA",
      [
        "storage",
        "00c815b8",
        null,
        "undefined *"
      ]
    ],
    [
      "0087d9cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087d9e8"
      ]
    ],
    [
      "0087da00",
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

- 旧版 [`0087ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c9ec.md#insn-0087ca04) · [`0087ca1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c9ec.md#insn-0087ca1c) · [`0087ca20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087c9ec.md#insn-0087ca20)
- 新版 [`0087d9b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087d998.md#insn-0087d9b0)

~~~diff
- 0087ca04 ["INT_ADD", "register:40f0:8", ["const:87ca04:8", "const:4:8"]]
- 0087ca04 ["CALL", null, ["callee:00c58f30:8"]]
+ 0087d9b0 ["INT_ADD", "register:40f0:8", ["const:87d9b0:8", "const:4:8"]]
+ 0087d9b0 ["CALL", null, ["callee:00c58f30:8"]]
- 0087ca04 bytes 576d0f94
+ 0087d9b0 bytes 606d0f94
- 0087ca1c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0087ca1c ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 0087ca1c ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:10:8"]]
- 0087ca1c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0087ca1c bytes 880601f8
- 0087ca20 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0087ca20 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0087ca20 bytes e00000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-334549039f2140b8f76338f2e6c73e17"></a>

### [`0087caf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087caf4.md) → [`0087daa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087daa0.md) FUN_0087daa0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 90.38% / 新版 90.38%

CFGの説明率　旧版 64.71% / 新版 57.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0087dac8",
      "incomplete_value": false,
      "site": "0087dac8",
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
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0087cb1c",
      "incomplete_value": false,
      "site": "0087cb1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0087cb90"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "0087db3c"
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
      "0087dac8",
      "DATA",
      [
        "storage",
        "00c805e8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0087cb90",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0087dac8",
      "DATA",
      [
        "storage",
        "00c815b8",
        null,
        "undefined *"
      ]
    ],
    [
      "0087db3c",
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

- 旧版 [`0087cb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087caf4.md#insn-0087cb90) · [`0087cb10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087caf4.md#insn-0087cb10)
- 新版 [`0087db3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087daa0.md#insn-0087db3c) · [`0087dabc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087daa0.md#insn-0087dabc)

~~~diff
- 0087cb90 ["COPY", "register:0:8", ["register:4040:8"]]
- 0087cb90 ["INT_ADD", "register:40f0:8", ["const:87cb90:8", "const:4:8"]]
- 0087cb90 ["CALLIND", null, ["register:0:8"]]
- 0087cb90 bytes 00013fd6
+ 0087db3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0087db3c ["INT_ADD", "register:40f0:8", ["const:87db3c:8", "const:4:8"]]
+ 0087db3c ["CALLIND", null, ["register:0:8"]]
+ 0087db3c bytes 00013fd6
- 0087cb10 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 0087dabc ["COPY", "register:4040:8", ["const:c81000:8"]]
- 0087cb10 bytes 28200090
+ 0087dabc bytes 28200090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56ecb3e65fda1e188347494e5e03abf6"></a>

### [`0087cec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087cec8.md) → [`0087de74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087d/0087de74.md) _INIT_161

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00bc5880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5880.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.53% / 新版 70.53%

CFGの説明率　旧版 23.91% / 新版 24.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087cecc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087cecc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0087cef8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0087cecc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087cef8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0087cf04",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0087de78",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0087dea4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0087deb0",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0087cecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087cec8.md#insn-0087cecc) · [`0087cef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087cec8.md#insn-0087cef8) · [`0087cf20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087c/0087cec8.md#insn-0087cf20)

~~~diff
- 0087cecc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0087cecc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0087cecc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 0087cecc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0087cecc bytes fd7b0fa9
- 0087cef8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0087cef8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0087cef8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0087cef8 bytes a9831ff8
- 0087cf20 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 0087cf20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0087cf20 bytes e013813c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

