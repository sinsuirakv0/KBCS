# v16.0.0 → v16.0.1 · 命令位置の検査未完了 (10)

[一覧の目次](README.md)

<a id="compare-e8aed92c67ba8b5dc4afbf4d4fbfdc81"></a>

### [`00bb0534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0534.md) → [`00bb095c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb095c.md) FUN_00bb095c

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8dcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8dcb4.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5c640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c640.md)
- 新版 呼出元 1件 [`00b8e0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8e/00b8e0dc.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5ca40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ca40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 93.75% / 新版 88.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb0634"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bb0a5c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bb0634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0534.md#insn-00bb0634) · [`00bb0578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0534.md#insn-00bb0578)
- 新版 [`00bb0a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb095c.md#insn-00bb0a5c) · [`00bb09a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb095c.md#insn-00bb09a0)

~~~diff
- 00bb0634 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bb0634 ["RETURN", null, ["register:0:8"]]
- 00bb0634 bytes c0035fd6
+ 00bb0a5c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bb0a5c ["RETURN", null, ["register:0:8"]]
+ 00bb0a5c bytes c0035fd6
- 00bb0578 ["INT_ADD", "register:40f0:8", ["const:bb0578:8", "const:4:8"]]
- 00bb0578 ["CALL", null, ["callee:00c5ca40:8"]]
+ 00bb09a0 ["INT_ADD", "register:40f0:8", ["const:bb09a0:8", "const:4:8"]]
+ 00bb09a0 ["CALL", null, ["callee:00c5ca40:8"]]
- 00bb0578 bytes 32b00294
+ 00bb09a0 bytes 28b00294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6778c76318a8dc89ae29ab7d831fb7f4"></a>

### [`00bb0b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0b80.md) → [`00bb0fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb0fa8.md) _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEjT0_SA_SA_SA_T_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ccc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccc0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5d0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0c0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 93.81% / 新版 93.81%

CFGの説明率　旧版 79.31% / 新版 92.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb0b80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb0b80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb0b84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb0b80",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb0b84",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb0b88",
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
      "00bb0fa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bb0fac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bb0fb0",
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

- 旧版 [`00bb0b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0b80.md#insn-00bb0b80) · [`00bb0b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0b80.md#insn-00bb0b84) · [`00bb0b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0b80.md#insn-00bb0b88)

~~~diff
- 00bb0b80 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bb0b80 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bb0b80 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00bb0b80 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb0b80 bytes f85fbca9
- 00bb0b84 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bb0b84 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bb0b84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb0b84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb0b84 bytes f65701a9
- 00bb0b88 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb0b88 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb0b88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bb0b88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb0b88 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-083a793c49141f284b40b5b2ddf14f0d"></a>

### [`00bb0f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0f68.md) → [`00bb1390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1390.md) _ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEbT0_SA_T_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5c9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c9c0.md) · 呼出先 2件 [`00bb0d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0d04.md) [`00c5ccc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccc0.md)
- 新版 呼出元 1件 [`00c5cdc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cdc0.md) · 呼出先 2件 [`00bb112c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb112c.md) [`00c5d0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0c0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.67% / 新版 97.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb13d0",
      "DATA",
      [
        "storage",
        "0030e1ea",
        "switchD_00bb0fb4::switchdataD_0030e1ea",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00bb13d0",
      "DATA",
      [
        "storage",
        "0030e22a",
        "switchD_00bb13dc::switchdataD_0030e22a",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb0fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0f68.md#insn-00bb0fa0) · [`00bb0fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0f68.md#insn-00bb0fa4) · [`00bb0fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0f68.md#insn-00bb0fc4)
- 新版 [`00bb13c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1390.md#insn-00bb13c8) · [`00bb13ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1390.md#insn-00bb13ec)

~~~diff
- 00bb0fa0 ["COPY", "tmp:0:8", ["const:1ea:8"]]
- 00bb0fa0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bb0fa0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bb0fa0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bb13c8 ["COPY", "tmp:0:8", ["const:22a:8"]]
+ 00bb13c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb13c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb13c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bb0fa0 bytes 29a90791
+ 00bb13c8 bytes 29a90891
- 00bb0fa4 ["COPY", "register:4050:8", ["const:bb0fb8:8"]]
- 00bb0fa4 bytes aa000010
- 00bb0fc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb0fc4 ["INT_ADD", "register:40f0:8", ["const:bb0fc4:8", "const:4:8"]]
- 00bb0fc4 ["CALLIND", null, ["register:0:8"]]
+ 00bb13ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb13ec ["INT_ADD", "register:40f0:8", ["const:bb13ec:8", "const:4:8"]]
+ 00bb13ec ["CALLIND", null, ["register:0:8"]]
- 00bb0fc4 bytes 00013fd6
+ 00bb13ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fc682d51a4daabdfa15d5041afe6196"></a>

### [`00bb134c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb134c.md) → [`00bb1774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1774.md) _ZNSt6__ndk16__sortIRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c9e0.md) · 呼出先 5件 [`00bb19e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb19e8.md) [`00c5c7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c7e0.md) [`00c5c9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c9a0.md) [`00c5c9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c9e0.md) [`00c5cca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cca0.md)
- 新版 呼出元 1件 [`00c5cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cde0.md) · 呼出先 5件 [`00bb1e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1e10.md) [`00c5cbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cbe0.md) [`00c5cda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cda0.md) [`00c5cde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cde0.md) [`00c5d0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0a0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 96.63% / 新版 96.63%

CFGの説明率　旧版 75.68% / 新版 72.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb1630"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb1634"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb1a58"
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
      "unmatched:00bb16e8",
      "DATA",
      [
        "storage",
        "0030e1f0",
        "switchD_00bb16f0::switchdataD_0030e1f0",
        "byte"
      ]
    ],
    [
      "unmatched:00bb1700",
      "READ",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb1704",
      "READ",
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
      "00bb1b10",
      "DATA",
      [
        "storage",
        "0030e230",
        "switchD_00bb1b18::switchdataD_0030e230",
        "byte"
      ]
    ],
    [
      "00bb1b28",
      "READ",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bb1b2c",
      "READ",
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

- 旧版 [`00bb1630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb134c.md#insn-00bb1630) · [`00bb1634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb134c.md#insn-00bb1634) · [`00bb1694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb134c.md#insn-00bb1694)

~~~diff
- 00bb1630 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00bb1630 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb1630 bytes e80200f9
- 00bb1634 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bb1634 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bb1634 bytes c90200f9
- 00bb1694 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb1694 ["INT_ADD", "register:40f0:8", ["const:bb1694:8", "const:4:8"]]
- 00bb1694 ["CALLIND", null, ["register:0:8"]]
- 00bb1694 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e47a2acc3cae916dc047a5215ca9c9ef"></a>

### [`00bb1864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1864.md) → [`00bb1c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1c8c.md) _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEjT0_SA_SA_SA_T_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5cca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cca0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5d0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0a0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.66% / 新版 88.66%

CFGの説明率　旧版 57.14% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb18e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb18e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb1904"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb18f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb1d6c"
      ]
    ],
    [
      "unmatched:00bb18f4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb1d20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb1d6c"
      ]
    ],
    [
      "00bb1d1c",
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

- 旧版 [`00bb18e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1864.md#insn-00bb18e0) · [`00bb18e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1864.md#insn-00bb18e4) · [`00bb18f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1864.md#insn-00bb18f4)

~~~diff
- 00bb18e0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bb18e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb18e0 bytes 680200f9
- 00bb18e4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bb18e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bb18e4 bytes c90200f9
- 00bb18f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb18f4 ["INT_ADD", "register:40f0:8", ["const:bb18f4:8", "const:4:8"]]
- 00bb18f4 ["CALLIND", null, ["register:0:8"]]
- 00bb18f4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea6a34693de1e959dff2b1b3e38c75ea"></a>

### [`00bb19e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb19e8.md) → [`00bb1e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1e10.md) FUN_00bb1e10

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bb134c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb134c.md) [`00bb1c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1c4c.md) · 呼出先 1件 [`00c5cca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cca0.md)
- 新版 呼出元 2件 [`00bb1774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1774.md) [`00bb2074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb2/00bb2074.md) · 呼出先 1件 [`00c5d0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0a0.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 53.85% / 新版 53.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb1a8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb1a90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb1eb4"
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
      "unmatched:00bb1a80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb1ef0"
      ]
    ],
    [
      "unmatched:00bb1a7c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb1ea8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb1ef0"
      ]
    ],
    [
      "00bb1ea4",
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

- 旧版 [`00bb1a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb19e8.md#insn-00bb1a7c) · [`00bb1a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb19e8.md#insn-00bb1a80) · [`00bb1a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb19e8.md#insn-00bb1a8c)

~~~diff
- 00bb1a7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb1a7c ["INT_ADD", "register:40f0:8", ["const:bb1a7c:8", "const:4:8"]]
- 00bb1a7c ["CALLIND", null, ["register:0:8"]]
- 00bb1a7c bytes 00013fd6
- 00bb1a80 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00bb1a80 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00bb1a80 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00bb1a80 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00bb1a80 bytes 40020036
- 00bb1a8c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb1a8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb1a8c bytes 880200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09b01aa1acfa3444f396c4aaf3c02c09"></a>

### [`00bb1af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1af0.md) → [`00bb1f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1f18.md) _ZNSt6__ndk118__insertion_sort_3IRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c7e0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5cbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cbe0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 73.33% / 新版 75.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb1bec"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bb2014"
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
      "unmatched:00bb1bec",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb2014",
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

- 旧版 [`00bb1bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1af0.md#insn-00bb1bec) · [`00bb1b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1af0.md#insn-00bb1b04)
- 新版 [`00bb2014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1f18.md#insn-00bb2014)

~~~diff
- 00bb1bec ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb1bec ["INT_ADD", "register:40f0:8", ["const:bb1bec:8", "const:4:8"]]
- 00bb1bec ["CALLIND", null, ["register:0:8"]]
- 00bb1bec bytes 00013fd6
+ 00bb2014 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb2014 ["INT_ADD", "register:40f0:8", ["const:bb2014:8", "const:4:8"]]
+ 00bb2014 ["CALLIND", null, ["register:0:8"]]
+ 00bb2014 bytes 00013fd6
- 00bb1b04 ["COPY", "tmp:0:8", ["const:40:8"]]
- 00bb1b04 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 00bb1b04 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 00bb1b04 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 00bb1b04 bytes fd030191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab7947b54acfd7adb34f4340af4735bf"></a>

### [`00bb1c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1c4c.md) → [`00bb2074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb2/00bb2074.md) _ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEbT0_SA_T_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c9a0.md) · 呼出先 2件 [`00bb19e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb19e8.md) [`00c5cca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cca0.md)
- 新版 呼出元 1件 [`00c5cda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cda0.md) · 呼出先 2件 [`00bb1e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1e10.md) [`00c5d0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0a0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.86% / 新版 91.86%

CFGの説明率　旧版 75.41% / 新版 75.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb1cb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb1e10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb20e0"
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
      "unmatched:00bb1c7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb214c"
      ]
    ],
    [
      "00bb20b4",
      "DATA",
      [
        "storage",
        "0030e1f6",
        "switchD_00bb1c98::switchdataD_0030e1f6",
        "byte"
      ]
    ],
    [
      "unmatched:00bb1cbc",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb223c"
      ]
    ]
  ],
  "added": [
    [
      "00bb20a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb214c"
      ]
    ],
    [
      "00bb20b4",
      "DATA",
      [
        "storage",
        "0030e236",
        "switchD_00bb20c0::switchdataD_0030e236",
        "byte"
      ]
    ],
    [
      "00bb20e4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb223c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb1c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1c4c.md#insn-00bb1c7c) · [`00bb1cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1c4c.md#insn-00bb1cb8) · [`00bb1e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1c4c.md#insn-00bb1e10)

~~~diff
- 00bb1c7c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bb1c7c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bb1c7c ["CBRANCH", null, ["local:b10:8", "tmp:1:1"]]
- 00bb1c7c bytes 48050054
- 00bb1cb8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bb1cb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb1cb8 bytes 680200f9
- 00bb1e10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00bb1e10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb1e10 bytes 680600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92e1b9dbc977047d4491f73a8d5af1bc"></a>

### [`00bb211c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb211c.md) → [`00bb2544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb2/00bb2544.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c680.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5ca80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ca80.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 75.36% / 新版 75.36%

CFGの説明率　旧版 40.74% / 新版 44.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb211c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb211c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb2120"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb211c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb2120",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb2124",
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
      "00bb2544",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bb2548",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bb254c",
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

- 旧版 [`00bb211c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb211c.md#insn-00bb211c) · [`00bb2120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb211c.md#insn-00bb2120) · [`00bb2124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb211c.md#insn-00bb2124)

~~~diff
- 00bb211c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bb211c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bb211c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00bb211c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb211c bytes f85fbca9
- 00bb2120 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bb2120 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bb2120 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb2120 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb2120 bytes f65701a9
- 00bb2124 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb2124 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb2124 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bb2124 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb2124 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94743a9024af4990ca36920d70b84784"></a>

### [`00bb2c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2c58.md) → [`00bb3080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb3080.md) _ZN11flatbuffers13StripFileNameERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c330.md) · 呼出先 3件 [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md) [`00c5b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1c0.md) [`00c5b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3f0.md)
- 新版 呼出元 1件 [`00c5c730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c730.md) · 呼出先 3件 [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md) [`00c5b5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5c0.md) [`00c5b7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b7f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 83.72% / 新版 83.72%

CFGの説明率　旧版 75.00% / 新版 85.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb2c58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb2c5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb2c5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb2c58",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb2c5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb2c60",
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
      "00bb3080",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bb3084",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bb3088",
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

- 旧版 [`00bb2c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2c58.md#insn-00bb2c58) · [`00bb2c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2c58.md#insn-00bb2c5c) · [`00bb2c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2c58.md#insn-00bb2c60)

~~~diff
- 00bb2c58 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00bb2c58 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00bb2c58 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb2c58 bytes f70f1cf8
- 00bb2c5c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bb2c5c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bb2c5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb2c5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb2c5c bytes f65701a9
- 00bb2c60 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb2c60 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb2c60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bb2c60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb2c60 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3036c0a5a0d1a6f3a8e442a2b02b017"></a>

### [`00bb2d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2d04.md) → [`00bb312c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb312c.md) _ZN11flatbuffers11StripPrefixERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md) [`00c5b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3f0.md) [`00c5cd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md) [`00c5b7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b7f0.md) [`00c5d130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d130.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 85.29% / 新版 85.29%

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
      "site": "00bb2d34"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb2d3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb2d40"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bb2d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2d04.md#insn-00bb2d34) · [`00bb2d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2d04.md#insn-00bb2d3c) · [`00bb2d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2d04.md#insn-00bb2d40)

~~~diff
- 00bb2d34 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bb2d34 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00bb2d34 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bb2d34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
- 00bb2d34 bytes 2015809a
- 00bb2d3c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bb2d3c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bb2d3c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00bb2d3c ["COPY", "register:40a8:8", ["tmp:0:8"]]
- 00bb2d3c bytes 15018b9a
- 00bb2d40 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bb2d40 ["COPY", "tmp:1:8", ["register:4060:8"]]
- 00bb2d40 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bb2d40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00bb2d40 bytes 8115819a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54ed557bb4b4ac9c28425ed8c9c87d05"></a>

### [`00bb2f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2f1c.md) → [`00bb3344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb3344.md) _ZN11flatbuffers9PosixPathEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c470.md) · 呼出先 1件 [`00c5b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1c0.md)
- 新版 呼出元 1件 [`00c5c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c870.md) · 呼出先 1件 [`00c5b5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5c0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 93.75% / 新版 95.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb2f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2f1c.md#insn-00bb2f34) · [`00bb2f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2f1c.md#insn-00bb2f50) · [`00bb2f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2f1c.md#insn-00bb2f5c)
- 新版 [`00bb335c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb3344.md#insn-00bb335c) · [`00bb3378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb3344.md#insn-00bb3378) · [`00bb3384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb3344.md#insn-00bb3384)

~~~diff
- 00bb2f34 ["INT_ADD", "register:40f0:8", ["const:bb2f34:8", "const:4:8"]]
- 00bb2f34 ["CALL", null, ["callee:00c5b5c0:8"]]
+ 00bb335c ["INT_ADD", "register:40f0:8", ["const:bb335c:8", "const:4:8"]]
+ 00bb335c ["CALL", null, ["callee:00c5b5c0:8"]]
- 00bb2f34 bytes a3a00294
+ 00bb335c bytes 99a00294
- 00bb2f50 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00bb2f50 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
+ 00bb3378 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00bb3378 ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
- 00bb2f50 bytes a90800b4
+ 00bb3378 bytes a90800b4
- 00bb2f5c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bb2f5c ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
+ 00bb3384 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00bb3384 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 00bb2f5c bytes e3060054
+ 00bb3384 bytes e3060054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01ac133cbffee9d3e1a78682d24c210c"></a>

### [`00bb31d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb31d0.md) → [`00bb35f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb35f8.md) _ZN11flatbuffers15EnsureDirExistsERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bb31d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb31d0.md) · 呼出先 6件 [`00bb31d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb31d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md) [`00c59e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e50.md)
- 新版 呼出元 1件 [`00bb35f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb35f8.md) · 呼出先 6件 [`00bb35f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb35f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md) [`00c5a250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a250.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 72.22% / 新版 76.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb32c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bb36ec"
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
      "00bb3654",
      "PARAM",
      [
        "storage",
        "002a85ab",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb32c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb3708"
      ]
    ]
  ],
  "added": [
    [
      "00bb3654",
      "PARAM",
      [
        "storage",
        "002a8678",
        null,
        null
      ]
    ],
    [
      "00bb36ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb3708"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb32c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb31d0.md#insn-00bb32c4) · [`00bb3208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb31d0.md#insn-00bb3208)
- 新版 [`00bb36ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb35f8.md#insn-00bb36ec) · [`00bb3630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb35f8.md#insn-00bb3630)

~~~diff
- 00bb32c4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bb32c4 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00bb32c4 bytes e1000054
+ 00bb36ec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00bb36ec ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00bb36ec bytes e1000054
- 00bb3208 ["COPY", "tmp:0:8", ["const:5ab:8"]]
- 00bb3208 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00bb3208 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00bb3208 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00bb3630 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 00bb3630 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00bb3630 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00bb3630 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00bb3208 bytes b5ae1691
+ 00bb3630 bytes b5e21991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17753f8178fb356ccec12326b68dba80"></a>

### [`00bb32f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb32f4.md) → [`00bb371c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb371c.md) _ZN11flatbuffers12AbsolutePathERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c320.md) · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)
- 新版 呼出元 1件 [`00c5c720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c720.md) · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.98% / 新版 82.98%

CFGの説明率　旧版 45.45% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb331c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb3744"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb332c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb331c",
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
      "00bb3744",
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

- 旧版 [`00bb331c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb32f4.md#insn-00bb331c) · [`00bb332c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb32f4.md#insn-00bb332c)
- 新版 [`00bb3744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb371c.md#insn-00bb3744)

~~~diff
- 00bb331c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00bb331c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb331c bytes e80f00f9
- 00bb332c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bb332c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00bb332c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bb332c ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
- 00bb332c bytes 2015809a
+ 00bb3744 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
+ 00bb3744 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00bb3744 bytes e80f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58a6c7994b37b0e35852426a1b6b7339"></a>

### [`00bb3994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb3994.md) → [`00bb3dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb3dbc.md) _ZN11flatbuffers18RemoveStringQuotesERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md) [`00c5b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md) [`00c5b7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b7f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 52.17% / 新版 52.17%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb39a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb39ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb39b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb39b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb3e14"
      ]
    ],
    [
      "unmatched:00bb39cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb3e14"
      ]
    ]
  ],
  "added": [
    [
      "00bb3de0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb3e14"
      ]
    ],
    [
      "00bb3df4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb3e14"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb39a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb3994.md#insn-00bb39a8) · [`00bb39ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb3994.md#insn-00bb39ac) · [`00bb39b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb3994.md#insn-00bb39b8)

~~~diff
- 00bb39a8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bb39a8 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00bb39a8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bb39a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
- 00bb39a8 bytes 4915809a
- 00bb39ac ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00bb39ac ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bb39ac ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00bb39ac ["COPY", "register:4050:8", ["tmp:0:8"]]
- 00bb39ac bytes 8a018b9a
- 00bb39b8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bb39b8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bb39b8 bytes a3010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1bdf48cd24dc93ccf68a14e0dc0f82c"></a>

### [`00bb495c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb4/00bb495c.md) → [`00bb4d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb4/00bb4d84.md) FUN_00bb4d84

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bb3be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb3be8.md) · 呼出先 3件 [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md) [`00c5ce50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce50.md) [`00c5ce60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce60.md)
- 新版 呼出元 1件 [`00bb4010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb4/00bb4010.md) · 呼出先 3件 [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md) [`00c5d250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d250.md) [`00c5d260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d260.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 6.54% / 新版 6.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 18件, `unresolved_call_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb4b38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb4c24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb4c80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb499c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb5134"
      ]
    ],
    [
      "unmatched:00bb49fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb5134"
      ]
    ],
    [
      "00bb4e40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb4f50"
      ]
    ]
  ],
  "added": [
    [
      "00bb4dc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb5134"
      ]
    ],
    [
      "00bb4e24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb5134"
      ]
    ],
    [
      "00bb4e40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb4e88"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb499c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb4/00bb495c.md#insn-00bb499c) · [`00bb49f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb4/00bb495c.md#insn-00bb49f0) · [`00bb49fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb4/00bb495c.md#insn-00bb49fc)

~~~diff
- 00bb499c ["INT_EQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
- 00bb499c ["CBRANCH", null, ["local:b78:8", "tmp:0:1"]]
- 00bb499c bytes 8b1b00b4
- 00bb49f0 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00bb49f0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bb49f0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bb49f0 ["COPY", "register:4058:8", ["tmp:0:8"]]
- 00bb49f0 bytes 6b01899a
- 00bb49fc ["CBRANCH", null, ["local:b78:8", "register:102:1"]]
- 00bb49fc bytes 82180054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74df9b6c19d1eb495af0cf48b3f25cfe"></a>

### [`00bb4d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb4/00bb4d40.md) → [`00bb5168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5168.md) _ZN11flatbuffers11CharToLowerEc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bb3be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb3be8.md) · 呼出先 1件 [`00c5ce50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce50.md)
- 新版 呼出元 1件 [`00bb4010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb4/00bb4010.md) · 呼出先 1件 [`00c5d250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d250.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb4d54"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bb517c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bb4d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb4/00bb4d40.md#insn-00bb4d54) · [`00bb4d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb4/00bb4d40.md#insn-00bb4d4c)
- 新版 [`00bb517c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5168.md#insn-00bb517c) · [`00bb5174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5168.md#insn-00bb5174)

~~~diff
- 00bb4d54 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bb4d54 ["RETURN", null, ["register:0:8"]]
- 00bb4d54 bytes c0035fd6
+ 00bb517c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bb517c ["RETURN", null, ["register:0:8"]]
+ 00bb517c bytes c0035fd6
- 00bb4d4c ["INT_ADD", "register:40f0:8", ["const:bb4d4c:8", "const:4:8"]]
- 00bb4d4c ["CALL", null, ["callee:00c5d250:8"]]
+ 00bb5174 ["INT_ADD", "register:40f0:8", ["const:bb5174:8", "const:4:8"]]
+ 00bb5174 ["CALL", null, ["callee:00c5d250:8"]]
- 00bb4d4c bytes 41a00294
+ 00bb5174 bytes 37a00294
~~~


<a id="compare-c771a4a3d23ad11dafbc1dad194596ca"></a>

### [`00bb5084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5084.md) → [`00bb54ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb54ac.md) FUN_00bb54ac

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md) [`00c5cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md) [`00c5d1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1b0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb50a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb50a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb54cc"
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
      "unmatched:00bb5094",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bb50a4",
      "DATA",
      [
        "storage",
        "00c90ac0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bb50a8",
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
      "00bb54bc",
      "READ",
      [
        "storage",
        "00c9b030",
        null,
        "pointer"
      ]
    ],
    [
      "00bb54cc",
      "DATA",
      [
        "storage",
        "00c90ec0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb54d0",
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

- 旧版 [`00bb50a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5084.md#insn-00bb50a4) · [`00bb50a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5084.md#insn-00bb50a8)
- 新版 [`00bb54cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb54ac.md#insn-00bb54cc)

~~~diff
- 00bb50a4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bb50a4 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00bb50a4 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bb50a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bb50a4 bytes 090401f8
- 00bb50a8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bb50a8 ["INT_ADD", "register:4098:8", ["register:4098:8", "const:b8:8"]]
- 00bb50a8 ["STORE", null, ["const:1b1:8", "register:4098:8", "tmp:0:8"]]
- 00bb50a8 bytes 688e0bf8
+ 00bb54cc ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00bb54cc ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00bb54cc ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
+ 00bb54cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00bb54cc bytes 090401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a72b763b27f9b6acc1d2be0666e80a65"></a>

### [`00bb51dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb51dc.md) → [`00bb5604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5604.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE4openEPKcj

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b10.md) · 呼出先 3件 [`00c59c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c00.md) [`00c59c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c60.md) [`00c59c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c90.md)
- 新版 呼出元 1件 [`00c58f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f10.md) · 呼出先 3件 [`00c5a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a000.md) [`00c5a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a060.md) [`00c5a090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a090.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 77.03% / 新版 77.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb5650",
      "DATA",
      [
        "storage",
        "0030e516",
        "switchD_00bb5238::switchdataD_0030e516",
        "byte"
      ]
    ],
    [
      "00bb56e8",
      "PARAM",
      [
        "storage",
        "002b3694",
        null,
        null
      ]
    ],
    [
      "00bb56e8",
      "PARAM",
      [
        "storage",
        "002a1b07",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb5650",
      "DATA",
      [
        "storage",
        "0030e556",
        "switchD_00bb5660::switchdataD_0030e556",
        "byte"
      ]
    ],
    [
      "00bb56e8",
      "PARAM",
      [
        "storage",
        "002b36d4",
        null,
        null
      ]
    ],
    [
      "00bb56e8",
      "PARAM",
      [
        "storage",
        "002a1bd4",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb5220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb51dc.md#insn-00bb5220) · [`00bb5224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb51dc.md#insn-00bb5224) · [`00bb5230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb51dc.md#insn-00bb5230)
- 新版 [`00bb5648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5604.md#insn-00bb5648)

~~~diff
- 00bb5220 ["COPY", "tmp:0:8", ["const:516:8"]]
- 00bb5220 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bb5220 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bb5220 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bb5648 ["COPY", "tmp:0:8", ["const:556:8"]]
+ 00bb5648 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb5648 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb5648 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bb5220 bytes 29591491
+ 00bb5648 bytes 29591591
- 00bb5224 ["COPY", "register:4050:8", ["const:bb51f4:8"]]
- 00bb5224 bytes 8afeff10
- 00bb5230 ["COPY", "register:4040:8", ["const:2bc000:8"]]
- 00bb5230 bytes 28b8fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab340317a92bc9e2cb4a5d0cf0bd3c02"></a>

### [`00bb5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5750.md) → [`00bb5b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5b78.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE7seekposENS_4fposI9mbstate_tEEj

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5cde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cde0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5d1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1e0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 62.50% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb577c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bb5ba4"
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
      "unmatched:00bb577c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb5ba4",
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

- 旧版 [`00bb577c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5750.md#insn-00bb577c) · [`00bb5764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5750.md#insn-00bb5764)
- 新版 [`00bb5ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5b78.md#insn-00bb5ba4) · [`00bb5b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5b78.md#insn-00bb5b8c)

~~~diff
- 00bb577c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb577c ["INT_ADD", "register:40f0:8", ["const:bb577c:8", "const:4:8"]]
- 00bb577c ["CALLIND", null, ["register:0:8"]]
- 00bb577c bytes 00013fd6
+ 00bb5ba4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb5ba4 ["INT_ADD", "register:40f0:8", ["const:bb5ba4:8", "const:4:8"]]
+ 00bb5ba4 ["CALLIND", null, ["register:0:8"]]
+ 00bb5ba4 bytes 00013fd6
- 00bb5764 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bb5764 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bb5b8c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bb5b8c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bb5764 bytes a80100b4
+ 00bb5b8c bytes a80100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7657b2d76a36e9a2ea3972b91ce7f310"></a>

### [`00bb59b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb59b0.md) → [`00bb5dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5dd8.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE9underflowEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bb5ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5ec4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c59c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bb62ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb62ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5a080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a080.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.28% / 新版 84.28%

CFGの説明率　旧版 64.15% / 新版 64.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5a1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5a28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5a28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb5a30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb5e88"
      ]
    ],
    [
      "unmatched:00bb5ba4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb5e58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb5e88"
      ]
    ],
    [
      "00bb5fcc",
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

- 旧版 [`00bb5a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb59b0.md#insn-00bb5a00) · [`00bb5a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb59b0.md#insn-00bb5a1c) · [`00bb5a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb59b0.md#insn-00bb5a28)

~~~diff
- 00bb5a00 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00bb5a00 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bb5a00 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bb5a00 ["COPY", "register:4048:8", ["tmp:0:8"]]
- 00bb5a00 bytes 4901899a
- 00bb5a1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c:8"]]
- 00bb5a1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00bb5a1c bytes 699e00b9
- 00bb5a28 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00bb5a28 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00bb5a28 ["INT_ADD", "tmp:2:8", ["register:4098:8", "const:10:8"]]
- 00bb5a28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb5a28 bytes 6a2201a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd1125450a82a61d889566bb5f556991"></a>

### [`00bb5c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5c8c.md) → [`00bb60b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb60b4.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE8overflowEi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb5ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5ec4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb62ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb62ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a220.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 95.07% / 新版 95.07%

CFGの説明率　旧版 75.93% / 新版 82.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5cb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb60d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5dac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb5cb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb5dac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb62e8"
      ]
    ],
    [
      "unmatched:00bb5dd0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb60d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bb61d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb62e8"
      ]
    ],
    [
      "00bb61f8",
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

- 旧版 [`00bb5cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5c8c.md#insn-00bb5cb0) · [`00bb5dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5c8c.md#insn-00bb5dac) · [`00bb5dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5c8c.md#insn-00bb5dd0)

~~~diff
- 00bb5cb0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00bb5cb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb5cb0 bytes e80f00f9
- 00bb5dac ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bb5dac ["CBRANCH", null, ["local:b38:8", "tmp:0:1"]]
- 00bb5dac bytes a00800b4
- 00bb5dd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb5dd0 ["INT_ADD", "register:40f0:8", ["const:bb5dd0:8", "const:4:8"]]
- 00bb5dd0 ["CALLIND", null, ["register:0:8"]]
- 00bb5dd0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1e56e28965d23b2cd418f1df34b71ec"></a>

### [`00bb61a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb61a0.md) → [`00bb65c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb65c8.md) _ZNKSt6__ndk110__function6__funcIPFccENS_9allocatorIS3_EES2_E7__cloneEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb61c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb61d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb65f0"
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
      "00bb65e4",
      "READ",
      [
        "storage",
        "00c9b4e8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bb61c8",
      "DATA",
      [
        "storage",
        "00c90d78",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "00bb65e4",
      "READ",
      [
        "storage",
        "00c9b8e8",
        null,
        "pointer"
      ]
    ],
    [
      "00bb65f0",
      "DATA",
      [
        "storage",
        "00c91178",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb61c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb61a0.md#insn-00bb61c8) · [`00bb61d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb61a0.md#insn-00bb61d0) · [`00bb61d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb61a0.md#insn-00bb61d8)

~~~diff
- 00bb61c8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00bb61c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb61c8 bytes 080000f9
- 00bb61d0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00bb61d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb61d0 bytes 080400f9
- 00bb61d8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bb61d8 ["RETURN", null, ["register:0:8"]]
- 00bb61d8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1eea5cf161d36997e8112c3040c41627"></a>

### [`00bb61dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb61dc.md) → [`00bb6604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6604.md) _ZNKSt6__ndk110__function6__funcIPFccENS_9allocatorIS3_EES2_E7__cloneEPNS0_6__baseIS2_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 14.29% / 新版 14.29%

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
      "site": "00bb61e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb61f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb6610"
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
      "unmatched:00bb61e0",
      "READ",
      [
        "storage",
        "00c9b4e8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bb61e8",
      "DATA",
      [
        "storage",
        "00c90d78",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "00bb6608",
      "READ",
      [
        "storage",
        "00c9b8e8",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6610",
      "DATA",
      [
        "storage",
        "00c91178",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb61e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb61dc.md#insn-00bb61e8) · [`00bb61f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb61dc.md#insn-00bb61f0)
- 新版 [`00bb6610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6604.md#insn-00bb6610)

~~~diff
- 00bb61e8 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00bb61e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb61e8 bytes 280000f9
- 00bb61f0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 00bb61f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb61f0 bytes 280400f9
+ 00bb6610 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00bb6610 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00bb6610 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-feaceb3431d12cf2d89d0a8ec2f36072"></a>

### [`00bb627c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb627c.md) → [`00bb66a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb66a4.md) FUN_00bb66a4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bb87b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb87b4.md) · 呼出先 2件 [`00c5a6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6d0.md) [`00c5a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a860.md)
- 新版 呼出元 1件 [`00bb8bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8bdc.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aad0.md) [`00c5ac60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac60.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb627c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6280"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6280"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb627c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb6280",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb628c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac60"
      ]
    ]
  ],
  "added": [
    [
      "00bb66a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb66a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb66b4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb627c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb627c.md#insn-00bb627c) · [`00bb6280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb627c.md#insn-00bb6280) · [`00bb628c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb627c.md#insn-00bb628c)

~~~diff
- 00bb627c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bb627c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb627c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb627c bytes f30f1ef8
- 00bb6280 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb6280 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb6280 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb6280 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb6280 bytes fd7b01a9
- 00bb628c ["INT_ADD", "register:40f0:8", ["const:bb628c:8", "const:4:8"]]
- 00bb628c ["CALL", null, ["callee:00c5ac60:8"]]
- 00bb628c bytes 75910294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60b21a2ca29b9f80276be9d83dd0ed7d"></a>

### [`00bb62f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb62f0.md) → [`00bb6718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6718.md) _ZN8firebase9messaging8internal36RegisterTerminateOnDefaultAppDestroyEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d020.md) · 呼出先 5件 [`00bb7224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7224.md) [`00c5a7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7d0.md) [`00c5a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7f0.md) [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md) [`00c5a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a860.md)
- 新版 呼出元 1件 [`00c5d420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d420.md) · 呼出先 5件 [`00bb764c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb764c.md) [`00c5abd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abd0.md) [`00c5abf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abf0.md) [`00c5ac00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac00.md) [`00c5ac60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac60.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb62f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb62f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb6718"
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
      "unmatched:00bb62f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb62fc",
      "PARAM",
      [
        "storage",
        "0030e69f",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bb6300",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5abd0"
      ]
    ]
  ],
  "added": [
    [
      "00bb6718",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb6724",
      "PARAM",
      [
        "storage",
        "0030e6df",
        null,
        "string"
      ]
    ],
    [
      "00bb6728",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5abd0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb62f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb62f0.md#insn-00bb62f0) · [`00bb6300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb62f0.md#insn-00bb6300) · [`00bb6304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb62f0.md#insn-00bb6304)

~~~diff
- 00bb62f0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb62f0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb62f0 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00bb62f0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb62f0 bytes fd7bbfa9
- 00bb6300 ["INT_ADD", "register:40f0:8", ["const:bb6300:8", "const:4:8"]]
- 00bb6300 ["CALL", null, ["callee:00c5abd0:8"]]
- 00bb6300 bytes 34910294
- 00bb6304 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00bb6304 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00bb6304 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00bb6304 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00bb6304 bytes 60000036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8e31c456f4b5bfd321df093e33627a1"></a>

### [`00bb7828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7828.md) → [`00bb7c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7c50.md) _ZN8firebase9messaging7MessageaSERKS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d000.md) · 呼出先 7件 [`0053b73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b73c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) [`00c5cec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cec0.md)
- 新版 呼出元 1件 [`00c5d400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d400.md) · 呼出先 7件 [`0053b77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b77c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) [`00c5d2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2c0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.04% / 新版 97.04%

CFGの説明率　旧版 77.78% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb7a24"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb7a28"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bb7e4c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bb7a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7828.md#insn-00bb7a24) · [`00bb7a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7828.md#insn-00bb7a28)
- 新版 [`00bb7e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7c50.md#insn-00bb7e4c)

~~~diff
- 00bb7a24 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bb7a24 ["COPY", "tmp:1:8", ["register:4058:8"]]
- 00bb7a24 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bb7a24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
- 00bb7a24 bytes 6115889a
- 00bb7a28 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00bb7a28 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bb7a28 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00bb7a28 ["COPY", "register:4010:8", ["tmp:0:8"]]
- 00bb7a28 bytes 82018a9a
+ 00bb7e4c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00bb7e4c ["COPY", "tmp:1:8", ["register:4058:8"]]
+ 00bb7e4c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00bb7e4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
+ 00bb7e4c bytes 6115889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-799233f6b13fba020abc07ef0544bdd0"></a>

### [`00bb7d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7d78.md) → [`00bb81a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb81a0.md) _ZN8firebase9messaging12NotificationaSERKS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5cee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cee0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md) [`00c5cc30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc30.md)
- 新版 呼出元 1件 [`00c5d2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2e0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md) [`00c5d030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d030.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 95.73% / 新版 95.73%

CFGの説明率　旧版 64.29% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb7ea8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb7eac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bb82d0"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bb7ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7d78.md#insn-00bb7ea8) · [`00bb7eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7d78.md#insn-00bb7eac) · [`00bb7f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7d78.md#insn-00bb7f48)

~~~diff
- 00bb7ea8 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00bb7ea8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bb7ea8 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00bb7ea8 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00bb7ea8 bytes 61018a9a
- 00bb7eac ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00bb7eac ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bb7eac ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bb7eac ["COPY", "register:4010:8", ["tmp:0:8"]]
- 00bb7eac bytes 8201899a
- 00bb7f48 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bb7f48 ["RETURN", null, ["register:0:8"]]
- 00bb7f48 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daa6f7f3ce2b51f424beb6f90e45f71e"></a>

### [`00bb83f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb83f4.md) → [`00bb881c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb881c.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageENS_9allocatorIS4_EEE10push_frontEOS4_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d070.md) · 呼出先 4件 [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00c5d470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d470.md) · 呼出先 4件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 68.18% / 新版 68.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8470"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8470"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb8898"
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
      "00bb8854",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bb8478"
      ]
    ],
    [
      "unmatched:00bb8474",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8928"
      ]
    ],
    [
      "unmatched:00bb852c",
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
      "00bb8854",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb88a0"
      ]
    ],
    [
      "00bb889c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8928"
      ]
    ],
    [
      "00bb8954",
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

- 旧版 [`00bb8470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb83f4.md#insn-00bb8470) · [`00bb8480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb83f4.md#insn-00bb8480) · [`00bb8530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb83f4.md#insn-00bb8530)

~~~diff
- 00bb8470 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bb8470 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00bb8470 ["INT_ADD", "tmp:2:8", ["register:4098:8", "const:8:8"]]
- 00bb8470 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb8470 bytes 76a200a9
- 00bb8480 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bb8480 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00bb8480 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bb8480 ["INT_ADD", "tmp:1:8", ["const:0:8", "const:1:8"]]
- 00bb8480 bytes 08159f9a
- 00bb8530 ["INT_ADD", "register:40f0:8", ["const:bb8530:8", "const:4:8"]]
- 00bb8530 ["CALL", null, ["callee:00b402c0:8"]]
- 00bb8530 bytes 5a1efe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8481bfcc15df1695d431f0e0ca2359a2"></a>

### [`00bb8b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8b44.md) → [`00bb8f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8f6c.md) _ZN8firebase9messaging18firebase_messaging10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.67% / 新版 26.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8b44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8b48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8b48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb8b44",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb8b48",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb8f80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bb8b68"
      ]
    ]
  ],
  "added": [
    [
      "00bb8f6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb8f70",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb8f80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8f90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8b44.md#insn-00bb8b44) · [`00bb8b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8b44.md#insn-00bb8b48) · [`00bb8b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8b44.md#insn-00bb8b64)

~~~diff
- 00bb8b44 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bb8b44 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb8b44 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb8b44 bytes f30f1ef8
- 00bb8b48 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb8b48 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb8b48 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb8b48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb8b48 bytes fd7b01a9
- 00bb8b64 ["INT_ADD", "register:40f0:8", ["const:bb8b64:8", "const:4:8"]]
- 00bb8b64 ["CALL", null, ["callee:00c5b000:8"]]
- 00bb8b64 bytes 27880294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0983a6c0c0ebe38332f614e17673bd5"></a>

### [`00bb8bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8bc0.md) → [`00bb8fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8fe8.md) _ZN8firebase9messaging27registration_intent_service19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8bec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb9014"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8bd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb8bd0",
      "READ",
      [
        "storage",
        "01125f18",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bb8bd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb9018"
      ]
    ],
    [
      "unmatched:00bb8bdc",
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
      "00bb8ff8",
      "READ",
      [
        "storage",
        "01126318",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8ffc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb9018"
      ]
    ],
    [
      "00bb9004",
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

- 旧版 [`00bb8bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8bc0.md#insn-00bb8bd4) · [`00bb8be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8bc0.md#insn-00bb8be4) · [`00bb8bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8bc0.md#insn-00bb8bec)

~~~diff
- 00bb8bd4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bb8bd4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bb8bd4 bytes e80000b5
- 00bb8be4 ["INT_ADD", "register:40f0:8", ["const:bb8be4:8", "const:4:8"]]
- 00bb8be4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bb8be4 bytes cb870294
- 00bb8bec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f18:8"]]
- 00bb8bec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8bec bytes 608e07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62f8afbe9ac52dcec950d6c121359fc0"></a>

### [`00bb8c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8c88.md) → [`00bb90b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb90b0.md) _ZN8firebase9messaging27registration_intent_service8GetClassEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8c90"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bb90b8"
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
      "unmatched:00bb8c8c",
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
      "00bb90b4",
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

- 旧版 [`00bb8c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8c88.md#insn-00bb8c90) · [`00bb8c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8c88.md#insn-00bb8c88)
- 新版 [`00bb90b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb90b0.md#insn-00bb90b8)

~~~diff
- 00bb8c90 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bb8c90 ["RETURN", null, ["register:0:8"]]
- 00bb8c90 bytes c0035fd6
+ 00bb90b8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bb90b8 ["RETURN", null, ["register:0:8"]]
+ 00bb90b8 bytes c0035fd6
- 00bb8c88 ["COPY", "register:4040:8", ["const:1125000:8"]]
- 00bb8c88 bytes 682b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f11e257cb2f0cdb4c0fb27ad624824e"></a>

### [`00bb8de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8de0.md) → [`00bb9208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9208.md) _ZN8firebase9messaging27registration_intent_service11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.67% / 新版 26.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8de0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8de4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8de4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb8de0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb8de4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb921c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bb8e04"
      ]
    ]
  ],
  "added": [
    [
      "00bb9208",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb920c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb921c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb922c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8de0.md#insn-00bb8de0) · [`00bb8de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8de0.md#insn-00bb8de4) · [`00bb8e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8de0.md#insn-00bb8e00)

~~~diff
- 00bb8de0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bb8de0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb8de0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb8de0 bytes f30f1ef8
- 00bb8de4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb8de4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb8de4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb8de4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb8de4 bytes fd7b01a9
- 00bb8e00 ["INT_ADD", "register:40f0:8", ["const:bb8e00:8", "const:4:8"]]
- 00bb8e00 ["CALL", null, ["callee:00c5b000:8"]]
- 00bb8e00 bytes 80870294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0c67a786c7201fb36fa0c530e69f3f8"></a>

### [`00bb8e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8e8c.md) → [`00bb92b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb92b4.md) _ZN8firebase9messaging27registration_intent_service10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 33.33% / 新版 33.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8ea0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bb92c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8eac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb8ea0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bb8eb0"
      ]
    ],
    [
      "unmatched:00bb8ea8",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bb8eac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bb92c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb92d8"
      ]
    ],
    [
      "00bb92d0",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bb92d4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8e8c.md#insn-00bb8ea0) · [`00bb8eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8e8c.md#insn-00bb8eac) · [`00bb8ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8e8c.md#insn-00bb8ec4)

~~~diff
- 00bb8ea0 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bb8ea0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bb8ea0 bytes 8b000054
- 00bb8eac ["INT_ADD", "register:40f0:8", ["const:bb8eac:8", "const:4:8"]]
- 00bb8eac ["CALL", null, ["callee:00c5b000:8"]]
- 00bb8eac bytes 55870294
- 00bb8ec4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bb8ec4 ["RETURN", null, ["register:0:8"]]
- 00bb8ec4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eeec9bfebff2fde2da3c7cd1f9abb54d"></a>

### [`00bb8ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8ec8.md) → [`00bb92f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb92f0.md) _ZN8firebase9messaging26illegal_argument_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 31.25% / 新版 31.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8ef4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb931c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8edc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb9300",
      "READ",
      [
        "storage",
        "01125f38",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bb8edc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bb8ef8"
      ]
    ],
    [
      "unmatched:00bb8ee8",
      "PARAM",
      [
        "storage",
        "002a4e38",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb9300",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9304",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb9320"
      ]
    ],
    [
      "00bb9310",
      "PARAM",
      [
        "storage",
        "002a4f14",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8ec8.md#insn-00bb8edc) · [`00bb8eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8ec8.md#insn-00bb8eec) · [`00bb8ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8ec8.md#insn-00bb8ef4)

~~~diff
- 00bb8edc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bb8edc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bb8edc bytes e80000b5
- 00bb8eec ["INT_ADD", "register:40f0:8", ["const:bb8eec:8", "const:4:8"]]
- 00bb8eec ["CALL", null, ["callee:00c5af10:8"]]
- 00bb8eec bytes 09870294
- 00bb8ef4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f38:8"]]
- 00bb8ef4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8ef4 bytes 609e07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f21108229e99fbe9440266f08a62baab"></a>

### [`00bb8fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8fdc.md) → [`00bb9404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9404.md) _ZN8firebase9messaging26illegal_argument_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb9034"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb945c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb901c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb9418",
      "READ",
      [
        "storage",
        "01125f40",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bb9010",
      "READ",
      [
        "storage",
        "01125f38",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bb9034",
      "WRITE",
      [
        "storage",
        "01125f40",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb9418",
      "READ",
      [
        "storage",
        "01126340",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9438",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb945c",
      "WRITE",
      [
        "storage",
        "01126340",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb901c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8fdc.md#insn-00bb901c) · [`00bb9034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8fdc.md#insn-00bb9034)
- 新版 [`00bb9444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9404.md#insn-00bb9444)

~~~diff
- 00bb901c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb901c ["INT_ADD", "register:40f0:8", ["const:bb901c:8", "const:4:8"]]
- 00bb901c ["CALLIND", null, ["register:0:8"]]
- 00bb901c bytes 00013fd6
- 00bb9034 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bb9034 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:f40:8"]]
- 00bb9034 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bb9034 bytes a0023d39
+ 00bb9444 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb9444 ["INT_ADD", "register:40f0:8", ["const:bb9444:8", "const:4:8"]]
+ 00bb9444 ["CALLIND", null, ["register:0:8"]]
+ 00bb9444 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53e35c96649619957180feae3fd37ba6"></a>

### [`00bb9048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9048.md) → [`00bb9470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9470.md) _ZN8firebase9messaging26illegal_argument_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.29% / 新版 64.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb9084"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb90a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb94ac"
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
      "00bb9484",
      "READ",
      [
        "storage",
        "01125f38",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bb9060",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb94d0"
      ]
    ],
    [
      "00bb9490",
      "READ",
      [
        "storage",
        "01125f40",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb9484",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9488",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb94d0"
      ]
    ],
    [
      "00bb9490",
      "READ",
      [
        "storage",
        "01126340",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9048.md#insn-00bb9060) · [`00bb9084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9048.md#insn-00bb9084) · [`00bb908c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9048.md#insn-00bb908c)

~~~diff
- 00bb9060 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bb9060 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00bb9060 bytes 410200b4
- 00bb9084 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bb9084 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bb9084 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:f40:8"]]
- 00bb9084 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bb9084 bytes bf023d39
- 00bb908c ["INT_ADD", "register:40f0:8", ["const:bb908c:8", "const:4:8"]]
- 00bb908c ["CALL", null, ["callee:00c5af60:8"]]
- 00bb908c bytes b5860294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df2d8a64149b09705f28ebedca697de1"></a>

### [`00bbcf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcf70.md) → [`00bbd398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd398.md) FUN_00bbd398

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbab28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbab28.md) · 呼出先 4件 [`00bbcd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcd98.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5cfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cfb0.md)
- 新版 呼出元 1件 [`00bbaf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbaf50.md) · 呼出先 4件 [`00bbd1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd1c0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5d3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 54.55% / 新版 46.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbcf9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bbd3c4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbcf88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbd3a8",
      "READ",
      [
        "storage",
        "01125f70",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bbcf88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbd3d4"
      ]
    ],
    [
      "unmatched:00bbcf9c",
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
      "00bbd3a8",
      "READ",
      [
        "storage",
        "01126370",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd3b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbd3d4"
      ]
    ],
    [
      "00bbd3c4",
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

- 旧版 [`00bbcf88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcf70.md#insn-00bbcf88) · [`00bbcf9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcf70.md#insn-00bbcf9c)
- 新版 [`00bbd3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd398.md#insn-00bbd3b0)

~~~diff
- 00bbcf88 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00bbcf88 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bbcf88 bytes 340100b4
- 00bbcf9c ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bbcf9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:8:8"]]
- 00bbcf9c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bbcf9c bytes 09210039
+ 00bbd3b0 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00bbd3b0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bbd3b0 bytes 340100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-703d8488d11f58ea0c026b26e745e1a7"></a>

### [`00bbd038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd038.md) → [`00bbd460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd460.md) FUN_00bbd460

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bbb274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb274.md) [`00bbb818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb818.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9a0.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)
- 新版 呼出元 2件 [`00bbb69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb69c.md) [`00bbbc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbc40.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ada0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd03c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd040"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd040"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbd03c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbd040",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbd044",
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
      "00bbd464",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bbd468",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bbd46c",
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

- 旧版 [`00bbd03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd038.md#insn-00bbd03c) · [`00bbd040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd038.md#insn-00bbd040) · [`00bbd044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd038.md#insn-00bbd044)

~~~diff
- 00bbd03c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00bbd03c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00bbd03c bytes f71300f9
- 00bbd040 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bbd040 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bbd040 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bbd040 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbd040 bytes f65703a9
- 00bbd044 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbd044 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbd044 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bbd044 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbd044 bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d87880d461b4594c30281f97ee492f14"></a>

### [`00bbe594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbe/00bbe594.md) → [`00bbe9bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbe/00bbe9bc.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIN11flatbuffers14VectorIteratorIhhPKhjEEEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valu

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d170.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)
- 新版 呼出元 1件 [`00c5d570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d570.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.03% / 新版 98.03%

CFGの説明率　旧版 91.43% / 新版 91.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbe600"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbe724"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bbea28"
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
      "unmatched:00bbe724",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbeb38"
      ]
    ]
  ],
  "added": [
    [
      "00bbeb4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbeb38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbe600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbe/00bbe594.md#insn-00bbe600) · [`00bbe724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbe/00bbe594.md#insn-00bbe724)
- 新版 [`00bbea28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbe/00bbe9bc.md#insn-00bbea28)

~~~diff
- 00bbe600 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bbe600 ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 00bbe600 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bbe600 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00bbe600 bytes d632889a
- 00bbe724 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bbe724 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
- 00bbe724 bytes 61ffff54
+ 00bbea28 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00bbea28 ["COPY", "tmp:1:8", ["register:40b0:8"]]
+ 00bbea28 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00bbea28 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00bbea28 bytes d632889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fefcc007cee7a3596602cc8c592f930d"></a>

### [`00bbe7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbe/00bbe7f4.md) → [`00bbec1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbe/00bbec1c.md) _ZNK3com6google8firebase9messaging3cpp15SerializedEvent6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d0d0.md) · 呼出先 4件 [`00c5d0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d0e0.md) [`00c5d100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d100.md) [`00c5d110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d110.md) [`00c5d120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d120.md)
- 新版 呼出元 1件 [`00c5d4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d4d0.md) · 呼出先 4件 [`00c5d4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d4e0.md) [`00c5d500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d500.md) [`00c5d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d510.md) [`00c5d520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d520.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 83.91% / 新版 80.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbe810"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbe860"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bbec38"
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
      "unmatched:00bbe810",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbec44"
      ]
    ],
    [
      "unmatched:00bbe860",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbecfc"
      ]
    ],
    [
      "unmatched:00bbe988",
      "DATA",
      [
        "storage",
        "0030e864",
        "switchD_00bbe990::switchdataD_0030e864",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00bbec38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbec44"
      ]
    ],
    [
      "00bbec88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbecfc"
      ]
    ],
    [
      "00bbedb0",
      "DATA",
      [
        "storage",
        "0030e8a4",
        "switchD_00bbedb8::switchdataD_0030e8a4",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbe810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbe/00bbe7f4.md#insn-00bbe810) · [`00bbe860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbe/00bbe7f4.md#insn-00bbe860)
- 新版 [`00bbec38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbe/00bbec1c.md#insn-00bbec38)

~~~diff
- 00bbe810 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00bbe810 bytes 60000054
- 00bbe860 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bbe860 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bbe860 ["CBRANCH", null, ["local:b17:8", "tmp:1:1"]]
- 00bbe860 bytes a8030054
+ 00bbec38 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00bbec38 bytes 60000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2648e19b94c43a9387d6305503aab0aa"></a>

### [`00bbea04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbe/00bbea04.md) → [`00bbee2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbe/00bbee2c.md) _ZNK3com6google8firebase9messaging3cpp17SerializedMessage6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d0e0.md) · 呼出先 2件 [`00c5d0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d0f0.md) [`00c5d130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d130.md)
- 新版 呼出元 1件 [`00c5d4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d4e0.md) · 呼出先 2件 [`00c5d4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d4f0.md) [`00c5d530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d530.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 55.72% / 新版 55.72%

CFGの説明率　旧版 34.27% / 新版 34.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 123件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbea44"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbea70"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbeaf8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbea44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbfbac"
      ]
    ],
    [
      "unmatched:00bbea70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbfba8"
      ]
    ],
    [
      "00bbef14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bbeb08"
      ]
    ]
  ],
  "added": [
    [
      "00bbee6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbfbac"
      ]
    ],
    [
      "00bbee98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbfba8"
      ]
    ],
    [
      "00bbef14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbef30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbea44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbe/00bbea04.md#insn-00bbea44) · [`00bbea70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbe/00bbea04.md#insn-00bbea70) · [`00bbeaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbe/00bbea04.md#insn-00bbeaf8)

~~~diff
- 00bbea44 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bbea44 ["CBRANCH", null, ["local:b299:8", "tmp:0:1"]]
- 00bbea44 bytes 036a0054
- 00bbea70 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bbea70 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bbea70 ["CBRANCH", null, ["local:b298:8", "tmp:1:1"]]
- 00bbea70 bytes 88680054
- 00bbeaf8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4080:4", "const:0:4"]]
- 00bbeaf8 ["CBRANCH", null, ["local:b299:8", "tmp:0:1"]]
- 00bbeaf8 bytes 70640035
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33cf2ae66d4472d78cd9eb66d4f8924a"></a>

### [`00bbf7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbf/00bbf7ac.md) → [`00bbfbd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbf/00bbfbd4.md) _ZNK3com6google8firebase9messaging3cpp8DataPair6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d130.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5d530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d530.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.68% / 新版 95.68%

CFGの説明率　旧版 75.89% / 新版 74.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbf824"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbf874"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbf8b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbf824",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbfe44"
      ]
    ],
    [
      "unmatched:00bbf874",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbfcb8"
      ]
    ],
    [
      "unmatched:00bbf8b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbfe44"
      ]
    ]
  ],
  "added": [
    [
      "00bbfc4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbfe44"
      ]
    ],
    [
      "00bbfc9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbfcb8"
      ]
    ],
    [
      "00bbfcd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbfe44"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbf824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbf/00bbf7ac.md#insn-00bbf824) · [`00bbf874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbf/00bbf7ac.md#insn-00bbf874) · [`00bbf8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbf/00bbf7ac.md#insn-00bbf8b0)

~~~diff
- 00bbf824 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bbf824 ["CBRANCH", null, ["local:b59:8", "tmp:0:1"]]
- 00bbf824 bytes c30f0054
- 00bbf874 ["CBRANCH", null, ["local:b21:8", "register:101:1"]]
- 00bbf874 bytes e0000054
- 00bbf8b0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bbf8b0 ["CBRANCH", null, ["local:b59:8", "tmp:0:1"]]
- 00bbf8b0 bytes 630b0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93e11c80685cff46767a8d1a5722887d"></a>

### [`00bbfa34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbf/00bbfa34.md) → [`00bbfe5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbf/00bbfe5c.md) _ZNK3com6google8firebase9messaging3cpp22SerializedNotification6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d0f0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5d4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d4f0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 33.69% / 新版 33.69%

CFGの説明率　旧版 8.90% / 新版 9.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 183件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbfa88"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbfad0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbfb0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbfa88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc0b90"
      ]
    ],
    [
      "unmatched:00bbfad0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc0b94"
      ]
    ],
    [
      "00bbff1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bbfb40"
      ]
    ]
  ],
  "added": [
    [
      "00bbfeb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc0b90"
      ]
    ],
    [
      "00bbfef8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc0b94"
      ]
    ],
    [
      "00bbff1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbff68"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbfa88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbf/00bbfa34.md#insn-00bbfa88) · [`00bbfad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbf/00bbfa34.md#insn-00bbfad0) · [`00bbfb0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbf/00bbfa34.md#insn-00bbfb0c)

~~~diff
- 00bbfa88 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bbfa88 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bbfa88 ["CBRANCH", null, ["local:b339:8", "tmp:1:1"]]
- 00bbfa88 bytes 08670054
- 00bbfad0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bbfad0 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bbfad0 ["CBRANCH", null, ["local:b340:8", "tmp:1:1"]]
- 00bbfad0 bytes e9640054
- 00bbfb0c ["INT_NOTEQUAL", "tmp:0:1", ["register:4088:4", "const:0:4"]]
- 00bbfb0c ["CBRANCH", null, ["local:b340:8", "tmp:0:1"]]
- 00bbfb0c bytes 11630035
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83c1a7bc2671361f2a661bc2c2b8283e"></a>

### [`00bc0784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0784.md) → [`00bc0bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc0/00bc0bac.md) _ZNK3com6google8firebase9messaging3cpp23SerializedTokenReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d100.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5d500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d500.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 59.72% / 新版 62.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc07d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc0860"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc08c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc07d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc0d3c"
      ]
    ],
    [
      "unmatched:00bc0860",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc0c98"
      ]
    ],
    [
      "unmatched:00bc08c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc0cf8"
      ]
    ]
  ],
  "added": [
    [
      "00bc0bfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc0d3c"
      ]
    ],
    [
      "00bc0c88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc0c98"
      ]
    ],
    [
      "00bc0ce8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc0cf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc07d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0784.md#insn-00bc07d4) · [`00bc0860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0784.md#insn-00bc0860) · [`00bc08c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc0/00bc0784.md#insn-00bc08c0)

~~~diff
- 00bc07d4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc07d4 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bc07d4 ["CBRANCH", null, ["local:b38:8", "tmp:1:1"]]
- 00bc07d4 bytes 080a0054
- 00bc0860 ["CBRANCH", null, ["local:b24:8", "register:102:1"]]
- 00bc0860 bytes 82000054
- 00bc08c0 ["CBRANCH", null, ["local:b33:8", "register:102:1"]]
- 00bc08c0 bytes 82000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e00a47f9f9e9da765e3aac89e960ba3c"></a>

### [`00bc1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1b78.md) → [`00bc1fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1fa0.md) _ZN8firebase13remote_config8internal12config_value15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1bd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc1ff8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1bb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc1fb4",
      "READ",
      [
        "storage",
        "01126128",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bc1bac",
      "READ",
      [
        "storage",
        "01126120",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc1bd0",
      "WRITE",
      [
        "storage",
        "01126128",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc1fb4",
      "READ",
      [
        "storage",
        "01126528",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1fd4",
      "READ",
      [
        "storage",
        "01126520",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1ff8",
      "WRITE",
      [
        "storage",
        "01126528",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1b78.md#insn-00bc1bb8) · [`00bc1bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1b78.md#insn-00bc1bd0)
- 新版 [`00bc1fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1fa0.md#insn-00bc1fe0)

~~~diff
- 00bc1bb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc1bb8 ["INT_ADD", "register:40f0:8", ["const:bc1bb8:8", "const:4:8"]]
- 00bc1bb8 ["CALLIND", null, ["register:0:8"]]
- 00bc1bb8 bytes 00013fd6
- 00bc1bd0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bc1bd0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:128:8"]]
- 00bc1bd0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc1bd0 bytes a0a20439
+ 00bc1fe0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc1fe0 ["INT_ADD", "register:40f0:8", ["const:bc1fe0:8", "const:4:8"]]
+ 00bc1fe0 ["CALLIND", null, ["register:0:8"]]
+ 00bc1fe0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf2075752d69caa434db2deb94f3574a"></a>

### [`00bc1cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1cc4.md) → [`00bc20ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc20ec.md) _ZN8firebase13remote_config8internal12config_value11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1cc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1cc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1cc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc1cc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc1cc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc1cd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc1ce8"
      ]
    ]
  ],
  "added": [
    [
      "00bc20ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc20f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc2100",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2110"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1cc4.md#insn-00bc1cc4) · [`00bc1cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1cc4.md#insn-00bc1cc8) · [`00bc1cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1cc4.md#insn-00bc1cd8)

~~~diff
- 00bc1cc4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc1cc4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc1cc4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc1cc4 bytes f30f1ef8
- 00bc1cc8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc1cc8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc1cc8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc1cc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc1cc8 bytes fd7b01a9
- 00bc1cd8 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bc1cd8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc1cd8 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97adc65ffdb0afba65de85774e0e007b"></a>

### [`00bc1d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1d70.md) → [`00bc2198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2198.md) _ZN8firebase13remote_config8internal12config_value10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1d90"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bc21b8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1da8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc21ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc1d94"
      ]
    ],
    [
      "unmatched:00bc1d8c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bc1d90",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bc21ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc21bc"
      ]
    ],
    [
      "00bc21b4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bc21b8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1d70.md#insn-00bc1d90) · [`00bc1da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1d70.md#insn-00bc1da8)
- 新版 [`00bc21b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2198.md#insn-00bc21b8)

~~~diff
- 00bc1d90 ["INT_ADD", "register:40f0:8", ["const:bc1d90:8", "const:4:8"]]
- 00bc1d90 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc1d90 bytes 9c630294
- 00bc1da8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc1da8 ["RETURN", null, ["register:0:8"]]
- 00bc1da8 bytes c0035fd6
+ 00bc21b8 ["INT_ADD", "register:40f0:8", ["const:bc21b8:8", "const:4:8"]]
+ 00bc21b8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc21b8 bytes 92630294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-129994976365ef6b927f289ffe140ccc"></a>

### [`00bc1eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1eb4.md) → [`00bc22dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc22dc.md) _ZN8firebase13remote_config8internal11config_info8GetClassEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1ebc"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bc22e4"
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
      "unmatched:00bc1eb8",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc22e0",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1eb4.md#insn-00bc1ebc) · [`00bc1eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1eb4.md#insn-00bc1eb4)
- 新版 [`00bc22e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc22dc.md#insn-00bc22e4)

~~~diff
- 00bc1ebc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc1ebc ["RETURN", null, ["register:0:8"]]
- 00bc1ebc bytes c0035fd6
+ 00bc22e4 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bc22e4 ["RETURN", null, ["register:0:8"]]
+ 00bc22e4 bytes c0035fd6
- 00bc1eb4 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bc1eb4 bytes 282b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85d00c2f0ab780c8fa823a6c71b30faf"></a>

### [`00bc20b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc20b8.md) → [`00bc24e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc24e0.md) _ZN8firebase13remote_config8internal11config_info10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.67% / 新版 26.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc20b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc20bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc20bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc20b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc20bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc24f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc20dc"
      ]
    ]
  ],
  "added": [
    [
      "00bc24e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc24e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc24f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2504"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc20b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc20b8.md#insn-00bc20b8) · [`00bc20bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc20b8.md#insn-00bc20bc) · [`00bc20d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc20b8.md#insn-00bc20d8)

~~~diff
- 00bc20b8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc20b8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc20b8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc20b8 bytes f30f1ef8
- 00bc20bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc20bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc20bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc20bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc20bc bytes fd7b01a9
- 00bc20d8 ["INT_ADD", "register:40f0:8", ["const:bc20d8:8", "const:4:8"]]
- 00bc20d8 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc20d8 bytes ca620294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a12ae1abcd932e68f5f826329eb9e63e"></a>

### [`00bc269c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc269c.md) → [`00bc2ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2ac4.md) _ZN8firebase13remote_config8internal23config_settings_builder11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.67% / 新版 26.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc269c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc26a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc26a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc269c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc26a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc2ad8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc26c0"
      ]
    ]
  ],
  "added": [
    [
      "00bc2ac4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc2ac8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc2ad8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2ae8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc269c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc269c.md#insn-00bc269c) · [`00bc26a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc269c.md#insn-00bc26a0) · [`00bc26bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc269c.md#insn-00bc26bc)

~~~diff
- 00bc269c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc269c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc269c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc269c bytes f30f1ef8
- 00bc26a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc26a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc26a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc26a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc26a0 bytes fd7b01a9
- 00bc26bc ["INT_ADD", "register:40f0:8", ["const:bc26bc:8", "const:4:8"]]
- 00bc26bc ["CALL", null, ["callee:00c5b000:8"]]
- 00bc26bc bytes 51610294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dc3c2b3efe80a765269eef531b81d8f"></a>

### [`00bc2748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2748.md) → [`00bc2b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2b70.md) _ZN8firebase13remote_config8internal23config_settings_builder10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 33.33% / 新版 33.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc275c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bc2b84"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2768"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc275c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc276c"
      ]
    ],
    [
      "unmatched:00bc2764",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bc2768",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bc2b84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2b94"
      ]
    ],
    [
      "00bc2b8c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bc2b90",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc275c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2748.md#insn-00bc275c) · [`00bc2768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2748.md#insn-00bc2768) · [`00bc2780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2748.md#insn-00bc2780)

~~~diff
- 00bc275c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bc275c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc275c bytes 8b000054
- 00bc2768 ["INT_ADD", "register:40f0:8", ["const:bc2768:8", "const:4:8"]]
- 00bc2768 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc2768 bytes 26610294
- 00bc2780 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc2780 ["RETURN", null, ["register:0:8"]]
- 00bc2780 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-719315f1b7d47649acf6e826159e614e"></a>

### [`00bc288c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc288c.md) → [`00bc2cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2cb4.md) _ZN8firebase13remote_config8internal22custom_signals_builder8GetClassEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2894"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bc2cbc"
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
      "unmatched:00bc2890",
      "READ",
      [
        "storage",
        "011261f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2cb8",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc288c.md#insn-00bc2894) · [`00bc288c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc288c.md#insn-00bc288c)
- 新版 [`00bc2cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2cb4.md#insn-00bc2cbc)

~~~diff
- 00bc2894 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc2894 ["RETURN", null, ["register:0:8"]]
- 00bc2894 bytes c0035fd6
+ 00bc2cbc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bc2cbc ["RETURN", null, ["register:0:8"]]
+ 00bc2cbc bytes c0035fd6
- 00bc288c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bc288c bytes 282b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6861a2865cbc7e4d9f50e4ad23f2a722"></a>

### [`00bc2d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2d2c.md) → [`00bc3154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3154.md) _ZN8firebase13remote_config8internal19throttled_exception11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2d2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2d30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2d30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc2d2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc2d30",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc2d40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc2d50"
      ]
    ]
  ],
  "added": [
    [
      "00bc3154",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc3158",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc3168",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3178"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2d2c.md#insn-00bc2d2c) · [`00bc2d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2d2c.md#insn-00bc2d30) · [`00bc2d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2d2c.md#insn-00bc2d40)

~~~diff
- 00bc2d2c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc2d2c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc2d2c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc2d2c bytes f30f1ef8
- 00bc2d30 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc2d30 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc2d30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc2d30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc2d30 bytes fd7b01a9
- 00bc2d40 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bc2d40 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00bc2d40 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b62cdd25058655f51cf491648b28154"></a>

### [`00bc2f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2f28.md) → [`00bc3350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3350.md) _ZN8firebase13remote_config8internal26jni_config_update_listener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2f80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc33a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2f68"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc3364",
      "READ",
      [
        "storage",
        "01126260",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bc2f5c",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc2f80",
      "WRITE",
      [
        "storage",
        "01126260",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc3364",
      "READ",
      [
        "storage",
        "01126660",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc3384",
      "READ",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc33a8",
      "WRITE",
      [
        "storage",
        "01126660",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2f28.md#insn-00bc2f68) · [`00bc2f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2f28.md#insn-00bc2f80)
- 新版 [`00bc3390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3350.md#insn-00bc3390)

~~~diff
- 00bc2f68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc2f68 ["INT_ADD", "register:40f0:8", ["const:bc2f68:8", "const:4:8"]]
- 00bc2f68 ["CALLIND", null, ["register:0:8"]]
- 00bc2f68 bytes 00013fd6
- 00bc2f80 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bc2f80 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:260:8"]]
- 00bc2f80 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc2f80 bytes a0820939
+ 00bc3390 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc3390 ["INT_ADD", "register:40f0:8", ["const:bc3390:8", "const:4:8"]]
+ 00bc3390 ["CALLIND", null, ["register:0:8"]]
+ 00bc3390 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-445e3edb2be63bad308b2b69de5874f7"></a>

### [`00bc3074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3074.md) → [`00bc349c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc349c.md) _ZN8firebase13remote_config8internal26jni_config_update_listener11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3094"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bc34bc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc30ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc34b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc3098"
      ]
    ],
    [
      "unmatched:00bc3090",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bc3094",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bc34b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc34c0"
      ]
    ],
    [
      "00bc34b8",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bc34bc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3074.md#insn-00bc3094) · [`00bc30ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3074.md#insn-00bc30ac)
- 新版 [`00bc34bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc349c.md#insn-00bc34bc)

~~~diff
- 00bc3094 ["INT_ADD", "register:40f0:8", ["const:bc3094:8", "const:4:8"]]
- 00bc3094 ["CALL", null, ["callee:00c5b000:8"]]
- 00bc3094 bytes db5e0294
- 00bc30ac ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc30ac ["RETURN", null, ["register:0:8"]]
- 00bc30ac bytes c0035fd6
+ 00bc34bc ["INT_ADD", "register:40f0:8", ["const:bc34bc:8", "const:4:8"]]
+ 00bc34bc ["CALL", null, ["callee:00c5b000:8"]]
+ 00bc34bc bytes d15e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dbe6ae396a1a4867132653557e4ae72"></a>

### [`00bc3624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3624.md) → [`00bc3a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3a4c.md) _ZN8firebase13remote_config8internal35config_update_listener_registration12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.29% / 新版 64.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3660"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3680"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc3a88"
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
      "00bc3a60",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc363c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3aac"
      ]
    ],
    [
      "00bc3a6c",
      "READ",
      [
        "storage",
        "011262a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc3a60",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3a64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3aac"
      ]
    ],
    [
      "00bc3a6c",
      "READ",
      [
        "storage",
        "011266a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc363c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3624.md#insn-00bc363c) · [`00bc3660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3624.md#insn-00bc3660) · [`00bc3668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc3/00bc3624.md#insn-00bc3668)

~~~diff
- 00bc363c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc363c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bc363c bytes 410200b4
- 00bc3660 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc3660 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc3660 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:2a0:8"]]
- 00bc3660 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc3660 bytes bf820a39
- 00bc3668 ["INT_ADD", "register:40f0:8", ["const:bc3668:8", "const:4:8"]]
- 00bc3668 ["CALL", null, ["callee:00c5af60:8"]]
- 00bc3668 bytes 3e5d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3426b3460d40c9883cc171728433e516"></a>

### [`00bc45a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc45a4.md) → [`00bc49cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc49cc.md) _ZN8firebase13remote_config8internal20RemoteConfigInternalD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d480.md) · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6a0.md) [`00c5a830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a830.md) [`00c5a850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a850.md) [`00c5ab00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab00.md)
- 新版 呼出元 1件 [`00c5d880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d880.md) · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aaa0.md) [`00c5ac30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac30.md) [`00c5ac50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac50.md) [`00c5af00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 94.29% / 新版 89.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc45a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc45a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc45a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc45a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc45a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc45ac",
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
      "00bc49cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bc49d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc49d4",
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

- 旧版 [`00bc45a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc45a4.md#insn-00bc45a4) · [`00bc45a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc45a4.md#insn-00bc45a8) · [`00bc45ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc45a4.md#insn-00bc45ac)

~~~diff
- 00bc45a4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bc45a4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bc45a4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bc45a4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc45a4 bytes f657bda9
- 00bc45a8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc45a8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc45a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc45a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc45a8 bytes f44f01a9
- 00bc45ac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc45ac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc45ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bc45ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc45ac bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38278e437799a237c2768cf5e398543a"></a>

### [`00bc4cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4cf8.md) → [`00bc5120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5120.md) _ZN8firebase13remote_config8internal18BoolResultCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bc55d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc55d8.md) [`00bc5904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc5/00bc5904.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5aee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aee0.md)
- 新版 呼出元 2件 [`00bc5a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5a00.md) [`00bc5d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5d2c.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) [`00c5b2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b2e0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 82.61% / 新版 90.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc4d2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc5154"
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
      "unmatched:00bc4d2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc5154",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4cf8.md#insn-00bc4d2c) · [`00bc4d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc4cf8.md#insn-00bc4d30)
- 新版 [`00bc5154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5120.md#insn-00bc5154) · [`00bc5158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc5120.md#insn-00bc5158)

~~~diff
- 00bc4d2c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00bc4d2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bc4d2c bytes e80f00f9
+ 00bc5154 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
+ 00bc5154 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00bc5154 bytes e80f00f9
- 00bc4d30 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc4d30 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bc5158 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bc5158 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc4d30 bytes 810000b4
+ 00bc5158 bytes 810000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8c1acbdaaf97dbdf46365373f6eab1e"></a>

### [`00bc9900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9900.md) → [`00bc9d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9d28.md) _ZN8firebase6FutureINS_13remote_config10ConfigInfoEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d510.md) · 呼出先 3件 [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9f0.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)
- 新版 呼出元 1件 [`00c5d910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d910.md) · 呼出先 3件 [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5adf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5adf0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9978"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bc9da0"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9900.md#insn-00bc9978) · [`00bc9920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9900.md#insn-00bc9920)
- 新版 [`00bc9da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9d28.md#insn-00bc9da0) · [`00bc9d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9d28.md#insn-00bc9d48)

~~~diff
- 00bc9978 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc9978 ["RETURN", null, ["register:0:8"]]
- 00bc9978 bytes c0035fd6
+ 00bc9da0 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bc9da0 ["RETURN", null, ["register:0:8"]]
+ 00bc9da0 bytes c0035fd6
- 00bc9920 ["INT_ADD", "register:40f0:8", ["const:bc9920:8", "const:4:8"]]
- 00bc9920 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00bc9d48 ["INT_ADD", "register:40f0:8", ["const:bc9d48:8", "const:4:8"]]
+ 00bc9d48 ["CALL", null, ["callee:00c5ac70:8"]]
- 00bc9920 bytes d4430294
+ 00bc9d48 bytes ca430294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bdb3a23fc6f765bbd84e66395a55a5c"></a>

### [`00bc9b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9b90.md) → [`00bc9fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9fb8.md) FUN_00bc9fb8

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
      "site": "00bc9b98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9ba0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc9fc0"
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
      "unmatched:00bc9b98",
      "DATA",
      [
        "storage",
        "00c91428",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc9fc0",
      "DATA",
      [
        "storage",
        "00c91828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9b90.md#insn-00bc9b98) · [`00bc9ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9b90.md#insn-00bc9ba0) · [`00bc9ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9b90.md#insn-00bc9ba4)

~~~diff
- 00bc9b98 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00bc9b98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bc9b98 bytes 280000f9
- 00bc9ba0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 00bc9ba0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bc9ba0 bytes 280400f9
- 00bc9ba4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc9ba4 ["RETURN", null, ["register:0:8"]]
- 00bc9ba4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0dd4db5ce92bb00a60ae54ffbccf788"></a>

### [`00bc9c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9c90.md) → [`00bca0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca0b8.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationC1ERKS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bc9f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9f38.md) [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bca360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca360.md) [`00c5ac00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 73.33% / 新版 73.33%

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
      "site": "00bc9c9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bca0c4"
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
      "unmatched:00bc9c94",
      "READ",
      [
        "storage",
        "00c9b528",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bc9c9c",
      "DATA",
      [
        "storage",
        "00c914a8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00bca0dc",
      "READ",
      [
        "storage",
        "00c9b520",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bca0bc",
      "READ",
      [
        "storage",
        "00c9b928",
        null,
        "pointer"
      ]
    ],
    [
      "00bca0c4",
      "DATA",
      [
        "storage",
        "00c918a8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00bca0dc",
      "READ",
      [
        "storage",
        "00c9b920",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9c90.md#insn-00bc9c9c) · [`00bc9c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9c90.md#insn-00bc9c90)
- 新版 [`00bca0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca0b8.md#insn-00bca0c4)

~~~diff
- 00bc9c9c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00bc9c9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc9c9c bytes 090000f9
+ 00bca0c4 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00bca0c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00bca0c4 bytes 090000f9
- 00bc9c90 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00bc9c90 bytes 890600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-240a2158049cce82b0d406767d9161f0"></a>

### [`00bc9ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9ccc.md) → [`00bca0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca0f4.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationC1EOS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc9f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9f38.md) [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md) [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bca360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca360.md) [`00c5ac00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac00.md) [`00c5ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 20.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9ccc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9ccc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9cd0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc9ccc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc9cd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bca104",
      "READ",
      [
        "storage",
        "00c9b528",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bca0f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bca0f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bca104",
      "READ",
      [
        "storage",
        "00c9b928",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9ccc.md#insn-00bc9ccc) · [`00bc9cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc9/00bc9ccc.md#insn-00bc9cd0)
- 新版 [`00bca0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca0f4.md#insn-00bca0f4)

~~~diff
- 00bc9ccc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc9ccc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc9ccc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc9ccc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc9ccc bytes f44fbea9
- 00bc9cd0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc9cd0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc9cd0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc9cd0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc9cd0 bytes fd7b01a9
+ 00bca0f4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00bca0f4 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00bca0f4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00bca0f4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00bca0f4 bytes f44fbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6542648df5e1589180e99fd515447d3"></a>

### [`00bca038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca038.md) → [`00bca460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca460.md) _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternal6RemoveEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d270.md) · 呼出先 1件 [`00b60d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60d04.md)
- 新版 呼出元 1件 [`00c5d670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d670.md) · 呼出先 1件 [`00b6112c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b6112c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 60.00% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bca04c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bca474"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bca04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca038.md#insn-00bca04c) · [`00bca044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca038.md#insn-00bca044)
- 新版 [`00bca474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca460.md#insn-00bca474) · [`00bca46c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca460.md#insn-00bca46c)

~~~diff
- 00bca04c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bca04c ["RETURN", null, ["register:0:8"]]
- 00bca04c bytes c0035fd6
+ 00bca474 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bca474 ["RETURN", null, ["register:0:8"]]
+ 00bca474 bytes c0035fd6
- 00bca044 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00bca044 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bca46c ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00bca46c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bca044 bytes 68000034
+ 00bca46c bytes 68000034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef2551f47c204698318a9892909c5340"></a>

### [`00bcadb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcadb4.md) → [`00bcb1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb1dc.md) _ZN8firebase4auth4Auth23RemoveAuthStateListenerEPNS0_17AuthStateListenerE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d670.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00c5da70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da70.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 80.88% / 新版 80.88%

CFGの説明率　旧版 58.82% / 新版 54.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcae1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcae80"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcae88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcae1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb22c"
      ]
    ],
    [
      "00bcb284",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcae84"
      ]
    ],
    [
      "unmatched:00bcae80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb290"
      ]
    ]
  ],
  "added": [
    [
      "00bcb244",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb22c"
      ]
    ],
    [
      "00bcb284",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb2ac"
      ]
    ],
    [
      "00bcb294",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb2d4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcae1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcadb4.md#insn-00bcae1c) · [`00bcae80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcadb4.md#insn-00bcae80) · [`00bcae88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bcadb4.md#insn-00bcae88)

~~~diff
- 00bcae1c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bcae1c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bcae1c bytes 41ffff54
- 00bcae80 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bcae80 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00bcae80 bytes 41ffff54
- 00bcae88 ["CBRANCH", null, ["local:b20:8", "register:101:1"]]
- 00bcae88 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15de64eec2a7ecd157f0bfcfabba1d9a"></a>

### [`00bcb024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb024.md) → [`00bcb44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb44c.md) _ZN8firebase4auth17AuthStateListenerD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5d670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d670.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5da70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da70.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 71.43% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb044"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcb46c"
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
      "00bcb45c",
      "READ",
      [
        "storage",
        "00c9b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bcb044",
      "DATA",
      [
        "storage",
        "00c914d8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bcb45c",
      "READ",
      [
        "storage",
        "00c9b9b8",
        null,
        "pointer"
      ]
    ],
    [
      "00bcb46c",
      "DATA",
      [
        "storage",
        "00c918d8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb024.md#insn-00bcb044) · [`00bcb034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb024.md#insn-00bcb034)
- 新版 [`00bcb46c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb44c.md#insn-00bcb46c) · [`00bcb45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb44c.md#insn-00bcb45c)

~~~diff
- 00bcb044 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bcb044 ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 00bcb044 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:8:8"]]
- 00bcb044 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bcb044 bytes 888600f8
+ 00bcb46c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00bcb46c ["COPY", "tmp:1:8", ["register:40a0:8"]]
+ 00bcb46c ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:8:8"]]
+ 00bcb46c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00bcb46c bytes 888600f8
- 00bcb034 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b8:8"]]
- 00bcb034 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bcb45c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
+ 00bcb45c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bcb034 bytes 08dd42f9
+ 00bcb45c bytes 08dd44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-392370851c95fc431b893c2b3073f705"></a>

### [`00bcb294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb294.md) → [`00bcb6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb6bc.md) _ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEEC2ERKS7_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d700.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)
- 新版 呼出元 1件 [`00c5db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db00.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 75.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb294"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb294"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb298"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcb294",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcb298",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcb29c",
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
      "00bcb6bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcb6c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcb6c4",
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

- 旧版 [`00bcb294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb294.md#insn-00bcb294) · [`00bcb298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb294.md#insn-00bcb298) · [`00bcb29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb294.md#insn-00bcb29c)

~~~diff
- 00bcb294 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bcb294 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bcb294 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bcb294 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcb294 bytes f657bda9
- 00bcb298 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcb298 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcb298 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcb298 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcb298 bytes f44f01a9
- 00bcb29c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcb29c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcb29c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bcb29c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcb29c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58aa23f7d6c68eedebcc45def7e7add3"></a>

### [`00bcb69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb69c.md) → [`00bcbac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbac4.md) _ZNK8firebase4auth4Auth31SignInWithCustomTokenLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb69c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb6a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb6a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcb69c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcb6a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcb6a4",
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
      "00bcbac4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcbac8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcbacc",
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

- 旧版 [`00bcb69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb69c.md#insn-00bcb69c) · [`00bcb6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb69c.md#insn-00bcb6a0) · [`00bcb6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb69c.md#insn-00bcb6a4)

~~~diff
- 00bcb69c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bcb69c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bcb69c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcb69c bytes f50f1df8
- 00bcb6a0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcb6a0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcb6a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcb6a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcb6a0 bytes f44f01a9
- 00bcb6a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcb6a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcb6a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bcb6a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcb6a4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa3cf34f7e02ac859d2ecc75e212582d"></a>

### [`00bcb72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb72c.md) → [`00bcbb54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbb54.md) _ZNK8firebase4auth4Auth45SignInAndRetrieveDataWithCredentialLastResultEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.46% / 新版 88.46%

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
      "site": "00bcb734"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb734"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcbb5c"
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
      "unmatched:00bcb734",
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
      "00bcbb5c",
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

- 旧版 [`00bcb734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb72c.md#insn-00bcb734) · [`00bcb738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb72c.md#insn-00bcb738)
- 新版 [`00bcbb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbb54.md#insn-00bcbb5c)

~~~diff
- 00bcb734 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcb734 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcb734 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bcb734 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcb734 bytes fd7b02a9
+ 00bcbb5c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00bcbb5c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00bcbb5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
+ 00bcbb5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00bcbb5c bytes fd7b02a9
- 00bcb738 ["COPY", "tmp:0:8", ["const:20:8"]]
- 00bcb738 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 00bcb738 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 00bcb738 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 00bcb738 bytes fd830091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-580f8f899a512b1f9e7ad742af5480ef"></a>

### [`00bcbd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbd8c.md) → [`00bcc1b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc1b4.md) _ZN8firebase4auth23GetCredentialFutureImplEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d750.md) · 呼出先 1件 [`00c5b930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b930.md)
- 新版 呼出元 1件 [`00c5db50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db50.md) · 呼出先 1件 [`00c5bd30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcbd90",
      "PARAM",
      [
        "storage",
        "0030f023",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcbd98",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5bd30"
      ]
    ]
  ],
  "added": [
    [
      "00bcc1b8",
      "PARAM",
      [
        "storage",
        "0030f063",
        null,
        "string"
      ]
    ],
    [
      "00bcc1c0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5bd30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbd8c.md#insn-00bcbd8c) · [`00bcbd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbd8c.md#insn-00bcbd90) · [`00bcbd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbd8c.md#insn-00bcbd94)

~~~diff
- 00bcbd8c ["COPY", "register:4000:8", ["const:30f000:8"]]
- 00bcbd8c bytes 20baff90
- 00bcbd90 ["COPY", "tmp:0:8", ["const:23:8"]]
- 00bcbd90 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bcbd90 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bcbd90 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bcbd90 bytes 008c0091
- 00bcbd94 ["COPY", "register:4008:8", ["const:1:8"]]
- 00bcbd94 bytes 21008052
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-207226477963315e245fc9408f853520"></a>

### [`00bcbda8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbda8.md) → [`00bcc1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc1d0.md) _ZN8firebase4auth14ClearUserInfosEPNS0_8AuthDataE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d5a0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5d9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d9a0.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 77.78% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbe1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bcc244"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbe1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbda8.md#insn-00bcbe1c) · [`00bcbe04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbda8.md#insn-00bcbe04)
- 新版 [`00bcc244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc1d0.md#insn-00bcc244) · [`00bcc22c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc1d0.md#insn-00bcc22c)

~~~diff
- 00bcbe1c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bcbe1c ["RETURN", null, ["register:0:8"]]
- 00bcbe1c bytes c0035fd6
+ 00bcc244 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bcc244 ["RETURN", null, ["register:0:8"]]
+ 00bcc244 bytes c0035fd6
- 00bcbe04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbe04 ["INT_ADD", "register:40f0:8", ["const:bcbe04:8", "const:4:8"]]
- 00bcbe04 ["CALLIND", null, ["register:0:8"]]
+ 00bcc22c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcc22c ["INT_ADD", "register:40f0:8", ["const:bcc22c:8", "const:4:8"]]
+ 00bcc22c ["CALLIND", null, ["register:0:8"]]
- 00bcbe04 bytes 00013fd6
+ 00bcc22c bytes 00013fd6
~~~


<a id="compare-5786a905d53a9c121ba3f7eadf29f795"></a>

### [`00bcbfec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbfec.md) → [`00bcc414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc414.md) _ZN8firebase4auth4auth8GetClassEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00bcbff4"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bcc41c"
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
      "unmatched:00bcbff0",
      "READ",
      [
        "storage",
        "01126328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc418",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbfec.md#insn-00bcbff4) · [`00bcbfec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbfec.md#insn-00bcbfec)
- 新版 [`00bcc41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc414.md#insn-00bcc41c)

~~~diff
- 00bcbff4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bcbff4 ["RETURN", null, ["register:0:8"]]
- 00bcbff4 bytes c0035fd6
+ 00bcc41c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bcc41c ["RETURN", null, ["register:0:8"]]
+ 00bcc41c bytes c0035fd6
- 00bcbfec ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bcbfec bytes c82a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-622635b85b78bb58c27f985458245806"></a>

### [`00bcc1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc1f0.md) → [`00bcc618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc618.md) _ZN8firebase4auth4auth10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc210"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bcc638"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc228"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcc62c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcc214"
      ]
    ],
    [
      "unmatched:00bcc20c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcc210",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bcc62c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc63c"
      ]
    ],
    [
      "00bcc634",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bcc638",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc1f0.md#insn-00bcc210) · [`00bcc228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc1f0.md#insn-00bcc228)
- 新版 [`00bcc638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc618.md#insn-00bcc638)

~~~diff
- 00bcc210 ["INT_ADD", "register:40f0:8", ["const:bcc210:8", "const:4:8"]]
- 00bcc210 ["CALL", null, ["callee:00c5b000:8"]]
- 00bcc210 bytes 7c3a0294
- 00bcc228 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bcc228 ["RETURN", null, ["register:0:8"]]
- 00bcc228 bytes c0035fd6
+ 00bcc638 ["INT_ADD", "register:40f0:8", ["const:bcc638:8", "const:4:8"]]
+ 00bcc638 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bcc638 bytes 723a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c91d6cc82eb871a9539943e6e66105b"></a>

### [`00bcc538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc538.md) → [`00bcc960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc960.md) _ZN8firebase4auth17signinmethodquery10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.67% / 新版 26.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc538"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc53c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc53c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc538",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc53c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bcc974",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcc55c"
      ]
    ]
  ],
  "added": [
    [
      "00bcc960",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcc964",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bcc974",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc984"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc538.md#insn-00bcc538) · [`00bcc53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc538.md#insn-00bcc53c) · [`00bcc558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc538.md#insn-00bcc558)

~~~diff
- 00bcc538 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bcc538 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bcc538 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcc538 bytes f30f1ef8
- 00bcc53c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcc53c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcc53c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcc53c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcc53c bytes fd7b01a9
- 00bcc558 ["INT_ADD", "register:40f0:8", ["const:bcc558:8", "const:4:8"]]
- 00bcc558 ["CALL", null, ["callee:00c5b000:8"]]
- 00bcc558 bytes aa390294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54d605213c16eb3c12ca11a848772338"></a>

### [`00bcc5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc5b4.md) → [`00bcc9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc9dc.md) _ZN8firebase4auth11jnilistener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc5b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc5b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc5b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc5b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc5b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc5c4",
      "READ",
      [
        "storage",
        "011263f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcc9dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcc9e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bcc9ec",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc5b4.md#insn-00bcc5b4) · [`00bcc5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc5b4.md#insn-00bcc5b8) · [`00bcc5c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc5b4.md#insn-00bcc5c8)

~~~diff
- 00bcc5b4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bcc5b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bcc5b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcc5b4 bytes f30f1ef8
- 00bcc5b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcc5b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcc5b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcc5b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcc5b8 bytes fd7b01a9
- 00bcc5c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcc5c8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bcc5c8 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f898c60c92fca50b7187c14582ee65b3"></a>

### [`00bcc688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc688.md) → [`00bccab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccab0.md) _ZN8firebase4auth11jnilistener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 20.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc688"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc68c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc68c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc688",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc68c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc690",
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
      "00bccab0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bccab4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bccab8",
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

- 旧版 [`00bcc688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc688.md#insn-00bcc688) · [`00bcc68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc688.md#insn-00bcc68c) · [`00bcc690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc688.md#insn-00bcc690)

~~~diff
- 00bcc688 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bcc688 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bcc688 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcc688 bytes f50f1df8
- 00bcc68c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcc68c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcc68c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcc68c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcc68c bytes f44f01a9
- 00bcc690 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcc690 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcc690 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bcc690 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcc690 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd583bd2b3cdd95ccfeb4e94f236c043"></a>

### [`00bcc7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc7d4.md) → [`00bccbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccbfc.md) _ZN8firebase4auth11jnilistener11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc7f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bccc1c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc80c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bccc10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcc7f8"
      ]
    ],
    [
      "unmatched:00bcc7f0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcc7f4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bccc10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccc20"
      ]
    ],
    [
      "00bccc18",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bccc1c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc7d4.md#insn-00bcc7f4) · [`00bcc80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc7d4.md#insn-00bcc80c)
- 新版 [`00bccc1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccbfc.md#insn-00bccc1c)

~~~diff
- 00bcc7f4 ["INT_ADD", "register:40f0:8", ["const:bcc7f4:8", "const:4:8"]]
- 00bcc7f4 ["CALL", null, ["callee:00c5b000:8"]]
- 00bcc7f4 bytes 03390294
- 00bcc80c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bcc80c ["RETURN", null, ["register:0:8"]]
- 00bcc80c bytes c0035fd6
+ 00bccc1c ["INT_ADD", "register:40f0:8", ["const:bccc1c:8", "const:4:8"]]
+ 00bccc1c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bccc1c bytes f9380294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a99300c0b029e3b56509746f96f8b3c7"></a>

### [`00bcc8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc8fc.md) → [`00bccd24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccd24.md) _ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc928"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bccd50"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc910"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc90c",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcc910",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccd54"
      ]
    ],
    [
      "unmatched:00bcc918",
      "PARAM",
      [
        "storage",
        "002aa8bd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bccd34",
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccd38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccd54"
      ]
    ],
    [
      "00bccd40",
      "PARAM",
      [
        "storage",
        "002aa98a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc8fc.md#insn-00bcc910) · [`00bcc920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc8fc.md#insn-00bcc920) · [`00bcc928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc8fc.md#insn-00bcc928)

~~~diff
- 00bcc910 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcc910 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bcc910 bytes e80000b5
- 00bcc920 ["INT_ADD", "register:40f0:8", ["const:bcc920:8", "const:4:8"]]
- 00bcc920 ["CALL", null, ["callee:00c5af10:8"]]
- 00bcc920 bytes 7c380294
- 00bcc928 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
- 00bcc928 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc928 bytes 600e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d2d7f60777d2c314830aed7044c80d6"></a>

### [`00bccb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccb1c.md) → [`00bccf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccf44.md) _ZN8firebase4auth21jni_id_token_listener11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccb3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bccf64"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccb54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bccf58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bccb40"
      ]
    ],
    [
      "unmatched:00bccb38",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bccb3c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bccf58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccf68"
      ]
    ],
    [
      "00bccf60",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bccf64",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bccb3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccb1c.md#insn-00bccb3c) · [`00bccb54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccb1c.md#insn-00bccb54)
- 新版 [`00bccf64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccf44.md#insn-00bccf64)

~~~diff
- 00bccb3c ["INT_ADD", "register:40f0:8", ["const:bccb3c:8", "const:4:8"]]
- 00bccb3c ["CALL", null, ["callee:00c5b000:8"]]
- 00bccb3c bytes 31380294
- 00bccb54 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bccb54 ["RETURN", null, ["register:0:8"]]
- 00bccb54 bytes c0035fd6
+ 00bccf64 ["INT_ADD", "register:40f0:8", ["const:bccf64:8", "const:4:8"]]
+ 00bccf64 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bccf64 bytes 27380294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-faebaaeef1ac854c3b332d3051b23ee6"></a>

### [`00bccbc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccbc8.md) → [`00bccff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccff0.md) _ZN8firebase4auth21jni_id_token_listener10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.67% / 新版 26.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccbc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccbcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccbcc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bccbc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bccbcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bcd004",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bccbec"
      ]
    ]
  ],
  "added": [
    [
      "00bccff0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bccff4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bcd004",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcd014"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bccbc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccbc8.md#insn-00bccbc8) · [`00bccbcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccbc8.md#insn-00bccbcc) · [`00bccbe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccbc8.md#insn-00bccbe8)

~~~diff
- 00bccbc8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bccbc8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bccbc8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bccbc8 bytes f30f1ef8
- 00bccbcc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bccbcc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bccbcc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bccbcc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bccbcc bytes fd7b01a9
- 00bccbe8 ["INT_ADD", "register:40f0:8", ["const:bccbe8:8", "const:4:8"]]
- 00bccbe8 ["CALL", null, ["callee:00c5b000:8"]]
- 00bccbe8 bytes 06380294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a12601809318ad7a9f133a3f4b0172f"></a>

### [`00bcf478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf478.md) → [`00bcf8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf8a0.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4Auth20FetchProvidersResultEEEvPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bcd788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd788.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00bcdbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdbb0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 55.56% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcf494"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bcf8bc"
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
      "unmatched:00bcf494",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcf910"
      ]
    ]
  ],
  "added": [
    [
      "00bcf8bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcf910"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf478.md#insn-00bcf494) · [`00bcf478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf478.md#insn-00bcf478)
- 新版 [`00bcf8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf8a0.md#insn-00bcf8bc) · [`00bcf8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf8a0.md#insn-00bcf8a0)

~~~diff
- 00bcf494 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00bcf494 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00bcf494 bytes b40200b4
+ 00bcf8bc ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00bcf8bc ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00bcf8bc bytes b40200b4
- 00bcf478 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bcf478 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00bcf8a0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00bcf8a0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00bcf478 bytes c00200b4
+ 00bcf8a0 bytes c00200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-408e0d0610d1e8cda238cdac8df91873"></a>

### [`00bd0504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0504.md) → [`00bd092c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd092c.md) _ZN8firebase4auth10authresult11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0524"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd094c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd053c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd0940",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd0528"
      ]
    ],
    [
      "unmatched:00bd0520",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd0524",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd0940",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0950"
      ]
    ],
    [
      "00bd0948",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd094c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0504.md#insn-00bd0524) · [`00bd053c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0504.md#insn-00bd053c)
- 新版 [`00bd094c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd092c.md#insn-00bd094c)

~~~diff
- 00bd0524 ["INT_ADD", "register:40f0:8", ["const:bd0524:8", "const:4:8"]]
- 00bd0524 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd0524 bytes b7290294
- 00bd053c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd053c ["RETURN", null, ["register:0:8"]]
- 00bd053c bytes c0035fd6
+ 00bd094c ["INT_ADD", "register:40f0:8", ["const:bd094c:8", "const:4:8"]]
+ 00bd094c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd094c bytes ad290294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2719aa268165b586df02d2dd5cdf1790"></a>

### [`00bd05b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd05b0.md) → [`00bd09d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd09d8.md) _ZN8firebase4auth10authresult10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd05d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd09f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd05e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd09ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd05d4"
      ]
    ],
    [
      "unmatched:00bd05cc",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd05d0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd09ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd09fc"
      ]
    ],
    [
      "00bd09f4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd09f8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd05d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd05b0.md#insn-00bd05d0) · [`00bd05e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd05b0.md#insn-00bd05e8)
- 新版 [`00bd09f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd09d8.md#insn-00bd09f8)

~~~diff
- 00bd05d0 ["INT_ADD", "register:40f0:8", ["const:bd05d0:8", "const:4:8"]]
- 00bd05d0 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd05d0 bytes 8c290294
- 00bd05e8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd05e8 ["RETURN", null, ["register:0:8"]]
- 00bd05e8 bytes c0035fd6
+ 00bd09f8 ["INT_ADD", "register:40f0:8", ["const:bd09f8:8", "const:4:8"]]
+ 00bd09f8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd09f8 bytes 82290294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a96227282223ef6149503574dcaf5b7c"></a>

### [`00bd09b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd09b4.md) → [`00bd0ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0ddc.md) _ZN8firebase4auth27api_not_available_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 23.53% / 新版 23.53%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd09b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd09b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd09b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd09b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd09b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd09c4",
      "READ",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0ddc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd0de0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd0dec",
      "READ",
      [
        "storage",
        "011268a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd09b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd09b4.md#insn-00bd09b4) · [`00bd09b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd09b4.md#insn-00bd09b8) · [`00bd09c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd09b4.md#insn-00bd09c8)

~~~diff
- 00bd09b4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd09b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd09b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd09b4 bytes f30f1ef8
- 00bd09b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd09b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd09b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd09b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd09b8 bytes fd7b01a9
- 00bd09c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd09c8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd09c8 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-463dffc1b20cc9f88b3dbd2462a59ae2"></a>

### [`00bd0a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0a48.md) → [`00bd0e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0e70.md) _ZN8firebase4auth27api_not_available_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 25.00% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0a48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0a4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0a4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0a48",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd0a4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd0a50",
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
      "00bd0e70",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd0e74",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd0e78",
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

- 旧版 [`00bd0a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0a48.md#insn-00bd0a48) · [`00bd0a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0a48.md#insn-00bd0a4c) · [`00bd0a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0a48.md#insn-00bd0a50)

~~~diff
- 00bd0a48 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bd0a48 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd0a48 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd0a48 bytes f50f1df8
- 00bd0a4c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd0a4c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd0a4c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd0a4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd0a4c bytes f44f01a9
- 00bd0a50 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd0a50 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd0a50 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd0a50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd0a50 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6336da0d82313c77fd2c003bf5b1f253"></a>

### [`00bd0c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0c40.md) → [`00bd1068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1068.md) _ZN8firebase4auth27api_not_available_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0c60"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd1088"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0c78"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd107c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd0c64"
      ]
    ],
    [
      "unmatched:00bd0c5c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd0c60",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd107c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd108c"
      ]
    ],
    [
      "00bd1084",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd1088",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0c40.md#insn-00bd0c60) · [`00bd0c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0c40.md#insn-00bd0c78)
- 新版 [`00bd1088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1068.md#insn-00bd1088)

~~~diff
- 00bd0c60 ["INT_ADD", "register:40f0:8", ["const:bd0c60:8", "const:4:8"]]
- 00bd0c60 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd0c60 bytes e8270294
- 00bd0c78 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd0c78 ["RETURN", null, ["register:0:8"]]
- 00bd0c78 bytes c0035fd6
+ 00bd1088 ["INT_ADD", "register:40f0:8", ["const:bd1088:8", "const:4:8"]]
+ 00bd1088 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd1088 bytes de270294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-780e49760fcf61c2d8657c3f148ab569"></a>

### [`00bd0cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0cbc.md) → [`00bd10e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd10e4.md) _ZN8firebase4auth21action_code_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0ce8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1110"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0cd0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0ccc",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd0cd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1114"
      ]
    ],
    [
      "unmatched:00bd0cd8",
      "PARAM",
      [
        "storage",
        "002a4f33",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd10f4",
      "READ",
      [
        "storage",
        "011268c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd10f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1114"
      ]
    ],
    [
      "00bd1100",
      "PARAM",
      [
        "storage",
        "002a500f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0cbc.md#insn-00bd0cd0) · [`00bd0ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0cbc.md#insn-00bd0ce0) · [`00bd0ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0cbc.md#insn-00bd0ce8)

~~~diff
- 00bd0cd0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd0cd0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd0cd0 bytes e80000b5
- 00bd0ce0 ["INT_ADD", "register:40f0:8", ["const:bd0ce0:8", "const:4:8"]]
- 00bd0ce0 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd0ce0 bytes 8c270294
- 00bd0ce8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
- 00bd0ce8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd0ce8 bytes 606602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b82b68cd32af12505985a7a7ffad05be"></a>

### [`00bd0cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0cfc.md) → [`00bd1124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1124.md) _ZN8firebase4auth21action_code_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0d2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1154"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0d10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0d0c",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd0d10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1158"
      ]
    ],
    [
      "unmatched:00bd0d1c",
      "PARAM",
      [
        "storage",
        "002a4f33",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd1134",
      "READ",
      [
        "storage",
        "011268c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1138",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1158"
      ]
    ],
    [
      "00bd1144",
      "PARAM",
      [
        "storage",
        "002a500f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0cfc.md#insn-00bd0d10) · [`00bd0d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0cfc.md#insn-00bd0d24) · [`00bd0d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0cfc.md#insn-00bd0d2c)

~~~diff
- 00bd0d10 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd0d10 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd0d10 bytes 080100b5
- 00bd0d24 ["INT_ADD", "register:40f0:8", ["const:bd0d24:8", "const:4:8"]]
- 00bd0d24 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd0d24 bytes 7b270294
- 00bd0d2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
- 00bd0d2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd0d2c bytes 606602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a09c850d34be8feef7e243d926dda15c"></a>

### [`00bd0d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0d90.md) → [`00bd11b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd11b8.md) _ZN8firebase4auth21action_code_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call, call_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0de8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1210"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0dd0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd11cc",
      "READ",
      [
        "storage",
        "011264d0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bd0dc4",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd0de8",
      "WRITE",
      [
        "storage",
        "011264d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd11cc",
      "READ",
      [
        "storage",
        "011268d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd11ec",
      "READ",
      [
        "storage",
        "011268c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1210",
      "WRITE",
      [
        "storage",
        "011268d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0d90.md#insn-00bd0dd0) · [`00bd0de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0d90.md#insn-00bd0de8)
- 新版 [`00bd11f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd11b8.md#insn-00bd11f8)

~~~diff
- 00bd0dd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0dd0 ["INT_ADD", "register:40f0:8", ["const:bd0dd0:8", "const:4:8"]]
- 00bd0dd0 ["CALLIND", null, ["register:0:8"]]
- 00bd0dd0 bytes 00013fd6
- 00bd0de8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd0de8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4d0:8"]]
- 00bd0de8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd0de8 bytes a0421339
+ 00bd11f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd11f8 ["INT_ADD", "register:40f0:8", ["const:bd11f8:8", "const:4:8"]]
+ 00bd11f8 ["CALLIND", null, ["register:0:8"]]
+ 00bd11f8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ea2a88f48e9b3e574ce5da8b573e949"></a>

### [`00bd0edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0edc.md) → [`00bd1304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1304.md) _ZN8firebase4auth21action_code_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0efc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd1324"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0f14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd1318",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd0f00"
      ]
    ],
    [
      "unmatched:00bd0ef8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd0efc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd1318",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1328"
      ]
    ],
    [
      "00bd1320",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd1324",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0edc.md#insn-00bd0efc) · [`00bd0f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0edc.md#insn-00bd0f14)
- 新版 [`00bd1324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1304.md#insn-00bd1324)

~~~diff
- 00bd0efc ["INT_ADD", "register:40f0:8", ["const:bd0efc:8", "const:4:8"]]
- 00bd0efc ["CALL", null, ["callee:00c5b000:8"]]
- 00bd0efc bytes 41270294
- 00bd0f14 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd0f14 ["RETURN", null, ["register:0:8"]]
- 00bd0f14 bytes c0035fd6
+ 00bd1324 ["INT_ADD", "register:40f0:8", ["const:bd1324:8", "const:4:8"]]
+ 00bd1324 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd1324 bytes 37270294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8ce4c15221d30e9507d3a249e7a7321"></a>

### [`00bd0f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0f88.md) → [`00bd13b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd13b0.md) _ZN8firebase4auth21action_code_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0f88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0f8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0f8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0f88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd0f8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd0f9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd0fac"
      ]
    ]
  ],
  "added": [
    [
      "00bd13b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd13b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd13c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd13d4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0f88.md#insn-00bd0f88) · [`00bd0f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0f88.md#insn-00bd0f8c) · [`00bd0f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0f88.md#insn-00bd0f9c)

~~~diff
- 00bd0f88 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd0f88 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd0f88 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd0f88 bytes f30f1ef8
- 00bd0f8c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd0f8c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd0f8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd0f8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd0f8c bytes fd7b01a9
- 00bd0f9c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd0f9c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd0f9c bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-465bdfe6c32aa6ecdd38ce102240419a"></a>

### [`00bd1004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1004.md) → [`00bd142c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd142c.md) _ZN8firebase4auth15email_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1030"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1458"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1018"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd1014",
      "READ",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd1018",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd145c"
      ]
    ],
    [
      "unmatched:00bd1020",
      "PARAM",
      [
        "storage",
        "002a1bb7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd143c",
      "READ",
      [
        "storage",
        "011268e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1440",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd145c"
      ]
    ],
    [
      "00bd1448",
      "PARAM",
      [
        "storage",
        "002a1c84",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1004.md#insn-00bd1018) · [`00bd1028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1004.md#insn-00bd1028) · [`00bd1030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1004.md#insn-00bd1030)

~~~diff
- 00bd1018 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd1018 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd1018 bytes e80000b5
- 00bd1028 ["INT_ADD", "register:40f0:8", ["const:bd1028:8", "const:4:8"]]
- 00bd1028 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1028 bytes ba260294
- 00bd1030 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
- 00bd1030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1030 bytes 607602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a699dbcef6372e974f9cbe3f2ff6be23"></a>

### [`00bd12d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd12d0.md) → [`00bd16f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd16f8.md) _ZN8firebase4auth15email_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 33.33% / 新版 33.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd12e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd170c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd12f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd12e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd12f4"
      ]
    ],
    [
      "unmatched:00bd12ec",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd12f0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd170c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd171c"
      ]
    ],
    [
      "00bd1714",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd1718",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd12e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd12d0.md#insn-00bd12e4) · [`00bd12f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd12d0.md#insn-00bd12f0) · [`00bd1308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd12d0.md#insn-00bd1308)

~~~diff
- 00bd12e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd12e4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd12e4 bytes 8b000054
- 00bd12f0 ["INT_ADD", "register:40f0:8", ["const:bd12f0:8", "const:4:8"]]
- 00bd12f0 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd12f0 bytes 44260294
- 00bd1308 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd1308 ["RETURN", null, ["register:0:8"]]
- 00bd1308 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1beb4303b85da8d43e82257467ebc310"></a>

### [`00bd138c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd138c.md) → [`00bd17b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd17b4.md) _ZN8firebase4auth23weak_password_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 23.53% / 新版 23.53%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd13bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd17e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd13a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd139c",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd13a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd13c0"
      ]
    ],
    [
      "unmatched:00bd13ac",
      "PARAM",
      [
        "storage",
        "002af52a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd17c4",
      "READ",
      [
        "storage",
        "01126908",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd17c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd17e8"
      ]
    ],
    [
      "00bd17d4",
      "PARAM",
      [
        "storage",
        "002af56a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd13a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd138c.md#insn-00bd13a0) · [`00bd13b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd138c.md#insn-00bd13b4) · [`00bd13bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd138c.md#insn-00bd13bc)

~~~diff
- 00bd13a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd13a0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd13a0 bytes 080100b5
- 00bd13b4 ["INT_ADD", "register:40f0:8", ["const:bd13b4:8", "const:4:8"]]
- 00bd13b4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd13b4 bytes d7250294
- 00bd13bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00bd13bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd13bc bytes 608602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d20d92b06e45599b5520392d7d9a047"></a>

### [`00bd1960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1960.md) → [`00bd1d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1d88.md) _ZN8firebase4auth29invalid_credentials_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 33.33% / 新版 33.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1974"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd1d9c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1980"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd1974",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd1984"
      ]
    ],
    [
      "unmatched:00bd197c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd1980",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd1d9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1dac"
      ]
    ],
    [
      "00bd1da4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd1da8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1960.md#insn-00bd1974) · [`00bd1980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1960.md#insn-00bd1980) · [`00bd1998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1960.md#insn-00bd1998)

~~~diff
- 00bd1974 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd1974 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd1974 bytes 8b000054
- 00bd1980 ["INT_ADD", "register:40f0:8", ["const:bd1980:8", "const:4:8"]]
- 00bd1980 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd1980 bytes a0240294
- 00bd1998 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd1998 ["RETURN", null, ["register:0:8"]]
- 00bd1998 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb08f60f54dc4283ebac1970e8862a85"></a>

### [`00bd1aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1aa4.md) → [`00bd1ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1ecc.md) _ZN8firebase4auth22invalid_user_exception8GetClassEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00bd1aac"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bd1ed4"
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
      "unmatched:00bd1aa8",
      "READ",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1ed0",
      "READ",
      [
        "storage",
        "01126948",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1aa4.md#insn-00bd1aac) · [`00bd1aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1aa4.md#insn-00bd1aa4)
- 新版 [`00bd1ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1ecc.md#insn-00bd1ed4)

~~~diff
- 00bd1aac ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd1aac ["RETURN", null, ["register:0:8"]]
- 00bd1aac bytes c0035fd6
+ 00bd1ed4 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bd1ed4 ["RETURN", null, ["register:0:8"]]
+ 00bd1ed4 bytes c0035fd6
- 00bd1aa4 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd1aa4 bytes a82a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a81872c3b9fddf7860a139d73cd5ee8"></a>

### [`00bd1ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ca8.md) → [`00bd20d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd20d0.md) _ZN8firebase4auth22invalid_user_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1cc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd20f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1ce0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd20e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd1ccc"
      ]
    ],
    [
      "unmatched:00bd1cc4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd1cc8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd20e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd20f4"
      ]
    ],
    [
      "00bd20ec",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd20f0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ca8.md#insn-00bd1cc8) · [`00bd1ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ca8.md#insn-00bd1ce0)
- 新版 [`00bd20f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd20d0.md#insn-00bd20f0)

~~~diff
- 00bd1cc8 ["INT_ADD", "register:40f0:8", ["const:bd1cc8:8", "const:4:8"]]
- 00bd1cc8 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd1cc8 bytes ce230294
- 00bd1ce0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd1ce0 ["RETURN", null, ["register:0:8"]]
- 00bd1ce0 bytes c0035fd6
+ 00bd20f0 ["INT_ADD", "register:40f0:8", ["const:bd20f0:8", "const:4:8"]]
+ 00bd20f0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd20f0 bytes c4230294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f57513f5cb95a5c109c4947587fc6b37"></a>

### [`00bd1d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1d24.md) → [`00bd214c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd214c.md) _ZN8firebase4auth31recent_login_required_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1d50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd2178"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1d38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd1d34",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd1d38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd217c"
      ]
    ],
    [
      "unmatched:00bd1d40",
      "PARAM",
      [
        "storage",
        "002bc100",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd215c",
      "READ",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2160",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd217c"
      ]
    ],
    [
      "00bd2168",
      "PARAM",
      [
        "storage",
        "002bc140",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1d24.md#insn-00bd1d38) · [`00bd1d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1d24.md#insn-00bd1d48) · [`00bd1d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1d24.md#insn-00bd1d50)

~~~diff
- 00bd1d38 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd1d38 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd1d38 bytes e80000b5
- 00bd1d48 ["INT_ADD", "register:40f0:8", ["const:bd1d48:8", "const:4:8"]]
- 00bd1d48 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd1d48 bytes 72230294
- 00bd1d50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
- 00bd1d50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1d50 bytes 60b602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60eebd261a8bef8390adaed5d154aa23"></a>

### [`00bd1f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1f44.md) → [`00bd236c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd236c.md) _ZN8firebase4auth31recent_login_required_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 33.33% / 新版 33.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1f58"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd2380"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1f64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd1f58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd1f68"
      ]
    ],
    [
      "unmatched:00bd1f60",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd1f64",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd2380",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd2390"
      ]
    ],
    [
      "00bd2388",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd238c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1f44.md#insn-00bd1f58) · [`00bd1f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1f44.md#insn-00bd1f64) · [`00bd1f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1f44.md#insn-00bd1f7c)

~~~diff
- 00bd1f58 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd1f58 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd1f58 bytes 8b000054
- 00bd1f64 ["INT_ADD", "register:40f0:8", ["const:bd1f64:8", "const:4:8"]]
- 00bd1f64 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd1f64 bytes 27230294
- 00bd1f7c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd1f7c ["RETURN", null, ["register:0:8"]]
- 00bd1f7c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-012969ef6b88fe14bbbf760a04843d2f"></a>

### [`00bd20ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd20ac.md) → [`00bd24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd24d4.md) _ZN8firebase4auth24user_collision_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd20dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd2504"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd20c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd20bc",
      "READ",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd20c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd2508"
      ]
    ],
    [
      "unmatched:00bd20cc",
      "PARAM",
      [
        "storage",
        "002a2c2a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd24e4",
      "READ",
      [
        "storage",
        "01126988",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd24e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd2508"
      ]
    ],
    [
      "00bd24f4",
      "PARAM",
      [
        "storage",
        "002a2cf7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd20c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd20ac.md#insn-00bd20c0) · [`00bd20d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd20ac.md#insn-00bd20d4) · [`00bd20dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd20ac.md#insn-00bd20dc)

~~~diff
- 00bd20c0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd20c0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd20c0 bytes 080100b5
- 00bd20d4 ["INT_ADD", "register:40f0:8", ["const:bd20d4:8", "const:4:8"]]
- 00bd20d4 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd20d4 bytes 8f220294
- 00bd20dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:588:8"]]
- 00bd20dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd20dc bytes 60c602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

