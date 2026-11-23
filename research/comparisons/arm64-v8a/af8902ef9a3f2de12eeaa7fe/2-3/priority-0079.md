# v16.0.0 → v16.0.1 · 最優先の変更候補 (79)

[一覧の目次](README.md)

<a id="compare-fee4d2b407df73ce2bae2766dea113be"></a>

### [`00bb4e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb4/00bb4e24.md) → [`00bb524c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb524c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5tellgEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c593e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c593e0.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c58af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58af0.md)
- 新版 呼出元 1件 [`00c597e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c597e0.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c58ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ef0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.40% / 新版 81.40%

CFGの説明率　旧版 6.67% / 新版 6.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb4e24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb4e24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb4e28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb4e24",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb4e28",
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
      "00bb524c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb5250",
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

- 旧版 [`00bb4e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb4/00bb4e24.md#insn-00bb4e24) · [`00bb4e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb4/00bb4e24.md#insn-00bb4e28) · [`00bb4e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb4/00bb4e24.md#insn-00bb4e4c)
- 新版 `00bb5274`（命令位置の公開資料なし）

~~~diff
- 00bb4e24 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb4e24 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb4e24 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb4e24 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb4e24 bytes f44fbea9
- 00bb4e28 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb4e28 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb4e28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb4e28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb4e28 bytes fd7b01a9
- 00bb4e4c ["INT_ADD", "register:40f0:8", ["const:bb4e4c:8", "const:4:8"]]
- 00bb4e4c ["CALL", null, ["callee:00c582a0:8"]]
+ 00bb5274 ["INT_ADD", "register:40f0:8", ["const:bb5274:8", "const:4:8"]]
+ 00bb5274 ["CALL", null, ["callee:00c582a0:8"]]
- 00bb4e4c bytes 158c0294
+ 00bb5274 bytes 0b8c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-009bae051f0782fff41faf19f2c3e083"></a>

### [`00bb4ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb4/00bb4ed0.md) → [`00bb52f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb52f8.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5cdc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdc0.md) · 呼出先 3件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c58af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58af0.md) [`00c5ccf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccf0.md)
- 新版 呼出元 1件 [`00c5d1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1c0.md) · 呼出先 3件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c58ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ef0.md) [`00c5d0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0f0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.99% / 新版 88.99%

CFGの説明率　旧版 41.18% / 新版 44.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb4ed0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb4ed0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb4ed4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb4ed0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb4ed4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb4ed8",
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
      "00bb52f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bb52fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb5300",
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

- 旧版 [`00bb4ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb4/00bb4ed0.md#insn-00bb4ed0) · [`00bb4ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb4/00bb4ed0.md#insn-00bb4ed4) · [`00bb4ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb4/00bb4ed0.md#insn-00bb4ed8)

~~~diff
- 00bb4ed0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bb4ed0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bb4ed0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bb4ed0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb4ed0 bytes f657bda9
- 00bb4ed4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb4ed4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb4ed4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb4ed4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb4ed4 bytes f44f01a9
- 00bb4ed8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb4ed8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb4ed8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bb4ed8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb4ed8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ebb87deca89e120abcfa17022abc973"></a>

### [`00bb50c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb50c0.md) → [`00bb54e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb54e8.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEEC2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5cda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cda0.md) · 呼出先 7件 [`00bb5598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5598.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3a0.md)
- 新版 呼出元 1件 [`00c5d1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1a0.md) · 呼出先 7件 [`00bb59c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb59c0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7a0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 69.01% / 新版 69.01%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb50c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb50c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb50c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb50c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb50c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb50cc",
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
      "00bb54ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bb54f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb54f4",
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

- 旧版 [`00bb50c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb50c0.md#insn-00bb50c4) · [`00bb50c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb50c0.md#insn-00bb50c8) · [`00bb50cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb50c0.md#insn-00bb50cc)

~~~diff
- 00bb50c4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bb50c4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bb50c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb50c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb50c4 bytes f65701a9
- 00bb50c8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb50c8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb50c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bb50c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb50c8 bytes f44f02a9
- 00bb50cc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb50cc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb50cc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bb50cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb50cc bytes fd7b03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56017f09bf3fb4abbaac5b5250dcb3ba"></a>

### [`00bb534c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb534c.md) → [`00bb5774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5774.md) FUN_00bb5774

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md) [`00c5cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md) [`00c5d1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb57a0",
      "incomplete_value": true,
      "site": "00bb57a0",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb5378",
      "incomplete_value": true,
      "site": "00bb5378",
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
            "const:18:8"
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
      "definition_site": "00bb57a4",
      "incomplete_value": true,
      "site": "00bb57a4",
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
      "definition_site": "00bb537c",
      "incomplete_value": true,
      "site": "00bb537c",
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
      "00bb578c",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00bb57a0",
      "DATA",
      [
        "storage",
        "00c90ac0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb57a4",
      "DATA",
      [
        "storage",
        "00c90ae8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb578c",
      "READ",
      [
        "storage",
        "00c9b030",
        null,
        "pointer"
      ]
    ],
    [
      "00bb57a0",
      "DATA",
      [
        "storage",
        "00c90ec0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb57a4",
      "DATA",
      [
        "storage",
        "00c90ee8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb535c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb534c.md#insn-00bb535c) · [`00bb5364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb534c.md#insn-00bb5364) · [`00bb5380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb534c.md#insn-00bb5380)
- 新版 `00bb5784`（命令位置の公開資料なし） · `00bb578c`（命令位置の公開資料なし） · `00bb57a8`（命令位置の公開資料なし）

~~~diff
- 00bb535c ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00bb5784 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00bb535c bytes 290700b0
+ 00bb5784 bytes 290700d0
- 00bb5364 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c30:8"]]
- 00bb5364 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb578c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:30:8"]]
+ 00bb578c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb5364 bytes 291946f9
+ 00bb578c bytes 291940f9
- 00bb5380 ["INT_ADD", "register:40f0:8", ["const:bb5380:8", "const:4:8"]]
- 00bb5380 ["CALL", null, ["callee:00c5d1b0:8"]]
+ 00bb57a8 ["INT_ADD", "register:40f0:8", ["const:bb57a8:8", "const:4:8"]]
+ 00bb57a8 ["CALL", null, ["callee:00c5d1b0:8"]]
- 00bb5380 bytes 8c9e0294
+ 00bb57a8 bytes 829e0294
~~~


<a id="compare-6dc6daa42207313c320acc774a14b5fb"></a>

### [`00bb5394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5394.md) → [`00bb57bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb57bc.md) FUN_00bb57bc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md) [`00c5cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md) [`00c5d1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb57ec",
      "incomplete_value": true,
      "site": "00bb57ec",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb53c4",
      "incomplete_value": true,
      "site": "00bb53c4",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb57f0",
      "incomplete_value": true,
      "site": "00bb57f0",
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
      "definition_site": "00bb53c8",
      "incomplete_value": true,
      "site": "00bb53c8",
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
      "00bb57d4",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00bb57ec",
      "DATA",
      [
        "storage",
        "00c90ac0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb57f0",
      "DATA",
      [
        "storage",
        "00c90ae8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb57d4",
      "READ",
      [
        "storage",
        "00c9b030",
        null,
        "pointer"
      ]
    ],
    [
      "00bb57ec",
      "DATA",
      [
        "storage",
        "00c90ec0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb57f0",
      "DATA",
      [
        "storage",
        "00c90ee8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb53a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5394.md#insn-00bb53a4) · [`00bb53ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5394.md#insn-00bb53ac) · [`00bb53cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5394.md#insn-00bb53cc)
- 新版 `00bb57cc`（命令位置の公開資料なし） · `00bb57d4`（命令位置の公開資料なし） · `00bb57f4`（命令位置の公開資料なし）

~~~diff
- 00bb53a4 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00bb57cc ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00bb53a4 bytes 290700b0
+ 00bb57cc bytes 290700d0
- 00bb53ac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c30:8"]]
- 00bb53ac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb57d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:30:8"]]
+ 00bb57d4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb53ac bytes 291946f9
+ 00bb57d4 bytes 291940f9
- 00bb53cc ["INT_ADD", "register:40f0:8", ["const:bb53cc:8", "const:4:8"]]
- 00bb53cc ["CALL", null, ["callee:00c5d1b0:8"]]
+ 00bb57f4 ["INT_ADD", "register:40f0:8", ["const:bb57f4:8", "const:4:8"]]
+ 00bb57f4 ["CALL", null, ["callee:00c5d1b0:8"]]
- 00bb53cc bytes 799e0294
+ 00bb57f4 bytes 6f9e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e91e917dad2ad604609b3fba7f5abfa"></a>

### [`00bb53e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb53e8.md) → [`00bb5810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5810.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEED2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdb0.md) · 呼出先 5件 [`00bb5598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5598.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c59c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c00.md) [`00c5ba40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba40.md) [`00c5cd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd90.md)
- 新版 呼出元 1件 [`00c5d1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1b0.md) · 呼出先 5件 [`00bb59c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb59c0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a000.md) [`00c5be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be40.md) [`00c5d190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d190.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb582c",
      "incomplete_value": true,
      "site": "00bb5830",
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
      "definition_site": "00bb5404",
      "incomplete_value": true,
      "site": "00bb5408",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb5898",
      "incomplete_value": true,
      "site": "00bb5898",
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
      "definition_site": "00bb5470",
      "incomplete_value": true,
      "site": "00bb5470",
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
      "00bb5824",
      "READ",
      [
        "storage",
        "00c9b4f0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb5830",
      "DATA",
      [
        "storage",
        "00c90b70",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00bb5858",
      "READ",
      [
        "storage",
        "00c90b88",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00bb5824",
      "READ",
      [
        "storage",
        "00c9b8f0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb5830",
      "DATA",
      [
        "storage",
        "00c90f70",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00bb5858",
      "READ",
      [
        "storage",
        "00c90f88",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb53fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb53e8.md#insn-00bb53fc) · [`00bb5414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb53e8.md#insn-00bb5414) · [`00bb541c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb53e8.md#insn-00bb541c)
- 新版 `00bb5824`（命令位置の公開資料なし） · `00bb583c`（命令位置の公開資料なし） · `00bb5844`（命令位置の公開資料なし）

~~~diff
- 00bb53fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4f0:8"]]
- 00bb53fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb5824 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8f0:8"]]
+ 00bb5824 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb53fc bytes 087942f9
+ 00bb5824 bytes 087944f9
- 00bb5414 ["INT_ADD", "register:40f0:8", ["const:bb5414:8", "const:4:8"]]
- 00bb5414 ["CALL", null, ["callee:00c5d190:8"]]
+ 00bb583c ["INT_ADD", "register:40f0:8", ["const:bb583c:8", "const:4:8"]]
+ 00bb583c ["CALL", null, ["callee:00c5d190:8"]]
- 00bb5414 bytes 5f9e0294
+ 00bb583c bytes 559e0294
- 00bb541c ["INT_ADD", "register:40f0:8", ["const:bb541c:8", "const:4:8"]]
- 00bb541c ["CALL", null, ["callee:00c5a000:8"]]
+ 00bb5844 ["INT_ADD", "register:40f0:8", ["const:bb5844:8", "const:4:8"]]
+ 00bb5844 ["CALL", null, ["callee:00c5a000:8"]]
- 00bb541c bytes f9910294
+ 00bb5844 bytes ef910294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff4c196ded105c6f5ac37f2391650300"></a>

### [`00bb5690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5690.md) → [`00bb5ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5ab8.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE7seekoffExNS_8ios_base7seekdirEj

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb5ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5ec4.md) [`00c5cde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cde0.md) [`00c5cdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdf0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb62ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb62ec.md) [`00c5d1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1e0.md) [`00c5d1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 52.94% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5690"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5690"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5694"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb5690",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb5694",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb5698",
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
      "00bb5ab8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bb5abc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb5ac0",
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

- 旧版 [`00bb5690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5690.md#insn-00bb5690) · [`00bb5694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5690.md#insn-00bb5694) · [`00bb5698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5690.md#insn-00bb5698)

~~~diff
- 00bb5690 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bb5690 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bb5690 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bb5690 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb5690 bytes f657bda9
- 00bb5694 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb5694 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb5694 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb5694 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb5694 bytes f44f01a9
- 00bb5698 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb5698 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb5698 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bb5698 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb5698 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e868ccf9f2a5fe7530f3e79ad2aa20bc"></a>

### [`00bb57c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb57c0.md) → [`00bb5be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5be8.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE4syncEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5cd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd90.md) · 呼出先 5件 [`00bb5ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5ec4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c59e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e20.md) [`00c5cde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cde0.md)
- 新版 呼出元 1件 [`00c5d190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d190.md) · 呼出先 5件 [`00bb62ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb62ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5a220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a220.md) [`00c5d1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.90% / 新版 87.90%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb57c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb57c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb57c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb57c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb57c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb57cc",
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
      "00bb5bec",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bb5bf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bb5bf4",
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

- 旧版 [`00bb57c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb57c0.md#insn-00bb57c4) · [`00bb57c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb57c0.md#insn-00bb57c8) · [`00bb57cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb57c0.md#insn-00bb57cc)

~~~diff
- 00bb57c4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bb57c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00bb57c4 bytes f70b00f9
- 00bb57c8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bb57c8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bb57c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bb57c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb57c8 bytes f65702a9
- 00bb57cc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb57cc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb57cc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bb57cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb57cc bytes f44f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88d34cfb96ae208f5694b98607d7da2d"></a>

### [`00bb5f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5f44.md) → [`00bb636c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb636c.md) FUN_00bb636c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, store_value

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb6390",
      "incomplete_value": true,
      "site": "00bb6398",
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
      "definition_site": "00bb5f68",
      "incomplete_value": true,
      "site": "00bb5f70",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb63a0",
      "incomplete_value": true,
      "site": "00bb63a0",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb5f78",
      "incomplete_value": true,
      "site": "00bb5f78",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb63a0",
      "incomplete_value": true,
      "site": "00bb63a0",
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
      "definition_site": "00bb5f78",
      "incomplete_value": true,
      "site": "00bb5f78",
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
      "00bb637c",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6384",
      "READ",
      [
        "storage",
        "00c9a7c0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6398",
      "DATA",
      [
        "storage",
        "00c90c38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb637c",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6384",
      "READ",
      [
        "storage",
        "00c9abc0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6398",
      "DATA",
      [
        "storage",
        "00c91038",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb5f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5f44.md#insn-00bb5f54) · [`00bb5f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5f44.md#insn-00bb5f5c) · [`00bb5f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5f44.md#insn-00bb5f84)
- 新版 `00bb637c`（命令位置の公開資料なし） · `00bb6384`（命令位置の公開資料なし） · `00bb63ac`（命令位置の公開資料なし）

~~~diff
- 00bb5f54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:888:8"]]
- 00bb5f54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb637c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c88:8"]]
+ 00bb637c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb5f54 bytes 084544f9
+ 00bb637c bytes 084546f9
- 00bb5f5c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7c0:8"]]
- 00bb5f5c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb6384 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bc0:8"]]
+ 00bb6384 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb5f5c bytes 29e143f9
+ 00bb6384 bytes 29e145f9
- 00bb5f84 ["INT_ADD", "register:40f0:8", ["const:bb5f84:8", "const:4:8"]]
- 00bb5f84 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bb63ac ["INT_ADD", "register:40f0:8", ["const:bb63ac:8", "const:4:8"]]
+ 00bb63ac ["CALL", null, ["callee:00c57eb0:8"]]
- 00bb5f84 bytes cb860294
+ 00bb63ac bytes c1860294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4de11ce0d52c8115f4f6414ee1421a93"></a>

### [`00bb5fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5fb8.md) → [`00bb63e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb63e0.md) FUN_00bb63e0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 41.94% / 新版 41.94%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5fb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5fb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5fbc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb5fb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb5fbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb5fd0",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb63e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb63e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb63f8",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb5fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5fb8.md#insn-00bb5fb8) · [`00bb5fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5fb8.md#insn-00bb5fbc) · [`00bb5fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5fb8.md#insn-00bb5fe4)

~~~diff
- 00bb5fb8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb5fb8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb5fb8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb5fb8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb5fb8 bytes f44fbea9
- 00bb5fbc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb5fbc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb5fbc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb5fbc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb5fbc bytes fd7b01a9
- 00bb5fe4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb5fe4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00bb5fe4 bytes 8a0200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-735053305d3d52b81bd9768927f37190"></a>

### [`00bb6034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6034.md) → [`00bb645c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb645c.md) FUN_00bb645c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 45.45% / 新版 45.45%

CFGの説明率　旧版 33.33% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6034"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6034"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6038"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb6034",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb6038",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb604c",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb645c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb6460",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb6474",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6034.md#insn-00bb6034) · [`00bb6038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6034.md#insn-00bb6038) · [`00bb6060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6034.md#insn-00bb6060)

~~~diff
- 00bb6034 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb6034 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb6034 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb6034 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb6034 bytes f44fbea9
- 00bb6038 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb6038 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb6038 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb6038 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb6038 bytes fd7b01a9
- 00bb6060 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bb6060 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00bb6060 bytes 6a0200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e760a967d5ee48569131ec95d713b2e4"></a>

### [`00bb60b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb60b8.md) → [`00bb64e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb64e0.md) FUN_00bb64e0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md) [`00c5cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md) [`00c5d1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1b0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb60e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb60e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb650c"
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
      "unmatched:00bb60d0",
      "READ",
      [
        "storage",
        "00c9aac0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bb60e4",
      "DATA",
      [
        "storage",
        "00c90cc8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bb60e8",
      "DATA",
      [
        "storage",
        "00c90cf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb64f8",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb650c",
      "DATA",
      [
        "storage",
        "00c910c8",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6510",
      "DATA",
      [
        "storage",
        "00c910f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb60e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb60b8.md#insn-00bb60e4) · [`00bb60e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb60b8.md#insn-00bb60e8) · [`00bb60ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb60b8.md#insn-00bb60ec)
- 新版 `00bb6514`（命令位置の公開資料なし）

~~~diff
- 00bb60e4 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00bb60e4 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00bb60e4 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
- 00bb60e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bb60e4 bytes 0a8400f8
- 00bb60e8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bb60e8 ["INT_ADD", "register:4098:8", ["register:4098:8", "const:b0:8"]]
- 00bb60e8 ["STORE", null, ["const:1b1:8", "register:4098:8", "tmp:0:8"]]
- 00bb60e8 bytes 680e0bf8
- 00bb60ec ["INT_ADD", "register:40f0:8", ["const:bb60ec:8", "const:4:8"]]
- 00bb60ec ["CALL", null, ["callee:00c5d1b0:8"]]
+ 00bb6514 ["INT_ADD", "register:40f0:8", ["const:bb6514:8", "const:4:8"]]
+ 00bb6514 ["CALL", null, ["callee:00c5d1b0:8"]]
- 00bb60ec bytes 319b0294
+ 00bb6514 bytes 279b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7833af191bb49da1ff4c59243129017e"></a>

### [`00bb6100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6100.md) → [`00bb6528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6528.md) FUN_00bb6528

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md) [`00c5cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md) [`00c5d1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1b0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 61.11% / 新版 61.11%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6100"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6100"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6104"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb6100",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb6104",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb6538",
      "READ",
      [
        "storage",
        "00c9aac0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb6528",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb652c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb6538",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6100.md#insn-00bb6100) · [`00bb6104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6100.md#insn-00bb6104) · [`00bb6124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6100.md#insn-00bb6124)

~~~diff
- 00bb6100 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb6100 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb6100 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb6100 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb6100 bytes f44fbea9
- 00bb6104 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb6104 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb6104 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb6104 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb6104 bytes fd7b01a9
- 00bb6124 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bb6124 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00bb6124 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
- 00bb6124 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bb6124 bytes 098400f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae9460b89d08b046b25f5e22e3d31131"></a>

### [`00bb6148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6148.md) → [`00bb6570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6570.md) FUN_00bb6570

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md) [`00c5cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md) [`00c5d1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1b0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 33.33% / 新版 33.33%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6148"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6148"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb614c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb6148",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb614c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb6160",
      "READ",
      [
        "storage",
        "00c9aac0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb6570",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb6574",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb6588",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6148.md#insn-00bb6148) · [`00bb614c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6148.md#insn-00bb614c) · [`00bb6178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6148.md#insn-00bb6178)

~~~diff
- 00bb6148 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb6148 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb6148 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb6148 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb6148 bytes f44fbea9
- 00bb614c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb614c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb614c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb614c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb614c bytes fd7b01a9
- 00bb6178 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00bb6178 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00bb6178 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
- 00bb6178 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bb6178 bytes 0a8400f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ea5bf67c19637377291edfc6fa5c7c3"></a>

### [`00bb620c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb620c.md) → [`00bb6634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6634.md) _ZNKSt6__ndk110__function6__funcIPFccENS_9allocatorIS3_EES2_E6targetERKSt9type_info

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb6644",
      "incomplete_value": true,
      "site": "00bb6648",
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
      "definition_site": "00bb621c",
      "incomplete_value": true,
      "site": "00bb6220",
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
      "00bb663c",
      "READ",
      [
        "storage",
        "00c9b4e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb663c",
      "READ",
      [
        "storage",
        "00c9b8e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb620c.md#insn-00bb6214)
- 新版 `00bb663c`（命令位置の公開資料なし）

~~~diff
- 00bb6214 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:4e0:8"]]
- 00bb6214 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb663c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:8e0:8"]]
+ 00bb663c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb6214 bytes 297142f9
+ 00bb663c bytes 297144f9
~~~


<a id="compare-61a38910fdf4cd848c18f902d337cada"></a>

### [`00bb6238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6238.md) → [`00bb6660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6660.md) _INIT_284

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb398c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb398c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb3db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb3db4.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 29.41% / 新版 29.41%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6238"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6238"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb626c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb6238",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb6244",
      "PARAM",
      [
        "storage",
        "002b613c",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb625c",
      "READ",
      [
        "storage",
        "00c9b430",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb6660",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb666c",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ],
    [
      "00bb6684",
      "READ",
      [
        "storage",
        "00c9b830",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6238.md#insn-00bb6238) · [`00bb6250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6238.md#insn-00bb6250) · [`00bb626c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6238.md#insn-00bb626c)
- 新版 `00bb6678`（命令位置の公開資料なし）

~~~diff
- 00bb6238 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb6238 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb6238 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00bb6238 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb6238 bytes fd7bbfa9
- 00bb6250 ["INT_ADD", "register:40f0:8", ["const:bb6250:8", "const:4:8"]]
- 00bb6250 ["CALL", null, ["callee:00c5d220:8"]]
+ 00bb6678 ["INT_ADD", "register:40f0:8", ["const:bb6678:8", "const:4:8"]]
+ 00bb6678 ["CALL", null, ["callee:00c5d220:8"]]
- 00bb6250 bytes f49a0294
+ 00bb6678 bytes ea9a0294
- 00bb626c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00bb626c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb626c bytes 200000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef720a9ded1abd06aa86ff24b6d53094"></a>

### [`00bb6330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6330.md) → [`00bb6758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6758.md) _ZN8firebase9messaging8internal38UnregisterTerminateOnDefaultAppDestroyEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d030.md) · 呼出先 5件 [`00c5a7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7d0.md) [`00c5a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7f0.md) [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md) [`00c5a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a860.md) [`00c5d010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d010.md)
- 新版 呼出元 1件 [`00c5d430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d430.md) · 呼出先 5件 [`00c5abd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abd0.md) [`00c5abf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abf0.md) [`00c5ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md) [`00c5ac60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac60.md) [`00c5d410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d410.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 43.75% / 新版 43.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6330"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6330"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb6758"
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
      "unmatched:00bb6330",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb633c",
      "PARAM",
      [
        "storage",
        "0030e69f",
        null,
        "string"
      ]
    ],
    [
      "00bb676c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bb6368"
      ]
    ]
  ],
  "added": [
    [
      "00bb6758",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb6764",
      "PARAM",
      [
        "storage",
        "0030e6df",
        null,
        "string"
      ]
    ],
    [
      "00bb676c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb6790"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6330.md#insn-00bb6330) · [`00bb6340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6330.md#insn-00bb6340) · [`00bb636c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6330.md#insn-00bb636c)
- 新版 `00bb6768`（命令位置の公開資料なし）

~~~diff
- 00bb6330 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb6330 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb6330 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00bb6330 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb6330 bytes fd7bbfa9
- 00bb6340 ["INT_ADD", "register:40f0:8", ["const:bb6340:8", "const:4:8"]]
- 00bb6340 ["CALL", null, ["callee:00c5abd0:8"]]
+ 00bb6768 ["INT_ADD", "register:40f0:8", ["const:bb6768:8", "const:4:8"]]
+ 00bb6768 ["CALL", null, ["callee:00c5abd0:8"]]
- 00bb6340 bytes 24910294
+ 00bb6768 bytes 1a910294
- 00bb636c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bb636c ["RETURN", null, ["register:0:8"]]
- 00bb636c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0fb67d448850c52b4e9238e6f9278f6"></a>

### [`00bb6370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6370.md) → [`00bb6798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6798.md) _ZN8firebase9messaging11SetListenerEPNS0_8ListenerE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ceb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ceb0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5cef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cef0.md)
- 新版 呼出元 1件 [`00c5d2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2b0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5d2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2f0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 15.00% / 新版 19.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 3件, `store_destination` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6370"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6370"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6374"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb6370",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb6374",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb6378",
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
      "00bb6798",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bb679c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bb67a0",
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

- 旧版 [`00bb6370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6370.md#insn-00bb6370) · [`00bb6374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6370.md#insn-00bb6374) · [`00bb6378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6370.md#insn-00bb6378)

~~~diff
- 00bb6370 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bb6370 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bb6370 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00bb6370 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb6370 bytes fa67bba9
- 00bb6374 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bb6374 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bb6374 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb6374 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb6374 bytes f85f01a9
- 00bb6378 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bb6378 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bb6378 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bb6378 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb6378 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fd033b1783b1027a90d833312cfe78f"></a>

### [`00bb6538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6538.md) → [`00bb6960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6960.md) _ZN8firebase9messaging11HasListenerEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5cea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cea0.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00c5d2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2a0.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb6974",
      "incomplete_value": false,
      "site": "00bb6978",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb654c",
      "incomplete_value": false,
      "site": "00bb6550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1125000:8"
          ],
          [
            "leaf",
            "const:e08:8"
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
      "unmatched:00bb654c",
      "PARAM",
      [
        "storage",
        "01125e08",
        null,
        null
      ]
    ],
    [
      "00bb6980",
      "READ",
      [
        "storage",
        "01125e30",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb6984",
      "PARAM",
      [
        "storage",
        "01125e08",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb6974",
      "PARAM",
      [
        "storage",
        "01126208",
        null,
        null
      ]
    ],
    [
      "00bb6980",
      "READ",
      [
        "storage",
        "01126230",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb6984",
      "PARAM",
      [
        "storage",
        "01126208",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6538.md#insn-00bb6550) · [`00bb6544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6538.md#insn-00bb6544) · [`00bb6548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6538.md#insn-00bb6548)
- 新版 `00bb6978`（命令位置の公開資料なし） · `00bb696c`（命令位置の公開資料なし）

~~~diff
- 00bb6550 ["INT_ADD", "register:40f0:8", ["const:bb6550:8", "const:4:8"]]
- 00bb6550 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bb6978 ["INT_ADD", "register:40f0:8", ["const:bb6978:8", "const:4:8"]]
+ 00bb6978 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bb6550 bytes 2c900294
+ 00bb6978 bytes 22900294
- 00bb6544 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00bb696c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bb6544 bytes 732b00f0
+ 00bb696c bytes 932b0090
- 00bb6548 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 00bb6548 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00bb6548 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00bb6548 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00bb6548 bytes 73223891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-100230d62616e16d9bb2a81f5c9cf571"></a>

### [`00bb6590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6590.md) → [`00bb69b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb69b8.md) _ZN8firebase9messaging23NotifyListenerOnMessageERKNS0_7MessageE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5cfa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cfa0.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00c5d3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3a0.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 45.00% / 新版 45.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb65b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bb69dc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb65a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb65a4",
      "PARAM",
      [
        "storage",
        "01125e08",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb65a8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5aa00"
      ]
    ],
    [
      "unmatched:00bb65b0",
      "READ",
      [
        "storage",
        "01125e30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb69cc",
      "PARAM",
      [
        "storage",
        "01126208",
        null,
        null
      ]
    ],
    [
      "00bb69d0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5aa00"
      ]
    ],
    [
      "00bb69d8",
      "READ",
      [
        "storage",
        "01126230",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb65a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6590.md#insn-00bb65a8) · [`00bb65b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6590.md#insn-00bb65b4) · [`00bb65c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6590.md#insn-00bb65c4)

~~~diff
- 00bb65a8 ["INT_ADD", "register:40f0:8", ["const:bb65a8:8", "const:4:8"]]
- 00bb65a8 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bb65a8 bytes 16900294
- 00bb65b4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bb65b4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bb65b4 bytes a00000b4
- 00bb65c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb65c4 ["INT_ADD", "register:40f0:8", ["const:bb65c4:8", "const:4:8"]]
- 00bb65c4 ["CALLIND", null, ["register:0:8"]]
- 00bb65c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53b38ff8e5aa0f8714f24f8004583f20"></a>

### [`00bb6600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6600.md) → [`00bb6a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6a28.md) _ZN8firebase9messaging29NotifyListenerOnTokenReceivedEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5cfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cfb0.md) · 呼出先 8件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md)
- 新版 呼出元 1件 [`00c5d3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3b0.md) · 呼出先 8件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 2件, `store_condition` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb6ab8",
      "incomplete_value": true,
      "site": "00bb6ab8",
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
            "const:238:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6690",
      "incomplete_value": true,
      "site": "00bb6690",
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
            "const:e38:8"
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
      "definition_site": "00bb6afc",
      "incomplete_value": false,
      "site": "00bb6afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb66d4",
      "incomplete_value": false,
      "site": "00bb66d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1125000:8"
          ],
          [
            "leaf",
            "const:e48:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb6a50",
      "incomplete_value": true,
      "site": "00bb6a50",
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
      "definition_site": "00bb6628",
      "incomplete_value": true,
      "site": "00bb6628",
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
      "00bb6a40",
      "PARAM",
      [
        "storage",
        "01125e08",
        null,
        null
      ]
    ],
    [
      "00bb6a4c",
      "READ",
      [
        "storage",
        "01125e38",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb6ab8",
      "WRITE",
      [
        "storage",
        "01125e38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb6a40",
      "PARAM",
      [
        "storage",
        "01126208",
        null,
        null
      ]
    ],
    [
      "00bb6a4c",
      "READ",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb6ab8",
      "WRITE",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb661c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6600.md#insn-00bb661c) · [`00bb6690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6600.md#insn-00bb6690) · [`00bb66d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6600.md#insn-00bb66d4)
- 新版 `00bb6a44`（命令位置の公開資料なし） · `00bb6ab8`（命令位置の公開資料なし） · `00bb6afc`（命令位置の公開資料なし）

~~~diff
- 00bb661c ["INT_ADD", "register:40f0:8", ["const:bb661c:8", "const:4:8"]]
- 00bb661c ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bb6a44 ["INT_ADD", "register:40f0:8", ["const:bb6a44:8", "const:4:8"]]
+ 00bb6a44 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bb661c bytes f98f0294
+ 00bb6a44 bytes ef8f0294
- 00bb6690 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e38:8"]]
- 00bb6690 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb6ab8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:238:8"]]
+ 00bb6ab8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb6690 bytes a01e07f9
+ 00bb6ab8 bytes a01e01f9
- 00bb66d4 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bb66d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:e48:8"]]
- 00bb66d4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bb6afc ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00bb6afc ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:248:8"]]
+ 00bb6afc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bb66d4 bytes 09213939
+ 00bb6afc bytes 09210939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-498df7bb4c1bac610df20c6ccaac31e5"></a>

### [`00bb6720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6720.md) → [`00bb6b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6b48.md) _ZN8firebase9messaging36NotifyListenerOnRegistrationReceivedEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5cfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cfc0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)
- 新版 呼出元 1件 [`00c5d3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3c0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 2件, `store_condition` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb6b94",
      "incomplete_value": true,
      "site": "00bb6b94",
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
            "const:240:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb676c",
      "incomplete_value": true,
      "site": "00bb676c",
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
            "const:e40:8"
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
      "definition_site": "00bb6bd8",
      "incomplete_value": false,
      "site": "00bb6bd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:249:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb67b0",
      "incomplete_value": false,
      "site": "00bb67b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1125000:8"
          ],
          [
            "leaf",
            "const:e49:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb6b7c",
      "incomplete_value": true,
      "site": "00bb6b7c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb6754",
      "incomplete_value": true,
      "site": "00bb6754",
      "value": [
        "INT_NOTEQUAL",
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
      "00bb6b6c",
      "PARAM",
      [
        "storage",
        "01125e08",
        null,
        null
      ]
    ],
    [
      "00bb6b78",
      "READ",
      [
        "storage",
        "01125e40",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb6b94",
      "WRITE",
      [
        "storage",
        "01125e40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb6b6c",
      "PARAM",
      [
        "storage",
        "01126208",
        null,
        null
      ]
    ],
    [
      "00bb6b78",
      "READ",
      [
        "storage",
        "01126240",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb6b94",
      "WRITE",
      [
        "storage",
        "01126240",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6720.md#insn-00bb6748) · [`00bb676c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6720.md#insn-00bb676c) · [`00bb67b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6720.md#insn-00bb67b0)
- 新版 `00bb6b70`（命令位置の公開資料なし） · `00bb6b94`（命令位置の公開資料なし） · `00bb6bd8`（命令位置の公開資料なし）

~~~diff
- 00bb6748 ["INT_ADD", "register:40f0:8", ["const:bb6748:8", "const:4:8"]]
- 00bb6748 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bb6b70 ["INT_ADD", "register:40f0:8", ["const:bb6b70:8", "const:4:8"]]
+ 00bb6b70 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bb6748 bytes ae8f0294
+ 00bb6b70 bytes a48f0294
- 00bb676c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e40:8"]]
- 00bb676c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb6b94 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:240:8"]]
+ 00bb6b94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb676c bytes a02207f9
+ 00bb6b94 bytes a02201f9
- 00bb67b0 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bb67b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:e49:8"]]
- 00bb67b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bb6bd8 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00bb6bd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:249:8"]]
+ 00bb6bd8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bb67b0 bytes 09253939
+ 00bb6bd8 bytes 09250939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-912845c0a08e2744322aa3d857b27fb8"></a>

### [`00bb67f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb67f0.md) → [`00bb6c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6c18.md) _ZN8firebase9messaging38NotifyListenerOnUnregistrationReceivedEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5cfd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cfd0.md) · 呼出先 7件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md)
- 新版 呼出元 1件 [`00c5d3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3d0.md) · 呼出先 7件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 86.21% / 新版 86.21%

CFGの説明率　旧版 86.96% / 新版 90.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb67f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb67f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb67f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb67f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb67f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb67f8",
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
      "00bb6c18",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bb6c1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb6c20",
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

- 旧版 [`00bb67f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb67f0.md#insn-00bb67f0) · [`00bb67f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb67f0.md#insn-00bb67f4) · [`00bb67f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb67f0.md#insn-00bb67f8)

~~~diff
- 00bb67f0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bb67f0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bb67f0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bb67f0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb67f0 bytes f657bda9
- 00bb67f4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb67f4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb67f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb67f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb67f4 bytes f44f01a9
- 00bb67f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb67f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb67f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bb67f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb67f8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2bfed215a5c932d0849f3c08c78da44"></a>

### [`00bb698c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb698c.md) → [`00bb6db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6db4.md) _ZN8firebase9messaging16PollableListenerD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6c0.md) [`00c5cf80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cf80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aac0.md) [`00c5d380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d380.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb6dd0",
      "incomplete_value": true,
      "site": "00bb6dd4",
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
      "definition_site": "00bb69a8",
      "incomplete_value": true,
      "site": "00bb69ac",
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
      "00bb6dc8",
      "READ",
      [
        "storage",
        "00c9b500",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6dd4",
      "DATA",
      [
        "storage",
        "00c90e28",
        null,
        "undefined1[64]"
      ]
    ]
  ],
  "added": [
    [
      "00bb6dc8",
      "READ",
      [
        "storage",
        "00c9b900",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6dd4",
      "DATA",
      [
        "storage",
        "00c91228",
        null,
        "undefined1[64]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb69a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb698c.md#insn-00bb69a0) · [`00bb69b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb698c.md#insn-00bb69b8) · [`00bb69c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb698c.md#insn-00bb69c0)
- 新版 `00bb6dc8`（命令位置の公開資料なし） · `00bb6de0`（命令位置の公開資料なし） · `00bb6de8`（命令位置の公開資料なし）

~~~diff
- 00bb69a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:500:8"]]
- 00bb69a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb6dc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:900:8"]]
+ 00bb6dc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb69a0 bytes 088142f9
+ 00bb6dc8 bytes 088144f9
- 00bb69b8 ["INT_ADD", "register:40f0:8", ["const:bb69b8:8", "const:4:8"]]
- 00bb69b8 ["CALL", null, ["callee:00c5d380:8"]]
+ 00bb6de0 ["INT_ADD", "register:40f0:8", ["const:bb6de0:8", "const:4:8"]]
+ 00bb6de0 ["CALL", null, ["callee:00c5d380:8"]]
- 00bb69b8 bytes 72990294
+ 00bb6de0 bytes 68990294
- 00bb69c0 ["INT_ADD", "register:40f0:8", ["const:bb69c0:8", "const:4:8"]]
- 00bb69c0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bb6de8 ["INT_ADD", "register:40f0:8", ["const:bb6de8:8", "const:4:8"]]
+ 00bb6de8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00bb69c0 bytes 3c840294
+ 00bb6de8 bytes 32840294
~~~


<a id="compare-7bf8adb6e343ec67eb98b15aa836e109"></a>

### [`00bb6a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6a94.md) → [`00bb6ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6ebc.md) _ZN8firebase9messaging16PollableListenerD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6c0.md) [`00c5cf80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cf80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aac0.md) [`00c5d380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d380.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb6ed8",
      "incomplete_value": true,
      "site": "00bb6edc",
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
      "definition_site": "00bb6ab0",
      "incomplete_value": true,
      "site": "00bb6ab4",
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
      "00bb6ed0",
      "READ",
      [
        "storage",
        "00c9b500",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6edc",
      "DATA",
      [
        "storage",
        "00c90e28",
        null,
        "undefined1[64]"
      ]
    ]
  ],
  "added": [
    [
      "00bb6ed0",
      "READ",
      [
        "storage",
        "00c9b900",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6edc",
      "DATA",
      [
        "storage",
        "00c91228",
        null,
        "undefined1[64]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6a94.md#insn-00bb6aa8) · [`00bb6ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6a94.md#insn-00bb6ac0) · [`00bb6ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6a94.md#insn-00bb6ac8)
- 新版 `00bb6ed0`（命令位置の公開資料なし） · `00bb6ee8`（命令位置の公開資料なし） · `00bb6ef0`（命令位置の公開資料なし）

~~~diff
- 00bb6aa8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:500:8"]]
- 00bb6aa8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb6ed0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:900:8"]]
+ 00bb6ed0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb6aa8 bytes 088142f9
+ 00bb6ed0 bytes 088144f9
- 00bb6ac0 ["INT_ADD", "register:40f0:8", ["const:bb6ac0:8", "const:4:8"]]
- 00bb6ac0 ["CALL", null, ["callee:00c5d380:8"]]
+ 00bb6ee8 ["INT_ADD", "register:40f0:8", ["const:bb6ee8:8", "const:4:8"]]
+ 00bb6ee8 ["CALL", null, ["callee:00c5d380:8"]]
- 00bb6ac0 bytes 30990294
+ 00bb6ee8 bytes 26990294
- 00bb6ac8 ["INT_ADD", "register:40f0:8", ["const:bb6ac8:8", "const:4:8"]]
- 00bb6ac8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00bb6ef0 ["INT_ADD", "register:40f0:8", ["const:bb6ef0:8", "const:4:8"]]
+ 00bb6ef0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00bb6ac8 bytes fa830294
+ 00bb6ef0 bytes f0830294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5319f1d259eaca2291e23d0289f4e31"></a>

### [`00bb7224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7224.md) → [`00bb764c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb764c.md) FUN_00bb764c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb62f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb62f0.md) · 呼出先 3件 [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5d010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d010.md) [`00c5d040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d040.md)
- 新版 呼出元 1件 [`00bb6718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6718.md) · 呼出先 3件 [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5d410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d410.md) [`00c5d440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d440.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb7658",
      "incomplete_value": false,
      "site": "00bb765c",
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
            "const:b80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb7230",
      "incomplete_value": false,
      "site": "00bb7234",
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
            "const:ab3:8"
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
      "00bb7658",
      "PARAM",
      [
        "storage",
        "0029fab3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb7658",
      "PARAM",
      [
        "storage",
        "0029fb80",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb7234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7224.md#insn-00bb7234) · [`00bb7230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7224.md#insn-00bb7230) · [`00bb7238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7224.md#insn-00bb7238)
- 新版 `00bb765c`（命令位置の公開資料なし） · `00bb7658`（命令位置の公開資料なし） · `00bb7660`（命令位置の公開資料なし）

~~~diff
- 00bb7234 ["INT_ADD", "register:40f0:8", ["const:bb7234:8", "const:4:8"]]
- 00bb7234 ["CALL", null, ["callee:00c5aca0:8"]]
+ 00bb765c ["INT_ADD", "register:40f0:8", ["const:bb765c:8", "const:4:8"]]
+ 00bb765c ["CALL", null, ["callee:00c5aca0:8"]]
- 00bb7234 bytes 9b8d0294
+ 00bb765c bytes 918d0294
- 00bb7230 ["COPY", "tmp:0:8", ["const:ab3:8"]]
- 00bb7230 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb7230 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb7230 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb7658 ["COPY", "tmp:0:8", ["const:b80:8"]]
+ 00bb7658 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb7658 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb7658 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb7230 bytes 00cc2a91
+ 00bb7658 bytes 00002e91
- 00bb7238 ["INT_ADD", "register:40f0:8", ["const:bb7238:8", "const:4:8"]]
- 00bb7238 ["CALL", null, ["callee:00c5d410:8"]]
+ 00bb7660 ["INT_ADD", "register:40f0:8", ["const:bb7660:8", "const:4:8"]]
+ 00bb7660 ["CALL", null, ["callee:00c5d410:8"]]
- 00bb7238 bytes 76970294
+ 00bb7660 bytes 6c970294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-978f6d0844d7a0f44aff9980ccefb0a2"></a>

### [`00bb7f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7f60.md) → [`00bb8388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8388.md) _ZNSt6__ndk15dequeIN8firebase9messaging7MessageENS_9allocatorIS3_EEE19__add_back_capacityEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d0b0.md) · 呼出先 9件 [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00bb8174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8174.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5d4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d4b0.md) · 呼出先 9件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00bb859c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb859c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.82% / 新版 91.82%

CFGの説明率　旧版 69.23% / 新版 72.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb80c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb80e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb84ec"
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
      "unmatched:00bb80c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb80c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb850c"
      ]
    ],
    [
      "unmatched:00bb80e0",
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
      "00bb84ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bb84f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb850c"
      ]
    ],
    [
      "00bb8508",
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

- 旧版 [`00bb80c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7f60.md#insn-00bb80c4) · [`00bb80c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7f60.md#insn-00bb80c8) · [`00bb80e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7f60.md#insn-00bb80e0)

~~~diff
- 00bb80c4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00bb80c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00bb80c4 bytes e10b803d
- 00bb80c8 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 00bb80c8 bytes e0000054
- 00bb80e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00bb80e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb80e0 bytes e81300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1150cd35ffca127887d4aa60c955bac"></a>

### [`00bb8174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8174.md) → [`00bb859c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb859c.md) FUN_00bb859c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb7f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7f60.md) · 呼出先 4件 [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00bb8388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8388.md) · 呼出先 4件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.75% / 新版 98.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb86d4",
      "incomplete_value": false,
      "site": "00bb86d8",
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
            "const:67b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb82ac",
      "incomplete_value": false,
      "site": "00bb82b0",
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
            "const:5ae:8"
          ]
        ]
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
      "00bb86d4",
      "PARAM",
      [
        "storage",
        "002a85ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb86d4",
      "PARAM",
      [
        "storage",
        "002a867b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb82b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8174.md#insn-00bb82b0) · [`00bb81e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8174.md#insn-00bb81e0) · [`00bb8218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8174.md#insn-00bb8218)
- 新版 `00bb86d8`（命令位置の公開資料なし） · `00bb8608`（命令位置の公開資料なし） · `00bb8640`（命令位置の公開資料なし）

~~~diff
- 00bb82b0 ["INT_ADD", "register:40f0:8", ["const:bb82b0:8", "const:4:8"]]
- 00bb82b0 ["CALL", null, ["callee:00b402c0:8"]]
+ 00bb86d8 ["INT_ADD", "register:40f0:8", ["const:bb86d8:8", "const:4:8"]]
+ 00bb86d8 ["CALL", null, ["callee:00b402c0:8"]]
- 00bb82b0 bytes fa1efe97
+ 00bb86d8 bytes fa1efe97
- 00bb81e0 ["INT_ADD", "register:40f0:8", ["const:bb81e0:8", "const:4:8"]]
- 00bb81e0 ["CALL", null, ["callee:00c57f40:8"]]
+ 00bb8608 ["INT_ADD", "register:40f0:8", ["const:bb8608:8", "const:4:8"]]
+ 00bb8608 ["CALL", null, ["callee:00c57f40:8"]]
- 00bb81e0 bytes 587e0294
+ 00bb8608 bytes 4e7e0294
- 00bb8218 ["INT_ADD", "register:40f0:8", ["const:bb8218:8", "const:4:8"]]
- 00bb8218 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bb8640 ["INT_ADD", "register:40f0:8", ["const:bb8640:8", "const:4:8"]]
+ 00bb8640 ["CALL", null, ["callee:00c57e90:8"]]
- 00bb8218 bytes 1e7e0294
+ 00bb8640 bytes 147e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1046b065f87885b034cef192cd1d38eb"></a>

### [`00bb82b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb82b4.md) → [`00bb86dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb86dc.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageENS_9allocatorIS4_EEE9push_backEOS4_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d080.md) · 呼出先 4件 [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00c5d480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d480.md) · 呼出先 4件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 66.67% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb82b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb82b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb82b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb82b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb82b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb82bc",
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
      "00bb86dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bb86e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bb86e4",
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

- 旧版 [`00bb82b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb82b4.md#insn-00bb82b4) · [`00bb82b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb82b4.md#insn-00bb82b8) · [`00bb82bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb82b4.md#insn-00bb82bc)

~~~diff
- 00bb82b4 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00bb82b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00bb82b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb82b4 bytes f90f1bf8
- 00bb82b8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bb82b8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bb82b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb82b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb82b8 bytes f85f01a9
- 00bb82bc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bb82bc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bb82bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bb82bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb82bc bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae4337b6ec9f0648020071772327693a"></a>

### [`00bb8534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8534.md) → [`00bb895c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb895c.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageERNS_9allocatorIS4_EEE9push_backEOS4_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d0a0.md) · 呼出先 4件 [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00c5d4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d4a0.md) · 呼出先 4件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 28.57% / 新版 26.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8608"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb8a30"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb857c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb866c",
      "PARAM",
      [
        "storage",
        "002a85ae",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bb8670",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b402c0"
      ]
    ]
  ],
  "added": [
    [
      "00bb8a94",
      "PARAM",
      [
        "storage",
        "002a867b",
        null,
        "string"
      ]
    ],
    [
      "00bb8a98",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b402c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb857c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8534.md#insn-00bb857c) · [`00bb85d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8534.md#insn-00bb85d8) · [`00bb8608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8534.md#insn-00bb8608)
- 新版 `00bb8a00`（命令位置の公開資料なし）

~~~diff
- 00bb857c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bb857c ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00bb857c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bb857c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
- 00bb857c bytes 48b5889a
- 00bb85d8 ["INT_ADD", "register:40f0:8", ["const:bb85d8:8", "const:4:8"]]
- 00bb85d8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bb8a00 ["INT_ADD", "register:40f0:8", ["const:bb8a00:8", "const:4:8"]]
+ 00bb8a00 ["CALL", null, ["callee:00c57e90:8"]]
- 00bb85d8 bytes 2e7d0294
+ 00bb8a00 bytes 247d0294
- 00bb8608 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00bb8608 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4068:8"]]
- 00bb8608 bytes 8d0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eef598ce4678ae09bd77f30925e8510e"></a>

### [`00bb8674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8674.md) → [`00bb8a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8a9c.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageERNS_9allocatorIS4_EEE10push_frontERKS4_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d090.md) · 呼出先 4件 [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00c5d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d490.md) · 呼出先 4件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 45.83% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb86f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb86f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb8b18"
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
      "unmatched:00bb86ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8b20"
      ]
    ],
    [
      "unmatched:00bb8708",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8bd0"
      ]
    ],
    [
      "unmatched:00bb87ac",
      "PARAM",
      [
        "storage",
        "002a85ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb8ad4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8b20"
      ]
    ],
    [
      "00bb8b30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8bd0"
      ]
    ],
    [
      "00bb8bd4",
      "PARAM",
      [
        "storage",
        "002a867b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb86ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8674.md#insn-00bb86ac) · [`00bb86f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8674.md#insn-00bb86f0) · [`00bb8708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8674.md#insn-00bb8708)

~~~diff
- 00bb86ac ["CBRANCH", null, ["local:b8:8", "register:102:1"]]
- 00bb86ac bytes 62020054
- 00bb86f0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bb86f0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00bb86f0 ["INT_ADD", "tmp:2:8", ["register:4098:8", "const:8:8"]]
- 00bb86f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb86f0 bytes 76a200a9
- 00bb8708 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00bb8708 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00bb8708 bytes 090500b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5a48079724fbf0c43c49c394877e67d"></a>

### [`00bb87b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb87b4.md) → [`00bb8bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8bdc.md) _INIT_285

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b650e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b650e8.md) [`00bb627c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb627c.md) [`00bb62bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb62bc.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c5a7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00b65510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65510.md) [`00bb66a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb66a4.md) [`00bb66e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb66e4.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c5abc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abc0.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 46.43% / 新版 46.43%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb87b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb87b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb87b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb87b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb87b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb87d0",
      "PARAM",
      [
        "storage",
        "01125de8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb8bdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb8be0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb8bf8",
      "PARAM",
      [
        "storage",
        "011261e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb87b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb87b4.md#insn-00bb87b4) · [`00bb87b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb87b4.md#insn-00bb87b8) · [`00bb87e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb87b4.md#insn-00bb87e0)

~~~diff
- 00bb87b4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bb87b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb87b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb87b4 bytes f30f1ef8
- 00bb87b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb87b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb87b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb87b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb87b8 bytes fd7b01a9
- 00bb87e0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bb87e0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00bb87e0 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00bb87e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb87e0 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-724d3a8db82d13dc2e6dd0a2c976ee45"></a>

### [`00bb8838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8838.md) → [`00bb8c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8c60.md) _ZN8firebase9messaging18firebase_messaging19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8864"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb8c8c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb8c74",
      "incomplete_value": true,
      "site": "00bb8c74",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb884c",
      "incomplete_value": true,
      "site": "00bb884c",
      "value": [
        "INT_NOTEQUAL",
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
      "00bb8c70",
      "READ",
      [
        "storage",
        "01125ea8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8c74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bb8868"
      ]
    ],
    [
      "unmatched:00bb8858",
      "PARAM",
      [
        "storage",
        "002bae5e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb8c70",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8c74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8c90"
      ]
    ],
    [
      "00bb8c80",
      "PARAM",
      [
        "storage",
        "002bae9e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb884c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8838.md#insn-00bb884c) · [`00bb885c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8838.md#insn-00bb885c) · [`00bb8864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8838.md#insn-00bb8864)
- 新版 `00bb8c74`（命令位置の公開資料なし）

~~~diff
- 00bb884c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bb884c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bb8c74 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bb8c74 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bb884c bytes e80000b5
+ 00bb8c74 bytes e80000b5
- 00bb885c ["INT_ADD", "register:40f0:8", ["const:bb885c:8", "const:4:8"]]
- 00bb885c ["CALL", null, ["callee:00c5af10:8"]]
- 00bb885c bytes ad880294
- 00bb8864 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ea8:8"]]
- 00bb8864 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8864 bytes 605607f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f2326a4fa454b0eeb1e3de7cc5bffc8"></a>

### [`00bb8878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8878.md) → [`00bb8ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8ca0.md) _ZN8firebase9messaging18firebase_messaging19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb8ccc",
      "incomplete_value": true,
      "site": "00bb8ccc",
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
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb88a4",
      "incomplete_value": true,
      "site": "00bb88a4",
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
            "const:ea8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb8cb4",
      "incomplete_value": true,
      "site": "00bb8cb4",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb888c",
      "incomplete_value": true,
      "site": "00bb888c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb8cbc",
      "incomplete_value": false,
      "site": "00bb8cc4",
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
            "const:e9e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8894",
      "incomplete_value": false,
      "site": "00bb889c",
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
            "const:e5e:8"
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
      "00bb8cb0",
      "READ",
      [
        "storage",
        "01125ea8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8cbc",
      "PARAM",
      [
        "storage",
        "002bae5e",
        null,
        "string"
      ]
    ],
    [
      "00bb8ccc",
      "WRITE",
      [
        "storage",
        "01125ea8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb8cb0",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8cbc",
      "PARAM",
      [
        "storage",
        "002bae9e",
        null,
        "string"
      ]
    ],
    [
      "00bb8ccc",
      "WRITE",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb889c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8878.md#insn-00bb889c) · [`00bb88a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8878.md#insn-00bb88a4) · [`00bb8884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8878.md#insn-00bb8884)
- 新版 `00bb8cc4`（命令位置の公開資料なし） · `00bb8ccc`（命令位置の公開資料なし） · `00bb8cac`（命令位置の公開資料なし）

~~~diff
- 00bb889c ["INT_ADD", "register:40f0:8", ["const:bb889c:8", "const:4:8"]]
- 00bb889c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bb8cc4 ["INT_ADD", "register:40f0:8", ["const:bb8cc4:8", "const:4:8"]]
+ 00bb8cc4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bb889c bytes 9d880294
+ 00bb8cc4 bytes 93880294
- 00bb88a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ea8:8"]]
- 00bb88a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb8ccc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a8:8"]]
+ 00bb8ccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb88a4 bytes 605607f9
+ 00bb8ccc bytes 605601f9
- 00bb8884 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00bb8cac ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bb8884 bytes 732b00b0
+ 00bb8cac bytes 732b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31d103cda45c96d39ad415eb3372e5da"></a>

### [`00bb88b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb88b8.md) → [`00bb8ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8ce0.md) _ZN8firebase9messaging18firebase_messaging10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb8d10",
      "incomplete_value": true,
      "site": "00bb8d10",
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
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb88e8",
      "incomplete_value": true,
      "site": "00bb88e8",
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
            "const:ea8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb8cf4",
      "incomplete_value": true,
      "site": "00bb8cf4",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb88cc",
      "incomplete_value": true,
      "site": "00bb88cc",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb8d00",
      "incomplete_value": false,
      "site": "00bb8d08",
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
            "const:e9e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb88d8",
      "incomplete_value": false,
      "site": "00bb88e0",
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
            "const:e5e:8"
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
      "00bb8cf0",
      "READ",
      [
        "storage",
        "01125ea8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8d00",
      "PARAM",
      [
        "storage",
        "002bae5e",
        null,
        "string"
      ]
    ],
    [
      "00bb8d10",
      "WRITE",
      [
        "storage",
        "01125ea8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb8cf0",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8d00",
      "PARAM",
      [
        "storage",
        "002bae9e",
        null,
        "string"
      ]
    ],
    [
      "00bb8d10",
      "WRITE",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb88e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb88b8.md#insn-00bb88e0) · [`00bb88e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb88b8.md#insn-00bb88e8) · [`00bb88c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb88b8.md#insn-00bb88c4)
- 新版 `00bb8d08`（命令位置の公開資料なし） · `00bb8d10`（命令位置の公開資料なし） · `00bb8cec`（命令位置の公開資料なし）

~~~diff
- 00bb88e0 ["INT_ADD", "register:40f0:8", ["const:bb88e0:8", "const:4:8"]]
- 00bb88e0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bb8d08 ["INT_ADD", "register:40f0:8", ["const:bb8d08:8", "const:4:8"]]
+ 00bb8d08 ["CALL", null, ["callee:00c5af10:8"]]
- 00bb88e0 bytes 8c880294
+ 00bb8d08 bytes 82880294
- 00bb88e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ea8:8"]]
- 00bb88e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb8d10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a8:8"]]
+ 00bb8d10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb88e8 bytes 605607f9
+ 00bb8d10 bytes 605601f9
- 00bb88c4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00bb8cec ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bb88c4 bytes 732b00b0
+ 00bb8cec bytes 732b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc3fac923304c7c4193ae4ab5ec1b894"></a>

### [`00bb88fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb88fc.md) → [`00bb8d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8d24.md) _ZN8firebase9messaging18firebase_messaging10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb8d54",
      "incomplete_value": true,
      "site": "00bb8d54",
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
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb892c",
      "incomplete_value": true,
      "site": "00bb892c",
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
            "const:ea8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb8d38",
      "incomplete_value": true,
      "site": "00bb8d38",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb8910",
      "incomplete_value": true,
      "site": "00bb8910",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb8d40",
      "incomplete_value": false,
      "site": "00bb8d4c",
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
            "const:e9e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8918",
      "incomplete_value": false,
      "site": "00bb8924",
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
            "const:e5e:8"
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
      "00bb8d34",
      "READ",
      [
        "storage",
        "01125ea8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8d40",
      "PARAM",
      [
        "storage",
        "002bae5e",
        null,
        "string"
      ]
    ],
    [
      "00bb8d54",
      "WRITE",
      [
        "storage",
        "01125ea8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb8d34",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8d40",
      "PARAM",
      [
        "storage",
        "002bae9e",
        null,
        "string"
      ]
    ],
    [
      "00bb8d54",
      "WRITE",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb88fc.md#insn-00bb8924) · [`00bb892c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb88fc.md#insn-00bb892c) · [`00bb8908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb88fc.md#insn-00bb8908)
- 新版 `00bb8d4c`（命令位置の公開資料なし） · `00bb8d54`（命令位置の公開資料なし） · `00bb8d30`（命令位置の公開資料なし）

~~~diff
- 00bb8924 ["INT_ADD", "register:40f0:8", ["const:bb8924:8", "const:4:8"]]
- 00bb8924 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bb8d4c ["INT_ADD", "register:40f0:8", ["const:bb8d4c:8", "const:4:8"]]
+ 00bb8d4c ["CALL", null, ["callee:00c5af10:8"]]
- 00bb8924 bytes 7b880294
+ 00bb8d4c bytes 71880294
- 00bb892c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ea8:8"]]
- 00bb892c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb8d54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a8:8"]]
+ 00bb8d54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb892c bytes 605607f9
+ 00bb8d54 bytes 605601f9
- 00bb8908 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00bb8d30 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bb8908 bytes 732b00b0
+ 00bb8d30 bytes 732b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca47bce9b6890d9aa2ef2487bcce2c8f"></a>

### [`00bb894c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb894c.md) → [`00bb8d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8d74.md) _ZN8firebase9messaging18firebase_messaging15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb8dcc",
      "incomplete_value": true,
      "site": "00bb8dcc",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb89a4",
      "incomplete_value": true,
      "site": "00bb89a4",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb8da8",
      "incomplete_value": true,
      "site": "00bb8db4",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:2a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8980",
      "incomplete_value": true,
      "site": "00bb898c",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:ea8:8"
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
      "00bb8d88",
      "READ",
      [
        "storage",
        "01125eb0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb8da8",
      "READ",
      [
        "storage",
        "01125ea8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8dcc",
      "WRITE",
      [
        "storage",
        "01125eb0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb8d88",
      "READ",
      [
        "storage",
        "011262b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb8da8",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8dcc",
      "WRITE",
      [
        "storage",
        "011262b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb898c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb894c.md#insn-00bb898c) · [`00bb89a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb894c.md#insn-00bb89a4) · [`00bb895c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb894c.md#insn-00bb895c)
- 新版 `00bb8db4`（命令位置の公開資料なし） · `00bb8dcc`（命令位置の公開資料なし） · `00bb8d84`（命令位置の公開資料なし）

~~~diff
- 00bb898c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb898c ["INT_ADD", "register:40f0:8", ["const:bb898c:8", "const:4:8"]]
- 00bb898c ["CALLIND", null, ["register:0:8"]]
+ 00bb8db4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb8db4 ["INT_ADD", "register:40f0:8", ["const:bb8db4:8", "const:4:8"]]
+ 00bb8db4 ["CALLIND", null, ["register:0:8"]]
- 00bb898c bytes 00013fd6
+ 00bb8db4 bytes 00013fd6
- 00bb89a4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bb89a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:eb0:8"]]
- 00bb89a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bb8dcc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bb8dcc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:2b0:8"]]
+ 00bb8dcc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bb89a4 bytes a0c23a39
+ 00bb8dcc bytes a0c20a39
- 00bb895c ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00bb8d84 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bb895c bytes 752b00b0
+ 00bb8d84 bytes 752b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cce9fd14c394e9984a40e809a4db7e22"></a>

### [`00bb89b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb89b8.md) → [`00bb8de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8de0.md) _ZN8firebase9messaging18firebase_messaging12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb8e1c",
      "incomplete_value": true,
      "site": "00bb8e1c",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb89f4",
      "incomplete_value": true,
      "site": "00bb89f4",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb8e3c",
      "incomplete_value": true,
      "site": "00bb8e3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8a14",
      "incomplete_value": true,
      "site": "00bb8a14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb8df8",
      "incomplete_value": true,
      "site": "00bb8df8",
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
      "definition_site": "00bb89d0",
      "incomplete_value": true,
      "site": "00bb89d0",
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
      "00bb8df4",
      "READ",
      [
        "storage",
        "01125ea8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8e00",
      "READ",
      [
        "storage",
        "01125eb0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb8e1c",
      "WRITE",
      [
        "storage",
        "01125eb0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb8df4",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8e00",
      "READ",
      [
        "storage",
        "011262b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb8e1c",
      "WRITE",
      [
        "storage",
        "011262b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb89f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb89b8.md#insn-00bb89f4) · [`00bb8a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb89b8.md#insn-00bb8a10) · [`00bb8a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb89b8.md#insn-00bb8a14)
- 新版 `00bb8e1c`（命令位置の公開資料なし） · `00bb8e38`（命令位置の公開資料なし） · `00bb8e3c`（命令位置の公開資料なし）

~~~diff
- 00bb89f4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bb89f4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bb89f4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:eb0:8"]]
- 00bb89f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bb8e1c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bb8e1c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bb8e1c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:2b0:8"]]
+ 00bb8e1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bb89f4 bytes bfc23a39
+ 00bb8e1c bytes bfc20a39
- 00bb8a10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb8a10 ["INT_ADD", "register:40f0:8", ["const:bb8a10:8", "const:4:8"]]
- 00bb8a10 ["CALLIND", null, ["register:0:8"]]
+ 00bb8e38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb8e38 ["INT_ADD", "register:40f0:8", ["const:bb8e38:8", "const:4:8"]]
+ 00bb8e38 ["CALLIND", null, ["register:0:8"]]
- 00bb8a10 bytes 00013fd6
+ 00bb8e38 bytes 00013fd6
- 00bb8a14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ea8:8"]]
- 00bb8a14 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bb8a14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bb8e3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2a8:8"]]
+ 00bb8e3c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bb8e3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bb8a14 bytes 9f5607f9
+ 00bb8e3c bytes 9f5601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-953f0925640e2eddd8d1d98089f32392"></a>

### [`00bb8a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8a28.md) → [`00bb8e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8e50.md) _ZN8firebase9messaging18firebase_messaging14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8a68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb8e90"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8a44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb8a3c",
      "READ",
      [
        "storage",
        "01125ea8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bb8a44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8e94"
      ]
    ],
    [
      "unmatched:00bb8a4c",
      "PARAM",
      [
        "storage",
        "002bae5e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb8e64",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8e6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8e94"
      ]
    ],
    [
      "00bb8e74",
      "PARAM",
      [
        "storage",
        "002bae9e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8a28.md#insn-00bb8a44) · [`00bb8a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8a28.md#insn-00bb8a60) · [`00bb8a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8a28.md#insn-00bb8a68)
- 新版 `00bb8e88`（命令位置の公開資料なし）

~~~diff
- 00bb8a44 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bb8a44 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bb8a44 bytes 410100b5
- 00bb8a60 ["INT_ADD", "register:40f0:8", ["const:bb8a60:8", "const:4:8"]]
- 00bb8a60 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bb8e88 ["INT_ADD", "register:40f0:8", ["const:bb8e88:8", "const:4:8"]]
+ 00bb8e88 ["CALL", null, ["callee:00c5af10:8"]]
- 00bb8a60 bytes 2c880294
+ 00bb8e88 bytes 22880294
- 00bb8a68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ea8:8"]]
- 00bb8a68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8a68 bytes 805607f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de1f6de19eed608669a815724e3db8e2"></a>

### [`00bb8a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8a98.md) → [`00bb8ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8ec0.md) _ZN8firebase9messaging18firebase_messaging11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb8edc",
      "incomplete_value": false,
      "site": "00bb8ee0",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8ab4",
      "incomplete_value": false,
      "site": "00bb8ab8",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bb8eec",
      "incomplete_value": true,
      "site": "00bb8ef8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8ac4",
      "incomplete_value": true,
      "site": "00bb8ad0",
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
              "INT_LEFT"
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
      "00bb8edc",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bb8eec",
      "DATA",
      [
        "storage",
        "01125eb8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb8edc",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bb8eec",
      "DATA",
      [
        "storage",
        "011262b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8a98.md#insn-00bb8ab8) · [`00bb8ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8a98.md#insn-00bb8ab4) · [`00bb8abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8a98.md#insn-00bb8abc)
- 新版 `00bb8ee0`（命令位置の公開資料なし） · `00bb8edc`（命令位置の公開資料なし） · `00bb8ee4`（命令位置の公開資料なし）

~~~diff
- 00bb8ab8 ["INT_ADD", "register:40f0:8", ["const:bb8ab8:8", "const:4:8"]]
- 00bb8ab8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bb8ee0 ["INT_ADD", "register:40f0:8", ["const:bb8ee0:8", "const:4:8"]]
+ 00bb8ee0 ["CALL", null, ["callee:00c5b000:8"]]
- 00bb8ab8 bytes 52880294
+ 00bb8ee0 bytes 48880294
- 00bb8ab4 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bb8ab4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb8ab4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb8ab4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb8edc ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bb8edc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb8edc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb8edc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb8ab4 bytes 00680a91
+ 00bb8edc bytes 009c0d91
- 00bb8abc ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00bb8ee4 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bb8abc bytes 682b00b0
+ 00bb8ee4 bytes 682b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c5187c9baa11d44f4b15a34399942a4"></a>

### [`00bb8ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8ad4.md) → [`00bb8efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8efc.md) _ZN8firebase9messaging18firebase_messaging13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8b14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb8f3c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8af0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb8ae8",
      "READ",
      [
        "storage",
        "01125ea8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bb8af0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8f40"
      ]
    ],
    [
      "unmatched:00bb8af8",
      "PARAM",
      [
        "storage",
        "002bae5e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb8f10",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8f18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8f40"
      ]
    ],
    [
      "00bb8f20",
      "PARAM",
      [
        "storage",
        "002bae9e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8ad4.md#insn-00bb8af0) · [`00bb8b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8ad4.md#insn-00bb8b0c) · [`00bb8b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8ad4.md#insn-00bb8b14)
- 新版 `00bb8f34`（命令位置の公開資料なし）

~~~diff
- 00bb8af0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bb8af0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bb8af0 bytes 410100b5
- 00bb8b0c ["INT_ADD", "register:40f0:8", ["const:bb8b0c:8", "const:4:8"]]
- 00bb8b0c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bb8f34 ["INT_ADD", "register:40f0:8", ["const:bb8f34:8", "const:4:8"]]
+ 00bb8f34 ["CALL", null, ["callee:00c5af10:8"]]
- 00bb8b0c bytes 01880294
+ 00bb8f34 bytes f7870294
- 00bb8b14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ea8:8"]]
- 00bb8b14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8b14 bytes 805607f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92956f1412059bc233cbb42fd24442db"></a>

### [`00bb8b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8b80.md) → [`00bb8fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8fa8.md) _ZN8firebase9messaging27registration_intent_service19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb8fd4",
      "incomplete_value": true,
      "site": "00bb8fd4",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8bac",
      "incomplete_value": true,
      "site": "00bb8bac",
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
            "const:f18:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb8fbc",
      "incomplete_value": true,
      "site": "00bb8fbc",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb8b94",
      "incomplete_value": true,
      "site": "00bb8b94",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb8fc8",
      "incomplete_value": false,
      "site": "00bb8fcc",
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
            "const:b77:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8ba0",
      "incomplete_value": false,
      "site": "00bb8ba4",
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
            "const:b37:8"
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
      "00bb8fb8",
      "READ",
      [
        "storage",
        "01125f18",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8fc8",
      "PARAM",
      [
        "storage",
        "002b9b37",
        null,
        "string"
      ]
    ],
    [
      "00bb8fd4",
      "WRITE",
      [
        "storage",
        "01125f18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb8fb8",
      "READ",
      [
        "storage",
        "01126318",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8fc8",
      "PARAM",
      [
        "storage",
        "002b9b77",
        null,
        "string"
      ]
    ],
    [
      "00bb8fd4",
      "WRITE",
      [
        "storage",
        "01126318",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8b80.md#insn-00bb8ba4) · [`00bb8bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8b80.md#insn-00bb8bac) · [`00bb8b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8b80.md#insn-00bb8b8c)
- 新版 `00bb8fcc`（命令位置の公開資料なし） · `00bb8fd4`（命令位置の公開資料なし） · `00bb8fb4`（命令位置の公開資料なし）

~~~diff
- 00bb8ba4 ["INT_ADD", "register:40f0:8", ["const:bb8ba4:8", "const:4:8"]]
- 00bb8ba4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bb8fcc ["INT_ADD", "register:40f0:8", ["const:bb8fcc:8", "const:4:8"]]
+ 00bb8fcc ["CALL", null, ["callee:00c5af10:8"]]
- 00bb8ba4 bytes db870294
+ 00bb8fcc bytes d1870294
- 00bb8bac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f18:8"]]
- 00bb8bac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb8fd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:318:8"]]
+ 00bb8fd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8bac bytes 608e07f9
+ 00bb8fd4 bytes 608e01f9
- 00bb8b8c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00bb8fb4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bb8b8c bytes 732b00b0
+ 00bb8fb4 bytes 732b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cea993297c637f2511e8b3c3a19c722"></a>

### [`00bb8c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8c00.md) → [`00bb9028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9028.md) _ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb9058",
      "incomplete_value": true,
      "site": "00bb9058",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8c30",
      "incomplete_value": true,
      "site": "00bb8c30",
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
            "const:f18:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb903c",
      "incomplete_value": true,
      "site": "00bb903c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb8c14",
      "incomplete_value": true,
      "site": "00bb8c14",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb9048",
      "incomplete_value": false,
      "site": "00bb9050",
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
            "const:b77:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8c20",
      "incomplete_value": false,
      "site": "00bb8c28",
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
            "const:b37:8"
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
      "00bb9038",
      "READ",
      [
        "storage",
        "01125f18",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9048",
      "PARAM",
      [
        "storage",
        "002b9b37",
        null,
        "string"
      ]
    ],
    [
      "00bb9058",
      "WRITE",
      [
        "storage",
        "01125f18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb9038",
      "READ",
      [
        "storage",
        "01126318",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9048",
      "PARAM",
      [
        "storage",
        "002b9b77",
        null,
        "string"
      ]
    ],
    [
      "00bb9058",
      "WRITE",
      [
        "storage",
        "01126318",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8c00.md#insn-00bb8c28) · [`00bb8c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8c00.md#insn-00bb8c30) · [`00bb8c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8c00.md#insn-00bb8c0c)
- 新版 `00bb9050`（命令位置の公開資料なし） · `00bb9058`（命令位置の公開資料なし） · `00bb9034`（命令位置の公開資料なし）

~~~diff
- 00bb8c28 ["INT_ADD", "register:40f0:8", ["const:bb8c28:8", "const:4:8"]]
- 00bb8c28 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bb9050 ["INT_ADD", "register:40f0:8", ["const:bb9050:8", "const:4:8"]]
+ 00bb9050 ["CALL", null, ["callee:00c5af10:8"]]
- 00bb8c28 bytes ba870294
+ 00bb9050 bytes b0870294
- 00bb8c30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f18:8"]]
- 00bb8c30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb9058 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:318:8"]]
+ 00bb9058 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8c30 bytes 608e07f9
+ 00bb9058 bytes 608e01f9
- 00bb8c0c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00bb9034 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bb8c0c bytes 732b00b0
+ 00bb9034 bytes 732b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77da4a1ee1682cfb64829660f6d7265f"></a>

### [`00bb8c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8c44.md) → [`00bb906c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb906c.md) _ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8c74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb909c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8c58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb8c54",
      "READ",
      [
        "storage",
        "01125f18",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bb8c58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb90a0"
      ]
    ],
    [
      "unmatched:00bb8c60",
      "PARAM",
      [
        "storage",
        "002b9b37",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb907c",
      "READ",
      [
        "storage",
        "01126318",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9080",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb90a0"
      ]
    ],
    [
      "00bb9088",
      "PARAM",
      [
        "storage",
        "002b9b77",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8c44.md#insn-00bb8c58) · [`00bb8c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8c44.md#insn-00bb8c6c) · [`00bb8c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8c44.md#insn-00bb8c74)
- 新版 `00bb9094`（命令位置の公開資料なし）

~~~diff
- 00bb8c58 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bb8c58 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bb8c58 bytes 080100b5
- 00bb8c6c ["INT_ADD", "register:40f0:8", ["const:bb8c6c:8", "const:4:8"]]
- 00bb8c6c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bb9094 ["INT_ADD", "register:40f0:8", ["const:bb9094:8", "const:4:8"]]
+ 00bb9094 ["CALL", null, ["callee:00c5af10:8"]]
- 00bb8c6c bytes a9870294
+ 00bb9094 bytes 9f870294
- 00bb8c74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f18:8"]]
- 00bb8c74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8c74 bytes 608e07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a5c420fe57b9dc2ec9b55f82c91a5fd"></a>

### [`00bb8c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8c94.md) → [`00bb90bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb90bc.md) _ZN8firebase9messaging27registration_intent_service15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.96% / 新版 62.96%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8c94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8c98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8c98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb8c94",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb8c98",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb8c9c",
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
      "00bb90bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bb90c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb90c4",
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

- 旧版 [`00bb8c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8c94.md#insn-00bb8c94) · [`00bb8c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8c94.md#insn-00bb8c98) · [`00bb8c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8c94.md#insn-00bb8c9c)

~~~diff
- 00bb8c94 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bb8c94 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bb8c94 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb8c94 bytes f50f1df8
- 00bb8c98 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb8c98 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb8c98 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb8c98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb8c98 bytes f44f01a9
- 00bb8c9c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb8c9c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb8c9c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bb8c9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb8c9c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-245a3b0a5b99039b943e5656504a0dca"></a>

### [`00bb8d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8d00.md) → [`00bb9128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9128.md) _ZN8firebase9messaging27registration_intent_service12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8d3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb9184",
      "incomplete_value": true,
      "site": "00bb9184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8d5c",
      "incomplete_value": true,
      "site": "00bb8d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb9164"
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
      "00bb913c",
      "READ",
      [
        "storage",
        "01125f18",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9148",
      "READ",
      [
        "storage",
        "01125f20",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bb8d3c",
      "WRITE",
      [
        "storage",
        "01125f20",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb913c",
      "READ",
      [
        "storage",
        "01126318",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9148",
      "READ",
      [
        "storage",
        "01126320",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9164",
      "WRITE",
      [
        "storage",
        "01126320",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8d00.md#insn-00bb8d18) · [`00bb8d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8d00.md#insn-00bb8d38) · [`00bb8d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8d00.md#insn-00bb8d3c)
- 新版 `00bb9140`（命令位置の公開資料なし）

~~~diff
- 00bb8d18 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bb8d18 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bb9140 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bb9140 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bb8d18 bytes 410200b4
+ 00bb9140 bytes 410200b4
- 00bb8d38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb8d38 ["INT_ADD", "register:40f0:8", ["const:bb8d38:8", "const:4:8"]]
- 00bb8d38 ["CALLIND", null, ["register:0:8"]]
- 00bb8d38 bytes 00013fd6
- 00bb8d3c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bb8d3c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bb8d3c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:f20:8"]]
- 00bb8d3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bb8d3c bytes bf823c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c7f973739d8886f2da4d2b4afe3b88c"></a>

### [`00bb8d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8d70.md) → [`00bb9198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9198.md) _ZN8firebase9messaging27registration_intent_service14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8d70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8d70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8d74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb8d70",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb8d74",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb8d84",
      "READ",
      [
        "storage",
        "01125f18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb9198",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb919c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb91ac",
      "READ",
      [
        "storage",
        "01126318",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8d70.md#insn-00bb8d70) · [`00bb8d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8d70.md#insn-00bb8d74) · [`00bb8d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8d70.md#insn-00bb8d8c)

~~~diff
- 00bb8d70 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb8d70 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb8d70 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb8d70 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb8d70 bytes f44fbea9
- 00bb8d74 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb8d74 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb8d74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb8d74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb8d74 bytes fd7b01a9
- 00bb8d8c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bb8d8c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bb8d8c bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd3698b1e09fa94f516b5eb2880b96fd"></a>

### [`00bb8e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8e1c.md) → [`00bb9244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9244.md) _ZN8firebase9messaging27registration_intent_service13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8e5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb9284"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8e38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb8e30",
      "READ",
      [
        "storage",
        "01125f18",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bb8e38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb9288"
      ]
    ],
    [
      "unmatched:00bb8e40",
      "PARAM",
      [
        "storage",
        "002b9b37",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb9258",
      "READ",
      [
        "storage",
        "01126318",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9260",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb9288"
      ]
    ],
    [
      "00bb9268",
      "PARAM",
      [
        "storage",
        "002b9b77",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8e1c.md#insn-00bb8e38) · [`00bb8e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8e1c.md#insn-00bb8e54) · [`00bb8e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8e1c.md#insn-00bb8e5c)
- 新版 `00bb927c`（命令位置の公開資料なし）

~~~diff
- 00bb8e38 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bb8e38 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bb8e38 bytes 410100b5
- 00bb8e54 ["INT_ADD", "register:40f0:8", ["const:bb8e54:8", "const:4:8"]]
- 00bb8e54 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bb927c ["INT_ADD", "register:40f0:8", ["const:bb927c:8", "const:4:8"]]
+ 00bb927c ["CALL", null, ["callee:00c5af10:8"]]
- 00bb8e54 bytes 2f870294
+ 00bb927c bytes 25870294
- 00bb8e5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f18:8"]]
- 00bb8e5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8e5c bytes 808e07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ae26c967a929bc53fc5091765841ef3"></a>

### [`00bb8f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8f08.md) → [`00bb9330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9330.md) _ZN8firebase9messaging26illegal_argument_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8f08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8f0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8f0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb8f08",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb8f0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb9340",
      "READ",
      [
        "storage",
        "01125f38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb9330",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb9334",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb9340",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8f08.md#insn-00bb8f08) · [`00bb8f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8f08.md#insn-00bb8f0c) · [`00bb8f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8f08.md#insn-00bb8f1c)
- 新版 `00bb9344`（命令位置の公開資料なし）

~~~diff
- 00bb8f08 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bb8f08 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb8f08 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb8f08 bytes f30f1ef8
- 00bb8f0c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb8f0c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb8f0c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb8f0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb8f0c bytes fd7b01a9
- 00bb8f1c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bb8f1c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bb9344 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bb9344 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bb8f1c bytes e80000b5
+ 00bb9344 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d115c5a85f6a2fc3a7996d0ad3e3a243"></a>

### [`00bb8f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8f48.md) → [`00bb9370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9370.md) _ZN8firebase9messaging26illegal_argument_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb93a0",
      "incomplete_value": true,
      "site": "00bb93a0",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8f78",
      "incomplete_value": true,
      "site": "00bb8f78",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb9384",
      "incomplete_value": true,
      "site": "00bb9384",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb8f5c",
      "incomplete_value": true,
      "site": "00bb8f5c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb9390",
      "incomplete_value": false,
      "site": "00bb9398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:f14:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8f68",
      "incomplete_value": false,
      "site": "00bb8f70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:e38:8"
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
      "00bb9380",
      "READ",
      [
        "storage",
        "01125f38",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9390",
      "PARAM",
      [
        "storage",
        "002a4e38",
        null,
        "string"
      ]
    ],
    [
      "00bb93a0",
      "WRITE",
      [
        "storage",
        "01125f38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb9380",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9390",
      "PARAM",
      [
        "storage",
        "002a4f14",
        null,
        "string"
      ]
    ],
    [
      "00bb93a0",
      "WRITE",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8f48.md#insn-00bb8f70) · [`00bb8f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8f48.md#insn-00bb8f78) · [`00bb8f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8f48.md#insn-00bb8f54)
- 新版 `00bb9398`（命令位置の公開資料なし） · `00bb93a0`（命令位置の公開資料なし） · `00bb937c`（命令位置の公開資料なし）

~~~diff
- 00bb8f70 ["INT_ADD", "register:40f0:8", ["const:bb8f70:8", "const:4:8"]]
- 00bb8f70 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bb9398 ["INT_ADD", "register:40f0:8", ["const:bb9398:8", "const:4:8"]]
+ 00bb9398 ["CALL", null, ["callee:00c5af10:8"]]
- 00bb8f70 bytes e8860294
+ 00bb9398 bytes de860294
- 00bb8f78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f38:8"]]
- 00bb8f78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb93a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:338:8"]]
+ 00bb93a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8f78 bytes 609e07f9
+ 00bb93a0 bytes 609e01f9
- 00bb8f54 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00bb937c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bb8f54 bytes 732b00b0
+ 00bb937c bytes 732b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-504d28add8111266ae8485c350acc928"></a>

### [`00bb8f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8f8c.md) → [`00bb93b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb93b4.md) _ZN8firebase9messaging26illegal_argument_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8fbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb93e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb93c8",
      "incomplete_value": true,
      "site": "00bb93c8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb8fa0",
      "incomplete_value": true,
      "site": "00bb8fa0",
      "value": [
        "INT_NOTEQUAL",
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
      "00bb93c4",
      "READ",
      [
        "storage",
        "01125f38",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bb8fa8",
      "PARAM",
      [
        "storage",
        "002a4e38",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bb8fbc",
      "WRITE",
      [
        "storage",
        "01125f38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb93c4",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb93d0",
      "PARAM",
      [
        "storage",
        "002a4f14",
        null,
        "string"
      ]
    ],
    [
      "00bb93e4",
      "WRITE",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8f8c.md#insn-00bb8fa0) · [`00bb8fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8f8c.md#insn-00bb8fb4) · [`00bb8fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8f8c.md#insn-00bb8fbc)
- 新版 `00bb93c8`（命令位置の公開資料なし） · `00bb93dc`（命令位置の公開資料なし）

~~~diff
- 00bb8fa0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bb8fa0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bb93c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bb93c8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bb8fa0 bytes 080100b5
+ 00bb93c8 bytes 080100b5
- 00bb8fb4 ["INT_ADD", "register:40f0:8", ["const:bb8fb4:8", "const:4:8"]]
- 00bb8fb4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bb93dc ["INT_ADD", "register:40f0:8", ["const:bb93dc:8", "const:4:8"]]
+ 00bb93dc ["CALL", null, ["callee:00c5af10:8"]]
- 00bb8fb4 bytes d7860294
+ 00bb93dc bytes cd860294
- 00bb8fbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f38:8"]]
- 00bb8fbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8fbc bytes 609e07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59cd79a127112a305f45ad646bb91b91"></a>

### [`00bb90b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb90b8.md) → [`00bb94e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb94e0.md) _ZN8firebase9messaging26illegal_argument_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb9520",
      "incomplete_value": true,
      "site": "00bb9520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb90f8",
      "incomplete_value": true,
      "site": "00bb90f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb94fc",
      "incomplete_value": true,
      "site": "00bb94fc",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb90d4",
      "incomplete_value": true,
      "site": "00bb90d4",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb9504",
      "incomplete_value": false,
      "site": "00bb9518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:f14:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb90dc",
      "incomplete_value": false,
      "site": "00bb90f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:e38:8"
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
      "00bb94f4",
      "READ",
      [
        "storage",
        "01125f38",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9504",
      "PARAM",
      [
        "storage",
        "002a4e38",
        null,
        "string"
      ]
    ],
    [
      "00bb9520",
      "WRITE",
      [
        "storage",
        "01125f38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb94f4",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9504",
      "PARAM",
      [
        "storage",
        "002a4f14",
        null,
        "string"
      ]
    ],
    [
      "00bb9520",
      "WRITE",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb90f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb90b8.md#insn-00bb90f0) · [`00bb90f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb90b8.md#insn-00bb90f8) · [`00bb90c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb90b8.md#insn-00bb90c4)
- 新版 `00bb9518`（命令位置の公開資料なし） · `00bb9520`（命令位置の公開資料なし） · `00bb94ec`（命令位置の公開資料なし）

~~~diff
- 00bb90f0 ["INT_ADD", "register:40f0:8", ["const:bb90f0:8", "const:4:8"]]
- 00bb90f0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bb9518 ["INT_ADD", "register:40f0:8", ["const:bb9518:8", "const:4:8"]]
+ 00bb9518 ["CALL", null, ["callee:00c5af10:8"]]
- 00bb90f0 bytes 88860294
+ 00bb9518 bytes 7e860294
- 00bb90f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f38:8"]]
- 00bb90f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb9520 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:338:8"]]
+ 00bb9520 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb90f8 bytes 809e07f9
+ 00bb9520 bytes 809e01f9
- 00bb90c4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00bb94ec ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bb90c4 bytes 742b0090
+ 00bb94ec bytes 742b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3511d2c8d89cebc4fecf669f39d95ce"></a>

### [`00bb9128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9128.md) → [`00bb9550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9550.md) _ZN8firebase9messaging26illegal_argument_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb956c",
      "incomplete_value": false,
      "site": "00bb9570",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9144",
      "incomplete_value": false,
      "site": "00bb9148",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bb957c",
      "incomplete_value": true,
      "site": "00bb9588",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9154",
      "incomplete_value": true,
      "site": "00bb9160",
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
              "INT_LEFT"
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
      "00bb956c",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bb957c",
      "DATA",
      [
        "storage",
        "01125f48",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb956c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bb957c",
      "DATA",
      [
        "storage",
        "01126348",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9128.md#insn-00bb9148) · [`00bb9144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9128.md#insn-00bb9144) · [`00bb914c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9128.md#insn-00bb914c)
- 新版 `00bb9570`（命令位置の公開資料なし） · `00bb956c`（命令位置の公開資料なし） · `00bb9574`（命令位置の公開資料なし）

~~~diff
- 00bb9148 ["INT_ADD", "register:40f0:8", ["const:bb9148:8", "const:4:8"]]
- 00bb9148 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bb9570 ["INT_ADD", "register:40f0:8", ["const:bb9570:8", "const:4:8"]]
+ 00bb9570 ["CALL", null, ["callee:00c5b000:8"]]
- 00bb9148 bytes ae860294
+ 00bb9570 bytes a4860294
- 00bb9144 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00bb9144 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb9144 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb9144 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb956c ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00bb956c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb956c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb956c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb9144 bytes 00680a91
+ 00bb956c bytes 009c0d91
- 00bb914c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00bb9574 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bb914c bytes 682b0090
+ 00bb9574 bytes 682b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f7f9a6f7fa7c6898966517e34eb85c7"></a>

### [`00bb9164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9164.md) → [`00bb958c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb958c.md) _ZN8firebase9messaging26illegal_argument_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb95cc",
      "incomplete_value": true,
      "site": "00bb95cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb91a4",
      "incomplete_value": true,
      "site": "00bb91a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb95a8",
      "incomplete_value": true,
      "site": "00bb95a8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb9180",
      "incomplete_value": true,
      "site": "00bb9180",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bb95b0",
      "incomplete_value": false,
      "site": "00bb95c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:f14:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9188",
      "incomplete_value": false,
      "site": "00bb919c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:e38:8"
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
      "00bb95a0",
      "READ",
      [
        "storage",
        "01125f38",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb95b0",
      "PARAM",
      [
        "storage",
        "002a4e38",
        null,
        "string"
      ]
    ],
    [
      "00bb95cc",
      "WRITE",
      [
        "storage",
        "01125f38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb95a0",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb95b0",
      "PARAM",
      [
        "storage",
        "002a4f14",
        null,
        "string"
      ]
    ],
    [
      "00bb95cc",
      "WRITE",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb919c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9164.md#insn-00bb919c) · [`00bb91a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9164.md#insn-00bb91a4) · [`00bb9170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9164.md#insn-00bb9170)
- 新版 `00bb95c4`（命令位置の公開資料なし） · `00bb95cc`（命令位置の公開資料なし） · `00bb9598`（命令位置の公開資料なし）

~~~diff
- 00bb919c ["INT_ADD", "register:40f0:8", ["const:bb919c:8", "const:4:8"]]
- 00bb919c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bb95c4 ["INT_ADD", "register:40f0:8", ["const:bb95c4:8", "const:4:8"]]
+ 00bb95c4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bb919c bytes 5d860294
+ 00bb95c4 bytes 53860294
- 00bb91a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f38:8"]]
- 00bb91a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb95cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:338:8"]]
+ 00bb95cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb91a4 bytes 809e07f9
+ 00bb95cc bytes 809e01f9
- 00bb9170 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00bb9598 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bb9170 bytes 742b0090
+ 00bb9598 bytes 742b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8512bb71b2d0cb608414f8bf50f979b0"></a>

### [`00bb91d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb91d4.md) → [`00bb95fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb95fc.md) _ZN8firebase9messaging26illegal_argument_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9618",
      "incomplete_value": false,
      "site": "00bb961c",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb91f0",
      "incomplete_value": false,
      "site": "00bb91f4",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bb9628",
      "incomplete_value": true,
      "site": "00bb9634",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9200",
      "incomplete_value": true,
      "site": "00bb920c",
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
              "INT_LEFT"
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
      "00bb9618",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bb9628",
      "DATA",
      [
        "storage",
        "01125f50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb9618",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bb9628",
      "DATA",
      [
        "storage",
        "01126350",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb91f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb91d4.md#insn-00bb91f4) · [`00bb91f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb91d4.md#insn-00bb91f0) · [`00bb91f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb91d4.md#insn-00bb91f8)
- 新版 `00bb961c`（命令位置の公開資料なし） · `00bb9618`（命令位置の公開資料なし） · `00bb9620`（命令位置の公開資料なし）

~~~diff
- 00bb91f4 ["INT_ADD", "register:40f0:8", ["const:bb91f4:8", "const:4:8"]]
- 00bb91f4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bb961c ["INT_ADD", "register:40f0:8", ["const:bb961c:8", "const:4:8"]]
+ 00bb961c ["CALL", null, ["callee:00c5b000:8"]]
- 00bb91f4 bytes 83860294
+ 00bb961c bytes 79860294
- 00bb91f0 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00bb91f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb91f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb91f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb9618 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00bb9618 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb9618 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb9618 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb91f0 bytes 00441191
+ 00bb9618 bytes 00781491
- 00bb91f8 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00bb9620 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bb91f8 bytes 682b0090
+ 00bb9620 bytes 682b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b6885e772275f5962943bd453616ca3"></a>

### [`00bb9304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9304.md) → [`00bb972c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb972c.md) _ZN8firebase9messaging17NotifyListenerSetEPNS0_8ListenerE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00c5cef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cef0.md) · 呼出先 6件 [`00c593d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c593d0.md) [`00c59c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c00.md) [`00c59c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c90.md) [`00c59e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e60.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00c5d2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2f0.md) · 呼出先 6件 [`00c597d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c597d0.md) [`00c5a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a000.md) [`00c5a090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a090.md) [`00c5a260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a260.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 85.00% / 新版 80.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb9744",
      "incomplete_value": true,
      "site": "00bb9744",
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
      "definition_site": "00bb931c",
      "incomplete_value": true,
      "site": "00bb931c",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb97bc",
      "incomplete_value": true,
      "site": "00bb97bc",
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
      "definition_site": "00bb9394",
      "incomplete_value": true,
      "site": "00bb9394",
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9790",
      "incomplete_value": false,
      "site": "00bb9794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:137:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9368",
      "incomplete_value": false,
      "site": "00bb936c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:6a:8"
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
      "00bb9740",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb974c",
      "READ",
      [
        "storage",
        "01125f90",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9770",
      "READ",
      [
        "storage",
        "01125f68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb9740",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb974c",
      "READ",
      [
        "storage",
        "01126390",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9770",
      "READ",
      [
        "storage",
        "01126368",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb931c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9304.md#insn-00bb931c) · [`00bb936c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9304.md#insn-00bb936c) · [`00bb9388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9304.md#insn-00bb9388)
- 新版 `00bb9744`（命令位置の公開資料なし） · `00bb9794`（命令位置の公開資料なし） · `00bb97b0`（命令位置の公開資料なし）

~~~diff
- 00bb931c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bb931c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 00bb9744 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bb9744 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00bb931c bytes 080400b4
+ 00bb9744 bytes 080400b4
- 00bb936c ["INT_ADD", "register:40f0:8", ["const:bb936c:8", "const:4:8"]]
- 00bb936c ["CALL", null, ["callee:00c5a090:8"]]
+ 00bb9794 ["INT_ADD", "register:40f0:8", ["const:bb9794:8", "const:4:8"]]
+ 00bb9794 ["CALL", null, ["callee:00c5a090:8"]]
- 00bb936c bytes 49820294
+ 00bb9794 bytes 3f820294
- 00bb9388 ["INT_ADD", "register:40f0:8", ["const:bb9388:8", "const:4:8"]]
- 00bb9388 ["CALL", null, ["callee:00c597d0:8"]]
+ 00bb97b0 ["INT_ADD", "register:40f0:8", ["const:bb97b0:8", "const:4:8"]]
+ 00bb97b0 ["CALL", null, ["callee:00c597d0:8"]]
- 00bb9388 bytes 12800294
+ 00bb97b0 bytes 08800294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fedafd3a7c0d289b0670bf881e5748c6"></a>

### [`00bb93f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb93f0.md) → [`00bb9818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9818.md) _ZN8firebase9messaging17RequestPermissionEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9a0.md) [`00c5a9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9d0.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ada0.md) [`00c5add0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5add0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.25% / 新版 98.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb9844",
      "incomplete_value": true,
      "site": "00bb9844",
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
      "definition_site": "00bb941c",
      "incomplete_value": true,
      "site": "00bb941c",
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
      "definition_site": "00bb98c4",
      "incomplete_value": false,
      "site": "00bb98c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:915:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb949c",
      "incomplete_value": false,
      "site": "00bb94a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "00bb9840",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb98c4",
      "PARAM",
      [
        "storage",
        "002a2848",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb9840",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb98c4",
      "PARAM",
      [
        "storage",
        "002a2915",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb94a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb93f0.md#insn-00bb94a0) · [`00bb9414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb93f0.md#insn-00bb9414) · [`00bb9418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb93f0.md#insn-00bb9418)
- 新版 `00bb98c8`（命令位置の公開資料なし） · `00bb983c`（命令位置の公開資料なし） · `00bb9840`（命令位置の公開資料なし）

~~~diff
- 00bb94a0 ["INT_ADD", "register:40f0:8", ["const:bb94a0:8", "const:4:8"]]
- 00bb94a0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bb98c8 ["INT_ADD", "register:40f0:8", ["const:bb98c8:8", "const:4:8"]]
+ 00bb98c8 ["CALL", null, ["callee:00c5b000:8"]]
- 00bb94a0 bytes d8850294
+ 00bb98c8 bytes ce850294
- 00bb9414 ["COPY", "register:4048:8", ["const:1125000:8"]]
+ 00bb983c ["COPY", "register:4048:8", ["const:1126000:8"]]
- 00bb9414 bytes 692b0090
+ 00bb983c bytes 692b00b0
- 00bb9418 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f60:8"]]
- 00bb9418 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb9840 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:360:8"]]
+ 00bb9840 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb9418 bytes 29b147f9
+ 00bb9840 bytes 29b141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05949bdbf79258ee85ce6ebd16bc9259"></a>

### [`00bb9518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9518.md) → [`00bb9940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9940.md) _ZN8firebase9messaging27RequestPermissionLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d1b0.md) · 呼出先 8件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md)
- 新版 呼出元 1件 [`00c5d5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d5b0.md) · 呼出先 8件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_return_alignment

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb995c",
      "incomplete_value": true,
      "site": "00bb995c",
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
      "definition_site": "00bb9534",
      "incomplete_value": true,
      "site": "00bb9534",
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
      "definition_site": "00bb99b0",
      "incomplete_value": false,
      "site": "00bb99b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:915:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9588",
      "incomplete_value": false,
      "site": "00bb958c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bb959c",
      "incomplete_value": true,
      "site": "00bb95ac",
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
            "const:30:8"
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
      "00bb9954",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bb9588",
      "PARAM",
      [
        "storage",
        "002a2848",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb9954",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb99b0",
      "PARAM",
      [
        "storage",
        "002a2915",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9518.md#insn-00bb9534) · [`00bb958c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9518.md#insn-00bb958c) · [`00bb95ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9518.md#insn-00bb95ac)
- 新版 `00bb995c`（命令位置の公開資料なし） · `00bb99b4`（命令位置の公開資料なし） · `00bb99d4`（命令位置の公開資料なし）

~~~diff
- 00bb9534 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00bb9534 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bb995c ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00bb995c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bb9534 bytes 890200b4
+ 00bb995c bytes 890200b4
- 00bb958c ["INT_ADD", "register:40f0:8", ["const:bb958c:8", "const:4:8"]]
- 00bb958c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bb99b4 ["INT_ADD", "register:40f0:8", ["const:bb99b4:8", "const:4:8"]]
+ 00bb99b4 ["CALL", null, ["callee:00c5b000:8"]]
- 00bb958c bytes 9d850294
+ 00bb99b4 bytes 93850294
- 00bb95ac ["INT_ADD", "register:40f0:8", ["const:bb95ac:8", "const:4:8"]]
- 00bb95ac ["CALL", null, ["callee:00c5abe0:8"]]
+ 00bb99d4 ["INT_ADD", "register:40f0:8", ["const:bb99d4:8", "const:4:8"]]
+ 00bb99d4 ["CALL", null, ["callee:00c5abe0:8"]]
- 00bb95ac bytes 8d840294
+ 00bb99d4 bytes 83840294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11167c6cc9c4e650688040146628f1f2"></a>

### [`00bb95ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb95ec.md) → [`00bb9a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9a14.md) _ZN8firebase9messaging15ProcessMessagesEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d1a0.md) · 呼出先 41件 [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00bbcd2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcd2c.md) [`00bbcd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcd30.md)
- 新版 呼出元 1件 [`00c5d5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d5a0.md) · 呼出先 41件 [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00bbd154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd154.md) [`00bbd158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd158.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.43% / 新版 73.43%

CFGの説明率　旧版 23.81% / 新版 22.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 20件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 25件, `unresolved_store_alignment` 45件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb95ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb95ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb95f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb95ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb95f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb95f4",
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
      "00bb9a14",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00bb9a18",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bb9a1c",
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

- 旧版 [`00bb95ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb95ec.md#insn-00bb95ec) · [`00bb95f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb95ec.md#insn-00bb95f0) · [`00bb95f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb95ec.md#insn-00bb95f4)

~~~diff
- 00bb95ec ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00bb95ec ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00bb95ec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00bb95ec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb95ec bytes fc6fbaa9
- 00bb95f0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bb95f0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bb95f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb95f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb95f0 bytes fa6701a9
- 00bb95f4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bb95f4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bb95f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bb95f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb95f4 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54a602327d846ce49289282a5aa38553"></a>

### [`00bba200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba200.md) → [`00bba628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bba628.md) _ZN8firebase9messaging10InitializeERKNS_3AppEPNS0_8ListenerERKNS0_16MessagingOptionsE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d190.md) · 呼出先 33件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00b5a78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md) [`00bba728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba728.md) [`00bba7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba7e4.md)
- 新版 呼出元 1件 [`00c5d590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d590.md) · 呼出先 33件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00b5abb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5abb4.md) [`00bbab50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbab50.md) [`00bbac0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbac0c.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 59.47% / 新版 59.47%

CFGの説明率　旧版 26.47% / 新版 29.51%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 15件, `unresolved_store_alignment` 26件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba2d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba32c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba368"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bba678",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba684",
      "PARAM",
      [
        "storage",
        "002a3adc",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bba2ac",
      "READ",
      [
        "storage",
        "01125ea8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bba678",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba684",
      "PARAM",
      [
        "storage",
        "002a3ba9",
        null,
        "string"
      ]
    ],
    [
      "00bba6d4",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba200.md#insn-00bba2d4) · [`00bba32c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba200.md#insn-00bba32c) · [`00bba368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba200.md#insn-00bba368)

~~~diff
- 00bba2d4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:ea8:8"]]
- 00bba2d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bba2d4 bytes 005707f9
- 00bba32c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:f18:8"]]
- 00bba32c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bba32c bytes a08e07f9
- 00bba368 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:f60:8"]]
- 00bba368 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00bba368 bytes f4b207f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd1aa2b2f933333d43db120551999158"></a>

### [`00bba728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba728.md) → [`00bbab50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbab50.md) FUN_00bbab50

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bba200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba200.md) [`00bbac30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbac30.md) · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 2件 [`00bba628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bba628.md) [`00bbb058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb058.md) · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.72% / 新版 78.72%

CFGの説明率　旧版 76.92% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbab8c",
      "incomplete_value": true,
      "site": "00bbab8c",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba764",
      "incomplete_value": true,
      "site": "00bba764",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbabac",
      "incomplete_value": true,
      "site": "00bbabac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba784",
      "incomplete_value": true,
      "site": "00bba784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba7b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbab64",
      "READ",
      [
        "storage",
        "01125ea8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbab74",
      "READ",
      [
        "storage",
        "01125eb0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bbab8c",
      "WRITE",
      [
        "storage",
        "01125eb0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bbab64",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbab74",
      "READ",
      [
        "storage",
        "011262b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bbab8c",
      "WRITE",
      [
        "storage",
        "011262b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba728.md#insn-00bba764) · [`00bba780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba728.md#insn-00bba780) · [`00bba784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba728.md#insn-00bba784)
- 新版 `00bbab8c`（命令位置の公開資料なし） · `00bbaba8`（命令位置の公開資料なし） · `00bbabac`（命令位置の公開資料なし）

~~~diff
- 00bba764 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bba764 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bba764 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:eb0:8"]]
- 00bba764 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bbab8c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bbab8c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bbab8c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:2b0:8"]]
+ 00bbab8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bba764 bytes bfc23a39
+ 00bbab8c bytes bfc20a39
- 00bba780 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bba780 ["INT_ADD", "register:40f0:8", ["const:bba780:8", "const:4:8"]]
- 00bba780 ["CALLIND", null, ["register:0:8"]]
+ 00bbaba8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bbaba8 ["INT_ADD", "register:40f0:8", ["const:bbaba8:8", "const:4:8"]]
+ 00bbaba8 ["CALLIND", null, ["register:0:8"]]
- 00bba780 bytes 00013fd6
+ 00bbaba8 bytes 00013fd6
- 00bba784 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ea8:8"]]
- 00bba784 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bba784 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bbabac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2a8:8"]]
+ 00bbabac ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bbabac ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bba784 bytes 9f5607f9
+ 00bbabac bytes 9f5601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3126bb59f0f6132d09d91b270e67b7f"></a>

### [`00bba7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba7e4.md) → [`00bbac0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbac0c.md) FUN_00bbac0c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bba200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba200.md) · 呼出先 11件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00bba628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bba628.md) · 呼出先 11件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.47% / 新版 92.47%

CFGの説明率　旧版 90.32% / 新版 93.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbac4c",
      "incomplete_value": true,
      "site": "00bbac4c",
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
      "definition_site": "00bba824",
      "incomplete_value": true,
      "site": "00bba824",
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
      "definition_site": "00bbac38",
      "incomplete_value": false,
      "site": "00bbac40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba810",
      "incomplete_value": false,
      "site": "00bba818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1125000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "definition_site": "00bbac64",
      "incomplete_value": false,
      "site": "00bbac68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba83c",
      "incomplete_value": false,
      "site": "00bba840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1125000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "00bbac38",
      "PARAM",
      [
        "storage",
        "01125e58",
        null,
        null
      ]
    ],
    [
      "00bbac48",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbac64",
      "PARAM",
      [
        "storage",
        "01125e58",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bbac38",
      "PARAM",
      [
        "storage",
        "01126258",
        null,
        null
      ]
    ],
    [
      "00bbac48",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbac64",
      "PARAM",
      [
        "storage",
        "01126258",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba7e4.md#insn-00bba818) · [`00bba840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba7e4.md#insn-00bba840) · [`00bba80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba7e4.md#insn-00bba80c)
- 新版 `00bbac40`（命令位置の公開資料なし） · `00bbac68`（命令位置の公開資料なし） · `00bbac34`（命令位置の公開資料なし）

~~~diff
- 00bba818 ["INT_ADD", "register:40f0:8", ["const:bba818:8", "const:4:8"]]
- 00bba818 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bbac40 ["INT_ADD", "register:40f0:8", ["const:bbac40:8", "const:4:8"]]
+ 00bbac40 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bba818 bytes 7a7f0294
+ 00bbac40 bytes 707f0294
- 00bba840 ["INT_ADD", "register:40f0:8", ["const:bba840:8", "const:4:8"]]
- 00bba840 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bbac68 ["INT_ADD", "register:40f0:8", ["const:bbac68:8", "const:4:8"]]
+ 00bbac68 ["CALL", null, ["callee:00c5aa10:8"]]
- 00bba840 bytes 747f0294
+ 00bbac68 bytes 6a7f0294
- 00bba80c ["COPY", "register:4000:8", ["const:1125000:8"]]
+ 00bbac34 ["COPY", "register:4000:8", ["const:1126000:8"]]
- 00bba80c bytes 402b00f0
+ 00bbac34 bytes 602b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37e606e25e7f507f17918b94124832e5"></a>

### [`00bba97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba97c.md) → [`00bbada4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbada4.md) _ZN8firebase9messaging33SetTokenRegistrationOnInitEnabledEb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5a6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6e0.md) · 呼出先 6件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00bbab28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbab28.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5aae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aae0.md) · 呼出先 6件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00bbaf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbaf50.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 4件, `call_argument_candidate` 9件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbaea0",
      "incomplete_value": false,
      "site": "00bbaea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbaa78",
      "incomplete_value": false,
      "site": "00bbaa78",
      "value": [
        "leaf",
        "const:1126000:8"
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbadc4",
      "incomplete_value": true,
      "site": "00bbadc4",
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
      "definition_site": "00bba99c",
      "incomplete_value": true,
      "site": "00bba99c",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbadd8",
      "incomplete_value": true,
      "site": "00bbadd8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bba9b0",
      "incomplete_value": true,
      "site": "00bba9b0",
      "value": [
        "INT_NOTEQUAL",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbadbc",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbadd0",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbade0",
      "PARAM",
      [
        "storage",
        "002a2848",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbadbc",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbadd0",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbade0",
      "PARAM",
      [
        "storage",
        "002a2915",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba97c.md#insn-00bba9bc) · [`00bba9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba97c.md#insn-00bba9c8) · [`00bba9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba97c.md#insn-00bba9f0)
- 新版 `00bbade4`（命令位置の公開資料なし） · `00bbadf0`（命令位置の公開資料なし） · `00bbae18`（命令位置の公開資料なし）

~~~diff
- 00bba9bc ["INT_ADD", "register:40f0:8", ["const:bba9bc:8", "const:4:8"]]
- 00bba9bc ["CALL", null, ["callee:00c5aca0:8"]]
+ 00bbade4 ["INT_ADD", "register:40f0:8", ["const:bbade4:8", "const:4:8"]]
+ 00bbade4 ["CALL", null, ["callee:00c5aca0:8"]]
- 00bba9bc bytes b97f0294
+ 00bbade4 bytes af7f0294
- 00bba9c8 ["INT_ADD", "register:40f0:8", ["const:bba9c8:8", "const:4:8"]]
- 00bba9c8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bbadf0 ["INT_ADD", "register:40f0:8", ["const:bbadf0:8", "const:4:8"]]
+ 00bbadf0 ["CALL", null, ["callee:00c5b000:8"]]
- 00bba9c8 bytes 8e800294
+ 00bbadf0 bytes 84800294
- 00bba9f0 ["INT_ADD", "register:40f0:8", ["const:bba9f0:8", "const:4:8"]]
- 00bba9f0 ["CALL", null, ["callee:00497a48:8"]]
+ 00bbae18 ["INT_ADD", "register:40f0:8", ["const:bbae18:8", "const:4:8"]]
+ 00bbae18 ["CALL", null, ["callee:00497a48:8"]]
- 00bba9f0 bytes 0674e397
+ 00bbae18 bytes 0c73e397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-170594141238bfbe7ca3816f0c508d18"></a>

### [`00bbaabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbaabc.md) → [`00bbaee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbaee4.md) _ZN8firebase9messaging32IsTokenRegistrationOnInitEnabledEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 74.07% / 新版 74.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbaef8",
      "incomplete_value": true,
      "site": "00bbaef8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bbaad0",
      "incomplete_value": true,
      "site": "00bbaad0",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbaf18",
      "incomplete_value": true,
      "site": "00bbaf18",
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
      "definition_site": "00bbaaf0",
      "incomplete_value": true,
      "site": "00bbaaf0",
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
      "definition_site": "00bbaf00",
      "incomplete_value": false,
      "site": "00bbaf04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:915:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbaad8",
      "incomplete_value": false,
      "site": "00bbaadc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "00bbaef4",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbaf00",
      "PARAM",
      [
        "storage",
        "002a2848",
        null,
        "string"
      ]
    ],
    [
      "00bbaf0c",
      "PARAM",
      [
        "storage",
        "002b0737",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbaef4",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbaf00",
      "PARAM",
      [
        "storage",
        "002a2915",
        null,
        "string"
      ]
    ],
    [
      "00bbaf0c",
      "PARAM",
      [
        "storage",
        "002b0777",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbaadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbaabc.md#insn-00bbaadc) · [`00bbaae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbaabc.md#insn-00bbaae8) · [`00bbab08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbaabc.md#insn-00bbab08)
- 新版 `00bbaf04`（命令位置の公開資料なし） · `00bbaf10`（命令位置の公開資料なし） · `00bbaf30`（命令位置の公開資料なし）

~~~diff
- 00bbaadc ["INT_ADD", "register:40f0:8", ["const:bbaadc:8", "const:4:8"]]
- 00bbaadc ["CALL", null, ["callee:00c5aca0:8"]]
+ 00bbaf04 ["INT_ADD", "register:40f0:8", ["const:bbaf04:8", "const:4:8"]]
+ 00bbaf04 ["CALL", null, ["callee:00c5aca0:8"]]
- 00bbaadc bytes 717f0294
+ 00bbaf04 bytes 677f0294
- 00bbaae8 ["INT_ADD", "register:40f0:8", ["const:bbaae8:8", "const:4:8"]]
- 00bbaae8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bbaf10 ["INT_ADD", "register:40f0:8", ["const:bbaf10:8", "const:4:8"]]
+ 00bbaf10 ["CALL", null, ["callee:00c5b000:8"]]
- 00bbaae8 bytes 46800294
+ 00bbaf10 bytes 3c800294
- 00bbab08 ["INT_ADD", "register:40f0:8", ["const:bbab08:8", "const:4:8"]]
- 00bbab08 ["CALL", null, ["callee:00497a48:8"]]
+ 00bbaf30 ["INT_ADD", "register:40f0:8", ["const:bbaf30:8", "const:4:8"]]
+ 00bbaf30 ["CALL", null, ["callee:00497a48:8"]]
- 00bbab08 bytes c073e397
+ 00bbaf30 bytes c672e397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddea48c9cc1d39b80caa6f97399d8de4"></a>

### [`00bbab28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbab28.md) → [`00bbaf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbaf50.md) FUN_00bbaf50

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00bba200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba200.md) [`00bba97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba97c.md) · 呼出先 11件 [`0087b37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b37c.md) [`00bbcf4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcf4c.md) [`00bbcf64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcf64.md) [`00bbcf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcf70.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`00bba628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bba628.md) [`00bbada4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbada4.md) · 呼出先 11件 [`0087b3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b3bc.md) [`00bbd374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd374.md) [`00bbd38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd38c.md) [`00bbd398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd398.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.74% / 新版 90.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbafa0",
      "incomplete_value": false,
      "site": "00bbafa0",
      "value": [
        "leaf",
        "const:bbd398:8"
      ]
    },
    "old": {
      "definition_site": "00bbab78",
      "incomplete_value": false,
      "site": "00bbab78",
      "value": [
        "leaf",
        "const:bbcf70:8"
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbaf74",
      "incomplete_value": true,
      "site": "00bbaf74",
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
      "definition_site": "00bbab4c",
      "incomplete_value": true,
      "site": "00bbab4c",
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
      "definition_site": "00bbafc0",
      "incomplete_value": true,
      "site": "00bbafd4",
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbab98",
      "incomplete_value": true,
      "site": "00bbabac",
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
                "const:510:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbaf70",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbafa0",
      "DATA",
      [
        "storage",
        "00bbcf70",
        null,
        null
      ]
    ],
    [
      "00bbafc0",
      "READ",
      [
        "storage",
        "00c9b510",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bbaf70",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbafa0",
      "DATA",
      [
        "storage",
        "00bbd398",
        null,
        null
      ]
    ],
    [
      "00bbafc0",
      "READ",
      [
        "storage",
        "00c9b910",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbabac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbab28.md#insn-00bbabac) · [`00bbabcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbab28.md#insn-00bbabcc) · [`00bbabd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbab28.md#insn-00bbabd8)
- 新版 `00bbafd4`（命令位置の公開資料なし） · `00bbaff4`（命令位置の公開資料なし） · `00bbb000`（命令位置の公開資料なし）

~~~diff
- 00bbabac ["COPY", "register:0:8", ["register:4048:8"]]
- 00bbabac ["INT_ADD", "register:40f0:8", ["const:bbabac:8", "const:4:8"]]
- 00bbabac ["CALLIND", null, ["register:0:8"]]
+ 00bbafd4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bbafd4 ["INT_ADD", "register:40f0:8", ["const:bbafd4:8", "const:4:8"]]
+ 00bbafd4 ["CALLIND", null, ["register:0:8"]]
- 00bbabac bytes 20013fd6
+ 00bbafd4 bytes 20013fd6
- 00bbabcc ["INT_ADD", "register:40f0:8", ["const:bbabcc:8", "const:4:8"]]
- 00bbabcc ["CALL", null, ["callee:00c5aca0:8"]]
+ 00bbaff4 ["INT_ADD", "register:40f0:8", ["const:bbaff4:8", "const:4:8"]]
+ 00bbaff4 ["CALL", null, ["callee:00c5aca0:8"]]
- 00bbabcc bytes 357f0294
+ 00bbaff4 bytes 2b7f0294
- 00bbabd8 ["INT_ADD", "register:40f0:8", ["const:bbabd8:8", "const:4:8"]]
- 00bbabd8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bbb000 ["INT_ADD", "register:40f0:8", ["const:bbb000:8", "const:4:8"]]
+ 00bbb000 ["CALL", null, ["callee:00c5b000:8"]]
- 00bbabd8 bytes 0a800294
+ 00bbb000 bytes 00800294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d3b244a2972e918bddd4ad312a7d68a"></a>

### [`00bbac30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbac30.md) → [`00bbb058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb058.md) _ZN8firebase9messaging9TerminateEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d040.md) · 呼出先 23件 [`00bba728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bba728.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c593d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c593d0.md) [`00c59c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c00.md) [`00c59c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c90.md)
- 新版 呼出元 1件 [`00c5d440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d440.md) · 呼出先 23件 [`00bbab50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbab50.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c597d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c597d0.md) [`00c5a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a000.md) [`00c5a090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a090.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.50% / 新版 74.50%

CFGの説明率　旧版 65.75% / 新版 64.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 8件, `store_destination` 3件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 4件, `call_argument_candidate` 2件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbb0a8",
      "incomplete_value": true,
      "site": "00bbb0a8",
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
            "const:360:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbac80",
      "incomplete_value": true,
      "site": "00bbac80",
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
            "const:f60:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbad9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbb1e4",
      "incomplete_value": true,
      "site": "00bbb1e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbadbc",
      "incomplete_value": true,
      "site": "00bbadbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      "00bbb074",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb080",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb08c",
      "PARAM",
      [
        "storage",
        "0030e781",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbb074",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb080",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb08c",
      "PARAM",
      [
        "storage",
        "0030e7c1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbac30.md#insn-00bbac80) · [`00bbad9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbac30.md#insn-00bbad9c) · [`00bbada0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbac30.md#insn-00bbada0)
- 新版 `00bbb0a8`（命令位置の公開資料なし）

~~~diff
- 00bbac80 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:f60:8"]]
- 00bbac80 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bbac80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bbb0a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:360:8"]]
+ 00bbb0a8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bbb0a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bbac80 bytes bfb207f9
+ 00bbb0a8 bytes bfb201f9
- 00bbad9c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:f70:8"]]
- 00bbad9c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bbad9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bbad9c bytes bfba07f9
- 00bbada0 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00bbada0 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 00bbada0 bytes b40000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f23c2d3e91b7faf7af3b667ae1d1ffec"></a>

### [`00bbafa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbafa4.md) → [`00bbb3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb3cc.md) _ZN8firebase9messaging9SubscribeEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 18件 [`00bbb274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb274.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00bbb69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb69c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 94.20% / 新版 94.20%

CFGの説明率　旧版 44.00% / 新版 44.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbafcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bbb3f4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbb400",
      "incomplete_value": true,
      "site": "00bbb400",
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
      "definition_site": "00bbafd8",
      "incomplete_value": true,
      "site": "00bbafd8",
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
      "unmatched:00bbafcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bbb3fc",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb408",
      "READ",
      [
        "storage",
        "01125f70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbb3f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bbb3fc",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb408",
      "READ",
      [
        "storage",
        "01126370",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbafcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbafa4.md#insn-00bbafcc) · [`00bbafec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbafa4.md#insn-00bbafec) · [`00bbb014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbafa4.md#insn-00bbb014)
- 新版 `00bbb414`（命令位置の公開資料なし） · `00bbb43c`（命令位置の公開資料なし）

~~~diff
- 00bbafcc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bbafcc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 00bbafcc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bbafcc bytes a9831bf8
- 00bbafec ["INT_ADD", "register:40f0:8", ["const:bbafec:8", "const:4:8"]]
- 00bbafec ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bbb414 ["INT_ADD", "register:40f0:8", ["const:bbb414:8", "const:4:8"]]
+ 00bbb414 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bbafec bytes 857d0294
+ 00bbb414 bytes 7b7d0294
- 00bbb014 ["INT_ADD", "register:40f0:8", ["const:bbb014:8", "const:4:8"]]
- 00bbb014 ["CALL", null, ["callee:00c5ae00:8"]]
+ 00bbb43c ["INT_ADD", "register:40f0:8", ["const:bbb43c:8", "const:4:8"]]
+ 00bbb43c ["CALL", null, ["callee:00c5ae00:8"]]
- 00bbb014 bytes 7b7e0294
+ 00bbb43c bytes 717e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-570a63ef8c6289d2a021aaad17b81129"></a>

### [`00bbb274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb274.md) → [`00bbb69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb69c.md) FUN_00bbb69c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bbafa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbafa4.md) [`00bbcd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcd98.md) · 呼出先 14件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bbd038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd038.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00bbb3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb3cc.md) [`00bbd1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd1c0.md) · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bbd460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd460.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 54.55% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbb6c8",
      "incomplete_value": false,
      "site": "00bbb6d4",
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
            "const:3d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb2a0",
      "incomplete_value": false,
      "site": "00bbb2ac",
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
            "const:391:8"
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
      "definition_site": "00bbb6dc",
      "incomplete_value": true,
      "site": "00bbb6e0",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:360:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb2b4",
      "incomplete_value": true,
      "site": "00bbb2b8",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:f60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb2cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbb2a0",
      "PARAM",
      [
        "storage",
        "002ae391",
        null,
        "string"
      ]
    ],
    [
      "00bbb6dc",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bbb2d8",
      "READ",
      [
        "storage",
        "01125f98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbb6c8",
      "PARAM",
      [
        "storage",
        "002ae3d1",
        null,
        "string"
      ]
    ],
    [
      "00bbb6dc",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb700",
      "READ",
      [
        "storage",
        "01126398",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb274.md#insn-00bbb2ac) · [`00bbb2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb274.md#insn-00bbb2b8) · [`00bbb2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb274.md#insn-00bbb2cc)
- 新版 `00bbb6d4`（命令位置の公開資料なし） · `00bbb6e0`（命令位置の公開資料なし）

~~~diff
- 00bbb2ac ["INT_ADD", "register:40f0:8", ["const:bbb2ac:8", "const:4:8"]]
- 00bbb2ac ["CALL", null, ["callee:00c5b130:8"]]
+ 00bbb6d4 ["INT_ADD", "register:40f0:8", ["const:bbb6d4:8", "const:4:8"]]
+ 00bbb6d4 ["CALL", null, ["callee:00c5b130:8"]]
- 00bbb2ac bytes a17e0294
+ 00bbb6d4 bytes 977e0294
- 00bbb2b8 ["INT_ADD", "register:40f0:8", ["const:bbb2b8:8", "const:4:8"]]
- 00bbb2b8 ["CALL", null, ["callee:00c5b080:8"]]
+ 00bbb6e0 ["INT_ADD", "register:40f0:8", ["const:bbb6e0:8", "const:4:8"]]
+ 00bbb6e0 ["CALL", null, ["callee:00c5b080:8"]]
- 00bbb2b8 bytes 727e0294
+ 00bbb6e0 bytes 687e0294
- 00bbb2cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bbb2cc ["INT_ADD", "register:40f0:8", ["const:bbb2cc:8", "const:4:8"]]
- 00bbb2cc ["CALLIND", null, ["register:0:8"]]
- 00bbb2cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0abcb5e5c97d917f275a2a081c512b04"></a>

### [`00bbb470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb470.md) → [`00bbb898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb898.md) _ZN8firebase9messaging19SubscribeLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbb8b4",
      "incomplete_value": true,
      "site": "00bbb8b4",
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
      "definition_site": "00bbb48c",
      "incomplete_value": true,
      "site": "00bbb48c",
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
      "definition_site": "00bbb908",
      "incomplete_value": false,
      "site": "00bbb90c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:915:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb4e0",
      "incomplete_value": false,
      "site": "00bbb4e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bbb4f4",
      "incomplete_value": true,
      "site": "00bbb504",
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
            "const:30:8"
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
      "00bbb8ac",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb908",
      "PARAM",
      [
        "storage",
        "002a2848",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbb8ac",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb908",
      "PARAM",
      [
        "storage",
        "002a2915",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb470.md#insn-00bbb4e4) · [`00bbb504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb470.md#insn-00bbb504) · [`00bbb480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb470.md#insn-00bbb480)
- 新版 `00bbb90c`（命令位置の公開資料なし） · `00bbb92c`（命令位置の公開資料なし） · `00bbb8a8`（命令位置の公開資料なし）

~~~diff
- 00bbb4e4 ["INT_ADD", "register:40f0:8", ["const:bbb4e4:8", "const:4:8"]]
- 00bbb4e4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bbb90c ["INT_ADD", "register:40f0:8", ["const:bbb90c:8", "const:4:8"]]
+ 00bbb90c ["CALL", null, ["callee:00c5b000:8"]]
- 00bbb4e4 bytes c77d0294
+ 00bbb90c bytes bd7d0294
- 00bbb504 ["INT_ADD", "register:40f0:8", ["const:bbb504:8", "const:4:8"]]
- 00bbb504 ["CALL", null, ["callee:00c5abe0:8"]]
+ 00bbb92c ["INT_ADD", "register:40f0:8", ["const:bbb92c:8", "const:4:8"]]
+ 00bbb92c ["CALL", null, ["callee:00c5abe0:8"]]
- 00bbb504 bytes b77c0294
+ 00bbb92c bytes ad7c0294
- 00bbb480 ["COPY", "register:4048:8", ["const:1125000:8"]]
+ 00bbb8a8 ["COPY", "register:4048:8", ["const:1126000:8"]]
- 00bbb480 bytes 492b00d0
+ 00bbb8a8 bytes 492b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f28b6117c4204fd703dc65dba8236e3"></a>

### [`00bbb548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb548.md) → [`00bbb970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb970.md) _ZN8firebase9messaging11UnsubscribeEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 18件 [`00bbb818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb818.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00bbbc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbc40.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 40.00% / 新版 34.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb570"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb6a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bbb998"
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
      "unmatched:00bbb570",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbb578",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bbb57c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbba0c"
      ]
    ]
  ],
  "added": [
    [
      "00bbb998",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bbb9a0",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb9a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbba0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb548.md#insn-00bbb570) · [`00bbb57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb548.md#insn-00bbb57c) · [`00bbb590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb548.md#insn-00bbb590)
- 新版 `00bbb9b8`（命令位置の公開資料なし）

~~~diff
- 00bbb570 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bbb570 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 00bbb570 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bbb570 bytes a9831bf8
- 00bbb57c ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00bbb57c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bbb57c bytes 490300b4
- 00bbb590 ["INT_ADD", "register:40f0:8", ["const:bbb590:8", "const:4:8"]]
- 00bbb590 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bbb9b8 ["INT_ADD", "register:40f0:8", ["const:bbb9b8:8", "const:4:8"]]
+ 00bbb9b8 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bbb590 bytes 1c7c0294
+ 00bbb9b8 bytes 127c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2b08c1f98230ef6696bbd83249f3968"></a>

### [`00bbb818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb818.md) → [`00bbbc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbc40.md) FUN_00bbbc40

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bbb548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb548.md) [`00bbcd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcd98.md) · 呼出先 14件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bbd038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd038.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00bbb970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb970.md) [`00bbd1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd1c0.md) · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bbd460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd460.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.39% / 新版 87.39%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb84c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bbbc74"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb9b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbb844",
      "PARAM",
      [
        "storage",
        "002c0b53",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bbb84c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00bbbc80",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbbc6c",
      "PARAM",
      [
        "storage",
        "002c0b93",
        null,
        "string"
      ]
    ],
    [
      "00bbbc74",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00bbbc80",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb818.md#insn-00bbb84c) · [`00bbb850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb818.md#insn-00bbb850) · [`00bbb85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb818.md#insn-00bbb85c)
- 新版 `00bbbc78`（命令位置の公開資料なし） · `00bbbc84`（命令位置の公開資料なし）

~~~diff
- 00bbb84c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00bbb84c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bbb84c bytes e81f00f9
- 00bbb850 ["INT_ADD", "register:40f0:8", ["const:bbb850:8", "const:4:8"]]
- 00bbb850 ["CALL", null, ["callee:00c5b130:8"]]
+ 00bbbc78 ["INT_ADD", "register:40f0:8", ["const:bbbc78:8", "const:4:8"]]
+ 00bbbc78 ["CALL", null, ["callee:00c5b130:8"]]
- 00bbb850 bytes 387d0294
+ 00bbbc78 bytes 2e7d0294
- 00bbb85c ["INT_ADD", "register:40f0:8", ["const:bbb85c:8", "const:4:8"]]
- 00bbb85c ["CALL", null, ["callee:00c5b080:8"]]
+ 00bbbc84 ["INT_ADD", "register:40f0:8", ["const:bbbc84:8", "const:4:8"]]
+ 00bbbc84 ["CALL", null, ["callee:00c5b080:8"]]
- 00bbb85c bytes 097d0294
+ 00bbbc84 bytes ff7c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ced8486a7f651c88f75d667d155d1de9"></a>

### [`00bbba14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbba14.md) → [`00bbbe3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbe3c.md) _ZN8firebase9messaging21UnsubscribeLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_store_alignment

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbba14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbba14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbba18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbba14",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbba18",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbba1c",
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
      "00bbbe3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bbbe40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bbbe44",
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

- 旧版 [`00bbba14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbba14.md#insn-00bbba14) · [`00bbba18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbba14.md#insn-00bbba18) · [`00bbba1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbba14.md#insn-00bbba1c)

~~~diff
- 00bbba14 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bbba14 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bbba14 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bbba14 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbba14 bytes f657bda9
- 00bbba18 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbba18 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbba18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bbba18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbba18 bytes f44f01a9
- 00bbba1c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbba1c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbba1c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bbba1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbba1c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa64f912959307b30f8018a81004669b"></a>

### [`00bbbaec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbaec.md) → [`00bbbf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbf14.md) _ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbbf24",
      "incomplete_value": true,
      "site": "00bbbf24",
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
      "definition_site": "00bbbafc",
      "incomplete_value": true,
      "site": "00bbbafc",
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
      "definition_site": "00bbbf34",
      "incomplete_value": true,
      "site": "00bbbf3c",
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
                "const:1126000:8"
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
      "definition_site": "00bbbb0c",
      "incomplete_value": true,
      "site": "00bbbb14",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:f98:8"
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
      "definition_site": "00bbbf38",
      "incomplete_value": true,
      "site": "00bbbf3c",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:2e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbb10",
      "incomplete_value": true,
      "site": "00bbbb14",
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
                "const:1125000:8"
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
      "00bbbf20",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbbf24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bbbb28"
      ]
    ],
    [
      "unmatched:00bbbb0c",
      "READ",
      [
        "storage",
        "01125f98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbbf20",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbbf24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbbf50"
      ]
    ],
    [
      "00bbbf34",
      "READ",
      [
        "storage",
        "01126398",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbafc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbaec.md#insn-00bbbafc) · [`00bbbb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbaec.md#insn-00bbbb14) · [`00bbbb24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbaec.md#insn-00bbbb24)
- 新版 `00bbbf24`（命令位置の公開資料なし） · `00bbbf3c`（命令位置の公開資料なし）

~~~diff
- 00bbbafc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bbbafc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bbbf24 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00bbbf24 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bbbafc bytes 600100b4
+ 00bbbf24 bytes 600100b4
- 00bbbb14 ["INT_ADD", "register:40f0:8", ["const:bbbb14:8", "const:4:8"]]
- 00bbbb14 ["CALL", null, ["callee:00497a48:8"]]
+ 00bbbf3c ["INT_ADD", "register:40f0:8", ["const:bbbf3c:8", "const:4:8"]]
+ 00bbbf3c ["CALL", null, ["callee:00497a48:8"]]
- 00bbbb14 bytes bd6fe397
+ 00bbbf3c bytes c36ee397
- 00bbbb24 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bbbb24 ["RETURN", null, ["register:0:8"]]
- 00bbbb24 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d70111b06c4db4bf025fb6efb495eee8"></a>

### [`00bbbbac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbbac.md) → [`00bbbfd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbfd4.md) _ZN8firebase9messaging27IsRegistrationOnInitEnabledEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 14.29% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbbfe8",
      "incomplete_value": true,
      "site": "00bbbfe8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bbbbc0",
      "incomplete_value": true,
      "site": "00bbbbc0",
      "value": [
        "INT_NOTEQUAL",
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbbbe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bbc008"
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
      "00bbbfe4",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbbfe8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bbbbe4"
      ]
    ],
    [
      "unmatched:00bbbbc8",
      "PARAM",
      [
        "storage",
        "002a2848",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbbfe4",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbbfe8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbc00c"
      ]
    ],
    [
      "00bbbff0",
      "PARAM",
      [
        "storage",
        "002a2915",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbbc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbbac.md#insn-00bbbbc0) · [`00bbbbcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbbac.md#insn-00bbbbcc) · [`00bbbbd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbbac.md#insn-00bbbbd8)
- 新版 `00bbbfe8`（命令位置の公開資料なし）

~~~diff
- 00bbbbc0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bbbbc0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bbbfe8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00bbbfe8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bbbbc0 bytes 200100b5
+ 00bbbfe8 bytes 200100b5
- 00bbbbcc ["INT_ADD", "register:40f0:8", ["const:bbbbcc:8", "const:4:8"]]
- 00bbbbcc ["CALL", null, ["callee:00c5aca0:8"]]
- 00bbbbcc bytes 357b0294
- 00bbbbd8 ["INT_ADD", "register:40f0:8", ["const:bbbbd8:8", "const:4:8"]]
- 00bbbbd8 ["CALL", null, ["callee:00c5b000:8"]]
- 00bbbbd8 bytes 0a7c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df80d8f821c4d4decdee7e42adfbbbf4"></a>

### [`00bbbc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbc18.md) → [`00bbc040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc040.md) _ZN8firebase9messaging8RegisterEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 20件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bbbe80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbe80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md)
- 新版 呼出元 0件  · 呼出先 20件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bbc2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc2a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 88.03% / 新版 88.03%

CFGの説明率　旧版 29.41% / 新版 29.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbbc48"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bbc070"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbc07c",
      "incomplete_value": true,
      "site": "00bbc080",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:370:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbc54",
      "incomplete_value": true,
      "site": "00bbbc58",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:f70:8"
              ]
            ]
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
      "unmatched:00bbbc44",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bbbc48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbc140"
      ]
    ],
    [
      "00bbc078",
      "READ",
      [
        "storage",
        "01125f70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbc06c",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc070",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbc140"
      ]
    ],
    [
      "00bbc078",
      "READ",
      [
        "storage",
        "01126370",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbc48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbc18.md#insn-00bbbc48) · [`00bbbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbc18.md#insn-00bbbc58) · [`00bbbc74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbc18.md#insn-00bbbc74)
- 新版 `00bbc080`（命令位置の公開資料なし） · `00bbc09c`（命令位置の公開資料なし）

~~~diff
- 00bbbc48 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00bbbc48 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bbbc48 bytes 890600b4
- 00bbbc58 ["INT_ADD", "register:40f0:8", ["const:bbbc58:8", "const:4:8"]]
- 00bbbc58 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bbc080 ["INT_ADD", "register:40f0:8", ["const:bbc080:8", "const:4:8"]]
+ 00bbc080 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bbbc58 bytes 6a7a0294
+ 00bbc080 bytes 607a0294
- 00bbbc74 ["INT_ADD", "register:40f0:8", ["const:bbbc74:8", "const:4:8"]]
- 00bbbc74 ["CALL", null, ["callee:00c5ae40:8"]]
+ 00bbc09c ["INT_ADD", "register:40f0:8", ["const:bbc09c:8", "const:4:8"]]
+ 00bbc09c ["CALL", null, ["callee:00c5ae40:8"]]
- 00bbbc74 bytes 737b0294
+ 00bbc09c bytes 697b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abc22587660bd434c64fd77689a1d7c5"></a>

### [`00bbbe80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbe80.md) → [`00bbc2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc2a8.md) FUN_00bbc2a8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bbbc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbc18.md) [`00bbc070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc070.md) [`00bbc9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc9ec.md) · 呼出先 8件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md)
- 新版 呼出元 3件 [`00bbc040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc040.md) [`00bbc498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc498.md) [`00bbce14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbce14.md) · 呼出先 8件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.44% / 新版 75.44%

CFGの説明率　旧版 45.45% / 新版 38.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbbe84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbbe88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbbe88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbbe84",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbbe88",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbbe8c",
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
      "00bbc2ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bbc2b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bbc2b4",
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

- 旧版 [`00bbbe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbe80.md#insn-00bbbe84) · [`00bbbe88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbe80.md#insn-00bbbe88) · [`00bbbe8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbe80.md#insn-00bbbe8c)

~~~diff
- 00bbbe84 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00bbbe84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00bbbe84 bytes f71300f9
- 00bbbe88 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bbbe88 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bbbe88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bbbe88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbbe88 bytes f65703a9
- 00bbbe8c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbbe8c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbbe8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bbbe8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbbe8c bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8b7b063a8adf6d1c68593f6ebf6dd03"></a>

### [`00bbbf98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbf98.md) → [`00bbc3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc3c0.md) _ZN8firebase9messaging18RegisterLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md)

変更の種類 branch_value, call_argument_candidate, constant, local_def_use, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbc3dc",
      "incomplete_value": true,
      "site": "00bbc3dc",
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
      "definition_site": "00bbbfb4",
      "incomplete_value": true,
      "site": "00bbbfb4",
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
    "new": null,
    "old": {
      "definition_site": "00bbbfec",
      "incomplete_value": true,
      "site": "00bbbff0",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbc430",
      "incomplete_value": false,
      "site": "00bbc434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:915:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbc008",
      "incomplete_value": false,
      "site": "00bbc00c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "00bbc3d4",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc430",
      "PARAM",
      [
        "storage",
        "002a2848",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbc3d4",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc430",
      "PARAM",
      [
        "storage",
        "002a2915",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbf98.md#insn-00bbbff0) · [`00bbc00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbf98.md#insn-00bbc00c) · [`00bbbfa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbf98.md#insn-00bbbfa8)
- 新版 `00bbc418`（命令位置の公開資料なし） · `00bbc434`（命令位置の公開資料なし） · `00bbc3d0`（命令位置の公開資料なし）

~~~diff
- 00bbbff0 ["INT_ADD", "register:40f0:8", ["const:bbbff0:8", "const:4:8"]]
- 00bbbff0 ["CALL", null, ["callee:00c5ae10:8"]]
+ 00bbc418 ["INT_ADD", "register:40f0:8", ["const:bbc418:8", "const:4:8"]]
+ 00bbc418 ["CALL", null, ["callee:00c5ae10:8"]]
- 00bbbff0 bytes 887a0294
+ 00bbc418 bytes 7e7a0294
- 00bbc00c ["INT_ADD", "register:40f0:8", ["const:bbc00c:8", "const:4:8"]]
- 00bbc00c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bbc434 ["INT_ADD", "register:40f0:8", ["const:bbc434:8", "const:4:8"]]
+ 00bbc434 ["CALL", null, ["callee:00c5b000:8"]]
- 00bbc00c bytes fd7a0294
+ 00bbc434 bytes f37a0294
- 00bbbfa8 ["COPY", "register:4048:8", ["const:1125000:8"]]
+ 00bbc3d0 ["COPY", "register:4048:8", ["const:1126000:8"]]
- 00bbbfa8 bytes 492b00d0
+ 00bbc3d0 bytes 492b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4e4e182122aedd3f8b880525989e098"></a>

### [`00bbc070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc070.md) → [`00bbc498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc498.md) _ZN8firebase9messaging10UnregisterEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 20件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bbbe80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbe80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md)
- 新版 呼出元 0件  · 呼出先 20件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bbc2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc2a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 85.47% / 新版 85.47%

CFGの説明率　旧版 23.53% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc0a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc128"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc224"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbc09c",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bbc0a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbc598"
      ]
    ],
    [
      "00bbc4d0",
      "READ",
      [
        "storage",
        "01125f70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbc4c4",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc4c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbc598"
      ]
    ],
    [
      "00bbc4d0",
      "READ",
      [
        "storage",
        "01126370",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbc0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc070.md#insn-00bbc0a0) · [`00bbc0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc070.md#insn-00bbc0b0) · [`00bbc0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc070.md#insn-00bbc0d8)
- 新版 `00bbc4d8`（命令位置の公開資料なし） · `00bbc500`（命令位置の公開資料なし）

~~~diff
- 00bbc0a0 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00bbc0a0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bbc0a0 bytes 890600b4
- 00bbc0b0 ["INT_ADD", "register:40f0:8", ["const:bbc0b0:8", "const:4:8"]]
- 00bbc0b0 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bbc4d8 ["INT_ADD", "register:40f0:8", ["const:bbc4d8:8", "const:4:8"]]
+ 00bbc4d8 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bbc0b0 bytes 54790294
+ 00bbc4d8 bytes 4a790294
- 00bbc0d8 ["INT_ADD", "register:40f0:8", ["const:bbc0d8:8", "const:4:8"]]
- 00bbc0d8 ["CALL", null, ["callee:00c5ae00:8"]]
+ 00bbc500 ["INT_ADD", "register:40f0:8", ["const:bbc500:8", "const:4:8"]]
+ 00bbc500 ["CALL", null, ["callee:00c5ae00:8"]]
- 00bbc0d8 bytes 4a7a0294
+ 00bbc500 bytes 407a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbdc3a170ba31b6591b9fee6beff8897"></a>

### [`00bbc2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc2d8.md) → [`00bbc700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc700.md) _ZN8firebase9messaging20UnregisterLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.95% / 新版 80.95%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc2d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc2d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc2dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbc2d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbc2dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbc2e0",
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
      "00bbc700",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bbc704",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bbc708",
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

- 旧版 [`00bbc2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc2d8.md#insn-00bbc2d8) · [`00bbc2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc2d8.md#insn-00bbc2dc) · [`00bbc2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc2d8.md#insn-00bbc2e0)

~~~diff
- 00bbc2d8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bbc2d8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bbc2d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bbc2d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbc2d8 bytes f657bda9
- 00bbc2dc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbc2dc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbc2dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bbc2dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbc2dc bytes f44f01a9
- 00bbc2e0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbc2e0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbc2e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bbc2e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbc2e0 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91bab77708ca7f05085e3482266a7e14"></a>

### [`00bbc3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc3b0.md) → [`00bbc7d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc7d8.md) _ZN8firebase9messaging8GetTokenEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d1c0.md) · 呼出先 22件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00b43b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43b90.md) [`00bbc68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc68c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c5d5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d5c0.md) · 呼出先 22件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00b43fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43fb8.md) [`00bbcab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbcab4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.68% / 新版 78.68%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `store_condition` 4件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc3b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc3b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc3b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbc3b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbc3b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbc3bc",
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
      "00bbc7dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bbc7e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bbc7e4",
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

- 旧版 [`00bbc3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc3b0.md#insn-00bbc3b4) · [`00bbc3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc3b0.md#insn-00bbc3b8) · [`00bbc3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc3b0.md#insn-00bbc3bc)

~~~diff
- 00bbc3b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00bbc3b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00bbc3b4 bytes f93300f9
- 00bbc3b8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bbc3b8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bbc3b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00bbc3b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbc3b8 bytes f85f07a9
- 00bbc3bc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bbc3bc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bbc3bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00bbc3bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbc3bc bytes f65708a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41ec7ea1c1df28c7f5a5aa43e5080e71"></a>

### [`00bbc68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc68c.md) → [`00bbcab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbcab4.md) FUN_00bbcab4

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbc3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc3b0.md) · 呼出先 15件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00bbc7d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc7d8.md) · 呼出先 15件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.54% / 新版 90.54%

CFGの説明率　旧版 30.36% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 4件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc784"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc788"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bbcbac"
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
      "unmatched:00bbc6c0",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "00bbcb68",
      "PARAM",
      [
        "storage",
        "01125e80",
        null,
        null
      ]
    ],
    [
      "00bbcb74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bbc790"
      ]
    ]
  ],
  "added": [
    [
      "00bbcae8",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "00bbcb68",
      "PARAM",
      [
        "storage",
        "01126280",
        null,
        null
      ]
    ],
    [
      "00bbcb74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbcbb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbc6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc68c.md#insn-00bbc6d8) · [`00bbc744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc68c.md#insn-00bbc744) · [`00bbc784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc68c.md#insn-00bbc784)
- 新版 `00bbcb00`（命令位置の公開資料なし） · `00bbcb6c`（命令位置の公開資料なし）

~~~diff
- 00bbc6d8 ["INT_ADD", "register:40f0:8", ["const:bbc6d8:8", "const:4:8"]]
- 00bbc6d8 ["CALL", null, ["callee:00c5b5c0:8"]]
+ 00bbcb00 ["INT_ADD", "register:40f0:8", ["const:bbcb00:8", "const:4:8"]]
+ 00bbcb00 ["CALL", null, ["callee:00c5b5c0:8"]]
- 00bbc6d8 bytes ba7a0294
+ 00bbcb00 bytes b07a0294
- 00bbc744 ["INT_ADD", "register:40f0:8", ["const:bbc744:8", "const:4:8"]]
- 00bbc744 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bbcb6c ["INT_ADD", "register:40f0:8", ["const:bbcb6c:8", "const:4:8"]]
+ 00bbcb6c ["CALL", null, ["callee:00c5aa00:8"]]
- 00bbc744 bytes af770294
+ 00bbcb6c bytes a5770294
- 00bbc784 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00bbc784 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00bbc784 bytes e00f803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-feabe51bc43a338848683d728e64fe36"></a>

### [`00bbc914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc914.md) → [`00bbcd3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbcd3c.md) _ZN8firebase9messaging18GetTokenLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_return_alignment

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 20.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbcd58",
      "incomplete_value": true,
      "site": "00bbcd58",
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
      "definition_site": "00bbc930",
      "incomplete_value": true,
      "site": "00bbc930",
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
      "definition_site": "00bbcdac",
      "incomplete_value": false,
      "site": "00bbcdb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:915:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbc984",
      "incomplete_value": false,
      "site": "00bbc988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bbc998",
      "incomplete_value": true,
      "site": "00bbc9a8",
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
            "const:30:8"
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
      "00bbcd50",
      "READ",
      [
        "storage",
        "01125f60",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bbc984",
      "PARAM",
      [
        "storage",
        "002a2848",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbcd50",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbcdac",
      "PARAM",
      [
        "storage",
        "002a2915",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbc988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc914.md#insn-00bbc988) · [`00bbc9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc914.md#insn-00bbc9a8) · [`00bbc9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc914.md#insn-00bbc9b8)
- 新版 `00bbcdb0`（命令位置の公開資料なし） · `00bbcdd0`（命令位置の公開資料なし）

~~~diff
- 00bbc988 ["INT_ADD", "register:40f0:8", ["const:bbc988:8", "const:4:8"]]
- 00bbc988 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bbcdb0 ["INT_ADD", "register:40f0:8", ["const:bbcdb0:8", "const:4:8"]]
+ 00bbcdb0 ["CALL", null, ["callee:00c5b000:8"]]
- 00bbc988 bytes 9e780294
+ 00bbcdb0 bytes 94780294
- 00bbc9a8 ["INT_ADD", "register:40f0:8", ["const:bbc9a8:8", "const:4:8"]]
- 00bbc9a8 ["CALL", null, ["callee:00c5abe0:8"]]
+ 00bbcdd0 ["INT_ADD", "register:40f0:8", ["const:bbcdd0:8", "const:4:8"]]
+ 00bbcdd0 ["CALL", null, ["callee:00c5abe0:8"]]
- 00bbc9a8 bytes 8e770294
+ 00bbcdd0 bytes 84770294
- 00bbc9b8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bbc9b8 ["RETURN", null, ["register:0:8"]]
- 00bbc9b8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d3498731dfb9418b5b5b43680899af9"></a>

### [`00bbc9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc9ec.md) → [`00bbce14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbce14.md) _ZN8firebase9messaging11DeleteTokenEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 20件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bbbe80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbbe80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md)
- 新版 呼出元 0件  · 呼出先 20件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bbc2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc2a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.63% / 新版 78.63%

CFGの説明率　旧版 35.29% / 新版 21.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc9f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc9f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc9f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbc9f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbc9f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbc9f8",
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
      "00bbce18",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bbce1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bbce20",
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

- 旧版 [`00bbc9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc9ec.md#insn-00bbc9f0) · [`00bbc9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc9ec.md#insn-00bbc9f4) · [`00bbc9f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc9ec.md#insn-00bbc9f8)

~~~diff
- 00bbc9f0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bbc9f0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bbc9f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00bbc9f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbc9f0 bytes f85f05a9
- 00bbc9f4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bbc9f4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bbc9f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00bbc9f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbc9f4 bytes f65706a9
- 00bbc9f8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbc9f8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbc9f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00bbc9f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbc9f8 bytes f44f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7de71078aec4d1c80830a40d357831e7"></a>

### [`00bbcc54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcc54.md) → [`00bbd07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd07c.md) _ZN8firebase9messaging21DeleteTokenLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.05% / 新版 69.05%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbcc54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbcc54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbcc58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbcc54",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbcc58",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbcc5c",
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
      "00bbd07c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bbd080",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bbd084",
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

- 旧版 [`00bbcc54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcc54.md#insn-00bbcc54) · [`00bbcc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcc54.md#insn-00bbcc58) · [`00bbcc5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcc54.md#insn-00bbcc5c)

~~~diff
- 00bbcc54 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bbcc54 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bbcc54 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bbcc54 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbcc54 bytes f657bda9
- 00bbcc58 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbcc58 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbcc58 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bbcc58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbcc58 bytes f44f01a9
- 00bbcc5c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbcc5c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbcc5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bbcc5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbcc5c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5e2d546f2bca211dffb6e53fef9b506"></a>

### [`00bbcd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcd30.md) → [`00bbd158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd158.md) FUN_00bbd158

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb95ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb95ec.md) · 呼出先 4件 [`00bbcd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcd98.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5cfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cfb0.md)
- 新版 呼出元 1件 [`00bb9a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9a14.md) · 呼出先 4件 [`00bbd1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd1c0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5d3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3b0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbd184",
      "incomplete_value": false,
      "site": "00bbd184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbcd5c",
      "incomplete_value": false,
      "site": "00bbcd5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
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
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbd170",
      "incomplete_value": true,
      "site": "00bbd170",
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
      "definition_site": "00bbcd48",
      "incomplete_value": true,
      "site": "00bbcd48",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00bbcd48"
      ],
      [
        "FALL_THROUGH",
        "00bbd170"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bbd170",
      "incomplete_value": true,
      "site": "00bbd184",
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
      "definition_site": "00bbcd48",
      "incomplete_value": true,
      "site": "00bbcd5c",
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
    "ordinal": 4,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbd168",
      "READ",
      [
        "storage",
        "01125f70",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd184",
      "WRITE",
      [
        "storage",
        "01126008",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bbd168",
      "READ",
      [
        "storage",
        "01126370",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd184",
      "WRITE",
      [
        "storage",
        "01126408",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbcd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcd30.md#insn-00bbcd5c) · [`00bbcd3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcd30.md#insn-00bbcd3c) · [`00bbcd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcd30.md#insn-00bbcd40)
- 新版 `00bbd184`（命令位置の公開資料なし） · `00bbd164`（命令位置の公開資料なし） · `00bbd168`（命令位置の公開資料なし）

~~~diff
- 00bbcd5c ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bbcd5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:8:8"]]
- 00bbcd5c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bbd184 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00bbd184 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:408:8"]]
+ 00bbd184 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bbcd5c bytes 09210039
+ 00bbd184 bytes 09211039
- 00bbcd3c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00bbd164 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bbcd3c bytes 482b00b0
+ 00bbd164 bytes 482b00b0
- 00bbcd40 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
- 00bbcd40 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbd168 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
+ 00bbd168 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbcd40 bytes 14b947f9
+ 00bbd168 bytes 14b941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a1e8587412eb9f44348365c9350534b"></a>

### [`00bbcd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcd98.md) → [`00bbd1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd1c0.md) FUN_00bbd1c0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bbcd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcd30.md) [`00bbcee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcee0.md) [`00bbcf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcf70.md) · 呼出先 4件 [`00bbb274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb274.md) [`00bbb818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb818.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md)
- 新版 呼出元 3件 [`00bbd158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd158.md) [`00bbd308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd308.md) [`00bbd398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd398.md) · 呼出先 4件 [`00bbb69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb69c.md) [`00bbbc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbc40.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 60.98% / 新版 60.98%

CFGの説明率　旧版 13.95% / 新版 13.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 2件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbd1d8",
      "incomplete_value": true,
      "site": "00bbd1d8",
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
      "definition_site": "00bbcdb0",
      "incomplete_value": true,
      "site": "00bbcdb0",
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbcde4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbcdec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbd1d4",
      "READ",
      [
        "storage",
        "01125f78",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd1e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bbcde8"
      ]
    ],
    [
      "unmatched:00bbcdd4",
      "READ",
      [
        "storage",
        "01125f78",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbd1d4",
      "READ",
      [
        "storage",
        "01126378",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd1e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbd210"
      ]
    ],
    [
      "00bbd1fc",
      "READ",
      [
        "storage",
        "01126378",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbcdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcd98.md#insn-00bbcdb0) · [`00bbcde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcd98.md#insn-00bbcde4) · [`00bbcdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcd98.md#insn-00bbcdec)
- 新版 `00bbd1d8`（命令位置の公開資料なし）

~~~diff
- 00bbcdb0 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00bbcdb0 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 00bbd1d8 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00bbd1d8 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00bbcdb0 bytes 740400b4
+ 00bbd1d8 bytes 740400b4
- 00bbcde4 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00bbcde4 bytes a0000054
- 00bbcdec ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00bbcdec ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00bbcdec ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00bbcdec ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00bbcdec bytes e8fe0736
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14a0546615a65f18e70cb72410be638a"></a>

### [`00bbcee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcee0.md) → [`00bbd308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd308.md) FUN_00bbd308

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb95ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb95ec.md) · 呼出先 4件 [`00bbcd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcd98.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5cfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cfc0.md)
- 新版 呼出元 1件 [`00bb9a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9a14.md) · 呼出先 4件 [`00bbd1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd1c0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5d3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3c0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbd334",
      "incomplete_value": false,
      "site": "00bbd334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbcf0c",
      "incomplete_value": false,
      "site": "00bbcf0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
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
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbd320",
      "incomplete_value": true,
      "site": "00bbd320",
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
      "definition_site": "00bbcef8",
      "incomplete_value": true,
      "site": "00bbcef8",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00bbcef8"
      ],
      [
        "FALL_THROUGH",
        "00bbd320"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bbd320",
      "incomplete_value": true,
      "site": "00bbd334",
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
      "definition_site": "00bbcef8",
      "incomplete_value": true,
      "site": "00bbcf0c",
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
    "ordinal": 4,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbd318",
      "READ",
      [
        "storage",
        "01125f70",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd334",
      "WRITE",
      [
        "storage",
        "01126008",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bbd318",
      "READ",
      [
        "storage",
        "01126370",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd334",
      "WRITE",
      [
        "storage",
        "01126408",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbcf0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcee0.md#insn-00bbcf0c) · [`00bbceec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcee0.md#insn-00bbceec) · [`00bbcef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcee0.md#insn-00bbcef0)
- 新版 `00bbd334`（命令位置の公開資料なし） · `00bbd314`（命令位置の公開資料なし） · `00bbd318`（命令位置の公開資料なし）

~~~diff
- 00bbcf0c ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bbcf0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:8:8"]]
- 00bbcf0c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bbd334 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00bbd334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:408:8"]]
+ 00bbd334 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bbcf0c bytes 09210039
+ 00bbd334 bytes 09211039
- 00bbceec ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00bbd314 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bbceec bytes 482b00b0
+ 00bbd314 bytes 482b00b0
- 00bbcef0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
- 00bbcef0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbd318 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
+ 00bbd318 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbcef0 bytes 14b947f9
+ 00bbd318 bytes 14b941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fe15fa840f79a7269d69b12cc23e974"></a>

### [`00bbd0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd0f4.md) → [`00bbd51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd51c.md) _ZNSt6__ndk16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase16SafeFutureHandleIvEEEENS5_ISB_EEE21__push

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d1d0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md) [`00c5b860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b860.md)
- 新版 呼出元 1件 [`00c5d5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d5d0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md) [`00c5bc60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bc60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 35.71% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd1bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd1fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bbd5e4"
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
      "unmatched:00bbd1bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbd634"
      ]
    ],
    [
      "unmatched:00bbd1fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbd5f0"
      ]
    ],
    [
      "unmatched:00bbd27c",
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
      "00bbd5e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbd634"
      ]
    ],
    [
      "00bbd624",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbd5f0"
      ]
    ],
    [
      "00bbd6a4",
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

- 旧版 [`00bbd1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd0f4.md#insn-00bbd1bc) · [`00bbd1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd0f4.md#insn-00bbd1fc) · [`00bbd284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd0f4.md#insn-00bbd284)

~~~diff
- 00bbd1bc ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 00bbd1bc bytes 80020054
- 00bbd1fc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bbd1fc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00bbd1fc bytes 61feff54
- 00bbd284 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bbd284 ["RETURN", null, ["register:0:8"]]
- 00bbd284 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-495700f2d1a87bff4d9d04e59c24cf65"></a>

### [`00bbd298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd298.md) → [`00bbd6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd6c0.md) _INIT_286

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b650e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b650e8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c5a880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a880.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b65510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65510.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c5ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac80.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 48.28% / 新版 48.28%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd298"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd29c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd29c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbd298",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbd29c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbd2a0",
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
      "00bbd6c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bbd6c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bbd6c8",
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

- 旧版 [`00bbd298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd298.md#insn-00bbd298) · [`00bbd29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd298.md#insn-00bbd29c) · [`00bbd2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd298.md#insn-00bbd2a0)

~~~diff
- 00bbd298 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bbd298 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bbd298 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbd298 bytes f50f1df8
- 00bbd29c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbd29c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbd29c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bbd29c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbd29c bytes f44f01a9
- 00bbd2a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbd2a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbd2a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bbd2a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbd2a0 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9221e0c695b2c3bc39bc244998723241"></a>

### [`00bbd30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd30c.md) → [`00bbd734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd734.md) _ZNK8firebase9messaging8internal13MessageReader14ReadFromBufferERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d150.md) · 呼出先 4件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5d0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d0d0.md) [`00c5d140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d140.md)
- 新版 呼出元 1件 [`00c5d550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d550.md) · 呼出先 4件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5d4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d4d0.md) [`00c5d540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d540.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.71% / 新版 70.71%

CFGの説明率　旧版 40.43% / 新版 41.30%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 9件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd310"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd314"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd314"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbd310",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbd314",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbd318",
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
      "00bbd738",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00bbd73c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00bbd740",
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

- 旧版 [`00bbd310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd30c.md#insn-00bbd310) · [`00bbd314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd30c.md#insn-00bbd314) · [`00bbd318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd30c.md#insn-00bbd318)

~~~diff
- 00bbd310 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 00bbd310 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 00bbd310 bytes e82b00fd
- 00bbd314 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00bbd314 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00bbd314 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00bbd314 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbd314 bytes fc6f06a9
- 00bbd318 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bbd318 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bbd318 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00bbd318 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbd318 bytes fa6707a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89f948e4a5a59da1fd028b61524b2ca6"></a>

### [`00bbd624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd624.md) → [`00bbda4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbda4c.md) _ZNK8firebase9messaging8internal13MessageReader14ConsumeMessageEPKN3com6google8firebase9messaging3cpp17SerializedMessageE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d140.md) · 呼出先 13件 [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)
- 新版 呼出元 1件 [`00c5d540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d540.md) · 呼出先 13件 [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 36.70% / 新版 36.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_condition` 1件, `unresolved_branch_alignment` 15件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 52件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd65c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd660"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd660"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbd65c",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbd660",
      "WRITE",
      [
        "storage",
        "Stack[-0x170]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbd664",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bbda84",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00bbda88",
      "WRITE",
      [
        "storage",
        "Stack[-0x170]",
        null,
        null
      ]
    ],
    [
      "00bbda8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd65c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd624.md#insn-00bbd65c) · [`00bbd660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd624.md#insn-00bbd660) · [`00bbd664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd624.md#insn-00bbd664)

~~~diff
- 00bbd65c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bbd65c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffff98:8"]]
- 00bbd65c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bbd65c bytes a88319f8
- 00bbd660 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00bbd660 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bbd660 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00bbd660 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00bbd660 bytes ff7f1da9
- 00bbd664 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:180:8"]]
- 00bbd664 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00bbd664 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00bbd664 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00bbd664 bytes e0030cad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c84c733bc119dd9be3fce7d5778e3346"></a>

### [`00bc0eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0eec.md) → [`00bc1314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1314.md) _INIT_287

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc0e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0e44.md) [`00bc0e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0e4c.md) [`00c5a7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc126c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc126c.md) [`00bc1274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1274.md) [`00c5abc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abc0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 41.67% / 新版 41.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc1334",
      "incomplete_value": false,
      "site": "00bc1334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:410:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0f0c",
      "incomplete_value": false,
      "site": "00bc0f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc1334",
      "incomplete_value": false,
      "site": "00bc1334",
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
            "const:815:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0f0c",
      "incomplete_value": false,
      "site": "00bc0f0c",
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
            "const:748:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc1334",
      "incomplete_value": false,
      "site": "00bc1334",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:410:8"
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
      "definition_site": "00bc0f0c",
      "incomplete_value": false,
      "site": "00bc0f0c",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:10:8"
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
      "00bc1324",
      "PARAM",
      [
        "storage",
        "01126010",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1334",
      "WRITE",
      [
        "storage",
        "01126010",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1334",
      "DATA",
      [
        "storage",
        "002a9748",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc1324",
      "PARAM",
      [
        "storage",
        "01126410",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1334",
      "WRITE",
      [
        "storage",
        "01126410",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1334",
      "DATA",
      [
        "storage",
        "002a9815",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0eec.md#insn-00bc0ef4) · [`00bc0ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0eec.md#insn-00bc0ef8) · [`00bc0efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0eec.md#insn-00bc0efc)
- 新版 `00bc131c`（命令位置の公開資料なし） · `00bc1320`（命令位置の公開資料なし） · `00bc1324`（命令位置の公開資料なし）

~~~diff
- 00bc0ef4 ["COPY", "register:4048:8", ["const:bc0000:8"]]
+ 00bc131c ["COPY", "register:4048:8", ["const:bc1000:8"]]
- 00bc0ef4 bytes 09000090
+ 00bc131c bytes 09000090
- 00bc0ef8 ["COPY", "register:4050:8", ["const:bc0000:8"]]
+ 00bc1320 ["COPY", "register:4050:8", ["const:bc1000:8"]]
- 00bc0ef8 bytes 0a000090
+ 00bc1320 bytes 0a000090
- 00bc0efc ["COPY", "tmp:0:8", ["const:10:8"]]
- 00bc0efc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc0efc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc0efc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc1324 ["COPY", "tmp:0:8", ["const:410:8"]]
+ 00bc1324 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1324 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1324 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc0efc bytes 00400091
+ 00bc1324 bytes 00401091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-658cbbc284df5a47858140770c0435f6"></a>

### [`00bc0f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0f24.md) → [`00bc134c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc134c.md) _ZN8firebase13remote_config12RemoteConfig11GetInstanceEPNS_3AppE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a730.md) · 呼出先 11件 [`00bc163c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc163c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7f0.md)
- 新版 呼出元 1件 [`00c5ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ab30.md) · 呼出先 11件 [`00bc1a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1a64.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abf0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.45% / 新版 98.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc1388",
      "incomplete_value": true,
      "site": "00bc1388",
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
      "definition_site": "00bc0f60",
      "incomplete_value": true,
      "site": "00bc0f60",
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
      "definition_site": "00bc136c",
      "incomplete_value": true,
      "site": "00bc1370",
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
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0f44",
      "incomplete_value": true,
      "site": "00bc0f48",
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
                "const:530:8"
              ]
            ]
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
      "definition_site": "00bc13c8",
      "incomplete_value": true,
      "site": "00bc13cc",
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
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0fa0",
      "incomplete_value": true,
      "site": "00bc0fa4",
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
                "const:530:8"
              ]
            ]
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
      "00bc1364",
      "READ",
      [
        "storage",
        "00c9b530",
        null,
        "pointer"
      ]
    ],
    [
      "00bc136c",
      "PARAM",
      [
        "storage",
        "01126050",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ],
    [
      "00bc1374",
      "PARAM",
      [
        "storage",
        "01126050",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bc1364",
      "READ",
      [
        "storage",
        "00c9b930",
        null,
        "pointer"
      ]
    ],
    [
      "00bc136c",
      "PARAM",
      [
        "storage",
        "01126450",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ],
    [
      "00bc1374",
      "PARAM",
      [
        "storage",
        "01126450",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0f24.md#insn-00bc0f48) · [`00bc0fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0f24.md#insn-00bc0fa4) · [`00bc0fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0f24.md#insn-00bc0fc4)
- 新版 `00bc1370`（命令位置の公開資料なし） · `00bc13cc`（命令位置の公開資料なし） · `00bc13ec`（命令位置の公開資料なし）

~~~diff
- 00bc0f48 ["INT_ADD", "register:40f0:8", ["const:bc0f48:8", "const:4:8"]]
- 00bc0f48 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bc1370 ["INT_ADD", "register:40f0:8", ["const:bc1370:8", "const:4:8"]]
+ 00bc1370 ["CALL", null, ["callee:00c5aa00:8"]]
- 00bc0f48 bytes ae650294
+ 00bc1370 bytes a4650294
- 00bc0fa4 ["INT_ADD", "register:40f0:8", ["const:bc0fa4:8", "const:4:8"]]
- 00bc0fa4 ["CALL", null, ["callee:00c5aa10:8"]]
+ 00bc13cc ["INT_ADD", "register:40f0:8", ["const:bc13cc:8", "const:4:8"]]
+ 00bc13cc ["CALL", null, ["callee:00c5aa10:8"]]
- 00bc0fa4 bytes 9b650294
+ 00bc13cc bytes 91650294
- 00bc0fc4 ["INT_ADD", "register:40f0:8", ["const:bc0fc4:8", "const:4:8"]]
- 00bc0fc4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc13ec ["INT_ADD", "register:40f0:8", ["const:bc13ec:8", "const:4:8"]]
+ 00bc13ec ["CALL", null, ["callee:00c5b000:8"]]
- 00bc0fc4 bytes 0f670294
+ 00bc13ec bytes 05670294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f78c8d0598ae414780643e33959f436d"></a>

### [`00bc1358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1358.md) → [`00bc1780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1780.md) _ZN8firebase13remote_config12RemoteConfigC2EPNS_3AppE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5d470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d470.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5d870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d870.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc17a0",
      "incomplete_value": false,
      "site": "00bc17a4",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1378",
      "incomplete_value": false,
      "site": "00bc137c",
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
            "const:598:8"
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
      "00bc17a0",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc17a0",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc137c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1358.md#insn-00bc137c) · [`00bc1378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1358.md#insn-00bc1378) · [`00bc1388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1358.md#insn-00bc1388)
- 新版 `00bc17a4`（命令位置の公開資料なし） · `00bc17a0`（命令位置の公開資料なし） · `00bc17b0`（命令位置の公開資料なし）

~~~diff
- 00bc137c ["INT_ADD", "register:40f0:8", ["const:bc137c:8", "const:4:8"]]
- 00bc137c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc17a4 ["INT_ADD", "register:40f0:8", ["const:bc17a4:8", "const:4:8"]]
+ 00bc17a4 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc137c bytes 21660294
+ 00bc17a4 bytes 17660294
- 00bc1378 ["COPY", "tmp:0:8", ["const:598:8"]]
- 00bc1378 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc1378 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc1378 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc17a0 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 00bc17a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc17a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc17a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc1378 bytes 00601691
+ 00bc17a0 bytes 00601791
- 00bc1388 ["INT_ADD", "register:40f0:8", ["const:bc1388:8", "const:4:8"]]
- 00bc1388 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bc17b0 ["INT_ADD", "register:40f0:8", ["const:bc17b0:8", "const:4:8"]]
+ 00bc17b0 ["CALL", null, ["callee:00c57e90:8"]]
- 00bc1388 bytes c2590294
+ 00bc17b0 bytes b8590294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d416b0f125666bec97efaba76ec74dfc"></a>

### [`00bc163c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc163c.md) → [`00bc1a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1a64.md) FUN_00bc1a64

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc0f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0f24.md) · 呼出先 2件 [`00c5a9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9e0.md) [`00c5d2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d2b0.md)
- 新版 呼出元 1件 [`00bc134c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc134c.md) · 呼出先 2件 [`00c5ade0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ade0.md) [`00c5d6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d6b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc1a7c",
      "incomplete_value": false,
      "site": "00bc1a84",
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
            "const:1d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1654",
      "incomplete_value": false,
      "site": "00bc165c",
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
            "const:191:8"
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
      "00bc1a7c",
      "PARAM",
      [
        "storage",
        "002ac191",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc1a7c",
      "PARAM",
      [
        "storage",
        "002ac1d1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc165c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc163c.md#insn-00bc165c) · [`00bc1654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc163c.md#insn-00bc1654)
- 新版 `00bc1a84`（命令位置の公開資料なし） · `00bc1a7c`（命令位置の公開資料なし）

~~~diff
- 00bc165c ["INT_ADD", "register:40f0:8", ["const:bc165c:8", "const:4:8"]]
- 00bc165c ["CALL", null, ["callee:00c5ade0:8"]]
+ 00bc1a84 ["INT_ADD", "register:40f0:8", ["const:bc1a84:8", "const:4:8"]]
+ 00bc1a84 ["CALL", null, ["callee:00c5ade0:8"]]
- 00bc165c bytes e1640294
+ 00bc1a84 bytes d7640294
- 00bc1654 ["COPY", "tmp:0:8", ["const:191:8"]]
- 00bc1654 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc1654 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc1654 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc1a7c ["COPY", "tmp:0:8", ["const:1d1:8"]]
+ 00bc1a7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1a7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1a7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc1654 bytes 00440691
+ 00bc1a7c bytes 00440791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a5178465fb9af7e80a82c822ff6c716"></a>

### [`00bc16b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc16b0.md) → [`00bc1ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1ad8.md) _INIT_288

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b650e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b650e8.md) [`00bc0f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0f1c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c5a880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a880.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b65510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65510.md) [`00bc1344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1344.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c5ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc1afc",
      "incomplete_value": true,
      "site": "00bc1afc",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc16d4",
      "incomplete_value": true,
      "site": "00bc16d4",
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
            "const:8:8"
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
      "definition_site": "00bc1b08",
      "incomplete_value": true,
      "site": "00bc1b08",
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
      "definition_site": "00bc16e0",
      "incomplete_value": true,
      "site": "00bc16e0",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc1b0c",
      "incomplete_value": true,
      "site": "00bc1b0c",
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
                "const:938:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc16e4",
      "incomplete_value": true,
      "site": "00bc16e4",
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
                "const:538:8"
              ]
            ]
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
      "00bc1ae8",
      "READ",
      [
        "storage",
        "00c9b538",
        null,
        "pointer"
      ]
    ],
    [
      "00bc1ae8",
      "PARAM",
      [
        "storage",
        "01126038",
        "_ZN8firebase13remote_config5g_rcsE",
        "undefined8"
      ]
    ],
    [
      "00bc1afc",
      "WRITE",
      [
        "storage",
        "01126040",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1ae8",
      "READ",
      [
        "storage",
        "00c9b938",
        null,
        "pointer"
      ]
    ],
    [
      "00bc1ae8",
      "PARAM",
      [
        "storage",
        "01126438",
        "_ZN8firebase13remote_config5g_rcsE",
        "undefined8"
      ]
    ],
    [
      "00bc1afc",
      "WRITE",
      [
        "storage",
        "01126440",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc16e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc16b0.md#insn-00bc16e8) · [`00bc16fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc16b0.md#insn-00bc16fc) · [`00bc16c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc16b0.md#insn-00bc16c0)
- 新版 `00bc1b10`（命令位置の公開資料なし） · `00bc1b24`（命令位置の公開資料なし） · `00bc1ae8`（命令位置の公開資料なし）

~~~diff
- 00bc16e8 ["INT_ADD", "register:40f0:8", ["const:bc16e8:8", "const:4:8"]]
- 00bc16e8 ["CALL", null, ["callee:00c57e30:8"]]
+ 00bc1b10 ["INT_ADD", "register:40f0:8", ["const:bc1b10:8", "const:4:8"]]
+ 00bc1b10 ["CALL", null, ["callee:00c57e30:8"]]
- 00bc16e8 bytes d2580294
+ 00bc1b10 bytes c8580294
- 00bc16fc ["INT_ADD", "register:40f0:8", ["const:bc16fc:8", "const:4:8"]]
- 00bc16fc ["CALL", null, ["callee:00c5ac80:8"]]
+ 00bc1b24 ["INT_ADD", "register:40f0:8", ["const:bc1b24:8", "const:4:8"]]
+ 00bc1b24 ["CALL", null, ["callee:00c5ac80:8"]]
- 00bc16fc bytes 61640294
+ 00bc1b24 bytes 57640294
- 00bc16c0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:538:8"]]
- 00bc16c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc1ae8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:938:8"]]
+ 00bc1ae8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc16c0 bytes 219c42f9
+ 00bc1ae8 bytes 219c44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03af72266179e69907774645555e06ed"></a>

### [`00bc171c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc171c.md) → [`00bc1b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1b44.md) _ZN8firebase13remote_config8internal6config19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allo

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc1b70",
      "incomplete_value": true,
      "site": "00bc1b70",
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
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1748",
      "incomplete_value": true,
      "site": "00bc1748",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc1b58",
      "incomplete_value": true,
      "site": "00bc1b58",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bc1730",
      "incomplete_value": true,
      "site": "00bc1730",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bc1b64",
      "incomplete_value": false,
      "site": "00bc1b68",
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
            "const:696:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc173c",
      "incomplete_value": false,
      "site": "00bc1740",
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
            "const:656:8"
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
      "00bc1b54",
      "READ",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1b64",
      "PARAM",
      [
        "storage",
        "002b1656",
        null,
        "string"
      ]
    ],
    [
      "00bc1b70",
      "WRITE",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1b54",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1b64",
      "PARAM",
      [
        "storage",
        "002b1696",
        null,
        "string"
      ]
    ],
    [
      "00bc1b70",
      "WRITE",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc171c.md#insn-00bc1740) · [`00bc1748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc171c.md#insn-00bc1748) · [`00bc172c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc171c.md#insn-00bc172c)
- 新版 `00bc1b68`（命令位置の公開資料なし） · `00bc1b70`（命令位置の公開資料なし） · `00bc1b54`（命令位置の公開資料なし）

~~~diff
- 00bc1740 ["INT_ADD", "register:40f0:8", ["const:bc1740:8", "const:4:8"]]
- 00bc1740 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc1b68 ["INT_ADD", "register:40f0:8", ["const:bc1b68:8", "const:4:8"]]
+ 00bc1b68 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc1740 bytes f4640294
+ 00bc1b68 bytes ea640294
- 00bc1748 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
- 00bc1748 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1b70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
+ 00bc1b70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1748 bytes 603e00f9
+ 00bc1b70 bytes 603e02f9
- 00bc172c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
- 00bc172c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc1b54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
+ 00bc1b54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc172c bytes 683e40f9
+ 00bc1b54 bytes 683e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-329592906169dcb8bd1831c2a333d4dd"></a>

### [`00bc175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc175c.md) → [`00bc1b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1b84.md) _ZN8firebase13remote_config8internal6config19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allo

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc1bb0",
      "incomplete_value": true,
      "site": "00bc1bb0",
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
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1788",
      "incomplete_value": true,
      "site": "00bc1788",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc1b98",
      "incomplete_value": true,
      "site": "00bc1b98",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bc1770",
      "incomplete_value": true,
      "site": "00bc1770",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bc1ba0",
      "incomplete_value": false,
      "site": "00bc1ba8",
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
            "const:696:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1778",
      "incomplete_value": false,
      "site": "00bc1780",
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
            "const:656:8"
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
      "00bc1b94",
      "READ",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1ba0",
      "PARAM",
      [
        "storage",
        "002b1656",
        null,
        "string"
      ]
    ],
    [
      "00bc1bb0",
      "WRITE",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1b94",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1ba0",
      "PARAM",
      [
        "storage",
        "002b1696",
        null,
        "string"
      ]
    ],
    [
      "00bc1bb0",
      "WRITE",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc175c.md#insn-00bc1780) · [`00bc1788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc175c.md#insn-00bc1788) · [`00bc176c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc175c.md#insn-00bc176c)
- 新版 `00bc1ba8`（命令位置の公開資料なし） · `00bc1bb0`（命令位置の公開資料なし） · `00bc1b94`（命令位置の公開資料なし）

~~~diff
- 00bc1780 ["INT_ADD", "register:40f0:8", ["const:bc1780:8", "const:4:8"]]
- 00bc1780 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc1ba8 ["INT_ADD", "register:40f0:8", ["const:bc1ba8:8", "const:4:8"]]
+ 00bc1ba8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc1780 bytes e4640294
+ 00bc1ba8 bytes da640294
- 00bc1788 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
- 00bc1788 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1bb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
+ 00bc1bb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1788 bytes 603e00f9
+ 00bc1bb0 bytes 603e02f9
- 00bc176c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
- 00bc176c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc1b94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
+ 00bc1b94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc176c bytes 683e40f9
+ 00bc1b94 bytes 683e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0bd47462cdc9f11ee3c529fa394f128"></a>

### [`00bc179c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc179c.md) → [`00bc1bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1bc4.md) _ZN8firebase13remote_config8internal6config10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc1bf4",
      "incomplete_value": true,
      "site": "00bc1bf4",
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
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc17cc",
      "incomplete_value": true,
      "site": "00bc17cc",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc1bd8",
      "incomplete_value": true,
      "site": "00bc1bd8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bc17b0",
      "incomplete_value": true,
      "site": "00bc17b0",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bc1be4",
      "incomplete_value": false,
      "site": "00bc1bec",
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
            "const:696:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc17bc",
      "incomplete_value": false,
      "site": "00bc17c4",
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
            "const:656:8"
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
      "00bc1bd4",
      "READ",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1be4",
      "PARAM",
      [
        "storage",
        "002b1656",
        null,
        "string"
      ]
    ],
    [
      "00bc1bf4",
      "WRITE",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1bd4",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1be4",
      "PARAM",
      [
        "storage",
        "002b1696",
        null,
        "string"
      ]
    ],
    [
      "00bc1bf4",
      "WRITE",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc17c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc179c.md#insn-00bc17c4) · [`00bc17cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc179c.md#insn-00bc17cc) · [`00bc17ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc179c.md#insn-00bc17ac)
- 新版 `00bc1bec`（命令位置の公開資料なし） · `00bc1bf4`（命令位置の公開資料なし） · `00bc1bd4`（命令位置の公開資料なし）

~~~diff
- 00bc17c4 ["INT_ADD", "register:40f0:8", ["const:bc17c4:8", "const:4:8"]]
- 00bc17c4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc1bec ["INT_ADD", "register:40f0:8", ["const:bc1bec:8", "const:4:8"]]
+ 00bc1bec ["CALL", null, ["callee:00c5af10:8"]]
- 00bc17c4 bytes d3640294
+ 00bc1bec bytes c9640294
- 00bc17cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
- 00bc17cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1bf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
+ 00bc1bf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc17cc bytes 603e00f9
+ 00bc1bf4 bytes 603e02f9
- 00bc17ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
- 00bc17ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc1bd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
+ 00bc1bd4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc17ac bytes 683e40f9
+ 00bc1bd4 bytes 683e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27283ee1d0c64977312c9578651c5d4f"></a>

### [`00bc17e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc17e0.md) → [`00bc1c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1c08.md) _ZN8firebase13remote_config8internal6config10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc1c38",
      "incomplete_value": true,
      "site": "00bc1c38",
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
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1810",
      "incomplete_value": true,
      "site": "00bc1810",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc1c1c",
      "incomplete_value": true,
      "site": "00bc1c1c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bc17f4",
      "incomplete_value": true,
      "site": "00bc17f4",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00bc1c24",
      "incomplete_value": false,
      "site": "00bc1c30",
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
            "const:696:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc17fc",
      "incomplete_value": false,
      "site": "00bc1808",
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
            "const:656:8"
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
      "00bc1c18",
      "READ",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1c24",
      "PARAM",
      [
        "storage",
        "002b1656",
        null,
        "string"
      ]
    ],
    [
      "00bc1c38",
      "WRITE",
      [
        "storage",
        "01126078",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1c18",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1c24",
      "PARAM",
      [
        "storage",
        "002b1696",
        null,
        "string"
      ]
    ],
    [
      "00bc1c38",
      "WRITE",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc17e0.md#insn-00bc1808) · [`00bc1810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc17e0.md#insn-00bc1810) · [`00bc17f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc17e0.md#insn-00bc17f0)
- 新版 `00bc1c30`（命令位置の公開資料なし） · `00bc1c38`（命令位置の公開資料なし） · `00bc1c18`（命令位置の公開資料なし）

~~~diff
- 00bc1808 ["INT_ADD", "register:40f0:8", ["const:bc1808:8", "const:4:8"]]
- 00bc1808 ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc1c30 ["INT_ADD", "register:40f0:8", ["const:bc1c30:8", "const:4:8"]]
+ 00bc1c30 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc1808 bytes c2640294
+ 00bc1c30 bytes b8640294
- 00bc1810 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
- 00bc1810 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1c38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
+ 00bc1c38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1810 bytes 603e00f9
+ 00bc1c38 bytes 603e02f9
- 00bc17f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
- 00bc17f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc1c18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
+ 00bc1c18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc17f0 bytes 683e40f9
+ 00bc1c18 bytes 683e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

