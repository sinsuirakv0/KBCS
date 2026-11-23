# v16.0.0 → v16.0.1 · 命令位置の検査未完了 (4)

[一覧の目次](README.md)

<a id="compare-c278c65dba6566d971d112da7597be6b"></a>

### [`00a39024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39024.md) → [`00a3921c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a3921c.md) FUN_00a3921c

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a35f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a35/00a35f24.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00a39208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39208.md) [`00a39330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39330.md) [`00a394d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a394d8.md) [`00a394ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a394ec.md)
- 新版 呼出元 1件 [`00a3611c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a36/00a3611c.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00a39400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39400.md) [`00a39528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39528.md) [`00a396d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a396d0.md) [`00a396e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a396e4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 88.39% / 新版 88.39%

CFGの説明率　旧版 64.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39078"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a390d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a390d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a39078",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a392f8"
      ]
    ]
  ],
  "added": [
    [
      "00a39270",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a392f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a39078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39024.md#insn-00a39078) · [`00a390d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39024.md#insn-00a390d0) · [`00a390d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39024.md#insn-00a390d8)

~~~diff
- 00a39078 ["CBRANCH", null, ["local:b7:8", "register:102:1"]]
- 00a39078 bytes 42040054
- 00a390d0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a390d0 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00a390d0 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00a390d0 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00a390d0 bytes 29818b9a
- 00a390d8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00a390d8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a390d8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00a390d8 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00a390d8 bytes 37318a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b54f2a692a705567f900ce308a2bebd5"></a>

### [`00a397d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a397d8.md) → [`00a399d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a399d0.md) FUN_00a399d0

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a39648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39648.md) · 呼出先 2件 [`00a3999c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a3999c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00a39840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39840.md) · 呼出先 2件 [`00a39b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39b94.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.76% / 新版 91.76%

CFGの説明率　旧版 33.33% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39820"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39820"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39824"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a39820",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a39824",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a39828",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a39ab0"
      ]
    ]
  ],
  "added": [
    [
      "00a39a18",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00a39a1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00a39a20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a39ab0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a39820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a397d8.md#insn-00a39820) · [`00a39824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a397d8.md#insn-00a39824) · [`00a39828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a397d8.md#insn-00a39828)

~~~diff
- 00a39820 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a39820 ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 00a39820 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:8:8"]]
- 00a39820 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a39820 bytes f6db00a9
- 00a39824 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00a39824 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a39824 bytes e81700f9
- 00a39828 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00a39828 bytes 80040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f97c85175b86a71df5fbfe9240ad06b"></a>

### [`00a39988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39988.md) → [`00a39b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39b80.md) FUN_00a39b80

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a39648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39648.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00a39840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39840.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39988"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39988"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a39b80"
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
      "unmatched:00a39988",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a39994",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a39998",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043b778"
      ]
    ]
  ],
  "added": [
    [
      "00a39b80",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a39b8c",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ],
    [
      "00a39b90",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043b778"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a39988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39988.md#insn-00a39988) · [`00a39998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39988.md#insn-00a39998)
- 新版 `00a39b80`（命令位置の公開資料なし）

~~~diff
- 00a39988 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a39988 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a39988 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00a39988 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a39988 bytes fd7bbfa9
- 00a39998 ["INT_ADD", "register:40f0:8", ["const:a39998:8", "const:4:8"]]
- 00a39998 ["CALL", null, ["callee:0043b778:8"]]
- 00a39998 bytes 6807e897
+ 00a39b80 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00a39b80 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00a39b80 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00a39b80 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00a39b80 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-548ae7984001fb3994a65723712b3b84"></a>

### [`00a39a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39a7c.md) → [`00a39c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39c74.md) FUN_00a39c74

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a39a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39a44.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00a39c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39c3c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 64.00% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39a8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39a8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a39c84"
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
      "unmatched:00a39a8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a39aec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a39c98"
      ]
    ]
  ],
  "added": [
    [
      "00a39c84",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a39ce4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a39c98"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a39a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39a7c.md#insn-00a39a8c) · [`00a39aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39a7c.md#insn-00a39aec)
- 新版 `00a39c84`（命令位置の公開資料なし）

~~~diff
- 00a39a8c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a39a8c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a39a8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a39a8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a39a8c bytes f44f02a9
- 00a39aec ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00a39aec bytes a0fdff54
+ 00a39c84 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00a39c84 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00a39c84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
+ 00a39c84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a39c84 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01ea86ec0478d841f0de7bea48c2018b"></a>

### [`00a39be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39be0.md) → [`00a39dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a39/00a39dd8.md) FUN_00a39dd8

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a37f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a37/00a37f10.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`008691e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008691e8.md) [`00a39e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39e0c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00a38108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38108.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00869228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869228.md) [`00a3a004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3a/00a3a004.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.65% / 新版 90.65%

CFGの説明率　旧版 57.14% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39d84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a39f7c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a39c18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a39c18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a39e8c"
      ]
    ]
  ],
  "added": [
    [
      "00a39e10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a39e8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a39c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39be0.md#insn-00a39c18) · [`00a39c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39be0.md#insn-00a39c64) · [`00a39c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a39/00a39be0.md#insn-00a39c6c)

~~~diff
- 00a39c18 ["CBRANCH", null, ["local:b6:8", "register:102:1"]]
- 00a39c18 bytes e2030054
- 00a39c64 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a39c64 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00a39c64 ["COPY", "tmp:2:8", ["register:4058:8"]]
- 00a39c64 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00a39c64 bytes 6a818a9a
- 00a39c6c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00a39c6c ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00a39c6c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00a39c6c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a39c6c bytes 5731899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7ed9212596ac90d4d2fcb53a765a13b"></a>

### [`00a3e59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e59c.md) → [`00a3e794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e794.md) FUN_00a3e794

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00a3e5a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3e5a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a3e7a0"
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
      "unmatched:00a3e5a8",
      "DATA",
      [
        "storage",
        "00c8afb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3e7a0",
      "DATA",
      [
        "storage",
        "00c8b3b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3e5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e59c.md#insn-00a3e5a8) · [`00a3e5ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e59c.md#insn-00a3e5ac)
- 新版 `00a3e7a0`（命令位置の公開資料なし）

~~~diff
- 00a3e5a8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a3e5a8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a3e5a8 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00a3e5a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a3e5a8 bytes 292000a9
- 00a3e5ac ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a3e5ac ["RETURN", null, ["register:0:8"]]
- 00a3e5ac bytes c0035fd6
+ 00a3e7a0 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a3e7a0 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00a3e7a0 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00a3e7a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a3e7a0 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f65cf9607862de05fb6c3296bb9d5c9"></a>

### [`00a3e630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e630.md) → [`00a3e828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e828.md) FUN_00a3e828

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3e670"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00a3e868"
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
      "00a3e844",
      "DATA",
      [
        "storage",
        "00c8b038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3e844",
      "DATA",
      [
        "storage",
        "00c8b438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3e670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e630.md#insn-00a3e670) · [`00a3e644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e630.md#insn-00a3e644)
- 新版 `00a3e868`（命令位置の公開資料なし）

~~~diff
- 00a3e670 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a3e670 ["RETURN", null, ["register:0:8"]]
- 00a3e670 bytes c0035fd6
+ 00a3e868 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00a3e868 ["RETURN", null, ["register:0:8"]]
+ 00a3e868 bytes c0035fd6
- 00a3e644 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00a3e644 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a3e644 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a3e644 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a3e644 bytes 08e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90905cf9f8c0199fafd6396a029b30da"></a>

### [`00a3e728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e728.md) → [`00a3e920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e920.md) FUN_00a3e920

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00a3ea6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3ea6c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00a3ec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3ec64.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00a3e734"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a3e92c"
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
      "unmatched:00a3e734",
      "DATA",
      [
        "storage",
        "00c8b038",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a3e740",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00a3ec64"
      ]
    ]
  ],
  "added": [
    [
      "00a3e92c",
      "DATA",
      [
        "storage",
        "00c8b438",
        null,
        "undefined *"
      ]
    ],
    [
      "00a3e938",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00a3ec64"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3e734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e728.md#insn-00a3e734) · [`00a3e728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e728.md#insn-00a3e728)
- 新版 `00a3e92c`（命令位置の公開資料なし）

~~~diff
- 00a3e734 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a3e734 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a3e734 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:8:8"]]
- 00a3e734 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a3e734 bytes 098500f8
+ 00a3e92c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a3e92c ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00a3e92c ["INT_ADD", "register:4040:8", ["register:4040:8", "const:8:8"]]
+ 00a3e92c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00a3e92c bytes 098500f8
- 00a3e728 ["COPY", "register:4040:8", ["register:4008:8"]]
- 00a3e728 bytes e80301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eac188500329a6c077bd0aa387e6009"></a>

### [`00a3e790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e790.md) → [`00a3e988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e988.md) FUN_00a3e988

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a3cc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3c/00a3cc20.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00a3ce18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3c/00a3ce18.md) · 呼出先 2件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3e794"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a3e98c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a3e79c",
      "incomplete_value": true,
      "site": "00a3e7a8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
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
      "unmatched:00a3e794",
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
      "00a3e98c",
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

- 旧版 [`00a3e794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e790.md#insn-00a3e794) · [`00a3e7a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e790.md#insn-00a3e7a8)
- 新版 `00a3e9a0`（命令位置の公開資料なし） · `00a3e98c`（命令位置の公開資料なし）

~~~diff
- 00a3e794 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a3e794 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00a3e794 bytes f30b00f9
- 00a3e7a8 ["INT_ADD", "register:40f0:8", ["const:a3e7a8:8", "const:4:8"]]
- 00a3e7a8 ["CALL", null, ["callee:005c179c:8"]]
+ 00a3e9a0 ["INT_ADD", "register:40f0:8", ["const:a3e9a0:8", "const:4:8"]]
+ 00a3e9a0 ["CALL", null, ["callee:005c179c:8"]]
- 00a3e7a8 bytes ed0bee97
+ 00a3e9a0 bytes 7f0bee97
+ 00a3e98c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 00a3e98c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00a3e98c bytes f30b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0af16eb6451e62aa2ded16b2e938bf19"></a>

### [`00a3eb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3eb90.md) → [`00a3ed88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3ed88.md) FUN_00a3ed88

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 42.86% / 新版 42.86%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3eb90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3eb90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a3eb94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a3eb90",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a3eb94",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a3ebac",
      "DATA",
      [
        "storage",
        "00c8b0a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3ed88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a3ed8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a3eda4",
      "DATA",
      [
        "storage",
        "00c8b4a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a3eb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3eb90.md#insn-00a3eb90) · [`00a3eb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3eb90.md#insn-00a3eb94) · [`00a3ebac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3eb90.md#insn-00a3ebac)

~~~diff
- 00a3eb90 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a3eb90 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a3eb90 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a3eb90 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a3eb90 bytes fd7bbea9
- 00a3eb94 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a3eb94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00a3eb94 bytes f30b00f9
- 00a3ebac ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a3ebac ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00a3ebac ["INT_ADD", "register:4000:8", ["register:4000:8", "const:28:8"]]
- 00a3ebac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a3ebac bytes 088402f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-604de44d2c1dedc58293abb5d8eac814"></a>

### [`00a4099c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a4099c.md) → [`00a40b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a40/00a40b94.md) FUN_00a40b94

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a40a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40a94.md) · 呼出先 6件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00a40c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a40/00a40c8c.md) · 呼出先 6件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.42% / 新版 77.42%

CFGの説明率　旧版 22.73% / 新版 23.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a409bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a40a50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a40bb4"
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
      "unmatched:00a409bc",
      "DATA",
      [
        "storage",
        "00c8b1b8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00a409c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a40be4"
      ]
    ],
    [
      "00a40c5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a40be4"
      ]
    ]
  ],
  "added": [
    [
      "00a40bb4",
      "DATA",
      [
        "storage",
        "00c8b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "00a40bb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a40be4"
      ]
    ],
    [
      "00a40bc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a40be4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a409bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a4099c.md#insn-00a409bc) · [`00a409c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a4099c.md#insn-00a409c0) · [`00a409e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a4099c.md#insn-00a409e0)

~~~diff
- 00a409bc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a409bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a409bc bytes 080000f9
- 00a409c0 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00a409c0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00a409c0 bytes 740100b4
- 00a409e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a409e0 ["INT_ADD", "register:40f0:8", ["const:a409e0:8", "const:4:8"]]
- 00a409e0 ["CALLIND", null, ["register:0:8"]]
- 00a409e0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdd4e375385b22dcdcd5be62575c3ff3"></a>

### [`00a40b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40b98.md) → [`00a40d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a40/00a40d90.md) FUN_00a40d90

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00a40d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40d00.md) [`00a40d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40d04.md) [`00ac9398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac9398.md) [`00aca9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca9d8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00a40ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a40/00a40ef8.md) [`00a40efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a40/00a40efc.md) [`00ac9594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac9/00ac9594.md) [`00acabd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00acabd4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 66.67% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a40bd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a40bd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a40dd0"
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
      "unmatched:00a40bd8",
      "DATA",
      [
        "storage",
        "00c8b2c8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a40bd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a40bf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a40dfc"
      ]
    ]
  ],
  "added": [
    [
      "00a40dd0",
      "DATA",
      [
        "storage",
        "00c8b6c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00a40dd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00a40dec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a40dfc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a40bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40b98.md#insn-00a40bd8) · [`00a40bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40b98.md#insn-00a40bf4) · [`00a40c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40b98.md#insn-00a40c38)

~~~diff
- 00a40bd8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a40bd8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a40bd8 ["COPY", "tmp:2:8", ["register:8:8"]]
- 00a40bd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a40bd8 bytes e85700a9
- 00a40bf4 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00a40bf4 bytes 80000054
- 00a40c38 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a40c38 ["RETURN", null, ["register:0:8"]]
- 00a40c38 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4f0d14ee005121c03bab1509668e293"></a>

### [`00a40cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40cb8.md) → [`00a40eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a40/00a40eb0.md) FUN_00a40eb0

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00a40cdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a40cdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a40ed4"
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
      "unmatched:00a40cdc",
      "DATA",
      [
        "storage",
        "00c8b2c8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a40ce0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a40ce4",
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
      "00a40ed4",
      "DATA",
      [
        "storage",
        "00c8b6c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00a40ed8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a40edc",
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

- 旧版 [`00a40cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40cb8.md#insn-00a40cdc) · [`00a40ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40cb8.md#insn-00a40ce8)
- 新版 `00a40ed4`（命令位置の公開資料なし）

~~~diff
- 00a40cdc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a40cdc ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a40cdc ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a40cdc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a40cdc bytes 082400a9
- 00a40ce8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a40ce8 ["RETURN", null, ["register:0:8"]]
- 00a40ce8 bytes c0035fd6
+ 00a40ed4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a40ed4 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a40ed4 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00a40ed4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a40ed4 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23142687cfa2b3aebbb959829959e8a5"></a>

### [`00a4118c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a4118c.md) → [`00a41384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a41/00a41384.md) FUN_00a41384

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a413b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a413b4.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00a415ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a41/00a415ac.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.58% / 新版 96.58%

CFGの説明率　旧版 88.89% / 新版 85.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a41354"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a4154c"
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
      "unmatched:00a4134c",
      "READ",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a41354",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a415a8"
      ]
    ]
  ],
  "added": [
    [
      "00a41544",
      "READ",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00a4154c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a415a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a41354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a4118c.md#insn-00a41354) · [`00a411e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a4118c.md#insn-00a411e8)
- 新版 `00a4154c`（命令位置の公開資料なし） · `00a413e0`（命令位置の公開資料なし）

~~~diff
- 00a41354 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a41354 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 00a41354 bytes e1020054
+ 00a4154c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a4154c ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
+ 00a4154c bytes e1020054
- 00a411e8 ["INT_ADD", "register:40f0:8", ["const:a411e8:8", "const:4:8"]]
- 00a411e8 ["CALL", null, ["callee:00487a64:8"]]
+ 00a413e0 ["INT_ADD", "register:40f0:8", ["const:a413e0:8", "const:4:8"]]
+ 00a413e0 ["CALL", null, ["callee:00487a64:8"]]
- 00a411e8 bytes 0f1ae997
+ 00a413e0 bytes a119e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56fada682f9bb6485f1955616ad8f257"></a>

### [`00a42e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a42/00a42e60.md) → [`00a43058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a43/00a43058.md) FUN_00a43058

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005e15e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e15e0.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 5件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00853c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853c30.md) [`00a41e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41e38.md) [`00a41ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41ec4.md) [`00af34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af34c8.md)
- 新版 呼出元 2件 [`005e1620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1620.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 5件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00853c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853c70.md) [`00a42030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a42030.md) [`00a420bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a42/00a420bc.md) [`00af38f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af38f0.md)

変更の種類 branch_condition_or_target, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.21% / 新版 98.21%

CFGの説明率　旧版 30.77% / 新版 30.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a42ea8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a430a0"
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
      "unmatched:00a42ea8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a4311c"
      ]
    ]
  ],
  "added": [
    [
      "00a430a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a4311c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a42ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a42/00a42e60.md#insn-00a42ea8) · [`00a42e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a42/00a42e60.md#insn-00a42e74)
- 新版 `00a430a0`（命令位置の公開資料なし） · `00a4306c`（命令位置の公開資料なし）

~~~diff
- 00a42ea8 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00a42ea8 bytes e0030054
+ 00a430a0 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
+ 00a430a0 bytes e0030054
- 00a42e74 ["INT_ADD", "register:40f0:8", ["const:a42e74:8", "const:4:8"]]
- 00a42e74 ["CALL", null, ["callee:00a42030:8"]]
+ 00a4306c ["INT_ADD", "register:40f0:8", ["const:a4306c:8", "const:4:8"]]
+ 00a4306c ["CALL", null, ["callee:00a42030:8"]]
- 00a42e74 bytes f1fbff97
+ 00a4306c bytes f1fbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b349066d09f39419227cef09ce82f55c"></a>

### [`00a46a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46a3c.md) → [`00a46c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46c34.md) FUN_00a46c34

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 30件 [`005c4918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4918.md) [`005c6938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6938.md) [`005c8780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8780.md) [`005c8ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8ebc.md) [`00653560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/00653560.md) · 呼出先 2件 [`00a46a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46a3c.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md)
- 新版 呼出元 30件 [`005c4958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c4958.md) [`005c6978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6978.md) [`005c87c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c8/005c87c0.md) [`005c8efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c8/005c8efc.md) [`006535a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/006535a0.md) · 呼出先 2件 [`00a46c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46c34.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a46c84",
      "PARAM",
      [
        "storage",
        "00c8b378",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a46c88",
      "PARAM",
      [
        "storage",
        "00c8b388",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a46c84",
      "PARAM",
      [
        "storage",
        "00c8b778",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a46c88",
      "PARAM",
      [
        "storage",
        "00c8b788",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a46a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46a3c.md#insn-00a46a7c) · [`00a46a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46a3c.md#insn-00a46a80) · [`00a46a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46a3c.md#insn-00a46a84)
- 新版 `00a46c74`（命令位置の公開資料なし） · `00a46c7c`（命令位置の公開資料なし）

~~~diff
- 00a46a7c ["COPY", "tmp:0:8", ["const:378:8"]]
- 00a46a7c ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 00a46a7c ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 00a46a7c ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 00a46c74 ["COPY", "tmp:0:8", ["const:778:8"]]
+ 00a46c74 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 00a46c74 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 00a46c74 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 00a46a7c bytes f7e20d91
+ 00a46c74 bytes f7e21d91
- 00a46a80 ["COPY", "register:40c0:8", ["const:c8b000:8"]]
- 00a46a80 bytes 381200b0
- 00a46a84 ["COPY", "tmp:0:8", ["const:388:8"]]
- 00a46a84 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 00a46a84 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 00a46a84 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 00a46c7c ["COPY", "tmp:0:8", ["const:788:8"]]
+ 00a46c7c ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 00a46c7c ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 00a46c7c ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 00a46a84 bytes 18230e91
+ 00a46c7c bytes 18231e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ffe95e97576ac2be351d5904e2c6fd5"></a>

### [`00a46f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46f0c.md) → [`00a47104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47104.md) FUN_00a47104

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0046763c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046763c.md) [`004676a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004676a0.md) [`004676d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004676d8.md) [`004677e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004677e4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0046767c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046767c.md) [`004676e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/004676e0.md) [`00467718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467718.md) [`00467824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467824.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.15% / 新版 94.15%

CFGの説明率　旧版 65.45% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a46f2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a470d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a470d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a46f2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a47000",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a4729c"
      ]
    ]
  ],
  "added": [
    [
      "00a47124",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a471f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a4729c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a46f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46f0c.md#insn-00a46f2c) · [`00a47000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46f0c.md#insn-00a47000) · [`00a470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46f0c.md#insn-00a470d0)

~~~diff
- 00a46f2c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00a46f2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a46f2c bytes e80700f9
- 00a47000 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a47000 ["CBRANCH", null, ["local:b30:8", "tmp:0:1"]]
- 00a47000 bytes 21050054
- 00a470d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a0:8"]]
- 00a470d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:4"]]
- 00a470d0 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:4:8"]]
- 00a470d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5040:4"]]
- 00a470d0 bytes 610a142d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f53c99b69c170f8c70459694bd7d2aa7"></a>

### [`00a47830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47830.md) → [`00a47a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47a28.md) FUN_00a47a28

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`005c6114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6114.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c6154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6154.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4784c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a47a44"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a47850"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a4784c",
      "DATA",
      [
        "storage",
        "00c8b358",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a47850",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a47a8c"
      ]
    ]
  ],
  "added": [
    [
      "00a47a44",
      "DATA",
      [
        "storage",
        "00c8b758",
        null,
        "undefined *"
      ]
    ],
    [
      "00a47a48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a47a8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a4784c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47830.md#insn-00a4784c) · [`00a47850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47830.md#insn-00a47850)
- 新版 `00a47a44`（命令位置の公開資料なし）

~~~diff
- 00a4784c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a4784c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a4784c bytes 080000f9
- 00a47850 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00a47850 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00a47850 bytes 350200b4
+ 00a47a44 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00a47a44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00a47a44 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8bb789283a9d64877287f3b7a4575a4"></a>

### [`00a4efb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4e/00a4efb4.md) → [`00a4f1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f1ac.md) FUN_00a4f1ac

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 1件 [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 branch_condition_or_target, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 55.00% / 新版 55.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4f0d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00a4f2c8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a4f0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4e/00a4efb4.md#insn-00a4f0d0) · [`00a4efd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4e/00a4efb4.md#insn-00a4efd8)
- 新版 `00a4f2c8`（命令位置の公開資料なし） · `00a4f1d0`（命令位置の公開資料なし）

~~~diff
- 00a4f0d0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a4f0d0 ["RETURN", null, ["register:0:8"]]
- 00a4f0d0 bytes c0035fd6
+ 00a4f2c8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00a4f2c8 ["RETURN", null, ["register:0:8"]]
+ 00a4f2c8 bytes c0035fd6
- 00a4efd8 ["INT_ADD", "register:40f0:8", ["const:a4efd8:8", "const:4:8"]]
- 00a4efd8 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00a4f1d0 ["INT_ADD", "register:40f0:8", ["const:a4f1d0:8", "const:4:8"]]
+ 00a4f1d0 ["CALL", null, ["callee:00c57fe0:8"]]
- 00a4efd8 bytes 02230894
+ 00a4f1d0 bytes 84230894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a89999d3e2ea8be4edbad7516a7dc9ed"></a>

### [`00a5f690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f690.md) → [`00a5f888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5f/00a5f888.md) FUN_00a5f888

採用 · 移動量 `+0x1f8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00a5e71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e71c.md) [`00a5f690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f690.md) · 呼出先 3件 [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00a5f690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f690.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00a5e914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e914.md) [`00a5f888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5f/00a5f888.md) · 呼出先 3件 [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00a5f888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5f/00a5f888.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a5f8a4",
      "incomplete_value": true,
      "site": "00a5f8a8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4008:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a5f6ac",
      "incomplete_value": true,
      "site": "00a5f6b0",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a5f6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f690.md#insn-00a5f6b0) · [`00a5f69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f690.md#insn-00a5f69c) · [`00a5f6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f690.md#insn-00a5f6a0)
- 新版 `00a5f8a8`（命令位置の公開資料なし）

~~~diff
- 00a5f6b0 ["INT_ADD", "register:40f0:8", ["const:a5f6b0:8", "const:4:8"]]
- 00a5f6b0 ["CALL", null, ["local:b0:8"]]
+ 00a5f8a8 ["INT_ADD", "register:40f0:8", ["const:a5f8a8:8", "const:4:8"]]
+ 00a5f8a8 ["CALL", null, ["local:b0:8"]]
- 00a5f6b0 bytes f8ffff97
+ 00a5f8a8 bytes f8ffff97
- 00a5f69c ["COPY", "register:40e8:8", ["register:8:8"]]
- 00a5f69c bytes fd030091
- 00a5f6a0 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00a5f6a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00a5f6a0 bytes 280040f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e954de6d43c4db26ee9c13d927249d06"></a>

### [`00a5fea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5fea0.md) → [`00a60098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a60/00a60098.md) FUN_00a60098

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

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
      "site": "00a5fea0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5fea0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5fea4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a5fea0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5fea4",
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
      "00a60098",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a6009c",
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

- 旧版 [`00a5fea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5fea0.md#insn-00a5fea0) · [`00a5fea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5fea0.md#insn-00a5fea4)
- 新版 `00a60098`（命令位置の公開資料なし）

~~~diff
- 00a5fea0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a5fea0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a5fea0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a5fea0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a5fea0 bytes fd7bbea9
- 00a5fea4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a5fea4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00a5fea4 bytes f30b00f9
+ 00a60098 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00a60098 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00a60098 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00a60098 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00a60098 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e3c7279424e8138c22d00c1b0992221"></a>

### [`00a65668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65668.md) → [`00a65860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65860.md) FUN_00a65860

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`007dd760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd760.md) [`00a65868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65868.md) [`00a65a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65a74.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 3件 [`007dd7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd7a0.md) [`00a65a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65a60.md) [`00a65c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65c6c.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 84.91% / 新版 84.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a65730"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a65738"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a65928"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a65730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65668.md#insn-00a65730) · [`00a65738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65668.md#insn-00a65738)
- 新版 `00a65928`（命令位置の公開資料なし）

~~~diff
- 00a65730 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00a65730 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00a65730 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:30:8"]]
- 00a65730 ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:1:8"]]
- 00a65730 bytes 1f0d03f8
- 00a65738 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:28:8"]]
- 00a65738 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a65738 bytes 081400f9
+ 00a65928 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 00a65928 ["COPY", "tmp:1:8", ["tmp:0:8"]]
+ 00a65928 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:30:8"]]
+ 00a65928 ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:1:8"]]
+ 00a65928 bytes 1f0d03f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e6eff6b7cd70d542f227d87313d1568"></a>

### [`00a66a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a66a3c.md) → [`00a66c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a66/00a66c34.md) FUN_00a66c34

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 2件 [`00a65bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65bf4.md) [`00a662bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a662bc.md)
- 新版 呼出元 3件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 2件 [`00a65dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65dec.md) [`00a664b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a66/00a664b4.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00a66a6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00a66c64"
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
      "unmatched:00a66a6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ]
  ],
  "added": [
    [
      "00a66c64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a66a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a66/00a66a3c.md#insn-00a66a6c)
- 新版 `00a66c64`（命令位置の公開資料なし）

~~~diff
- 00a66a6c ["INT_ADD", "register:40f0:8", ["const:a66a6c:8", "const:4:8"]]
- 00a66a6c ["CALL", null, ["ram:a65bf4:8"]]
- 00a66a6c bytes 62fcff97
+ 00a66c64 ["INT_ADD", "register:40f0:8", ["const:a66c64:8", "const:4:8"]]
+ 00a66c64 ["CALL", null, ["ram:a65dec:8"]]
+ 00a66c64 bytes 62fcff97
~~~


<a id="compare-59fcb081d83422fc828403bc53e62b31"></a>

### [`00a68614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68614.md) → [`00a6880c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a6880c.md) FUN_00a6880c

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a68dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68dc0.md) · 呼出先 4件 [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`006917c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00691/006917c0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00a68fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68fb8.md) · 呼出先 4件 [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00691800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691800.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.23% / 新版 87.23%

CFGの説明率　旧版 60.71% / 新版 60.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a68618"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a68618"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6861c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a68618",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a6861c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a68620",
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
      "00a68810",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a68814",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00a68818",
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

- 旧版 [`00a68618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68614.md#insn-00a68618) · [`00a6861c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68614.md#insn-00a6861c) · [`00a68620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68614.md#insn-00a68620)

~~~diff
- 00a68618 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a68618 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a68618 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00a68618 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a68618 bytes fd7b03a9
- 00a6861c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a6861c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a6861c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00a6861c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6861c bytes fa6704a9
- 00a68620 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00a68620 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00a68620 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00a68620 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a68620 bytes f85f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-896ca930058f90cfd8718c59da95ca5c"></a>

### [`00a68dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68dc0.md) → [`00a68fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a68fb8.md) FUN_00a68fb8

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 6件 [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md) [`00a68614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68614.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 6件 [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md) [`00a6880c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a68/00a6880c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 60.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a68e1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a69014"
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
      "unmatched:00a68e1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a69100"
      ]
    ]
  ],
  "added": [
    [
      "00a69014",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a69100"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a68e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68dc0.md#insn-00a68e1c) · [`00a68dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68dc0.md#insn-00a68dfc)
- 新版 `00a69014`（命令位置の公開資料なし） · `00a68ff4`（命令位置の公開資料なし）

~~~diff
- 00a68e1c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a68e1c ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00a68e1c bytes 61070054
+ 00a69014 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a69014 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
+ 00a69014 bytes 61070054
- 00a68dfc ["INT_ADD", "register:40f0:8", ["const:a68dfc:8", "const:4:8"]]
- 00a68dfc ["CALL", null, ["callee:00480e28:8"]]
+ 00a68ff4 ["INT_ADD", "register:40f0:8", ["const:a68ff4:8", "const:4:8"]]
+ 00a68ff4 ["CALL", null, ["callee:00480e28:8"]]
- 00a68dfc bytes fb5fe897
+ 00a68ff4 bytes 8d5fe897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a476789fd6bf0c0ffa5b76d37fe8bdb"></a>

### [`00a69240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69240.md) → [`00a69438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a69/00a69438.md) FUN_00a69438

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a2de6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2d/00a2de6c.md) · 呼出先 1件 [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md)
- 新版 呼出元 1件 [`00a2e064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2e064.md) · 呼出先 1件 [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a69240"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a69240"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a69244"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a69240",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a69244",
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
      "00a69438",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a6943c",
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

- 旧版 [`00a69240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69240.md#insn-00a69240) · [`00a69244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69240.md#insn-00a69244)
- 新版 `00a69438`（命令位置の公開資料なし）

~~~diff
- 00a69240 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a69240 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a69240 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a69240 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a69240 bytes fd7bbea9
- 00a69244 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a69244 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a69244 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a69244 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a69244 bytes f44f01a9
+ 00a69438 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00a69438 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00a69438 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00a69438 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00a69438 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da5bcad0000b16b2f66c8776d9d411f3"></a>

### [`00a7b92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7b92c.md) → [`00a7bb24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7b/00a7bb24.md) FUN_00a7bb24

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00a7b92c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7b92c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7b930"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a7b92c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7b930",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7b950",
      "DATA",
      [
        "storage",
        "00c8b600",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7bb24",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a7bb28",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a7bb48",
      "DATA",
      [
        "storage",
        "00c8ba00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7b92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7b92c.md#insn-00a7b92c) · [`00a7b930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7b92c.md#insn-00a7b930) · [`00a7b950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7b92c.md#insn-00a7b950)

~~~diff
- 00a7b92c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a7b92c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a7b92c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a7b92c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a7b92c bytes fd7bbea9
- 00a7b930 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a7b930 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00a7b930 bytes f30b00f9
- 00a7b950 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a7b950 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a7b950 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a7b950 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7b950 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-205bccb9be65b2a9e3cff67c3fc1cf93"></a>

### [`00a7bc84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bc84.md) → [`00a7be7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7b/00a7be7c.md) FUN_00a7be7c

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00a7bca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7bca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a7bea0"
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
      "unmatched:00a7bca8",
      "DATA",
      [
        "storage",
        "00c8b700",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a7bcac",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7bcb0",
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
      "00a7bea0",
      "DATA",
      [
        "storage",
        "00c8bb00",
        null,
        "undefined *"
      ]
    ],
    [
      "00a7bea4",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a7bea8",
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

- 旧版 [`00a7bca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bc84.md#insn-00a7bca8) · [`00a7bcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bc84.md#insn-00a7bcb4)
- 新版 `00a7bea0`（命令位置の公開資料なし）

~~~diff
- 00a7bca8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a7bca8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a7bca8 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a7bca8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7bca8 bytes 082400a9
- 00a7bcb4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a7bcb4 ["RETURN", null, ["register:0:8"]]
- 00a7bcb4 bytes c0035fd6
+ 00a7bea0 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a7bea0 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a7bea0 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00a7bea0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a7bea0 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5acccb0bafdcf697c6ed79d147ac610"></a>

### [`00a7bcb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bcb8.md) → [`00a7beb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7b/00a7beb0.md) FUN_00a7beb0

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00a7bcc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7bcc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a7bebc"
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
      "unmatched:00a7bcc4",
      "DATA",
      [
        "storage",
        "00c8b700",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7bebc",
      "DATA",
      [
        "storage",
        "00c8bb00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7bcc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bcb8.md#insn-00a7bcc4) · [`00a7bcc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bcb8.md#insn-00a7bcc8)
- 新版 `00a7bebc`（命令位置の公開資料なし）

~~~diff
- 00a7bcc4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a7bcc4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a7bcc4 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00a7bcc4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7bcc4 bytes 292000a9
- 00a7bcc8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a7bcc8 ["RETURN", null, ["register:0:8"]]
- 00a7bcc8 bytes c0035fd6
+ 00a7bebc ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a7bebc ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00a7bebc ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00a7bebc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a7bebc bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19117e45f4af12adc432f8b2330f4c76"></a>

### [`00a7bf5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bf5c.md) → [`00a7c154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7c/00a7c154.md) FUN_00a7c154

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00a7bf74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a7c16c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7bf7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a7bf74",
      "DATA",
      [
        "storage",
        "00c8b770",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a7bf78",
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
      "00a7c16c",
      "DATA",
      [
        "storage",
        "00c8bb70",
        null,
        "undefined *"
      ]
    ],
    [
      "00a7c170",
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

- 旧版 [`00a7bf74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bf5c.md#insn-00a7bf74) · [`00a7bf7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7b/00a7bf5c.md#insn-00a7bf7c)
- 新版 `00a7c16c`（命令位置の公開資料なし）

~~~diff
- 00a7bf74 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a7bf74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a7bf74 bytes 080000f9
- 00a7bf7c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a7bf7c ["RETURN", null, ["register:0:8"]]
- 00a7bf7c bytes c0035fd6
+ 00a7c16c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00a7c16c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00a7c16c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d4efa88d9ce449e9b5cb141ca2752e1"></a>

### [`00a7c158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c158.md) → [`00a7c350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7c/00a7c350.md) FUN_00a7c350

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00a7c164"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7c164"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a7c35c"
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
      "unmatched:00a7c164",
      "DATA",
      [
        "storage",
        "00c8b880",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7c35c",
      "DATA",
      [
        "storage",
        "00c8bc80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7c164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c158.md#insn-00a7c164) · [`00a7c168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7c/00a7c158.md#insn-00a7c168)
- 新版 `00a7c35c`（命令位置の公開資料なし）

~~~diff
- 00a7c164 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a7c164 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a7c164 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00a7c164 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7c164 bytes 292000a9
- 00a7c168 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a7c168 ["RETURN", null, ["register:0:8"]]
- 00a7c168 bytes c0035fd6
+ 00a7c35c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a7c35c ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00a7c35c ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00a7c35c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a7c35c bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b8387ba04319b85eba8c9a5890f1527"></a>

### [`00a7e464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e464.md) → [`00a7e65c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e65c.md) FUN_00a7e65c

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00a7e488"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7e488"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a7e680"
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
      "unmatched:00a7e488",
      "DATA",
      [
        "storage",
        "00c8bca0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a7e48c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a7e490",
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
      "00a7e680",
      "DATA",
      [
        "storage",
        "00c8c0a0",
        null,
        "undefined *"
      ]
    ],
    [
      "00a7e684",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a7e688",
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

- 旧版 [`00a7e488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e464.md#insn-00a7e488) · [`00a7e494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e464.md#insn-00a7e494)
- 新版 `00a7e680`（命令位置の公開資料なし）

~~~diff
- 00a7e488 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a7e488 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a7e488 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a7e488 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a7e488 bytes 082400a9
- 00a7e494 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a7e494 ["RETURN", null, ["register:0:8"]]
- 00a7e494 bytes c0035fd6
+ 00a7e680 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a7e680 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a7e680 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00a7e680 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a7e680 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35284f6de89b8ae94b979767417d415a"></a>

### [`00a7e63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e63c.md) → [`00a7e834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7e834.md) FUN_00a7e834

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a7989c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a79/00a7989c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00a79a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a79/00a79a94.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 99.06% / 新版 99.06%

CFGの説明率　旧版 83.61% / 新版 85.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7e790"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a7e988"
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
      "unmatched:00a7e790",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a7e9a0"
      ]
    ]
  ],
  "added": [
    [
      "00a7e988",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a7e9a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7e790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e63c.md#insn-00a7e790) · [`00a7e644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e63c.md#insn-00a7e644)
- 新版 `00a7e988`（命令位置の公開資料なし） · `00a7e83c`（命令位置の公開資料なし）

~~~diff
- 00a7e790 ["INT_NOTEQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
- 00a7e790 ["CBRANCH", null, ["local:b38:8", "tmp:0:1"]]
- 00a7e790 bytes cb0000b5
+ 00a7e988 ["INT_NOTEQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
+ 00a7e988 ["CBRANCH", null, ["local:b37:8", "tmp:0:1"]]
+ 00a7e988 bytes cb0000b5
- 00a7e644 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
+ 00a7e83c ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00a7e644 bytes a0000054
+ 00a7e83c bytes a0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d3cf1d5da40128e40ccd0765170488c"></a>

### [`00a7e850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e850.md) → [`00a7ea48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7e/00a7ea48.md) FUN_00a7ea48

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00a7e858"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a7ea50"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00a7e85c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a7e858",
      "DATA",
      [
        "storage",
        "00c8bd20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a7ea50",
      "DATA",
      [
        "storage",
        "00c8c120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a7e858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e850.md#insn-00a7e858) · [`00a7e85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7e/00a7e850.md#insn-00a7e85c)
- 新版 `00a7ea50`（命令位置の公開資料なし）

~~~diff
- 00a7e858 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00a7e858 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a7e858 bytes 280000f9
- 00a7e85c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a7e85c ["RETURN", null, ["register:0:8"]]
- 00a7e85c bytes c0035fd6
+ 00a7ea50 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00a7ea50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00a7ea50 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1518f64742d7d7b2b1cbfdf9c5549e99"></a>

### [`00a80fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a80/00a80fd8.md) → [`00a811d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a81/00a811d0.md) FUN_00a811d0

採用 · 移動量 `+0x1f8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00a80fe4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a80fe4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a811dc"
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
      "unmatched:00a80fe4",
      "DATA",
      [
        "storage",
        "00c8bea0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a811dc",
      "DATA",
      [
        "storage",
        "00c8c2a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a80fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a80/00a80fd8.md#insn-00a80fe4) · [`00a80fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a80/00a80fd8.md#insn-00a80fe8)
- 新版 `00a811dc`（命令位置の公開資料なし）

~~~diff
- 00a80fe4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a80fe4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00a80fe4 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00a80fe4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a80fe4 bytes 292000a9
- 00a80fe8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a80fe8 ["RETURN", null, ["register:0:8"]]
- 00a80fe8 bytes c0035fd6
+ 00a811dc ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a811dc ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00a811dc ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00a811dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a811dc bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3108c94ed1d4f64826672501de3f57ee"></a>

### [`00a82908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a82/00a82908.md) → [`00a82b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a82/00a82b00.md) FUN_00a82b00

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00680dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00680/00680dc8.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`008eae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ea/008eae30.md) [`009f53b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f5/009f53b8.md) [`009f6a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009f6/009f6a78.md) · 呼出先 10件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`008bbc14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bbc14.md) [`00a84140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84140.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 5件 [`00680e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00680/00680e08.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`008eafcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ea/008eafcc.md) [`009f5554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5554.md) [`009f6c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6c14.md) · 呼出先 10件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`008bbc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bb/008bbc58.md) [`00a84338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a84/00a84338.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.77% / 新版 94.77%

CFGの説明率　旧版 62.50% / 新版 61.40%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a82940"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a82b38"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a82948"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a82940",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a82948",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a82b58"
      ]
    ],
    [
      "unmatched:00a82a20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a82d2c"
      ]
    ]
  ],
  "added": [
    [
      "00a82b38",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00a82b40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a82b58"
      ]
    ],
    [
      "00a82c18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a82d2c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a82940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a82/00a82908.md#insn-00a82940) · [`00a82948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a82/00a82908.md#insn-00a82948) · [`00a82a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a82/00a82908.md#insn-00a82a20)

~~~diff
- 00a82940 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a82940 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a82940 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a82940 bytes a8831ff8
- 00a82948 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a82948 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00a82948 bytes c80000b5
- 00a82a20 ["CBRANCH", null, ["local:b32:8", "register:101:1"]]
- 00a82a20 bytes a0080054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05463ea1cb38c8e105ee5c51453a2dce"></a>

### [`00a82d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a82/00a82d34.md) → [`00a82f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a82/00a82f2c.md) FUN_00a82f2c

採用 · 移動量 `+0x1f8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 9件 [`0067f004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067f/0067f004.md) [`006ff2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff2d8.md) [`0082c69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082c69c.md) [`008caa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa24.md) [`008dcf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dcf58.md) · 呼出先 6件 [`00869948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869948.md) [`00a82f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a82/00a82f34.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 9件 [`0067f044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067f/0067f044.md) [`006ff318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff318.md) [`0082c6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c6dc.md) [`008cabc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008cabc0.md) [`008dd0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008dd0f4.md) · 呼出先 6件 [`00869988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869988.md) [`00a8312c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a83/00a8312c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.97% / 新版 92.97%

CFGの説明率　旧版 88.52% / 新版 88.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a82d38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a82d38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a82d3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a82d38",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a82d3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a82d40",
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
      "00a82f30",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a82f34",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a82f38",
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

- 旧版 [`00a82d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a82/00a82d34.md#insn-00a82d38) · [`00a82d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a82/00a82d34.md#insn-00a82d3c) · [`00a82d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a82/00a82d34.md#insn-00a82d40)

~~~diff
- 00a82d38 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a82d38 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a82d38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00a82d38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a82d38 bytes fd7b04a9
- 00a82d3c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 00a82d3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00a82d3c bytes fb2b00f9
- 00a82d40 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a82d40 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a82d40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00a82d40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a82d40 bytes fa6706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93e22bfbde816c86e24543c2a8a776de"></a>

### [`00a84be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84be8.md) → [`00a84de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a84/00a84de0.md) FUN_00a84de0

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 1件 [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md)
- 新版 呼出元 1件 [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 1件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a84c10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a84e08"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a84c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84be8.md#insn-00a84c10) · [`00a84c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a84/00a84be8.md#insn-00a84c24)
- 新版 `00a84e08`（命令位置の公開資料なし） · `00a84e1c`（命令位置の公開資料なし）

~~~diff
- 00a84c10 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a84c10 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:80:8"]]
- 00a84c10 ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:0:8"]]
- 00a84c10 bytes 880e08f8
+ 00a84e08 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a84e08 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:80:8"]]
+ 00a84e08 ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:0:8"]]
+ 00a84e08 bytes 880e08f8
- 00a84c24 ["INT_ADD", "register:40f0:8", ["const:a84c24:8", "const:4:8"]]
- 00a84c24 ["CALL", null, ["callee:0048ce84:8"]]
+ 00a84e1c ["INT_ADD", "register:40f0:8", ["const:a84e1c:8", "const:4:8"]]
+ 00a84e1c ["CALL", null, ["callee:0048ce84:8"]]
- 00a84c24 bytes 8820e897
+ 00a84e1c bytes 1a20e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28af54bbe94d8d270a71a0b37cc95b8d"></a>

### [`00a86c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86c20.md) → [`00a86e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a86/00a86e18.md) FUN_00a86e18

採用 · 移動量 `+0x1f8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 1件 [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 1件 [`00480744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 64.29% / 新版 64.29%

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
      "site": "00a86c20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a86c20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a86c24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a86c20",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a86c24",
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
      "00a86e18",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a86e1c",
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

- 旧版 [`00a86c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86c20.md#insn-00a86c20) · [`00a86c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86c20.md#insn-00a86c24) · [`00a86c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86c20.md#insn-00a86c48)

~~~diff
- 00a86c20 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a86c20 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a86c20 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a86c20 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a86c20 bytes fd7bbea9
- 00a86c24 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a86c24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00a86c24 bytes f30b00f9
- 00a86c48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:70:8"]]
- 00a86c48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:8"]]
- 00a86c48 bytes 603a00fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1440dfc4352d03338b95df7dd19d3c69"></a>

### [`00a86c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86c6c.md) → [`00a86e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a86/00a86e64.md) FUN_00a86e64

採用 · 移動量 `+0x1f8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 1件 [`00480704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480704.md)
- 新版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 1件 [`00480744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 35.71% / 新版 35.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a86c6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a86c6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a86c70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a86c6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a86c70",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a86c88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a86c98"
      ]
    ]
  ],
  "added": [
    [
      "00a86e64",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a86e68",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a86e80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a86e90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a86c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86c6c.md#insn-00a86c6c) · [`00a86c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86c6c.md#insn-00a86c70) · [`00a86c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a86/00a86c6c.md#insn-00a86c88)

~~~diff
- 00a86c6c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a86c6c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a86c6c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a86c6c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a86c6c bytes fd7bbea9
- 00a86c70 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a86c70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00a86c70 bytes f30b00f9
- 00a86c88 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a86c88 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 00a86c88 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00a86c88 bytes 8d000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb4814fc7b3e526ada5d65b02adbbf68"></a>

### [`00a99d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a99/00a99d14.md) → [`00a99f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a99/00a99f0c.md) FUN_00a99f0c

採用 · 移動量 `+0x1f8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 62.50% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a99d3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a99d90"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a99f34"
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
      "unmatched:00a99d3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a99f44"
      ]
    ],
    [
      "00a99f74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a99d8c"
      ]
    ],
    [
      "unmatched:00a99d90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a99f7c"
      ]
    ]
  ],
  "added": [
    [
      "00a99f34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a99f44"
      ]
    ],
    [
      "00a99f74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a99f84"
      ]
    ],
    [
      "00a99f88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a99f7c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a99d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a99/00a99d14.md#insn-00a99d3c) · [`00a99d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a99/00a99d14.md#insn-00a99d90)
- 新版 `00a99f34`（命令位置の公開資料なし）

~~~diff
- 00a99d3c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a99d3c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00a99d3c bytes 81000054
- 00a99d90 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00a99d90 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00a99d90 bytes a0ffffb4
+ 00a99f34 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a99f34 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00a99f34 bytes 81000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c86b8bf91a9f9c83651fc6d0fbbfa966"></a>

### [`00a9a1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9a1b8.md) → [`00a9a3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9a/00a9a3b4.md) FUN_00a9a3b4

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00a955d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a95/00a955d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00a957c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a95/00a957c8.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 87.50% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9a1dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00a9a3d8"
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
      "unmatched:00a9a1dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00a9a3d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9a1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9a1b8.md#insn-00a9a1dc) · [`00a9a1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9a1b8.md#insn-00a9a1c4)
- 新版 `00a9a3d8`（命令位置の公開資料なし） · `00a9a3c0`（命令位置の公開資料なし）

~~~diff
- 00a9a1dc ["INT_ADD", "register:40f0:8", ["const:a9a1dc:8", "const:4:8"]]
- 00a9a1dc ["CALL", null, ["ram:47acb4:8"]]
- 00a9a1dc bytes b682e797
+ 00a9a3d8 ["INT_ADD", "register:40f0:8", ["const:a9a3d8:8", "const:4:8"]]
+ 00a9a3d8 ["CALL", null, ["ram:47acf4:8"]]
+ 00a9a3d8 bytes 4782e797
- 00a9a1c4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a9a1c4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00a9a3c0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a9a3c0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00a9a1c4 bytes c1010054
+ 00a9a3c0 bytes c1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-689bba211a7130cc379f7130a7c089af"></a>

### [`00a9a240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9a240.md) → [`00a9a43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9a/00a9a43c.md) FUN_00a9a43c

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00a9a264"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9a264"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a9a460"
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
      "unmatched:00a9a264",
      "DATA",
      [
        "storage",
        "00c8c768",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a9a268",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a9a26c",
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
      "00a9a460",
      "DATA",
      [
        "storage",
        "00c8cb68",
        null,
        "undefined *"
      ]
    ],
    [
      "00a9a464",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a9a468",
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

- 旧版 [`00a9a264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9a240.md#insn-00a9a264) · [`00a9a270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9a240.md#insn-00a9a270)
- 新版 `00a9a460`（命令位置の公開資料なし）

~~~diff
- 00a9a264 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a9a264 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a9a264 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a9a264 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a9a264 bytes 082400a9
- 00a9a270 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a9a270 ["RETURN", null, ["register:0:8"]]
- 00a9a270 bytes c0035fd6
+ 00a9a460 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a9a460 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a9a460 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00a9a460 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a9a460 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33739fcbdfa0ab2070d5c7dc26190570"></a>

### [`00a9a544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9a544.md) → [`00a9a740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9a/00a9a740.md) FUN_00a9a740

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 60.00% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9a568"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00a9a764"
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
      "unmatched:00a9a568",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00a9a764",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9a568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9a544.md#insn-00a9a568) · [`00a9a54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9a544.md#insn-00a9a54c)
- 新版 `00a9a764`（命令位置の公開資料なし） · `00a9a748`（命令位置の公開資料なし）

~~~diff
- 00a9a568 ["INT_ADD", "register:40f0:8", ["const:a9a568:8", "const:4:8"]]
- 00a9a568 ["CALL", null, ["ram:47acb4:8"]]
- 00a9a568 bytes d381e797
+ 00a9a764 ["INT_ADD", "register:40f0:8", ["const:a9a764:8", "const:4:8"]]
+ 00a9a764 ["CALL", null, ["ram:47acf4:8"]]
+ 00a9a764 bytes 6481e797
- 00a9a54c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a9a54c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00a9a748 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a9a748 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00a9a54c bytes e1010054
+ 00a9a748 bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca74c9f9a70f0ca39e220f9528a50661"></a>

### [`00a9a924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9a924.md) → [`00a9ab20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9a/00a9ab20.md) FUN_00a9ab20

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0046ca88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca88.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0046cac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cac8.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 62.50% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9a944"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a9ab40"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9a94c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a9a944",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9ab68"
      ]
    ],
    [
      "unmatched:00a9a94c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00a9ab40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9ab68"
      ]
    ],
    [
      "00a9ab48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9a944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9a924.md#insn-00a9a944) · [`00a9a94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9a924.md#insn-00a9a94c)
- 新版 `00a9ab40`（命令位置の公開資料なし）

~~~diff
- 00a9a944 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00a9a944 bytes 40010054
- 00a9a94c ["INT_ADD", "register:40f0:8", ["const:a9a94c:8", "const:4:8"]]
- 00a9a94c ["CALL", null, ["ram:47acb4:8"]]
- 00a9a94c bytes da80e797
+ 00a9ab40 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 00a9ab40 bytes 40010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-375c8d3ab8da3aad118c7cf5c43d8617"></a>

### [`00a9b0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9b/00a9b0e0.md) → [`00a9b2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9b/00a9b2dc.md) FUN_00a9b2dc

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00a9b104"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9b104"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a9b300"
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
      "unmatched:00a9b104",
      "DATA",
      [
        "storage",
        "00c8cce8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a9b108",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a9b10c",
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
      "00a9b300",
      "DATA",
      [
        "storage",
        "00c8d0e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00a9b304",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a9b308",
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

- 旧版 [`00a9b104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9b/00a9b0e0.md#insn-00a9b104) · [`00a9b110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9b/00a9b0e0.md#insn-00a9b110)
- 新版 `00a9b300`（命令位置の公開資料なし）

~~~diff
- 00a9b104 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a9b104 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a9b104 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00a9b104 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a9b104 bytes 082400a9
- 00a9b110 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a9b110 ["RETURN", null, ["register:0:8"]]
- 00a9b110 bytes c0035fd6
+ 00a9b300 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a9b300 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a9b300 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00a9b300 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00a9b300 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55857e6a72f78cbfbd2d4903af765116"></a>

### [`00a9f220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9f/00a9f220.md) → [`00a9f41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9f/00a9f41c.md) FUN_00a9f41c

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00763d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00763/00763d18.md) · 呼出先 4件 [`0055f538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f538.md) [`00a9f460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9f/00a9f460.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00763d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00763/00763d58.md) · 呼出先 4件 [`0055f578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055f578.md) [`00a9f65c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9f/00a9f65c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 99.26% / 新版 99.26%

CFGの説明率　旧版 92.00% / 新版 93.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9f304"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a9f500"
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
      "unmatched:00a9f304",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9f4f0"
      ]
    ]
  ],
  "added": [
    [
      "00a9f500",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9f4f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9f304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9f/00a9f220.md#insn-00a9f304) · [`00a9f25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9f/00a9f220.md#insn-00a9f25c)
- 新版 `00a9f500`（命令位置の公開資料なし） · `00a9f458`（命令位置の公開資料なし）

~~~diff
- 00a9f304 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a9f304 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00a9f304 bytes 81ffff54
+ 00a9f500 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00a9f500 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00a9f500 bytes 81ffff54
- 00a9f25c ["INT_ADD", "register:40f0:8", ["const:a9f25c:8", "const:4:8"]]
- 00a9f25c ["CALL", null, ["callee:00a9f65c:8"]]
+ 00a9f458 ["INT_ADD", "register:40f0:8", ["const:a9f458:8", "const:4:8"]]
+ 00a9f458 ["CALL", null, ["callee:00a9f65c:8"]]
- 00a9f25c bytes 81000094
+ 00a9f458 bytes 81000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f26ef20306d95147d0a76cb64df08cf3"></a>

### [`00a9f460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9f/00a9f460.md) → [`00a9f65c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9f/00a9f65c.md) FUN_00a9f65c

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a9f220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9f/00a9f220.md) · 呼出先 8件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00615ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615ea0.md) [`00aa006c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa0/00aa006c.md) [`00aa0d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa0/00aa0d80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00a9f41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9f/00a9f41c.md) · 呼出先 8件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00615ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615ee0.md) [`00aa0268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa0/00aa0268.md) [`00aa0f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa0/00aa0f7c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 93.03% / 新版 93.03%

CFGの説明率　旧版 80.72% / 新版 80.72%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9f638"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9f638"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9f63c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a9f600",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9f828"
      ]
    ],
    [
      "00a9f874",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a9f688"
      ]
    ],
    [
      "unmatched:00a9f684",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00615ee0"
      ]
    ]
  ],
  "added": [
    [
      "00a9f7fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9f828"
      ]
    ],
    [
      "00a9f874",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9f884"
      ]
    ],
    [
      "00a9f880",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00615ee0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9f4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9f/00a9f460.md#insn-00a9f4a0) · [`00a9f600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9f/00a9f460.md#insn-00a9f600) · [`00a9f638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9f/00a9f460.md#insn-00a9f638)
- 新版 `00a9f69c`（命令位置の公開資料なし）

~~~diff
- 00a9f4a0 ["INT_ADD", "register:40f0:8", ["const:a9f4a0:8", "const:4:8"]]
- 00a9f4a0 ["CALL", null, ["callee:00aa0268:8"]]
+ 00a9f69c ["INT_ADD", "register:40f0:8", ["const:a9f69c:8", "const:4:8"]]
+ 00a9f69c ["CALL", null, ["callee:00aa0268:8"]]
- 00a9f4a0 bytes f3020094
+ 00a9f69c bytes f3020094
- 00a9f600 ["CBRANCH", null, ["local:b30:8", "register:101:1"]]
- 00a9f600 bytes 60010054
- 00a9f638 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00a9f638 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a9f638 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00a9f638 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00a9f638 bytes bf7e00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f1cd1fcae9d78296340e1f3130cbb4c"></a>

### [`00aa16c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa16c8.md) → [`00aa18c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa1/00aa18c4.md) FUN_00aa18c4

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a9be68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9b/00a9be68.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00aa1890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa1890.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00a9c064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9c/00a9c064.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00aa1a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa1/00aa1a8c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 60.00% / 新版 58.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa1800"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aa19fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa1718"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa1718",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa1a80"
      ]
    ]
  ],
  "added": [
    [
      "00aa1914",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa1a80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa1718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa16c8.md#insn-00aa1718) · [`00aa1748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa16c8.md#insn-00aa1748) · [`00aa1750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa16c8.md#insn-00aa1750)

~~~diff
- 00aa1718 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00aa1718 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00aa1718 ["CBRANCH", null, ["local:b21:8", "tmp:1:1"]]
- 00aa1718 bytes 680b0054
- 00aa1748 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00aa1748 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00aa1748 ["COPY", "tmp:2:8", ["register:4058:8"]]
- 00aa1748 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00aa1748 bytes 6981899a
- 00aa1750 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00aa1750 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00aa1750 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00aa1750 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00aa1750 bytes 3531889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-822a36366977470ba4b9cbd5aa1b5e6e"></a>

### [`00aa18a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa18a4.md) → [`00aa1aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa1/00aa1aa0.md) FUN_00aa1aa0

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00aa11f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa11f0.md) [`00aa1bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa1bb0.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00aa13ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa1/00aa13ec.md) [`00aa1dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa1/00aa1dac.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 99.06% / 新版 99.06%

CFGの説明率　旧版 77.05% / 新版 75.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa1978"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aa1b74"
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
      "unmatched:00aa1978",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa1b5c"
      ]
    ]
  ],
  "added": [
    [
      "00aa1b74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa1b5c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa1978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa18a4.md#insn-00aa1978) · [`00aa18d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa18a4.md#insn-00aa18d0)
- 新版 `00aa1b74`（命令位置の公開資料なし） · `00aa1acc`（命令位置の公開資料なし）

~~~diff
- 00aa1978 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00aa1978 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 00aa1978 bytes 4bffff54
+ 00aa1b74 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00aa1b74 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
+ 00aa1b74 bytes 4bffff54
- 00aa18d0 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00aa18d0 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 00aa1acc ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00aa1acc ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00aa18d0 bytes 490200b4
+ 00aa1acc bytes 490200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ba9c1344fa7030404d7a4a7482d06b1"></a>

### [`00aa1b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa1b14.md) → [`00aa1d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa1/00aa1d10.md) FUN_00aa1d10

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.21% / 新版 84.21%

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
      "site": "00aa1b14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa1b14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa1b18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa1b14",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa1b18",
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
      "00aa1d10",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa1d14",
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

- 旧版 [`00aa1b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa1b14.md#insn-00aa1b14) · [`00aa1b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa1b14.md#insn-00aa1b18)
- 新版 `00aa1d10`（命令位置の公開資料なし）

~~~diff
- 00aa1b14 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa1b14 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa1b14 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00aa1b14 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa1b14 bytes fd7bbea9
- 00aa1b18 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aa1b18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00aa1b18 bytes f30b00f9
+ 00aa1d10 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00aa1d10 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00aa1d10 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00aa1d10 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00aa1d10 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e8d38899d8c96c97c19c23871619b5f"></a>

### [`00aa1bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa1bb0.md) → [`00aa1dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa1/00aa1dac.md) FUN_00aa1dac

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00aa006c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa0/00aa006c.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00aa18a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa18a4.md) [`00aa1a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa1a4c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00aa0268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa0/00aa0268.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00aa1aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa1/00aa1aa0.md) [`00aa1c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa1/00aa1c48.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 86.96% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa1c3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa1c3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa1c40"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa1c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa1bb0.md#insn-00aa1c3c) · [`00aa1c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa1bb0.md#insn-00aa1c40) · [`00aa1c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa1bb0.md#insn-00aa1c44)

~~~diff
- 00aa1c3c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00aa1c3c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aa1c3c ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00aa1c3c ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00aa1c3c bytes 3f7c00a9
- 00aa1c40 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:10:8"]]
- 00aa1c40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00aa1c40 bytes 280800f9
- 00aa1c44 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aa1c44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00aa1c44 bytes c10200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39fef64865c2f263d6f1b4f1490582d6"></a>

### [`00aa6f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa6/00aa6f4c.md) → [`00aa7148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa7/00aa7148.md) FUN_00aa7148

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 1件 [`00aac7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aac/00aac7f8.md)
- 新版 呼出元 1件 [`00aa3e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa3/00aa3e24.md) · 呼出先 1件 [`00aac9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aac/00aac9f4.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 45.45% / 新版 45.45%

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
      "site": "00aa6f64"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00aa7160"
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
      "00aa714c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aa6f6c"
      ]
    ],
    [
      "unmatched:00aa6f60",
      "PARAM",
      [
        "storage",
        "002b32f7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00aa6f64",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00aac9f4"
      ]
    ]
  ],
  "added": [
    [
      "00aa714c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa7168"
      ]
    ],
    [
      "00aa715c",
      "PARAM",
      [
        "storage",
        "002b3337",
        null,
        "string"
      ]
    ],
    [
      "00aa7160",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00aac9f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa6f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa6/00aa6f4c.md#insn-00aa6f64) · [`00aa6f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa6/00aa6f4c.md#insn-00aa6f50)
- 新版 `00aa7160`（命令位置の公開資料なし） · `00aa714c`（命令位置の公開資料なし）

~~~diff
- 00aa6f64 ["INT_ADD", "register:40f0:8", ["const:aa6f64:8", "const:4:8"]]
- 00aa6f64 ["CALL", null, ["callee:00aac9f4:8"]]
- 00aa6f64 bytes 25160094
+ 00aa7160 ["INT_ADD", "register:40f0:8", ["const:aa7160:8", "const:4:8"]]
+ 00aa7160 ["CALL", null, ["callee:00aac9f4:8"]]
+ 00aa7160 bytes 25160094
- 00aa6f50 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00aa6f50 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00aa714c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00aa714c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aa6f50 bytes eb000054
+ 00aa714c bytes eb000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-040cb83804bb2685666c97c63cd1aa5c"></a>

### [`00aa8d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa8/00aa8d8c.md) → [`00aa8f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa8/00aa8f88.md) FUN_00aa8f88

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 9件 [`00784240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784240.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0087925c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/0087925c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00aa3e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa3/00aa3e24.md) · 呼出先 9件 [`00784280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00784/00784280.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0087929c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/0087929c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 79.57% / 新版 79.57%

CFGの説明率　旧版 50.00% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa8dcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa8e10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa8e30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa8dcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa8de0",
      "PARAM",
      [
        "storage",
        "002a7e44",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00aa8de0",
      "PARAM",
      [
        "storage",
        "002b0ed1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aa8fc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00aa8fdc",
      "PARAM",
      [
        "storage",
        "002a7f20",
        null,
        "string"
      ]
    ],
    [
      "00aa8fdc",
      "PARAM",
      [
        "storage",
        "002b0f11",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa8dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa8/00aa8d8c.md#insn-00aa8dcc) · [`00aa8de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa8/00aa8d8c.md#insn-00aa8de0) · [`00aa8e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa8/00aa8d8c.md#insn-00aa8e10)

~~~diff
- 00aa8dcc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aa8dcc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00aa8dcc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00aa8dcc bytes a9831ff8
- 00aa8de0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aa8de0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00aa8de0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aa8de0 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00aa8de0 bytes 2101889a
- 00aa8e10 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:48:8"]]
- 00aa8e10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00aa8e10 bytes e82700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d75c70711d9feb0249ec1da5d57f8a0"></a>

### [`00aadd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadd94.md) → [`00aadf90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aad/00aadf90.md) FUN_00aadf90

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`00624768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00624/00624768.md) · 呼出先 1件 [`00aac7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aac/00aac7f8.md)
- 新版 呼出元 2件 [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`006247a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/006247a8.md) · 呼出先 1件 [`00aac9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aac/00aac9f4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 40.00% / 新版 40.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aadf90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aadd9c"
      ]
    ],
    [
      "unmatched:00aadda0",
      "PARAM",
      [
        "storage",
        "002bf677",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00aadda4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00aac9f4"
      ]
    ]
  ],
  "added": [
    [
      "00aadf90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aadf98"
      ]
    ],
    [
      "00aadf9c",
      "PARAM",
      [
        "storage",
        "002bf6b7",
        null,
        "string"
      ]
    ],
    [
      "00aadfa0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00aac9f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aadd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadd94.md#insn-00aadd9c) · [`00aadda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadd94.md#insn-00aadda0) · [`00aadda4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadd94.md#insn-00aadda4)

~~~diff
- 00aadd9c ["COPY", "register:4000:8", ["const:2bf000:8"]]
- 00aadd9c bytes 80c0ffd0
- 00aadda0 ["COPY", "tmp:0:8", ["const:677:8"]]
- 00aadda0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aadda0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aadda0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aadda0 bytes 00dc1991
- 00aadda4 ["BRANCH", null, ["callee:00aac9f4:8"]]
- 00aadda4 bytes 95faff17
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9a6fdcfe9e07536bdc3146ce8d20606"></a>

### [`00aae2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae2a8.md) → [`00aae4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aae/00aae4a4.md) FUN_00aae4a4

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 33.33% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aae2b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aae2cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aae4ac"
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
      "unmatched:00aae2b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aae4f0"
      ]
    ],
    [
      "unmatched:00aae2cc",
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
      "00aae4b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aae4f0"
      ]
    ],
    [
      "00aae4c8",
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

- 旧版 [`00aae2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae2a8.md#insn-00aae2b0) · [`00aae2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae2a8.md#insn-00aae2b4) · [`00aae2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae2a8.md#insn-00aae2cc)

~~~diff
- 00aae2b0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aae2b0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aae2b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aae2b0 bytes 1f0100f9
- 00aae2b4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00aae2b4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00aae2b4 bytes 000200b4
- 00aae2cc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aae2cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00aae2cc bytes f30b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef1d5e3cf13f83c9f0095c92f7253048"></a>

### [`00aae2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae2f8.md) → [`00aae4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aae/00aae4f4.md) FUN_00aae4f4

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00aa76e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa7/00aa76e4.md) [`00aa82a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa8/00aa82a8.md) [`00aae2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae2f8.md) · 呼出先 2件 [`00aae2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae2f8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`00aa78e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa7/00aa78e0.md) [`00aa84a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa8/00aa84a4.md) [`00aae4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aae/00aae4f4.md) · 呼出先 2件 [`00aae4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aae/00aae4f4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aae300"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aae300"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aae4fc"
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
      "unmatched:00aae300",
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
      "00aae4fc",
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

- 旧版 [`00aae300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae2f8.md#insn-00aae300) · [`00aae304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae2f8.md#insn-00aae304)
- 新版 `00aae4fc`（命令位置の公開資料なし）

~~~diff
- 00aae300 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aae300 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aae300 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aae300 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aae300 bytes f44f01a9
+ 00aae4fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00aae4fc ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00aae4fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
+ 00aae4fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00aae4fc bytes f44f01a9
- 00aae304 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00aae304 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee172a015da0506278b1b58947dfc480"></a>

### [`00ab7ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab7/00ab7ad8.md) → [`00ab7cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab7/00ab7cd4.md) FUN_00ab7cd4

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00672708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672708.md) [`0067e5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e5a8.md) [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00672748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672748.md) [`0067e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e5e8.md) [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 73.53% / 新版 73.53%

CFGの説明率　旧版 42.86% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ab7ad8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ab7ad8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ab7adc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ab7ad8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ab7adc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ab7af0",
      "DATA",
      [
        "storage",
        "00c8cd68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ab7cd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ab7cd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ab7cec",
      "DATA",
      [
        "storage",
        "00c8d168",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ab7ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab7/00ab7ad8.md#insn-00ab7ad8) · [`00ab7adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab7/00ab7ad8.md#insn-00ab7adc) · [`00ab7af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab7/00ab7ad8.md#insn-00ab7af0)

~~~diff
- 00ab7ad8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ab7ad8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ab7ad8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ab7ad8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ab7ad8 bytes fd7bbea9
- 00ab7adc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ab7adc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ab7adc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ab7adc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ab7adc bytes f44f01a9
- 00ab7af0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00ab7af0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ab7af0 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1f462f7bc02750734f2d95e0e313192"></a>

### [`00ab8fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab8/00ab8fbc.md) → [`00ab91b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab9/00ab91b8.md) FUN_00ab91b8

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`0085bec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085bec8.md) [`00ab28dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab2/00ab28dc.md) [`00ab2fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab2/00ab2fa8.md) [`00ab4b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab4/00ab4b04.md) · 呼出先 3件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 10件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`0085bf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085bf08.md) [`00ab2ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab2/00ab2ad8.md) [`00ab31a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab3/00ab31a4.md) [`00ab4d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab4/00ab4d00.md) · 呼出先 3件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.49% / 新版 80.49%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ab8ff4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ab8ff8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ab8ff8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ab9008",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ab9230"
      ]
    ]
  ],
  "added": [
    [
      "00ab9204",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ab9230"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ab8ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab8/00ab8fbc.md#insn-00ab8ff4) · [`00ab8ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab8/00ab8fbc.md#insn-00ab8ff8) · [`00ab9000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab8/00ab8fbc.md#insn-00ab9000)

~~~diff
- 00ab8ff4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00ab8ff4 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00ab8ff4 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:8:8"]]
- 00ab8ff4 ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:1:8"]]
- 00ab8ff4 bytes 9f8e00f8
- 00ab8ff8 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00ab8ff8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ab8ff8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00ab8ff8 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00ab8ff8 bytes 7f7e01a9
- 00ab9000 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ab9000 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00ab9000 bytes 680200b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0393a74d2c9cf085e3af8a1cdd50f13"></a>

### [`00ab9834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab9834.md) → [`00ab9a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab9/00ab9a30.md) FUN_00ab9a30

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ab95b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab95b4.md) · 呼出先 4件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00ab97b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab9/00ab97b0.md) · 呼出先 4件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 72.06% / 新版 72.06%

CFGの説明率　旧版 27.78% / 新版 31.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ab9860"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ab9868"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ab9868"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ab9860",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ab9868",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ab9870",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ab9a5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00ab9a64",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00ab9a6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ab9860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab9834.md#insn-00ab9860) · [`00ab9868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab9834.md#insn-00ab9868) · [`00ab9870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab9834.md#insn-00ab9870)

~~~diff
- 00ab9860 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ab9860 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00ab9860 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ab9860 bytes a8831ff8
- 00ab9868 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00ab9868 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00ab9868 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:18:8"]]
- 00ab9868 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ab9868 bytes e0a301a9
- 00ab9870 ["COPY", "tmp:0:8", ["register:4018:8"]]
- 00ab9870 ["COPY", "tmp:1:8", ["register:4018:8"]]
- 00ab9870 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:8:8"]]
- 00ab9870 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ab9870 bytes e38f00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a4b4ac74b40ca9d23c39e5ba3709411"></a>

### [`00aba964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00aba964.md) → [`00abab60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aba/00abab60.md) FUN_00abab60

採用 · 移動量 `+0x1fc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) · 呼出先 4件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00ab8fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab8/00ab8fbc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 4件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00ab91b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab9/00ab91b8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.91% / 新版 81.91%

CFGの説明率　旧版 52.00% / 新版 48.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aba978"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aba978"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aba97c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aba978",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aba97c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aba990",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00abab74",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00abab78",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00abab8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aba978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00aba964.md#insn-00aba978) · [`00aba97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00aba964.md#insn-00aba97c) · [`00aba990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00aba964.md#insn-00aba990)

~~~diff
- 00aba978 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aba978 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aba978 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00aba978 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aba978 bytes f65708a9
- 00aba97c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aba97c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aba97c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00aba97c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aba97c bytes f44f09a9
- 00aba990 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aba990 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00aba990 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00aba990 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50f1e232e74d3e44133ac60659c8a24a"></a>

### [`00abaf28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00abaf28.md) → [`00abb124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abb/00abb124.md) FUN_00abb124

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`0069a4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a4c4.md) [`007caa88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007caa88.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) [`00aba520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00aba520.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 6件 [`0069a504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069a/0069a504.md) [`007caac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007caac8.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) [`00aba71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aba/00aba71c.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 14.29% / 新版 11.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00abaf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00abaf28.md#insn-00abaf40) · [`00abaf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00abaf28.md#insn-00abaf58) · [`00abaf60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00abaf28.md#insn-00abaf60)
- 新版 `00abb13c`（命令位置の公開資料なし） · `00abb154`（命令位置の公開資料なし） · `00abb15c`（命令位置の公開資料なし）

~~~diff
- 00abaf40 ["INT_ADD", "register:40f0:8", ["const:abaf40:8", "const:4:8"]]
- 00abaf40 ["CALL", null, ["callee:008514f8:8"]]
+ 00abb13c ["INT_ADD", "register:40f0:8", ["const:abb13c:8", "const:4:8"]]
+ 00abb13c ["CALL", null, ["callee:008514f8:8"]]
- 00abaf40 bytes 5e59f697
+ 00abb13c bytes ef58f697
- 00abaf58 ["BRANCH", null, ["local:b2:8"]]
+ 00abb154 ["BRANCH", null, ["local:b5:8"]]
- 00abaf58 bytes 09000014
+ 00abb154 bytes 09000014
- 00abaf60 ["INT_ADD", "register:40f0:8", ["const:abaf60:8", "const:4:8"]]
- 00abaf60 ["CALL", null, ["callee:008514f8:8"]]
+ 00abb15c ["INT_ADD", "register:40f0:8", ["const:abb15c:8", "const:4:8"]]
+ 00abb15c ["CALL", null, ["callee:008514f8:8"]]
- 00abaf60 bytes 5659f697
+ 00abb15c bytes e758f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc3250b6ee8c070ed53fa9c7f03ae2e0"></a>

### [`00abd614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd614.md) → [`00abd810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abd/00abd810.md) FUN_00abd810

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 1件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md)
- 新版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 1件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 69.57% / 新版 69.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abd614"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abd614"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abd618"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00abd614",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00abd618",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00abd664",
      "READ",
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
      "00abd810",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00abd814",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00abd860",
      "READ",
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

- 旧版 [`00abd614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd614.md#insn-00abd614) · [`00abd618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd614.md#insn-00abd618) · [`00abd660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd614.md#insn-00abd660)

~~~diff
- 00abd614 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00abd614 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00abd614 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00abd614 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00abd614 bytes fd7bbea9
- 00abd618 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00abd618 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00abd618 bytes f30b00f9
- 00abd660 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:48:8"]]
- 00abd660 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00abd660 bytes 682600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06e8b34d2f1dc272c1de9568f264d988"></a>

### [`00abd670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd670.md) → [`00abd86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abd/00abd86c.md) FUN_00abd86c

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0086a1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a1ac.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0086a1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a1ec.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 78.12% / 新版 78.12%

CFGの説明率　旧版 15.38% / 新版 15.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abd670"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abd670"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00abd674"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00abd670",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00abd674",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00abd678",
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
      "00abd86c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00abd870",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00abd874",
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

- 旧版 [`00abd670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd670.md#insn-00abd670) · [`00abd674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd670.md#insn-00abd674) · [`00abd678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd670.md#insn-00abd678)

~~~diff
- 00abd670 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00abd670 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00abd670 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00abd670 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00abd670 bytes fd7bbda9
- 00abd674 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00abd674 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00abd674 bytes f50b00f9
- 00abd678 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00abd678 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00abd678 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00abd678 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00abd678 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c09452b84f4b5c575b38f02775c05212"></a>

### [`00abe1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe1c8.md) → [`00abe3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abe/00abe3c4.md) FUN_00abe3c4

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`006144ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00614/006144ec.md) [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md)
- 新版 呼出元 8件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0061452c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00614/0061452c.md) [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00aa3e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa3/00aa3e24.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 85.19% / 新版 85.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00abe20c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00abe274"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00abe408"
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
      "unmatched:00abe20c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abe5fc"
      ]
    ],
    [
      "unmatched:00abe274",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abe438"
      ]
    ]
  ],
  "added": [
    [
      "00abe408",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abe5fc"
      ]
    ],
    [
      "00abe470",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abe438"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00abe20c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe1c8.md#insn-00abe20c) · [`00abe274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe1c8.md#insn-00abe274)
- 新版 `00abe408`（命令位置の公開資料なし）

~~~diff
- 00abe20c ["CBRANCH", null, ["local:b33:8", "register:101:1"]]
- 00abe20c bytes a00f0054
- 00abe274 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00abe274 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00abe274 bytes 41feff54
+ 00abe408 ["CBRANCH", null, ["local:b33:8", "register:101:1"]]
+ 00abe408 bytes a00f0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de8c1428dbba49b50eeaa266edabcb5b"></a>

### [`00ac0de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0de8.md) → [`00ac0fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac0/00ac0fe4.md) FUN_00ac0fe4

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00abd6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd6f0.md) [`00abe1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe1c8.md) [`00abe5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe5fc.md) [`00abf8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abf/00abf8ac.md) [`00ac1b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1b44.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 5件 [`00abd8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abd/00abd8ec.md) [`00abe3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abe/00abe3c4.md) [`00abe7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abe/00abe7f8.md) [`00abfaa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abf/00abfaa8.md) [`00ac1d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac1/00ac1d40.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac0de8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac0de8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ac0fe4"
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
      "unmatched:00ac0de8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac0df4",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ac0df8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00442930"
      ]
    ]
  ],
  "added": [
    [
      "00ac0fe4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ac0ff0",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ],
    [
      "00ac0ff4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00442930"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac0de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0de8.md#insn-00ac0de8) · [`00ac0df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0de8.md#insn-00ac0df8)
- 新版 `00ac0fe4`（命令位置の公開資料なし）

~~~diff
- 00ac0de8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ac0de8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ac0de8 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00ac0de8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ac0de8 bytes fd7bbfa9
- 00ac0df8 ["INT_ADD", "register:40f0:8", ["const:ac0df8:8", "const:4:8"]]
- 00ac0df8 ["CALL", null, ["callee:00442930:8"]]
- 00ac0df8 bytes be06e697
+ 00ac0fe4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00ac0fe4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00ac0fe4 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00ac0fe4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00ac0fe4 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb6953ba191759b32124660bd52170c2"></a>

### [`00ac0e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0e10.md) → [`00ac100c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac1/00ac100c.md) FUN_00ac100c

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00abd6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd6f0.md) [`00ac0e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0e10.md) [`00ac118c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac118c.md) · 呼出先 3件 [`00ac0e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0e10.md) [`00ac118c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac118c.md) [`00ac1464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1464.md)
- 新版 呼出元 3件 [`00abd8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abd/00abd8ec.md) [`00ac100c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac1/00ac100c.md) [`00ac1388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac1/00ac1388.md) · 呼出先 3件 [`00ac100c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac1/00ac100c.md) [`00ac1388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac1/00ac1388.md) [`00ac1660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac1/00ac1660.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.83% / 新版 92.83%

CFGの説明率　旧版 59.74% / 新版 60.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac0e10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac0e10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac0e14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac0e10",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac0e14",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac0e18",
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
      "00ac100c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00ac1010",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00ac1014",
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

- 旧版 [`00ac0e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0e10.md#insn-00ac0e10) · [`00ac0e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0e10.md#insn-00ac0e14) · [`00ac0e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0e10.md#insn-00ac0e18)

~~~diff
- 00ac0e10 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ac0e10 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ac0e10 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00ac0e10 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ac0e10 bytes fd7bbba9
- 00ac0e14 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00ac0e14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00ac0e14 bytes f90b00f9
- 00ac0e18 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ac0e18 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ac0e18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ac0e18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac0e18 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74b5145a1f9519271cb7caea4074020a"></a>

### [`00ac118c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac118c.md) → [`00ac1388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac1/00ac1388.md) FUN_00ac1388

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ac0e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0e10.md) · 呼出先 1件 [`00ac0e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0e10.md)
- 新版 呼出元 1件 [`00ac100c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac1/00ac100c.md) · 呼出先 1件 [`00ac100c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac1/00ac100c.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 92.31% / 新版 92.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac11d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ac13d0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac11cc"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ac11cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac118c.md#insn-00ac11cc) · [`00ac11d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac118c.md#insn-00ac11d0) · [`00ac11d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac118c.md#insn-00ac11d4)

~~~diff
- 00ac11cc ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00ac11cc ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00ac11cc ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00ac11cc ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00ac11cc bytes 08b1899a
- 00ac11d0 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00ac11d0 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00ac11d0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00ac11d0 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 00ac11d0 bytes 00b0819a
- 00ac11d4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ac11d4 ["COPY", "tmp:1:8", ["register:4018:8"]]
- 00ac11d4 ["INT_ADD", "register:4018:8", ["register:4018:8", "const:8:8"]]
- 00ac11d4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ac11d4 bytes 688400f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8916fd5de652e6415eff75dad7a36c5a"></a>

### [`00ac1aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1aec.md) → [`00ac1ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac1/00ac1ce8.md) FUN_00ac1ce8

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac1b10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ac1d0c"
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
      "unmatched:00ac1b10",
      "DATA",
      [
        "storage",
        "00c8cf20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac1d0c",
      "DATA",
      [
        "storage",
        "00c8d320",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac1b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1aec.md#insn-00ac1b10) · [`00ac1b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1aec.md#insn-00ac1b00)
- 新版 `00ac1d0c`（命令位置の公開資料なし） · `00ac1cfc`（命令位置の公開資料なし）

~~~diff
- 00ac1b10 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00ac1b10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ac1b10 bytes 080000f9
+ 00ac1d0c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00ac1d0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00ac1d0c bytes 080000f9
- 00ac1b00 ["INT_ADD", "register:40f0:8", ["const:ac1b00:8", "const:4:8"]]
- 00ac1b00 ["CALL", null, ["callee:00c57e90:8"]]
+ 00ac1cfc ["INT_ADD", "register:40f0:8", ["const:ac1cfc:8", "const:4:8"]]
+ 00ac1cfc ["CALL", null, ["callee:00c57e90:8"]]
- 00ac1b00 bytes e4570694
+ 00ac1cfc bytes 65580694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-236c8eb06fcb126818a77372cfd57500"></a>

### [`00ac1b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1b24.md) → [`00ac1d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac1/00ac1d20.md) FUN_00ac1d20

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00ac1b2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac1b34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ac1d28"
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
      "unmatched:00ac1b2c",
      "DATA",
      [
        "storage",
        "00c8cf20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac1d28",
      "DATA",
      [
        "storage",
        "00c8d320",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac1b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1b24.md#insn-00ac1b2c) · [`00ac1b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1b24.md#insn-00ac1b34) · [`00ac1b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1b24.md#insn-00ac1b38)

~~~diff
- 00ac1b2c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00ac1b2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ac1b2c bytes 280000f9
- 00ac1b34 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 00ac1b34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00ac1b34 bytes 2080803c
- 00ac1b38 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ac1b38 ["RETURN", null, ["register:0:8"]]
- 00ac1b38 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfd3102e59dbce5881dcb3e0dc0d16c5"></a>

### [`00ac2f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2f54.md) → [`00ac3150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac3150.md) FUN_00ac3150

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00ac2ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2ddc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00ac2fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac2/00ac2fd8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac2f54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac2f54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac2f58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac2f54",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac2f58",
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
      "00ac3150",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ac3154",
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

- 旧版 [`00ac2f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2f54.md#insn-00ac2f54) · [`00ac2f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2f54.md#insn-00ac2f58)
- 新版 `00ac3150`（命令位置の公開資料なし）

~~~diff
- 00ac2f54 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ac2f54 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ac2f54 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ac2f54 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ac2f54 bytes fd7bbea9
- 00ac2f58 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00ac2f58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00ac2f58 bytes f30b00f9
+ 00ac3150 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00ac3150 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00ac3150 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00ac3150 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00ac3150 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc2d15fc61ba28909a428af859202606"></a>

### [`00ac2f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2f7c.md) → [`00ac3178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac3178.md) FUN_00ac3178

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00ac2fa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac2fa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ac319c"
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
      "unmatched:00ac2fa0",
      "DATA",
      [
        "storage",
        "00c8d040",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00ac2fa4",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac2fa8",
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
      "00ac319c",
      "DATA",
      [
        "storage",
        "00c8d440",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac31a0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ac31a4",
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

- 旧版 [`00ac2fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2f7c.md#insn-00ac2fa0) · [`00ac2fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2f7c.md#insn-00ac2fac)
- 新版 `00ac319c`（命令位置の公開資料なし）

~~~diff
- 00ac2fa0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ac2fa0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00ac2fa0 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00ac2fa0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac2fa0 bytes 082400a9
- 00ac2fac ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ac2fac ["RETURN", null, ["register:0:8"]]
- 00ac2fac bytes c0035fd6
+ 00ac319c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00ac319c ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00ac319c ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00ac319c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00ac319c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc8ebba3f7c1567c8592871c24c2058c"></a>

### [`00ac30a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac30a4.md) → [`00ac32a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac32a0.md) FUN_00ac32a0

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00ac30ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac30b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ac32a8"
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
      "unmatched:00ac30ac",
      "DATA",
      [
        "storage",
        "00c8d0c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac32a8",
      "DATA",
      [
        "storage",
        "00c8d4c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac30ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac30a4.md#insn-00ac30ac) · [`00ac30b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac30a4.md#insn-00ac30b4) · [`00ac30b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac30a4.md#insn-00ac30b8)

~~~diff
- 00ac30ac ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00ac30ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ac30ac bytes 280000f9
- 00ac30b4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 00ac30b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00ac30b4 bytes 2080803c
- 00ac30b8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ac30b8 ["RETURN", null, ["register:0:8"]]
- 00ac30b8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9074d5bdbdc85ec08fdc7a5ea1e6815"></a>

### [`00ac3270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3270.md) → [`00ac346c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac346c.md) FUN_00ac346c

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 46.15% / 新版 46.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac3274"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac3294"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac3294"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac3274",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac3294",
      "DATA",
      [
        "storage",
        "00c8d1b0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00ac3298",
      "READ",
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
      "00ac3470",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ac3490",
      "DATA",
      [
        "storage",
        "00c8d5b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac3494",
      "READ",
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

- 旧版 [`00ac3274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3270.md#insn-00ac3274) · [`00ac3294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3270.md#insn-00ac3294) · [`00ac32a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3270.md#insn-00ac32a0)

~~~diff
- 00ac3274 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00ac3274 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00ac3274 bytes f30b00f9
- 00ac3294 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ac3294 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00ac3294 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00ac3294 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac3294 bytes 082400a9
- 00ac32a0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ac32a0 ["RETURN", null, ["register:0:8"]]
- 00ac32a0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-956c62f46b4f1a29cc48339fa76debc4"></a>

### [`00ac894c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac894c.md) → [`00ac8b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac8b48.md) FUN_00ac8b48

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00788c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md) [`0082ede0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ede0.md) [`008caa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa24.md) [`00a7239c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a72/00a7239c.md) [`00ac0258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0258.md) · 呼出先 3件 [`0057c614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057c/0057c614.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 5件 [`00788cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788cac.md) [`0082ee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ee20.md) [`008cabc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008cabc0.md) [`00a72594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a72/00a72594.md) [`00ac0454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac0/00ac0454.md) · 呼出先 3件 [`0057c654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c654.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.55% / 新版 98.55%

CFGの説明率　旧版 70.59% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac8a34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ac8c30"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ac8a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac894c.md#insn-00ac8a34) · [`00ac89a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac894c.md#insn-00ac89a0)
- 新版 `00ac8c30`（命令位置の公開資料なし） · `00ac8b9c`（命令位置の公開資料なし）

~~~diff
- 00ac8a34 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ac8a34 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ac8a34 ["COPY", "tmp:2:8", ["register:4040:8"]]
- 00ac8a34 ["COPY", "tmp:3:8", ["tmp:2:8"]]
- 00ac8a34 bytes 1f682838
+ 00ac8c30 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ac8c30 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ac8c30 ["COPY", "tmp:2:8", ["register:4040:8"]]
+ 00ac8c30 ["COPY", "tmp:3:8", ["tmp:2:8"]]
+ 00ac8c30 bytes 1f682838
- 00ac89a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ac89a0 ["INT_ADD", "register:40f0:8", ["const:ac89a0:8", "const:4:8"]]
- 00ac89a0 ["CALLIND", null, ["register:0:8"]]
+ 00ac8b9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ac8b9c ["INT_ADD", "register:40f0:8", ["const:ac8b9c:8", "const:4:8"]]
+ 00ac8b9c ["CALLIND", null, ["register:0:8"]]
- 00ac89a0 bytes 00013fd6
+ 00ac8b9c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e245e51f9db73b2f448276ed93a97b9"></a>

### [`00ac8d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8d84.md) → [`00ac8f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac8f80.md) FUN_00ac8f80

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ac8c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8c60.md) [`00ac8ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8ee4.md) · 呼出先 6件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00859b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b0c.md) [`0085b274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b274.md) [`0085b27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b27c.md) [`0085b294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b294.md)
- 新版 呼出元 2件 [`00ac8e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac8e5c.md) [`00ac90e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac9/00ac90e0.md) · 呼出先 6件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00859b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b4c.md) [`0085b2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2b4.md) [`0085b2bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2bc.md) [`0085b2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2d4.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 83.54% / 新版 83.54%

CFGの説明率　旧版 17.14% / 新版 17.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac8de8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac8dec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac8e20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ac8fcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac900c"
      ]
    ],
    [
      "unmatched:00ac8dec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac90a4"
      ]
    ],
    [
      "unmatched:00ac8e10",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ]
  ],
  "added": [
    [
      "00ac8fcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac9034"
      ]
    ],
    [
      "00ac8fe8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac90a4"
      ]
    ],
    [
      "00ac9034",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac8de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8d84.md#insn-00ac8de8) · [`00ac8dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8d84.md#insn-00ac8dec) · [`00ac8e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8d84.md#insn-00ac8e10)

~~~diff
- 00ac8de8 ["COPY", "register:100:1", ["const:0:1"]]
- 00ac8de8 ["COPY", "register:101:1", ["const:0:1"]]
- 00ac8de8 ["COPY", "register:102:1", ["const:1:1"]]
- 00ac8de8 ["COPY", "register:103:1", ["const:1:1"]]
- 00ac8de8 bytes 2020201e
- 00ac8dec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00ac8dec ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00ac8dec ["CBRANCH", null, ["local:b20:8", "tmp:1:1"]]
- 00ac8dec bytes e8050054
- 00ac8e10 ["INT_ADD", "register:40f0:8", ["const:ac8e10:8", "const:4:8"]]
- 00ac8e10 ["CALL", null, ["callee:008514f8:8"]]
- 00ac8e10 bytes aa21f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8cb59443368f06812991250033c0a76"></a>

### [`00ac923c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac923c.md) → [`00ac9438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac9/00ac9438.md) FUN_00ac9438

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0073c8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073c/0073c8f8.md) [`00788c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md) · 呼出先 5件 [`00acae6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acae6c.md) [`00acb00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb00c.md) [`00acb010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb010.md) [`00acb044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb044.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`0073c938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073c/0073c938.md) [`00788cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788cac.md) · 呼出先 5件 [`00acb068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb068.md) [`00acb208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb208.md) [`00acb20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb20c.md) [`00acb240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb240.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.61% / 新版 81.61%

CFGの説明率　旧版 50.00% / 新版 48.39%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac9300"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac9304"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac9308"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ac94c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ac92d4"
      ]
    ],
    [
      "unmatched:00ac92c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac94e4"
      ]
    ],
    [
      "unmatched:00ac92d0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac94d8"
      ]
    ]
  ],
  "added": [
    [
      "00ac94c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac94d0"
      ]
    ],
    [
      "00ac94c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac94e4"
      ]
    ],
    [
      "00ac94cc",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac94d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac92c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac923c.md#insn-00ac92c8) · [`00ac9300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac923c.md#insn-00ac9300) · [`00ac9304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac923c.md#insn-00ac9304)

~~~diff
- 00ac92c8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00ac92c8 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00ac92c8 bytes 000100b4
- 00ac9300 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00ac9300 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ac9300 bytes e80300f9
- 00ac9304 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00ac9304 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00ac9304 bytes e91300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67a2f78de8dd2cc87166e3010c61b31b"></a>

### [`00acea58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acea58.md) → [`00acec54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ace/00acec54.md) FUN_00acec54

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 11件 [`006623ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/006623ac.md) [`00662450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662450.md) [`006624f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/006624f4.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007de880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007de/007de880.md) · 呼出先 7件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) [`00aea9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea9c8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 11件 [`006623ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/006623ec.md) [`00662490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662490.md) [`00662534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662534.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007de8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007de/007de8c0.md) · 呼出先 7件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00aeadf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aea/00aeadf0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.35% / 新版 88.35%

CFGの説明率　旧版 61.90% / 新版 61.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acea68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acea68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acea8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00acea68",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00acea8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00acea90",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008026b8"
      ]
    ]
  ],
  "added": [
    [
      "00acec64",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00acec88",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00acec8c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008026b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acea68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acea58.md#insn-00acea68) · [`00acea8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acea58.md#insn-00acea8c) · [`00acea90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acea58.md#insn-00acea90)

~~~diff
- 00acea68 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00acea68 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00acea68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00acea68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00acea68 bytes f85f06a9
- 00acea8c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00acea8c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00acea8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00acea8c bytes a8831ff8
- 00acea90 ["INT_ADD", "register:40f0:8", ["const:acea90:8", "const:4:8"]]
- 00acea90 ["CALL", null, ["callee:008026b8:8"]]
- 00acea90 bytes facef497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5d2866cfd983b3b36f5a99608f100f2"></a>

### [`00ad6824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6824.md) → [`00ad6a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6a20.md) FUN_00ad6a20

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) · 呼出先 4件 [`00664e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664e00.md) [`009df498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df498.md) [`009e0e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0e24.md) [`009e2df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e2df8.md)
- 新版 呼出元 1件 [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) · 呼出先 4件 [`00664e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664e40.md) [`009df634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df634.md) [`009e0fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0fc0.md) [`009e2f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2f94.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad6828"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad6828"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ad6a24"
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
      "unmatched:00ad6828",
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
      "00ad6a24",
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

- 旧版 [`00ad6828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6824.md#insn-00ad6828) · [`00ad6844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6824.md#insn-00ad6844)
- 新版 `00ad6a40`（命令位置の公開資料なし） · `00ad6a24`（命令位置の公開資料なし）

~~~diff
- 00ad6828 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ad6828 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ad6828 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ad6828 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ad6828 bytes f44f01a9
- 00ad6844 ["INT_ADD", "register:40f0:8", ["const:ad6844:8", "const:4:8"]]
- 00ad6844 ["CALL", null, ["callee:009e0fc0:8"]]
+ 00ad6a40 ["INT_ADD", "register:40f0:8", ["const:ad6a40:8", "const:4:8"]]
+ 00ad6a40 ["CALL", null, ["callee:009e0fc0:8"]]
- 00ad6844 bytes 7829fc97
+ 00ad6a40 bytes 6029fc97
+ 00ad6a24 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00ad6a24 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00ad6a24 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
+ 00ad6a24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00ad6a24 bytes f44f01a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db05c9bf3409475bab88582944930599"></a>

### [`00aec12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec12c.md) → [`00aec554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aec/00aec554.md) FUN_00aec554

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00aec12c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec12c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec130"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aec12c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aec130",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aec150",
      "DATA",
      [
        "storage",
        "00c8d578",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aec554",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aec558",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aec578",
      "DATA",
      [
        "storage",
        "00c8d978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec12c.md#insn-00aec12c) · [`00aec130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec12c.md#insn-00aec130) · [`00aec150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec12c.md#insn-00aec150)

~~~diff
- 00aec12c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aec12c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aec12c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00aec12c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aec12c bytes fd7bbea9
- 00aec130 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aec130 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00aec130 bytes f30b00f9
- 00aec150 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aec150 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00aec150 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00aec150 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aec150 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90c37a59beae55f6824d0c99d09506c8"></a>

### [`00aecf44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf44.md) → [`00aed36c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aed36c.md) FUN_00aed36c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00aecf68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aecf68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aed390"
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
      "unmatched:00aecf68",
      "DATA",
      [
        "storage",
        "00c8d678",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00aecf6c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aecf70",
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
      "00aed390",
      "DATA",
      [
        "storage",
        "00c8da78",
        null,
        "undefined *"
      ]
    ],
    [
      "00aed394",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aed398",
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

- 旧版 [`00aecf68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf44.md#insn-00aecf68) · [`00aecf74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aecf44.md#insn-00aecf74)
- 新版 `00aed390`（命令位置の公開資料なし）

~~~diff
- 00aecf68 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aecf68 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00aecf68 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00aecf68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aecf68 bytes 082400a9
- 00aecf74 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aecf74 ["RETURN", null, ["register:0:8"]]
- 00aecf74 bytes c0035fd6
+ 00aed390 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00aed390 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00aed390 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00aed390 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00aed390 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7da365087f5a730586a37186f448978"></a>

### [`00aed4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4d8.md) → [`00aed900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aed900.md) FUN_00aed900

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00aed4fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed4fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aed924"
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
      "unmatched:00aed4fc",
      "DATA",
      [
        "storage",
        "00c8d7f8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00aed500",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aed504",
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
      "00aed924",
      "DATA",
      [
        "storage",
        "00c8dbf8",
        null,
        "undefined *"
      ]
    ],
    [
      "00aed928",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aed92c",
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

- 旧版 [`00aed4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4d8.md#insn-00aed4fc) · [`00aed508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed4d8.md#insn-00aed508)
- 新版 `00aed924`（命令位置の公開資料なし）

~~~diff
- 00aed4fc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aed4fc ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00aed4fc ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00aed4fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aed4fc bytes 082400a9
- 00aed508 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aed508 ["RETURN", null, ["register:0:8"]]
- 00aed508 bytes c0035fd6
+ 00aed924 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00aed924 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00aed924 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00aed924 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00aed924 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75a4c519ee28bfe63e12e0fe1342662d"></a>

### [`00aed968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed968.md) → [`00aedd90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aedd90.md) FUN_00aedd90

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

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
      "site": "00aed98c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed98c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aeddb4"
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
      "unmatched:00aed98c",
      "DATA",
      [
        "storage",
        "00c8d868",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aeddb4",
      "DATA",
      [
        "storage",
        "00c8dc68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed98c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed968.md#insn-00aed98c) · [`00aed970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed968.md#insn-00aed970)
- 新版 `00aeddb4`（命令位置の公開資料なし）

~~~diff
- 00aed98c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aed98c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00aed98c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00aed98c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aed98c bytes 082400a9
+ 00aeddb4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00aeddb4 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00aeddb4 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00aeddb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00aeddb4 bytes 082400a9
- 00aed970 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00aed970 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d085bcbd1e0c2f1aac47f2ff04b7e53a"></a>

### [`00aed99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed99c.md) → [`00aeddc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aeddc4.md) FUN_00aeddc4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00aed9a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed9a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aeddd0"
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
      "unmatched:00aed9a8",
      "DATA",
      [
        "storage",
        "00c8d868",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aeddd0",
      "DATA",
      [
        "storage",
        "00c8dc68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed99c.md#insn-00aed9a8) · [`00aed9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed99c.md#insn-00aed9ac)
- 新版 `00aeddd0`（命令位置の公開資料なし）

~~~diff
- 00aed9a8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aed9a8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00aed9a8 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00aed9a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aed9a8 bytes 292000a9
- 00aed9ac ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aed9ac ["RETURN", null, ["register:0:8"]]
- 00aed9ac bytes c0035fd6
+ 00aeddd0 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00aeddd0 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00aeddd0 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00aeddd0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00aeddd0 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e1dcf6772b4fbf12df9a6f3c94c7216"></a>

### [`00aee424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee424.md) → [`00aee84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aee84c.md) FUN_00aee84c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00aee430"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee430"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aee858"
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
      "unmatched:00aee430",
      "DATA",
      [
        "storage",
        "00c8d8d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aee858",
      "DATA",
      [
        "storage",
        "00c8dcd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee424.md#insn-00aee430) · [`00aee434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee424.md#insn-00aee434)
- 新版 `00aee858`（命令位置の公開資料なし）

~~~diff
- 00aee430 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aee430 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00aee430 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00aee430 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aee430 bytes 292000a9
- 00aee434 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aee434 ["RETURN", null, ["register:0:8"]]
- 00aee434 bytes c0035fd6
+ 00aee858 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00aee858 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00aee858 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00aee858 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00aee858 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ce5d3985313db0956895c00ecb1bf74"></a>

### [`00aee6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee6d0.md) → [`00aeeaf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aeeaf8.md) FUN_00aeeaf8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee6d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee6d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee6e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aee6d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aee6dc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "unmatched:00aee6e8",
      "DATA",
      [
        "storage",
        "00c8d9d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aeeaf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aeeb04",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "00aeeb10",
      "DATA",
      [
        "storage",
        "00c8ddd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee6d0.md#insn-00aee6d0) · [`00aee6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee6d0.md#insn-00aee6dc) · [`00aee6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee6d0.md#insn-00aee6e8)

~~~diff
- 00aee6d0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aee6d0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aee6d0 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00aee6d0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aee6d0 bytes fd7bbfa9
- 00aee6dc ["INT_ADD", "register:40f0:8", ["const:aee6dc:8", "const:4:8"]]
- 00aee6dc ["CALL", null, ["callee:00c57e90:8"]]
- 00aee6dc bytes eda40594
- 00aee6e8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00aee6e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00aee6e8 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18e384e4bb63570843a36bd43f7d350d"></a>

### [`00aee778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee778.md) → [`00aeeba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aeeba0.md) FUN_00aeeba0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00aee778"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee778"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee77c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aee778",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aee77c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aee79c",
      "DATA",
      [
        "storage",
        "00c8da68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aeeba0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aeeba4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aeebc4",
      "DATA",
      [
        "storage",
        "00c8de68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee778.md#insn-00aee778) · [`00aee77c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee778.md#insn-00aee77c) · [`00aee79c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee778.md#insn-00aee79c)

~~~diff
- 00aee778 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aee778 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aee778 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00aee778 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aee778 bytes fd7bbea9
- 00aee77c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aee77c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00aee77c bytes f30b00f9
- 00aee79c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aee79c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00aee79c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00aee79c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aee79c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f814d337a63b2eb1b5ce727a8939eca"></a>

### [`00aeec40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeec40.md) → [`00aef068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aef068.md) FUN_00aef068

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 64.29% / 新版 64.29%

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
      "site": "00aeec40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeec40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeec44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeec40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeec44",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeec64",
      "DATA",
      [
        "storage",
        "00c8db68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aef068",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aef06c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aef08c",
      "DATA",
      [
        "storage",
        "00c8df68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeec40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeec40.md#insn-00aeec40) · [`00aeec44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeec40.md#insn-00aeec44) · [`00aeec64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeec40.md#insn-00aeec64)

~~~diff
- 00aeec40 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aeec40 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aeec40 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00aeec40 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aeec40 bytes fd7bbea9
- 00aeec44 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aeec44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00aeec44 bytes f30b00f9
- 00aeec64 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00aeec64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00aeec64 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-228b57c8acff6cad79b98b987ef9d3ba"></a>

### [`00aeec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeec78.md) → [`00aef0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aef0a0.md) FUN_00aef0a0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 33.33% / 新版 33.33%

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
      "site": "00aeec80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeec88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aef0a8"
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
      "unmatched:00aeec80",
      "DATA",
      [
        "storage",
        "00c8db68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aef0a8",
      "DATA",
      [
        "storage",
        "00c8df68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeec80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeec78.md#insn-00aeec80) · [`00aeec88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeec78.md#insn-00aeec88)
- 新版 `00aef0a8`（命令位置の公開資料なし）

~~~diff
- 00aeec80 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00aeec80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00aeec80 bytes 280000f9
- 00aeec88 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 00aeec88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00aeec88 bytes 2080803c
+ 00aef0a8 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00aef0a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00aef0a8 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd01232b0e581aa023b731ea70630eb8"></a>

### [`00aef454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef454.md) → [`00aef87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aef87c.md) FUN_00aef87c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00aef454"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef454"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef458"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aef454",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aef458",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aef478",
      "DATA",
      [
        "storage",
        "00c8dc68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aef87c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aef880",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aef8a0",
      "DATA",
      [
        "storage",
        "00c8e068",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aef454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef454.md#insn-00aef454) · [`00aef458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef454.md#insn-00aef458) · [`00aef478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef454.md#insn-00aef478)

~~~diff
- 00aef454 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aef454 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aef454 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00aef454 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aef454 bytes fd7bbea9
- 00aef458 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aef458 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00aef458 bytes f30b00f9
- 00aef478 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aef478 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00aef478 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00aef478 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aef478 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99e5502ce1c6fc0ecd4f3ae40f0aab7c"></a>

### [`00aef488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef488.md) → [`00aef8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aef8b0.md) FUN_00aef8b0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00aef494"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef494"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aef8bc"
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
      "unmatched:00aef494",
      "DATA",
      [
        "storage",
        "00c8dc68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aef8bc",
      "DATA",
      [
        "storage",
        "00c8e068",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aef494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef488.md#insn-00aef494) · [`00aef498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef488.md#insn-00aef498)
- 新版 `00aef8bc`（命令位置の公開資料なし）

~~~diff
- 00aef494 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aef494 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00aef494 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00aef494 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aef494 bytes 292000a9
- 00aef498 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aef498 ["RETURN", null, ["register:0:8"]]
- 00aef498 bytes c0035fd6
+ 00aef8bc ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00aef8bc ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00aef8bc ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00aef8bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00aef8bc bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6f5b4c11d244bbac56f97aaa0d98327"></a>

### [`00aef660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef660.md) → [`00aefa88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aefa88.md) FUN_00aefa88

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00aef684"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef684"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aefaac"
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
      "unmatched:00aef684",
      "DATA",
      [
        "storage",
        "00c8dd68",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00aef688",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aef68c",
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
      "00aefaac",
      "DATA",
      [
        "storage",
        "00c8e168",
        null,
        "undefined *"
      ]
    ],
    [
      "00aefab0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aefab4",
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

- 旧版 [`00aef684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef660.md#insn-00aef684) · [`00aef690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef660.md#insn-00aef690)
- 新版 `00aefaac`（命令位置の公開資料なし）

~~~diff
- 00aef684 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aef684 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00aef684 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00aef684 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aef684 bytes 082400a9
- 00aef690 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aef690 ["RETURN", null, ["register:0:8"]]
- 00aef690 bytes c0035fd6
+ 00aefaac ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00aefaac ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00aefaac ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00aefaac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00aefaac bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e93f5218212eb2b4fe2acb767f65028"></a>

### [`00aef694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef694.md) → [`00aefabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aefabc.md) FUN_00aefabc

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00aef6a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef6a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aefac8"
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
      "unmatched:00aef6a0",
      "DATA",
      [
        "storage",
        "00c8dd68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aefac8",
      "DATA",
      [
        "storage",
        "00c8e168",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aef6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef694.md#insn-00aef6a0) · [`00aef6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef694.md#insn-00aef6a4)
- 新版 `00aefac8`（命令位置の公開資料なし）

~~~diff
- 00aef6a0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aef6a0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00aef6a0 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00aef6a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aef6a0 bytes 292000a9
- 00aef6a4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aef6a4 ["RETURN", null, ["register:0:8"]]
- 00aef6a4 bytes c0035fd6
+ 00aefac8 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00aefac8 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00aefac8 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00aefac8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00aefac8 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e4dd754850f0409fead1d1d398c1a3c"></a>

### [`00aefa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefa24.md) → [`00aefe4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aefe4c.md) FUN_00aefe4c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00aefa2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aefa34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aefe54"
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
      "unmatched:00aefa2c",
      "DATA",
      [
        "storage",
        "00c8dde8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aefe54",
      "DATA",
      [
        "storage",
        "00c8e1e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aefa2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefa24.md#insn-00aefa2c) · [`00aefa34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefa24.md#insn-00aefa34) · [`00aefa38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefa24.md#insn-00aefa38)

~~~diff
- 00aefa2c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00aefa2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00aefa2c bytes 280000f9
- 00aefa34 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 00aefa34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00aefa34 bytes 2080803c
- 00aefa38 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aefa38 ["RETURN", null, ["register:0:8"]]
- 00aefa38 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfd2de3c9290db6e115ee78be696caea"></a>

### [`00aefb58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefb58.md) → [`00aeff80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aeff80.md) FUN_00aeff80

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

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
      "site": "00aefb7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aefb80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aeffa4"
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
      "unmatched:00aefb7c",
      "DATA",
      [
        "storage",
        "00c8de78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aeffa4",
      "DATA",
      [
        "storage",
        "00c8e278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aefb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefb58.md#insn-00aefb7c) · [`00aefb80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefb58.md#insn-00aefb80)
- 新版 `00aeffa4`（命令位置の公開資料なし）

~~~diff
- 00aefb7c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00aefb7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00aefb7c bytes 080000f9
- 00aefb80 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00aefb80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00aefb80 bytes 0080803c
+ 00aeffa4 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00aeffa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00aeffa4 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dea9d50ba9138cec4a0c2b4e93157e4"></a>

### [`00af01bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af01bc.md) → [`00af05e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af05e4.md) FUN_00af05e4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00af01c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af05ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00af01c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af01c4",
      "DATA",
      [
        "storage",
        "00c8df68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af05ec",
      "DATA",
      [
        "storage",
        "00c8e368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af01c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af01bc.md#insn-00af01c4) · [`00af01c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af01bc.md#insn-00af01c8)
- 新版 `00af05ec`（命令位置の公開資料なし）

~~~diff
- 00af01c4 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00af01c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00af01c4 bytes 280000f9
- 00af01c8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af01c8 ["RETURN", null, ["register:0:8"]]
- 00af01c8 bytes c0035fd6
+ 00af05ec ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00af05ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00af05ec bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7df3661d37d9e3d55119daa279c9ff9"></a>

### [`00af01d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af01d4.md) → [`00af05fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af05fc.md) FUN_00af05fc

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af01f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00af0620"
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
      "unmatched:00af01f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00af0620",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af01f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af01d4.md#insn-00af01f8) · [`00af01f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af01d4.md#insn-00af01f0)
- 新版 `00af0620`（命令位置の公開資料なし）

~~~diff
- 00af01f8 ["INT_ADD", "register:40f0:8", ["const:af01f8:8", "const:4:8"]]
- 00af01f8 ["CALL", null, ["ram:47acb4:8"]]
- 00af01f8 bytes af2ae697
+ 00af0620 ["INT_ADD", "register:40f0:8", ["const:af0620:8", "const:4:8"]]
+ 00af0620 ["CALL", null, ["ram:47acf4:8"]]
+ 00af0620 bytes b529e697
- 00af01f0 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00af01f0 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-013ecd41cff4c7d6af1073fffcd3fa96"></a>

### [`00af0248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0248.md) → [`00af0670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0670.md) FUN_00af0670

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

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
      "site": "00af026c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af026c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af0694"
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
      "unmatched:00af026c",
      "DATA",
      [
        "storage",
        "00c8dfe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af0694",
      "DATA",
      [
        "storage",
        "00c8e3e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af026c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0248.md#insn-00af026c) · [`00af025c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0248.md#insn-00af025c)
- 新版 `00af0694`（命令位置の公開資料なし） · `00af0684`（命令位置の公開資料なし）

~~~diff
- 00af026c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00af026c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af026c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00af026c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af026c bytes 082400a9
+ 00af0694 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00af0694 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00af0694 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00af0694 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00af0694 bytes 082400a9
- 00af025c ["INT_ADD", "register:40f0:8", ["const:af025c:8", "const:4:8"]]
- 00af025c ["CALL", null, ["callee:00c57e90:8"]]
+ 00af0684 ["INT_ADD", "register:40f0:8", ["const:af0684:8", "const:4:8"]]
+ 00af0684 ["CALL", null, ["callee:00c57e90:8"]]
- 00af025c bytes 0d9e0594
+ 00af0684 bytes 039e0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6e9a36d44817f4a99f3e3f32c839862"></a>

### [`00af027c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af027c.md) → [`00af06a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af06a4.md) FUN_00af06a4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00af0288"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0288"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af06b0"
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
      "unmatched:00af0288",
      "DATA",
      [
        "storage",
        "00c8dfe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af06b0",
      "DATA",
      [
        "storage",
        "00c8e3e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af027c.md#insn-00af0288) · [`00af028c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af027c.md#insn-00af028c)
- 新版 `00af06b0`（命令位置の公開資料なし）

~~~diff
- 00af0288 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00af0288 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00af0288 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00af0288 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af0288 bytes 292000a9
- 00af028c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af028c ["RETURN", null, ["register:0:8"]]
- 00af028c bytes c0035fd6
+ 00af06b0 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00af06b0 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00af06b0 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00af06b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00af06b0 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bda3d47285edf4680d5e736eac3728d"></a>

### [`00af0388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0388.md) → [`00af07b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af07b0.md) FUN_00af07b0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_argument_candidate, call_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af03a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af07cc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af03b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af03a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af03b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00af07cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af07d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af03a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0388.md#insn-00af03a4) · [`00af03b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0388.md#insn-00af03b0) · [`00af03bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0388.md#insn-00af03bc)
- 新版 `00af07e4`（命令位置の公開資料なし）

~~~diff
- 00af03a4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af03a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00af03a4 bytes f30b00f9
- 00af03b0 ["INT_ADD", "register:40f0:8", ["const:af03b0:8", "const:4:8"]]
- 00af03b0 ["CALL", null, ["ram:47acb4:8"]]
- 00af03b0 bytes 412ae697
- 00af03bc ["INT_ADD", "register:40f0:8", ["const:af03bc:8", "const:4:8"]]
- 00af03bc ["CALL", null, ["callee:0047cdd4:8"]]
+ 00af07e4 ["INT_ADD", "register:40f0:8", ["const:af07e4:8", "const:4:8"]]
+ 00af07e4 ["CALL", null, ["callee:0047cdd4:8"]]
- 00af03bc bytes 7632e697
+ 00af07e4 bytes 7c31e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

