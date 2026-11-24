# v16.0.0 → v16.0.1 · 命令位置の検査未完了 (8)

[一覧の目次](README.md)

<a id="compare-3859734472e86abdd493e4efc1df4ceb"></a>

### [`00b4566c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4566c.md) → [`00b45a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45a94.md) _ZN8firebase4util19cppthreaddispatcher19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocator

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 31.25% / 新版 31.25%

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
      "site": "00b4566c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45670"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45670"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4566c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45670",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4567c",
      "READ",
      [
        "storage",
        "011252b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45a94",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b45a98",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45aa4",
      "READ",
      [
        "storage",
        "011256b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4566c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4566c.md#insn-00b4566c) · [`00b45670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4566c.md#insn-00b45670) · [`00b45680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4566c.md#insn-00b45680)

~~~diff
- 00b4566c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4566c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4566c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4566c bytes f30f1ef8
- 00b45670 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b45670 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b45670 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b45670 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45670 bytes fd7b01a9
- 00b45680 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b45680 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b45680 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72599738189e3e2edb2ab80e3ace7d55"></a>

### [`00b45734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45734.md) → [`00b45b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45b5c.md) _ZN8firebase4util19cppthreaddispatcher8GetClassEv

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
      "site": "00b4573c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b45b64"
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
      "unmatched:00b45738",
      "READ",
      [
        "storage",
        "011252b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45b60",
      "READ",
      [
        "storage",
        "011256b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4573c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45734.md#insn-00b4573c) · [`00b45734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45734.md#insn-00b45734)
- 新版 [`00b45b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45b5c.md#insn-00b45b64)

~~~diff
- 00b4573c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4573c ["RETURN", null, ["register:0:8"]]
- 00b4573c bytes c0035fd6
+ 00b45b64 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b45b64 ["RETURN", null, ["register:0:8"]]
+ 00b45b64 bytes c0035fd6
- 00b45734 ["COPY", "register:4040:8", ["const:1125000:8"]]
- 00b45734 bytes 082f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db36a53f2e122a2ead53c3ed4f5520f7"></a>

### [`00b458ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b458ec.md) → [`00b45d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45d14.md) _ZN8firebase4util19cppthreaddispatcher11GetMethodIdENS1_6MethodE

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
      "site": "00b45900"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b45d28"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4590c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45900",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b45910"
      ]
    ],
    [
      "unmatched:00b45908",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4590c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b45d28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45d38"
      ]
    ],
    [
      "00b45d30",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b45d34",
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

- 旧版 [`00b45900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b458ec.md#insn-00b45900) · [`00b4590c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b458ec.md#insn-00b4590c) · [`00b45924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b458ec.md#insn-00b45924)

~~~diff
- 00b45900 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b45900 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b45900 bytes 8b000054
- 00b4590c ["INT_ADD", "register:40f0:8", ["const:b4590c:8", "const:4:8"]]
- 00b4590c ["CALL", null, ["callee:00c5b000:8"]]
- 00b4590c bytes bd540494
- 00b45924 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b45924 ["RETURN", null, ["register:0:8"]]
- 00b45924 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f1062ce4296dadae5b3be7b36b3bcd1"></a>

### [`00b45998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45998.md) → [`00b45dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45dc0.md) _ZN8firebase4util19cppthreaddispatcher10GetFieldIdENS1_5FieldE

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
      "site": "00b45998"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4599c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4599c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45998",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4599c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45dd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b459bc"
      ]
    ]
  ],
  "added": [
    [
      "00b45dc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b45dc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45dd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45de4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45998.md#insn-00b45998) · [`00b4599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45998.md#insn-00b4599c) · [`00b459b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45998.md#insn-00b459b8)

~~~diff
- 00b45998 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b45998 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b45998 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b45998 bytes f30f1ef8
- 00b4599c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4599c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4599c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4599c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4599c bytes fd7b01a9
- 00b459b8 ["INT_ADD", "register:40f0:8", ["const:b459b8:8", "const:4:8"]]
- 00b459b8 ["CALL", null, ["callee:00c5b000:8"]]
- 00b459b8 bytes 92540494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a79890f2c2bb7259c271395f851f03d"></a>

### [`00b459d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b459d4.md) → [`00b45dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45dfc.md) _ZN8firebase4util3log19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

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
      "site": "00b459d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b459d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b459d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b459d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b459d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b459e4",
      "READ",
      [
        "storage",
        "011252d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45dfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b45e00",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45e0c",
      "READ",
      [
        "storage",
        "011256d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b459d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b459d4.md#insn-00b459d4) · [`00b459d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b459d4.md#insn-00b459d8) · [`00b459e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b459d4.md#insn-00b459e8)

~~~diff
- 00b459d4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b459d4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b459d4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b459d4 bytes f30f1ef8
- 00b459d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b459d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b459d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b459d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b459d8 bytes fd7b01a9
- 00b459e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b459e8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b459e8 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-118c5040b4ff0b8249063c125861653b"></a>

### [`00b45a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45a14.md) → [`00b45e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45e3c.md) _ZN8firebase4util3log19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45a14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45a18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45a18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45a14",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45a18",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45a24",
      "READ",
      [
        "storage",
        "011252d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45e3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b45e40",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45e4c",
      "READ",
      [
        "storage",
        "011256d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45a14.md#insn-00b45a14) · [`00b45a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45a14.md#insn-00b45a18) · [`00b45a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45a14.md#insn-00b45a28)

~~~diff
- 00b45a14 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b45a14 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b45a14 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b45a14 bytes f30f1ef8
- 00b45a18 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b45a18 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b45a18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b45a18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45a18 bytes fd7b01a9
- 00b45a28 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b45a28 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b45a28 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3ae9fd43ae11dc451211346aa3e8b9c"></a>

### [`00b45a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45a54.md) → [`00b45e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45e7c.md) _ZN8firebase4util3log10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 5.88% / 新版 5.88%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45a54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45a58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45a58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45a54",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45a58",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45a64",
      "READ",
      [
        "storage",
        "011252d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45e7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b45e80",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45e8c",
      "READ",
      [
        "storage",
        "011256d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45a54.md#insn-00b45a54) · [`00b45a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45a54.md#insn-00b45a58) · [`00b45a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45a54.md#insn-00b45a7c)

~~~diff
- 00b45a54 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b45a54 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b45a54 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b45a54 bytes f30f1ef8
- 00b45a58 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b45a58 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b45a58 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b45a58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45a58 bytes fd7b01a9
- 00b45a7c ["INT_ADD", "register:40f0:8", ["const:b45a7c:8", "const:4:8"]]
- 00b45a7c ["CALL", null, ["callee:00c5af10:8"]]
- 00b45a7c bytes 25540494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-726147fd5b5675b4df79bc0c03750899"></a>

### [`00b45b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45b84.md) → [`00b45fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45fac.md) _ZN8firebase4util3log12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 52.50% / 新版 52.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45bc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45c10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45fe8"
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
      "unmatched:00b45b98",
      "READ",
      [
        "storage",
        "011252d8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b45b9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b45c14"
      ]
    ],
    [
      "00b45fcc",
      "READ",
      [
        "storage",
        "011252e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b45fc0",
      "READ",
      [
        "storage",
        "011256d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45fc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4603c"
      ]
    ],
    [
      "00b45fcc",
      "READ",
      [
        "storage",
        "011256e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45b84.md#insn-00b45b9c) · [`00b45bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45b84.md#insn-00b45bc0) · [`00b45bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45b84.md#insn-00b45bd0)

~~~diff
- 00b45b9c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b45b9c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b45b9c bytes c10300b4
- 00b45bc0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b45bc0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b45bc0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:2e0:8"]]
- 00b45bc0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b45bc0 bytes bf820b39
- 00b45bd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45bd0 ["INT_ADD", "register:40f0:8", ["const:b45bd0:8", "const:4:8"]]
- 00b45bd0 ["CALLIND", null, ["register:0:8"]]
- 00b45bd0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6e9dbbc52a283ed2ce03ce60018036b"></a>

### [`00b45c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45c94.md) → [`00b460bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b460bc.md) _ZN8firebase4util3log11GetMethodIdENS1_6MethodE

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
      "site": "00b45c94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45c98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45c98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45c94",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45c98",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45ca8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b45cb8"
      ]
    ]
  ],
  "added": [
    [
      "00b460bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b460c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b460d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b460e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45c94.md#insn-00b45c94) · [`00b45c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45c94.md#insn-00b45c98) · [`00b45ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45c94.md#insn-00b45ca8)

~~~diff
- 00b45c94 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b45c94 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b45c94 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b45c94 bytes f30f1ef8
- 00b45c98 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b45c98 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b45c98 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b45c98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45c98 bytes fd7b01a9
- 00b45ca8 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b45ca8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b45ca8 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f75b27ab38c46f7eef5ca2673b7ac9ee"></a>

### [`00b45d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45d40.md) → [`00b46168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46168.md) _ZN8firebase4util3log10GetFieldIdENS1_5FieldE

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
      "site": "00b45d40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45d44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45d44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45d40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45d44",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4617c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b45d64"
      ]
    ]
  ],
  "added": [
    [
      "00b46168",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4616c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4617c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4618c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45d40.md#insn-00b45d40) · [`00b45d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45d40.md#insn-00b45d44) · [`00b45d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45d40.md#insn-00b45d60)

~~~diff
- 00b45d40 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b45d40 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b45d40 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b45d40 bytes f30f1ef8
- 00b45d44 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b45d44 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b45d44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b45d44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45d44 bytes fd7b01a9
- 00b45d60 ["INT_ADD", "register:40f0:8", ["const:b45d60:8", "const:4:8"]]
- 00b45d60 ["CALL", null, ["callee:00c5b000:8"]]
- 00b45d60 bytes a8530494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28128ee1077ed23cc316be7d408bb9d3"></a>

### [`00b45dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45dfc.md) → [`00b46224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46224.md) _ZN8firebase4util10uribuilder10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 29.41% / 新版 29.41%

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
      "site": "00b45e2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46254"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45e10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46234",
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b45e10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b45e30"
      ]
    ],
    [
      "unmatched:00b45e1c",
      "PARAM",
      [
        "storage",
        "002af2cd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46234",
      "READ",
      [
        "storage",
        "011256f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46238",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46258"
      ]
    ],
    [
      "00b46244",
      "PARAM",
      [
        "storage",
        "002af30d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45dfc.md#insn-00b45e10) · [`00b45e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45dfc.md#insn-00b45e24) · [`00b45e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45dfc.md#insn-00b45e2c)

~~~diff
- 00b45e10 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b45e10 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b45e10 bytes 080100b5
- 00b45e24 ["INT_ADD", "register:40f0:8", ["const:b45e24:8", "const:4:8"]]
- 00b45e24 ["CALL", null, ["callee:00c5af10:8"]]
- 00b45e24 bytes 3b530494
- 00b45e2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
- 00b45e2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45e2c bytes 607e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08123dff46d13b63523b56069a7d183b"></a>

### [`00b4603c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4603c.md) → [`00b46464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46464.md) _ZN8firebase4util10uribuilder11GetMethodIdENS1_6MethodE

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
      "site": "00b4605c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b46484"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46074"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46478",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b46060"
      ]
    ],
    [
      "unmatched:00b46058",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4605c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b46478",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46488"
      ]
    ],
    [
      "00b46480",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b46484",
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

- 旧版 [`00b4605c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4603c.md#insn-00b4605c) · [`00b46074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4603c.md#insn-00b46074)
- 新版 [`00b46484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46464.md#insn-00b46484)

~~~diff
- 00b4605c ["INT_ADD", "register:40f0:8", ["const:b4605c:8", "const:4:8"]]
- 00b4605c ["CALL", null, ["callee:00c5b000:8"]]
- 00b4605c bytes e9520494
- 00b46074 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b46074 ["RETURN", null, ["register:0:8"]]
- 00b46074 bytes c0035fd6
+ 00b46484 ["INT_ADD", "register:40f0:8", ["const:b46484:8", "const:4:8"]]
+ 00b46484 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b46484 bytes df520494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dffbc2f70882fb45f48d268ec7a80b3"></a>

### [`00b460e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b460e8.md) → [`00b46510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46510.md) _ZN8firebase4util10uribuilder10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

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
      "site": "00b46108"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b46530"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46120"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46524",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4610c"
      ]
    ],
    [
      "unmatched:00b46104",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b46108",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b46524",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46534"
      ]
    ],
    [
      "00b4652c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b46530",
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

- 旧版 [`00b46108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b460e8.md#insn-00b46108) · [`00b46120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b460e8.md#insn-00b46120)
- 新版 [`00b46530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46510.md#insn-00b46530)

~~~diff
- 00b46108 ["INT_ADD", "register:40f0:8", ["const:b46108:8", "const:4:8"]]
- 00b46108 ["CALL", null, ["callee:00c5b000:8"]]
- 00b46108 bytes be520494
- 00b46120 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b46120 ["RETURN", null, ["register:0:8"]]
- 00b46120 bytes c0035fd6
+ 00b46530 ["INT_ADD", "register:40f0:8", ["const:b46530:8", "const:4:8"]]
+ 00b46530 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b46530 bytes b4520494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bc7128de7515d0878e1bc7020592474"></a>

### [`00b46490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46490.md) → [`00b468b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b468b8.md) _ZN8firebase4util3url10GetFieldIdENS1_5FieldE

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
      "site": "00b464b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b468d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b464c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b468cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b464b4"
      ]
    ],
    [
      "unmatched:00b464ac",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b464b0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b468cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b468dc"
      ]
    ],
    [
      "00b468d4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b468d8",
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

- 旧版 [`00b464b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46490.md#insn-00b464b0) · [`00b464c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46490.md#insn-00b464c8)
- 新版 [`00b468d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b468b8.md#insn-00b468d8)

~~~diff
- 00b464b0 ["INT_ADD", "register:40f0:8", ["const:b464b0:8", "const:4:8"]]
- 00b464b0 ["CALL", null, ["callee:00c5b000:8"]]
- 00b464b0 bytes d4510494
- 00b464c8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b464c8 ["RETURN", null, ["register:0:8"]]
- 00b464c8 bytes c0035fd6
+ 00b468d8 ["INT_ADD", "register:40f0:8", ["const:b468d8:8", "const:4:8"]]
+ 00b468d8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b468d8 bytes ca510494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13209b327cd2757ab88c1cf60810855f"></a>

### [`00b4678c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4678c.md) → [`00b46bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46bb4.md) _ZN8firebase4util18file_output_stream11GetMethodIdENS1_6MethodE

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
      "site": "00b467ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b46bd4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b467c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46bc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b467b0"
      ]
    ],
    [
      "unmatched:00b467a8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b467ac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b46bc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46bd8"
      ]
    ],
    [
      "00b46bd0",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b46bd4",
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

- 旧版 [`00b467ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4678c.md#insn-00b467ac) · [`00b467c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4678c.md#insn-00b467c4)
- 新版 [`00b46bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46bb4.md#insn-00b46bd4)

~~~diff
- 00b467ac ["INT_ADD", "register:40f0:8", ["const:b467ac:8", "const:4:8"]]
- 00b467ac ["CALL", null, ["callee:00c5b000:8"]]
- 00b467ac bytes 15510494
- 00b467c4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b467c4 ["RETURN", null, ["register:0:8"]]
- 00b467c4 bytes c0035fd6
+ 00b46bd4 ["INT_ADD", "register:40f0:8", ["const:b46bd4:8", "const:4:8"]]
+ 00b46bd4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b46bd4 bytes 0b510494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db7a1c8fabd44fb0e3b5bf30439f46fe"></a>

### [`00b46874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46874.md) → [`00b46c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46c9c.md) _ZN8firebase4util16dex_class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

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
      "site": "00b468a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46cc8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46888"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46cac",
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b46888",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46ccc"
      ]
    ],
    [
      "unmatched:00b46894",
      "PARAM",
      [
        "storage",
        "002b8a16",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46cac",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46cb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46ccc"
      ]
    ],
    [
      "00b46cbc",
      "PARAM",
      [
        "storage",
        "002b8a56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46874.md#insn-00b46888) · [`00b46898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46874.md#insn-00b46898) · [`00b468a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46874.md#insn-00b468a0)

~~~diff
- 00b46888 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b46888 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b46888 bytes e80000b5
- 00b46898 ["INT_ADD", "register:40f0:8", ["const:b46898:8", "const:4:8"]]
- 00b46898 ["CALL", null, ["callee:00c5af10:8"]]
- 00b46898 bytes 9e500494
- 00b468a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:380:8"]]
- 00b468a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b468a0 bytes 60c201f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a00c569ca03977a34995ea427da2635"></a>

### [`00b468f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b468f4.md) → [`00b46d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46d1c.md) _ZN8firebase4util16dex_class_loader10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 52.94% / 新版 52.94%

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
      "site": "00b46924"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46d4c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46908"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46d2c",
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b46908",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46d50"
      ]
    ],
    [
      "unmatched:00b46914",
      "PARAM",
      [
        "storage",
        "002b8a16",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46d2c",
      "READ",
      [
        "storage",
        "01125780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46d30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46d50"
      ]
    ],
    [
      "00b46d3c",
      "PARAM",
      [
        "storage",
        "002b8a56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b468f4.md#insn-00b46908) · [`00b4691c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b468f4.md#insn-00b4691c) · [`00b46924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b468f4.md#insn-00b46924)

~~~diff
- 00b46908 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b46908 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b46908 bytes 080100b5
- 00b4691c ["INT_ADD", "register:40f0:8", ["const:b4691c:8", "const:4:8"]]
- 00b4691c ["CALL", null, ["callee:00c5af10:8"]]
- 00b4691c bytes 7d500494
- 00b46924 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:380:8"]]
- 00b46924 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46924 bytes 60c201f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbaa328d7c49a5b06332ecfb1738736c"></a>

### [`00b46b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46b34.md) → [`00b46f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46f5c.md) _ZN8firebase4util16dex_class_loader11GetMethodIdENS1_6MethodE

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
      "site": "00b46b54"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b46f7c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46b6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46f70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b46b58"
      ]
    ],
    [
      "unmatched:00b46b50",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b46b54",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b46f70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46f80"
      ]
    ],
    [
      "00b46f78",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b46f7c",
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

- 旧版 [`00b46b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46b34.md#insn-00b46b54) · [`00b46b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46b34.md#insn-00b46b6c)
- 新版 [`00b46f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b46/00b46f5c.md#insn-00b46f7c)

~~~diff
- 00b46b54 ["INT_ADD", "register:40f0:8", ["const:b46b54:8", "const:4:8"]]
- 00b46b54 ["CALL", null, ["callee:00c5b000:8"]]
- 00b46b54 bytes 2b500494
- 00b46b6c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b46b6c ["RETURN", null, ["register:0:8"]]
- 00b46b6c bytes c0035fd6
+ 00b46f7c ["INT_ADD", "register:40f0:8", ["const:b46f7c:8", "const:4:8"]]
+ 00b46f7c ["CALL", null, ["callee:00c5b000:8"]]
+ 00b46f7c bytes 21500494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f5fc24d49be1ad18129d4be20429c4c"></a>

### [`00b479d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b479d4.md) → [`00b47dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47dfc.md) _ZN8firebase4util21asset_file_descriptor11GetMethodIdENS1_6MethodE

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
      "site": "00b479f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b47e1c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47a0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47e10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b479f8"
      ]
    ],
    [
      "unmatched:00b479f0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b479f4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b47e10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47e20"
      ]
    ],
    [
      "00b47e18",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b47e1c",
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

- 旧版 [`00b479f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b479d4.md#insn-00b479f4) · [`00b47a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b479d4.md#insn-00b47a0c)
- 新版 [`00b47e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47dfc.md#insn-00b47e1c)

~~~diff
- 00b479f4 ["INT_ADD", "register:40f0:8", ["const:b479f4:8", "const:4:8"]]
- 00b479f4 ["CALL", null, ["callee:00c5b000:8"]]
- 00b479f4 bytes 834c0494
- 00b47a0c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b47a0c ["RETURN", null, ["register:0:8"]]
- 00b47a0c bytes c0035fd6
+ 00b47e1c ["INT_ADD", "register:40f0:8", ["const:b47e1c:8", "const:4:8"]]
+ 00b47e1c ["CALL", null, ["callee:00c5b000:8"]]
+ 00b47e1c bytes 794c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0330a790c3a16f0b9ef61f9103217243"></a>

### [`00b47abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47abc.md) → [`00b47ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b47/00b47ee4.md) _ZN8firebase4util13boolean_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "site": "00b47ae8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47f10"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47ad0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b47acc",
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b47ad0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47f14"
      ]
    ],
    [
      "unmatched:00b47adc",
      "PARAM",
      [
        "storage",
        "002a832f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b47ef4",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47ef8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47f14"
      ]
    ],
    [
      "00b47f04",
      "PARAM",
      [
        "storage",
        "002a83fc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47abc.md#insn-00b47ad0) · [`00b47ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47abc.md#insn-00b47ae0) · [`00b47ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47abc.md#insn-00b47ae8)

~~~diff
- 00b47ad0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b47ad0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b47ad0 bytes e80000b5
- 00b47ae0 ["INT_ADD", "register:40f0:8", ["const:b47ae0:8", "const:4:8"]]
- 00b47ae0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b47ae0 bytes 0c4c0494
- 00b47ae8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00b47ae8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47ae8 bytes 604202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-447172fa6fd44db0bac9188677be79c2"></a>

### [`00b48124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48124.md) → [`00b4854c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4854c.md) _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab90.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af90.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

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
      "site": "00b48144"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b4856c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4815c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48560",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b48148"
      ]
    ],
    [
      "unmatched:00b48140",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b48144",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b48560",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48570"
      ]
    ],
    [
      "00b48568",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4856c",
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

- 旧版 [`00b48144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48124.md#insn-00b48144) · [`00b4815c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48124.md#insn-00b4815c)
- 新版 [`00b4856c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b4854c.md#insn-00b4856c)

~~~diff
- 00b48144 ["INT_ADD", "register:40f0:8", ["const:b48144:8", "const:4:8"]]
- 00b48144 ["CALL", null, ["callee:00c5b000:8"]]
- 00b48144 bytes af4a0494
- 00b4815c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4815c ["RETURN", null, ["register:0:8"]]
- 00b4815c bytes c0035fd6
+ 00b4856c ["INT_ADD", "register:40f0:8", ["const:b4856c:8", "const:4:8"]]
+ 00b4856c ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4856c bytes a54a0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c006a114f75facd17397dfd196148ac"></a>

### [`00b481d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b481d0.md) → [`00b485f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b485f8.md) _ZN8firebase4util6bundle10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

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
      "site": "00b481e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b4860c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b481f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b481e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b481f4"
      ]
    ],
    [
      "unmatched:00b481ec",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b481f0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b4860c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4861c"
      ]
    ],
    [
      "00b48614",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b48618",
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

- 旧版 [`00b481e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b481d0.md#insn-00b481e4) · [`00b481f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b481d0.md#insn-00b481f0) · [`00b48208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b481d0.md#insn-00b48208)

~~~diff
- 00b481e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b481e4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b481e4 bytes 8b000054
- 00b481f0 ["INT_ADD", "register:40f0:8", ["const:b481f0:8", "const:4:8"]]
- 00b481f0 ["CALL", null, ["callee:00c5b000:8"]]
- 00b481f0 bytes 844a0494
- 00b48208 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b48208 ["RETURN", null, ["register:0:8"]]
- 00b48208 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ba0cfe8d36f5757be5ef62cf00d35e7"></a>

### [`00b485b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b485b4.md) → [`00b489dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b489dc.md) _ZN8firebase4util15character_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

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
      "site": "00b485e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48a08"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b485c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b485c4",
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b485c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48a0c"
      ]
    ],
    [
      "unmatched:00b485d4",
      "PARAM",
      [
        "storage",
        "002bbdb9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b489ec",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b489f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48a0c"
      ]
    ],
    [
      "00b489fc",
      "PARAM",
      [
        "storage",
        "002bbdf9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b485c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b485b4.md#insn-00b485c8) · [`00b485d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b485b4.md#insn-00b485d8) · [`00b485e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b485b4.md#insn-00b485e0)

~~~diff
- 00b485c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b485c8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b485c8 bytes e80000b5
- 00b485d8 ["INT_ADD", "register:40f0:8", ["const:b485d8:8", "const:4:8"]]
- 00b485d8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b485d8 bytes 4e490494
- 00b485e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00b485e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b485e0 bytes 609a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8f4b314cc6d9ecbc3f9ff83acf4b9a2"></a>

### [`00b48874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48874.md) → [`00b48c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48c9c.md) _ZN8firebase4util15character_class11GetMethodIdENS1_6MethodE

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
      "site": "00b48894"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b48cbc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b488ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48cb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b48898"
      ]
    ],
    [
      "unmatched:00b48890",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b48894",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b48cb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48cc0"
      ]
    ],
    [
      "00b48cb8",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b48cbc",
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

- 旧版 [`00b48894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48874.md#insn-00b48894) · [`00b488ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48874.md#insn-00b488ac)
- 新版 [`00b48cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48c9c.md#insn-00b48cbc)

~~~diff
- 00b48894 ["INT_ADD", "register:40f0:8", ["const:b48894:8", "const:4:8"]]
- 00b48894 ["CALL", null, ["callee:00c5b000:8"]]
- 00b48894 bytes db480494
- 00b488ac ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b488ac ["RETURN", null, ["register:0:8"]]
- 00b488ac bytes c0035fd6
+ 00b48cbc ["INT_ADD", "register:40f0:8", ["const:b48cbc:8", "const:4:8"]]
+ 00b48cbc ["CALL", null, ["callee:00c5b000:8"]]
+ 00b48cbc bytes d1480494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cd9204f06fe50402de9055a7786a013"></a>

### [`00b48920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48920.md) → [`00b48d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48d48.md) _ZN8firebase4util15character_class10GetFieldIdENS1_5FieldE

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
      "site": "00b48940"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b48d68"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48958"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48d5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b48944"
      ]
    ],
    [
      "unmatched:00b4893c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b48940",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b48d5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48d6c"
      ]
    ],
    [
      "00b48d64",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b48d68",
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

- 旧版 [`00b48940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48920.md#insn-00b48940) · [`00b48958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48920.md#insn-00b48958)
- 新版 [`00b48d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48d48.md#insn-00b48d68)

~~~diff
- 00b48940 ["INT_ADD", "register:40f0:8", ["const:b48940:8", "const:4:8"]]
- 00b48940 ["CALL", null, ["callee:00c5b000:8"]]
- 00b48940 bytes b0480494
- 00b48958 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b48958 ["RETURN", null, ["register:0:8"]]
- 00b48958 bytes c0035fd6
+ 00b48d68 ["INT_ADD", "register:40f0:8", ["const:b48d68:8", "const:4:8"]]
+ 00b48d68 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b48d68 bytes a6480494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-753c575d8be8b5ddc90bb355eb147611"></a>

### [`00b4899c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4899c.md) → [`00b48dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b48/00b48dc4.md) _ZN8firebase4util11class_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 call, call_count, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 20.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4899c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b489a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b489a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4899c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b489a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b48dd4",
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48dc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b48dc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b48dd4",
      "READ",
      [
        "storage",
        "01125958",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4899c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4899c.md#insn-00b4899c) · [`00b489a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4899c.md#insn-00b489a0) · [`00b489c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4899c.md#insn-00b489c0)

~~~diff
- 00b4899c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4899c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4899c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4899c bytes f30f1ef8
- 00b489a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b489a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b489a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b489a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b489a0 bytes fd7b01a9
- 00b489c0 ["INT_ADD", "register:40f0:8", ["const:b489c0:8", "const:4:8"]]
- 00b489c0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b489c0 bytes 54480494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71c2825ec3db26ccf9657392d4bf49b8"></a>

### [`00b49070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49070.md) → [`00b49498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49498.md) _ZN8firebase4util16content_resolver10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

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
      "site": "00b49090"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b494b8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b490a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b494ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b49094"
      ]
    ],
    [
      "unmatched:00b4908c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b49090",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b494ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b494bc"
      ]
    ],
    [
      "00b494b4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b494b8",
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

- 旧版 [`00b49090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49070.md#insn-00b49090) · [`00b490a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49070.md#insn-00b490a8)
- 新版 [`00b494b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49498.md#insn-00b494b8)

~~~diff
- 00b49090 ["INT_ADD", "register:40f0:8", ["const:b49090:8", "const:4:8"]]
- 00b49090 ["CALL", null, ["callee:00c5b000:8"]]
- 00b49090 bytes dc460494
- 00b490a8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b490a8 ["RETURN", null, ["register:0:8"]]
- 00b490a8 bytes c0035fd6
+ 00b494b8 ["INT_ADD", "register:40f0:8", ["const:b494b8:8", "const:4:8"]]
+ 00b494b8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b494b8 bytes d2460494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e1fc03d4314200af9616631f7eae047"></a>

### [`00b49418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49418.md) → [`00b49840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49840.md) _ZN8firebase4util7context10GetFieldIdENS1_5FieldE

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
      "site": "00b49438"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b49860"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49450"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49854",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4943c"
      ]
    ],
    [
      "unmatched:00b49434",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b49438",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b49854",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49864"
      ]
    ],
    [
      "00b4985c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b49860",
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

- 旧版 [`00b49438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49418.md#insn-00b49438) · [`00b49450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49418.md#insn-00b49450)
- 新版 [`00b49860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49840.md#insn-00b49860)

~~~diff
- 00b49438 ["INT_ADD", "register:40f0:8", ["const:b49438:8", "const:4:8"]]
- 00b49438 ["CALL", null, ["callee:00c5b000:8"]]
- 00b49438 bytes f2450494
- 00b49450 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b49450 ["RETURN", null, ["register:0:8"]]
- 00b49450 bytes c0035fd6
+ 00b49860 ["INT_ADD", "register:40f0:8", ["const:b49860:8", "const:4:8"]]
+ 00b49860 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b49860 bytes e8450494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9e0dff0fa4a5c4239bcc087f5aff557"></a>

### [`00b497fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b497fc.md) → [`00b49c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49c24.md) _ZN8firebase4util4date19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b497fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49800"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49800"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b497fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b49800",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4980c",
      "READ",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49c24",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b49c28",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b49c34",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b497fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b497fc.md#insn-00b497fc) · [`00b49800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b497fc.md#insn-00b49800) · [`00b49810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b497fc.md#insn-00b49810)

~~~diff
- 00b497fc ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b497fc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b497fc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b497fc bytes f30f1ef8
- 00b49800 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b49800 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b49800 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b49800 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b49800 bytes fd7b01a9
- 00b49810 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b49810 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b49810 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f717162501845fd47016cdd15fc1610d"></a>

### [`00b4987c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4987c.md) → [`00b49ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ca4.md) _ZN8firebase4util4date10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "site": "00b4987c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49880"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49880"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4987c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b49880",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4988c",
      "READ",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49ca4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b49ca8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b49cb4",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4987c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4987c.md#insn-00b4987c) · [`00b49880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4987c.md#insn-00b49880) · [`00b49890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4987c.md#insn-00b49890)

~~~diff
- 00b4987c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4987c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4987c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4987c bytes f30f1ef8
- 00b49880 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b49880 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b49880 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b49880 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b49880 bytes fd7b01a9
- 00b49890 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b49890 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b49890 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-323c39c04e6167ccdd0f2999183c7cb2"></a>

### [`00b49abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49abc.md) → [`00b49ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ee4.md) _ZN8firebase4util4date11GetMethodIdENS1_6MethodE

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
      "site": "00b49adc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b49f04"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49af4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49ef8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b49ae0"
      ]
    ],
    [
      "unmatched:00b49ad8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b49adc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b49ef8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49f08"
      ]
    ],
    [
      "00b49f00",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b49f04",
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

- 旧版 [`00b49adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49abc.md#insn-00b49adc) · [`00b49af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49abc.md#insn-00b49af4)
- 新版 [`00b49f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49ee4.md#insn-00b49f04)

~~~diff
- 00b49adc ["INT_ADD", "register:40f0:8", ["const:b49adc:8", "const:4:8"]]
- 00b49adc ["CALL", null, ["callee:00c5b000:8"]]
- 00b49adc bytes 49440494
- 00b49af4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b49af4 ["RETURN", null, ["register:0:8"]]
- 00b49af4 bytes c0035fd6
+ 00b49f04 ["INT_ADD", "register:40f0:8", ["const:b49f04:8", "const:4:8"]]
+ 00b49f04 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b49f04 bytes 3f440494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95b2b858981491fdde845f1406042b32"></a>

### [`00b4b0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b0ac.md) → [`00b4b4d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b4d4.md) _ZN8firebase4util13integer_class11GetMethodIdENS1_6MethodE

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
      "site": "00b4b0cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b4b4f4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b0e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b4e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4b0d0"
      ]
    ],
    [
      "unmatched:00b4b0c8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4b0cc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b4b4e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b4f8"
      ]
    ],
    [
      "00b4b4f0",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4b4f4",
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

- 旧版 [`00b4b0cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b0ac.md#insn-00b4b0cc) · [`00b4b0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b0ac.md#insn-00b4b0e4)
- 新版 [`00b4b4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b4d4.md#insn-00b4b4f4)

~~~diff
- 00b4b0cc ["INT_ADD", "register:40f0:8", ["const:b4b0cc:8", "const:4:8"]]
- 00b4b0cc ["CALL", null, ["callee:00c5b000:8"]]
- 00b4b0cc bytes cd3e0494
- 00b4b0e4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4b0e4 ["RETURN", null, ["register:0:8"]]
- 00b4b0e4 bytes c0035fd6
+ 00b4b4f4 ["INT_ADD", "register:40f0:8", ["const:b4b4f4:8", "const:4:8"]]
+ 00b4b4f4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4b4f4 bytes c33e0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1002bebe73d129339aa40236605acdd6"></a>

### [`00b4b158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b158.md) → [`00b4b580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b580.md) _ZN8firebase4util13integer_class10GetFieldIdENS1_5FieldE

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
      "site": "00b4b178"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b4b5a0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b190"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b594",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4b17c"
      ]
    ],
    [
      "unmatched:00b4b174",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4b178",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b4b594",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b5a4"
      ]
    ],
    [
      "00b4b59c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4b5a0",
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

- 旧版 [`00b4b178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b158.md#insn-00b4b178) · [`00b4b190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b158.md#insn-00b4b190)
- 新版 [`00b4b5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b580.md#insn-00b4b5a0)

~~~diff
- 00b4b178 ["INT_ADD", "register:40f0:8", ["const:b4b178:8", "const:4:8"]]
- 00b4b178 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4b178 bytes a23e0494
- 00b4b190 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4b190 ["RETURN", null, ["register:0:8"]]
- 00b4b190 bytes c0035fd6
+ 00b4b5a0 ["INT_ADD", "register:40f0:8", ["const:b4b5a0:8", "const:4:8"]]
+ 00b4b5a0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4b5a0 bytes 983e0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd7481752c1acfcec5a28bcfa16bcc05"></a>

### [`00b4bff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bff8.md) → [`00b4c420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c420.md) _ZN8firebase4util4list10GetFieldIdENS1_5FieldE

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
      "site": "00b4bff8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4bffc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4bffc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4bff8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4bffc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4c434",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4c01c"
      ]
    ]
  ],
  "added": [
    [
      "00b4c420",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4c424",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4c434",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4c444"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bff8.md#insn-00b4bff8) · [`00b4bffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bff8.md#insn-00b4bffc) · [`00b4c018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bff8.md#insn-00b4c018)

~~~diff
- 00b4bff8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4bff8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4bff8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4bff8 bytes f30f1ef8
- 00b4bffc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4bffc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4bffc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4bffc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4bffc bytes fd7b01a9
- 00b4c018 ["INT_ADD", "register:40f0:8", ["const:b4c018:8", "const:4:8"]]
- 00b4c018 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4c018 bytes fa3a0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b3a810dcc22a634850993dc2c1b4424"></a>

### [`00b4c2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c2f4.md) → [`00b4c71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c71c.md) _ZN8firebase4util10long_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ae70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae70.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5b270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b270.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "site": "00b4c314"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b4c73c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c32c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4c730",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4c318"
      ]
    ],
    [
      "unmatched:00b4c310",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4c314",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b4c730",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4c740"
      ]
    ],
    [
      "00b4c738",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4c73c",
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

- 旧版 [`00b4c314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c2f4.md#insn-00b4c314) · [`00b4c32c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c2f4.md#insn-00b4c32c)
- 新版 [`00b4c73c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c71c.md#insn-00b4c73c)

~~~diff
- 00b4c314 ["INT_ADD", "register:40f0:8", ["const:b4c314:8", "const:4:8"]]
- 00b4c314 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4c314 bytes 3b3a0494
- 00b4c32c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4c32c ["RETURN", null, ["register:0:8"]]
- 00b4c32c bytes c0035fd6
+ 00b4c73c ["INT_ADD", "register:40f0:8", ["const:b4c73c:8", "const:4:8"]]
+ 00b4c73c ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4c73c bytes 313a0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7aac1829b7142a7ee2563fd4404abef5"></a>

### [`00b4c748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c748.md) → [`00b4cb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cb70.md) _ZN8firebase4util3map10GetFieldIdENS1_5FieldE

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
      "site": "00b4c768"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b4cb90"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c780"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4cb84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4c76c"
      ]
    ],
    [
      "unmatched:00b4c764",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4c768",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b4cb84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4cb94"
      ]
    ],
    [
      "00b4cb8c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4cb90",
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

- 旧版 [`00b4c768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c748.md#insn-00b4c768) · [`00b4c780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c748.md#insn-00b4c780)
- 新版 [`00b4cb90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cb70.md#insn-00b4cb90)

~~~diff
- 00b4c768 ["INT_ADD", "register:40f0:8", ["const:b4c768:8", "const:4:8"]]
- 00b4c768 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4c768 bytes 26390494
- 00b4c780 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4c780 ["RETURN", null, ["register:0:8"]]
- 00b4c780 bytes c0035fd6
+ 00b4cb90 ["INT_ADD", "register:40f0:8", ["const:b4cb90:8", "const:4:8"]]
+ 00b4cb90 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4cb90 bytes 1c390494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd04c9af262d3007c08f9bef8e604e20"></a>

### [`00b4e034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e034.md) → [`00b4e45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e45c.md) _ZN8firebase4util6object11GetMethodIdENS1_6MethodE

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
      "site": "00b4e054"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b4e47c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e06c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4e470",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4e058"
      ]
    ],
    [
      "unmatched:00b4e050",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4e054",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b4e470",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4e480"
      ]
    ],
    [
      "00b4e478",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4e47c",
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

- 旧版 [`00b4e054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e034.md#insn-00b4e054) · [`00b4e06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e034.md#insn-00b4e06c)
- 新版 [`00b4e47c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e45c.md#insn-00b4e47c)

~~~diff
- 00b4e054 ["INT_ADD", "register:40f0:8", ["const:b4e054:8", "const:4:8"]]
- 00b4e054 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4e054 bytes eb320494
- 00b4e06c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4e06c ["RETURN", null, ["register:0:8"]]
- 00b4e06c bytes c0035fd6
+ 00b4e47c ["INT_ADD", "register:40f0:8", ["const:b4e47c:8", "const:4:8"]]
+ 00b4e47c ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4e47c bytes e1320494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70dd2bbd6ffd9f9fcf73095840cc1942"></a>

### [`00b4e0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e0e0.md) → [`00b4e508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e508.md) _ZN8firebase4util6object10GetFieldIdENS1_5FieldE

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
      "site": "00b4e0e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e0e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e0e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4e0e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4e0e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4e51c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4e104"
      ]
    ]
  ],
  "added": [
    [
      "00b4e508",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4e50c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4e51c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4e52c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e0e0.md#insn-00b4e0e0) · [`00b4e0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e0e0.md#insn-00b4e0e4) · [`00b4e100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e0e0.md#insn-00b4e100)

~~~diff
- 00b4e0e0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4e0e0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4e0e0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4e0e0 bytes f30f1ef8
- 00b4e0e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4e0e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4e0e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4e0e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4e0e4 bytes fd7b01a9
- 00b4e100 ["INT_ADD", "register:40f0:8", ["const:b4e100:8", "const:4:8"]]
- 00b4e100 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4e100 bytes c0320494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a49e76a97fd63f2805b56eb9719f4c52"></a>

### [`00b5216c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b5216c.md) → [`00b52594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b52594.md) _ZN8firebase4util15JStringToStringEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1c0.md)
- 新版 呼出元 1件 [`00c5af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af20.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5b5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5c0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 81.82% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5227c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b526a4"
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
      "00b52628",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b52628",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5227c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b5216c.md#insn-00b5227c) · [`00b521a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b5216c.md#insn-00b521a4)
- 新版 [`00b526a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b52594.md#insn-00b526a4) · [`00b525cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b52594.md#insn-00b525cc)

~~~diff
- 00b5227c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b5227c ["RETURN", null, ["register:0:8"]]
- 00b5227c bytes c0035fd6
+ 00b526a4 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b526a4 ["RETURN", null, ["register:0:8"]]
+ 00b526a4 bytes c0035fd6
- 00b521a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b521a4 ["INT_ADD", "register:40f0:8", ["const:b521a4:8", "const:4:8"]]
- 00b521a4 ["CALLIND", null, ["register:0:8"]]
+ 00b525cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b525cc ["INT_ADD", "register:40f0:8", ["const:b525cc:8", "const:4:8"]]
+ 00b525cc ["CALLIND", null, ["register:0:8"]]
- 00b521a4 bytes 00013fd6
+ 00b525cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1c2c2278710bcb5bd994dbf3abdc206"></a>

### [`00b52f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52f24.md) → [`00b5334c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b5334c.md) _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5af90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af90.md) · 呼出先 1件 [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md)
- 新版 呼出元 1件 [`00c5b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b390.md) · 呼出先 1件 [`00c5af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af20.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b52f24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b52f24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b52f28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b52f24",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b52f28",
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
      "00b5334c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b53350",
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

- 旧版 [`00b52f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52f24.md#insn-00b52f24) · [`00b52f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52f24.md#insn-00b52f28)
- 新版 [`00b5334c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b5334c.md#insn-00b5334c)

~~~diff
- 00b52f24 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b52f24 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b52f24 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b52f24 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b52f24 bytes f44fbea9
- 00b52f28 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b52f28 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b52f28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b52f28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b52f28 bytes fd7b01a9
+ 00b5334c ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00b5334c ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00b5334c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00b5334c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b5334c bytes f44fbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fec8facdaea2a87773f810fbdfc0d058"></a>

### [`00b52f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52f58.md) → [`00b53380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53380.md) _ZN8firebase4util23VariantVectorToJavaListEP7_JNIEnvRKNSt6__ndk16vectorINS_7VariantENS3_9allocatorIS5_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b0c0.md) · 呼出先 3件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5b040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b040.md)
- 新版 呼出元 1件 [`00c5b4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b4c0.md) · 呼出先 3件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5b440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b440.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 81.48% / 新版 91.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b52f58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b52f58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b52f5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b52f58",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b52f5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b52f60",
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
      "00b53380",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b53384",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b53388",
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

- 旧版 [`00b52f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52f58.md#insn-00b52f58) · [`00b52f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52f58.md#insn-00b52f5c) · [`00b52f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b52/00b52f58.md#insn-00b52f60)

~~~diff
- 00b52f58 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b52f58 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b52f58 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b52f58 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b52f58 bytes f85fbca9
- 00b52f5c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b52f5c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b52f5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b52f5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b52f5c bytes f65701a9
- 00b52f60 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b52f60 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b52f60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b52f60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b52f60 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ee75cdfb7e598a879501ea08e8056df"></a>

### [`00b53218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53218.md) → [`00b53640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53640.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE7reserveEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7b0.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5abb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abb0.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 67.65% / 新版 67.65%

CFGの説明率　旧版 9.09% / 新版 13.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53218"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53218"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5321c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53218",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5321c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53220",
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
      "00b53640",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b53644",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b53648",
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

- 旧版 [`00b53218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53218.md#insn-00b53218) · [`00b5321c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53218.md#insn-00b5321c) · [`00b53220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53218.md#insn-00b53220)

~~~diff
- 00b53218 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b53218 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b53218 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b53218 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b53218 bytes f657bda9
- 00b5321c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5321c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5321c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5321c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5321c bytes f44f01a9
- 00b53220 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b53220 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b53220 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b53220 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53220 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb3788b6f4603d8d3902481fd58de33a"></a>

### [`00b53904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53904.md) → [`00b53d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53d2c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1c0.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5b5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5c0.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.49% / 新版 86.49%

CFGの説明率　旧版 50.00% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53904"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53904"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53908"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53904",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53908",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5390c",
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
      "00b53d2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b53d30",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b53d34",
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

- 旧版 [`00b53904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53904.md#insn-00b53904) · [`00b53908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53904.md#insn-00b53908) · [`00b5390c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53904.md#insn-00b5390c)

~~~diff
- 00b53904 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b53904 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b53904 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b53904 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b53904 bytes f657bda9
- 00b53908 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b53908 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b53908 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b53908 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53908 bytes f44f01a9
- 00b5390c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5390c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5390c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5390c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5390c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3372e1e09cb3b06d0226eeeb508dce27"></a>

### [`00b53bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53bb4.md) → [`00b53fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b53/00b53fdc.md) _ZN7_JNIEnv14CallByteMethodEP8_jobjectP10_jmethodIDz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ae00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae00.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5b200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b200.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 30.77% / 新版 30.77%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53bc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53bc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53bc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53bc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53bc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53bcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b53fec",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "00b53ff0",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "00b53ff4",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53bb4.md#insn-00b53bc4) · [`00b53bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53bb4.md#insn-00b53bc8) · [`00b53bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53bb4.md#insn-00b53bcc)

~~~diff
- 00b53bc4 ["COPY", "tmp:0:8", ["register:4018:8"]]
- 00b53bc4 ["COPY", "tmp:1:8", ["register:4020:8"]]
- 00b53bc4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:88:8"]]
- 00b53bc4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53bc4 bytes e39308a9
- 00b53bc8 ["COPY", "tmp:0:8", ["register:4028:8"]]
- 00b53bc8 ["COPY", "tmp:1:8", ["register:4030:8"]]
- 00b53bc8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:98:8"]]
- 00b53bc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53bc8 bytes e59b09a9
- 00b53bcc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:a8:8"]]
- 00b53bcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4038:8"]]
- 00b53bcc bytes e75700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c4e2a65d3acb9e6fa0cc53f4a50fdc5"></a>

### [`00b53cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53cb8.md) → [`00b540e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b540e0.md) _ZN7_JNIEnv14CallCharMethodEP8_jobjectP10_jmethodIDz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5ae10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae10.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5b210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b210.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_target, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.18% / 新版 87.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b54144",
      "incomplete_value": true,
      "site": "00b54150",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53d1c",
      "incomplete_value": true,
      "site": "00b53d28",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40e8:8"
              ],
              [
                "leaf",
                "const:38:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b54144",
      "incomplete_value": true,
      "site": "00b54150",
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
                "live",
                "register:4048:8"
              ],
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
      "definition_site": "00b53d1c",
      "incomplete_value": true,
      "site": "00b53d28",
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
              "INT_SUB",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00b54154",
      "incomplete_value": true,
      "site": "00b54154",
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
                "const:160:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53d2c",
      "incomplete_value": true,
      "site": "00b53d2c",
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
                "const:160:8"
              ]
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
      "unmatched:00b53d1c",
      "READ",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54144",
      "READ",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53cb8.md#insn-00b53d2c) · [`00b53d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53cb8.md#insn-00b53d18) · [`00b53d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53cb8.md#insn-00b53d1c)
- 新版 [`00b54154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b540e0.md#insn-00b54154)

~~~diff
- 00b53d2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53d2c ["INT_ADD", "register:40f0:8", ["const:b53d2c:8", "const:4:8"]]
- 00b53d2c ["CALLIND", null, ["register:0:8"]]
+ 00b54154 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b54154 ["INT_ADD", "register:40f0:8", ["const:b54154:8", "const:4:8"]]
+ 00b54154 ["CALLIND", null, ["register:0:8"]]
- 00b53d2c bytes 00013fd6
+ 00b54154 bytes 00013fd6
- 00b53d18 ["INT_SUB", "register:4048:8", ["register:40e8:8", "const:38:8"]]
- 00b53d18 bytes a9e300d1
- 00b53d1c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b53d1c ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 00b53d1c ["COPY", "register:5030:8", ["const:0:8"]]
- 00b53d1c ["COPY", "register:5038:8", ["const:0:8"]]
- 00b53d1c bytes 210140ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62a7276f757f51f37a415b8c91dccf4e"></a>

### [`00b53dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53dbc.md) → [`00b541e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b541e4.md) _ZN7_JNIEnv15CallShortMethodEP8_jobjectP10_jmethodIDz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5ae20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae20.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5b220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b220.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53dd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53dd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53dd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53dd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53dd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53dd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x120]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b541f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "00b541fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00b54200",
      "WRITE",
      [
        "storage",
        "Stack[-0x120]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53dbc.md#insn-00b53dd0) · [`00b53dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53dbc.md#insn-00b53dd4) · [`00b53dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53dbc.md#insn-00b53dd8)

~~~diff
- 00b53dd0 ["COPY", "tmp:0:8", ["register:4028:8"]]
- 00b53dd0 ["COPY", "tmp:1:8", ["register:4030:8"]]
- 00b53dd0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:98:8"]]
- 00b53dd0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53dd0 bytes e59b09a9
- 00b53dd4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:a8:8"]]
- 00b53dd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4038:8"]]
- 00b53dd4 bytes e75700f9
- 00b53dd8 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b53dd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b53dd8 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b53dd8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00b53dd8 bytes e00700ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a85472f8ab100c07d1911a5fe4068396"></a>

### [`00b54008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54008.md) → [`00b54430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54430.md) _ZN7_JNIEnv16CallDoubleMethodEP8_jobjectP10_jmethodIDz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae30.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5b230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b230.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 43.59% / 新版 43.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54028"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54028"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5402c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b54028",
      "WRITE",
      [
        "storage",
        "Stack[-0x100]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5402c",
      "WRITE",
      [
        "storage",
        "Stack[-0xe0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b54030",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54450",
      "WRITE",
      [
        "storage",
        "Stack[-0x100]",
        null,
        null
      ]
    ],
    [
      "00b54454",
      "WRITE",
      [
        "storage",
        "Stack[-0xe0]",
        null,
        null
      ]
    ],
    [
      "00b54458",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54008.md#insn-00b54028) · [`00b5402c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54008.md#insn-00b5402c) · [`00b54030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54008.md#insn-00b54030)

~~~diff
- 00b54028 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b54028 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5040:16"]]
- 00b54028 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b54028 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5060:16"]]
- 00b54028 bytes e20f01ad
- 00b5402c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00b5402c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5080:16"]]
- 00b5402c ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b5402c ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:50a0:16"]]
- 00b5402c bytes e41702ad
- 00b54030 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00b54030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:50c0:16"]]
- 00b54030 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b54030 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:50e0:16"]]
- 00b54030 bytes e61f03ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b94a1046e5a1d4d8a9735738a5b4bb39"></a>

### [`00b540a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b540a4.md) → [`00b544cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b544cc.md) _ZN8firebase4util15IsJBooleanArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b540cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b540e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54104"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b540c0",
      "PARAM",
      [
        "storage",
        "002abf4e",
        null,
        null
      ]
    ],
    [
      "unmatched:00b540cc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00b540e8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b544e8",
      "PARAM",
      [
        "storage",
        "002abf8e",
        null,
        null
      ]
    ],
    [
      "00b544f4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00b54510",
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

- 旧版 [`00b540cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b540a4.md#insn-00b540cc) · [`00b540e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b540a4.md#insn-00b540e8) · [`00b54104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b540a4.md#insn-00b54104)

~~~diff
- 00b540cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b540cc ["INT_ADD", "register:40f0:8", ["const:b540cc:8", "const:4:8"]]
- 00b540cc ["CALLIND", null, ["register:0:8"]]
- 00b540cc bytes 00013fd6
- 00b540e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b540e8 ["INT_ADD", "register:40f0:8", ["const:b540e8:8", "const:4:8"]]
- 00b540e8 ["CALLIND", null, ["register:0:8"]]
- 00b540e8 bytes 00013fd6
- 00b54104 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54104 ["INT_ADD", "register:40f0:8", ["const:b54104:8", "const:4:8"]]
- 00b54104 ["CALLIND", null, ["register:0:8"]]
- 00b54104 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5f4669f76f71e08eaa87ce902386725"></a>

### [`00b54194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54194.md) → [`00b545bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b545bc.md) _ZN8firebase4util12IsJCharArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 43.33% / 新版 43.33%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54194"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54198"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54198"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b54194",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b54198",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5419c",
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
      "00b545bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b545c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b545c4",
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

- 旧版 [`00b54194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54194.md#insn-00b54194) · [`00b54198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54194.md#insn-00b54198) · [`00b5419c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54194.md#insn-00b5419c)

~~~diff
- 00b54194 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b54194 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b54194 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b54194 bytes f50f1df8
- 00b54198 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b54198 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b54198 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b54198 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b54198 bytes f44f01a9
- 00b5419c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5419c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5419c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5419c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5419c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6629daaf0cb527ede37246722102ea70"></a>

### [`00b54284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54284.md) → [`00b546ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b546ac.md) _ZN8firebase4util11IsJIntArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 86.67% / 新版 86.67%

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
      "site": "00b542ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b546d4"
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
      "unmatched:00b542a0",
      "PARAM",
      [
        "storage",
        "002bad56",
        null,
        null
      ]
    ],
    [
      "unmatched:00b542ac",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b546c8",
      "PARAM",
      [
        "storage",
        "002bad96",
        null,
        null
      ]
    ],
    [
      "00b546d4",
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

- 旧版 [`00b542ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54284.md#insn-00b542ac) · [`00b542a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54284.md#insn-00b542a0)
- 新版 [`00b546d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b546ac.md#insn-00b546d4)

~~~diff
- 00b542ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b542ac ["INT_ADD", "register:40f0:8", ["const:b542ac:8", "const:4:8"]]
- 00b542ac ["CALLIND", null, ["register:0:8"]]
- 00b542ac bytes 00013fd6
+ 00b546d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b546d4 ["INT_ADD", "register:40f0:8", ["const:b546d4:8", "const:4:8"]]
+ 00b546d4 ["CALLIND", null, ["register:0:8"]]
+ 00b546d4 bytes 00013fd6
- 00b542a0 ["COPY", "tmp:0:8", ["const:d56:8"]]
- 00b542a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b542a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b542a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b542a0 bytes 21583591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-008396d8bacc7506eb6a1733aec2040d"></a>

### [`00b542fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b542fc.md) → [`00b54724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54724.md) _ZN8firebase4util12IsJLongArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 76.67% / 新版 76.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54340"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5435c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b54768"
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
      "unmatched:00b54318",
      "PARAM",
      [
        "storage",
        "002a82d7",
        null,
        null
      ]
    ],
    [
      "unmatched:00b54340",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00b5435c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54740",
      "PARAM",
      [
        "storage",
        "002a83a4",
        null,
        null
      ]
    ],
    [
      "00b54768",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00b54784",
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

- 旧版 [`00b54340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b542fc.md#insn-00b54340) · [`00b5435c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b542fc.md#insn-00b5435c)
- 新版 [`00b54768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54724.md#insn-00b54768)

~~~diff
- 00b54340 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54340 ["INT_ADD", "register:40f0:8", ["const:b54340:8", "const:4:8"]]
- 00b54340 ["CALLIND", null, ["register:0:8"]]
- 00b54340 bytes 00013fd6
- 00b5435c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5435c ["INT_ADD", "register:40f0:8", ["const:b5435c:8", "const:4:8"]]
- 00b5435c ["CALLIND", null, ["register:0:8"]]
- 00b5435c bytes 00013fd6
+ 00b54768 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b54768 ["INT_ADD", "register:40f0:8", ["const:b54768:8", "const:4:8"]]
+ 00b54768 ["CALLIND", null, ["register:0:8"]]
+ 00b54768 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ea37bd68988250a8397432eaf88c54f"></a>

### [`00b543ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b543ec.md) → [`00b54814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54814.md) _ZN8firebase4util14IsJDoubleArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 63.33% / 新版 63.33%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b543ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b543f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b543f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b543ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b543f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b543f4",
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
      "00b54814",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b54818",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5481c",
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

- 旧版 [`00b543ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b543ec.md#insn-00b543ec) · [`00b543f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b543ec.md#insn-00b543f0) · [`00b543f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b543ec.md#insn-00b543f4)

~~~diff
- 00b543ec ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b543ec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b543ec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b543ec bytes f50f1df8
- 00b543f0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b543f0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b543f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b543f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b543f0 bytes f44f01a9
- 00b543f4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b543f4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b543f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b543f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b543f4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee82f927f15b7eb9119233ed6b53aa34"></a>

### [`00b545e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b545e8.md) → [`00b54a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54a10.md) _ZN8firebase4util19JByteArrayToVariantEP7_JNIEnvP11_jbyteArray

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5afd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afd0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5b3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3d0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.37% / 新版 87.37%

CFGの説明率　旧版 53.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b545f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b545f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b545fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b545f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b545fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b54600",
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
      "00b54a20",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b54a24",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b54a28",
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

- 旧版 [`00b545f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b545e8.md#insn-00b545f8) · [`00b545fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b545e8.md#insn-00b545fc) · [`00b54600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b545e8.md#insn-00b54600)

~~~diff
- 00b545f8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b545f8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b545f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b545f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b545f8 bytes f65705a9
- 00b545fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b545fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b545fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b545fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b545fc bytes f44f06a9
- 00b54600 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b54600 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b54600 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b54600 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b54600 bytes fd7b07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7206b9585a1bbbc327262af6a79286f2"></a>

### [`00b54a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54a60.md) → [`00b54e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b54/00b54e88.md) _ZN8firebase4util18JIntArrayToVariantEP7_JNIEnvP10_jintArray

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5afb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afb0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5b3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3b0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.42% / 新版 88.42%

CFGの説明率　旧版 26.32% / 新版 29.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54a70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54a70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54a74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b54a70",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b54a74",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b54a78",
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
      "00b54e98",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b54e9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b54ea0",
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

- 旧版 [`00b54a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54a60.md#insn-00b54a70) · [`00b54a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54a60.md#insn-00b54a74) · [`00b54a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54a60.md#insn-00b54a78)

~~~diff
- 00b54a70 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b54a70 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b54a70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b54a70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b54a70 bytes f65705a9
- 00b54a74 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b54a74 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b54a74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b54a74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b54a74 bytes f44f06a9
- 00b54a78 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b54a78 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b54a78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b54a78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b54a78 bytes fd7b07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e16041bd5f8a86bbc9d98eb8e97167f6"></a>

### [`00b54bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54bdc.md) → [`00b55004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55004.md) _ZN8firebase4util19JLongArrayToVariantEP7_JNIEnvP11_jlongArray

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5aff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aff0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5b3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3f0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 97.89% / 新版 97.89%

CFGの説明率　旧版 37.50% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54d1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b55144"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54d4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b54d1c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b55144",
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

- 旧版 [`00b54d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54bdc.md#insn-00b54d1c) · [`00b54d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54bdc.md#insn-00b54d4c)
- 新版 [`00b55144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55004.md#insn-00b55144)

~~~diff
- 00b54d1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54d1c ["INT_ADD", "register:40f0:8", ["const:b54d1c:8", "const:4:8"]]
- 00b54d1c ["CALLIND", null, ["register:0:8"]]
- 00b54d1c bytes 00013fd6
- 00b54d4c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b54d4c ["RETURN", null, ["register:0:8"]]
- 00b54d4c bytes c0035fd6
+ 00b55144 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b55144 ["INT_ADD", "register:40f0:8", ["const:b55144:8", "const:4:8"]]
+ 00b55144 ["CALLIND", null, ["register:0:8"]]
+ 00b55144 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4438499508030f85f2db6c146ca7cb14"></a>

### [`00b555e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b555e8.md) → [`00b55a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55a10.md) _ZN8firebase4util25ByteBufferToJavaByteArrayEP7_JNIEnvPKhm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.00% / 新版 96.00%

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
      "site": "00b55648"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b55a70"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b55648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b555e8.md#insn-00b55648) · [`00b55610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b555e8.md#insn-00b55610)
- 新版 [`00b55a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55a10.md#insn-00b55a70) · [`00b55a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55a10.md#insn-00b55a38)

~~~diff
- 00b55648 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b55648 ["RETURN", null, ["register:0:8"]]
- 00b55648 bytes c0035fd6
+ 00b55a70 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b55a70 ["RETURN", null, ["register:0:8"]]
+ 00b55a70 bytes c0035fd6
- 00b55610 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55610 ["INT_ADD", "register:40f0:8", ["const:b55610:8", "const:4:8"]]
- 00b55610 ["CALLIND", null, ["register:0:8"]]
+ 00b55a38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b55a38 ["INT_ADD", "register:40f0:8", ["const:b55a38:8", "const:4:8"]]
+ 00b55a38 ["CALLIND", null, ["register:0:8"]]
- 00b55610 bytes 00013fd6
+ 00b55a38 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4518ee82b75e903d844eae7f55663146"></a>

### [`00b55970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55970.md) → [`00b55d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55d98.md) _ZN8firebase4util20JniByteArrayToVectorEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5b070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b070.md) · 呼出先 1件 [`00c5b260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b260.md)
- 新版 呼出元 1件 [`00c5b470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b470.md) · 呼出先 1件 [`00c5b660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b660.md)

変更の種類 call, call_argument_candidate, call_count, call_target, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 84.85% / 新版 84.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 4件, `call_target` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5599c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b559ac",
      "incomplete_value": true,
      "site": "00b559b0",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b559a8",
      "incomplete_value": true,
      "site": "00b559b0",
      "value": [
        "INT_SEXT",
        "8",
        [
          [
            "live",
            "register:40b0:4"
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
      "unmatched:00b5599c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b55dc4",
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

- 旧版 [`00b5599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55970.md#insn-00b5599c) · [`00b559b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55970.md#insn-00b559b0) · [`00b559d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55970.md#insn-00b559d0)
- 新版 [`00b55dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55d98.md#insn-00b55dd8) · [`00b55df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55d98.md#insn-00b55df8)

~~~diff
- 00b5599c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5599c ["INT_ADD", "register:40f0:8", ["const:b5599c:8", "const:4:8"]]
- 00b5599c ["CALLIND", null, ["register:0:8"]]
- 00b5599c bytes 00013fd6
- 00b559b0 ["INT_ADD", "register:40f0:8", ["const:b559b0:8", "const:4:8"]]
- 00b559b0 ["CALL", null, ["callee:00c5b660:8"]]
+ 00b55dd8 ["INT_ADD", "register:40f0:8", ["const:b55dd8:8", "const:4:8"]]
+ 00b55dd8 ["CALL", null, ["callee:00c5b660:8"]]
- 00b559b0 bytes 2c160494
+ 00b55dd8 bytes 22160494
- 00b559d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b559d0 ["INT_ADD", "register:40f0:8", ["const:b559d0:8", "const:4:8"]]
- 00b559d0 ["CALLIND", null, ["register:0:8"]]
+ 00b55df8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b55df8 ["INT_ADD", "register:40f0:8", ["const:b55df8:8", "const:4:8"]]
+ 00b55df8 ["CALLIND", null, ["register:0:8"]]
- 00b559d0 bytes 00013fd6
+ 00b55df8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3de83e85622dc3504e2539e04cf9581"></a>

### [`00b55a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55a50.md) → [`00b55e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55e78.md) _ZN8firebase4util15ContinueBuilderEP7_JNIEnvP8_jobjectS4_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55a68"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b55e90"
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
      "unmatched:00b55a68",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b55e90",
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

- 旧版 [`00b55a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55a50.md#insn-00b55a68)
- 新版 [`00b55e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55e78.md#insn-00b55e90)

~~~diff
- 00b55a68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55a68 ["INT_ADD", "register:40f0:8", ["const:b55a68:8", "const:4:8"]]
- 00b55a68 ["CALLIND", null, ["register:0:8"]]
- 00b55a68 bytes 00013fd6
+ 00b55e90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b55e90 ["INT_ADD", "register:40f0:8", ["const:b55e90:8", "const:4:8"]]
+ 00b55e90 ["CALLIND", null, ["register:0:8"]]
+ 00b55e90 bytes 00013fd6
~~~


<a id="compare-de6c29c94c2773c8922106ac2d0ecbe8"></a>

### [`00b55dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55dc4.md) → [`00b561ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b561ec.md) _ZN8firebase4util17JavaThreadContext6CancelEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ade0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ade0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5b1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1e0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55ddc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55e04"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b56204"
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
      "unmatched:00b55ddc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b56258"
      ]
    ],
    [
      "00b5620c",
      "READ",
      [
        "storage",
        "01125290",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b55e04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b56258"
      ]
    ]
  ],
  "added": [
    [
      "00b56204",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b56258"
      ]
    ],
    [
      "00b5620c",
      "READ",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5622c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b56258"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b55ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55dc4.md#insn-00b55ddc) · [`00b55dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55dc4.md#insn-00b55dec) · [`00b55dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55dc4.md#insn-00b55dfc)
- 新版 [`00b56214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b561ec.md#insn-00b56214) · [`00b56224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b56/00b561ec.md#insn-00b56224)

~~~diff
- 00b55ddc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b55ddc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b55ddc bytes a10200b4
- 00b55dec ["INT_ADD", "register:40f0:8", ["const:b55dec:8", "const:4:8"]]
- 00b55dec ["CALL", null, ["callee:00574cec:8"]]
+ 00b56214 ["INT_ADD", "register:40f0:8", ["const:b56214:8", "const:4:8"]]
+ 00b56214 ["CALL", null, ["callee:00574cec:8"]]
- 00b55dec bytes b07be897
+ 00b56214 bytes b67ae897
- 00b55dfc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55dfc ["INT_ADD", "register:40f0:8", ["const:b55dfc:8", "const:4:8"]]
- 00b55dfc ["CALLIND", null, ["register:0:8"]]
+ 00b56224 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b56224 ["INT_ADD", "register:40f0:8", ["const:b56224:8", "const:4:8"]]
+ 00b56224 ["CALLIND", null, ["register:0:8"]]
- 00b55dfc bytes 00013fd6
+ 00b56224 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57e36044d54fcad1863fb91ba6f4ff83"></a>

### [`00b57020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57020.md) → [`00b57448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57448.md) _ZN8firebase4util23GetMessageFromExceptionEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ab50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab50.md) · 呼出先 3件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab20.md) [`00c5b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1c0.md)
- 新版 呼出元 1件 [`00c5af50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af50.md) · 呼出先 3件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00c5af20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af20.md) [`00c5b5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5c0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 62.86% / 新版 62.86%

CFGの説明率　旧版 22.22% / 新版 21.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 7件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b570b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57138"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5748c"
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
      "00b57464",
      "READ",
      [
        "storage",
        "01125900",
        null,
        "undefined8"
      ]
    ],
    [
      "00b57560",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b574b0"
      ]
    ],
    [
      "00b574b8",
      "READ",
      [
        "storage",
        "01125908",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b57464",
      "READ",
      [
        "storage",
        "01125d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5748c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b574b0"
      ]
    ],
    [
      "00b574b8",
      "READ",
      [
        "storage",
        "01125d08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5709c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57020.md#insn-00b5709c) · [`00b570b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57020.md#insn-00b570b0) · [`00b570b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57020.md#insn-00b570b8)

~~~diff
- 00b5709c ["INT_ADD", "register:40f0:8", ["const:b5709c:8", "const:4:8"]]
- 00b5709c ["CALL", null, ["callee:00497834:8"]]
- 00b5709c bytes d601e597
- 00b570b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b570b0 ["INT_ADD", "register:40f0:8", ["const:b570b0:8", "const:4:8"]]
- 00b570b0 ["CALLIND", null, ["register:0:8"]]
- 00b570b0 bytes 00013fd6
- 00b570b8 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 00b570b8 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fac9fd81e76949ff9f78488d1779665"></a>

### [`00b57478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57478.md) → [`00b578a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b578a0.md) DetachJVMThreads

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b574f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b574f0.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00b57918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57918.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5747c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5747c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57480"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5747c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b57480",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5749c",
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
      "00b578a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b578a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b578c4",
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

- 旧版 [`00b5747c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57478.md#insn-00b5747c) · [`00b57480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57478.md#insn-00b57480) · [`00b5749c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57478.md#insn-00b5749c)

~~~diff
- 00b5747c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5747c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5747c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5747c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5747c bytes f44f01a9
- 00b57480 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b57480 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b57480 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b57480 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b57480 bytes fd7b02a9
- 00b5749c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b5749c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5749c bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6ddda439a5d40f43a041717dc373d9f"></a>

### [`00b574f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b574f0.md) → [`00b57918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57918.md) SetupJvmDetachOnThreadDestruction

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b57504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57504.md) · 呼出先 2件 [`00b57478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57478.md) [`00c59f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f00.md)
- 新版 呼出元 1件 [`00b5792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b5792c.md) · 呼出先 2件 [`00b578a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b578a0.md) [`00c5a300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a300.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b574f8",
      "READ",
      [
        "storage",
        "00c9b330",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b574f8",
      "PARAM",
      [
        "storage",
        "01125bb4",
        "_ZN8firebase4util11jni_env_keyE",
        "undefined4"
      ]
    ],
    [
      "unmatched:00b574fc",
      "READ",
      [
        "storage",
        "00c9b308",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b57920",
      "READ",
      [
        "storage",
        "00c9b730",
        null,
        "pointer"
      ]
    ],
    [
      "00b57920",
      "PARAM",
      [
        "storage",
        "01125fb4",
        "_ZN8firebase4util11jni_env_keyE",
        "undefined4"
      ]
    ],
    [
      "00b57924",
      "READ",
      [
        "storage",
        "00c9b708",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b574f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b574f0.md#insn-00b574f0) · [`00b574f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b574f0.md#insn-00b574f4) · [`00b574f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b574f0.md#insn-00b574f8)

~~~diff
- 00b574f0 ["COPY", "register:4000:8", ["const:c9b000:8"]]
- 00b574f0 bytes 200a0090
- 00b574f4 ["COPY", "register:4008:8", ["const:c9b000:8"]]
- 00b574f4 bytes 210a0090
- 00b574f8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:330:8"]]
- 00b574f8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b574f8 bytes 009841f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d18f77412bc2d0103c54051fe895c743"></a>

### [`00b57ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57ba4.md) → [`00b57fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57fcc.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIS6_EEvOT_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b250.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5b650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b650.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.41% / 新版 78.41%

CFGの説明率　旧版 19.35% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57c38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57c3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b58060"
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
      "unmatched:00b57bdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58128"
      ]
    ],
    [
      "unmatched:00b57c08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58044"
      ]
    ],
    [
      "00b58040",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b57cf8"
      ]
    ]
  ],
  "added": [
    [
      "00b58004",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58128"
      ]
    ],
    [
      "00b58030",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58044"
      ]
    ],
    [
      "00b58040",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58120"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b57bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57ba4.md#insn-00b57bdc) · [`00b57c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57ba4.md#insn-00b57c08) · [`00b57c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57ba4.md#insn-00b57c38)

~~~diff
- 00b57bdc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b57bdc ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b57bdc ["CBRANCH", null, ["local:b23:8", "tmp:1:1"]]
- 00b57bdc bytes 28090054
- 00b57c08 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b57c08 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b57c08 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00b57c08 bytes a8000054
- 00b57c38 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:10:8"]]
- 00b57c38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b57c38 bytes 480900f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bf450eef8f0412d003689dcc99c4a66"></a>

### [`00b57d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57d04.md) → [`00b5812c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b5812c.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE21__push_back_slow_pathIS2_EEvOT_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b220.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5b620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b620.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 75.28% / 新版 75.28%

CFGの説明率　旧版 46.15% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57d44"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57d70"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57e08"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b57d44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5828c"
      ]
    ],
    [
      "unmatched:00b57d70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b581ac"
      ]
    ],
    [
      "unmatched:00b57e08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5824c"
      ]
    ]
  ],
  "added": [
    [
      "00b5816c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5828c"
      ]
    ],
    [
      "00b58198",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b581ac"
      ]
    ],
    [
      "00b58230",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5824c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b57d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57d04.md#insn-00b57d44) · [`00b57d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57d04.md#insn-00b57d70) · [`00b57e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b57/00b57d04.md#insn-00b57e08)

~~~diff
- 00b57d44 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b57d44 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b57d44 ["CBRANCH", null, ["local:b20:8", "tmp:1:1"]]
- 00b57d44 bytes 08090054
- 00b57d70 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b57d70 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b57d70 ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
- 00b57d70 bytes a8000054
- 00b57e08 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 00b57e08 bytes e0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-604731463ba125a388b7c39a7f187838"></a>

### [`00b586c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b586c8.md) → [`00b58af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58af0.md) _ZN8firebase8internal16JObjectReferenceC1EP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5ad90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad90.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5b190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b190.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58718"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b58b40"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b586e8",
      "incomplete_value": true,
      "site": "00b58700",
      "value": [
        "live",
        "register:4040:8"
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
      "unmatched:00b58718",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58b54"
      ]
    ]
  ],
  "added": [
    [
      "00b58b40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58b54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b586c8.md#insn-00b58700) · [`00b58718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b586c8.md#insn-00b58718)
- 新版 [`00b58b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58af0.md#insn-00b58b28) · [`00b58b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58af0.md#insn-00b58b40)

~~~diff
- 00b58700 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b58700 ["INT_ADD", "register:40f0:8", ["const:b58700:8", "const:4:8"]]
- 00b58700 ["CALLIND", null, ["register:0:8"]]
+ 00b58b28 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b58b28 ["INT_ADD", "register:40f0:8", ["const:b58b28:8", "const:4:8"]]
+ 00b58b28 ["CALLIND", null, ["register:0:8"]]
- 00b58700 bytes 20013fd6
+ 00b58b28 bytes 20013fd6
- 00b58718 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b58718 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b58718 bytes a1000054
+ 00b58b40 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b58b40 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b58b40 bytes a1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19664ed30f086d23878ead7f73974297"></a>

### [`00b58818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58818.md) → [`00b58c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58c40.md) _ZN8firebase8internal16JObjectReference10InitializeEP7_JavaVMP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 40.00% / 新版 40.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58818"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5881c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5881c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b58818",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5881c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b58c50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b58848"
      ]
    ]
  ],
  "added": [
    [
      "00b58c40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b58c44",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b58c50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58c70"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58818.md#insn-00b58818) · [`00b5881c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58818.md#insn-00b5881c) · [`00b58840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58818.md#insn-00b58840)

~~~diff
- 00b58818 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b58818 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b58818 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b58818 bytes f30f1ef8
- 00b5881c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5881c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5881c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5881c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5881c bytes fd7b01a9
- 00b58840 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58840 ["INT_ADD", "register:40f0:8", ["const:b58840:8", "const:4:8"]]
- 00b58840 ["CALLIND", null, ["register:0:8"]]
- 00b58840 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09585c0f6a5646a9d8d8e9743954dc4e"></a>

### [`00b58854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58854.md) → [`00b58c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58c7c.md) _ZN8firebase8internal16JObjectReferenceC2ERKS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ada0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ada0.md) · 呼出先 1件 [`00c5afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afc0.md)
- 新版 呼出元 1件 [`00c5b1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1a0.md) · 呼出先 1件 [`00c5b3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3c0.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b588ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b58cd4"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b588ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58854.md#insn-00b588ac) · [`00b58878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58854.md#insn-00b58878)
- 新版 [`00b58cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58c7c.md#insn-00b58cd4) · [`00b58ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58c7c.md#insn-00b58ca0)

~~~diff
- 00b588ac ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b588ac ["RETURN", null, ["register:0:8"]]
- 00b588ac bytes c0035fd6
+ 00b58cd4 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b58cd4 ["RETURN", null, ["register:0:8"]]
+ 00b58cd4 bytes c0035fd6
- 00b58878 ["INT_ADD", "register:40f0:8", ["const:b58878:8", "const:4:8"]]
- 00b58878 ["CALL", null, ["callee:00c5b3c0:8"]]
+ 00b58ca0 ["INT_ADD", "register:40f0:8", ["const:b58ca0:8", "const:4:8"]]
+ 00b58ca0 ["CALL", null, ["callee:00c5b3c0:8"]]
- 00b58878 bytes d2090494
+ 00b58ca0 bytes c8090494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbf251b09d0d14d6f7b6097280e0f940"></a>

### [`00b588e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b588e0.md) → [`00b58d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58d08.md) _ZN8firebase8internal16JObjectReferenceD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00c5adb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5adb0.md) [`00c5adc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5adc0.md) · 呼出先 1件 [`00c5afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afc0.md)
- 新版 呼出元 2件 [`00c5b1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1b0.md) [`00c5b1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1c0.md) · 呼出先 1件 [`00c5b3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3c0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 22.22% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58920"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b58d48"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b58920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b588e0.md#insn-00b58920) · [`00b588f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b588e0.md#insn-00b588f4)
- 新版 [`00b58d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58d08.md#insn-00b58d48) · [`00b58d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58d08.md#insn-00b58d1c)

~~~diff
- 00b58920 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b58920 ["RETURN", null, ["register:0:8"]]
- 00b58920 bytes c0035fd6
+ 00b58d48 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b58d48 ["RETURN", null, ["register:0:8"]]
+ 00b58d48 bytes c0035fd6
- 00b588f4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b588f4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b58d1c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b58d1c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b588f4 bytes 000100b4
+ 00b58d1c bytes 000100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24749a9a34d04dd233024f6ba840649f"></a>

### [`00b58924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58924.md) → [`00b58d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58d4c.md) _ZN8firebase8internal16JObjectReference3SetEP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ad80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad80.md) · 呼出先 1件 [`00c5afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afc0.md)
- 新版 呼出元 1件 [`00c5b180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b180.md) · 呼出先 1件 [`00c5b3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3c0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.85% / 新版 84.85%

CFGの説明率　旧版 53.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58924"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58928"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58928"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b58924",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58928",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5892c",
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
      "00b58d4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b58d50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b58d54",
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

- 旧版 [`00b58924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58924.md#insn-00b58924) · [`00b58928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58924.md#insn-00b58928) · [`00b5892c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58924.md#insn-00b5892c)

~~~diff
- 00b58924 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b58924 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b58924 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b58924 bytes f50f1df8
- 00b58928 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b58928 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b58928 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b58928 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58928 bytes f44f01a9
- 00b5892c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5892c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5892c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5892c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5892c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07c8e1f71435c14002fd03ec075d2f74"></a>

### [`00b58a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58a7c.md) → [`00b58ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58ea4.md) _ZN8firebase8internal16JObjectReference3SetEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.09% / 新版 84.09%

CFGの説明率　旧版 18.18% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58a80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58a80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58a84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b58a80",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58a84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58a88",
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
      "00b58ea8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b58eac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b58eb0",
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

- 旧版 [`00b58a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58a7c.md#insn-00b58a80) · [`00b58a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58a7c.md#insn-00b58a84) · [`00b58a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58a7c.md#insn-00b58a88)

~~~diff
- 00b58a80 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b58a80 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b58a80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b58a80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58a80 bytes f65701a9
- 00b58a84 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b58a84 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b58a84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b58a84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58a84 bytes f44f02a9
- 00b58a88 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b58a88 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b58a88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b58a88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58a88 bytes fd7b03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84fd704ebc94e92118fd262081fc1963"></a>

### [`00b58b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58b2c.md) → [`00b58f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58f54.md) _ZNK8firebase8internal16JObjectReference11GetLocalRefEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5add0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5add0.md) · 呼出先 1件 [`00c5afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afc0.md)
- 新版 呼出元 1件 [`00c5b1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1d0.md) · 呼出先 1件 [`00c5b3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3c0.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 63.16% / 新版 63.16%

CFGの説明率　旧版 12.50% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58b74"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b58f9c"
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
      "00b58f68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b58b68"
      ]
    ],
    [
      "00b58f70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b58b68"
      ]
    ],
    [
      "00b58f78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b58b68"
      ]
    ]
  ],
  "added": [
    [
      "00b58f68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58f90"
      ]
    ],
    [
      "00b58f70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58f90"
      ]
    ],
    [
      "00b58f78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58f90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58b2c.md#insn-00b58b74) · [`00b58b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b58/00b58b2c.md#insn-00b58b44)
- 新版 [`00b58f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58f54.md#insn-00b58f9c) · [`00b58f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58f54.md#insn-00b58f6c)

~~~diff
- 00b58b74 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b58b74 ["RETURN", null, ["register:0:8"]]
- 00b58b74 bytes c0035fd6
+ 00b58f9c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b58f9c ["RETURN", null, ["register:0:8"]]
+ 00b58f9c bytes c0035fd6
- 00b58b44 ["INT_ADD", "register:40f0:8", ["const:b58b44:8", "const:4:8"]]
- 00b58b44 ["CALL", null, ["callee:00c5b3c0:8"]]
+ 00b58f6c ["INT_ADD", "register:40f0:8", ["const:b58f6c:8", "const:4:8"]]
+ 00b58f6c ["CALL", null, ["callee:00c5b3c0:8"]]
- 00b58b44 bytes 1f090494
+ 00b58f6c bytes 15090494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb1b58af934d3fc25571f2147c264948"></a>

### [`00b59cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59cb0.md) → [`00b5a0d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5a0d8.md) _ZN8firebase10app_common15LibraryRegistry15UpdateUserAgentEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b310.md) · 呼出先 5件 [`00b5a78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c5b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3f0.md)
- 新版 呼出元 1件 [`00c5b710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b710.md) · 呼出先 5件 [`00b5abb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5abb4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c5b7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b7f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 62.50% / 新版 60.34%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59cdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5a104"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b59ce4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b59cdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b59ce4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5a118"
      ]
    ],
    [
      "unmatched:00b59d24",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5a15c"
      ]
    ]
  ],
  "added": [
    [
      "00b5a104",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b5a10c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5a118"
      ]
    ],
    [
      "00b5a14c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5a15c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b59cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59cb0.md#insn-00b59cdc) · [`00b59ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59cb0.md#insn-00b59ce4) · [`00b59d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b59/00b59cb0.md#insn-00b59d30)

~~~diff
- 00b59cdc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b59cdc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 00b59cdc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b59cdc bytes a8831bf8
- 00b59ce4 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b59ce4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b59ce4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b59ce4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b59ce4 bytes 68000037
- 00b59d30 ["CBRANCH", null, ["local:b23:8", "register:101:1"]]
- 00b59d30 bytes 60090054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2ea69ae83ddf226dd42be68d6bd3dd9"></a>

### [`00b5a874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a874.md) → [`00b5ac9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5ac9c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3f0.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5b7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b7f0.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 53.85% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a8b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5acdc"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a874.md#insn-00b5a8b4) · [`00b5a884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a874.md#insn-00b5a884)
- 新版 [`00b5acdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5ac9c.md#insn-00b5acdc)

~~~diff
- 00b5a8b4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b5a8b4 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b5a8b4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b5a8b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b5a8b4 bytes 5715819a
+ 00b5acdc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b5acdc ["COPY", "tmp:1:8", ["register:4050:8"]]
+ 00b5acdc ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00b5acdc ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
+ 00b5acdc bytes 5715819a
- 00b5a884 ["COPY", "tmp:0:8", ["const:30:8"]]
- 00b5a884 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 00b5a884 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 00b5a884 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 00b5a884 bytes fdc30091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f948365b94d1c889b50db071818dbc1"></a>

### [`00b5aebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5aebc.md) → [`00b5b2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b2e4.md) _ZNK8firebase10LoggerBase17FilterLogMessageVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5aee8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5b310"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5af34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5aee8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5af34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5b378"
      ]
    ]
  ],
  "added": [
    [
      "00b5b310",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b5b35c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5b378"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5aee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5aebc.md#insn-00b5aee8) · [`00b5af34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5aebc.md#insn-00b5af34) · [`00b5af4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5aebc.md#insn-00b5af4c)

~~~diff
- 00b5aee8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b5aee8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5aee8 bytes e81700f9
- 00b5af34 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b5af34 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b5af34 bytes e1000054
- 00b5af4c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b5af4c ["RETURN", null, ["register:0:8"]]
- 00b5af4c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0555ee6a848e2c22c8049fde781a584"></a>

### [`00b5af54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5af54.md) → [`00b5b37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b37c.md) _ZNK8firebase10LoggerBase7LogInfoEPKcz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 46.15% / 新版 46.15%

CFGの説明率　旧版 60.00% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 27件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5af58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5af58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5af5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5af58",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5af5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5af60",
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
      "00b5b380",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5b384",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5b388",
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

- 旧版 [`00b5af58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5af54.md#insn-00b5af58) · [`00b5af5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5af54.md#insn-00b5af5c) · [`00b5af60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5af54.md#insn-00b5af60)

~~~diff
- 00b5af58 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b5af58 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5af58 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00b5af58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5af58 bytes fc5712a9
- 00b5af5c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5af5c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5af5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00b5af5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5af5c bytes f44f13a9
- 00b5af60 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5af60 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5af60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00b5af60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5af60 bytes fd7b14a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-767f05c493dd9e7ce1ef309cdefb3956"></a>

### [`00b5b024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b024.md) → [`00b5b44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b44c.md) _ZNK8firebase10LoggerBase10LogWarningEPKcz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.85% / 新版 53.85%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b078"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b07c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b07c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5b078",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5b07c",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5b080",
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
      "00b5b4a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b5b4a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "00b5b4a8",
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

- 旧版 [`00b5b078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b024.md#insn-00b5b078) · [`00b5b07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b024.md#insn-00b5b07c) · [`00b5b080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b024.md#insn-00b5b080)

~~~diff
- 00b5b078 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b5b078 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b5b078 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b5b078 bytes ab831df8
- 00b5b07c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b5b07c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b5b07c ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffff90:8"]]
- 00b5b07c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b07c bytes a92339a9
- 00b5b080 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00b5b080 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b5b080 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b5b080 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b080 bytes ac2b3aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-077f17c30e78d80ff41c7639bcc92047"></a>

### [`00b5b1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b1c4.md) → [`00b5b5ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b5ec.md) _ZNK8firebase10LoggerBase9LogAssertEPKcz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.77% / 新版 55.77%

CFGの説明率　旧版 22.22% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b1dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b1dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b1e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5b1dc",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5b1e0",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5b1e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x150]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5b604",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "00b5b608",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ],
    [
      "00b5b60c",
      "WRITE",
      [
        "storage",
        "Stack[-0x150]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b1c4.md#insn-00b5b1dc) · [`00b5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b1c4.md#insn-00b5b1e0) · [`00b5b1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b1c4.md#insn-00b5b1e4)

~~~diff
- 00b5b1dc ["COPY", "tmp:0:8", ["register:4020:8"]]
- 00b5b1dc ["COPY", "tmp:1:8", ["register:4028:8"]]
- 00b5b1dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00b5b1dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b1dc bytes e41709a9
- 00b5b1e0 ["COPY", "tmp:0:8", ["register:4030:8"]]
- 00b5b1e0 ["COPY", "tmp:1:8", ["register:4038:8"]]
- 00b5b1e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00b5b1e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b1e0 bytes e61f0aa9
- 00b5b1e4 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b5b1e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b5b1e4 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b5b1e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00b5b1e4 bytes e00700ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8e364195f2ba4f056e99b014a73f08f"></a>

### [`00b5bfcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bfcc.md) → [`00b5c3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c3f4.md) _ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEED2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.10% / 新版 87.10%

CFGの説明率　旧版 66.67% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5bff0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5c418"
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
      "unmatched:00b5bfe4",
      "READ",
      [
        "storage",
        "00c9b388",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b5bff0",
      "DATA",
      [
        "storage",
        "00c8ff18",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00b5c40c",
      "READ",
      [
        "storage",
        "00c9b788",
        null,
        "pointer"
      ]
    ],
    [
      "00b5c418",
      "DATA",
      [
        "storage",
        "00c90318",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5bff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bfcc.md#insn-00b5bff0) · [`00b5bfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bfcc.md#insn-00b5bfe4)
- 新版 [`00b5c418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c3f4.md#insn-00b5c418)

~~~diff
- 00b5bff0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b5bff0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5bff0 bytes 080000f9
+ 00b5c418 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00b5c418 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b5c418 bytes 080000f9
- 00b5bfe4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:388:8"]]
- 00b5bfe4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5bfe4 bytes 08c541f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-461188a8269d3d2f2cfd4604e1899094"></a>

### [`00b5c0cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c0cc.md) → [`00b5c4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c4f4.md) _ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEE16__on_zero_sharedEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b5b884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b884.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00b5bcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5bcac.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 25.00% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c0cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c0d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c0d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5c0cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c0d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c0d4",
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
      "00b5c4f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5c4f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5c4fc",
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

- 旧版 [`00b5c0cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c0cc.md#insn-00b5c0cc) · [`00b5c0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c0cc.md#insn-00b5c0d0) · [`00b5c0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c0cc.md#insn-00b5c0d4)

~~~diff
- 00b5c0cc ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b5c0cc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b5c0cc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5c0cc bytes f50f1df8
- 00b5c0d0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5c0d0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5c0d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5c0d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c0d0 bytes f44f01a9
- 00b5c0d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5c0d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5c0d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5c0d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c0d4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcbc76fdcbf0ca8a5735c1b08a50b81a"></a>

### [`00b5c7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c7a0.md) → [`00b5cbc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5cbc8.md) _ZN8firebase15CleanupNotifier15UnregisterOwnerEPS0_Pv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5b7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5bba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bba0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 32.26% / 新版 32.26%

CFGの説明率　旧版 27.78% / 新版 17.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c7a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c7a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c7a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5c7a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c7a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c7b0",
      "READ",
      [
        "storage",
        "00c9b398",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5cbc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5cbcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b5cbd8",
      "READ",
      [
        "storage",
        "00c9b798",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c7a0.md#insn-00b5c7a0) · [`00b5c7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c7a0.md#insn-00b5c7a4) · [`00b5c7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5c7a0.md#insn-00b5c7c0)

~~~diff
- 00b5c7a0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5c7a0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5c7a0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b5c7a0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5c7a0 bytes f44fbea9
- 00b5c7a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5c7a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5c7a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5c7a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c7a4 bytes fd7b01a9
- 00b5c7c0 ["INT_ADD", "register:40f0:8", ["const:b5c7c0:8", "const:4:8"]]
- 00b5c7c0 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5c7c0 bytes 90f70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fc4f26859ab7d6fdb5d63e992f7da0d"></a>

### [`00b5cc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5cc80.md) → [`00b5d0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d0a8.md) _ZN8firebase4PathC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bbf0.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 20.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5cc80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5cc80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5d0a8"
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
      "unmatched:00b5cc80",
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
      "00b5d0a8",
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

- 旧版 [`00b5cc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5cc80.md#insn-00b5cc80) · [`00b5cc84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5cc80.md#insn-00b5cc84)
- 新版 [`00b5d0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d0a8.md#insn-00b5d0a8)

~~~diff
- 00b5cc80 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5cc80 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5cc80 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00b5cc80 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5cc80 bytes fd7bbfa9
+ 00b5d0a8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00b5d0a8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00b5d0a8 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00b5d0a8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b5d0a8 bytes fd7bbfa9
- 00b5cc84 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00b5cc84 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff46acec7396eebb87e94269ee40434c"></a>

### [`00b5d488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d488.md) → [`00b5d8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d8b0.md) _ZN8firebase4Path8MakePathERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

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
      "site": "00b5d49c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5d8c4"
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
      "unmatched:00b5d49c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d8e8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d8c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d8e8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d488.md#insn-00b5d49c) · [`00b5d4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d488.md#insn-00b5d4a0)
- 新版 [`00b5d8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d8b0.md#insn-00b5d8c4)

~~~diff
- 00b5d49c ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00b5d49c bytes 20010054
+ 00b5d8c4 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00b5d8c4 bytes 20010054
- 00b5d4a0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b5d4a0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b5d4a0 ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
- 00b5d4a0 bytes 09004039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a311c507094742ccd436ccc711204c2"></a>

### [`00b5d4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d4c8.md) → [`00b5d8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d8f0.md) _ZNK8firebase4Path11GetBaseNameEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 69.57% / 新版 69.57%

CFGの説明率　旧版 38.10% / 新版 42.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d4d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d4f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d51c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5d4d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d910"
      ]
    ],
    [
      "unmatched:00b5d4f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d90c"
      ]
    ]
  ],
  "added": [
    [
      "00b5d900",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d910"
      ]
    ],
    [
      "00b5d920",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d90c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d4c8.md#insn-00b5d4d8) · [`00b5d4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d4c8.md#insn-00b5d4f8) · [`00b5d51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d4c8.md#insn-00b5d51c)

~~~diff
- 00b5d4d8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b5d4d8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b5d4d8 bytes 880000b5
- 00b5d4f8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b5d4f8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b5d4f8 bytes 61ffff54
- 00b5d51c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b5d51c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b5d51c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:1:8"]]
- 00b5d51c ["COPY", "register:4000:8", ["tmp:0:8"]]
- 00b5d51c bytes 20058a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-772cc7ba856b4f2b09f714683063dc81"></a>

### [`00b5d8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d8f4.md) → [`00b5dd1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5dd1c.md) _ZNK8firebase4Path14FrontDirectoryEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5b7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7f0.md) [`00c5b800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b800.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5bbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bbf0.md) [`00c5bc00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bc00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 53.33% / 新版 69.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d8f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d8fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d8fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5d8f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5d8fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5d900",
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
      "00b5dd20",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5dd24",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5dd28",
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

- 旧版 [`00b5d8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d8f4.md#insn-00b5d8f8) · [`00b5d8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d8f4.md#insn-00b5d8fc) · [`00b5d900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d8f4.md#insn-00b5d900)

~~~diff
- 00b5d8f8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b5d8f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b5d8f8 bytes f51300f9
- 00b5d8fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5d8fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5d8fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b5d8fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5d8fc bytes f44f03a9
- 00b5d900 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5d900 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5d900 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b5d900 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5d900 bytes fd7b04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d47f013a81280edba53eccf71301c4d"></a>

### [`00b5dde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5dde0.md) → [`00b5e208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5e208.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertINS_11__wrap_iterIPKcEEEENS_9enable_ifIXaasr21__is_forward_iterator

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b810.md) · 呼出先 7件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md)
- 新版 呼出元 1件 [`00c5bc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bc10.md) · 呼出先 7件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.00% / 新版 94.00%

CFGの説明率　旧版 75.00% / 新版 70.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e08c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e08c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5e4b4"
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
      "unmatched:00b5e094",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b5e080"
      ]
    ],
    [
      "unmatched:00b5e09c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e4d8"
      ]
    ]
  ],
  "added": [
    [
      "00b5e4bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e4a8"
      ]
    ],
    [
      "00b5e4c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e4d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5e08c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5dde0.md#insn-00b5e08c) · [`00b5e094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5dde0.md#insn-00b5e094) · [`00b5e09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5dde0.md#insn-00b5e09c)

~~~diff
- 00b5e08c ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:fffffffffffffff0:8"]]
- 00b5e08c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b5e08c ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b5e08c ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00b5e08c bytes 80853fad
- 00b5e094 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b5e094 ["CBRANCH", null, ["local:b48:8", "tmp:0:1"]]
- 00b5e094 bytes 61ffff54
- 00b5e09c ["CBRANCH", null, ["local:b51:8", "register:101:1"]]
- 00b5e09c bytes a0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b140305c421c0626d9371ee0c64d367"></a>

### [`00b5e100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e100.md) → [`00b5e528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5e528.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7reserveEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c581f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581f0.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c585f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585f0.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.81% / 新版 94.81%

CFGの説明率　旧版 72.97% / 新版 67.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e190"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5e5b8"
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
      "unmatched:00b5e190",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e588"
      ]
    ]
  ],
  "added": [
    [
      "00b5e5b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e588"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5e190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e100.md#insn-00b5e190) · [`00b5e11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e100.md#insn-00b5e11c)
- 新版 [`00b5e5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5e528.md#insn-00b5e5b8) · [`00b5e544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5e528.md#insn-00b5e544)

~~~diff
- 00b5e190 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b5e190 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b5e190 bytes 81feff54
+ 00b5e5b8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b5e5b8 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b5e5b8 bytes 81feff54
- 00b5e11c ["CBRANCH", null, ["local:b25:8", "register:102:1"]]
+ 00b5e544 ["CBRANCH", null, ["local:b28:8", "register:102:1"]]
- 00b5e11c bytes a2080054
+ 00b5e544 bytes a2080054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00e89e39561eb71c39bcc32e3e050281"></a>

### [`00b5f52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f52c.md) → [`00b5f954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5f954.md) _ZN8firebase26ReferenceCountedFutureImpl11RunCallbackEPNS_10FutureBaseEPFvRKS1_PvES5_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f52c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f530"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f530"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5f52c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5f530",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5f534",
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
      "00b5f954",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b5f958",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5f95c",
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

- 旧版 [`00b5f52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f52c.md#insn-00b5f52c) · [`00b5f530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f52c.md#insn-00b5f530) · [`00b5f534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f52c.md#insn-00b5f534)

~~~diff
- 00b5f52c ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00b5f52c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b5f52c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5f52c bytes f70f1cf8
- 00b5f530 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5f530 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5f530 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5f530 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5f530 bytes f65701a9
- 00b5f534 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5f534 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5f534 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5f534 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5f534 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80271bd17ddb8f226c02815429185fd0"></a>

### [`00b5f634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f634.md) → [`00b5fa5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5fa5c.md) _ZN8firebase26ReferenceCountedFutureImpl15ReferenceFutureERKNS_12FutureHandleE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 72.73% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f684"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5faac"
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
      "unmatched:00b5f684",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5fa98"
      ]
    ]
  ],
  "added": [
    [
      "00b5faac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5fa98"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5f684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f634.md#insn-00b5f684) · [`00b5f654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f634.md#insn-00b5f654)
- 新版 [`00b5faac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5fa5c.md#insn-00b5faac) · [`00b5fa7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5fa5c.md#insn-00b5fa7c)

~~~diff
- 00b5f684 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b5f684 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5f684 bytes 69ffffb5
+ 00b5faac ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00b5faac ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b5faac bytes 69ffffb5
- 00b5f654 ["INT_ADD", "register:40f0:8", ["const:b5f654:8", "const:4:8"]]
- 00b5f654 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b5fa7c ["INT_ADD", "register:40f0:8", ["const:b5fa7c:8", "const:4:8"]]
+ 00b5fa7c ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5f654 bytes ebeb0394
+ 00b5fa7c bytes e1eb0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a60da0e6c46b7ba571706854e555163"></a>

### [`00b5f944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f944.md) → [`00b5fd6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5fd6c.md) _ZNK8firebase26ReferenceCountedFutureImpl21GetFutureErrorMessageERKNS_12FutureHandleE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 70.59% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f944"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f948"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f948"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5f944",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5f948",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5f94c",
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
      "00b5fd6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5fd70",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5fd74",
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

- 旧版 [`00b5f944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f944.md#insn-00b5f944) · [`00b5f948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f944.md#insn-00b5f948) · [`00b5f94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f944.md#insn-00b5f94c)

~~~diff
- 00b5f944 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b5f944 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b5f944 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5f944 bytes f50f1df8
- 00b5f948 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5f948 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5f948 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5f948 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5f948 bytes f44f01a9
- 00b5f94c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5f94c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5f94c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5f94c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5f94c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89109606e289d72c50c6e32deda9c7f7"></a>

### [`00b5fc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5fc68.md) → [`00b60090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60090.md) _ZN8firebase26ReferenceCountedFutureImpl24RemoveCompletionCallbackERKNS_12FutureHandleENS_6detail24CompletionCallbackHandleE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 99.20% / 新版 99.20%

CFGの説明率　旧版 52.83% / 新版 60.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5fcd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b60100"
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
      "unmatched:00b5fcd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b60110"
      ]
    ]
  ],
  "added": [
    [
      "00b60100",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b60110"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5fcd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5fc68.md#insn-00b5fcd8) · [`00b5fca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5fc68.md#insn-00b5fca0)
- 新版 [`00b60100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60090.md#insn-00b60100) · [`00b600c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60090.md#insn-00b600c8)

~~~diff
- 00b5fcd8 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00b5fcd8 bytes 80000054
+ 00b60100 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 00b60100 bytes 80000054
- 00b5fca0 ["INT_ADD", "register:40f0:8", ["const:b5fca0:8", "const:4:8"]]
- 00b5fca0 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b600c8 ["INT_ADD", "register:40f0:8", ["const:b600c8:8", "const:4:8"]]
+ 00b600c8 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5fca0 bytes 58ea0394
+ 00b600c8 bytes 4eea0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c22e92527e850da2bab902089913b3e6"></a>

### [`00b60938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60938.md) → [`00b60d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60d60.md) _ZN8firebase26ReferenceCountedFutureImpl18ForceReleaseFutureERKNS_12FutureHandleE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b8c0.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 1件 [`00c5bcc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bcc0.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.43% / 新版 80.43%

CFGの説明率　旧版 18.75% / 新版 21.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60938"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60938"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6093c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b60938",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6093c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b60940",
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
      "00b60d60",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b60d64",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b60d68",
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

- 旧版 [`00b60938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60938.md#insn-00b60938) · [`00b6093c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60938.md#insn-00b6093c) · [`00b60940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60938.md#insn-00b60940)

~~~diff
- 00b60938 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b60938 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b60938 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b60938 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b60938 bytes f657bda9
- 00b6093c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6093c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6093c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6093c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6093c bytes f44f01a9
- 00b60940 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b60940 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b60940 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b60940 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b60940 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-866c280b785a81892d3b19bc869ec053"></a>

### [`00b609f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b609f0.md) → [`00b60e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60e18.md) _ZN8firebase26ReferenceCountedFutureImpl12MarkOrphanedEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

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
      "site": "00b609f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b609f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b609f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b609f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b609f4",
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
      "00b60e18",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b60e1c",
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

- 旧版 [`00b609f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b609f0.md#insn-00b609f0) · [`00b609f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b609f0.md#insn-00b609f4)
- 新版 [`00b60e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60e18.md#insn-00b60e18)

~~~diff
- 00b609f0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b609f0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b609f0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b609f0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b609f0 bytes f44fbea9
- 00b609f4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b609f4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b609f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b609f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b609f4 bytes fd7b01a9
+ 00b60e18 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00b60e18 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00b60e18 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00b60e18 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b60e18 bytes f44fbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b839e259424f40c020d25e15b1d7fc74"></a>

### [`00b60a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a2c.md) → [`00b60e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60e54.md) _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) · 呼出先 2件 [`00b60a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a84.md) [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md)
- 新版 呼出元 1件 [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) · 呼出先 2件 [`00b60eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60eac.md) [`00c5ac00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 50.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b60e8c",
      "PARAM",
      [
        "storage",
        "00b60a84",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b60e8c",
      "PARAM",
      [
        "storage",
        "00b60eac",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a2c.md#insn-00b60a3c) · [`00b60a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a2c.md#insn-00b60a54) · [`00b60a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a2c.md#insn-00b60a64)
- 新版 [`00b60e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60e54.md#insn-00b60e64) · [`00b60e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60e54.md#insn-00b60e7c) · [`00b60e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60e54.md#insn-00b60e8c)

~~~diff
- 00b60a3c ["INT_EQUAL", "tmp:0:1", ["register:4010:8", "const:0:8"]]
- 00b60a3c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b60e64 ["INT_EQUAL", "tmp:0:1", ["register:4010:8", "const:0:8"]]
+ 00b60e64 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b60a3c bytes e20100b4
+ 00b60e64 bytes e20100b4
- 00b60a54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b60a54 ["INT_ADD", "register:40f0:8", ["const:b60a54:8", "const:4:8"]]
- 00b60a54 ["CALLIND", null, ["register:0:8"]]
+ 00b60e7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b60e7c ["INT_ADD", "register:40f0:8", ["const:b60e7c:8", "const:4:8"]]
+ 00b60e7c ["CALLIND", null, ["register:0:8"]]
- 00b60a54 bytes 00013fd6
+ 00b60e7c bytes 00013fd6
- 00b60a64 ["COPY", "register:4010:8", ["const:b60a84:8"]]
+ 00b60e8c ["COPY", "register:4010:8", ["const:b60eac:8"]]
- 00b60a64 bytes 02010010
+ 00b60e8c bytes 02010010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0a9ad582126fcd4dcd0af4ef42d9e75"></a>

### [`00b60adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60adc.md) → [`00b60f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60f04.md) _ZN8firebase12FutureHandleC1ERKS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) · 呼出先 2件 [`00b60a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a84.md) [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md)
- 新版 呼出元 1件 [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) · 呼出先 2件 [`00b60eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60eac.md) [`00c5ac00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 66.67% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b60f44",
      "PARAM",
      [
        "storage",
        "00b60a84",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b60f44",
      "PARAM",
      [
        "storage",
        "00b60eac",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60adc.md#insn-00b60afc) · [`00b60b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60adc.md#insn-00b60b0c) · [`00b60b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60adc.md#insn-00b60b1c)
- 新版 [`00b60f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60f04.md#insn-00b60f24) · [`00b60f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60f04.md#insn-00b60f34) · [`00b60f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60f04.md#insn-00b60f44)

~~~diff
- 00b60afc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b60afc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b60f24 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b60f24 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b60afc bytes a00100b4
+ 00b60f24 bytes a00100b4
- 00b60b0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b60b0c ["INT_ADD", "register:40f0:8", ["const:b60b0c:8", "const:4:8"]]
- 00b60b0c ["CALLIND", null, ["register:0:8"]]
+ 00b60f34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b60f34 ["INT_ADD", "register:40f0:8", ["const:b60f34:8", "const:4:8"]]
+ 00b60f34 ["CALLIND", null, ["register:0:8"]]
- 00b60b0c bytes 00013fd6
+ 00b60f34 bytes 00013fd6
- 00b60b1c ["COPY", "register:4010:8", ["const:b60a84:8"]]
+ 00b60f44 ["COPY", "register:4010:8", ["const:b60eac:8"]]
- 00b60b1c bytes 42fbff10
+ 00b60f44 bytes 42fbff10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-272d0b51815d54a0a10c848320ace6b0"></a>

### [`00b60ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60ef8.md) → [`00b61320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b61320.md) FUN_00b61320

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b5e8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e8a8.md) · 呼出先 4件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6a0.md) [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)
- 新版 呼出元 1件 [`00b5ecd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5ecd0.md) · 呼出先 4件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5aaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aaa0.md) [`00c5ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 28.57% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60f74"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b6139c"
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
      "unmatched:00b60f74",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6139c",
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

- 旧版 [`00b60f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60ef8.md#insn-00b60f74) · [`00b60f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60ef8.md#insn-00b60f0c)
- 新版 [`00b6139c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b61320.md#insn-00b6139c) · [`00b61334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b61320.md#insn-00b61334)

~~~diff
- 00b60f74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b60f74 ["INT_ADD", "register:40f0:8", ["const:b60f74:8", "const:4:8"]]
- 00b60f74 ["CALLIND", null, ["register:0:8"]]
- 00b60f74 bytes 00013fd6
+ 00b6139c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6139c ["INT_ADD", "register:40f0:8", ["const:b6139c:8", "const:4:8"]]
+ 00b6139c ["CALLIND", null, ["register:0:8"]]
+ 00b6139c bytes 00013fd6
- 00b60f0c ["INT_ADD", "register:40f0:8", ["const:b60f0c:8", "const:4:8"]]
- 00b60f0c ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b61334 ["INT_ADD", "register:40f0:8", ["const:b61334:8", "const:4:8"]]
+ 00b61334 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b60f0c bytes bde50394
+ 00b61334 bytes b3e50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ead915b3fc32761020a968ffecacdc7a"></a>

### [`00b60f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60f88.md) → [`00b613b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b613b0.md) _INIT_282

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b60a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a8c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b60eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60eb4.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60fa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60fa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b613c8"
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
      "unmatched:00b60f90",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b60f90",
      "PARAM",
      [
        "storage",
        "01125c18",
        "_ZN8firebase26ReferenceCountedFutureImpl14kInvalidHandleE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b60f94",
      "READ",
      [
        "storage",
        "00c9b3a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b613b8",
      "READ",
      [
        "storage",
        "00c9b7a8",
        null,
        "pointer"
      ]
    ],
    [
      "00b613b8",
      "PARAM",
      [
        "storage",
        "01126018",
        "_ZN8firebase26ReferenceCountedFutureImpl14kInvalidHandleE",
        "undefined8"
      ]
    ],
    [
      "00b613bc",
      "READ",
      [
        "storage",
        "00c9b7a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60f88.md#insn-00b60fa0) · [`00b60f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60f88.md#insn-00b60f88)
- 新版 [`00b613c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b613b0.md#insn-00b613c8)

~~~diff
- 00b60fa0 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b60fa0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b60fa0 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b60fa0 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b60fa0 bytes 3f7c00a9
+ 00b613c8 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 00b613c8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b613c8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00b613c8 ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 00b613c8 bytes 3f7c00a9
- 00b60f88 ["COPY", "register:4008:8", ["const:c9b000:8"]]
- 00b60f88 bytes c10900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c998a875364b21220fba9872e3aefa80"></a>

### [`00b60fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60fa8.md) → [`00b613d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b613d0.md) _ZN8firebase17ModuleInitializerC1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a840.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac40.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b613e8",
      "incomplete_value": true,
      "site": "00b613ec",
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
      "definition_site": "00b60fc0",
      "incomplete_value": true,
      "site": "00b60fc4",
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
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61008"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b61430"
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
      "00b613e0",
      "READ",
      [
        "storage",
        "00c9b3e8",
        null,
        "pointer"
      ]
    ],
    [
      "00b613ec",
      "DATA",
      [
        "storage",
        "00c900d8",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00b613e0",
      "READ",
      [
        "storage",
        "00c9b7e8",
        null,
        "pointer"
      ]
    ],
    [
      "00b613ec",
      "DATA",
      [
        "storage",
        "00c904d8",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60fa8.md#insn-00b61008) · [`00b60fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60fa8.md#insn-00b60fb0)
- 新版 [`00b61430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b613d0.md#insn-00b61430)

~~~diff
- 00b61008 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b61008 ["RETURN", null, ["register:0:8"]]
- 00b61008 bytes c0035fd6
+ 00b61430 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b61430 ["RETURN", null, ["register:0:8"]]
+ 00b61430 bytes c0035fd6
- 00b60fb0 ["COPY", "tmp:0:8", ["const:10:8"]]
- 00b60fb0 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 00b60fb0 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 00b60fb0 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 00b60fb0 bytes fd430091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c755aab27a417d3ed371aaa88646230"></a>

### [`00b6100c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b6100c.md) → [`00b61434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b61434.md) _ZN8firebase17ModuleInitializerD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a850.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ac50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 79.17% / 新版 79.17%

CFGの説明率　旧版 50.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6102c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b61454"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61030"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61020",
      "READ",
      [
        "storage",
        "00c9b3e8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b6102c",
      "DATA",
      [
        "storage",
        "00c900d8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "unmatched:00b61030",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61484"
      ]
    ]
  ],
  "added": [
    [
      "00b61448",
      "READ",
      [
        "storage",
        "00c9b7e8",
        null,
        "pointer"
      ]
    ],
    [
      "00b61454",
      "DATA",
      [
        "storage",
        "00c904d8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00b61458",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61484"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6102c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b6100c.md#insn-00b6102c) · [`00b61030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b6100c.md#insn-00b61030)
- 新版 [`00b61454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b61434.md#insn-00b61454)

~~~diff
- 00b6102c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b6102c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b6102c bytes 080000f9
- 00b61030 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00b61030 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b61030 bytes 740100b4
+ 00b61454 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00b61454 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b61454 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f5e6f12257b51e77558144df5f6cc82"></a>

### [`00b6106c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b6106c.md) → [`00b61494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b61494.md) _ZN8firebase17ModuleInitializerD0Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a850.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ac50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 79.17% / 新版 79.17%

CFGの説明率　旧版 14.29% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6108c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b614b4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61090"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61080",
      "READ",
      [
        "storage",
        "00c9b3e8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b6108c",
      "DATA",
      [
        "storage",
        "00c900d8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "unmatched:00b61090",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b614e4"
      ]
    ]
  ],
  "added": [
    [
      "00b614a8",
      "READ",
      [
        "storage",
        "00c9b7e8",
        null,
        "pointer"
      ]
    ],
    [
      "00b614b4",
      "DATA",
      [
        "storage",
        "00c904d8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00b614b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b614e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6108c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b6106c.md#insn-00b6108c) · [`00b61090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b6106c.md#insn-00b61090)
- 新版 [`00b614b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b61494.md#insn-00b614b4)

~~~diff
- 00b6108c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b6108c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b6108c bytes 080000f9
- 00b61090 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00b61090 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b61090 bytes 740100b4
+ 00b614b4 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00b614b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b614b4 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e785ae27acca53dcdcdfbfcf21325038"></a>

### [`00b62178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62178.md) → [`00b625a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b625a0.md) _ZN8firebase11SplitStringERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md) [`00c5b250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b250.md) [`00c5b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3f0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md) [`00c5b650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b650.md) [`00c5b7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b7f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.48% / 新版 73.48%

CFGの説明率　旧版 52.38% / 新版 53.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62280"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62284"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62288"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b62228",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b62714"
      ]
    ],
    [
      "unmatched:00b62264",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b7f0"
      ]
    ],
    [
      "unmatched:00b62270",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b62298"
      ]
    ]
  ],
  "added": [
    [
      "00b62650",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b62714"
      ]
    ],
    [
      "00b6268c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b7f0"
      ]
    ],
    [
      "00b62698",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b626c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62178.md#insn-00b62220) · [`00b62228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62178.md#insn-00b62228) · [`00b62270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62178.md#insn-00b62270)

~~~diff
- 00b62220 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b62220 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b62220 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b62220 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b62220 bytes 4801899a
- 00b62228 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b62228 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b62228 ["CBRANCH", null, ["local:b20:8", "tmp:1:1"]]
- 00b62228 bytes 29060054
- 00b62270 ["CBRANCH", null, ["local:b13:8", "register:102:1"]]
- 00b62270 bytes 42010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

