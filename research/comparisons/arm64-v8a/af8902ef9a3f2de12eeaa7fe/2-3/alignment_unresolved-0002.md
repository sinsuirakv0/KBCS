# v16.0.0 → v16.0.1 · 命令位置の検査未完了 (2)

[一覧の目次](README.md)

<a id="compare-cc7bddeb0f2d084267979f46259c2394"></a>

### [`008ce8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ce/008ce8d8.md) → [`008cea74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008cea74.md) FUN_008cea74

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008ce428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ce/008ce428.md) · 呼出先 3件 [`008ce428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ce/008ce428.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`008ce5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008ce5c4.md) · 呼出先 3件 [`008ce5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008ce5c4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 99.48% / 新版 99.48%

CFGの説明率　旧版 95.24% / 新版 96.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008ce8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ce/008ce8d8.md#insn-008ce8ec) · [`008ce8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ce/008ce8d8.md#insn-008ce8f0) · [`008ce904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ce/008ce8d8.md#insn-008ce904)
- 新版 `008cea8c`（命令位置の公開資料なし） · `008ceaa0`（命令位置の公開資料なし）

~~~diff
- 008ce8ec ["COPY", "register:40e8:8", ["register:8:8"]]
- 008ce8ec bytes fd030091
- 008ce8f0 ["INT_EQUAL", "tmp:0:1", ["register:4010:8", "const:0:8"]]
- 008ce8f0 ["CBRANCH", null, ["local:b40:8", "tmp:0:1"]]
+ 008cea8c ["INT_EQUAL", "tmp:0:1", ["register:4010:8", "const:0:8"]]
+ 008cea8c ["CBRANCH", null, ["local:b39:8", "tmp:0:1"]]
- 008ce8f0 bytes 821600b4
+ 008cea8c bytes 821600b4
- 008ce904 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 008ceaa0 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 008ce904 bytes 20010054
+ 008ceaa0 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc109b4652fb502fa68cc2b21a8a977f"></a>

### [`008d06ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d0/008d06ac.md) → [`008d0848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0848.md) FUN_008d0848

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "008d06b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008d0850"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008d06b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d06b4",
      "DATA",
      [
        "storage",
        "00c84128",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d0850",
      "DATA",
      [
        "storage",
        "00c84528",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d06b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d0/008d06ac.md#insn-008d06b4) · [`008d06b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d0/008d06ac.md#insn-008d06b8)
- 新版 `008d0850`（命令位置の公開資料なし）

~~~diff
- 008d06b4 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008d06b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008d06b4 bytes 280000f9
- 008d06b8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008d06b8 ["RETURN", null, ["register:0:8"]]
- 008d06b8 bytes c0035fd6
+ 008d0850 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 008d0850 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008d0850 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc80eb357aa854b12ddf488b9b099c5b"></a>

### [`008d80b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d80b0.md) → [`008d824c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d824c.md) FUN_008d824c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008d7058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d7/008d7058.md) · 呼出先 5件 [`008d809c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d809c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`008d71f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d71f4.md) · 呼出先 5件 [`008d8238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8238.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.63% / 新版 96.63%

CFGの説明率　旧版 84.00% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d81ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008d8348"
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
      "unmatched:008d81ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d8378"
      ]
    ]
  ],
  "added": [
    [
      "008d8348",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d8378"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d81ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d80b0.md#insn-008d81ac) · [`008d8104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d80b0.md#insn-008d8104)
- 新版 `008d8348`（命令位置の公開資料なし） · `008d82a0`（命令位置の公開資料なし）

~~~diff
- 008d81ac ["CBRANCH", null, ["local:b13:8", "register:102:1"]]
- 008d81ac bytes 82010054
+ 008d8348 ["CBRANCH", null, ["local:b12:8", "register:102:1"]]
+ 008d8348 bytes 82010054
- 008d8104 ["INT_ADD", "register:40f0:8", ["const:8d8104:8", "const:4:8"]]
- 008d8104 ["CALL", null, ["callee:00c57eb0:8"]]
+ 008d82a0 ["INT_ADD", "register:40f0:8", ["const:8d82a0:8", "const:4:8"]]
+ 008d82a0 ["CALL", null, ["callee:00c57eb0:8"]]
- 008d8104 bytes 6bfe0d94
+ 008d82a0 bytes 04ff0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17f86a279ec4097711c77f51aedcac5e"></a>

### [`008d8c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8c68.md) → [`008d8e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8e04.md) FUN_008d8e04

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

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
      "site": "008d8c90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008d8e2c"
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
      "unmatched:008d8c90",
      "DATA",
      [
        "storage",
        "00c84598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8e2c",
      "DATA",
      [
        "storage",
        "00c84998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8c68.md#insn-008d8c90) · [`008d8c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8c68.md#insn-008d8c7c)
- 新版 `008d8e2c`（命令位置の公開資料なし） · `008d8e18`（命令位置の公開資料なし）

~~~diff
- 008d8c90 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008d8c90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008d8c90 bytes 080000f9
+ 008d8e2c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008d8e2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008d8e2c bytes 080000f9
- 008d8c7c ["INT_ADD", "register:40f0:8", ["const:8d8c7c:8", "const:4:8"]]
- 008d8c7c ["CALL", null, ["callee:00c57e90:8"]]
+ 008d8e18 ["INT_ADD", "register:40f0:8", ["const:8d8e18:8", "const:4:8"]]
+ 008d8e18 ["CALL", null, ["callee:00c57e90:8"]]
- 008d8c7c bytes 85fb0d94
+ 008d8e18 bytes 1efc0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec98b85fe64ee6d6b9606a153ba569b5"></a>

### [`008d9270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9270.md) → [`008d940c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d940c.md) FUN_008d940c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "008d9270"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9270"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9274"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d9270",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d9274",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d9294",
      "DATA",
      [
        "storage",
        "00c84608",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d940c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008d9410",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008d9430",
      "DATA",
      [
        "storage",
        "00c84a08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d9270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9270.md#insn-008d9270) · [`008d9274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9270.md#insn-008d9274) · [`008d9294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9270.md#insn-008d9294)

~~~diff
- 008d9270 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d9270 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d9270 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008d9270 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008d9270 bytes fd7bbea9
- 008d9274 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008d9274 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008d9274 bytes f30b00f9
- 008d9294 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008d9294 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008d9294 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-902e7f1bbb6caba1202a992a74be6f00"></a>

### [`008d92c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d92c8.md) → [`008d9464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9464.md) FUN_008d9464

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0058fb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fb40.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058fb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fb80.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d92f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008d9494"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008d92f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d92c8.md#insn-008d92f8) · [`008d92ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d92c8.md#insn-008d92ec)
- 新版 `008d9494`（命令位置の公開資料なし） · `008d9488`（命令位置の公開資料なし）

~~~diff
- 008d92f8 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 008d92f8 ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 008d92f8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 008d92f8 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 008d92f8 bytes 686a3438
+ 008d9494 ["COPY", "tmp:0:4", ["register:4040:4"]]
+ 008d9494 ["COPY", "tmp:1:8", ["register:40a0:8"]]
+ 008d9494 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 008d9494 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 008d9494 bytes 686a3438
- 008d92ec ["INT_ADD", "register:40f0:8", ["const:8d92ec:8", "const:4:8"]]
- 008d92ec ["CALL", null, ["callee:0058fb80:8"]]
+ 008d9488 ["INT_ADD", "register:40f0:8", ["const:8d9488:8", "const:4:8"]]
+ 008d9488 ["CALL", null, ["callee:0058fb80:8"]]
- 008d92ec bytes 15daf297
+ 008d9488 bytes bed9f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2110d27f7aa3e33efddbec75deb050cb"></a>

### [`008d9348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9348.md) → [`008d94e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d94e4.md) FUN_008d94e4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "008d936c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d936c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008d9508"
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
      "unmatched:008d936c",
      "DATA",
      [
        "storage",
        "00c846a8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008d9370",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d9374",
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
      "008d9508",
      "DATA",
      [
        "storage",
        "00c84aa8",
        null,
        "undefined *"
      ]
    ],
    [
      "008d950c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008d9510",
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

- 旧版 [`008d936c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9348.md#insn-008d936c) · [`008d9378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9348.md#insn-008d9378)
- 新版 `008d9508`（命令位置の公開資料なし）

~~~diff
- 008d936c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d936c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008d936c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008d936c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d936c bytes 082400a9
- 008d9378 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008d9378 ["RETURN", null, ["register:0:8"]]
- 008d9378 bytes c0035fd6
+ 008d9508 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008d9508 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 008d9508 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 008d9508 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008d9508 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5526bd66242f8570ab470a0f67d4ff9a"></a>

### [`008d9520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9520.md) → [`008d96bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d96bc.md) FUN_008d96bc

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "008d9544"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9544"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008d96e0"
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
      "unmatched:008d9544",
      "DATA",
      [
        "storage",
        "00c84718",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008d9548",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d954c",
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
      "008d96e0",
      "DATA",
      [
        "storage",
        "00c84b18",
        null,
        "undefined *"
      ]
    ],
    [
      "008d96e4",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008d96e8",
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

- 旧版 [`008d9544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9520.md#insn-008d9544) · [`008d9550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9520.md#insn-008d9550)
- 新版 `008d96e0`（命令位置の公開資料なし）

~~~diff
- 008d9544 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d9544 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008d9544 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008d9544 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d9544 bytes 082400a9
- 008d9550 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008d9550 ["RETURN", null, ["register:0:8"]]
- 008d9550 bytes c0035fd6
+ 008d96e0 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008d96e0 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 008d96e0 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 008d96e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008d96e0 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f3fdc53bc5a37de6477078ea038b939"></a>

### [`008d9554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9554.md) → [`008d96f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d96f0.md) FUN_008d96f0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "008d9560"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9560"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008d96fc"
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
      "unmatched:008d9560",
      "DATA",
      [
        "storage",
        "00c84718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d96fc",
      "DATA",
      [
        "storage",
        "00c84b18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d9560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9554.md#insn-008d9560) · [`008d9564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9554.md#insn-008d9564)
- 新版 `008d96fc`（命令位置の公開資料なし）

~~~diff
- 008d9560 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008d9560 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 008d9560 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 008d9560 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d9560 bytes 292000a9
- 008d9564 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008d9564 ["RETURN", null, ["register:0:8"]]
- 008d9564 bytes c0035fd6
+ 008d96fc ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 008d96fc ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 008d96fc ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 008d96fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008d96fc bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-add4d5ff09cec6ad41cb9f019037eb44"></a>

### [`008d9770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9770.md) → [`008d990c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d990c.md) FUN_008d990c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`008d809c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d809c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 5件 [`008d8238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8238.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 68.97% / 新版 68.97%

CFGの説明率　旧版 54.55% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9770"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9770"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9774"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d9770",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d9774",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d9778",
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
      "008d990c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008d9910",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "008d9914",
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

- 旧版 [`008d9770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9770.md#insn-008d9770) · [`008d9774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9770.md#insn-008d9774) · [`008d9778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9770.md#insn-008d9778)

~~~diff
- 008d9770 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d9770 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d9770 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 008d9770 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008d9770 bytes fd7bbca9
- 008d9774 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008d9774 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 008d9774 bytes f70b00f9
- 008d9778 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 008d9778 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 008d9778 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008d9778 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d9778 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-085d2e0587094d56163a8af93de5e865"></a>

### [`008dce94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dce94.md) → [`008dd030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008dd030.md) FUN_008dd030

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008dcf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dcf58.md) · 呼出先 3件 [`008df27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008df/008df27c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a450.md)
- 新版 呼出元 1件 [`008dd0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008dd0f4.md) · 呼出先 3件 [`008df418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008df/008df418.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a850.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 74.42% / 新版 74.42%

CFGの説明率　旧版 69.23% / 新版 81.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008dce94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008dce94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008dce98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008dce94",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:008dce98",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:008dce9c",
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
      "008dd030",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008dd034",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "008dd038",
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

- 旧版 [`008dce94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dce94.md#insn-008dce94) · [`008dce98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dce94.md#insn-008dce98) · [`008dce9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dce94.md#insn-008dce9c)

~~~diff
- 008dce94 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008dce94 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008dce94 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 008dce94 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008dce94 bytes fd7bbca9
- 008dce98 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008dce98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 008dce98 bytes f70b00f9
- 008dce9c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 008dce9c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 008dce9c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008dce9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008dce9c bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce9bc011d39d9e0ad0a8512434628804"></a>

### [`008ddabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008ddabc.md) → [`008ddc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008ddc58.md) FUN_008ddc58

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008dde04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008dde04.md) · 呼出先 1件 [`008dbf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008db/008dbf84.md)
- 新版 呼出元 1件 [`008ddfa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008ddfa0.md) · 呼出先 1件 [`008dc120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dc/008dc120.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 60.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008ddae8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008ddc84"
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
      "unmatched:008ddae8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ddca4"
      ]
    ]
  ],
  "added": [
    [
      "008ddc84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ddca4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ddae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008ddabc.md#insn-008ddae8) · [`008ddae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008ddabc.md#insn-008ddae4)
- 新版 `008ddc84`（命令位置の公開資料なし）

~~~diff
- 008ddae8 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 008ddae8 bytes 00010054
+ 008ddc84 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 008ddc84 bytes 00010054
- 008ddae4 ["INT_LESSEQUAL", "register:105:1", ["register:40a8:8", "register:40a0:8"]]
- 008ddae4 ["INT_SBORROW", "register:106:1", ["register:40a0:8", "register:40a8:8"]]
- 008ddae4 ["INT_SUB", "tmp:0:8", ["register:40a0:8", "register:40a8:8"]]
- 008ddae4 ["INT_SLESS", "register:107:1", ["tmp:0:8", "const:0:8"]]
- 008ddae4 bytes 9f0215eb
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4abc63eef15737f78a4f987adcac4acc"></a>

### [`008e8dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8dec.md) → [`008e8f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8f88.md) FUN_008e8f88

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008e2720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e2/008e2720.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`008e8868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8868.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`008e28bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e2/008e28bc.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`008e8a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e8/008e8a04.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 98.78% / 新版 98.78%

CFGの説明率　旧版 91.67% / 新版 88.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008e8f24"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "008e90c0"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008e8f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8dec.md#insn-008e8f24) · [`008e8e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e8/008e8dec.md#insn-008e8e18)
- 新版 `008e90c0`（命令位置の公開資料なし） · `008e8fb4`（命令位置の公開資料なし）

~~~diff
- 008e8f24 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008e8f24 ["RETURN", null, ["register:0:8"]]
- 008e8f24 bytes c0035fd6
+ 008e90c0 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 008e90c0 ["RETURN", null, ["register:0:8"]]
+ 008e90c0 bytes c0035fd6
- 008e8e18 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 008e8e18 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
+ 008e8fb4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
+ 008e8fb4 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 008e8e18 bytes 8a0800b5
+ 008e8fb4 bytes 8a0800b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f12867277c680c95b54d43b2f8e90a61"></a>

### [`008e9150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9150.md) → [`008e92ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e92ec.md) FUN_008e92ec

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

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
      "site": "008e9174"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e9174"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008e9310"
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
      "unmatched:008e9174",
      "DATA",
      [
        "storage",
        "00c84ce0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008e9178",
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
      "008e9310",
      "DATA",
      [
        "storage",
        "00c850e0",
        null,
        "undefined *"
      ]
    ],
    [
      "008e9314",
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

- 旧版 [`008e9174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9150.md#insn-008e9174) · [`008e9164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9150.md#insn-008e9164)
- 新版 `008e9310`（命令位置の公開資料なし） · `008e9300`（命令位置の公開資料なし）

~~~diff
- 008e9174 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008e9174 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008e9174 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008e9174 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008e9174 bytes 082400a9
+ 008e9310 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008e9310 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 008e9310 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 008e9310 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008e9310 bytes 082400a9
- 008e9164 ["INT_ADD", "register:40f0:8", ["const:8e9164:8", "const:4:8"]]
- 008e9164 ["CALL", null, ["callee:00c57e90:8"]]
+ 008e9300 ["INT_ADD", "register:40f0:8", ["const:8e9300:8", "const:4:8"]]
+ 008e9300 ["CALL", null, ["callee:00c57e90:8"]]
- 008e9164 bytes 4bba0d94
+ 008e9300 bytes e4ba0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-818f6f54a54d36e759cf4644a8729579"></a>

### [`008e92d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e92d0.md) → [`008e946c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e946c.md) FUN_008e946c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "008e92f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e92f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008e9490"
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
      "unmatched:008e92f4",
      "DATA",
      [
        "storage",
        "00c84d60",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008e92f8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008e92fc",
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
      "008e9490",
      "DATA",
      [
        "storage",
        "00c85160",
        null,
        "undefined *"
      ]
    ],
    [
      "008e9494",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008e9498",
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

- 旧版 [`008e92f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e92d0.md#insn-008e92f4) · [`008e9300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e92d0.md#insn-008e9300)
- 新版 `008e9490`（命令位置の公開資料なし）

~~~diff
- 008e92f4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008e92f4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008e92f4 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008e92f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008e92f4 bytes 082400a9
- 008e9300 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008e9300 ["RETURN", null, ["register:0:8"]]
- 008e9300 bytes c0035fd6
+ 008e9490 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008e9490 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 008e9490 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 008e9490 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008e9490 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd2ebe53a4775c54a290ec88e65fd1cc"></a>

### [`008e93cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e93cc.md) → [`008e9568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e9568.md) FUN_008e9568

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

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
      "site": "008e93f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e93f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008e958c"
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
      "unmatched:008e93f0",
      "DATA",
      [
        "storage",
        "00c84de0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008e93f8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008e93fc",
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
      "008e958c",
      "DATA",
      [
        "storage",
        "00c851e0",
        null,
        "undefined *"
      ]
    ],
    [
      "008e9594",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008e9598",
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

- 旧版 [`008e93f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e93cc.md#insn-008e93f0) · [`008e93f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e93cc.md#insn-008e93f4) · [`008e9400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e93cc.md#insn-008e9400)

~~~diff
- 008e93f0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008e93f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008e93f0 bytes 080000f9
- 008e93f4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 008e93f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008e93f4 bytes 0080803c
- 008e9400 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008e9400 ["RETURN", null, ["register:0:8"]]
- 008e9400 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad50bb6b348d801b8853da1a2b3e3678"></a>

### [`008e9404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9404.md) → [`008e95a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e9/008e95a0.md) FUN_008e95a0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "008e940c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008e9414"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008e95a8"
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
      "unmatched:008e940c",
      "DATA",
      [
        "storage",
        "00c84de0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008e95a8",
      "DATA",
      [
        "storage",
        "00c851e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008e940c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9404.md#insn-008e940c) · [`008e9414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9404.md#insn-008e9414) · [`008e9418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e9/008e9404.md#insn-008e9418)

~~~diff
- 008e940c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008e940c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008e940c bytes 280000f9
- 008e9414 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 008e9414 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008e9414 bytes 2080803c
- 008e9418 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008e9418 ["RETURN", null, ["register:0:8"]]
- 008e9418 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-628ee126b4b69a606e0d3e7215242906"></a>

### [`008eb7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb7ec.md) → [`008eb988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008eb988.md) FUN_008eb988

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`008eb2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb2ec.md) [`008ec104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ec/008ec104.md) [`008f5214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5214.md) [`008f694c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f694c.md) · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008c4784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c4/008c4784.md) [`008caa20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa20.md)
- 新版 呼出元 4件 [`008eb488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008eb488.md) [`008ec2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ec/008ec2a0.md) [`008f53b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f53b0.md) [`008f7008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f7/008f7008.md) · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008c4920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c4/008c4920.md) [`008cabbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008cabbc.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.06% / 新版 83.06%

CFGの説明率　旧版 4.35% / 新版 6.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eb7ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eb7ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008eb7f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008eb7ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008eb7f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:008eb7f4",
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
      "008eb988",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008eb98c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008eb990",
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

- 旧版 [`008eb7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb7ec.md#insn-008eb7ec) · [`008eb7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb7ec.md#insn-008eb7f0) · [`008eb7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb7ec.md#insn-008eb7f4)

~~~diff
- 008eb7ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008eb7ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008eb7ec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 008eb7ec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008eb7ec bytes fd7bbba9
- 008eb7f0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008eb7f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 008eb7f0 bytes f90b00f9
- 008eb7f4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 008eb7f4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 008eb7f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008eb7f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008eb7f4 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2b79b2092a7715656af3a0484fd759e"></a>

### [`008f2148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f2148.md) → [`008f22e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f2/008f22e4.md) FUN_008f22e4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008f2ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f2ea8.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`008f3044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f3/008f3044.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 81.08% / 新版 81.08%

CFGの説明率　旧版 11.11% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008f21d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "008f2374"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008f21d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f2148.md#insn-008f21d8) · [`008f215c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f2/008f2148.md#insn-008f215c)
- 新版 `008f2374`（命令位置の公開資料なし） · `008f22f8`（命令位置の公開資料なし）

~~~diff
- 008f21d8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008f21d8 ["RETURN", null, ["register:0:8"]]
- 008f21d8 bytes c0035fd6
+ 008f2374 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 008f2374 ["RETURN", null, ["register:0:8"]]
+ 008f2374 bytes c0035fd6
- 008f215c ["INT_ADD", "register:40f0:8", ["const:8f215c:8", "const:4:8"]]
- 008f215c ["CALL", null, ["callee:008514f8:8"]]
+ 008f22f8 ["INT_ADD", "register:40f0:8", ["const:8f22f8:8", "const:4:8"]]
+ 008f22f8 ["CALL", null, ["callee:008514f8:8"]]
- 008f215c bytes d77cfd97
+ 008f22f8 bytes 807cfd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c90dc92b516c61e96f831536a27e974"></a>

### [`008f9a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9a78.md) → [`008f9c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f9c14.md) FUN_008f9c14

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`008eb380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008eb/008eb380.md) [`008f380c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f3/008f380c.md) [`008f5214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5214.md) [`008f5a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5a48.md) [`008f6148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f6/008f6148.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 7件 [`008eb51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008eb/008eb51c.md) [`008f39a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f3/008f39a8.md) [`008f53b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f53b0.md) [`008f5be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f5be4.md) [`008f62e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f62e4.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 94.85% / 新版 94.85%

CFGの説明率　旧版 68.42% / 新版 65.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f9b80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f9b84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f9b88"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008f9b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9a78.md#insn-008f9b80) · [`008f9b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9a78.md#insn-008f9b84) · [`008f9b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9a78.md#insn-008f9b88)

~~~diff
- 008f9b80 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:58:8"]]
- 008f9b80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4060:8"]]
- 008f9b80 bytes 0c2c00f9
- 008f9b84 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:48:8"]]
- 008f9b84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008f9b84 bytes 0080843c
- 008f9b88 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:38:8"]]
- 008f9b88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008f9b88 bytes 0080833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1371520795040d457ac3421e71d90fdd"></a>

### [`008f9c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9c6c.md) → [`008f9e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f9e08.md) FUN_008f9e08

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`008f5150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f5/008f5150.md) [`008f9c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9c6c.md) [`008fa0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa0e0.md) · 呼出先 4件 [`008f9c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9c6c.md) [`008f9f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9f70.md) [`008fa0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa0e0.md) [`008fa3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fa3a8.md)
- 新版 呼出元 3件 [`008f52ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f5/008f52ec.md) [`008f9e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f9e08.md) [`008fa27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fa27c.md) · 呼出先 4件 [`008f9e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f9/008f9e08.md) [`008fa10c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fa10c.md) [`008fa27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fa27c.md) [`008fa544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fa544.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 96.37% / 新版 96.37%

CFGの説明率　旧版 87.69% / 新版 89.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f9c6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f9c6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008f9c70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008f9c6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008f9c70",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:008f9c74",
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
      "008f9e08",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008f9e0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008f9e10",
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

- 旧版 [`008f9c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9c6c.md#insn-008f9c6c) · [`008f9c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9c6c.md#insn-008f9c70) · [`008f9c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008f9/008f9c6c.md#insn-008f9c74)

~~~diff
- 008f9c6c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008f9c6c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008f9c6c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 008f9c6c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008f9c6c bytes fd7bbba9
- 008f9c70 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008f9c70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 008f9c70 bytes f90b00f9
- 008f9c74 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 008f9c74 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 008f9c74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008f9c74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008f9c74 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-363bcb494022adfe1bc3515e95f0fac6"></a>

### [`008fac24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fac24.md) → [`008fadc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fadc0.md) FUN_008fadc0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "008fac3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008fadd8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008fac44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008fac3c",
      "DATA",
      [
        "storage",
        "00c85668",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008fac40",
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
      "008fadd8",
      "DATA",
      [
        "storage",
        "00c85a68",
        null,
        "undefined *"
      ]
    ],
    [
      "008faddc",
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

- 旧版 [`008fac3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fac24.md#insn-008fac3c) · [`008fac44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fa/008fac24.md#insn-008fac44)
- 新版 `008fadd8`（命令位置の公開資料なし）

~~~diff
- 008fac3c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008fac3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008fac3c bytes 080000f9
- 008fac44 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008fac44 ["RETURN", null, ["register:0:8"]]
- 008fac44 bytes c0035fd6
+ 008fadd8 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008fadd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008fadd8 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd499a5c957915ee488bef564efd77c3"></a>

### [`008ff060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff060.md) → [`008ff1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff1fc.md) FUN_008ff1fc

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "008ff084"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ff084"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008ff220"
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
      "unmatched:008ff084",
      "DATA",
      [
        "storage",
        "00c85730",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008ff088",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ff08c",
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
      "008ff220",
      "DATA",
      [
        "storage",
        "00c85b30",
        null,
        "undefined *"
      ]
    ],
    [
      "008ff224",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008ff228",
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

- 旧版 [`008ff084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff060.md#insn-008ff084) · [`008ff090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff060.md#insn-008ff090)
- 新版 `008ff220`（命令位置の公開資料なし）

~~~diff
- 008ff084 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008ff084 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008ff084 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008ff084 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ff084 bytes 082400a9
- 008ff090 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008ff090 ["RETURN", null, ["register:0:8"]]
- 008ff090 bytes c0035fd6
+ 008ff220 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008ff220 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 008ff220 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 008ff220 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008ff220 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d6dade317ae80af49f76256e0668090"></a>

### [`008ff094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff094.md) → [`008ff230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff230.md) FUN_008ff230

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "008ff0a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ff0a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008ff23c"
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
      "unmatched:008ff0a0",
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
      "008ff23c",
      "DATA",
      [
        "storage",
        "00c85b30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ff0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff094.md#insn-008ff0a0) · [`008ff0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff094.md#insn-008ff0a4)
- 新版 `008ff23c`（命令位置の公開資料なし）

~~~diff
- 008ff0a0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008ff0a0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 008ff0a0 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 008ff0a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ff0a0 bytes 292000a9
- 008ff0a4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008ff0a4 ["RETURN", null, ["register:0:8"]]
- 008ff0a4 bytes c0035fd6
+ 008ff23c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 008ff23c ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 008ff23c ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 008ff23c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008ff23c bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ce71c9fe7556bcb96b51ad7fd611e7b"></a>

### [`008ff4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff4e0.md) → [`008ff67c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff67c.md) FUN_008ff67c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008ff1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff1cc.md) [`008ff220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff220.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`006917c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00691/006917c0.md)
- 新版 呼出元 2件 [`008ff368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff368.md) [`008ff3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff3bc.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00691800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691800.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008ff4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff4e0.md#insn-008ff4f4) · [`008ff514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff4e0.md#insn-008ff514) · [`008ff528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff4e0.md#insn-008ff528)
- 新版 `008ff6b0`（命令位置の公開資料なし） · `008ff6c4`（命令位置の公開資料なし）

~~~diff
- 008ff4f4 ["COPY", "register:40e8:8", ["register:8:8"]]
- 008ff4f4 bytes fd030091
- 008ff514 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 008ff514 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 008ff514 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 008ff514 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 008ff6b0 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
+ 008ff6b0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 008ff6b0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 008ff6b0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 008ff514 bytes c9000037
+ 008ff6b0 bytes c9000037
- 008ff528 ["BRANCH", null, ["local:b3:8"]]
+ 008ff6c4 ["BRANCH", null, ["local:b4:8"]]
- 008ff528 bytes 04000014
+ 008ff6c4 bytes 04000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ab94a24119136f719cbc2b04eb07d01"></a>

### [`00901424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00901/00901424.md) → [`009015c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/009015c0.md) FUN_009015c0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "site": "00901430"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00901430"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009015cc"
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
      "unmatched:00901430",
      "DATA",
      [
        "storage",
        "00c85950",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009015cc",
      "DATA",
      [
        "storage",
        "00c85d50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00901430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00901/00901424.md#insn-00901430) · [`0090142c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00901/00901424.md#insn-0090142c)
- 新版 `009015cc`（命令位置の公開資料なし）

~~~diff
- 00901430 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00901430 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00901430 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00901430 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00901430 bytes 292000a9
+ 009015cc ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 009015cc ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 009015cc ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 009015cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 009015cc bytes 292000a9
- 0090142c ["COPY", "tmp:0:8", ["const:950:8"]]
- 0090142c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0090142c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0090142c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0090142c bytes 29412591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c467db4fbbe1c15efaa3c4e6e9cc4d3f"></a>

### [`00901560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00901/00901560.md) → [`009016fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/009016fc.md) FUN_009016fc

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00901584"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00901584"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00901720"
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
      "unmatched:00901584",
      "DATA",
      [
        "storage",
        "00c859c0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00901588",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0090158c",
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
      "00901720",
      "DATA",
      [
        "storage",
        "00c85dc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00901724",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00901728",
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

- 旧版 [`00901584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00901/00901560.md#insn-00901584) · [`00901590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00901/00901560.md#insn-00901590)
- 新版 `00901720`（命令位置の公開資料なし）

~~~diff
- 00901584 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00901584 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00901584 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00901584 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00901584 bytes 082400a9
- 00901590 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00901590 ["RETURN", null, ["register:0:8"]]
- 00901590 bytes c0035fd6
+ 00901720 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00901720 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00901720 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00901720 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00901720 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90f59014b5297ffecaae38058a670d49"></a>

### [`0091a884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a884.md) → [`0091aa20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0091a/0091aa20.md) FUN_0091aa20

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`009113c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00911/009113c4.md) [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) [`0091a9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a9dc.md) [`009222f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00922/009222f8.md) · 呼出先 8件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0071ac94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071ac94.md) [`0071acbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071acbc.md) [`0071b4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071b4e4.md) [`0071b894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071b894.md)
- 新版 呼出元 4件 [`00911560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00911/00911560.md) [`00914e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00914/00914e30.md) [`0091ab78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0091a/0091ab78.md) [`00922494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00922/00922494.md) · 呼出先 8件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0071acd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071a/0071acd4.md) [`0071acfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071a/0071acfc.md) [`0071b524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071b524.md) [`0071b8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071b8d4.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 87.21% / 新版 87.21%

CFGの説明率　旧版 31.43% / 新版 34.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0091a8a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0091a8b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0091a8c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0091a89c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00811928"
      ]
    ],
    [
      "unmatched:0091a8a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0091ab60"
      ]
    ],
    [
      "unmatched:0091a8ac",
      "DATA",
      [
        "storage",
        "0033a2e8",
        null,
        "fde_table_entry"
      ]
    ]
  ],
  "added": [
    [
      "0091aa38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00811968"
      ]
    ],
    [
      "0091aa3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0091ab60"
      ]
    ],
    [
      "0091aa48",
      "DATA",
      [
        "storage",
        "0033a2e8",
        null,
        "fde_table_entry"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0091a89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a884.md#insn-0091a89c) · [`0091a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a884.md#insn-0091a8a0) · [`0091a8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a884.md#insn-0091a8b4)

~~~diff
- 0091a89c ["INT_ADD", "register:40f0:8", ["const:91a89c:8", "const:4:8"]]
- 0091a89c ["CALL", null, ["ram:811928:8"]]
- 0091a89c bytes 23dcfb97
- 0091a8a0 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 0091a8a0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0091a8a0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0091a8a0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 0091a8a0 bytes 20090036
- 0091a8b4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0091a8b4 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 0091a8b4 bytes 81080054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f9420430c893ae6cdec619efe9a3102"></a>

### [`0091fdc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091f/0091fdc0.md) → [`0091ff5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0091f/0091ff5c.md) FUN_0091ff5c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00920118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00920/00920118.md) [`00a7d968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7d968.md) [`00a7d9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7d9f4.md) · 呼出先 7件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00672708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672708.md) [`006821d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006821d8.md) [`0092013c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00920/0092013c.md)
- 新版 呼出元 3件 [`009202b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00920/009202b4.md) [`00a7db60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7d/00a7db60.md) [`00a7dbec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a7d/00a7dbec.md) · 呼出先 7件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00672748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672748.md) [`00682218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682218.md) [`009202d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00920/009202d8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.79% / 新版 95.79%

CFGの説明率　旧版 85.42% / 新版 83.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0091fde0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0091ff7c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0091fdf4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0091fde0",
      "DATA",
      [
        "storage",
        "00c85a50",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0091fdf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0091ffac"
      ]
    ]
  ],
  "added": [
    [
      "0091ff7c",
      "DATA",
      [
        "storage",
        "00c85e50",
        null,
        "pointer"
      ]
    ],
    [
      "0091ff90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0091ffac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0091fde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091f/0091fdc0.md#insn-0091fde0) · [`0091fdf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091f/0091fdc0.md#insn-0091fdf4)
- 新版 `0091ff7c`（命令位置の公開資料なし）

~~~diff
- 0091fde0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0091fde0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0091fde0 bytes 080000f9
- 0091fdf4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0091fdf4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 0091fdf4 bytes e00000b5
+ 0091ff7c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 0091ff7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0091ff7c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95aa24d89fde2a0cf913737584dbf6df"></a>

### [`009215d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00921/009215d0.md) → [`0092176c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00921/0092176c.md) FUN_0092176c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "009215d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009215d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009215d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009215d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009215d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009215f4",
      "DATA",
      [
        "storage",
        "00c85a90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0092176c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00921770",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00921790",
      "DATA",
      [
        "storage",
        "00c85e90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009215d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00921/009215d0.md#insn-009215d0) · [`009215d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00921/009215d0.md#insn-009215d4) · [`009215f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00921/009215d0.md#insn-009215f4)

~~~diff
- 009215d0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009215d0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009215d0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009215d0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009215d0 bytes fd7bbea9
- 009215d4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009215d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 009215d4 bytes f30b00f9
- 009215f4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009215f4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 009215f4 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 009215f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009215f4 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17cda6e46c12115469ec4b1ef8cf152e"></a>

### [`00921668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00921/00921668.md) → [`00921804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00921/00921804.md) FUN_00921804

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "0092168c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0092168c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00921828"
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
      "unmatched:0092168c",
      "DATA",
      [
        "storage",
        "00c85b10",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00921690",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00921694",
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
      "00921828",
      "DATA",
      [
        "storage",
        "00c85f10",
        null,
        "undefined *"
      ]
    ],
    [
      "0092182c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00921830",
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

- 旧版 [`0092168c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00921/00921668.md#insn-0092168c) · [`00921698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00921/00921668.md#insn-00921698)
- 新版 `00921828`（命令位置の公開資料なし）

~~~diff
- 0092168c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0092168c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0092168c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0092168c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0092168c bytes 082400a9
- 00921698 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00921698 ["RETURN", null, ["register:0:8"]]
- 00921698 bytes c0035fd6
+ 00921828 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00921828 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00921828 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00921828 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00921828 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71609c623fc06aed650faa29989322aa"></a>

### [`009216f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00921/009216f4.md) → [`00921890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00921/00921890.md) FUN_00921890

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "009216f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009216f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0092170c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009216f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00921700",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "unmatched:0092170c",
      "DATA",
      [
        "storage",
        "00c85b90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00921890",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0092189c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "009218a8",
      "DATA",
      [
        "storage",
        "00c85f90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009216f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00921/009216f4.md#insn-009216f4) · [`00921700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00921/009216f4.md#insn-00921700) · [`0092170c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00921/009216f4.md#insn-0092170c)

~~~diff
- 009216f4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009216f4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009216f4 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 009216f4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009216f4 bytes fd7bbfa9
- 00921700 ["INT_ADD", "register:40f0:8", ["const:921700:8", "const:4:8"]]
- 00921700 ["CALL", null, ["callee:00c57e90:8"]]
- 00921700 bytes e4d80c94
- 0092170c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0092170c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0092170c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c5889d0bd3bb7c915cbe19687193718"></a>

### [`009217a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00921/009217a4.md) → [`00921940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00921/00921940.md) FUN_00921940

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "009217bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00921958"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "009217c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009217bc",
      "DATA",
      [
        "storage",
        "00c85c10",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009217c0",
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
      "00921958",
      "DATA",
      [
        "storage",
        "00c86010",
        null,
        "undefined *"
      ]
    ],
    [
      "0092195c",
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

- 旧版 [`009217bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00921/009217a4.md#insn-009217bc) · [`009217c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00921/009217a4.md#insn-009217c4)
- 新版 `00921958`（命令位置の公開資料なし）

~~~diff
- 009217bc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 009217bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009217bc bytes 080000f9
- 009217c4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 009217c4 ["RETURN", null, ["register:0:8"]]
- 009217c4 bytes c0035fd6
+ 00921958 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00921958 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00921958 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-007cc2a214d0e3086891bcd0617cb162"></a>

### [`00926cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00926/00926cc4.md) → [`00926e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00926/00926e60.md) FUN_00926e60

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00926f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00926/00926f00.md) · 呼出先 6件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00672b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672b08.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0092709c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00927/0092709c.md) · 呼出先 6件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00672b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672b48.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.21% / 新版 90.21%

CFGの説明率　旧版 73.44% / 新版 85.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00926cc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00926cc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00926cc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00926cc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00926cc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00926ccc",
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
      "00926e60",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00926e64",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00926e68",
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

- 旧版 [`00926cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00926/00926cc4.md#insn-00926cc4) · [`00926cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00926/00926cc4.md#insn-00926cc8) · [`00926ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00926/00926cc4.md#insn-00926ccc)

~~~diff
- 00926cc4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00926cc4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00926cc4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00926cc4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00926cc4 bytes fd7bbda9
- 00926cc8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00926cc8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00926cc8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00926cc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00926cc8 bytes f65701a9
- 00926ccc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00926ccc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00926ccc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00926ccc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00926ccc bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a3d5c859d566338d29a3e2f0e9eb81a"></a>

### [`00927f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00927/00927f7c.md) → [`00928118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00928/00928118.md) FUN_00928118

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 1件 [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md)
- 新版 呼出元 2件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 1件 [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00927fa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00928140"
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
      "unmatched:00927fa4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0049f3f0"
      ]
    ]
  ],
  "added": [
    [
      "00928140",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0049f3f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00927fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00927/00927f7c.md#insn-00927fa4) · [`00927fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00927/00927f7c.md#insn-00927fa0)
- 新版 `00928140`（命令位置の公開資料なし）

~~~diff
- 00927fa4 ["INT_ADD", "register:40f0:8", ["const:927fa4:8", "const:4:8"]]
- 00927fa4 ["CALL", null, ["callee:0049f3f0:8"]]
- 00927fa4 bytes 03dded97
+ 00928140 ["INT_ADD", "register:40f0:8", ["const:928140:8", "const:4:8"]]
+ 00928140 ["CALL", null, ["callee:0049f3f0:8"]]
+ 00928140 bytes acdced97
- 00927fa0 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00927fa0 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ce2e6785d4d8933a396974a7253c2d0"></a>

### [`00929a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929a70.md) → [`00929c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929c0c.md) FUN_00929c0c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 3件 [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md) [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md) [`00481058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481058.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 3件 [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md) [`00481098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481098.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

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
      "site": "00929a74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00929a74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00929c10"
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
      "unmatched:00929a74",
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
      "00929c10",
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

- 旧版 [`00929a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929a70.md#insn-00929a74) · [`00929a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929a70.md#insn-00929a78)
- 新版 `00929c10`（命令位置の公開資料なし） · `00929c34`（命令位置の公開資料なし）

~~~diff
- 00929a74 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00929a74 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00929a74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00929a74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00929a74 bytes f44f01a9
+ 00929c10 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00929c10 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00929c10 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
+ 00929c10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00929c10 bytes f44f01a9
- 00929a78 ["COPY", "register:40e8:8", ["register:8:8"]]
+ 00929c34 ["COPY", "register:4000:8", ["register:40a0:8"]]
- 00929a78 bytes fd030091
+ 00929c34 bytes e00314aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-665e80ca469cc3a964c00cfd5223fe9a"></a>

### [`00929af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929af8.md) → [`00929c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929c94.md) FUN_00929c94

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "site": "00929b04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00929b04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00929ca0"
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
      "unmatched:00929b04",
      "DATA",
      [
        "storage",
        "00c861c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00929ca0",
      "DATA",
      [
        "storage",
        "00c865c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00929b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929af8.md#insn-00929b04) · [`00929b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929af8.md#insn-00929b00)
- 新版 `00929ca0`（命令位置の公開資料なし）

~~~diff
- 00929b04 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00929b04 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00929b04 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00929b04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00929b04 bytes 292000a9
+ 00929ca0 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00929ca0 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00929ca0 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00929ca0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00929ca0 bytes 292000a9
- 00929b00 ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 00929b00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00929b00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00929b00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00929b00 bytes 29210791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8338a03652d301b08c76379a8aa67f72"></a>

### [`00929ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929ca0.md) → [`00929e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929e3c.md) FUN_00929e3c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00929cac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00929cac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00929e48"
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
      "unmatched:00929cac",
      "DATA",
      [
        "storage",
        "00c862c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00929e48",
      "DATA",
      [
        "storage",
        "00c866c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00929cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929ca0.md#insn-00929cac) · [`00929cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929ca0.md#insn-00929cb0)
- 新版 `00929e48`（命令位置の公開資料なし）

~~~diff
- 00929cac ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00929cac ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00929cac ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00929cac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00929cac bytes 292000a9
- 00929cb0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00929cb0 ["RETURN", null, ["register:0:8"]]
- 00929cb0 bytes c0035fd6
+ 00929e48 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00929e48 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00929e48 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00929e48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00929e48 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-734bcd063b1cab7eb7a1a191e6aea271"></a>

### [`00929cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929cbc.md) → [`00929e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929e58.md) FUN_00929e58

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 85.71% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00929ce4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00929e80"
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
      "unmatched:00929ce4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00929e80",
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

- 旧版 [`00929ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929cbc.md#insn-00929ce4) · [`00929cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929cbc.md#insn-00929cc8)
- 新版 `00929e80`（命令位置の公開資料なし） · `00929e64`（命令位置の公開資料なし）

~~~diff
- 00929ce4 ["INT_ADD", "register:40f0:8", ["const:929ce4:8", "const:4:8"]]
- 00929ce4 ["CALL", null, ["ram:47acb4:8"]]
- 00929ce4 bytes f443ed97
+ 00929e80 ["INT_ADD", "register:40f0:8", ["const:929e80:8", "const:4:8"]]
+ 00929e80 ["CALL", null, ["ram:47acf4:8"]]
+ 00929e80 bytes 9d43ed97
- 00929cc8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00929cc8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00929e64 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00929e64 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00929cc8 bytes e1010054
+ 00929e64 bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbb27b56d776ab7f51cef958731191bc"></a>

### [`00929e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929e54.md) → [`00929ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00929/00929ff0.md) FUN_00929ff0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00929e5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00929e64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00929ff8"
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
      "unmatched:00929e5c",
      "DATA",
      [
        "storage",
        "00c863c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00929ff8",
      "DATA",
      [
        "storage",
        "00c867c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00929e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929e54.md#insn-00929e5c) · [`00929e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929e54.md#insn-00929e64) · [`00929e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929e54.md#insn-00929e68)

~~~diff
- 00929e5c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00929e5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00929e5c bytes 280000f9
- 00929e64 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00929e64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:8:8"]]
- 00929e64 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00929e64 bytes 28200039
- 00929e68 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00929e68 ["RETURN", null, ["register:0:8"]]
- 00929e68 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a1a62eb58e4b08232e0b5fb37445271"></a>

### [`00929e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929e74.md) → [`0092a010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0092a/0092a010.md) FUN_0092a010

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00929eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929eb4.md)
- 新版 呼出元 0件  · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0092a050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0092a/0092a050.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00929e74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00929e74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0092a010"
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
      "unmatched:00929e74",
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
      "0092a010",
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

- 旧版 [`00929e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929e74.md#insn-00929e74) · [`00929e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929e74.md#insn-00929e78)
- 新版 `0092a010`（命令位置の公開資料なし）

~~~diff
- 00929e74 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00929e74 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00929e74 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00929e74 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00929e74 bytes fd7bbfa9
+ 0092a010 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0092a010 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0092a010 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 0092a010 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0092a010 bytes fd7bbfa9
- 00929e78 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00929e78 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed6d3376ce65ce1b0a156f535984d02d"></a>

### [`00929eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929eb4.md) → [`0092a050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0092a/0092a050.md) FUN_0092a050

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00929e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929e74.md) [`0092a238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092a/0092a238.md) · 呼出先 10件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`0055097c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055097c.md) [`00597e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e88.md)
- 新版 呼出元 2件 [`0092a010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0092a/0092a010.md) [`0092a3d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0092a/0092a3d4.md) · 呼出先 10件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`005509bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509bc.md) [`00597ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ec8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.39% / 新版 89.39%

CFGの説明率　旧版 76.92% / 新版 68.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00929f2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00929f38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00929f5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00929f2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "unmatched:00929f38",
      "WRITE",
      [
        "storage",
        "Stack[-0x87]",
        null,
        null
      ]
    ],
    [
      "unmatched:00929f54",
      "READ",
      [
        "storage",
        "002aef82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0092a0c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "0092a0d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x87]",
        null,
        null
      ]
    ],
    [
      "0092a0f0",
      "READ",
      [
        "storage",
        "002aefc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00929f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929eb4.md#insn-00929f2c) · [`00929f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929eb4.md#insn-00929f38) · [`00929f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00929/00929eb4.md#insn-00929f5c)

~~~diff
- 00929f2c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00929f2c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 00929f2c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00929f2c bytes a8831b38
- 00929f38 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00929f38 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb9:8"]]
- 00929f38 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00929f38 bytes a9931bf8
- 00929f5c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00929f5c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:50:8"]]
- 00929f5c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00929f5c bytes e8430139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab59abc79dc0c2361dfd0ee5e0dbe10d"></a>

### [`0092a218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092a/0092a218.md) → [`0092a3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0092a/0092a3b4.md) FUN_0092a3b4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "0092a220"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0092a228"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0092a3bc"
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
      "unmatched:0092a220",
      "DATA",
      [
        "storage",
        "00c86448",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0092a3bc",
      "DATA",
      [
        "storage",
        "00c86848",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0092a220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092a/0092a218.md#insn-0092a220) · [`0092a228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092a/0092a218.md#insn-0092a228) · [`0092a22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0092a/0092a218.md#insn-0092a22c)

~~~diff
- 0092a220 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 0092a220 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0092a220 bytes 280000f9
- 0092a228 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 0092a228 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:8:8"]]
- 0092a228 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0092a228 bytes 28200039
- 0092a22c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0092a22c ["RETURN", null, ["register:0:8"]]
- 0092a22c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0526be0704c88270eb0eef5036810e50"></a>

### [`009300f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/009300f4.md) → [`00930290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/00930290.md) FUN_00930290

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`009302e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/009302e0.md) [`00934468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934468.md) · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)
- 新版 呼出元 2件 [`0093047c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00930/0093047c.md) [`00934604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934604.md) · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 93.85% / 新版 93.85%

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
      "site": "009300f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009300f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009300f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009300f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:009300f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009300fc",
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
      "00930290",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00930294",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00930298",
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

- 旧版 [`009300f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/009300f4.md#insn-009300f4) · [`009300f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/009300f4.md#insn-009300f8) · [`009300fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/009300f4.md#insn-009300fc)

~~~diff
- 009300f4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009300f4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009300f4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 009300f4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009300f4 bytes fd7bbda9
- 009300f8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009300f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 009300f8 bytes f50b00f9
- 009300fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 009300fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 009300fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 009300fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009300fc bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b995f3b028a7f77fa819c7386ddad7e"></a>

### [`00930fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/00930fec.md) → [`00931188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931188.md) FUN_00931188

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00931004"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009311a0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0093100c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00931004",
      "DATA",
      [
        "storage",
        "00c86748",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00931008",
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
      "009311a0",
      "DATA",
      [
        "storage",
        "00c86b48",
        null,
        "undefined *"
      ]
    ],
    [
      "009311a4",
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

- 旧版 [`00931004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/00930fec.md#insn-00931004) · [`0093100c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/00930fec.md#insn-0093100c)
- 新版 `009311a0`（命令位置の公開資料なし）

~~~diff
- 00931004 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00931004 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00931004 bytes 080000f9
- 0093100c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0093100c ["RETURN", null, ["register:0:8"]]
- 0093100c bytes c0035fd6
+ 009311a0 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 009311a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009311a0 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20e165425e9beb54a7d8432782b3c9a0"></a>

### [`009312dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/009312dc.md) → [`00931478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931478.md) FUN_00931478

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "009312f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00931490"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "009312fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009312f4",
      "DATA",
      [
        "storage",
        "00c867b8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009312f8",
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
      "00931490",
      "DATA",
      [
        "storage",
        "00c86bb8",
        null,
        "undefined *"
      ]
    ],
    [
      "00931494",
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

- 旧版 [`009312f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/009312dc.md#insn-009312f4) · [`009312fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/009312dc.md#insn-009312fc)
- 新版 `00931490`（命令位置の公開資料なし）

~~~diff
- 009312f4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 009312f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009312f4 bytes 080000f9
- 009312fc ["COPY", "register:0:8", ["register:40f0:8"]]
- 009312fc ["RETURN", null, ["register:0:8"]]
- 009312fc bytes c0035fd6
+ 00931490 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00931490 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00931490 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-013de725055d26a711ce069541fc77e9"></a>

### [`00931370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931370.md) → [`0093150c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/0093150c.md) FUN_0093150c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00931370"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00931370"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00931374"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00931370",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00931374",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00931394",
      "DATA",
      [
        "storage",
        "00c86848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0093150c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00931510",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00931530",
      "DATA",
      [
        "storage",
        "00c86c48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00931370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931370.md#insn-00931370) · [`00931374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931370.md#insn-00931374) · [`00931394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/00931370.md#insn-00931394)

~~~diff
- 00931370 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00931370 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00931370 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00931370 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00931370 bytes fd7bbea9
- 00931374 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00931374 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00931374 bytes f30b00f9
- 00931394 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00931394 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00931394 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00931394 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00931394 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92e05d311b82eb17a53bedf738287a57"></a>

### [`009313a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/009313a4.md) → [`00931540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00931/00931540.md) FUN_00931540

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "009313b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009313b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0093154c"
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
      "unmatched:009313b0",
      "DATA",
      [
        "storage",
        "00c86848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0093154c",
      "DATA",
      [
        "storage",
        "00c86c48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009313b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/009313a4.md#insn-009313b0) · [`009313b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/009313a4.md#insn-009313b4)
- 新版 `0093154c`（命令位置の公開資料なし）

~~~diff
- 009313b0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 009313b0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 009313b0 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 009313b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009313b0 bytes 292000a9
- 009313b4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 009313b4 ["RETURN", null, ["register:0:8"]]
- 009313b4 bytes c0035fd6
+ 0093154c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0093154c ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 0093154c ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 0093154c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0093154c bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e68c57e1668020c4bac80de77c47a33"></a>

### [`009322ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/009322ac.md) → [`00932448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932448.md) FUN_00932448

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call, call_count, call_target, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.10% / 新版 87.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009322c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00932460"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "009322c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009322c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:009322c8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "0093246c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ea0"
      ]
    ]
  ],
  "added": [
    [
      "00932460",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00932464",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "0093246c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ee0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009322c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/009322ac.md#insn-009322c4) · [`009322c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/009322ac.md#insn-009322c8) · [`009322d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/009322ac.md#insn-009322d0)
- 新版 `0093246c`（命令位置の公開資料なし）

~~~diff
- 009322c4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009322c4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009322c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009322c4 bytes a8831ff8
- 009322c8 ["INT_ADD", "register:40f0:8", ["const:9322c8:8", "const:4:8"]]
- 009322c8 ["CALL", null, ["callee:008514f8:8"]]
- 009322c8 bytes 7c7cfc97
- 009322d0 ["INT_ADD", "register:40f0:8", ["const:9322d0:8", "const:4:8"]]
- 009322d0 ["CALL", null, ["ram:764ea0:8"]]
+ 0093246c ["INT_ADD", "register:40f0:8", ["const:93246c:8", "const:4:8"]]
+ 0093246c ["CALL", null, ["ram:764ee0:8"]]
- 009322d0 bytes f4caf897
+ 0093246c bytes 9dcaf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-201e4f0c398b791681323260dd84c9bd"></a>

### [`00932438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932438.md) → [`009325d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/009325d4.md) FUN_009325d4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00932450"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009325ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00932458"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00932450",
      "DATA",
      [
        "storage",
        "00c86cc8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00932454",
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
      "009325ec",
      "DATA",
      [
        "storage",
        "00c870c8",
        null,
        "undefined *"
      ]
    ],
    [
      "009325f0",
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

- 旧版 [`00932450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932438.md#insn-00932450) · [`00932458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932438.md#insn-00932458)
- 新版 `009325ec`（命令位置の公開資料なし）

~~~diff
- 00932450 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00932450 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00932450 bytes 080000f9
- 00932458 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00932458 ["RETURN", null, ["register:0:8"]]
- 00932458 bytes c0035fd6
+ 009325ec ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 009325ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009325ec bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d4ff340210747c352430e52658326bb"></a>

### [`0093245c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/0093245c.md) → [`009325f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/009325f8.md) FUN_009325f8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00932464"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00932600"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00932468"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00932464",
      "DATA",
      [
        "storage",
        "00c86cc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00932600",
      "DATA",
      [
        "storage",
        "00c870c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00932464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/0093245c.md#insn-00932464) · [`00932468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/0093245c.md#insn-00932468)
- 新版 `00932600`（命令位置の公開資料なし）

~~~diff
- 00932464 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00932464 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00932464 bytes 280000f9
- 00932468 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00932468 ["RETURN", null, ["register:0:8"]]
- 00932468 bytes c0035fd6
+ 00932600 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00932600 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00932600 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-082106f46c4731bb452742b7cc6a645a"></a>

### [`00932a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932a14.md) → [`00932bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932bb0.md) FUN_00932bb0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00932a2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00932bc8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00932a34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00932a2c",
      "DATA",
      [
        "storage",
        "00c86db8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00932a30",
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
      "00932bc8",
      "DATA",
      [
        "storage",
        "00c871b8",
        null,
        "undefined *"
      ]
    ],
    [
      "00932bcc",
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

- 旧版 [`00932a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932a14.md#insn-00932a2c) · [`00932a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932a14.md#insn-00932a34)
- 新版 `00932bc8`（命令位置の公開資料なし）

~~~diff
- 00932a2c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00932a2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00932a2c bytes 080000f9
- 00932a34 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00932a34 ["RETURN", null, ["register:0:8"]]
- 00932a34 bytes c0035fd6
+ 00932bc8 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00932bc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00932bc8 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-601c3ab5ffcde4f9ad44f8121fc24996"></a>

### [`00932a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932a50.md) → [`00932bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932bec.md) FUN_00932bec

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.52% / 新版 64.52%

CFGの説明率　旧版 25.00% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00932a54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00932a54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00932a58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00932a54",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00932a58",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00932a68",
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
      "00932bf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00932bf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00932c04",
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

- 旧版 [`00932a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932a50.md#insn-00932a54) · [`00932a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932a50.md#insn-00932a58) · [`00932a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932a50.md#insn-00932a68)

~~~diff
- 00932a54 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00932a54 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00932a54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00932a54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00932a54 bytes fd7b02a9
- 00932a58 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00932a58 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00932a58 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00932a58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00932a58 bytes f44f03a9
- 00932a68 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00932a68 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00932a68 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00932a68 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-396b1abcf8df2c8cc322c1e4536f23d5"></a>

### [`00932af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932af8.md) → [`00932c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932c94.md) FUN_00932c94

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00932b10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00932cac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00932b18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00932b10",
      "DATA",
      [
        "storage",
        "00c86e38",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00932b14",
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
      "00932cac",
      "DATA",
      [
        "storage",
        "00c87238",
        null,
        "undefined *"
      ]
    ],
    [
      "00932cb0",
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

- 旧版 [`00932b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932af8.md#insn-00932b10) · [`00932b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932af8.md#insn-00932b18)
- 新版 `00932cac`（命令位置の公開資料なし）

~~~diff
- 00932b10 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00932b10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00932b10 bytes 080000f9
- 00932b18 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00932b18 ["RETURN", null, ["register:0:8"]]
- 00932b18 bytes c0035fd6
+ 00932cac ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00932cac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00932cac bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c7421bf1c00b39e2f4ace83e37eedaf"></a>

### [`00932c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932c00.md) → [`00932d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00932/00932d9c.md) FUN_00932d9c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00932c08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00932da4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00932c0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00932c08",
      "DATA",
      [
        "storage",
        "00c86ec8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00932da4",
      "DATA",
      [
        "storage",
        "00c872c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00932c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932c00.md#insn-00932c08) · [`00932c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00932/00932c00.md#insn-00932c0c)
- 新版 `00932da4`（命令位置の公開資料なし）

~~~diff
- 00932c08 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00932c08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00932c08 bytes 280000f9
- 00932c0c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00932c0c ["RETURN", null, ["register:0:8"]]
- 00932c0c bytes c0035fd6
+ 00932da4 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00932da4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00932da4 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6e8f02a2593909c8efa289afa500efd"></a>

### [`0093305c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/0093305c.md) → [`009331f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/009331f8.md) FUN_009331f8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00933064"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00933200"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00933068"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00933064",
      "DATA",
      [
        "storage",
        "00c86f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00933200",
      "DATA",
      [
        "storage",
        "00c87338",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00933064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/0093305c.md#insn-00933064) · [`00933068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/0093305c.md#insn-00933068)
- 新版 `00933200`（命令位置の公開資料なし）

~~~diff
- 00933064 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00933064 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00933064 bytes 280000f9
- 00933068 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00933068 ["RETURN", null, ["register:0:8"]]
- 00933068 bytes c0035fd6
+ 00933200 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00933200 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00933200 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d08ca0aff6f1181a8a2bafccc17372b"></a>

### [`00933158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933158.md) → [`009332f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/009332f4.md) FUN_009332f4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.42% / 新版 77.42%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00933170"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0093330c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009331bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00933170",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00933174",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "unmatched:0093317c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ea0"
      ]
    ]
  ],
  "added": [
    [
      "0093330c",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00933310",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "00933318",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ee0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00933170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933158.md#insn-00933170) · [`00933174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933158.md#insn-00933174) · [`0093317c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933158.md#insn-0093317c)

~~~diff
- 00933170 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00933170 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00933170 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00933170 bytes a8831ff8
- 00933174 ["INT_ADD", "register:40f0:8", ["const:933174:8", "const:4:8"]]
- 00933174 ["CALL", null, ["callee:008514f8:8"]]
- 00933174 bytes d178fc97
- 0093317c ["INT_ADD", "register:40f0:8", ["const:93317c:8", "const:4:8"]]
- 0093317c ["CALL", null, ["ram:764ea0:8"]]
- 0093317c bytes 49c7f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-024a6b2e387087707dc40ea8c5084925"></a>

### [`00933200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933200.md) → [`0093339c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/0093339c.md) FUN_0093339c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00933200"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00933200"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00933218"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00933200",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0093320c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "unmatched:00933218",
      "DATA",
      [
        "storage",
        "00c87048",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0093339c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009333a8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "009333b4",
      "DATA",
      [
        "storage",
        "00c87448",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00933200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933200.md#insn-00933200) · [`0093320c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933200.md#insn-0093320c) · [`00933218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933200.md#insn-00933218)

~~~diff
- 00933200 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00933200 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00933200 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00933200 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00933200 bytes fd7bbfa9
- 0093320c ["INT_ADD", "register:40f0:8", ["const:93320c:8", "const:4:8"]]
- 0093320c ["CALL", null, ["callee:00c57e90:8"]]
- 0093320c bytes 21920c94
- 00933218 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00933218 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00933218 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63b565f00ff1b509f3ff957a6554081e"></a>

### [`00933224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933224.md) → [`009333c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00933/009333c0.md) FUN_009333c0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "0093322c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009333c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00933230"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0093322c",
      "DATA",
      [
        "storage",
        "00c87048",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009333c8",
      "DATA",
      [
        "storage",
        "00c87448",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0093322c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933224.md#insn-0093322c) · [`00933230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933224.md#insn-00933230)
- 新版 `009333c8`（命令位置の公開資料なし）

~~~diff
- 0093322c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 0093322c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0093322c bytes 280000f9
- 00933230 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00933230 ["RETURN", null, ["register:0:8"]]
- 00933230 bytes c0035fd6
+ 009333c8 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 009333c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009333c8 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63ce959258d5e8c41557bc899a19b19a"></a>

### [`00934fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934fc4.md) → [`00935160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935160.md) FUN_00935160

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00934fdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00935178"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00934fe4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00934fdc",
      "DATA",
      [
        "storage",
        "00c877b8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00934fe0",
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
      "00935178",
      "DATA",
      [
        "storage",
        "00c87bb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0093517c",
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

- 旧版 [`00934fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934fc4.md#insn-00934fdc) · [`00934fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934fc4.md#insn-00934fe4)
- 新版 `00935178`（命令位置の公開資料なし）

~~~diff
- 00934fdc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00934fdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00934fdc bytes 080000f9
- 00934fe4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00934fe4 ["RETURN", null, ["register:0:8"]]
- 00934fe4 bytes c0035fd6
+ 00935178 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00935178 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00935178 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ce42f361d39c89ab1f5434693a2aaaa"></a>

### [`00935000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935000.md) → [`0093519c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/0093519c.md) FUN_0093519c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "00935024"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "009351c0"
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
      "unmatched:00935024",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "009351c0",
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

- 旧版 [`00935024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935000.md#insn-00935024) · [`00935008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935000.md#insn-00935008)
- 新版 `009351c0`（命令位置の公開資料なし） · `009351a4`（命令位置の公開資料なし）

~~~diff
- 00935024 ["INT_ADD", "register:40f0:8", ["const:935024:8", "const:4:8"]]
- 00935024 ["CALL", null, ["ram:47acb4:8"]]
- 00935024 bytes 2417ed97
+ 009351c0 ["INT_ADD", "register:40f0:8", ["const:9351c0:8", "const:4:8"]]
+ 009351c0 ["CALL", null, ["ram:47acf4:8"]]
+ 009351c0 bytes cd16ed97
- 00935008 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00935008 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 009351a4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 009351a4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00935008 bytes e1010054
+ 009351a4 bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ff31f97074dac6c59b5f566875aab9b"></a>

### [`00935840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935840.md) → [`009359dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/009359dc.md) FUN_009359dc

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00acb88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb88c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00acba88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acba88.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.49% / 新版 86.49%

CFGの説明率　旧版 66.67% / 新版 53.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00935864"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00935a00"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00935868"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00935864",
      "DATA",
      [
        "storage",
        "00c87848",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00935868",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00935a14"
      ]
    ]
  ],
  "added": [
    [
      "00935a00",
      "DATA",
      [
        "storage",
        "00c87c48",
        null,
        "undefined *"
      ]
    ],
    [
      "00935a04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00935a14"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00935864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935840.md#insn-00935864) · [`00935868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935840.md#insn-00935868)
- 新版 `00935a00`（命令位置の公開資料なし）

~~~diff
- 00935864 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00935864 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00935864 bytes 680200f9
- 00935868 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00935868 bytes 80000054
+ 00935a00 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 00935a00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00935a00 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdbaa6bd3ccbc026eed1d2d7690894cb"></a>

### [`009358d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/009358d4.md) → [`00935a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935a70.md) FUN_00935a70

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "site": "009358e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00935a80"
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
      "unmatched:009358e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00935a94"
      ]
    ]
  ],
  "added": [
    [
      "00935a80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00935a94"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009358e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/009358d4.md#insn-009358e4) · [`009358f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/009358d4.md#insn-009358f0)
- 新版 `00935a80`（命令位置の公開資料なし） · `00935a8c`（命令位置の公開資料なし）

~~~diff
- 009358e4 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 009358e4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 009358e4 bytes b30000b4
+ 00935a80 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00935a80 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00935a80 bytes b30000b4
- 009358f0 ["INT_ADD", "register:40f0:8", ["const:9358f0:8", "const:4:8"]]
- 009358f0 ["CALL", null, ["callee:00c53d00:8"]]
+ 00935a8c ["INT_ADD", "register:40f0:8", ["const:935a8c:8", "const:4:8"]]
+ 00935a8c ["CALL", null, ["callee:00c53d00:8"]]
- 009358f0 bytes fc770c94
+ 00935a8c bytes 9d780c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b5a090b4144ea566eee70f1f47db87b"></a>

### [`00935974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935974.md) → [`00935b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935b10.md) FUN_00935b10

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`00859b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b0c.md) [`0085b264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b264.md) [`0085b26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b26c.md) [`0085b294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b294.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`00859b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b4c.md) [`0085b2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2a4.md) [`0085b2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2ac.md) [`0085b2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2d4.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 94.26% / 新版 94.26%

CFGの説明率　旧版 40.48% / 新版 45.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00935aa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00935ab4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00935c40"
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
      "unmatched:00935b10",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00935cac",
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

- 旧版 [`00935aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935974.md#insn-00935aa4) · [`00935ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935974.md#insn-00935ab4) · [`00935b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935974.md#insn-00935b10)

~~~diff
- 00935aa4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00935aa4 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00935aa4 ["BOOL_NEGATE", "tmp:2:1", ["tmp:0:1"]]
- 00935aa4 ["CBRANCH", null, ["const:2:4", "tmp:2:1"]]
- 00935aa4 bytes 08a5881a
- 00935ab4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00935ab4 ["COPY", "tmp:1:4", ["register:40b8:4"]]
- 00935ab4 ["BOOL_NEGATE", "tmp:2:1", ["tmp:0:1"]]
- 00935ab4 ["CBRANCH", null, ["const:2:4", "tmp:2:1"]]
- 00935ab4 bytes eaa6971a
- 00935b10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00935b10 ["INT_ADD", "register:40f0:8", ["const:935b10:8", "const:4:8"]]
- 00935b10 ["CALLIND", null, ["register:0:8"]]
- 00935b10 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03ca7220dbddc07385c185bf3adbb3b7"></a>

### [`00937e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937e48.md) → [`00937fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00937/00937fe4.md) FUN_00937fe4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 2件 [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md) [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md)
- 新版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 2件 [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 72.22% / 新版 81.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00937e80"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0093801c"
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
      "unmatched:00937e80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00938040"
      ]
    ]
  ],
  "added": [
    [
      "0093801c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00938040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00937e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937e48.md#insn-00937e80) · [`00937e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937e48.md#insn-00937e70)
- 新版 `0093801c`（命令位置の公開資料なし） · `0093800c`（命令位置の公開資料なし）

~~~diff
- 00937e80 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00937e80 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00937e80 bytes 21010054
+ 0093801c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0093801c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0093801c bytes 21010054
- 00937e70 ["INT_ADD", "register:40f0:8", ["const:937e70:8", "const:4:8"]]
- 00937e70 ["CALL", null, ["callee:00480b90:8"]]
+ 0093800c ["INT_ADD", "register:40f0:8", ["const:93800c:8", "const:4:8"]]
+ 0093800c ["CALL", null, ["callee:00480b90:8"]]
- 00937e70 bytes 3823ed97
+ 0093800c bytes e122ed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb0819f911caf0fb1440dee91d4deb5e"></a>

### [`00938364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/00938364.md) → [`00938500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/00938500.md) FUN_00938500

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00937f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937f14.md) [`009385d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/009385d8.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`009380b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/009380b0.md) [`00938774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00938/00938774.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 99.35% / 新版 99.35%

CFGの説明率　旧版 88.71% / 新版 91.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009383a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00938544"
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
      "unmatched:009383a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00938534"
      ]
    ]
  ],
  "added": [
    [
      "00938544",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00938534"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009383a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/00938364.md#insn-009383a8) · [`00938544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00938/00938364.md#insn-00938544)
- 新版 `009386e0`（命令位置の公開資料なし） · `00938544`（命令位置の公開資料なし）

~~~diff
- 009383a8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 009383a8 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 009383a8 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 009383a8 ["CBRANCH", null, ["local:b3:8", "tmp:2:1"]]
- 009383a8 bytes 8cffff54
- 00938544 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00938544 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00938544 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00938544 ["CBRANCH", null, ["local:b32:8", "tmp:2:1"]]
+ 009386e0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 009386e0 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 009386e0 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 009386e0 ["CBRANCH", null, ["local:b30:8", "tmp:2:1"]]
- 00938544 bytes 4cffff54
+ 009386e0 bytes 4cffff54
+ 00938544 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00938544 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 00938544 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 00938544 ["CBRANCH", null, ["local:b2:8", "tmp:2:1"]]
+ 00938544 bytes 8cffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a04561f0ec02ba30b19f46f5dc08ec29"></a>

### [`00942570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/00942570.md) → [`0094270c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094270c.md) FUN_0094270c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`0093f228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093f/0093f228.md) [`009426f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/009426f0.md) [`00942df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/00942df8.md) [`009437fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/009437fc.md) [`00943fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00943/00943fdc.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 5件 [`0093f3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093f/0093f3c4.md) [`0094288c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/0094288c.md) [`00942f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00942/00942f94.md) [`00943998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00943/00943998.md) [`00944178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00944/00944178.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 73.96% / 新版 73.96%

CFGの説明率　旧版 30.77% / 新版 26.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00942574"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00942574"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00942578"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00942574",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00942578",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0094257c",
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
      "00942710",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00942714",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00942718",
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

- 旧版 [`00942574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/00942570.md#insn-00942574) · [`00942578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/00942570.md#insn-00942578) · [`0094257c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00942/00942570.md#insn-0094257c)

~~~diff
- 00942574 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00942574 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00942574 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00942574 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00942574 bytes fd7b04a9
- 00942578 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 00942578 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00942578 bytes fb2b00f9
- 0094257c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0094257c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0094257c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 0094257c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0094257c bytes fa6706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae6916d17105fa489166f9f0d76a3807"></a>

### [`0097d0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d0d4.md) → [`0097d270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d270.md) FUN_0097d270

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

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
      "site": "0097d0f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0097d294"
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
      "unmatched:0097d0f8",
      "DATA",
      [
        "storage",
        "00c87968",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097d294",
      "DATA",
      [
        "storage",
        "00c87d68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097d0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d0d4.md#insn-0097d0f8) · [`0097d0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d0d4.md#insn-0097d0e8)
- 新版 `0097d294`（命令位置の公開資料なし） · `0097d284`（命令位置の公開資料なし）

~~~diff
- 0097d0f8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0097d0f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0097d0f8 bytes 080000f9
+ 0097d294 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 0097d294 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0097d294 bytes 080000f9
- 0097d0e8 ["INT_ADD", "register:40f0:8", ["const:97d0e8:8", "const:4:8"]]
- 0097d0e8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0097d284 ["INT_ADD", "register:40f0:8", ["const:97d284:8", "const:4:8"]]
+ 0097d284 ["CALL", null, ["callee:00c57e90:8"]]
- 0097d0e8 bytes 6a6a0b94
+ 0097d284 bytes 036b0b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa243a29d51c3020f43054c0600e28c8"></a>

### [`0097d7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d7dc.md) → [`0097d978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d978.md) FUN_0097d978

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 11.11% / 新版 11.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097d7f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0097d990"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0097d7e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097d7e8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "unmatched:0097d7f4",
      "DATA",
      [
        "storage",
        "00c87ae8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0097d7f8",
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
      "0097d984",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "0097d990",
      "DATA",
      [
        "storage",
        "00c87ee8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097d994",
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

- 旧版 [`0097d7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d7dc.md#insn-0097d7e8) · [`0097d7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d7dc.md#insn-0097d7f4) · [`0097d7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d7dc.md#insn-0097d7fc)

~~~diff
- 0097d7e8 ["INT_ADD", "register:40f0:8", ["const:97d7e8:8", "const:4:8"]]
- 0097d7e8 ["CALL", null, ["callee:00c57e90:8"]]
- 0097d7e8 bytes aa680b94
- 0097d7f4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0097d7f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0097d7f4 bytes 080000f9
- 0097d7fc ["COPY", "register:0:8", ["register:40f0:8"]]
- 0097d7fc ["RETURN", null, ["register:0:8"]]
- 0097d7fc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cde0197d43911b6e78cb5cff94b1720"></a>

### [`0097f5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f5e0.md) → [`0097f77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097f77c.md) FUN_0097f77c

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009806cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/009806cc.md) · 呼出先 3件 [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00981584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981584.md)
- 新版 呼出元 1件 [`00980868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980868.md) · 呼出先 3件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00981720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981720.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.43% / 新版 81.43%

CFGの説明率　旧版 25.64% / 新版 27.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097f648"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097f648"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0097f64c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0097f630",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097f7e0"
      ]
    ],
    [
      "unmatched:0097f648",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0097f64c",
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
      "0097f7cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0097f7e0"
      ]
    ],
    [
      "0097f7e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0097f7e8",
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

- 旧版 [`0097f630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f5e0.md#insn-0097f630) · [`0097f648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f5e0.md#insn-0097f648) · [`0097f64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f5e0.md#insn-0097f64c)

~~~diff
- 0097f630 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 0097f630 bytes a0000054
- 0097f648 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0097f648 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0097f648 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0097f648 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0097f648 bytes fd7b01a9
- 0097f64c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0097f64c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0097f64c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0097f64c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0097f64c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59b62fb74ef16d5d6bba185d4c19c670"></a>

### [`00980644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980644.md) → [`009807e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/009807e0.md) FUN_009807e0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

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
      "site": "00980660"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "009807fc"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00980660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980644.md#insn-00980660) · [`0098064c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980644.md#insn-0098064c)
- 新版 `009807fc`（命令位置の公開資料なし） · `009807e8`（命令位置の公開資料なし）

~~~diff
- 00980660 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00980660 ["RETURN", null, ["register:0:8"]]
- 00980660 bytes c0035fd6
+ 009807fc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 009807fc ["RETURN", null, ["register:0:8"]]
+ 009807fc bytes c0035fd6
- 0098064c ["INT_ADD", "register:40f0:8", ["const:98064c:8", "const:4:8"]]
- 0098064c ["CALL", null, ["callee:008514f8:8"]]
+ 009807e8 ["INT_ADD", "register:40f0:8", ["const:9807e8:8", "const:4:8"]]
+ 009807e8 ["CALL", null, ["callee:008514f8:8"]]
- 0098064c bytes 9b43fb97
+ 009807e8 bytes 4443fb97
~~~


<a id="compare-947f5909419b0cea3ad3704631ce765a"></a>

### [`00980b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980b68.md) → [`00980d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980d04.md) FUN_00980d04

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`009806cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/009806cc.md) [`00980d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980d90.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 2件 [`00980868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980868.md) [`00980f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980f2c.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 61.54% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980be8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00980d84"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00980be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980b68.md#insn-00980be8) · [`00980b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980b68.md#insn-00980b80)
- 新版 `00980d84`（命令位置の公開資料なし） · `00980d1c`（命令位置の公開資料なし）

~~~diff
- 00980be8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:30:8"]]
- 00980be8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00980be8 bytes 6002833c
+ 00980d84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:30:8"]]
+ 00980d84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 00980d84 bytes 6002833c
- 00980b80 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00980b80 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00980b80 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00980b80 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00980d1c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00980d1c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00980d1c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00980d1c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00980b80 bytes c8000037
+ 00980d1c bytes c8000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee3aba0edfc7797a1b9d1b38cb64207c"></a>

### [`00980d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980d90.md) → [`00980f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980f2c.md) FUN_00980f2c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006b8c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8c04.md) [`00980b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980b68.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006b8c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8c44.md) [`00980d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00980/00980d04.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 79.59% / 新版 79.59%

CFGの説明率　旧版 53.12% / 新版 53.97%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980dc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980dd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00980df4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00980dc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00980dd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x100]",
        null,
        null
      ]
    ],
    [
      "009810fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009810e8"
      ]
    ]
  ],
  "added": [
    [
      "00980f64",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00980f6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x100]",
        null,
        null
      ]
    ],
    [
      "00980f78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009810e8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980d90.md#insn-00980dc8) · [`00980dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980d90.md#insn-00980dd0) · [`00980de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00980/00980d90.md#insn-00980de8)

~~~diff
- 00980dc8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00980dc8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00980dc8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00980dc8 bytes a8031ff8
- 00980dd0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00980dd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00980dd0 bytes e90b00f9
- 00980de8 ["CBRANCH", null, ["local:b35:8", "register:101:1"]]
- 00980de8 bytes e00b0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0f665124f0d0656f376836d84740f35"></a>

### [`00981008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981008.md) → [`009811a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/009811a4.md) FUN_009811a4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`0075b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 4件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`0075b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b9c4.md) [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 64.71% / 新版 61.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981008"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981008"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098100c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00981008",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0098100c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00981010",
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
      "009811a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "009811a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "009811ac",
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

- 旧版 [`00981008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981008.md#insn-00981008) · [`0098100c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981008.md#insn-0098100c) · [`00981010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981008.md#insn-00981010)

~~~diff
- 00981008 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00981008 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00981008 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00981008 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00981008 bytes fd7bbca9
- 0098100c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0098100c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 0098100c bytes f70b00f9
- 00981010 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00981010 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00981010 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00981010 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00981010 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c954867cbf9f9d97d8c296f7b20db5a"></a>

### [`009810d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009810d0.md) → [`0098126c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/0098126c.md) FUN_0098126c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 2件 [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 93.88% / 新版 93.88%

CFGの説明率　旧版 36.84% / 新版 36.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981178"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00981314"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00981118"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00981118",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0098129c"
      ]
    ]
  ],
  "added": [
    [
      "009812b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0098129c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009810d0.md#insn-00981118) · [`00981178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009810d0.md#insn-00981178) · [`00981190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/009810d0.md#insn-00981190)

~~~diff
- 00981118 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00981118 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00981118 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00981118 ["CBRANCH", null, ["local:b3:8", "tmp:2:1"]]
- 00981118 bytes 4cffff54
- 00981178 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:50:8"]]
- 00981178 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00981178 bytes 682a00f9
- 00981190 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00981190 ["RETURN", null, ["register:0:8"]]
- 00981190 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f6544ceba73f72f8e5cfacfa73e2dd8"></a>

### [`0098168c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/0098168c.md) → [`00981828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981828.md) FUN_00981828

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "009816b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009816b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0098184c"
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
      "unmatched:009816b0",
      "DATA",
      [
        "storage",
        "00c87c00",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009816b4",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009816b8",
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
      "0098184c",
      "DATA",
      [
        "storage",
        "00c88000",
        null,
        "undefined *"
      ]
    ],
    [
      "00981850",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00981854",
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

- 旧版 [`009816b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/0098168c.md#insn-009816b0) · [`009816bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/0098168c.md#insn-009816bc)
- 新版 `0098184c`（命令位置の公開資料なし）

~~~diff
- 009816b0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009816b0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 009816b0 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 009816b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009816b0 bytes 082400a9
- 009816bc ["COPY", "register:0:8", ["register:40f0:8"]]
- 009816bc ["RETURN", null, ["register:0:8"]]
- 009816bc bytes c0035fd6
+ 0098184c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0098184c ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 0098184c ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 0098184c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0098184c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bc01e839f18f900dc81197bbfd04576"></a>

### [`00981e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981e24.md) → [`00981fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981fc0.md) FUN_00981fc0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00981c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981c20.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00981dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00981/00981dbc.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.37% / 新版 88.37%

CFGの説明率　旧版 32.14% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981e24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981e24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981e28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00981e24",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00981e28",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00981e2c",
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
      "00981fc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00981fc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00981fc8",
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

- 旧版 [`00981e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981e24.md#insn-00981e24) · [`00981e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981e24.md#insn-00981e28) · [`00981e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981e24.md#insn-00981e2c)

~~~diff
- 00981e24 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00981e24 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00981e24 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00981e24 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00981e24 bytes fd7bbca9
- 00981e28 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00981e28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00981e28 bytes f70b00f9
- 00981e2c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00981e2c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00981e2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00981e2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00981e2c bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30d037a02c2cd845bbfa43e4b4ff7b18"></a>

### [`00981f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981f7c.md) → [`00982118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982118.md) FUN_00982118

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 85.00% / 新版 94.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981f7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981f7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00981f80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00981f7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00981f80",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00981f84",
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
      "00982118",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0098211c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00982120",
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

- 旧版 [`00981f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981f7c.md#insn-00981f7c) · [`00981f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981f7c.md#insn-00981f80) · [`00981f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00981/00981f7c.md#insn-00981f84)

~~~diff
- 00981f7c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00981f7c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00981f7c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00981f7c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00981f7c bytes fd7bbda9
- 00981f80 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00981f80 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00981f80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00981f80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00981f80 bytes f65701a9
- 00981f84 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00981f84 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00981f84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00981f84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00981f84 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c71fc751e7a4af5985b25d3dfd99e2de"></a>

### [`00982160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982160.md) → [`009822fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009822fc.md) FUN_009822fc

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00982030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982030.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`009821cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009821cc.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.85% / 新版 93.85%

CFGの説明率　旧版 61.54% / 新版 53.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00982198"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0098219c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00982238"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00982238",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0098234c"
      ]
    ]
  ],
  "added": [
    [
      "009823d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0098234c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00982198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982160.md#insn-00982198) · [`0098219c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982160.md#insn-0098219c) · [`00982238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982160.md#insn-00982238)

~~~diff
- 00982198 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00982198 ["COPY", "tmp:1:8", ["register:4060:8"]]
- 00982198 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00982198 ["INT_ADD", "tmp:1:8", ["register:4010:8", "const:1:8"]]
- 00982198 bytes 9515829a
- 0098219c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 0098219c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 0098219c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 0098219c ["COPY", "register:40c8:8", ["tmp:0:8"]]
- 0098219c bytes 59018b9a
- 00982238 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00982238 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00982238 bytes c8fbffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bc17c65fb6a79afb0cfba964c351646"></a>

### [`00982264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982264.md) → [`00982400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982400.md) FUN_00982400

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098226c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00982408"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00982270"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00982270",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0098244c"
      ]
    ]
  ],
  "added": [
    [
      "0098240c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0098244c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098226c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982264.md#insn-0098226c) · [`00982270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982264.md#insn-00982270)
- 新版 `00982408`（命令位置の公開資料なし）

~~~diff
- 0098226c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0098226c ["COPY", "tmp:1:8", ["const:0:8"]]
- 0098226c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 0098226c bytes 1f0100f9
- 00982270 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00982270 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00982270 bytes 000200b4
+ 00982408 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00982408 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00982408 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00982408 bytes 1f0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b64c87206775b57359fae5c9c98cef1"></a>

### [`0098264c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/0098264c.md) → [`009827e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/009827e8.md) FUN_009827e8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`0086a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086a/0086a420.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0086a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086a460.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "site": "0098264c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0098264c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00982650"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0098264c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00982650",
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
      "009827e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009827ec",
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

- 旧版 [`0098264c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/0098264c.md#insn-0098264c) · [`00982650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/0098264c.md#insn-00982650)
- 新版 `009827e8`（命令位置の公開資料なし）

~~~diff
- 0098264c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0098264c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0098264c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0098264c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0098264c bytes fd7bbea9
- 00982650 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00982650 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00982650 bytes f30b00f9
+ 009827e8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 009827e8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 009827e8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 009827e8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 009827e8 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-268935e658f3b76e5eb26409102b9d72"></a>

### [`0098cd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098cd38.md) → [`0098ced4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098c/0098ced4.md) FUN_0098ced4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00996ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996ea0.md) [`0099b8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0099b/0099b8d4.md) · 呼出先 0件 
- 新版 呼出元 2件 [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) [`0099ba70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0099b/0099ba70.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 65.52% / 新版 67.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0098cdbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0098cf58"
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
      "unmatched:0098cdbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0098cf64"
      ]
    ]
  ],
  "added": [
    [
      "0098cf58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0098cf64"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098cdbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098cd38.md#insn-0098cdbc) · [`0098cd3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098cd38.md#insn-0098cd3c)
- 新版 `0098cf58`（命令位置の公開資料なし） · `0098ced8`（命令位置の公開資料なし）

~~~diff
- 0098cdbc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0098cdbc ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 0098cdbc ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
- 0098cdbc bytes 68000054
+ 0098cf58 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0098cf58 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 0098cf58 ["CBRANCH", null, ["local:b14:8", "tmp:1:1"]]
+ 0098cf58 bytes 68000054
- 0098cd3c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0098cd3c ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
+ 0098ced8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 0098ced8 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 0098cd3c bytes 280500b4
+ 0098ced8 bytes 280500b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a394eef90dfdda68fb86e5033381f9a"></a>

### [`00996824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996824.md) → [`009969c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00996/009969c0.md) FUN_009969c0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) · 呼出先 7件 [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008b9814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9814.md) [`008bac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008bac84.md) [`009a3ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3ac0.md) [`009a3ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3ac4.md)
- 新版 呼出元 1件 [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · 呼出先 7件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008b9858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9858.md) [`008bacc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ba/008bacc8.md) [`009a3c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3c5c.md) [`009a3c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3c60.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 45.00% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00996828"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00996828"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0099682c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00996828",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0099682c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00996830",
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
      "009969c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "009969c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009969cc",
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

- 旧版 [`00996828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996824.md#insn-00996828) · [`0099682c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996824.md#insn-0099682c) · [`00996830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996824.md#insn-00996830)

~~~diff
- 00996828 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00996828 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00996828 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00996828 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00996828 bytes fd7b07a9
- 0099682c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:80:8"]]
- 0099682c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0099682c bytes f54300f9
- 00996830 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00996830 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00996830 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00996830 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00996830 bytes f44f09a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38204d91844e1bc4908a76f72a053466"></a>

### [`009a11e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a1/009a11e0.md) → [`009a137c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a1/009a137c.md) FUN_009a137c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00996ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996ea0.md) [`0099b8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0099b/0099b8d4.md) · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 2件 [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) [`0099ba70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0099b/0099ba70.md) · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 85.45% / 新版 85.45%

CFGの説明率　旧版 18.18% / 新版 17.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a1290"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a1290"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a12a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009a1388",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:009a1290"
      ]
    ],
    [
      "unmatched:009a1220",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a13c8"
      ]
    ],
    [
      "009a13d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:009a1290"
      ]
    ]
  ],
  "added": [
    [
      "009a1388",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a142c"
      ]
    ],
    [
      "009a13bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a13c8"
      ]
    ],
    [
      "009a13d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a142c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a1220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a1/009a11e0.md#insn-009a1220) · [`009a1264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a1/009a11e0.md#insn-009a1264) · [`009a1290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a1/009a11e0.md#insn-009a1290)

~~~diff
- 009a1220 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 009a1220 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 009a1220 ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
- 009a1220 bytes 68000054
- 009a1264 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 009a1264 bytes 20ffff54
- 009a1290 ["COPY", "tmp:0:8", ["const:0:8"]]
- 009a1290 ["COPY", "tmp:1:8", ["const:0:8"]]
- 009a1290 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 009a1290 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 009a1290 bytes 1f7d00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fa22aa7f0cb0777af0a5cdc31a05d72"></a>

### [`009a2998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a2/009a2998.md) → [`009a2b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a2/009a2b34.md) FUN_009a2b34

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`00982bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00982/00982bd0.md) [`0098486c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00984/0098486c.md) [`00984a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00984/00984a98.md) [`0098527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/0098527c.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) · 呼出先 5件 [`009a2ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a2/009a2ae8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 10件 [`00982d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00982/00982d6c.md) [`00984a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00984/00984a08.md) [`00984c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00984/00984c34.md) [`00985418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00985/00985418.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · 呼出先 5件 [`009a2c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a2/009a2c84.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 45.45% / 新版 42.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a29b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009a2b50"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009a2a28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a29b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a2a28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a2bfc"
      ]
    ],
    [
      "009a2be0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:009a2a58"
      ]
    ]
  ],
  "added": [
    [
      "009a2b50",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "009a2bc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a2bfc"
      ]
    ],
    [
      "009a2be0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "009a2bf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a29b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a2/009a2998.md#insn-009a29b4) · [`009a2a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a2/009a2998.md#insn-009a2a28) · [`009a2a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a2/009a2998.md#insn-009a2a5c)

~~~diff
- 009a29b4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009a29b4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009a29b4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009a29b4 bytes a8831ff8
- 009a2a28 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 009a2a28 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 009a2a28 bytes c10100b4
- 009a2a5c ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 009a2a5c bytes 40feff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b811b56918872a85c2bb96d1cd09192"></a>

### [`009a33b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a33b8.md) → [`009a3554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3554.md) FUN_009a3554

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

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
      "site": "009a33b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a33b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a33bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a33b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a33bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a33dc",
      "DATA",
      [
        "storage",
        "00c87e10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a3554",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009a3558",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009a3578",
      "DATA",
      [
        "storage",
        "00c88210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a33b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a33b8.md#insn-009a33b8) · [`009a33bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a33b8.md#insn-009a33bc) · [`009a33dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a33b8.md#insn-009a33dc)

~~~diff
- 009a33b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009a33b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009a33b8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009a33b8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009a33b8 bytes fd7bbea9
- 009a33bc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009a33bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 009a33bc bytes f30b00f9
- 009a33dc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 009a33dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009a33dc bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48f1bf2e107db37c53ececb968c21c28"></a>

### [`009a34e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a34e8.md) → [`009a3684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3684.md) FUN_009a3684

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "009a34e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a34e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a34ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a34e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a34ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a350c",
      "DATA",
      [
        "storage",
        "00c87e90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a3684",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009a3688",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009a36a8",
      "DATA",
      [
        "storage",
        "00c88290",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a34e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a34e8.md#insn-009a34e8) · [`009a34ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a34e8.md#insn-009a34ec) · [`009a350c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a34e8.md#insn-009a350c)

~~~diff
- 009a34e8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009a34e8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009a34e8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009a34e8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009a34e8 bytes fd7bbea9
- 009a34ec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009a34ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 009a34ec bytes f30b00f9
- 009a350c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009a350c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 009a350c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 009a350c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009a350c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a91a125823be7557be9cfc56f27e40b0"></a>

### [`009a37bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a37bc.md) → [`009a3958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3958.md) FUN_009a3958

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "009a37bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a37bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a37c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a37bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a37c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a37e0",
      "DATA",
      [
        "storage",
        "00c87f90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a3958",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009a395c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009a397c",
      "DATA",
      [
        "storage",
        "00c88390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a37bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a37bc.md#insn-009a37bc) · [`009a37c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a37bc.md#insn-009a37c0) · [`009a37e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a37bc.md#insn-009a37e0)

~~~diff
- 009a37bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009a37bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009a37bc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009a37bc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009a37bc bytes fd7bbea9
- 009a37c0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009a37c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 009a37c0 bytes f30b00f9
- 009a37e0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009a37e0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 009a37e0 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 009a37e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009a37e0 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a36e424b9ac89324f73bc9a42f77ee07"></a>

### [`009a3898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3898.md) → [`009a3a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3a34.md) FUN_009a3a34

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

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
      "site": "009a38bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a38bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009a3a58"
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
      "unmatched:009a38bc",
      "DATA",
      [
        "storage",
        "00c88010",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009a38c0",
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
      "009a3a58",
      "DATA",
      [
        "storage",
        "00c88410",
        null,
        "undefined *"
      ]
    ],
    [
      "009a3a5c",
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

- 旧版 [`009a38bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3898.md#insn-009a38bc) · [`009a38a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3898.md#insn-009a38a0)
- 新版 `009a3a58`（命令位置の公開資料なし）

~~~diff
- 009a38bc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009a38bc ["COPY", "tmp:1:8", ["register:4048:8"]]
- 009a38bc ["COPY", "tmp:2:8", ["register:4000:8"]]
- 009a38bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009a38bc bytes 082400a9
+ 009a3a58 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 009a3a58 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 009a3a58 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 009a3a58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 009a3a58 bytes 082400a9
- 009a38a0 ["COPY", "register:40e8:8", ["register:8:8"]]
- 009a38a0 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bad5f7728af8cfe7791a7c4dfc4ae10"></a>

### [`009a392c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a392c.md) → [`009a3ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3ac8.md) FUN_009a3ac8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

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
      "site": "009a3944"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009a3ae0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "009a394c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a3944",
      "DATA",
      [
        "storage",
        "00c88090",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009a3948",
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
      "009a3ae0",
      "DATA",
      [
        "storage",
        "00c88490",
        null,
        "undefined *"
      ]
    ],
    [
      "009a3ae4",
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

- 旧版 [`009a3944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a392c.md#insn-009a3944) · [`009a394c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a392c.md#insn-009a394c)
- 新版 `009a3ae0`（命令位置の公開資料なし）

~~~diff
- 009a3944 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 009a3944 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009a3944 bytes 080000f9
- 009a394c ["COPY", "register:0:8", ["register:40f0:8"]]
- 009a394c ["RETURN", null, ["register:0:8"]]
- 009a394c bytes c0035fd6
+ 009a3ae0 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 009a3ae0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009a3ae0 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-254104b3691c2e72e5c4e33115d1f981"></a>

### [`009a3968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3968.md) → [`009a3b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3b04.md) FUN_009a3b04

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "009a398c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "009a3b28"
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
      "unmatched:009a398c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "009a3b28",
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

- 旧版 [`009a398c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3968.md#insn-009a398c) · [`009a3970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3968.md#insn-009a3970)
- 新版 `009a3b28`（命令位置の公開資料なし） · `009a3b0c`（命令位置の公開資料なし）

~~~diff
- 009a398c ["INT_ADD", "register:40f0:8", ["const:9a398c:8", "const:4:8"]]
- 009a398c ["CALL", null, ["ram:47acb4:8"]]
- 009a398c bytes ca5ceb97
+ 009a3b28 ["INT_ADD", "register:40f0:8", ["const:9a3b28:8", "const:4:8"]]
+ 009a3b28 ["CALL", null, ["ram:47acf4:8"]]
+ 009a3b28 bytes 735ceb97
- 009a3970 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 009a3970 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 009a3b0c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 009a3b0c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 009a3970 bytes e1010054
+ 009a3b0c bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-580150866249f8b629eba52f154f1f00"></a>

### [`009a39dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a39dc.md) → [`009a3b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3b78.md) FUN_009a3b78

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "009a39dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a39dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a39f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a39dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a39e8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "unmatched:009a39f4",
      "DATA",
      [
        "storage",
        "00c88110",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a3b78",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009a3b84",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "009a3b90",
      "DATA",
      [
        "storage",
        "00c88510",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a39dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a39dc.md#insn-009a39dc) · [`009a39e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a39dc.md#insn-009a39e8) · [`009a39f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a39dc.md#insn-009a39f4)

~~~diff
- 009a39dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009a39dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009a39dc ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 009a39dc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009a39dc bytes fd7bbfa9
- 009a39e8 ["INT_ADD", "register:40f0:8", ["const:9a39e8:8", "const:4:8"]]
- 009a39e8 ["CALL", null, ["callee:00c57e90:8"]]
- 009a39e8 bytes 2ad00a94
- 009a39f4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 009a39f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009a39f4 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12cde25c792c2397eda9ea742eaccea3"></a>

### [`009a3a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3a18.md) → [`009a3bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3bb4.md) FUN_009a3bb4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009a3a20"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009a3bbc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "009a3a3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a3a20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a3bf8"
      ]
    ],
    [
      "unmatched:009a3a3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "009a3bbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a3bf8"
      ]
    ],
    [
      "009a3bd8",
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

- 旧版 [`009a3a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3a18.md#insn-009a3a20) · [`009a3a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3a18.md#insn-009a3a3c)
- 新版 `009a3bbc`（命令位置の公開資料なし）

~~~diff
- 009a3a20 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 009a3a20 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 009a3a20 bytes e1010054
- 009a3a3c ["INT_ADD", "register:40f0:8", ["const:9a3a3c:8", "const:4:8"]]
- 009a3a3c ["CALL", null, ["ram:47acb4:8"]]
- 009a3a3c bytes 9e5ceb97
+ 009a3bbc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 009a3bbc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 009a3bbc bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d38576423efe912e649a13c574de432b"></a>

### [`009a3ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3ab0.md) → [`009a3c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a3/009a3c4c.md) FUN_009a3c4c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "009a3ab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009a3c54"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "009a3abc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a3ab8",
      "DATA",
      [
        "storage",
        "00c88190",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a3c54",
      "DATA",
      [
        "storage",
        "00c88590",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a3ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3ab0.md#insn-009a3ab8) · [`009a3abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3ab0.md#insn-009a3abc)
- 新版 `009a3c54`（命令位置の公開資料なし）

~~~diff
- 009a3ab8 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 009a3ab8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009a3ab8 bytes 280000f9
- 009a3abc ["COPY", "register:0:8", ["register:40f0:8"]]
- 009a3abc ["RETURN", null, ["register:0:8"]]
- 009a3abc bytes c0035fd6
+ 009a3c54 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 009a3c54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009a3c54 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d7cd3187a518fcd71c7398fc23a22c5"></a>

### [`009a3ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3ec8.md) → [`009a4064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a4/009a4064.md) FUN_009a4064

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 7件 [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) [`00961604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961604.md) [`00963e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963e3c.md) [`0098cdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098c/0098cdf0.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 7件 [`0094726c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00947/0094726c.md) [`009617a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00961/009617a0.md) [`00963fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963fd8.md) [`0098cf8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098c/0098cf8c.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009a3ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3ec8.md#insn-009a3ed8) · [`009a3ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3ec8.md#insn-009a3ee4) · [`009a3ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a3/009a3ec8.md#insn-009a3ef4)
- 新版 `009a4074`（命令位置の公開資料なし） · `009a4080`（命令位置の公開資料なし） · `009a4090`（命令位置の公開資料なし）

~~~diff
- 009a3ed8 ["INT_ADD", "register:40f0:8", ["const:9a3ed8:8", "const:4:8"]]
- 009a3ed8 ["CALL", null, ["callee:008514f8:8"]]
+ 009a4074 ["INT_ADD", "register:40f0:8", ["const:9a4074:8", "const:4:8"]]
+ 009a4074 ["CALL", null, ["callee:008514f8:8"]]
- 009a3ed8 bytes 78b5fa97
+ 009a4074 bytes 21b5fa97
- 009a3ee4 ["INT_ADD", "register:40f0:8", ["const:9a3ee4:8", "const:4:8"]]
- 009a3ee4 ["CALL", null, ["callee:008514f8:8"]]
+ 009a4080 ["INT_ADD", "register:40f0:8", ["const:9a4080:8", "const:4:8"]]
+ 009a4080 ["CALL", null, ["callee:008514f8:8"]]
- 009a3ee4 bytes 75b5fa97
+ 009a4080 bytes 1eb5fa97
- 009a3ef4 ["INT_ADD", "register:40f0:8", ["const:9a3ef4:8", "const:4:8"]]
- 009a3ef4 ["CALL", null, ["callee:008514f8:8"]]
+ 009a4090 ["INT_ADD", "register:40f0:8", ["const:9a4090:8", "const:4:8"]]
+ 009a4090 ["CALL", null, ["callee:008514f8:8"]]
- 009a3ef4 bytes 71b5fa97
+ 009a4090 bytes 1ab5fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e11038382b084e598eee5219f902906"></a>

### [`009a61ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a61ac.md) → [`009a6348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a6348.md) FUN_009a6348

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

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
      "site": "009a61d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009a636c"
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
      "unmatched:009a61d0",
      "DATA",
      [
        "storage",
        "00c88210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a636c",
      "DATA",
      [
        "storage",
        "00c88610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a61d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a61ac.md#insn-009a61d0) · [`009a61c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a61ac.md#insn-009a61c0)
- 新版 `009a636c`（命令位置の公開資料なし） · `009a635c`（命令位置の公開資料なし）

~~~diff
- 009a61d0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 009a61d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009a61d0 bytes 080000f9
+ 009a636c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 009a636c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009a636c bytes 080000f9
- 009a61c0 ["INT_ADD", "register:40f0:8", ["const:9a61c0:8", "const:4:8"]]
- 009a61c0 ["CALL", null, ["callee:00c57e90:8"]]
+ 009a635c ["INT_ADD", "register:40f0:8", ["const:9a635c:8", "const:4:8"]]
+ 009a635c ["CALL", null, ["callee:00c57e90:8"]]
- 009a61c0 bytes 34c60a94
+ 009a635c bytes cdc60a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67e429438f94fd958b5747f5e5e832b5"></a>

### [`009a6638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a6638.md) → [`009a67d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a67d4.md) FUN_009a67d4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 50.00% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "009a6674"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "009a6810"
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
      "unmatched:009a6674",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "009a6810",
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

- 旧版 [`009a6674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a6638.md#insn-009a6674) · [`009a6654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a6638.md#insn-009a6654)
- 新版 `009a6810`（命令位置の公開資料なし） · `009a67f0`（命令位置の公開資料なし）

~~~diff
- 009a6674 ["COPY", "register:0:8", ["register:4040:8"]]
- 009a6674 ["INT_ADD", "register:40f0:8", ["const:9a6674:8", "const:4:8"]]
- 009a6674 ["CALLIND", null, ["register:0:8"]]
- 009a6674 bytes 00013fd6
+ 009a6810 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009a6810 ["INT_ADD", "register:40f0:8", ["const:9a6810:8", "const:4:8"]]
+ 009a6810 ["CALLIND", null, ["register:0:8"]]
+ 009a6810 bytes 00013fd6
- 009a6654 ["INT_ADD", "register:40f0:8", ["const:9a6654:8", "const:4:8"]]
- 009a6654 ["CALL", null, ["callee:00c53d00:8"]]
+ 009a67f0 ["INT_ADD", "register:40f0:8", ["const:9a67f0:8", "const:4:8"]]
+ 009a67f0 ["CALL", null, ["callee:00c53d00:8"]]
- 009a6654 bytes a3b40a94
+ 009a67f0 bytes 44b50a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e5203e0312ff2004f7dba8fee611d6a"></a>

### [`009a6688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a6688.md) → [`009a6824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a6824.md) FUN_009a6824

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 33.33% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009a66b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009a66c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009a684c"
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
      "unmatched:009a66b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a6860"
      ]
    ],
    [
      "unmatched:009a66c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a6874"
      ]
    ],
    [
      "009a6864",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:009a66b8"
      ]
    ]
  ],
  "added": [
    [
      "009a684c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a6860"
      ]
    ],
    [
      "009a685c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a6874"
      ]
    ],
    [
      "009a6864",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009a6854"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a66b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a6688.md#insn-009a66b0) · [`009a66c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a6688.md#insn-009a66c0)
- 新版 `009a684c`（命令位置の公開資料なし）

~~~diff
- 009a66b0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 009a66b0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 009a66b0 bytes a1000054
- 009a66c0 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 009a66c0 bytes c0000054
+ 009a684c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 009a684c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 009a684c bytes a1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a430eaa30e41ed32ca197d2f6215f91"></a>

### [`009a68b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a68b0.md) → [`009a6a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a6a4c.md) FUN_009a6a4c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009a6204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a6204.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`009a6848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a6848.md) [`009a6a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a6a0c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`009a63a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a63a0.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`009a69e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a69e4.md) [`009a6ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a6ba8.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.93% / 新版 81.93%

CFGの説明率　旧版 14.81% / 新版 12.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a68d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a68d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009a68d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a68d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a68d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:009a68d8",
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
      "009a6a6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "009a6a70",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "009a6a74",
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

- 旧版 [`009a68d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a68b0.md#insn-009a68d0) · [`009a68d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a68b0.md#insn-009a68d4) · [`009a68d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a68b0.md#insn-009a68d8)

~~~diff
- 009a68d0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009a68d0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009a68d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009a68d0 bytes a8831ff8
- 009a68d4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 009a68d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 009a68d4 bytes e00f00f9
- 009a68d8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 009a68d8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 009a68d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 009a68d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 009a68d8 bytes ff830039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60564049f5364ce2b24449ae3d1403f1"></a>

### [`009a6a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a6a98.md) → [`009a6c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a6/009a6c34.md) FUN_009a6c34

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "009a6ab0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009a6c4c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "009a6ab8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009a6ab0",
      "DATA",
      [
        "storage",
        "00c882a0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009a6ab4",
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
      "009a6c4c",
      "DATA",
      [
        "storage",
        "00c886a0",
        null,
        "undefined *"
      ]
    ],
    [
      "009a6c50",
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

- 旧版 [`009a6ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a6a98.md#insn-009a6ab0) · [`009a6ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a6/009a6a98.md#insn-009a6ab8)
- 新版 `009a6c4c`（命令位置の公開資料なし）

~~~diff
- 009a6ab0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 009a6ab0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009a6ab0 bytes 080000f9
- 009a6ab8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 009a6ab8 ["RETURN", null, ["register:0:8"]]
- 009a6ab8 bytes c0035fd6
+ 009a6c4c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 009a6c4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 009a6c4c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

