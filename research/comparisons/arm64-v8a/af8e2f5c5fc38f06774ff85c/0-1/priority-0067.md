# v15.7.2 → v15.7.3 · 最優先の変更候補 (67)

[一覧の目次](README.md)

<a id="compare-0a8cea5fd74529b2cfaf08a1db9e14f7"></a>

### [`00b4ab1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ab1c.md) → [`00b4abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4abe4.md) _ZN8firebase9messaging18firebase_messaging15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 62.96% / 新版 62.96%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ab74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4ac3c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ab5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4abf8",
      "READ",
      [
        "storage",
        "010a0f00",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ac04",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4ab78"
      ]
    ],
    [
      "unmatched:00b4ab50",
      "READ",
      [
        "storage",
        "010a0ef8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4abf8",
      "READ",
      [
        "storage",
        "010a0fc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ac04",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4ac40"
      ]
    ],
    [
      "00b4ac18",
      "READ",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ab5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ab1c.md#insn-00b4ab5c) · [`00b4ab68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ab1c.md#insn-00b4ab68) · [`00b4ab74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ab1c.md#insn-00b4ab74)
- 新版 `00b4ac30`（命令位置の公開資料なし）

~~~diff
- 00b4ab5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4ab5c ["INT_ADD", "register:40f0:8", ["const:b4ab5c:8", "const:4:8"]]
- 00b4ab5c ["CALLIND", null, ["register:0:8"]]
- 00b4ab5c bytes 00013fd6
- 00b4ab68 ["INT_ADD", "register:40f0:8", ["const:b4ab68:8", "const:4:8"]]
- 00b4ab68 ["CALL", null, ["callee:00bde090:8"]]
+ 00b4ac30 ["INT_ADD", "register:40f0:8", ["const:b4ac30:8", "const:4:8"]]
+ 00b4ac30 ["CALL", null, ["callee:00bde090:8"]]
- 00b4ab68 bytes 1e4d0294
+ 00b4ac30 bytes 184d0294
- 00b4ab74 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4ab74 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:f00:8"]]
- 00b4ab74 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4ab74 bytes a0023c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4a3a3bba09c57ddc1f974c2d5ebe559"></a>

### [`00b4ab88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ab88.md) → [`00b4ac50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ac50.md) _ZN8firebase9messaging18firebase_messaging12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 32.14% / 新版 32.14%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ab88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ab8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ab8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4ab88",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4ab8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4ab90",
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
      "00b4ac50",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4ac54",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4ac58",
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

- 旧版 [`00b4ab88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ab88.md#insn-00b4ab88) · [`00b4ab8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ab88.md#insn-00b4ab8c) · [`00b4ab90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ab88.md#insn-00b4ab90)

~~~diff
- 00b4ab88 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b4ab88 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b4ab88 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4ab88 bytes f50f1df8
- 00b4ab8c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4ab8c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4ab8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4ab8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4ab8c bytes f44f01a9
- 00b4ab90 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4ab90 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4ab90 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b4ab90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4ab90 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9620b14275c85371f9dd43e126877f1d"></a>

### [`00b4abf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4abf8.md) → [`00b4acc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4acc0.md) _ZN8firebase9messaging18firebase_messaging14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4abf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4abf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4abfc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4abf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4abfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4ac0c",
      "READ",
      [
        "storage",
        "010a0ef8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4acc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4acc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4acd4",
      "READ",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4abf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4abf8.md#insn-00b4abf8) · [`00b4abfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4abf8.md#insn-00b4abfc) · [`00b4ac14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4abf8.md#insn-00b4ac14)

~~~diff
- 00b4abf8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4abf8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4abf8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4abf8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4abf8 bytes f44fbea9
- 00b4abfc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4abfc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4abfc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4abfc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4abfc bytes fd7b01a9
- 00b4ac14 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4ac14 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b4ac14 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf8e070b1bb2d84c8b45f65bc644c425"></a>

### [`00b4aca4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aca4.md) → [`00b4ad6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ad6c.md) _ZN8firebase9messaging18firebase_messaging13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aca4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aca4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aca8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4aca4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4aca8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4acb8",
      "READ",
      [
        "storage",
        "010a0ef8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ad6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4ad70",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4ad80",
      "READ",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aca4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aca4.md#insn-00b4aca4) · [`00b4aca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aca4.md#insn-00b4aca8) · [`00b4acc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aca4.md#insn-00b4acc0)

~~~diff
- 00b4aca4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4aca4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4aca4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4aca4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4aca4 bytes f44fbea9
- 00b4aca8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4aca8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4aca8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4aca8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4aca8 bytes fd7b01a9
- 00b4acc0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4acc0 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b4acc0 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d97c63f0c1b6f7b026971139d9327c6"></a>

### [`00b4ad50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ad50.md) → [`00b4ae18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ae18.md) _ZN8firebase9messaging27registration_intent_service19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ad7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4ae44"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4ae2c",
      "incomplete_value": true,
      "site": "00b4ae2c",
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
      "definition_site": "00b4ad64",
      "incomplete_value": true,
      "site": "00b4ad64",
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
      "00b4ae28",
      "READ",
      [
        "storage",
        "010a0f58",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4ad70",
      "PARAM",
      [
        "storage",
        "002a8e9a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4ad74",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b4ae28",
      "READ",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ae38",
      "PARAM",
      [
        "storage",
        "002a8e06",
        null,
        "string"
      ]
    ],
    [
      "00b4ae3c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ad64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ad50.md#insn-00b4ad64) · [`00b4ad74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ad50.md#insn-00b4ad74) · [`00b4ad7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ad50.md#insn-00b4ad7c)
- 新版 `00b4ae2c`（命令位置の公開資料なし）

~~~diff
- 00b4ad64 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4ad64 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b4ae2c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4ae2c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4ad64 bytes e80000b5
+ 00b4ae2c bytes e80000b5
- 00b4ad74 ["INT_ADD", "register:40f0:8", ["const:b4ad74:8", "const:4:8"]]
- 00b4ad74 ["CALL", null, ["callee:00bde040:8"]]
- 00b4ad74 bytes 874c0294
- 00b4ad7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f58:8"]]
- 00b4ad7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ad7c bytes 60ae07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be0b633af0e3bcc155381f7dbcb930ee"></a>

### [`00b4ad90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ad90.md) → [`00b4ae58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ae58.md) _ZN8firebase9messaging27registration_intent_service19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ad90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ad94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ad94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4ad90",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4ad94",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4ae68",
      "READ",
      [
        "storage",
        "010a0f58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ae58",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4ae5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4ae68",
      "READ",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ad90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ad90.md#insn-00b4ad90) · [`00b4ad94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ad90.md#insn-00b4ad94) · [`00b4adb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ad90.md#insn-00b4adb4)

~~~diff
- 00b4ad90 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4ad90 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4ad90 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4ad90 bytes f30f1ef8
- 00b4ad94 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4ad94 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4ad94 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4ad94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4ad94 bytes fd7b01a9
- 00b4adb4 ["INT_ADD", "register:40f0:8", ["const:b4adb4:8", "const:4:8"]]
- 00b4adb4 ["CALL", null, ["callee:00bde040:8"]]
- 00b4adb4 bytes 774c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a00eba7e2ba78d7e4f675a968af9db00"></a>

### [`00b4add0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4add0.md) → [`00b4ae98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ae98.md) _ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 58.82% / 新版 58.82%

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
      "site": "00b4add0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4add4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4add4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4add0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4add4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4aea8",
      "READ",
      [
        "storage",
        "010a0f58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ae98",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4ae9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4aea8",
      "READ",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4add0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4add0.md#insn-00b4add0) · [`00b4add4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4add0.md#insn-00b4add4) · [`00b4adf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4add0.md#insn-00b4adf8)

~~~diff
- 00b4add0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4add0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4add0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4add0 bytes f30f1ef8
- 00b4add4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4add4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4add4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4add4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4add4 bytes fd7b01a9
- 00b4adf8 ["INT_ADD", "register:40f0:8", ["const:b4adf8:8", "const:4:8"]]
- 00b4adf8 ["CALL", null, ["callee:00bde040:8"]]
- 00b4adf8 bytes 664c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5088843bf4930a5130a3c6e470c9399a"></a>

### [`00b4ae14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ae14.md) → [`00b4aedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4aedc.md) _ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00b4ae44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4af0c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4aef0",
      "incomplete_value": true,
      "site": "00b4aef0",
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
      "definition_site": "00b4ae28",
      "incomplete_value": true,
      "site": "00b4ae28",
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
      "00b4aeec",
      "READ",
      [
        "storage",
        "010a0f58",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4ae30",
      "PARAM",
      [
        "storage",
        "002a8e9a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4ae44",
      "WRITE",
      [
        "storage",
        "010a0f58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4aeec",
      "READ",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aef8",
      "PARAM",
      [
        "storage",
        "002a8e06",
        null,
        "string"
      ]
    ],
    [
      "00b4af0c",
      "WRITE",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ae28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ae14.md#insn-00b4ae28) · [`00b4ae3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ae14.md#insn-00b4ae3c) · [`00b4ae44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ae14.md#insn-00b4ae44)
- 新版 `00b4aef0`（命令位置の公開資料なし） · `00b4af04`（命令位置の公開資料なし）

~~~diff
- 00b4ae28 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4ae28 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b4aef0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4aef0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4ae28 bytes 080100b5
+ 00b4aef0 bytes 080100b5
- 00b4ae3c ["INT_ADD", "register:40f0:8", ["const:b4ae3c:8", "const:4:8"]]
- 00b4ae3c ["CALL", null, ["callee:00bde040:8"]]
+ 00b4af04 ["INT_ADD", "register:40f0:8", ["const:b4af04:8", "const:4:8"]]
+ 00b4af04 ["CALL", null, ["callee:00bde040:8"]]
- 00b4ae3c bytes 554c0294
+ 00b4af04 bytes 4f4c0294
- 00b4ae44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f58:8"]]
- 00b4ae44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ae44 bytes 60ae07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93fd009d909abefb43459a9977a7a135"></a>

### [`00b4af40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4af40.md) → [`00b4b008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b008.md) _ZN8firebase9messaging27registration_intent_service14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 20.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4af40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4af40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4af44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4af40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4af44",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4af54",
      "READ",
      [
        "storage",
        "010a0f58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b008",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4b00c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4b01c",
      "READ",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4af40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4af40.md#insn-00b4af40) · [`00b4af44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4af40.md#insn-00b4af44) · [`00b4af5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4af40.md#insn-00b4af5c)

~~~diff
- 00b4af40 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4af40 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4af40 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4af40 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4af40 bytes f44fbea9
- 00b4af44 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4af44 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4af44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4af44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4af44 bytes fd7b01a9
- 00b4af5c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4af5c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4af5c bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eeec7e655c9d647a8741281cb0036b3e"></a>

### [`00b4afec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4afec.md) → [`00b4b0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b0b4.md) _ZN8firebase9messaging27registration_intent_service13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b0f4",
      "incomplete_value": true,
      "site": "00b4b0f4",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b02c",
      "incomplete_value": true,
      "site": "00b4b02c",
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
            "const:f58:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b008"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b4b0d0"
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
      "unmatched:00b4b000",
      "READ",
      [
        "storage",
        "010a0f58",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4b008",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b0f8"
      ]
    ],
    [
      "00b4b0d8",
      "PARAM",
      [
        "storage",
        "002a8e9a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4b0c8",
      "READ",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b0d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b0f8"
      ]
    ],
    [
      "00b4b0d8",
      "PARAM",
      [
        "storage",
        "002a8e06",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4afec.md#insn-00b4b008) · [`00b4b024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4afec.md#insn-00b4b024) · [`00b4b02c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4afec.md#insn-00b4b02c)
- 新版 `00b4b0ec`（命令位置の公開資料なし） · `00b4b0f4`（命令位置の公開資料なし）

~~~diff
- 00b4b008 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4b008 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4b008 bytes 410100b5
- 00b4b024 ["INT_ADD", "register:40f0:8", ["const:b4b024:8", "const:4:8"]]
- 00b4b024 ["CALL", null, ["callee:00bde040:8"]]
+ 00b4b0ec ["INT_ADD", "register:40f0:8", ["const:b4b0ec:8", "const:4:8"]]
+ 00b4b0ec ["CALL", null, ["callee:00bde040:8"]]
- 00b4b024 bytes db4b0294
+ 00b4b0ec bytes d54b0294
- 00b4b02c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f58:8"]]
- 00b4b02c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b0f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:18:8"]]
+ 00b4b0f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b02c bytes 80ae07f9
+ 00b4b0f4 bytes 800e00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-907af45b0c540e56f27084f7eacde5d6"></a>

### [`00b4b0d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b0d8.md) → [`00b4b1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b1a0.md) _ZN8firebase9messaging26illegal_argument_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 33.33% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b104"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4b1cc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b1b4",
      "incomplete_value": true,
      "site": "00b4b1b4",
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
      "definition_site": "00b4b0ec",
      "incomplete_value": true,
      "site": "00b4b0ec",
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
      "00b4b1b0",
      "READ",
      [
        "storage",
        "010a0f78",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4b0f4",
      "PARAM",
      [
        "storage",
        "00295455",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4b0fc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b4b1b0",
      "READ",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b1bc",
      "PARAM",
      [
        "storage",
        "002954e2",
        null,
        "string"
      ]
    ],
    [
      "00b4b1c4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b0ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b0d8.md#insn-00b4b0ec) · [`00b4b0fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b0d8.md#insn-00b4b0fc) · [`00b4b104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b0d8.md#insn-00b4b104)
- 新版 `00b4b1b4`（命令位置の公開資料なし）

~~~diff
- 00b4b0ec ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4b0ec ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b4b1b4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4b1b4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b4b0ec bytes e80000b5
+ 00b4b1b4 bytes e80000b5
- 00b4b0fc ["INT_ADD", "register:40f0:8", ["const:b4b0fc:8", "const:4:8"]]
- 00b4b0fc ["CALL", null, ["callee:00bde040:8"]]
- 00b4b0fc bytes a54b0294
- 00b4b104 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f78:8"]]
- 00b4b104 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b104 bytes 60be07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2c0ad12979bda864cf326fce14f31fc"></a>

### [`00b4b118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b118.md) → [`00b4b1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b1e0.md) _ZN8firebase9messaging26illegal_argument_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 12.50% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b148"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4b210"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b1f4",
      "incomplete_value": true,
      "site": "00b4b1f4",
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
      "definition_site": "00b4b12c",
      "incomplete_value": true,
      "site": "00b4b12c",
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
      "00b4b1f0",
      "READ",
      [
        "storage",
        "010a0f78",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4b138",
      "PARAM",
      [
        "storage",
        "00295455",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4b140",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b4b1f0",
      "READ",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b200",
      "PARAM",
      [
        "storage",
        "002954e2",
        null,
        "string"
      ]
    ],
    [
      "00b4b208",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b12c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b118.md#insn-00b4b12c) · [`00b4b140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b118.md#insn-00b4b140) · [`00b4b148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b118.md#insn-00b4b148)
- 新版 `00b4b1f4`（命令位置の公開資料なし）

~~~diff
- 00b4b12c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4b12c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b4b1f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4b1f4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4b12c bytes 080100b5
+ 00b4b1f4 bytes 080100b5
- 00b4b140 ["INT_ADD", "register:40f0:8", ["const:b4b140:8", "const:4:8"]]
- 00b4b140 ["CALL", null, ["callee:00bde040:8"]]
- 00b4b140 bytes 944b0294
- 00b4b148 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f78:8"]]
- 00b4b148 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b148 bytes 60be07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de18e1e105a49ebb6c7f4ab81daf6bba"></a>

### [`00b4b15c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b15c.md) → [`00b4b224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b224.md) _ZN8firebase9messaging26illegal_argument_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b18c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4b254"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b170"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4b16c",
      "READ",
      [
        "storage",
        "010a0f78",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4b170",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b258"
      ]
    ],
    [
      "unmatched:00b4b178",
      "PARAM",
      [
        "storage",
        "00295455",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4b234",
      "READ",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b238",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b258"
      ]
    ],
    [
      "00b4b240",
      "PARAM",
      [
        "storage",
        "002954e2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b15c.md#insn-00b4b170) · [`00b4b184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b15c.md#insn-00b4b184) · [`00b4b18c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b15c.md#insn-00b4b18c)
- 新版 `00b4b24c`（命令位置の公開資料なし）

~~~diff
- 00b4b170 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4b170 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b4b170 bytes 080100b5
- 00b4b184 ["INT_ADD", "register:40f0:8", ["const:b4b184:8", "const:4:8"]]
- 00b4b184 ["CALL", null, ["callee:00bde040:8"]]
+ 00b4b24c ["INT_ADD", "register:40f0:8", ["const:b4b24c:8", "const:4:8"]]
+ 00b4b24c ["CALL", null, ["callee:00bde040:8"]]
- 00b4b184 bytes 834b0294
+ 00b4b24c bytes 7d4b0294
- 00b4b18c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f78:8"]]
- 00b4b18c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b18c bytes 60be07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f8352defc7c64ff5218ddf1b8824c4a"></a>

### [`00b4b1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b1ac.md) → [`00b4b274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b274.md) _ZN8firebase9messaging26illegal_argument_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b2cc",
      "incomplete_value": true,
      "site": "00b4b2cc",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b204",
      "incomplete_value": true,
      "site": "00b4b204",
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
            "const:f80:8"
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
      "definition_site": "00b4b2a8",
      "incomplete_value": true,
      "site": "00b4b2b4",
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
                "const:10a1000:8"
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
    "old": {
      "definition_site": "00b4b1e0",
      "incomplete_value": true,
      "site": "00b4b1ec",
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
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:f78:8"
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
      "00b4b288",
      "READ",
      [
        "storage",
        "010a0f80",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b2a8",
      "READ",
      [
        "storage",
        "010a0f78",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b2cc",
      "WRITE",
      [
        "storage",
        "010a0f80",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b288",
      "READ",
      [
        "storage",
        "010a1040",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b2a8",
      "READ",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b2cc",
      "WRITE",
      [
        "storage",
        "010a1040",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b1ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b1ac.md#insn-00b4b1ec) · [`00b4b204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b1ac.md#insn-00b4b204) · [`00b4b1bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b1ac.md#insn-00b4b1bc)
- 新版 `00b4b2b4`（命令位置の公開資料なし） · `00b4b2cc`（命令位置の公開資料なし） · `00b4b284`（命令位置の公開資料なし）

~~~diff
- 00b4b1ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b1ec ["INT_ADD", "register:40f0:8", ["const:b4b1ec:8", "const:4:8"]]
- 00b4b1ec ["CALLIND", null, ["register:0:8"]]
+ 00b4b2b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b2b4 ["INT_ADD", "register:40f0:8", ["const:b4b2b4:8", "const:4:8"]]
+ 00b4b2b4 ["CALLIND", null, ["register:0:8"]]
- 00b4b1ec bytes 00013fd6
+ 00b4b2b4 bytes 00013fd6
- 00b4b204 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4b204 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:f80:8"]]
- 00b4b204 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4b2cc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4b2cc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:40:8"]]
+ 00b4b2cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4b204 bytes a0023e39
+ 00b4b2cc bytes a0020139
- 00b4b1bc ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b4b284 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b4b1bc bytes b52a00b0
+ 00b4b284 bytes b52a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5674b999d59e2a66323cd2b7ba459a04"></a>

### [`00b4b218`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b218.md) → [`00b4b2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b2e0.md) _ZN8firebase9messaging26illegal_argument_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 33.33% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b254"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b274"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4b31c"
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
      "00b4b2f4",
      "READ",
      [
        "storage",
        "010a0f78",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b300",
      "READ",
      [
        "storage",
        "010a0f80",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b308",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4b258"
      ]
    ]
  ],
  "added": [
    [
      "00b4b2f4",
      "READ",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b300",
      "READ",
      [
        "storage",
        "010a1040",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b308",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b320"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b218.md#insn-00b4b230) · [`00b4b254`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b218.md#insn-00b4b254) · [`00b4b25c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b218.md#insn-00b4b25c)
- 新版 `00b4b2f8`（命令位置の公開資料なし）

~~~diff
- 00b4b230 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4b230 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b4b2f8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b4b2f8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b4b230 bytes 410200b4
+ 00b4b2f8 bytes 410200b4
- 00b4b254 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4b254 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4b254 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:f80:8"]]
- 00b4b254 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4b254 bytes bf023e39
- 00b4b25c ["INT_ADD", "register:40f0:8", ["const:b4b25c:8", "const:4:8"]]
- 00b4b25c ["CALL", null, ["callee:00bde090:8"]]
- 00b4b25c bytes 614b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9918bde5cfd2ecc0f51dde1bb2b21a09"></a>

### [`00b4b288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b288.md) → [`00b4b350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b350.md) _ZN8firebase9messaging26illegal_argument_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b2c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4b390"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b2a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4b29c",
      "READ",
      [
        "storage",
        "010a0f78",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4b2a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b394"
      ]
    ],
    [
      "unmatched:00b4b2ac",
      "PARAM",
      [
        "storage",
        "00295455",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4b364",
      "READ",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b36c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b394"
      ]
    ],
    [
      "00b4b374",
      "PARAM",
      [
        "storage",
        "002954e2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b2a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b288.md#insn-00b4b2a4) · [`00b4b2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b288.md#insn-00b4b2c0) · [`00b4b2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b288.md#insn-00b4b2c8)
- 新版 `00b4b388`（命令位置の公開資料なし）

~~~diff
- 00b4b2a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4b2a4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4b2a4 bytes 410100b5
- 00b4b2c0 ["INT_ADD", "register:40f0:8", ["const:b4b2c0:8", "const:4:8"]]
- 00b4b2c0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b4b388 ["INT_ADD", "register:40f0:8", ["const:b4b388:8", "const:4:8"]]
+ 00b4b388 ["CALL", null, ["callee:00bde040:8"]]
- 00b4b2c0 bytes 344b0294
+ 00b4b388 bytes 2e4b0294
- 00b4b2c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f78:8"]]
- 00b4b2c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b2c8 bytes 80be07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8898e51625c405f33f3d34e9387f5faa"></a>

### [`00b4b334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b334.md) → [`00b4b3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b3fc.md) _ZN8firebase9messaging26illegal_argument_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b334"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b334"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b338"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4b334",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4b338",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4b348",
      "READ",
      [
        "storage",
        "010a0f78",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b3fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4b400",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4b410",
      "READ",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b334.md#insn-00b4b334) · [`00b4b338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b334.md#insn-00b4b338) · [`00b4b350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b334.md#insn-00b4b350)

~~~diff
- 00b4b334 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4b334 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4b334 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4b334 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4b334 bytes f44fbea9
- 00b4b338 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4b338 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4b338 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4b338 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4b338 bytes fd7b01a9
- 00b4b350 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4b350 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4b350 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73ca7b64c1d7812c9faf515153f1544b"></a>

### [`00b4b414`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b414.md) → [`00b4b4dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b4dc.md) _ZN8firebase9messaging10FileLocker11AcquireLockEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be04a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be04a0.md) · 呼出先 5件 [`00bdc880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc880.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddc10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc10.md) [`00be0500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0500.md) [`00be0530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0530.md)
- 新版 呼出元 1件 [`00be0550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0550.md) · 呼出先 5件 [`00bdc930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc930.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddcc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcc0.md) [`00be05b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be05b0.md) [`00be05e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be05e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b42c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b4b4f4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b500",
      "incomplete_value": false,
      "site": "00b4b504",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "leaf",
            "const:0:4"
          ]
        ]
      ]
    },
    "old": null,
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
      "00b4b4ec",
      "READ",
      [
        "storage",
        "010a0f98",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4b42c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b500"
      ]
    ]
  ],
  "added": [
    [
      "00b4b4ec",
      "READ",
      [
        "storage",
        "010a1058",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b4f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b500"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b42c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b414.md#insn-00b4b42c) · [`00b4b43c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b414.md#insn-00b4b43c) · [`00b4b450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b414.md#insn-00b4b450)
- 新版 `00b4b504`（命令位置の公開資料なし） · `00b4b518`（命令位置の公開資料なし）

~~~diff
- 00b4b42c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4b42c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b4b42c bytes 680000b4
- 00b4b43c ["INT_ADD", "register:40f0:8", ["const:b4b43c:8", "const:4:8"]]
- 00b4b43c ["CALL", null, ["callee:00bddcc0:8"]]
+ 00b4b504 ["INT_ADD", "register:40f0:8", ["const:b4b504:8", "const:4:8"]]
+ 00b4b504 ["CALL", null, ["callee:00bddcc0:8"]]
- 00b4b43c bytes f5490294
+ 00b4b504 bytes ef490294
- 00b4b450 ["INT_ADD", "register:40f0:8", ["const:b4b450:8", "const:4:8"]]
- 00b4b450 ["CALL", null, ["callee:00be05e0:8"]]
+ 00b4b518 ["INT_ADD", "register:40f0:8", ["const:b4b518:8", "const:4:8"]]
+ 00b4b518 ["CALL", null, ["callee:00be05e0:8"]]
- 00b4b450 bytes 38540294
+ 00b4b518 bytes 32540294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0de160dc712a463e2e90aa239329fc16"></a>

### [`00b4b4d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b4d4.md) → [`00b4b59c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b59c.md) _ZN8firebase9messaging17NotifyListenerSetEPNS0_8ListenerE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0290.md) · 呼出先 6件 [`00bdc880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc880.md) [`00bdd0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0b0.md) [`00bdd140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd140.md) [`00bdd310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd310.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00be0340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0340.md) · 呼出先 6件 [`00bdc930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc930.md) [`00bdd160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd160.md) [`00bdd1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1f0.md) [`00bdd3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd3c0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b5b4",
      "incomplete_value": true,
      "site": "00b4b5b4",
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
      "definition_site": "00b4b4ec",
      "incomplete_value": true,
      "site": "00b4b4ec",
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
      "definition_site": "00b4b62c",
      "incomplete_value": true,
      "site": "00b4b62c",
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
      "definition_site": "00b4b564",
      "incomplete_value": true,
      "site": "00b4b564",
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
      "definition_site": "00b4b600",
      "incomplete_value": false,
      "site": "00b4b604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:9e7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b538",
      "incomplete_value": false,
      "site": "00b4b53c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:95a:8"
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
      "00b4b5b0",
      "READ",
      [
        "storage",
        "010a0fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b5bc",
      "READ",
      [
        "storage",
        "010a0fd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b5e0",
      "READ",
      [
        "storage",
        "010a0fa8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b5b0",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b5bc",
      "READ",
      [
        "storage",
        "010a1090",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b5e0",
      "READ",
      [
        "storage",
        "010a1068",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b53c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b4d4.md#insn-00b4b53c) · [`00b4b4e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b4d4.md#insn-00b4b4e4) · [`00b4b4e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b4d4.md#insn-00b4b4e8)
- 新版 `00b4b604`（命令位置の公開資料なし） · `00b4b5ac`（命令位置の公開資料なし） · `00b4b5b0`（命令位置の公開資料なし）

~~~diff
- 00b4b53c ["INT_ADD", "register:40f0:8", ["const:b4b53c:8", "const:4:8"]]
- 00b4b53c ["CALL", null, ["callee:00bdd1f0:8"]]
+ 00b4b604 ["INT_ADD", "register:40f0:8", ["const:b4b604:8", "const:4:8"]]
+ 00b4b604 ["CALL", null, ["callee:00bdd1f0:8"]]
- 00b4b53c bytes 01470294
+ 00b4b604 bytes fb460294
- 00b4b4e4 ["COPY", "register:4040:8", ["const:10a0000:8"]]
+ 00b4b5ac ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b4b4e4 bytes a82a00b0
+ 00b4b5ac bytes a82a00d0
- 00b4b4e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
- 00b4b4e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b5b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:60:8"]]
+ 00b4b5b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b4e8 bytes 08d147f9
+ 00b4b5b0 bytes 083140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-055afff3b193857b8da105dde7f1f6d6"></a>

### [`00b4b57c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b57c.md) → [`00b4b644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b644.md) _ZN8firebase9messaging10FileLockerD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdc880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc880.md) [`00bdd310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd310.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdc930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc930.md) [`00bdd3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd3c0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b670",
      "incomplete_value": true,
      "site": "00b4b670",
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
      "definition_site": "00b4b5a8",
      "incomplete_value": true,
      "site": "00b4b5a8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b66c",
      "READ",
      [
        "storage",
        "010a0f98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b66c",
      "READ",
      [
        "storage",
        "010a1058",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b5a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b57c.md#insn-00b4b5a8) · [`00b4b58c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b57c.md#insn-00b4b58c) · [`00b4b594`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b57c.md#insn-00b4b594)
- 新版 `00b4b670`（命令位置の公開資料なし） · `00b4b654`（命令位置の公開資料なし） · `00b4b65c`（命令位置の公開資料なし）

~~~diff
- 00b4b5a8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b4b5a8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b4b670 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b4b670 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b4b5a8 bytes 400000b4
+ 00b4b670 bytes 400000b4
- 00b4b58c ["INT_RIGHT", "tmp:0:4", ["register:4098:4", "const:1f:4"]]
- 00b4b58c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b4b58c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b4b58c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b4b654 ["INT_RIGHT", "tmp:0:4", ["register:4098:4", "const:1f:4"]]
+ 00b4b654 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b4b654 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b4b654 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b4b58c bytes 3301f837
+ 00b4b654 bytes 3301f837
- 00b4b594 ["INT_ADD", "register:40f0:8", ["const:b4b594:8", "const:4:8"]]
- 00b4b594 ["CALL", null, ["callee:00bdd3c0:8"]]
+ 00b4b65c ["INT_ADD", "register:40f0:8", ["const:b4b65c:8", "const:4:8"]]
+ 00b4b65c ["CALL", null, ["callee:00bdd3c0:8"]]
- 00b4b594 bytes 5f470294
+ 00b4b65c bytes 59470294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3bcff6538bf79b2479790c4d1fe67b0"></a>

### [`00b4b5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b5c0.md) → [`00b4b688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b688.md) _ZN8firebase9messaging17RequestPermissionEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md) [`00bddec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddec0.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00bddf70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf70.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.46% / 新版 82.46%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b5c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b5c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b5c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4b5c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4b5c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4b5cc",
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
      "00b4b68c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4b690",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4b694",
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

- 旧版 [`00b4b5c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b5c0.md#insn-00b4b5c4) · [`00b4b5c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b5c0.md#insn-00b4b5c8) · [`00b4b5cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b5c0.md#insn-00b4b5cc)

~~~diff
- 00b4b5c4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00b4b5c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b4b5c4 bytes f52300f9
- 00b4b5c8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4b5c8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4b5c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b4b5c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4b5c8 bytes f44f05a9
- 00b4b5cc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4b5cc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4b5cc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b4b5cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4b5cc bytes fd7b06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-113f35bc708374fb003a9b659f22cf1b"></a>

### [`00b4b6e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b6e8.md) → [`00b4b7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b7b0.md) _ZN8firebase9messaging27RequestPermissionLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be04d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be04d0.md) · 呼出先 8件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc80.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md)
- 新版 呼出元 1件 [`00be0580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0580.md) · 呼出先 8件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b7cc",
      "incomplete_value": true,
      "site": "00b4b7cc",
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
      "definition_site": "00b4b704",
      "incomplete_value": true,
      "site": "00b4b704",
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
      "definition_site": "00b4b7dc",
      "incomplete_value": true,
      "site": "00b4b7e0",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": {
      "definition_site": "00b4b714",
      "incomplete_value": true,
      "site": "00b4b718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b820",
      "incomplete_value": false,
      "site": "00b4b824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:16d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b758",
      "incomplete_value": false,
      "site": "00b4b75c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:e0:8"
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
      "00b4b7c4",
      "READ",
      [
        "storage",
        "010a0fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4b758",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4b7c4",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b820",
      "PARAM",
      [
        "storage",
        "0029316d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b6e8.md#insn-00b4b704) · [`00b4b718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b6e8.md#insn-00b4b718) · [`00b4b75c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b6e8.md#insn-00b4b75c)
- 新版 `00b4b7cc`（命令位置の公開資料なし） · `00b4b7e0`（命令位置の公開資料なし） · `00b4b824`（命令位置の公開資料なし）

~~~diff
- 00b4b704 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b4b704 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b4b7cc ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00b4b7cc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4b704 bytes 890200b4
+ 00b4b7cc bytes 890200b4
- 00b4b718 ["INT_ADD", "register:40f0:8", ["const:b4b718:8", "const:4:8"]]
- 00b4b718 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b4b7e0 ["INT_ADD", "register:40f0:8", ["const:b4b7e0:8", "const:4:8"]]
+ 00b4b7e0 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b4b718 bytes 02490294
+ 00b4b7e0 bytes fc480294
- 00b4b75c ["INT_ADD", "register:40f0:8", ["const:b4b75c:8", "const:4:8"]]
- 00b4b75c ["CALL", null, ["callee:00bde130:8"]]
+ 00b4b824 ["INT_ADD", "register:40f0:8", ["const:b4b824:8", "const:4:8"]]
+ 00b4b824 ["CALL", null, ["callee:00bde130:8"]]
- 00b4b75c bytes 494a0294
+ 00b4b824 bytes 434a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96e8acfe81f989b3333bd14ef367a9a7"></a>

### [`00b4b7bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b7bc.md) → [`00b4b884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b884.md) _ZN8firebase9messaging15ProcessMessagesEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be04c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be04c0.md) · 呼出先 39件 [`0044a6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a6d0.md) [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00b4e7d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e7d0.md) [`00b4e7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e7d4.md)
- 新版 呼出元 1件 [`00be0570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0570.md) · 呼出先 39件 [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00b4e898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e898.md) [`00b4e89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e89c.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.36% / 新版 75.36%

CFGの説明率　旧版 23.71% / 新版 23.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 21件, `store_condition` 12件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 30件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 23件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b7d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b7d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b7ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4b7d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4b7e8",
      "PARAM",
      [
        "storage",
        "010a0ea8",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4b7ec",
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
      "00b4b898",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4b8b0",
      "PARAM",
      [
        "storage",
        "010a0f68",
        null,
        null
      ]
    ],
    [
      "00b4b8b4",
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

- 旧版 [`00b4b7d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b7bc.md#insn-00b4b7d0) · [`00b4b7ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b7bc.md#insn-00b4b7ec) · [`00b4b848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b7bc.md#insn-00b4b848)

~~~diff
- 00b4b7d0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4b7d0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4b7d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b4b7d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4b7d0 bytes fd7b05a9
- 00b4b7ec ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b4b7ec ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffff98:8"]]
- 00b4b7ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b4b7ec bytes a88319f8
- 00b4b848 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b4b848 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:fc8:8"]]
- 00b4b848 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4b848 bytes a8223f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da5ba031aefd9e2f3bb72e3e8f52a741"></a>

### [`00b4c3b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c3b8.md) → [`00b4c480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c480.md) _ZN8firebase9messaging10InitializeERKNS_3AppEPNS0_8ListenerERKNS0_16MessagingOptionsE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be04b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be04b0.md) · 呼出先 33件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00afa8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa8fc.md) [`00b4c8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c8e0.md) [`00b4c99c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c99c.md)
- 新版 呼出元 1件 [`00be0560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0560.md) · 呼出先 33件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00afa9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) [`00b4c9a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c9a8.md) [`00b4ca64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ca64.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.45% / 新版 64.45%

CFGの説明率　旧版 8.24% / 新版 8.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 30件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 11件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 22件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c3c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c3c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c48c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4c3c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4c4d0",
      "READ",
      [
        "storage",
        "010a0fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4c414",
      "PARAM",
      [
        "storage",
        "00294235",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4c490",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4c4d0",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c4dc",
      "PARAM",
      [
        "storage",
        "002942c2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c3c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c3b8.md#insn-00b4c3c8) · [`00b4c458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c3b8.md#insn-00b4c458) · [`00b4c48c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c3b8.md#insn-00b4c48c)
- 新版 `00b4c520`（命令位置の公開資料なし）

~~~diff
- 00b4c3c8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4c3c8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4c3c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b4c3c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4c3c8 bytes fd7b07a9
- 00b4c458 ["INT_ADD", "register:40f0:8", ["const:b4c458:8", "const:4:8"]]
- 00b4c458 ["CALL", null, ["callee:00bddfd0:8"]]
+ 00b4c520 ["INT_ADD", "register:40f0:8", ["const:b4c520:8", "const:4:8"]]
+ 00b4c520 ["CALL", null, ["callee:00bddfd0:8"]]
- 00b4c458 bytes b2460294
+ 00b4c520 bytes ac460294
- 00b4c48c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:ef8:8"]]
- 00b4c48c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c48c bytes 007f07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b972552af0f2258997936596052b84a7"></a>

### [`00b4c8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c8e0.md) → [`00b4c9a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c9a8.md) FUN_00b4c9a8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b4c3b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c3b8.md) [`00b4cdc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cdc8.md) · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 2件 [`00b4c480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c480.md) [`00b4ce90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ce90.md) · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 31.91% / 新版 31.91%

CFGの説明率　旧版 13.33% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c8e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c8e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c8e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4c8e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4c8e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4c9bc",
      "READ",
      [
        "storage",
        "010a0ef8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c9a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4c9ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4c9bc",
      "READ",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c8e0.md#insn-00b4c8e0) · [`00b4c8e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c8e0.md#insn-00b4c8e4) · [`00b4c8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c8e0.md#insn-00b4c8fc)

~~~diff
- 00b4c8e0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b4c8e0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b4c8e0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4c8e0 bytes f50f1df8
- 00b4c8e4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4c8e4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4c8e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4c8e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4c8e4 bytes f44f01a9
- 00b4c8fc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4c8fc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b4c8fc bytes 210200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bb7e1747f54b39b469755b275520329"></a>

### [`00b4c99c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c99c.md) → [`00b4ca64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ca64.md) FUN_00b4ca64

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4c3b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c3b8.md) · 呼出先 11件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00b4c480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c480.md) · 呼出先 11件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 36.84% / 新版 37.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c9ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c9ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c9b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4c9ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4c9b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4c9b4",
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
      "00b4ca74",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4ca78",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4ca7c",
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

- 旧版 [`00b4c9ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c99c.md#insn-00b4c9ac) · [`00b4c9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c99c.md#insn-00b4c9b0) · [`00b4c9b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c99c.md#insn-00b4c9b4)

~~~diff
- 00b4c9ac ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b4c9ac ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b4c9ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 00b4c9ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4c9ac bytes f65715a9
- 00b4c9b0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4c9b0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4c9b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:160:8"]]
- 00b4c9b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4c9b0 bytes f44f16a9
- 00b4c9b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4c9b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4c9b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:170:8"]]
- 00b4c9b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4c9b4 bytes fd7b17a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-620a5a60d48eb4248b3de8e83da3f4c8"></a>

### [`00b4cb34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cb34.md) → [`00b4cbfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cbfc.md) _ZN8firebase9messaging33SetTokenRegistrationOnInitEnabledEb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddb90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb90.md) · 呼出先 6件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00b4cce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cce0.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bddc40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc40.md) · 呼出先 6件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00b4cda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cda8.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.00% / 新版 55.00%

CFGの説明率　旧版 9.52% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4cb34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4cb38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4cb38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4cb34",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4cb38",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4cc14",
      "READ",
      [
        "storage",
        "010a0fa0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cbfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b4cc00",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4cc14",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cb34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cb34.md#insn-00b4cb34) · [`00b4cb38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cb34.md#insn-00b4cb38) · [`00b4cb54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cb34.md#insn-00b4cb54)
- 新版 `00b4cc1c`（命令位置の公開資料なし）

~~~diff
- 00b4cb34 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00b4cb34 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b4cb34 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4cb34 bytes f70f1cf8
- 00b4cb38 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b4cb38 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b4cb38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4cb38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4cb38 bytes f65701a9
- 00b4cb54 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4cb54 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 00b4cc1c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4cc1c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b4cb54 bytes 680600b4
+ 00b4cc1c bytes 680600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9b823ef3becf502902eb93ef11a8967"></a>

### [`00b4cc74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cc74.md) → [`00b4cd3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cd3c.md) _ZN8firebase9messaging32IsTokenRegistrationOnInitEnabledEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 44.44% / 新版 44.44%

CFGの説明率　旧版 11.11% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4cd50",
      "incomplete_value": true,
      "site": "00b4cd50",
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
      "definition_site": "00b4cc88",
      "incomplete_value": true,
      "site": "00b4cc88",
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
      "site": "00b4cca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b4cd70"
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
      "00b4cd4c",
      "READ",
      [
        "storage",
        "010a0fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cd50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4ccac"
      ]
    ],
    [
      "unmatched:00b4cc90",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4cd4c",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cd50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4cd74"
      ]
    ],
    [
      "00b4cd58",
      "PARAM",
      [
        "storage",
        "0029316d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cc94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cc74.md#insn-00b4cc94) · [`00b4cca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cc74.md#insn-00b4cca0) · [`00b4cca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cc74.md#insn-00b4cca8)

~~~diff
- 00b4cc94 ["INT_ADD", "register:40f0:8", ["const:b4cc94:8", "const:4:8"]]
- 00b4cc94 ["CALL", null, ["callee:00bdddf0:8"]]
- 00b4cc94 bytes 2b440294
- 00b4cca0 ["INT_ADD", "register:40f0:8", ["const:b4cca0:8", "const:4:8"]]
- 00b4cca0 ["CALL", null, ["callee:00bde130:8"]]
- 00b4cca0 bytes f8440294
- 00b4cca8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b4cca8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b4cca8 bytes 800100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-032baabc8be540d306d6ee7f251667a9"></a>

### [`00b4cce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cce0.md) → [`00b4cda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cda8.md) FUN_00b4cda8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b4c3b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c3b8.md) [`00b4cb34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cb34.md) · 呼出先 8件 [`00848b34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00848/00848b34.md) [`00b4e984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e984.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 2件 [`00b4c480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c480.md) [`00b4cbfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cbfc.md) · 呼出先 8件 [`00848b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848b34.md) [`00b4ea4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ea4c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 63.83% / 新版 63.83%

CFGの説明率　旧版 15.38% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4cce4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4cce8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4cce8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4cce4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4cce8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4ccf8",
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
      "00b4cdac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4cdb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4cdc0",
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

- 旧版 [`00b4cce4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cce0.md#insn-00b4cce4) · [`00b4cce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cce0.md#insn-00b4cce8) · [`00b4ccf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cce0.md#insn-00b4ccf8)

~~~diff
- 00b4cce4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00b4cce4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b4cce4 bytes f33300f9
- 00b4cce8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4cce8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4cce8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b4cce8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4cce8 bytes fd7b07a9
- 00b4ccf8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b4ccf8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00b4ccf8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b4ccf8 bytes a8831ef8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13202d3610c501af338d47cb145b5f10"></a>

### [`00b4cdc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cdc8.md) → [`00b4ce90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ce90.md) _ZN8firebase9messaging9TerminateEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0370.md) · 呼出先 23件 [`00b4c8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c8e0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdc880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc880.md) [`00bdd0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0b0.md) [`00bdd140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd140.md)
- 新版 呼出元 1件 [`00be0420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0420.md) · 呼出先 23件 [`00b4c9a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c9a8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdc930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc930.md) [`00bdd160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd160.md) [`00bdd1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1f0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.00% / 新版 67.00%

CFGの説明率　旧版 22.99% / 新版 22.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 2件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 13件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `branch_value` 3件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4cdc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4cdc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4cdcc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4cdc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4cdcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b4ceac",
      "READ",
      [
        "storage",
        "010a0fa0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ce90",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b4ce94",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b4ceac",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cdc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cdc8.md#insn-00b4cdc8) · [`00b4cdcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cdc8.md#insn-00b4cdcc) · [`00b4cde8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cdc8.md#insn-00b4cde8)
- 新版 `00b4ceb0`（命令位置の公開資料なし）

~~~diff
- 00b4cdc8 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b4cdc8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b4cdc8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b4cdc8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4cdc8 bytes fa67bba9
- 00b4cdcc ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b4cdcc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b4cdcc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4cdcc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4cdcc bytes f85f01a9
- 00b4cde8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4cde8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b4ceb0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4ceb0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b4cde8 bytes a80200b4
+ 00b4ceb0 bytes a80200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dead23716648c1b0c3d26711038a217"></a>

### [`00b4d13c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d13c.md) → [`00b4d204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d204.md) _ZN8firebase9messaging9SubscribeEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 18件 [`00b4d40c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d40c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00b4d4d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d4d4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.68% / 新版 87.68%

CFGの説明率　旧版 13.89% / 新版 14.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 6件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4d140"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4d2b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4d208"
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
      "unmatched:00b4d140",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4d16c",
      "READ",
      [
        "storage",
        "010a0fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4d170",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4d2a0"
      ]
    ]
  ],
  "added": [
    [
      "00b4d208",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b4d234",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d238",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4d2a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d13c.md#insn-00b4d140) · [`00b4d170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d13c.md#insn-00b4d170) · [`00b4d184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d13c.md#insn-00b4d184)
- 新版 `00b4d24c`（命令位置の公開資料なし）

~~~diff
- 00b4d140 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00b4d140 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00b4d140 bytes f93300f9
- 00b4d170 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b4d170 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b4d170 bytes 490300b4
- 00b4d184 ["INT_ADD", "register:40f0:8", ["const:b4d184:8", "const:4:8"]]
- 00b4d184 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b4d24c ["INT_ADD", "register:40f0:8", ["const:b4d24c:8", "const:4:8"]]
+ 00b4d24c ["CALL", null, ["callee:00bddbd0:8"]]
- 00b4d184 bytes 67420294
+ 00b4d24c bytes 61420294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c544057aaa37cb9ed3a1f0517f07456"></a>

### [`00b4d40c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d40c.md) → [`00b4d4d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d4d4.md) FUN_00b4d4d4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b4d13c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d13c.md) [`00b4e83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e83c.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b4ea4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4ea4c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 2件 [`00b4d204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d204.md) [`00b4e904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e904.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b4eb14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4eb14.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.08% / 新版 81.08%

CFGの説明率　旧版 10.00% / 新版 9.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4d410"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4d410"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4d414"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4d410",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4d414",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4d418",
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
      "00b4d4d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b4d4dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4d4e0",
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

- 旧版 [`00b4d410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d40c.md#insn-00b4d410) · [`00b4d414`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d40c.md#insn-00b4d414) · [`00b4d418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d40c.md#insn-00b4d418)

~~~diff
- 00b4d410 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b4d410 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b4d410 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b4d410 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4d410 bytes f85f04a9
- 00b4d414 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b4d414 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b4d414 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b4d414 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4d414 bytes f65705a9
- 00b4d418 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4d418 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4d418 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b4d418 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4d418 bytes f44f06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ea6289c88eab6cb10aaca9f85ae415c"></a>

### [`00b4d608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d608.md) → [`00b4d6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d6d0.md) _ZN8firebase9messaging19SubscribeLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc80.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4d624"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b4d6ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4d628"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4d61c",
      "READ",
      [
        "storage",
        "010a0fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4d624",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4d73c"
      ]
    ],
    [
      "unmatched:00b4d628",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00be02b0"
      ]
    ]
  ],
  "added": [
    [
      "00b4d6e4",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d6ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4d73c"
      ]
    ],
    [
      "00b4d6f0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00be02b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d624`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d608.md#insn-00b4d624) · [`00b4d628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d608.md#insn-00b4d628) · [`00b4d638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d608.md#insn-00b4d638)
- 新版 `00b4d700`（命令位置の公開資料なし）

~~~diff
- 00b4d624 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b4d624 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b4d624 bytes 890200b4
- 00b4d628 ["INT_ADD", "register:40f0:8", ["const:b4d628:8", "const:4:8"]]
- 00b4d628 ["CALL", null, ["callee:00be02b0:8"]]
- 00b4d628 bytes f64a0294
- 00b4d638 ["INT_ADD", "register:40f0:8", ["const:b4d638:8", "const:4:8"]]
- 00b4d638 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b4d700 ["INT_ADD", "register:40f0:8", ["const:b4d700:8", "const:4:8"]]
+ 00b4d700 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b4d638 bytes 3a410294
+ 00b4d700 bytes 34410294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f45118b76a6935ea7859181a2145455"></a>

### [`00b4d6e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d6e0.md) → [`00b4d7a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d7a8.md) _ZN8firebase9messaging11UnsubscribeEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 18件 [`00b4d9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d9b0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00b4da78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4da78.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.41% / 新版 88.41%

CFGの説明率　旧版 19.72% / 新版 20.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 20件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4d6e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4d6e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4d6e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4d6e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4d6e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4d708",
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
      "00b4d7ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b4d7b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b4d7d0",
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

- 旧版 [`00b4d6e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d6e0.md#insn-00b4d6e4) · [`00b4d6e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d6e0.md#insn-00b4d6e8) · [`00b4d708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d6e0.md#insn-00b4d708)

~~~diff
- 00b4d6e4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00b4d6e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00b4d6e4 bytes f93300f9
- 00b4d6e8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b4d6e8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b4d6e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b4d6e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4d6e8 bytes f85f07a9
- 00b4d708 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b4d708 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 00b4d708 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b4d708 bytes a9831bf8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17e7275dd8999d5407873b4c898d102b"></a>

### [`00b4d9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d9b0.md) → [`00b4da78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4da78.md) FUN_00b4da78

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b4d6e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d6e0.md) [`00b4e83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e83c.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b4ea4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4ea4c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 2件 [`00b4d7a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d7a8.md) [`00b4e904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e904.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b4eb14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4eb14.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.68% / 新版 84.68%

CFGの説明率　旧版 6.52% / 新版 7.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4d9b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4d9b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4d9b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4d9b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4d9b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4d9dc",
      "PARAM",
      [
        "storage",
        "002af5f1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4da7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b4da80",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4daa4",
      "PARAM",
      [
        "storage",
        "002af5f1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d9b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d9b0.md#insn-00b4d9b4) · [`00b4d9b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d9b0.md#insn-00b4d9b8) · [`00b4d9e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d9b0.md#insn-00b4d9e8)
- 新版 `00b4dab0`（命令位置の公開資料なし）

~~~diff
- 00b4d9b4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b4d9b4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b4d9b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b4d9b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4d9b4 bytes f85f04a9
- 00b4d9b8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b4d9b8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b4d9b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b4d9b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4d9b8 bytes f65705a9
- 00b4d9e8 ["INT_ADD", "register:40f0:8", ["const:b4d9e8:8", "const:4:8"]]
- 00b4d9e8 ["CALL", null, ["callee:00bde260:8"]]
+ 00b4dab0 ["INT_ADD", "register:40f0:8", ["const:b4dab0:8", "const:4:8"]]
+ 00b4dab0 ["CALL", null, ["callee:00bde260:8"]]
- 00b4d9e8 bytes f2410294
+ 00b4dab0 bytes ec410294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-199e738085a5f052d392e0c8494effd8"></a>

### [`00b4dbac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4dbac.md) → [`00b4dc74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4dc74.md) _ZN8firebase9messaging21UnsubscribeLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc80.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.05% / 新版 69.05%

CFGの説明率　旧版 5.88% / 新版 4.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4dbac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4dbac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4dbb0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4dbac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4dbb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4dbb4",
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
      "00b4dc74",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4dc78",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4dc7c",
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

- 旧版 [`00b4dbac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4dbac.md#insn-00b4dbac) · [`00b4dbb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4dbac.md#insn-00b4dbb0) · [`00b4dbb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4dbac.md#insn-00b4dbb4)

~~~diff
- 00b4dbac ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b4dbac ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b4dbac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b4dbac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4dbac bytes f657bda9
- 00b4dbb0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4dbb0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4dbb0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4dbb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4dbb0 bytes f44f01a9
- 00b4dbb4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4dbb4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4dbb4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b4dbb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4dbb4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d2444236dfdb23c710f2e6807806e4c"></a>

### [`00b4dc84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4dc84.md) → [`00b4dd4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4dd4c.md) _ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.62% / 新版 47.62%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4dc84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4dc84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4dd4c"
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
      "unmatched:00b4dc84",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4dc90",
      "READ",
      [
        "storage",
        "010a0fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4dc94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4dd88"
      ]
    ]
  ],
  "added": [
    [
      "00b4dd4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4dd58",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dd5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4dd88"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dc84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4dc84.md#insn-00b4dc84) · [`00b4dc94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4dc84.md#insn-00b4dc94) · [`00b4dc98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4dc84.md#insn-00b4dc98)

~~~diff
- 00b4dc84 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4dc84 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4dc84 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00b4dc84 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4dc84 bytes fd7bbfa9
- 00b4dc94 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b4dc94 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b4dc94 bytes 600100b4
- 00b4dc98 ["INT_ADD", "register:40f0:8", ["const:b4dc98:8", "const:4:8"]]
- 00b4dc98 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b4dc98 bytes 1a410294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63d88b36f520e986d2c13698eb774acb"></a>

### [`00b4dcd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4dcd8.md) → [`00b4dda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4dda0.md) _ZN8firebase9messaging34SetDeliveryMetricsExportToBigQueryEb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 72.00% / 新版 72.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4dcd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4dcdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4dcdc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4dcd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4dcdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4dce8",
      "READ",
      [
        "storage",
        "010a0fa0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dda0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4dda4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4ddb0",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dcd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4dcd8.md#insn-00b4dcd8) · [`00b4dcdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4dcd8.md#insn-00b4dcdc) · [`00b4dcf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4dcd8.md#insn-00b4dcf8)
- 新版 `00b4ddc0`（命令位置の公開資料なし）

~~~diff
- 00b4dcd8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4dcd8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4dcd8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4dcd8 bytes f30f1ef8
- 00b4dcdc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4dcdc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4dcdc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4dcdc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4dcdc bytes fd7b01a9
- 00b4dcf8 ["INT_ADD", "register:40f0:8", ["const:b4dcf8:8", "const:4:8"]]
- 00b4dcf8 ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b4ddc0 ["INT_ADD", "register:40f0:8", ["const:b4ddc0:8", "const:4:8"]]
+ 00b4ddc0 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b4dcf8 bytes 02410294
+ 00b4ddc0 bytes fc400294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77bc45eeb7aa6e60411bb757dd580808"></a>

### [`00b4dd3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4dd3c.md) → [`00b4de04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4de04.md) _ZN8firebase9messaging8GetTokenEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be04e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be04e0.md) · 呼出先 22件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00ae3d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3d00.md) [`00b4e018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e018.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00be0590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0590.md) · 呼出先 22件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00ae3dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3dc8.md) [`00b4e0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e0e0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.41% / 新版 79.41%

CFGの説明率　旧版 3.70% / 新版 4.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `store_condition` 4件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4dd68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4de30"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4dd70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4dd68",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4dd6c",
      "READ",
      [
        "storage",
        "010a0fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4dd70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4df38"
      ]
    ]
  ],
  "added": [
    [
      "00b4de30",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b4de34",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4de38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4df38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dd68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4dd3c.md#insn-00b4dd68) · [`00b4dd70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4dd3c.md#insn-00b4dd70) · [`00b4dd80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4dd3c.md#insn-00b4dd80)
- 新版 `00b4de48`（命令位置の公開資料なし）

~~~diff
- 00b4dd68 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b4dd68 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 00b4dd68 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b4dd68 bytes a9831bf8
- 00b4dd70 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b4dd70 ["CBRANCH", null, ["local:b30:8", "tmp:0:1"]]
- 00b4dd70 bytes 090800b4
- 00b4dd80 ["INT_ADD", "register:40f0:8", ["const:b4dd80:8", "const:4:8"]]
- 00b4dd80 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b4de48 ["INT_ADD", "register:40f0:8", ["const:b4de48:8", "const:4:8"]]
+ 00b4de48 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b4dd80 bytes 683f0294
+ 00b4de48 bytes 623f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5cf14bde6206c547730f9a807520680"></a>

### [`00b4e018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e018.md) → [`00b4e0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e0e0.md) FUN_00b4e0e0

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4dd3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4dd3c.md) · 呼出先 15件 [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00b4de04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4de04.md) · 呼出先 15件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.16% / 新版 87.16%

CFGの説明率　旧版 15.15% / 新版 15.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e028"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e028"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e02c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4e028",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4e02c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4e030",
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
      "00b4e0f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4e0f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4e0f8",
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

- 旧版 [`00b4e028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e018.md#insn-00b4e028) · [`00b4e02c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e018.md#insn-00b4e02c) · [`00b4e030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e018.md#insn-00b4e030)

~~~diff
- 00b4e028 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b4e028 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b4e028 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00b4e028 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4e028 bytes f65708a9
- 00b4e02c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4e02c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4e02c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00b4e02c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4e02c bytes f44f09a9
- 00b4e030 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4e030 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4e030 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00b4e030 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4e030 bytes fd7b0aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b33ef86b2a45b7a073eec368e7716ddc"></a>

### [`00b4e2a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e2a0.md) → [`00b4e368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e368.md) _ZN8firebase9messaging18GetTokenLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc80.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e2a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e2a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e2a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4e2a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4e2a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4e2a8",
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
      "00b4e368",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4e36c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4e370",
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

- 旧版 [`00b4e2a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e2a0.md#insn-00b4e2a0) · [`00b4e2a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e2a0.md#insn-00b4e2a4) · [`00b4e2a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e2a0.md#insn-00b4e2a8)

~~~diff
- 00b4e2a0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b4e2a0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b4e2a0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b4e2a0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4e2a0 bytes f657bda9
- 00b4e2a4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4e2a4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4e2a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4e2a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4e2a4 bytes f44f01a9
- 00b4e2a8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4e2a8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4e2a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b4e2a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4e2a8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79cfc2e9b18dde9e1d2a59ec2f5e4b9c"></a>

### [`00b4e378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e378.md) → [`00b4e440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e440.md) _ZN8firebase9messaging11DeleteTokenEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 20件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b4e5e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e5e0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md)
- 新版 呼出元 0件  · 呼出先 20件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b4e6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e6a8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.07% / 新版 76.07%

CFGの説明率　旧版 14.81% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e37c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e37c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e380"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4e37c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4e380",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4e384",
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
      "00b4e444",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b4e448",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4e44c",
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

- 旧版 [`00b4e37c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e378.md#insn-00b4e37c) · [`00b4e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e378.md#insn-00b4e380) · [`00b4e384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e378.md#insn-00b4e384)

~~~diff
- 00b4e37c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b4e37c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b4e37c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b4e37c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4e37c bytes f85f05a9
- 00b4e380 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b4e380 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b4e380 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b4e380 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4e380 bytes f65706a9
- 00b4e384 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4e384 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4e384 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b4e384 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4e384 bytes f44f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a8ee369428345d3405c9583230c70ac"></a>

### [`00b4e5e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e5e0.md) → [`00b4e6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e6a8.md) FUN_00b4e6a8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4e378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e378.md) · 呼出先 8件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bddc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc80.md)
- 新版 呼出元 1件 [`00b4e440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e440.md) · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.72% / 新版 87.72%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e620"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4e6e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e624"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4e620",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4e624",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bddd30"
      ]
    ],
    [
      "unmatched:00b4e62c",
      "PARAM",
      [
        "storage",
        "010a0ed0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4e6e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b4e6ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bddd30"
      ]
    ],
    [
      "00b4e6f4",
      "PARAM",
      [
        "storage",
        "010a0f90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e5e0.md#insn-00b4e620) · [`00b4e624`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e5e0.md#insn-00b4e624) · [`00b4e630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e5e0.md#insn-00b4e630)
- 新版 `00b4e6f8`（命令位置の公開資料なし）

~~~diff
- 00b4e620 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b4e620 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b4e620 bytes e80f00f9
- 00b4e624 ["INT_ADD", "register:40f0:8", ["const:b4e624:8", "const:4:8"]]
- 00b4e624 ["CALL", null, ["callee:00bddd30:8"]]
- 00b4e624 bytes 973d0294
- 00b4e630 ["INT_ADD", "register:40f0:8", ["const:b4e630:8", "const:4:8"]]
- 00b4e630 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b4e6f8 ["INT_ADD", "register:40f0:8", ["const:b4e6f8:8", "const:4:8"]]
+ 00b4e6f8 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b4e630 bytes 3c3d0294
+ 00b4e6f8 bytes 363d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0829b1781656d153104b9995f9cc9f1"></a>

### [`00b4e6f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e6f8.md) → [`00b4e7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e7c0.md) _ZN8firebase9messaging21DeleteTokenLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc80.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e6f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e6f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e6fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4e6f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4e6fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4e700",
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
      "00b4e7c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4e7c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4e7c8",
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

- 旧版 [`00b4e6f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e6f8.md#insn-00b4e6f8) · [`00b4e6fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e6f8.md#insn-00b4e6fc) · [`00b4e700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e6f8.md#insn-00b4e700)

~~~diff
- 00b4e6f8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b4e6f8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b4e6f8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b4e6f8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4e6f8 bytes f657bda9
- 00b4e6fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4e6fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4e6fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4e6fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4e6fc bytes f44f01a9
- 00b4e700 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4e700 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4e700 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b4e700 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4e700 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65528387e9c920f0664b6f0570a6b285"></a>

### [`00b4e83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e83c.md) → [`00b4e904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e904.md) FUN_00b4e904

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b4e7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e7d4.md) [`00b4e984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e984.md) · 呼出先 4件 [`00b4d40c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d40c.md) [`00b4d9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d9b0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md)
- 新版 呼出元 2件 [`00b4e89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e89c.md) [`00b4ea4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ea4c.md) · 呼出先 4件 [`00b4d4d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d4d4.md) [`00b4da78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4da78.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 67.07% / 新版 67.07%

CFGの説明率　旧版 2.04% / 新版 2.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e854"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e864"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e8a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4e850",
      "READ",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4e854",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4e9a8"
      ]
    ],
    [
      "unmatched:00b4e864",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4e954"
      ]
    ]
  ],
  "added": [
    [
      "00b4e918",
      "READ",
      [
        "storage",
        "010a1078",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e91c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4e9a8"
      ]
    ],
    [
      "00b4e92c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4e954"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e83c.md#insn-00b4e854) · [`00b4e864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e83c.md#insn-00b4e864) · [`00b4e8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e83c.md#insn-00b4e8a4)

~~~diff
- 00b4e854 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00b4e854 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00b4e854 bytes 740400b4
- 00b4e864 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b4e864 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b4e864 bytes 41010054
- 00b4e8a4 ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
- 00b4e8a4 bytes a0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8297bb3dd5d246f1c6c6699ab7582aa7"></a>

### [`00b4ea4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4ea4c.md) → [`00b4eb14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4eb14.md) FUN_00b4eb14

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b4d40c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d40c.md) [`00b4d9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d9b0.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md) [`00bded00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded00.md)
- 新版 呼出元 2件 [`00b4d4d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d4d4.md) [`00b4da78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4da78.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00bdedb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.95% / 新版 80.95%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ea50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ea54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ea54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4ea50",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4ea54",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4ea7c",
      "WRITE",
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
      "00b4eb18",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b4eb1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4eb44",
      "WRITE",
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

- 旧版 [`00b4ea50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4ea4c.md#insn-00b4ea50) · [`00b4ea54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4ea4c.md#insn-00b4ea54) · [`00b4ea7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4ea4c.md#insn-00b4ea7c)

~~~diff
- 00b4ea50 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b4ea50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00b4ea50 bytes f71300f9
- 00b4ea54 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b4ea54 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b4ea54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b4ea54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4ea54 bytes f65703a9
- 00b4ea7c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b4ea7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b4ea7c bytes e80f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8085cdce32461f97ca69698d31bc0258"></a>

### [`00b4eb08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4eb08.md) → [`00b4ebd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ebd0.md) _ZN8firebase6FutureIvEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0490.md) · 呼出先 3件 [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdde70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde70.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md)
- 新版 呼出元 1件 [`00be0540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0540.md) · 呼出先 3件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 77.42% / 新版 77.42%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b4eb34",
      "incomplete_value": true,
      "site": "00b4eb3c",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b4eb38",
      "incomplete_value": true,
      "site": "00b4eb3c",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4eb50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4eb50",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00b4eb70",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4ec18",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00b4ec38",
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

- 旧版 [`00b4eb3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4eb08.md#insn-00b4eb3c) · [`00b4eb50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4eb08.md#insn-00b4eb50) · [`00b4eb58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4eb08.md#insn-00b4eb58)
- 新版 `00b4ec04`（命令位置の公開資料なし） · `00b4ec20`（命令位置の公開資料なし）

~~~diff
- 00b4eb3c ["INT_ADD", "register:40f0:8", ["const:b4eb3c:8", "const:4:8"]]
- 00b4eb3c ["CALL", null, ["callee:00bddf30:8"]]
+ 00b4ec04 ["INT_ADD", "register:40f0:8", ["const:b4ec04:8", "const:4:8"]]
+ 00b4ec04 ["CALL", null, ["callee:00bddf30:8"]]
- 00b4eb3c bytes d13c0294
+ 00b4ec04 bytes cb3c0294
- 00b4eb50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4eb50 ["INT_ADD", "register:40f0:8", ["const:b4eb50:8", "const:4:8"]]
- 00b4eb50 ["CALLIND", null, ["register:0:8"]]
- 00b4eb50 bytes 00013fd6
- 00b4eb58 ["INT_ADD", "register:40f0:8", ["const:b4eb58:8", "const:4:8"]]
- 00b4eb58 ["CALL", null, ["callee:00bddf20:8"]]
+ 00b4ec20 ["INT_ADD", "register:40f0:8", ["const:b4ec20:8", "const:4:8"]]
+ 00b4ec20 ["CALL", null, ["callee:00bddf20:8"]]
- 00b4eb58 bytes c63c0294
+ 00b4ec20 bytes c03c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38ef2d0bc086aaa991c70e4483edbdfd"></a>

### [`00b4eba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4eba8.md) → [`00b4ec70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ec70.md) _ZNSt6__ndk16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase16SafeFutureHandleIvEEEENS5_ISB_EEE21__push

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be04f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be04f0.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdddb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddb0.md) [`00bdeca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeca0.md)
- 新版 呼出元 1件 [`00be05a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be05a0.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md) [`00bded50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.90% / 新版 81.90%

CFGの説明率　旧版 12.90% / 新版 12.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ebb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ebb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ec50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4ebb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4ec14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4ecf0"
      ]
    ],
    [
      "unmatched:00b4ec70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4ed88"
      ]
    ]
  ],
  "added": [
    [
      "00b4ec80",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4ecdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4ecf0"
      ]
    ],
    [
      "00b4ed38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4ed88"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ebb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4eba8.md#insn-00b4ebb8) · [`00b4ec14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4eba8.md#insn-00b4ec14) · [`00b4ec30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4eba8.md#insn-00b4ec30)
- 新版 `00b4ecf8`（命令位置の公開資料なし）

~~~diff
- 00b4ebb8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4ebb8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4ebb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b4ebb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4ebb8 bytes fd7b04a9
- 00b4ec14 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b4ec14 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b4ec14 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00b4ec14 bytes a8000054
- 00b4ec30 ["INT_ADD", "register:40f0:8", ["const:b4ec30:8", "const:4:8"]]
- 00b4ec30 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b4ecf8 ["INT_ADD", "register:40f0:8", ["const:b4ecf8:8", "const:4:8"]]
+ 00b4ecf8 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b4ec30 bytes c4300294
+ 00b4ecf8 bytes be300294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf5520f634b57998db1aaa328c377c1a"></a>

### [`00b4ed4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4ed4c.md) → [`00b4ee14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ee14.md) _INIT_277

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b05384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05384.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bddd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b0544c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0544c.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 44.83% / 新版 44.83%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ed6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ed8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b4ed9c",
      "incomplete_value": false,
      "site": "00b4eda0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
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
      "unmatched:00b4ed68",
      "PARAM",
      [
        "storage",
        "010a0ea8",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4ed6c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdddd0"
      ]
    ],
    [
      "unmatched:00b4ed74",
      "READ",
      [
        "storage",
        "00c1b778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b4ee30",
      "PARAM",
      [
        "storage",
        "010a0f68",
        null,
        null
      ]
    ],
    [
      "00b4ee34",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdddd0"
      ]
    ],
    [
      "00b4ee3c",
      "READ",
      [
        "storage",
        "00c1b828",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ed6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4ed4c.md#insn-00b4ed6c) · [`00b4ed8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4ed4c.md#insn-00b4ed8c) · [`00b4eda0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4ed4c.md#insn-00b4eda0)
- 新版 `00b4ee68`（命令位置の公開資料なし）

~~~diff
- 00b4ed6c ["INT_ADD", "register:40f0:8", ["const:b4ed6c:8", "const:4:8"]]
- 00b4ed6c ["CALL", null, ["callee:00bdddd0:8"]]
- 00b4ed6c bytes ed3b0294
- 00b4ed8c ["INT_ADD", "register:40f0:8", ["const:b4ed8c:8", "const:4:8"]]
- 00b4ed8c ["CALL", null, ["callee:00bdaf90:8"]]
- 00b4ed8c bytes 55300294
- 00b4eda0 ["INT_ADD", "register:40f0:8", ["const:b4eda0:8", "const:4:8"]]
- 00b4eda0 ["CALL", null, ["callee:00bdddd0:8"]]
+ 00b4ee68 ["INT_ADD", "register:40f0:8", ["const:b4ee68:8", "const:4:8"]]
+ 00b4ee68 ["CALL", null, ["callee:00bdddd0:8"]]
- 00b4eda0 bytes e03b0294
+ 00b4ee68 bytes da3b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55aef5c221e8b3cc8e0d9ff035ec93a8"></a>

### [`00b4edc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4edc0.md) → [`00b4ee88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ee88.md) _ZNK8firebase9messaging8internal13MessageReader14ReadFromBufferERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0460.md) · 呼出先 4件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00be0400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0400.md) [`00be0450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0450.md)
- 新版 呼出元 1件 [`00be0510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0510.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00be04b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04b0.md) [`00be0500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0500.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.87% / 新版 61.87%

CFGの説明率　旧版 7.81% / 新版 7.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 3件, `unresolved_branch_alignment` 11件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4edd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4edd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4edd8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4edd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4edd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4eec8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4efb8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ee9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4eea0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4eec8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4f080"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4edd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4edc0.md#insn-00b4edd4) · [`00b4edd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4edc0.md#insn-00b4edd8) · [`00b4edfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4edc0.md#insn-00b4edfc)

~~~diff
- 00b4edd4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4edd4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4edd4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00b4edd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4edd4 bytes f44f09a9
- 00b4edd8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4edd8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4edd8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00b4edd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4edd8 bytes fd7b0aa9
- 00b4edfc ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b4edfc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b4edfc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b4edfc ["COPY", "register:40b8:8", ["tmp:0:8"]]
- 00b4edfc bytes 5701899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c9bccaf7f6ce70b0dc0ba9f05611cae"></a>

### [`00b4efec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4efec.md) → [`00b4f0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4f/00b4f0b4.md) _ZNK8firebase9messaging8internal13MessageReader14ConsumeMessageEPKN3com6google8firebase9messaging3cpp17SerializedMessageE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0450.md) · 呼出先 13件 [`0044a6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a6d0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00be0500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0500.md) · 呼出先 13件 [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.43% / 新版 72.43%

CFGの説明率　旧版 18.84% / 新版 18.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_condition` 1件, `unresolved_branch_alignment` 30件, `unresolved_call_alignment` 13件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4effc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4effc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4f000"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4effc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4f000",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4f038",
      "WRITE",
      [
        "storage",
        "Stack[-0x180]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4f0c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4f0c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4f100",
      "WRITE",
      [
        "storage",
        "Stack[-0x180]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4effc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4efec.md#insn-00b4effc) · [`00b4f000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4efec.md#insn-00b4f000) · [`00b4f038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4efec.md#insn-00b4f038)

~~~diff
- 00b4effc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4effc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4effc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b4effc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4effc bytes f44f04a9
- 00b4f000 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4f000 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4f000 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b4f000 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4f000 bytes fd7b05a9
- 00b4f038 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b4f038 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00b4f038 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00b4f038 ["INT_ADD", "tmp:3:8", ["register:8:8", "const:1c0:8"]]
- 00b4f038 bytes ff271ca9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e280a03d084c24933cbfd4f7a5bbca8"></a>

### [`00b52430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52430.md) → [`00b524f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b524f8.md) _ZN8firebase13remote_config10FutureData7DestroyEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddcf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddda0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b52510",
      "incomplete_value": true,
      "site": "00b52510",
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
      "definition_site": "00b52448",
      "incomplete_value": true,
      "site": "00b52448",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5251c",
      "incomplete_value": true,
      "site": "00b52520",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
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
      "00b52508",
      "READ",
      [
        "storage",
        "00c1b9e8",
        null,
        "pointer"
      ]
    ],
    [
      "00b5250c",
      "READ",
      [
        "storage",
        "010a1070",
        "_ZN8firebase13remote_config10FutureData14s_future_data_E",
        "undefined8"
      ]
    ],
    [
      "00b52528",
      "WRITE",
      [
        "storage",
        "010a1070",
        "_ZN8firebase13remote_config10FutureData14s_future_data_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b52508",
      "READ",
      [
        "storage",
        "00c1ba98",
        null,
        "pointer"
      ]
    ],
    [
      "00b5250c",
      "READ",
      [
        "storage",
        "010a1130",
        "_ZN8firebase13remote_config10FutureData14s_future_data_E",
        "undefined8"
      ]
    ],
    [
      "00b52528",
      "WRITE",
      [
        "storage",
        "010a1130",
        "_ZN8firebase13remote_config10FutureData14s_future_data_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52430.md#insn-00b52448) · [`00b52458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52430.md#insn-00b52458) · [`00b52440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52430.md#insn-00b52440)
- 新版 `00b52510`（命令位置の公開資料なし） · `00b52520`（命令位置の公開資料なし） · `00b52508`（命令位置の公開資料なし）

~~~diff
- 00b52448 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00b52448 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b52510 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00b52510 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b52448 bytes b30000b4
+ 00b52510 bytes b30000b4
- 00b52458 ["INT_ADD", "register:40f0:8", ["const:b52458:8", "const:4:8"]]
- 00b52458 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b52520 ["INT_ADD", "register:40f0:8", ["const:b52520:8", "const:4:8"]]
+ 00b52520 ["CALL", null, ["callee:00bdb010:8"]]
- 00b52458 bytes c2220294
+ 00b52520 bytes bc220294
- 00b52440 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9e8:8"]]
- 00b52440 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b52508 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a98:8"]]
+ 00b52508 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b52440 bytes 94f644f9
+ 00b52508 bytes 944e45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6b32b9c22e9f245507c21ab73fbede2"></a>

### [`00b5247c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b5247c.md) → [`00b52544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52544.md) _INIT_278

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b523d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b523d4.md) [`00b523dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b523dc.md) [`00bddc60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b5249c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b5249c.md) [`00b524a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b524a4.md) [`00bddd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd10.md)

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
      "definition_site": "00b52564",
      "incomplete_value": false,
      "site": "00b52564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5249c",
      "incomplete_value": false,
      "site": "00b5249c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:50:8"
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
      "definition_site": "00b52564",
      "incomplete_value": false,
      "site": "00b52564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:8fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5249c",
      "incomplete_value": false,
      "site": "00b5249c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:86f:8"
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
      "definition_site": "00b52564",
      "incomplete_value": false,
      "site": "00b52564",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:110:8"
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
      "definition_site": "00b5249c",
      "incomplete_value": false,
      "site": "00b5249c",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:50:8"
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
      "00b52554",
      "PARAM",
      [
        "storage",
        "010a1050",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52564",
      "WRITE",
      [
        "storage",
        "010a1050",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52564",
      "DATA",
      [
        "storage",
        "0029986f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b52554",
      "PARAM",
      [
        "storage",
        "010a1110",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52564",
      "WRITE",
      [
        "storage",
        "010a1110",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52564",
      "DATA",
      [
        "storage",
        "002998fc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5248c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b5247c.md#insn-00b5248c) · [`00b52490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b5247c.md#insn-00b52490) · [`00b52494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b5247c.md#insn-00b52494)
- 新版 `00b52554`（命令位置の公開資料なし） · `00b52558`（命令位置の公開資料なし） · `00b5255c`（命令位置の公開資料なし）

~~~diff
- 00b5248c ["COPY", "tmp:0:8", ["const:50:8"]]
- 00b5248c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5248c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5248c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b52554 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 00b52554 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b52554 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b52554 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5248c bytes 00400191
+ 00b52554 bytes 00400491
- 00b52490 ["COPY", "tmp:0:8", ["const:86f:8"]]
- 00b52490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b52490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b52490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b52558 ["COPY", "tmp:0:8", ["const:8fc:8"]]
+ 00b52558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b52558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b52558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b52490 bytes 08bd2191
+ 00b52558 bytes 08f12391
- 00b52494 ["COPY", "tmp:0:8", ["const:3d4:8"]]
- 00b52494 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b52494 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b52494 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b5255c ["COPY", "tmp:0:8", ["const:49c:8"]]
+ 00b5255c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b5255c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b5255c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b52494 bytes 29510f91
+ 00b5255c bytes 29711291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d09096978c3934e9c0680582f4b455cb"></a>

### [`00b524b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b524b4.md) → [`00b5257c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b5257c.md) _ZN8firebase13remote_config12RemoteConfig11GetInstanceEPNS_3AppE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddbe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddbe0.md) · 呼出先 11件 [`00b52bbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52bbc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddc90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc90.md)
- 新版 呼出元 1件 [`00bddc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc90.md) · 呼出先 11件 [`00b52c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52c84.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd40.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 97.67% / 新版 97.67%

CFGの説明率　旧版 53.85% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 1件, `unresolved_branch_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b525b8",
      "incomplete_value": true,
      "site": "00b525b8",
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
      "definition_site": "00b524f0",
      "incomplete_value": true,
      "site": "00b524f0",
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
      "site": "00b52668"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b52730"
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
      "00b52594",
      "READ",
      [
        "storage",
        "00c1ba00",
        null,
        "pointer"
      ]
    ],
    [
      "00b5259c",
      "PARAM",
      [
        "storage",
        "010a1090",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ],
    [
      "00b525a4",
      "PARAM",
      [
        "storage",
        "010a1090",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00b52594",
      "READ",
      [
        "storage",
        "00c1bab0",
        null,
        "pointer"
      ]
    ],
    [
      "00b5259c",
      "PARAM",
      [
        "storage",
        "010a1150",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ],
    [
      "00b525a4",
      "PARAM",
      [
        "storage",
        "010a1150",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b524d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b524b4.md#insn-00b524d8) · [`00b52534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b524b4.md#insn-00b52534) · [`00b52554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b524b4.md#insn-00b52554)
- 新版 `00b525a0`（命令位置の公開資料なし） · `00b525fc`（命令位置の公開資料なし） · `00b5261c`（命令位置の公開資料なし）

~~~diff
- 00b524d8 ["INT_ADD", "register:40f0:8", ["const:b524d8:8", "const:4:8"]]
- 00b524d8 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b525a0 ["INT_ADD", "register:40f0:8", ["const:b525a0:8", "const:4:8"]]
+ 00b525a0 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b524d8 bytes 922d0294
+ 00b525a0 bytes 8c2d0294
- 00b52534 ["INT_ADD", "register:40f0:8", ["const:b52534:8", "const:4:8"]]
- 00b52534 ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b525fc ["INT_ADD", "register:40f0:8", ["const:b525fc:8", "const:4:8"]]
+ 00b525fc ["CALL", null, ["callee:00bddbe0:8"]]
- 00b52534 bytes 7f2d0294
+ 00b525fc bytes 792d0294
- 00b52554 ["INT_ADD", "register:40f0:8", ["const:b52554:8", "const:4:8"]]
- 00b52554 ["CALL", null, ["callee:00bde130:8"]]
+ 00b5261c ["INT_ADD", "register:40f0:8", ["const:b5261c:8", "const:4:8"]]
+ 00b5261c ["CALL", null, ["callee:00bde130:8"]]
- 00b52554 bytes cb2e0294
+ 00b5261c bytes c52e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a37f52d9c82a05f0957590b7de417a9"></a>

### [`00b52708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52708.md) → [`00b527d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b527d0.md) _ZN8firebase13remote_config12RemoteConfig16FindRemoteConfigEPNS_3AppE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 15.38% / 新版 15.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b52708"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5270c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5270c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b52708",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5270c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b527e4",
      "READ",
      [
        "storage",
        "00c1ba00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b527d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b527d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b527e4",
      "READ",
      [
        "storage",
        "00c1bab0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52708.md#insn-00b52708) · [`00b5270c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52708.md#insn-00b5270c) · [`00b52720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52708.md#insn-00b52720)
- 新版 `00b527e8`（命令位置の公開資料なし）

~~~diff
- 00b52708 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b52708 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b52708 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b52708 bytes f30f1ef8
- 00b5270c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5270c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5270c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5270c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5270c bytes fd7b01a9
- 00b52720 ["INT_ADD", "register:40f0:8", ["const:b52720:8", "const:4:8"]]
- 00b52720 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b527e8 ["INT_ADD", "register:40f0:8", ["const:b527e8:8", "const:4:8"]]
+ 00b527e8 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b52720 bytes 002d0294
+ 00b527e8 bytes fa2c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5a18856008aec964e526af303f82d5c"></a>

### [`00b5279c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b5279c.md) → [`00b52864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52864.md) _ZN8firebase13remote_config12RemoteConfig14DeleteInternalEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be05d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be05d0.md) · 呼出先 8件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddc90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc90.md) [`00bddcb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcb0.md)
- 新版 呼出元 1件 [`00be0680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0680.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd40.md) [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 40.62% / 新版 43.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b528c8",
      "incomplete_value": true,
      "site": "00b528c8",
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
      "definition_site": "00b52800",
      "incomplete_value": true,
      "site": "00b52800",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5281c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5283c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b52878",
      "READ",
      [
        "storage",
        "00c1ba00",
        null,
        "pointer"
      ]
    ],
    [
      "00b52878",
      "PARAM",
      [
        "storage",
        "010a1090",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ],
    [
      "unmatched:00b527ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb010"
      ]
    ]
  ],
  "added": [
    [
      "00b52878",
      "READ",
      [
        "storage",
        "00c1bab0",
        null,
        "pointer"
      ]
    ],
    [
      "00b52878",
      "PARAM",
      [
        "storage",
        "010a1150",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ],
    [
      "00b528c0",
      "READ",
      [
        "storage",
        "00c1bab8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b527b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b5279c.md#insn-00b527b4) · [`00b527e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b5279c.md#insn-00b527e4) · [`00b527ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b5279c.md#insn-00b527ec)
- 新版 `00b5287c`（命令位置の公開資料なし） · `00b528ac`（命令位置の公開資料なし）

~~~diff
- 00b527b4 ["INT_ADD", "register:40f0:8", ["const:b527b4:8", "const:4:8"]]
- 00b527b4 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b5287c ["INT_ADD", "register:40f0:8", ["const:b5287c:8", "const:4:8"]]
+ 00b5287c ["CALL", null, ["callee:00bddbd0:8"]]
- 00b527b4 bytes db2c0294
+ 00b5287c bytes d52c0294
- 00b527e4 ["INT_ADD", "register:40f0:8", ["const:b527e4:8", "const:4:8"]]
- 00b527e4 ["CALL", null, ["callee:00be0830:8"]]
+ 00b528ac ["INT_ADD", "register:40f0:8", ["const:b528ac:8", "const:4:8"]]
+ 00b528ac ["CALL", null, ["callee:00be0830:8"]]
- 00b527e4 bytes e7370294
+ 00b528ac bytes e1370294
- 00b527ec ["INT_ADD", "register:40f0:8", ["const:b527ec:8", "const:4:8"]]
- 00b527ec ["CALL", null, ["callee:00bdb010:8"]]
- 00b527ec bytes dd210294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc1aca8d6d6eda49e2fd84221f03a991"></a>

### [`00b528e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b528e8.md) → [`00b529b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b529b0.md) _ZN8firebase13remote_config12RemoteConfigC1EPNS_3AppE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00be0770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0770.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00be0820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0820.md)

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
      "definition_site": "00b529d0",
      "incomplete_value": false,
      "site": "00b529d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:e4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52908",
      "incomplete_value": false,
      "site": "00b5290c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dbf:8"
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
      "00b529d0",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b529d0",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5290c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b528e8.md#insn-00b5290c) · [`00b52908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b528e8.md#insn-00b52908) · [`00b52918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b528e8.md#insn-00b52918)
- 新版 `00b529d4`（命令位置の公開資料なし） · `00b529d0`（命令位置の公開資料なし） · `00b529e0`（命令位置の公開資料なし）

~~~diff
- 00b5290c ["INT_ADD", "register:40f0:8", ["const:b5290c:8", "const:4:8"]]
- 00b5290c ["CALL", null, ["callee:00bde130:8"]]
+ 00b529d4 ["INT_ADD", "register:40f0:8", ["const:b529d4:8", "const:4:8"]]
+ 00b529d4 ["CALL", null, ["callee:00bde130:8"]]
- 00b5290c bytes dd2d0294
+ 00b529d4 bytes d72d0294
- 00b52908 ["COPY", "tmp:0:8", ["const:dbf:8"]]
- 00b52908 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b52908 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b52908 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b529d0 ["COPY", "tmp:0:8", ["const:e4c:8"]]
+ 00b529d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b529d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b529d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b52908 bytes 00fc3691
+ 00b529d0 bytes 00303991
- 00b52918 ["INT_ADD", "register:40f0:8", ["const:b52918:8", "const:4:8"]]
- 00b52918 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b529e0 ["INT_ADD", "register:40f0:8", ["const:b529e0:8", "const:4:8"]]
+ 00b529e0 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b52918 bytes 8a210294
+ 00b529e0 bytes 84210294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8476ba09bd0067bcfede5263c5b1bb98"></a>

### [`00b52950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52950.md) → [`00b52a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52a18.md) _ZN8firebase13remote_config12RemoteConfigD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be05d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be05d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be0680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0680.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b52958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52950.md#insn-00b52958)
- 新版 `00b52a20`（命令位置の公開資料なし）

~~~diff
- 00b52958 ["INT_ADD", "register:40f0:8", ["const:b52958:8", "const:4:8"]]
- 00b52958 ["CALL", null, ["callee:00be0680:8"]]
+ 00b52a20 ["INT_ADD", "register:40f0:8", ["const:b52a20:8", "const:4:8"]]
+ 00b52a20 ["CALL", null, ["callee:00be0680:8"]]
- 00b52958 bytes 1e370294
+ 00b52a20 bytes 18370294
~~~


<a id="compare-ee1cfb99c682e7a99018aa1f9e077143"></a>

### [`00b52970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52970.md) → [`00b52a38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52a38.md) _ZN8firebase13remote_config12RemoteConfig27EnsureInitializedLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be06c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be06c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be0770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0770.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b52974",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00be0770"
      ]
    ]
  ],
  "added": [
    [
      "00b52a3c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00be0770"
      ]
    ]
  ]
}
~~~


<a id="compare-fd890a1df32c96df2a27148728440126"></a>

### [`00b52998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52998.md) → [`00b52a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52a60.md) _ZN8firebase13remote_config12RemoteConfig5FetchEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be0660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0660.md) [`00be06e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be06e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be0710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0710.md) [`00be0790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0790.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b529b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52998.md#insn-00b529b0)
- 新版 `00b52a78`（命令位置の公開資料なし）

~~~diff
- 00b529b0 ["INT_ADD", "register:40f0:8", ["const:b529b0:8", "const:4:8"]]
- 00b529b0 ["CALL", null, ["callee:00be0710:8"]]
+ 00b52a78 ["INT_ADD", "register:40f0:8", ["const:b52a78:8", "const:4:8"]]
+ 00b52a78 ["CALL", null, ["callee:00be0710:8"]]
- 00b529b0 bytes 2c370294
+ 00b52a78 bytes 26370294
~~~


<a id="compare-55842ed41f5c7057224c222efd351763"></a>

### [`00b52a38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52a38.md) → [`00b52b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52b00.md) _ZN8firebase13remote_config12RemoteConfig10GetBooleanEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be05e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be05e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be0690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0690.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b52a3c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00be0690"
      ]
    ]
  ],
  "added": [
    [
      "00b52b04",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00be0690"
      ]
    ]
  ]
}
~~~


<a id="compare-71edc637fa24bc11cbcfda83bcbf05e3"></a>

### [`00b52aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52aa8.md) → [`00b52b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52b70.md) _ZN8firebase13remote_config12RemoteConfig7GetInfoEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be07a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be07a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be0850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0850.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b52aac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00be0850"
      ]
    ]
  ],
  "added": [
    [
      "00b52b74",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00be0850"
      ]
    ]
  ]
}
~~~


<a id="compare-af580bf61fc9be0e7a42963c3955fe5c"></a>

### [`00b52bbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52bbc.md) → [`00b52c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52c84.md) FUN_00b52c84

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b524b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b524b4.md) · 呼出先 2件 [`00bdde60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde60.md) [`00be05d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be05d0.md)
- 新版 呼出元 1件 [`00b5257c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b5257c.md) · 呼出先 2件 [`00bddf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf10.md) [`00be0680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0680.md)

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
      "definition_site": "00b52c9c",
      "incomplete_value": false,
      "site": "00b52ca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:f6d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52bd4",
      "incomplete_value": false,
      "site": "00b52bdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
      "00b52c9c",
      "PARAM",
      [
        "storage",
        "0029bee0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b52c9c",
      "PARAM",
      [
        "storage",
        "0029bf6d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52bdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52bbc.md#insn-00b52bdc) · [`00b52bd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52bbc.md#insn-00b52bd4)
- 新版 `00b52ca4`（命令位置の公開資料なし） · `00b52c9c`（命令位置の公開資料なし）

~~~diff
- 00b52bdc ["INT_ADD", "register:40f0:8", ["const:b52bdc:8", "const:4:8"]]
- 00b52bdc ["CALL", null, ["callee:00bddf10:8"]]
+ 00b52ca4 ["INT_ADD", "register:40f0:8", ["const:b52ca4:8", "const:4:8"]]
+ 00b52ca4 ["CALL", null, ["callee:00bddf10:8"]]
- 00b52bdc bytes a12c0294
+ 00b52ca4 bytes 9b2c0294
- 00b52bd4 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 00b52bd4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b52bd4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b52bd4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b52c9c ["COPY", "tmp:0:8", ["const:f6d:8"]]
+ 00b52c9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b52c9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b52c9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b52bd4 bytes 00803b91
+ 00b52c9c bytes 00b43d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd5f1d2b5488b230ade814158622c070"></a>

### [`00b52c30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52c30.md) → [`00b52cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52cf8.md) _INIT_279

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b05384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05384.md) [`00b524ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b524ac.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bddd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd20.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b0544c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0544c.md) [`00b52574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52574.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md)

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
      "definition_site": "00b52d1c",
      "incomplete_value": true,
      "site": "00b52d1c",
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
      "definition_site": "00b52c54",
      "incomplete_value": true,
      "site": "00b52c54",
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
      "definition_site": "00b52d28",
      "incomplete_value": true,
      "site": "00b52d28",
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
      "definition_site": "00b52c60",
      "incomplete_value": true,
      "site": "00b52c60",
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
      "definition_site": "00b52d2c",
      "incomplete_value": true,
      "site": "00b52d2c",
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
                "const:c1b000:8"
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
    "old": {
      "definition_site": "00b52c64",
      "incomplete_value": true,
      "site": "00b52c64",
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
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:a08:8"
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
      "00b52d08",
      "READ",
      [
        "storage",
        "00c1ba08",
        null,
        "pointer"
      ]
    ],
    [
      "00b52d08",
      "PARAM",
      [
        "storage",
        "010a1078",
        "_ZN8firebase13remote_config5g_rcsE",
        "undefined8"
      ]
    ],
    [
      "00b52d1c",
      "WRITE",
      [
        "storage",
        "010a1080",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b52d08",
      "READ",
      [
        "storage",
        "00c1bab8",
        null,
        "pointer"
      ]
    ],
    [
      "00b52d08",
      "PARAM",
      [
        "storage",
        "010a1138",
        "_ZN8firebase13remote_config5g_rcsE",
        "undefined8"
      ]
    ],
    [
      "00b52d1c",
      "WRITE",
      [
        "storage",
        "010a1140",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52c68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52c30.md#insn-00b52c68) · [`00b52c7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52c30.md#insn-00b52c7c) · [`00b52c40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52c30.md#insn-00b52c40)
- 新版 `00b52d30`（命令位置の公開資料なし） · `00b52d44`（命令位置の公開資料なし） · `00b52d08`（命令位置の公開資料なし）

~~~diff
- 00b52c68 ["INT_ADD", "register:40f0:8", ["const:b52c68:8", "const:4:8"]]
- 00b52c68 ["CALL", null, ["callee:00bdaf90:8"]]
+ 00b52d30 ["INT_ADD", "register:40f0:8", ["const:b52d30:8", "const:4:8"]]
+ 00b52d30 ["CALL", null, ["callee:00bdaf90:8"]]
- 00b52c68 bytes 9e200294
+ 00b52d30 bytes 98200294
- 00b52c7c ["INT_ADD", "register:40f0:8", ["const:b52c7c:8", "const:4:8"]]
- 00b52c7c ["CALL", null, ["callee:00bdddd0:8"]]
+ 00b52d44 ["INT_ADD", "register:40f0:8", ["const:b52d44:8", "const:4:8"]]
+ 00b52d44 ["CALL", null, ["callee:00bdddd0:8"]]
- 00b52c7c bytes 292c0294
+ 00b52d44 bytes 232c0294
- 00b52c40 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:a08:8"]]
- 00b52c40 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b52d08 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ab8:8"]]
+ 00b52d08 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b52c40 bytes 210445f9
+ 00b52d08 bytes 215c45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e94395147127ebdaf6e985e58afbd802"></a>

### [`00b52c9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52c9c.md) → [`00b52d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52d64.md) _ZN8firebase13remote_config8internal6config19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allo

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b52d90",
      "incomplete_value": true,
      "site": "00b52d90",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52cc8",
      "incomplete_value": true,
      "site": "00b52cc8",
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
            "const:b8:8"
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
      "definition_site": "00b52d78",
      "incomplete_value": true,
      "site": "00b52d78",
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
      "definition_site": "00b52cb0",
      "incomplete_value": true,
      "site": "00b52cb0",
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
      "definition_site": "00b52d84",
      "incomplete_value": false,
      "site": "00b52d88",
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
            "const:f7f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52cbc",
      "incomplete_value": false,
      "site": "00b52cc0",
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
            "const:ef2:8"
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
      "00b52d74",
      "READ",
      [
        "storage",
        "010a10b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52d84",
      "PARAM",
      [
        "storage",
        "002a0ef2",
        null,
        "string"
      ]
    ],
    [
      "00b52d90",
      "WRITE",
      [
        "storage",
        "010a10b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b52d74",
      "READ",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52d84",
      "PARAM",
      [
        "storage",
        "002a0f7f",
        null,
        "string"
      ]
    ],
    [
      "00b52d90",
      "WRITE",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52cc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52c9c.md#insn-00b52cc0) · [`00b52cc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52c9c.md#insn-00b52cc8) · [`00b52cac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52c9c.md#insn-00b52cac)
- 新版 `00b52d88`（命令位置の公開資料なし） · `00b52d90`（命令位置の公開資料なし） · `00b52d74`（命令位置の公開資料なし）

~~~diff
- 00b52cc0 ["INT_ADD", "register:40f0:8", ["const:b52cc0:8", "const:4:8"]]
- 00b52cc0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b52d88 ["INT_ADD", "register:40f0:8", ["const:b52d88:8", "const:4:8"]]
+ 00b52d88 ["CALL", null, ["callee:00bde040:8"]]
- 00b52cc0 bytes b42c0294
+ 00b52d88 bytes ae2c0294
- 00b52cc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b8:8"]]
- 00b52cc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b52d90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:178:8"]]
+ 00b52d90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b52cc8 bytes 605e00f9
+ 00b52d90 bytes 60be00f9
- 00b52cac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b8:8"]]
- 00b52cac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b52d74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:178:8"]]
+ 00b52d74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b52cac bytes 685e40f9
+ 00b52d74 bytes 68be40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a84a28b7e5cad93c81a44581cacf7ed"></a>

### [`00b52cdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52cdc.md) → [`00b52da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52da4.md) _ZN8firebase13remote_config8internal6config19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allo

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b52dd0",
      "incomplete_value": true,
      "site": "00b52dd0",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52d08",
      "incomplete_value": true,
      "site": "00b52d08",
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
            "const:b8:8"
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
      "definition_site": "00b52db8",
      "incomplete_value": true,
      "site": "00b52db8",
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
      "definition_site": "00b52cf0",
      "incomplete_value": true,
      "site": "00b52cf0",
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
      "definition_site": "00b52dc0",
      "incomplete_value": false,
      "site": "00b52dc8",
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
            "const:f7f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52cf8",
      "incomplete_value": false,
      "site": "00b52d00",
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
            "const:ef2:8"
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
      "00b52db4",
      "READ",
      [
        "storage",
        "010a10b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52dc0",
      "PARAM",
      [
        "storage",
        "002a0ef2",
        null,
        "string"
      ]
    ],
    [
      "00b52dd0",
      "WRITE",
      [
        "storage",
        "010a10b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b52db4",
      "READ",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52dc0",
      "PARAM",
      [
        "storage",
        "002a0f7f",
        null,
        "string"
      ]
    ],
    [
      "00b52dd0",
      "WRITE",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52cdc.md#insn-00b52d00) · [`00b52d08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52cdc.md#insn-00b52d08) · [`00b52cec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52cdc.md#insn-00b52cec)
- 新版 `00b52dc8`（命令位置の公開資料なし） · `00b52dd0`（命令位置の公開資料なし） · `00b52db4`（命令位置の公開資料なし）

~~~diff
- 00b52d00 ["INT_ADD", "register:40f0:8", ["const:b52d00:8", "const:4:8"]]
- 00b52d00 ["CALL", null, ["callee:00bde040:8"]]
+ 00b52dc8 ["INT_ADD", "register:40f0:8", ["const:b52dc8:8", "const:4:8"]]
+ 00b52dc8 ["CALL", null, ["callee:00bde040:8"]]
- 00b52d00 bytes a42c0294
+ 00b52dc8 bytes 9e2c0294
- 00b52d08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b8:8"]]
- 00b52d08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b52dd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:178:8"]]
+ 00b52dd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b52d08 bytes 605e00f9
+ 00b52dd0 bytes 60be00f9
- 00b52cec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b8:8"]]
- 00b52cec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b52db4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:178:8"]]
+ 00b52db4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b52cec bytes 685e40f9
+ 00b52db4 bytes 68be40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bc0341f34d5a556562c472771a78b69"></a>

### [`00b52d1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52d1c.md) → [`00b52de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52de4.md) _ZN8firebase13remote_config8internal6config10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b52e14",
      "incomplete_value": true,
      "site": "00b52e14",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52d4c",
      "incomplete_value": true,
      "site": "00b52d4c",
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
            "const:b8:8"
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
      "definition_site": "00b52df8",
      "incomplete_value": true,
      "site": "00b52df8",
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
      "definition_site": "00b52d30",
      "incomplete_value": true,
      "site": "00b52d30",
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
      "definition_site": "00b52e04",
      "incomplete_value": false,
      "site": "00b52e0c",
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
            "const:f7f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52d3c",
      "incomplete_value": false,
      "site": "00b52d44",
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
            "const:ef2:8"
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
      "00b52df4",
      "READ",
      [
        "storage",
        "010a10b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52e04",
      "PARAM",
      [
        "storage",
        "002a0ef2",
        null,
        "string"
      ]
    ],
    [
      "00b52e14",
      "WRITE",
      [
        "storage",
        "010a10b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b52df4",
      "READ",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52e04",
      "PARAM",
      [
        "storage",
        "002a0f7f",
        null,
        "string"
      ]
    ],
    [
      "00b52e14",
      "WRITE",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52d1c.md#insn-00b52d44) · [`00b52d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52d1c.md#insn-00b52d4c) · [`00b52d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52d1c.md#insn-00b52d2c)
- 新版 `00b52e0c`（命令位置の公開資料なし） · `00b52e14`（命令位置の公開資料なし） · `00b52df4`（命令位置の公開資料なし）

~~~diff
- 00b52d44 ["INT_ADD", "register:40f0:8", ["const:b52d44:8", "const:4:8"]]
- 00b52d44 ["CALL", null, ["callee:00bde040:8"]]
+ 00b52e0c ["INT_ADD", "register:40f0:8", ["const:b52e0c:8", "const:4:8"]]
+ 00b52e0c ["CALL", null, ["callee:00bde040:8"]]
- 00b52d44 bytes 932c0294
+ 00b52e0c bytes 8d2c0294
- 00b52d4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b8:8"]]
- 00b52d4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b52e14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:178:8"]]
+ 00b52e14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b52d4c bytes 605e00f9
+ 00b52e14 bytes 60be00f9
- 00b52d2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b8:8"]]
- 00b52d2c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b52df4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:178:8"]]
+ 00b52df4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b52d2c bytes 685e40f9
+ 00b52df4 bytes 68be40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-588a3e0d19be0093943d205150729ee7"></a>

### [`00b52d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52d60.md) → [`00b52e28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52e28.md) _ZN8firebase13remote_config8internal6config10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b52e58",
      "incomplete_value": true,
      "site": "00b52e58",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52d90",
      "incomplete_value": true,
      "site": "00b52d90",
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
            "const:b8:8"
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
      "definition_site": "00b52e3c",
      "incomplete_value": true,
      "site": "00b52e3c",
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
      "definition_site": "00b52d74",
      "incomplete_value": true,
      "site": "00b52d74",
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
      "definition_site": "00b52e44",
      "incomplete_value": false,
      "site": "00b52e50",
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
            "const:f7f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52d7c",
      "incomplete_value": false,
      "site": "00b52d88",
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
            "const:ef2:8"
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
      "00b52e38",
      "READ",
      [
        "storage",
        "010a10b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52e44",
      "PARAM",
      [
        "storage",
        "002a0ef2",
        null,
        "string"
      ]
    ],
    [
      "00b52e58",
      "WRITE",
      [
        "storage",
        "010a10b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b52e38",
      "READ",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52e44",
      "PARAM",
      [
        "storage",
        "002a0f7f",
        null,
        "string"
      ]
    ],
    [
      "00b52e58",
      "WRITE",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52d60.md#insn-00b52d88) · [`00b52d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52d60.md#insn-00b52d90) · [`00b52d70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52d60.md#insn-00b52d70)
- 新版 `00b52e50`（命令位置の公開資料なし） · `00b52e58`（命令位置の公開資料なし） · `00b52e38`（命令位置の公開資料なし）

~~~diff
- 00b52d88 ["INT_ADD", "register:40f0:8", ["const:b52d88:8", "const:4:8"]]
- 00b52d88 ["CALL", null, ["callee:00bde040:8"]]
+ 00b52e50 ["INT_ADD", "register:40f0:8", ["const:b52e50:8", "const:4:8"]]
+ 00b52e50 ["CALL", null, ["callee:00bde040:8"]]
- 00b52d88 bytes 822c0294
+ 00b52e50 bytes 7c2c0294
- 00b52d90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b8:8"]]
- 00b52d90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b52e58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:178:8"]]
+ 00b52e58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b52d90 bytes 605e00f9
+ 00b52e58 bytes 60be00f9
- 00b52d70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b8:8"]]
- 00b52d70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b52e38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:178:8"]]
+ 00b52e38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b52d70 bytes 685e40f9
+ 00b52e38 bytes 68be40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a1e83e7ce05b6af6810e8c40e515e3f"></a>

### [`00b52db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52db0.md) → [`00b52e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52e78.md) _ZN8firebase13remote_config8internal6config15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b52ed0",
      "incomplete_value": true,
      "site": "00b52ed0",
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
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52e08",
      "incomplete_value": true,
      "site": "00b52e08",
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
            "const:c0:8"
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
      "definition_site": "00b52eac",
      "incomplete_value": true,
      "site": "00b52eb8",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:178:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52de4",
      "incomplete_value": true,
      "site": "00b52df0",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:b8:8"
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
      "00b52e8c",
      "READ",
      [
        "storage",
        "010a10c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b52eac",
      "READ",
      [
        "storage",
        "010a10b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52ed0",
      "WRITE",
      [
        "storage",
        "010a10c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b52e8c",
      "READ",
      [
        "storage",
        "010a1180",
        null,
        "undefined1"
      ]
    ],
    [
      "00b52eac",
      "READ",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52ed0",
      "WRITE",
      [
        "storage",
        "010a1180",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52db0.md#insn-00b52df0) · [`00b52e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52db0.md#insn-00b52e08) · [`00b52dc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52db0.md#insn-00b52dc4)
- 新版 `00b52eb8`（命令位置の公開資料なし） · `00b52ed0`（命令位置の公開資料なし） · `00b52e8c`（命令位置の公開資料なし）

~~~diff
- 00b52df0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b52df0 ["INT_ADD", "register:40f0:8", ["const:b52df0:8", "const:4:8"]]
- 00b52df0 ["CALLIND", null, ["register:0:8"]]
+ 00b52eb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b52eb8 ["INT_ADD", "register:40f0:8", ["const:b52eb8:8", "const:4:8"]]
+ 00b52eb8 ["CALLIND", null, ["register:0:8"]]
- 00b52df0 bytes 00013fd6
+ 00b52eb8 bytes 00013fd6
- 00b52e08 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b52e08 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c0:8"]]
- 00b52e08 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b52ed0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b52ed0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:180:8"]]
+ 00b52ed0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b52e08 bytes a0020339
+ 00b52ed0 bytes a0020639
- 00b52dc4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c0:8"]]
- 00b52dc4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b52dc4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b52e8c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:180:8"]]
+ 00b52e8c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b52e8c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b52dc4 bytes a8024339
+ 00b52e8c bytes a8024639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9920f089ff78fb54112b864524c91b48"></a>

### [`00b52e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52e1c.md) → [`00b52ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52ee4.md) _ZN8firebase13remote_config8internal6config12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b52f20",
      "incomplete_value": true,
      "site": "00b52f20",
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
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52e58",
      "incomplete_value": true,
      "site": "00b52e58",
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
            "const:c0:8"
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
      "definition_site": "00b52f40",
      "incomplete_value": true,
      "site": "00b52f40",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52e78",
      "incomplete_value": true,
      "site": "00b52e78",
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
            "const:b8:8"
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
      "definition_site": "00b52efc",
      "incomplete_value": true,
      "site": "00b52efc",
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
      "definition_site": "00b52e34",
      "incomplete_value": true,
      "site": "00b52e34",
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
      "00b52ef8",
      "READ",
      [
        "storage",
        "010a10b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52f04",
      "READ",
      [
        "storage",
        "010a10c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b52f20",
      "WRITE",
      [
        "storage",
        "010a10c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b52ef8",
      "READ",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52f04",
      "READ",
      [
        "storage",
        "010a1180",
        null,
        "undefined1"
      ]
    ],
    [
      "00b52f20",
      "WRITE",
      [
        "storage",
        "010a1180",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52e58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52e1c.md#insn-00b52e58) · [`00b52e74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52e1c.md#insn-00b52e74) · [`00b52e78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52e1c.md#insn-00b52e78)
- 新版 `00b52f20`（命令位置の公開資料なし） · `00b52f3c`（命令位置の公開資料なし） · `00b52f40`（命令位置の公開資料なし）

~~~diff
- 00b52e58 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b52e58 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b52e58 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c0:8"]]
- 00b52e58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b52f20 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b52f20 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b52f20 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:180:8"]]
+ 00b52f20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b52e58 bytes bf020339
+ 00b52f20 bytes bf020639
- 00b52e74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b52e74 ["INT_ADD", "register:40f0:8", ["const:b52e74:8", "const:4:8"]]
- 00b52e74 ["CALLIND", null, ["register:0:8"]]
+ 00b52f3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b52f3c ["INT_ADD", "register:40f0:8", ["const:b52f3c:8", "const:4:8"]]
+ 00b52f3c ["CALLIND", null, ["register:0:8"]]
- 00b52e74 bytes 00013fd6
+ 00b52f3c bytes 00013fd6
- 00b52e78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b8:8"]]
- 00b52e78 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b52e78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b52f40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:178:8"]]
+ 00b52f40 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b52f40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b52e78 bytes 9f5e00f9
+ 00b52f40 bytes 9fbe00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b36312751781afe6a13f66af99d5cc60"></a>

### [`00b52e8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52e8c.md) → [`00b52f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52f54.md) _ZN8firebase13remote_config8internal6config14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "definition_site": "00b52f94",
      "incomplete_value": true,
      "site": "00b52f94",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52ecc",
      "incomplete_value": true,
      "site": "00b52ecc",
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
            "const:b8:8"
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
      "definition_site": "00b52f70",
      "incomplete_value": true,
      "site": "00b52f70",
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
      "definition_site": "00b52ea8",
      "incomplete_value": true,
      "site": "00b52ea8",
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
      "definition_site": "00b52f78",
      "incomplete_value": false,
      "site": "00b52f8c",
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
            "const:f7f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52eb0",
      "incomplete_value": false,
      "site": "00b52ec4",
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
            "const:ef2:8"
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
      "00b52f68",
      "READ",
      [
        "storage",
        "010a10b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52f78",
      "PARAM",
      [
        "storage",
        "002a0ef2",
        null,
        "string"
      ]
    ],
    [
      "00b52f94",
      "WRITE",
      [
        "storage",
        "010a10b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b52f68",
      "READ",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52f78",
      "PARAM",
      [
        "storage",
        "002a0f7f",
        null,
        "string"
      ]
    ],
    [
      "00b52f94",
      "WRITE",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52ec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52e8c.md#insn-00b52ec4) · [`00b52ecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52e8c.md#insn-00b52ecc) · [`00b52ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52e8c.md#insn-00b52ea0)
- 新版 `00b52f8c`（命令位置の公開資料なし） · `00b52f94`（命令位置の公開資料なし） · `00b52f68`（命令位置の公開資料なし）

~~~diff
- 00b52ec4 ["INT_ADD", "register:40f0:8", ["const:b52ec4:8", "const:4:8"]]
- 00b52ec4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b52f8c ["INT_ADD", "register:40f0:8", ["const:b52f8c:8", "const:4:8"]]
+ 00b52f8c ["CALL", null, ["callee:00bde040:8"]]
- 00b52ec4 bytes 332c0294
+ 00b52f8c bytes 2d2c0294
- 00b52ecc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b8:8"]]
- 00b52ecc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b52f94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:178:8"]]
+ 00b52f94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b52ecc bytes 805e00f9
+ 00b52f94 bytes 80be00f9
- 00b52ea0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b8:8"]]
- 00b52ea0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b52f68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:178:8"]]
+ 00b52f68 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b52ea0 bytes 815e40f9
+ 00b52f68 bytes 81be40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f458791a3a755a59ad29fe629a3f36b"></a>

### [`00b52efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52efc.md) → [`00b52fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52fc4.md) _ZN8firebase13remote_config8internal6config11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b52fe0",
      "incomplete_value": false,
      "site": "00b52fe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52f18",
      "incomplete_value": false,
      "site": "00b52f1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
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
      "definition_site": "00b52ff0",
      "incomplete_value": true,
      "site": "00b52ffc",
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
      "definition_site": "00b52f28",
      "incomplete_value": true,
      "site": "00b52f34",
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
      "00b52fe0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b52ff0",
      "DATA",
      [
        "storage",
        "010a10c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b52fe0",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b52ff0",
      "DATA",
      [
        "storage",
        "010a1188",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52f1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52efc.md#insn-00b52f1c) · [`00b52f18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52efc.md#insn-00b52f18) · [`00b52f24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52efc.md#insn-00b52f24)
- 新版 `00b52fe4`（命令位置の公開資料なし） · `00b52fe0`（命令位置の公開資料なし） · `00b52fec`（命令位置の公開資料なし）

~~~diff
- 00b52f1c ["INT_ADD", "register:40f0:8", ["const:b52f1c:8", "const:4:8"]]
- 00b52f1c ["CALL", null, ["callee:00bde130:8"]]
+ 00b52fe4 ["INT_ADD", "register:40f0:8", ["const:b52fe4:8", "const:4:8"]]
+ 00b52fe4 ["CALL", null, ["callee:00bde130:8"]]
- 00b52f1c bytes 592c0294
+ 00b52fe4 bytes 532c0294
- 00b52f18 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b52f18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b52f18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b52f18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b52fe0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b52fe0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b52fe0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b52fe0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b52f18 bytes 001c1591
+ 00b52fe0 bytes 00501791
- 00b52f24 ["COPY", "tmp:0:8", ["const:c8:8"]]
- 00b52f24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b52f24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b52f24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b52fec ["COPY", "tmp:0:8", ["const:188:8"]]
+ 00b52fec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b52fec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b52fec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b52f24 bytes 08210391
+ 00b52fec bytes 08210691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a2aaae1c7718ac05bb99bd313057972"></a>

### [`00b52f38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52f38.md) → [`00b53000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53000.md) _ZN8firebase13remote_config8internal6config13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b53040",
      "incomplete_value": true,
      "site": "00b53040",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52f78",
      "incomplete_value": true,
      "site": "00b52f78",
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
            "const:b8:8"
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
      "definition_site": "00b5301c",
      "incomplete_value": true,
      "site": "00b5301c",
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
      "definition_site": "00b52f54",
      "incomplete_value": true,
      "site": "00b52f54",
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
      "definition_site": "00b53024",
      "incomplete_value": false,
      "site": "00b53038",
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
            "const:f7f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52f5c",
      "incomplete_value": false,
      "site": "00b52f70",
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
            "const:ef2:8"
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
      "00b53014",
      "READ",
      [
        "storage",
        "010a10b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53024",
      "PARAM",
      [
        "storage",
        "002a0ef2",
        null,
        "string"
      ]
    ],
    [
      "00b53040",
      "WRITE",
      [
        "storage",
        "010a10b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53014",
      "READ",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53024",
      "PARAM",
      [
        "storage",
        "002a0f7f",
        null,
        "string"
      ]
    ],
    [
      "00b53040",
      "WRITE",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52f70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52f38.md#insn-00b52f70) · [`00b52f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52f38.md#insn-00b52f78) · [`00b52f4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52f38.md#insn-00b52f4c)
- 新版 `00b53038`（命令位置の公開資料なし） · `00b53040`（命令位置の公開資料なし） · `00b53014`（命令位置の公開資料なし）

~~~diff
- 00b52f70 ["INT_ADD", "register:40f0:8", ["const:b52f70:8", "const:4:8"]]
- 00b52f70 ["CALL", null, ["callee:00bde040:8"]]
+ 00b53038 ["INT_ADD", "register:40f0:8", ["const:b53038:8", "const:4:8"]]
+ 00b53038 ["CALL", null, ["callee:00bde040:8"]]
- 00b52f70 bytes 082c0294
+ 00b53038 bytes 022c0294
- 00b52f78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b8:8"]]
- 00b52f78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53040 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:178:8"]]
+ 00b53040 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b52f78 bytes 805e00f9
+ 00b53040 bytes 80be00f9
- 00b52f4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b8:8"]]
- 00b52f4c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53014 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:178:8"]]
+ 00b53014 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b52f4c bytes 815e40f9
+ 00b53014 bytes 81be40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a87081568098f249e5c7c2a1eaded7c3"></a>

### [`00b52fa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52fa8.md) → [`00b53070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53070.md) _ZN8firebase13remote_config8internal6config10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b5308c",
      "incomplete_value": false,
      "site": "00b53090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:67f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52fc4",
      "incomplete_value": false,
      "site": "00b52fc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:5f2:8"
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
      "definition_site": "00b5309c",
      "incomplete_value": true,
      "site": "00b530a8",
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
      "definition_site": "00b52fd4",
      "incomplete_value": true,
      "site": "00b52fe0",
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
      "00b5308c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b5309c",
      "DATA",
      [
        "storage",
        "010a1150",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5308c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b5309c",
      "DATA",
      [
        "storage",
        "010a1210",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52fc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52fa8.md#insn-00b52fc8) · [`00b52fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52fa8.md#insn-00b52fc4) · [`00b52fd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52fa8.md#insn-00b52fd0)
- 新版 `00b53090`（命令位置の公開資料なし） · `00b5308c`（命令位置の公開資料なし） · `00b53098`（命令位置の公開資料なし）

~~~diff
- 00b52fc8 ["INT_ADD", "register:40f0:8", ["const:b52fc8:8", "const:4:8"]]
- 00b52fc8 ["CALL", null, ["callee:00bde130:8"]]
+ 00b53090 ["INT_ADD", "register:40f0:8", ["const:b53090:8", "const:4:8"]]
+ 00b53090 ["CALL", null, ["callee:00bde130:8"]]
- 00b52fc8 bytes 2e2c0294
+ 00b53090 bytes 282c0294
- 00b52fc4 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b52fc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b52fc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b52fc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5308c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b5308c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5308c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5308c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b52fc4 bytes 00c81791
+ 00b5308c bytes 00fc1991
- 00b52fd0 ["COPY", "tmp:0:8", ["const:150:8"]]
- 00b52fd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b52fd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b52fd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b53098 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 00b53098 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53098 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53098 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b52fd0 bytes 08410591
+ 00b53098 bytes 08410891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b21334d2fe4a7d8c9d012d8a13c32a94"></a>

### [`00b52fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52fe4.md) → [`00b530ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b530ac.md) _ZN8firebase13remote_config8internal12config_value19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b530d8",
      "incomplete_value": true,
      "site": "00b530d8",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53010",
      "incomplete_value": true,
      "site": "00b53010",
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
            "const:158:8"
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
      "definition_site": "00b530c0",
      "incomplete_value": true,
      "site": "00b530c0",
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
      "definition_site": "00b52ff8",
      "incomplete_value": true,
      "site": "00b52ff8",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b52ff8"
      ],
      [
        "FALL_THROUGH",
        "00b530c0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b530c0",
      "incomplete_value": true,
      "site": "00b530d8",
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
      "definition_site": "00b52ff8",
      "incomplete_value": true,
      "site": "00b53010",
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
    "ordinal": 3,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b530bc",
      "READ",
      [
        "storage",
        "010a1158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b530d8",
      "WRITE",
      [
        "storage",
        "010a1158",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b530bc",
      "READ",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b530d8",
      "WRITE",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52fe4.md#insn-00b53010) · [`00b52ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52fe4.md#insn-00b52ff4) · [`00b53008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52fe4.md#insn-00b53008)
- 新版 `00b530d8`（命令位置の公開資料なし） · `00b530bc`（命令位置の公開資料なし） · `00b530d0`（命令位置の公開資料なし）

~~~diff
- 00b53010 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
- 00b53010 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b530d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
+ 00b530d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53010 bytes 60ae00f9
+ 00b530d8 bytes 600e01f9
- 00b52ff4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
- 00b52ff4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b530bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
+ 00b530bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b52ff4 bytes 68ae40f9
+ 00b530bc bytes 680e41f9
- 00b53008 ["INT_ADD", "register:40f0:8", ["const:b53008:8", "const:4:8"]]
- 00b53008 ["CALL", null, ["callee:00bde040:8"]]
+ 00b530d0 ["INT_ADD", "register:40f0:8", ["const:b530d0:8", "const:4:8"]]
+ 00b530d0 ["CALL", null, ["callee:00bde040:8"]]
- 00b53008 bytes e22b0294
+ 00b530d0 bytes dc2b0294
~~~


<a id="compare-730141c439eab33e6f92c6a4edb42046"></a>

### [`00b53024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53024.md) → [`00b530ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b530ec.md) _ZN8firebase13remote_config8internal12config_value19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b53118",
      "incomplete_value": true,
      "site": "00b53118",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53050",
      "incomplete_value": true,
      "site": "00b53050",
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
            "const:158:8"
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
      "definition_site": "00b53100",
      "incomplete_value": true,
      "site": "00b53100",
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
      "definition_site": "00b53038",
      "incomplete_value": true,
      "site": "00b53038",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b53038"
      ],
      [
        "FALL_THROUGH",
        "00b53100"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b53100",
      "incomplete_value": true,
      "site": "00b53118",
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
      "definition_site": "00b53038",
      "incomplete_value": true,
      "site": "00b53050",
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
    "ordinal": 3,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b530fc",
      "READ",
      [
        "storage",
        "010a1158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53118",
      "WRITE",
      [
        "storage",
        "010a1158",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b530fc",
      "READ",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53118",
      "WRITE",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53024.md#insn-00b53050) · [`00b53034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53024.md#insn-00b53034) · [`00b53048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53024.md#insn-00b53048)
- 新版 `00b53118`（命令位置の公開資料なし） · `00b530fc`（命令位置の公開資料なし） · `00b53110`（命令位置の公開資料なし）

~~~diff
- 00b53050 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
- 00b53050 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53118 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
+ 00b53118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53050 bytes 60ae00f9
+ 00b53118 bytes 600e01f9
- 00b53034 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
- 00b53034 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b530fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
+ 00b530fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53034 bytes 68ae40f9
+ 00b530fc bytes 680e41f9
- 00b53048 ["INT_ADD", "register:40f0:8", ["const:b53048:8", "const:4:8"]]
- 00b53048 ["CALL", null, ["callee:00bde040:8"]]
+ 00b53110 ["INT_ADD", "register:40f0:8", ["const:b53110:8", "const:4:8"]]
+ 00b53110 ["CALL", null, ["callee:00bde040:8"]]
- 00b53048 bytes d22b0294
+ 00b53110 bytes cc2b0294
~~~


<a id="compare-e5886bd0624a9ada641fb4e0ad744688"></a>

### [`00b53064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53064.md) → [`00b5312c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5312c.md) _ZN8firebase13remote_config8internal12config_value10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5315c",
      "incomplete_value": true,
      "site": "00b5315c",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53094",
      "incomplete_value": true,
      "site": "00b53094",
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
            "const:158:8"
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
      "definition_site": "00b53140",
      "incomplete_value": true,
      "site": "00b53140",
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
      "definition_site": "00b53078",
      "incomplete_value": true,
      "site": "00b53078",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b53078"
      ],
      [
        "FALL_THROUGH",
        "00b53140"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b53140",
      "incomplete_value": true,
      "site": "00b5315c",
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
      "definition_site": "00b53078",
      "incomplete_value": true,
      "site": "00b53094",
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
    "ordinal": 3,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5313c",
      "READ",
      [
        "storage",
        "010a1158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5315c",
      "WRITE",
      [
        "storage",
        "010a1158",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5313c",
      "READ",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5315c",
      "WRITE",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53094`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53064.md#insn-00b53094) · [`00b53074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53064.md#insn-00b53074) · [`00b5308c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53064.md#insn-00b5308c)
- 新版 `00b5315c`（命令位置の公開資料なし） · `00b5313c`（命令位置の公開資料なし） · `00b53154`（命令位置の公開資料なし）

~~~diff
- 00b53094 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
- 00b53094 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5315c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
+ 00b5315c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53094 bytes 60ae00f9
+ 00b5315c bytes 600e01f9
- 00b53074 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
- 00b53074 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5313c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
+ 00b5313c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53074 bytes 68ae40f9
+ 00b5313c bytes 680e41f9
- 00b5308c ["INT_ADD", "register:40f0:8", ["const:b5308c:8", "const:4:8"]]
- 00b5308c ["CALL", null, ["callee:00bde040:8"]]
+ 00b53154 ["INT_ADD", "register:40f0:8", ["const:b53154:8", "const:4:8"]]
+ 00b53154 ["CALL", null, ["callee:00bde040:8"]]
- 00b5308c bytes c12b0294
+ 00b53154 bytes bb2b0294
~~~


<a id="compare-4b5a643688ab55948a7283fdaa23e468"></a>

### [`00b530a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b530a8.md) → [`00b53170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53170.md) _ZN8firebase13remote_config8internal12config_value10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b531a0",
      "incomplete_value": true,
      "site": "00b531a0",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b530d8",
      "incomplete_value": true,
      "site": "00b530d8",
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
            "const:158:8"
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
      "definition_site": "00b53184",
      "incomplete_value": true,
      "site": "00b53184",
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
      "definition_site": "00b530bc",
      "incomplete_value": true,
      "site": "00b530bc",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b530bc"
      ],
      [
        "FALL_THROUGH",
        "00b53184"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b53184",
      "incomplete_value": true,
      "site": "00b531a0",
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
      "definition_site": "00b530bc",
      "incomplete_value": true,
      "site": "00b530d8",
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
    "ordinal": 3,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b53180",
      "READ",
      [
        "storage",
        "010a1158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b531a0",
      "WRITE",
      [
        "storage",
        "010a1158",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53180",
      "READ",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b531a0",
      "WRITE",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b530d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b530a8.md#insn-00b530d8) · [`00b530b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b530a8.md#insn-00b530b8) · [`00b530d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b530a8.md#insn-00b530d0)
- 新版 `00b531a0`（命令位置の公開資料なし） · `00b53180`（命令位置の公開資料なし） · `00b53198`（命令位置の公開資料なし）

~~~diff
- 00b530d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
- 00b530d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b531a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
+ 00b531a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b530d8 bytes 60ae00f9
+ 00b531a0 bytes 600e01f9
- 00b530b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
- 00b530b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53180 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
+ 00b53180 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b530b8 bytes 68ae40f9
+ 00b53180 bytes 680e41f9
- 00b530d0 ["INT_ADD", "register:40f0:8", ["const:b530d0:8", "const:4:8"]]
- 00b530d0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b53198 ["INT_ADD", "register:40f0:8", ["const:b53198:8", "const:4:8"]]
+ 00b53198 ["CALL", null, ["callee:00bde040:8"]]
- 00b530d0 bytes b02b0294
+ 00b53198 bytes aa2b0294
~~~


<a id="compare-f799f3d3a4a903c344c65d12e0ce41fc"></a>

### [`00b530f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b530f8.md) → [`00b531c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b531c0.md) _ZN8firebase13remote_config8internal12config_value15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b53218",
      "incomplete_value": true,
      "site": "00b53218",
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
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53150",
      "incomplete_value": true,
      "site": "00b53150",
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
            "const:160:8"
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
      "definition_site": "00b531f4",
      "incomplete_value": true,
      "site": "00b53200",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:218:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5312c",
      "incomplete_value": true,
      "site": "00b53138",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:158:8"
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
      "00b531d4",
      "READ",
      [
        "storage",
        "010a1160",
        null,
        "undefined1"
      ]
    ],
    [
      "00b531f4",
      "READ",
      [
        "storage",
        "010a1158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53218",
      "WRITE",
      [
        "storage",
        "010a1160",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b531d4",
      "READ",
      [
        "storage",
        "010a1220",
        null,
        "undefined1"
      ]
    ],
    [
      "00b531f4",
      "READ",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53218",
      "WRITE",
      [
        "storage",
        "010a1220",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b530f8.md#insn-00b53138) · [`00b53150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b530f8.md#insn-00b53150) · [`00b5310c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b530f8.md#insn-00b5310c)
- 新版 `00b53200`（命令位置の公開資料なし） · `00b53218`（命令位置の公開資料なし） · `00b531d4`（命令位置の公開資料なし）

~~~diff
- 00b53138 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53138 ["INT_ADD", "register:40f0:8", ["const:b53138:8", "const:4:8"]]
- 00b53138 ["CALLIND", null, ["register:0:8"]]
+ 00b53200 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b53200 ["INT_ADD", "register:40f0:8", ["const:b53200:8", "const:4:8"]]
+ 00b53200 ["CALLIND", null, ["register:0:8"]]
- 00b53138 bytes 00013fd6
+ 00b53200 bytes 00013fd6
- 00b53150 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b53150 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:160:8"]]
- 00b53150 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b53218 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b53218 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:220:8"]]
+ 00b53218 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b53150 bytes a0820539
+ 00b53218 bytes a0820839
- 00b5310c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:160:8"]]
- 00b5310c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b5310c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b531d4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:220:8"]]
+ 00b531d4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b531d4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b5310c bytes a8824539
+ 00b531d4 bytes a8824839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-531b174349505a83ebcc8bf994e64d02"></a>

### [`00b53164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53164.md) → [`00b5322c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5322c.md) _ZN8firebase13remote_config8internal12config_value12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b53268",
      "incomplete_value": true,
      "site": "00b53268",
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
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b531a0",
      "incomplete_value": true,
      "site": "00b531a0",
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
            "const:160:8"
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
      "definition_site": "00b53288",
      "incomplete_value": true,
      "site": "00b53288",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b531c0",
      "incomplete_value": true,
      "site": "00b531c0",
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
            "const:158:8"
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
      "definition_site": "00b53244",
      "incomplete_value": true,
      "site": "00b53244",
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
      "definition_site": "00b5317c",
      "incomplete_value": true,
      "site": "00b5317c",
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
      "00b53240",
      "READ",
      [
        "storage",
        "010a1158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5324c",
      "READ",
      [
        "storage",
        "010a1160",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53268",
      "WRITE",
      [
        "storage",
        "010a1160",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b53240",
      "READ",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5324c",
      "READ",
      [
        "storage",
        "010a1220",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53268",
      "WRITE",
      [
        "storage",
        "010a1220",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b531a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53164.md#insn-00b531a0) · [`00b531bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53164.md#insn-00b531bc) · [`00b531c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53164.md#insn-00b531c0)
- 新版 `00b53268`（命令位置の公開資料なし） · `00b53284`（命令位置の公開資料なし） · `00b53288`（命令位置の公開資料なし）

~~~diff
- 00b531a0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b531a0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b531a0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:160:8"]]
- 00b531a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b53268 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b53268 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b53268 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:220:8"]]
+ 00b53268 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b531a0 bytes bf820539
+ 00b53268 bytes bf820839
- 00b531bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b531bc ["INT_ADD", "register:40f0:8", ["const:b531bc:8", "const:4:8"]]
- 00b531bc ["CALLIND", null, ["register:0:8"]]
+ 00b53284 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b53284 ["INT_ADD", "register:40f0:8", ["const:b53284:8", "const:4:8"]]
+ 00b53284 ["CALLIND", null, ["register:0:8"]]
- 00b531bc bytes 00013fd6
+ 00b53284 bytes 00013fd6
- 00b531c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:158:8"]]
- 00b531c0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b531c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b53288 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:218:8"]]
+ 00b53288 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b53288 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b531c0 bytes 9fae00f9
+ 00b53288 bytes 9f0e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0ab79470fdaad4af6ea852b3a59fcc9"></a>

### [`00b531d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b531d4.md) → [`00b5329c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5329c.md) _ZN8firebase13remote_config8internal12config_value14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b532dc",
      "incomplete_value": true,
      "site": "00b532dc",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53214",
      "incomplete_value": true,
      "site": "00b53214",
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
            "const:158:8"
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
      "definition_site": "00b532b8",
      "incomplete_value": true,
      "site": "00b532b8",
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
      "definition_site": "00b531f0",
      "incomplete_value": true,
      "site": "00b531f0",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b531f0"
      ],
      [
        "FALL_THROUGH",
        "00b532b8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b532b8",
      "incomplete_value": true,
      "site": "00b532dc",
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
      "definition_site": "00b531f0",
      "incomplete_value": true,
      "site": "00b53214",
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
      "00b532b0",
      "READ",
      [
        "storage",
        "010a1158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b532dc",
      "WRITE",
      [
        "storage",
        "010a1158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b532f0",
      "PARAM",
      [
        "storage",
        "00c11778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b532b0",
      "READ",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b532dc",
      "WRITE",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b532f0",
      "PARAM",
      [
        "storage",
        "00c11828",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b531d4.md#insn-00b53214) · [`00b531e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b531d4.md#insn-00b531e8) · [`00b5320c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b531d4.md#insn-00b5320c)
- 新版 `00b532dc`（命令位置の公開資料なし） · `00b532b0`（命令位置の公開資料なし） · `00b532d4`（命令位置の公開資料なし）

~~~diff
- 00b53214 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:158:8"]]
- 00b53214 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b532dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:218:8"]]
+ 00b532dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53214 bytes 80ae00f9
+ 00b532dc bytes 800e01f9
- 00b531e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:158:8"]]
- 00b531e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b532b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:218:8"]]
+ 00b532b0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b531e8 bytes 81ae40f9
+ 00b532b0 bytes 810e41f9
- 00b5320c ["INT_ADD", "register:40f0:8", ["const:b5320c:8", "const:4:8"]]
- 00b5320c ["CALL", null, ["callee:00bde040:8"]]
+ 00b532d4 ["INT_ADD", "register:40f0:8", ["const:b532d4:8", "const:4:8"]]
+ 00b532d4 ["CALL", null, ["callee:00bde040:8"]]
- 00b5320c bytes 612b0294
+ 00b532d4 bytes 5b2b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b557cdbb240ebeab2f85e0e1a8f5c5f2"></a>

### [`00b53244`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53244.md) → [`00b5330c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5330c.md) _ZN8firebase13remote_config8internal12config_value11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b53328",
      "incomplete_value": false,
      "site": "00b5332c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53260",
      "incomplete_value": false,
      "site": "00b53264",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
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
      "definition_site": "00b53338",
      "incomplete_value": true,
      "site": "00b53344",
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
      "definition_site": "00b53270",
      "incomplete_value": true,
      "site": "00b5327c",
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
      "00b53328",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b53338",
      "DATA",
      [
        "storage",
        "010a1168",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53328",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b53338",
      "DATA",
      [
        "storage",
        "010a1228",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53244.md#insn-00b53264) · [`00b53260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53244.md#insn-00b53260) · [`00b5326c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53244.md#insn-00b5326c)
- 新版 `00b5332c`（命令位置の公開資料なし） · `00b53328`（命令位置の公開資料なし） · `00b53334`（命令位置の公開資料なし）

~~~diff
- 00b53264 ["INT_ADD", "register:40f0:8", ["const:b53264:8", "const:4:8"]]
- 00b53264 ["CALL", null, ["callee:00bde130:8"]]
+ 00b5332c ["INT_ADD", "register:40f0:8", ["const:b5332c:8", "const:4:8"]]
+ 00b5332c ["CALL", null, ["callee:00bde130:8"]]
- 00b53264 bytes 872b0294
+ 00b5332c bytes 812b0294
- 00b53260 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b53260 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b53260 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b53260 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b53328 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b53328 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b53328 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b53328 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b53260 bytes 001c1591
+ 00b53328 bytes 00501791
- 00b5326c ["COPY", "tmp:0:8", ["const:168:8"]]
- 00b5326c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5326c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5326c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b53334 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 00b53334 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53334 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5326c bytes 08a10591
+ 00b53334 bytes 08a10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92eeda320cf8274eab31bd8dcad8ccd7"></a>

### [`00b53280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53280.md) → [`00b53348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53348.md) _ZN8firebase13remote_config8internal12config_value13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b53388",
      "incomplete_value": true,
      "site": "00b53388",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b532c0",
      "incomplete_value": true,
      "site": "00b532c0",
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
            "const:158:8"
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
      "definition_site": "00b53364",
      "incomplete_value": true,
      "site": "00b53364",
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
      "definition_site": "00b5329c",
      "incomplete_value": true,
      "site": "00b5329c",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b5329c"
      ],
      [
        "FALL_THROUGH",
        "00b53364"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b53364",
      "incomplete_value": true,
      "site": "00b53388",
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
      "definition_site": "00b5329c",
      "incomplete_value": true,
      "site": "00b532c0",
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
      "00b5335c",
      "READ",
      [
        "storage",
        "010a1158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53388",
      "WRITE",
      [
        "storage",
        "010a1158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b533a0",
      "PARAM",
      [
        "storage",
        "010a1198",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5335c",
      "READ",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53388",
      "WRITE",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b533a0",
      "PARAM",
      [
        "storage",
        "010a1258",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b532c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53280.md#insn-00b532c0) · [`00b53294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53280.md#insn-00b53294) · [`00b532b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53280.md#insn-00b532b8)
- 新版 `00b53388`（命令位置の公開資料なし） · `00b5335c`（命令位置の公開資料なし） · `00b53380`（命令位置の公開資料なし）

~~~diff
- 00b532c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:158:8"]]
- 00b532c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53388 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:218:8"]]
+ 00b53388 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b532c0 bytes 80ae00f9
+ 00b53388 bytes 800e01f9
- 00b53294 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:158:8"]]
- 00b53294 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5335c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:218:8"]]
+ 00b5335c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53294 bytes 81ae40f9
+ 00b5335c bytes 810e41f9
- 00b532b8 ["INT_ADD", "register:40f0:8", ["const:b532b8:8", "const:4:8"]]
- 00b532b8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b53380 ["INT_ADD", "register:40f0:8", ["const:b53380:8", "const:4:8"]]
+ 00b53380 ["CALL", null, ["callee:00bde040:8"]]
- 00b532b8 bytes 362b0294
+ 00b53380 bytes 302b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5315078465c1c2a924ccf7bbfbb2ab4f"></a>

### [`00b532f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b532f0.md) → [`00b533b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b533b8.md) _ZN8firebase13remote_config8internal12config_value10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b533d4",
      "incomplete_value": false,
      "site": "00b533d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:67f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5330c",
      "incomplete_value": false,
      "site": "00b53310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:5f2:8"
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
      "definition_site": "00b533e4",
      "incomplete_value": true,
      "site": "00b533f0",
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
      "definition_site": "00b5331c",
      "incomplete_value": true,
      "site": "00b53328",
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
      "00b533d4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b533e4",
      "DATA",
      [
        "storage",
        "010a1198",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b533d4",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b533e4",
      "DATA",
      [
        "storage",
        "010a1258",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b532f0.md#insn-00b53310) · [`00b5330c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b532f0.md#insn-00b5330c) · [`00b53318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b532f0.md#insn-00b53318)
- 新版 `00b533d8`（命令位置の公開資料なし） · `00b533d4`（命令位置の公開資料なし） · `00b533e0`（命令位置の公開資料なし）

~~~diff
- 00b53310 ["INT_ADD", "register:40f0:8", ["const:b53310:8", "const:4:8"]]
- 00b53310 ["CALL", null, ["callee:00bde130:8"]]
+ 00b533d8 ["INT_ADD", "register:40f0:8", ["const:b533d8:8", "const:4:8"]]
+ 00b533d8 ["CALL", null, ["callee:00bde130:8"]]
- 00b53310 bytes 5c2b0294
+ 00b533d8 bytes 562b0294
- 00b5330c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b5330c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5330c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5330c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b533d4 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b533d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b533d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b533d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5330c bytes 00c81791
+ 00b533d4 bytes 00fc1991
- 00b53318 ["COPY", "tmp:0:8", ["const:198:8"]]
- 00b53318 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b53318 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b53318 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b533e0 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 00b533e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b533e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b533e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b53318 bytes 08610691
+ 00b533e0 bytes 08610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6cdec1b10861ed00f338350846a3ce8"></a>

### [`00b5332c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b5332c.md) → [`00b533f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b533f4.md) _ZN8firebase13remote_config8internal11config_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b53420",
      "incomplete_value": true,
      "site": "00b53420",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53358",
      "incomplete_value": true,
      "site": "00b53358",
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
            "const:1a0:8"
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
      "definition_site": "00b53408",
      "incomplete_value": true,
      "site": "00b53408",
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
      "definition_site": "00b53340",
      "incomplete_value": true,
      "site": "00b53340",
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
      "definition_site": "00b53414",
      "incomplete_value": false,
      "site": "00b53418",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:75e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5334c",
      "incomplete_value": false,
      "site": "00b53350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:6d1:8"
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
      "00b53404",
      "READ",
      [
        "storage",
        "010a11a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53414",
      "PARAM",
      [
        "storage",
        "002976d1",
        null,
        "string"
      ]
    ],
    [
      "00b53420",
      "WRITE",
      [
        "storage",
        "010a11a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53404",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53414",
      "PARAM",
      [
        "storage",
        "0029775e",
        null,
        "string"
      ]
    ],
    [
      "00b53420",
      "WRITE",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b5332c.md#insn-00b53350) · [`00b53358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b5332c.md#insn-00b53358) · [`00b5333c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b5332c.md#insn-00b5333c)
- 新版 `00b53418`（命令位置の公開資料なし） · `00b53420`（命令位置の公開資料なし） · `00b53404`（命令位置の公開資料なし）

~~~diff
- 00b53350 ["INT_ADD", "register:40f0:8", ["const:b53350:8", "const:4:8"]]
- 00b53350 ["CALL", null, ["callee:00bde040:8"]]
+ 00b53418 ["INT_ADD", "register:40f0:8", ["const:b53418:8", "const:4:8"]]
+ 00b53418 ["CALL", null, ["callee:00bde040:8"]]
- 00b53350 bytes 102b0294
+ 00b53418 bytes 0a2b0294
- 00b53358 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1a0:8"]]
- 00b53358 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53420 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:260:8"]]
+ 00b53420 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53358 bytes 60d200f9
+ 00b53420 bytes 603201f9
- 00b5333c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1a0:8"]]
- 00b5333c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53404 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:260:8"]]
+ 00b53404 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5333c bytes 68d240f9
+ 00b53404 bytes 683241f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-886fd25546947f303bbee1499bd91850"></a>

### [`00b5336c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b5336c.md) → [`00b53434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53434.md) _ZN8firebase13remote_config8internal11config_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b53460",
      "incomplete_value": true,
      "site": "00b53460",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53398",
      "incomplete_value": true,
      "site": "00b53398",
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
            "const:1a0:8"
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
      "definition_site": "00b53448",
      "incomplete_value": true,
      "site": "00b53448",
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
      "definition_site": "00b53380",
      "incomplete_value": true,
      "site": "00b53380",
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
      "definition_site": "00b53450",
      "incomplete_value": false,
      "site": "00b53458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:75e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53388",
      "incomplete_value": false,
      "site": "00b53390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:6d1:8"
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
      "00b53444",
      "READ",
      [
        "storage",
        "010a11a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53450",
      "PARAM",
      [
        "storage",
        "002976d1",
        null,
        "string"
      ]
    ],
    [
      "00b53460",
      "WRITE",
      [
        "storage",
        "010a11a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53444",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53450",
      "PARAM",
      [
        "storage",
        "0029775e",
        null,
        "string"
      ]
    ],
    [
      "00b53460",
      "WRITE",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b5336c.md#insn-00b53390) · [`00b53398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b5336c.md#insn-00b53398) · [`00b5337c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b5336c.md#insn-00b5337c)
- 新版 `00b53458`（命令位置の公開資料なし） · `00b53460`（命令位置の公開資料なし） · `00b53444`（命令位置の公開資料なし）

~~~diff
- 00b53390 ["INT_ADD", "register:40f0:8", ["const:b53390:8", "const:4:8"]]
- 00b53390 ["CALL", null, ["callee:00bde040:8"]]
+ 00b53458 ["INT_ADD", "register:40f0:8", ["const:b53458:8", "const:4:8"]]
+ 00b53458 ["CALL", null, ["callee:00bde040:8"]]
- 00b53390 bytes 002b0294
+ 00b53458 bytes fa2a0294
- 00b53398 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1a0:8"]]
- 00b53398 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53460 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:260:8"]]
+ 00b53460 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53398 bytes 60d200f9
+ 00b53460 bytes 603201f9
- 00b5337c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1a0:8"]]
- 00b5337c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53444 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:260:8"]]
+ 00b53444 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5337c bytes 68d240f9
+ 00b53444 bytes 683241f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53acddc753954d4ae46db4db8d5dba42"></a>

### [`00b533ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b533ac.md) → [`00b53474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53474.md) _ZN8firebase13remote_config8internal11config_info10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b534a4",
      "incomplete_value": true,
      "site": "00b534a4",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b533dc",
      "incomplete_value": true,
      "site": "00b533dc",
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
            "const:1a0:8"
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
      "definition_site": "00b53488",
      "incomplete_value": true,
      "site": "00b53488",
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
      "definition_site": "00b533c0",
      "incomplete_value": true,
      "site": "00b533c0",
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
      "definition_site": "00b53494",
      "incomplete_value": false,
      "site": "00b5349c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:75e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b533cc",
      "incomplete_value": false,
      "site": "00b533d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:6d1:8"
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
      "00b53484",
      "READ",
      [
        "storage",
        "010a11a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53494",
      "PARAM",
      [
        "storage",
        "002976d1",
        null,
        "string"
      ]
    ],
    [
      "00b534a4",
      "WRITE",
      [
        "storage",
        "010a11a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53484",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53494",
      "PARAM",
      [
        "storage",
        "0029775e",
        null,
        "string"
      ]
    ],
    [
      "00b534a4",
      "WRITE",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b533d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b533ac.md#insn-00b533d4) · [`00b533dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b533ac.md#insn-00b533dc) · [`00b533bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b533ac.md#insn-00b533bc)
- 新版 `00b5349c`（命令位置の公開資料なし） · `00b534a4`（命令位置の公開資料なし） · `00b53484`（命令位置の公開資料なし）

~~~diff
- 00b533d4 ["INT_ADD", "register:40f0:8", ["const:b533d4:8", "const:4:8"]]
- 00b533d4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b5349c ["INT_ADD", "register:40f0:8", ["const:b5349c:8", "const:4:8"]]
+ 00b5349c ["CALL", null, ["callee:00bde040:8"]]
- 00b533d4 bytes ef2a0294
+ 00b5349c bytes e92a0294
- 00b533dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1a0:8"]]
- 00b533dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b534a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:260:8"]]
+ 00b534a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b533dc bytes 60d200f9
+ 00b534a4 bytes 603201f9
- 00b533bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1a0:8"]]
- 00b533bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53484 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:260:8"]]
+ 00b53484 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b533bc bytes 68d240f9
+ 00b53484 bytes 683241f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf85ff41a97705dee7b8ad5ad83ba1f3"></a>

### [`00b533f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b533f0.md) → [`00b534b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b534b8.md) _ZN8firebase13remote_config8internal11config_info10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b534e8",
      "incomplete_value": true,
      "site": "00b534e8",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53420",
      "incomplete_value": true,
      "site": "00b53420",
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
            "const:1a0:8"
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
      "definition_site": "00b534cc",
      "incomplete_value": true,
      "site": "00b534cc",
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
      "definition_site": "00b53404",
      "incomplete_value": true,
      "site": "00b53404",
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
      "definition_site": "00b534d4",
      "incomplete_value": false,
      "site": "00b534e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:75e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5340c",
      "incomplete_value": false,
      "site": "00b53418",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:6d1:8"
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
      "00b534c8",
      "READ",
      [
        "storage",
        "010a11a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b534d4",
      "PARAM",
      [
        "storage",
        "002976d1",
        null,
        "string"
      ]
    ],
    [
      "00b534e8",
      "WRITE",
      [
        "storage",
        "010a11a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b534c8",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ],
    [
      "00b534d4",
      "PARAM",
      [
        "storage",
        "0029775e",
        null,
        "string"
      ]
    ],
    [
      "00b534e8",
      "WRITE",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b533f0.md#insn-00b53418) · [`00b53420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b533f0.md#insn-00b53420) · [`00b53400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b533f0.md#insn-00b53400)
- 新版 `00b534e0`（命令位置の公開資料なし） · `00b534e8`（命令位置の公開資料なし） · `00b534c8`（命令位置の公開資料なし）

~~~diff
- 00b53418 ["INT_ADD", "register:40f0:8", ["const:b53418:8", "const:4:8"]]
- 00b53418 ["CALL", null, ["callee:00bde040:8"]]
+ 00b534e0 ["INT_ADD", "register:40f0:8", ["const:b534e0:8", "const:4:8"]]
+ 00b534e0 ["CALL", null, ["callee:00bde040:8"]]
- 00b53418 bytes de2a0294
+ 00b534e0 bytes d82a0294
- 00b53420 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1a0:8"]]
- 00b53420 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b534e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:260:8"]]
+ 00b534e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53420 bytes 60d200f9
+ 00b534e8 bytes 603201f9
- 00b53400 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1a0:8"]]
- 00b53400 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b534c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:260:8"]]
+ 00b534c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53400 bytes 68d240f9
+ 00b534c8 bytes 683241f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14b879f89ca50e060081bb7e11899f48"></a>

### [`00b53440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53440.md) → [`00b53508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53508.md) _ZN8firebase13remote_config8internal11config_info15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b53560",
      "incomplete_value": true,
      "site": "00b53560",
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
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53498",
      "incomplete_value": true,
      "site": "00b53498",
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
            "const:1a8:8"
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
      "definition_site": "00b5353c",
      "incomplete_value": true,
      "site": "00b53548",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:260:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53474",
      "incomplete_value": true,
      "site": "00b53480",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:1a0:8"
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
      "00b5351c",
      "READ",
      [
        "storage",
        "010a11a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5353c",
      "READ",
      [
        "storage",
        "010a11a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53560",
      "WRITE",
      [
        "storage",
        "010a11a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5351c",
      "READ",
      [
        "storage",
        "010a1268",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5353c",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53560",
      "WRITE",
      [
        "storage",
        "010a1268",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53440.md#insn-00b53480) · [`00b53498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53440.md#insn-00b53498) · [`00b53454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53440.md#insn-00b53454)
- 新版 `00b53548`（命令位置の公開資料なし） · `00b53560`（命令位置の公開資料なし） · `00b5351c`（命令位置の公開資料なし）

~~~diff
- 00b53480 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53480 ["INT_ADD", "register:40f0:8", ["const:b53480:8", "const:4:8"]]
- 00b53480 ["CALLIND", null, ["register:0:8"]]
+ 00b53548 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b53548 ["INT_ADD", "register:40f0:8", ["const:b53548:8", "const:4:8"]]
+ 00b53548 ["CALLIND", null, ["register:0:8"]]
- 00b53480 bytes 00013fd6
+ 00b53548 bytes 00013fd6
- 00b53498 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b53498 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:1a8:8"]]
- 00b53498 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b53560 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b53560 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:268:8"]]
+ 00b53560 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b53498 bytes a0a20639
+ 00b53560 bytes a0a20939
- 00b53454 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:1a8:8"]]
- 00b53454 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b53454 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b5351c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:268:8"]]
+ 00b5351c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b5351c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b53454 bytes a8a24639
+ 00b5351c bytes a8a24939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60139c457dcaf4bc6d4da0b63d366fa1"></a>

### [`00b534ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b534ac.md) → [`00b53574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53574.md) _ZN8firebase13remote_config8internal11config_info12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b535b0",
      "incomplete_value": true,
      "site": "00b535b0",
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
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b534e8",
      "incomplete_value": true,
      "site": "00b534e8",
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
            "const:1a8:8"
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
      "definition_site": "00b535d0",
      "incomplete_value": true,
      "site": "00b535d0",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53508",
      "incomplete_value": true,
      "site": "00b53508",
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
            "const:1a0:8"
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
      "definition_site": "00b5358c",
      "incomplete_value": true,
      "site": "00b5358c",
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
      "definition_site": "00b534c4",
      "incomplete_value": true,
      "site": "00b534c4",
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
      "00b53588",
      "READ",
      [
        "storage",
        "010a11a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53594",
      "READ",
      [
        "storage",
        "010a11a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b535b0",
      "WRITE",
      [
        "storage",
        "010a11a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b53588",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53594",
      "READ",
      [
        "storage",
        "010a1268",
        null,
        "undefined1"
      ]
    ],
    [
      "00b535b0",
      "WRITE",
      [
        "storage",
        "010a1268",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b534e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b534ac.md#insn-00b534e8) · [`00b53504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b534ac.md#insn-00b53504) · [`00b53508`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b534ac.md#insn-00b53508)
- 新版 `00b535b0`（命令位置の公開資料なし） · `00b535cc`（命令位置の公開資料なし） · `00b535d0`（命令位置の公開資料なし）

~~~diff
- 00b534e8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b534e8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b534e8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:1a8:8"]]
- 00b534e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b535b0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b535b0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b535b0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:268:8"]]
+ 00b535b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b534e8 bytes bfa20639
+ 00b535b0 bytes bfa20939
- 00b53504 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53504 ["INT_ADD", "register:40f0:8", ["const:b53504:8", "const:4:8"]]
- 00b53504 ["CALLIND", null, ["register:0:8"]]
+ 00b535cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b535cc ["INT_ADD", "register:40f0:8", ["const:b535cc:8", "const:4:8"]]
+ 00b535cc ["CALLIND", null, ["register:0:8"]]
- 00b53504 bytes 00013fd6
+ 00b535cc bytes 00013fd6
- 00b53508 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1a0:8"]]
- 00b53508 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b53508 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b535d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:260:8"]]
+ 00b535d0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b535d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b53508 bytes 9fd200f9
+ 00b535d0 bytes 9f3201f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d62adafc2cfda64e5c874570253bb523"></a>

### [`00b5351c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b5351c.md) → [`00b535e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b535e4.md) _ZN8firebase13remote_config8internal11config_info14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "definition_site": "00b53624",
      "incomplete_value": true,
      "site": "00b53624",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5355c",
      "incomplete_value": true,
      "site": "00b5355c",
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
            "const:1a0:8"
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
      "definition_site": "00b53600",
      "incomplete_value": true,
      "site": "00b53600",
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
      "definition_site": "00b53538",
      "incomplete_value": true,
      "site": "00b53538",
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
      "definition_site": "00b53608",
      "incomplete_value": false,
      "site": "00b5361c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:75e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53540",
      "incomplete_value": false,
      "site": "00b53554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:6d1:8"
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
      "00b535f8",
      "READ",
      [
        "storage",
        "010a11a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53608",
      "PARAM",
      [
        "storage",
        "002976d1",
        null,
        "string"
      ]
    ],
    [
      "00b53624",
      "WRITE",
      [
        "storage",
        "010a11a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b535f8",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53608",
      "PARAM",
      [
        "storage",
        "0029775e",
        null,
        "string"
      ]
    ],
    [
      "00b53624",
      "WRITE",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b5351c.md#insn-00b53554) · [`00b5355c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b5351c.md#insn-00b5355c) · [`00b53530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b5351c.md#insn-00b53530)
- 新版 `00b5361c`（命令位置の公開資料なし） · `00b53624`（命令位置の公開資料なし） · `00b535f8`（命令位置の公開資料なし）

~~~diff
- 00b53554 ["INT_ADD", "register:40f0:8", ["const:b53554:8", "const:4:8"]]
- 00b53554 ["CALL", null, ["callee:00bde040:8"]]
+ 00b5361c ["INT_ADD", "register:40f0:8", ["const:b5361c:8", "const:4:8"]]
+ 00b5361c ["CALL", null, ["callee:00bde040:8"]]
- 00b53554 bytes 8f2a0294
+ 00b5361c bytes 892a0294
- 00b5355c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1a0:8"]]
- 00b5355c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53624 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:260:8"]]
+ 00b53624 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5355c bytes 80d200f9
+ 00b53624 bytes 803201f9
- 00b53530 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1a0:8"]]
- 00b53530 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b535f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:260:8"]]
+ 00b535f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53530 bytes 81d240f9
+ 00b535f8 bytes 813241f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83a6d790032005b94e086ee8aa6755a2"></a>

### [`00b5358c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b5358c.md) → [`00b53654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53654.md) _ZN8firebase13remote_config8internal11config_info11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b53670",
      "incomplete_value": false,
      "site": "00b53674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b535a8",
      "incomplete_value": false,
      "site": "00b535ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
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
      "definition_site": "00b53680",
      "incomplete_value": true,
      "site": "00b5368c",
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
      "definition_site": "00b535b8",
      "incomplete_value": true,
      "site": "00b535c4",
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
      "00b53670",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b53680",
      "DATA",
      [
        "storage",
        "010a11b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53670",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b53680",
      "DATA",
      [
        "storage",
        "010a1270",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b535ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b5358c.md#insn-00b535ac) · [`00b535a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b5358c.md#insn-00b535a8) · [`00b535b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b5358c.md#insn-00b535b4)
- 新版 `00b53674`（命令位置の公開資料なし） · `00b53670`（命令位置の公開資料なし） · `00b5367c`（命令位置の公開資料なし）

~~~diff
- 00b535ac ["INT_ADD", "register:40f0:8", ["const:b535ac:8", "const:4:8"]]
- 00b535ac ["CALL", null, ["callee:00bde130:8"]]
+ 00b53674 ["INT_ADD", "register:40f0:8", ["const:b53674:8", "const:4:8"]]
+ 00b53674 ["CALL", null, ["callee:00bde130:8"]]
- 00b535ac bytes b52a0294
+ 00b53674 bytes af2a0294
- 00b535a8 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b535a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b535a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b535a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b53670 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b53670 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b53670 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b53670 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b535a8 bytes 001c1591
+ 00b53670 bytes 00501791
- 00b535b4 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 00b535b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b535b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b535b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5367c ["COPY", "tmp:0:8", ["const:270:8"]]
+ 00b5367c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5367c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5367c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b535b4 bytes 08c10691
+ 00b5367c bytes 08c10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ad09a58174503778c1010880615b40a"></a>

### [`00b535c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b535c8.md) → [`00b53690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53690.md) _ZN8firebase13remote_config8internal11config_info13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b536d0",
      "incomplete_value": true,
      "site": "00b536d0",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53608",
      "incomplete_value": true,
      "site": "00b53608",
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
            "const:1a0:8"
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
      "definition_site": "00b536ac",
      "incomplete_value": true,
      "site": "00b536ac",
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
      "definition_site": "00b535e4",
      "incomplete_value": true,
      "site": "00b535e4",
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
      "definition_site": "00b536b4",
      "incomplete_value": false,
      "site": "00b536c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:75e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b535ec",
      "incomplete_value": false,
      "site": "00b53600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:6d1:8"
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
      "00b536a4",
      "READ",
      [
        "storage",
        "010a11a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b536b4",
      "PARAM",
      [
        "storage",
        "002976d1",
        null,
        "string"
      ]
    ],
    [
      "00b536d0",
      "WRITE",
      [
        "storage",
        "010a11a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b536a4",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ],
    [
      "00b536b4",
      "PARAM",
      [
        "storage",
        "0029775e",
        null,
        "string"
      ]
    ],
    [
      "00b536d0",
      "WRITE",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b535c8.md#insn-00b53600) · [`00b53608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b535c8.md#insn-00b53608) · [`00b535dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b535c8.md#insn-00b535dc)
- 新版 `00b536c8`（命令位置の公開資料なし） · `00b536d0`（命令位置の公開資料なし） · `00b536a4`（命令位置の公開資料なし）

~~~diff
- 00b53600 ["INT_ADD", "register:40f0:8", ["const:b53600:8", "const:4:8"]]
- 00b53600 ["CALL", null, ["callee:00bde040:8"]]
+ 00b536c8 ["INT_ADD", "register:40f0:8", ["const:b536c8:8", "const:4:8"]]
+ 00b536c8 ["CALL", null, ["callee:00bde040:8"]]
- 00b53600 bytes 642a0294
+ 00b536c8 bytes 5e2a0294
- 00b53608 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1a0:8"]]
- 00b53608 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b536d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:260:8"]]
+ 00b536d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53608 bytes 80d200f9
+ 00b536d0 bytes 803201f9
- 00b535dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1a0:8"]]
- 00b535dc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b536a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:260:8"]]
+ 00b536a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b535dc bytes 81d240f9
+ 00b536a4 bytes 813241f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d77b6846682d52687c7529b1f94f32d3"></a>

### [`00b53638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53638.md) → [`00b53700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53700.md) _ZN8firebase13remote_config8internal11config_info10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b5371c",
      "incomplete_value": false,
      "site": "00b53720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:67f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53654",
      "incomplete_value": false,
      "site": "00b53658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:5f2:8"
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
      "definition_site": "00b5372c",
      "incomplete_value": true,
      "site": "00b53738",
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
      "definition_site": "00b53664",
      "incomplete_value": true,
      "site": "00b53670",
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
      "00b5371c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b5372c",
      "DATA",
      [
        "storage",
        "010a11c8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5371c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b5372c",
      "DATA",
      [
        "storage",
        "010a1288",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53658`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53638.md#insn-00b53658) · [`00b53654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53638.md#insn-00b53654) · [`00b53660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53638.md#insn-00b53660)
- 新版 `00b53720`（命令位置の公開資料なし） · `00b5371c`（命令位置の公開資料なし） · `00b53728`（命令位置の公開資料なし）

~~~diff
- 00b53658 ["INT_ADD", "register:40f0:8", ["const:b53658:8", "const:4:8"]]
- 00b53658 ["CALL", null, ["callee:00bde130:8"]]
+ 00b53720 ["INT_ADD", "register:40f0:8", ["const:b53720:8", "const:4:8"]]
+ 00b53720 ["CALL", null, ["callee:00bde130:8"]]
- 00b53658 bytes 8a2a0294
+ 00b53720 bytes 842a0294
- 00b53654 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b53654 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b53654 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b53654 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5371c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b5371c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5371c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5371c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b53654 bytes 00c81791
+ 00b5371c bytes 00fc1991
- 00b53660 ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 00b53660 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b53660 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b53660 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b53728 ["COPY", "tmp:0:8", ["const:288:8"]]
+ 00b53728 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53728 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53728 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b53660 bytes 08210791
+ 00b53728 bytes 08210a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b7962c7ce259452228911d43cb1d9e6"></a>

### [`00b53674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53674.md) → [`00b5373c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5373c.md) _ZN8firebase13remote_config8internal15config_settings19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFile

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00b536a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b53768"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b53750",
      "incomplete_value": true,
      "site": "00b53750",
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
      "definition_site": "00b53688",
      "incomplete_value": true,
      "site": "00b53688",
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
      "00b5374c",
      "READ",
      [
        "storage",
        "010a11d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53750",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b536a4"
      ]
    ],
    [
      "unmatched:00b53694",
      "PARAM",
      [
        "storage",
        "002a7f38",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5374c",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53750",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5376c"
      ]
    ],
    [
      "00b5375c",
      "PARAM",
      [
        "storage",
        "002a7ea4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53674.md#insn-00b53698) · [`00b536a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53674.md#insn-00b536a0) · [`00b536b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53674.md#insn-00b536b0)

~~~diff
- 00b53698 ["INT_ADD", "register:40f0:8", ["const:b53698:8", "const:4:8"]]
- 00b53698 ["CALL", null, ["callee:00bde040:8"]]
- 00b53698 bytes 3e2a0294
- 00b536a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1d0:8"]]
- 00b536a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b536a0 bytes 60ea00f9
- 00b536b0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b536b0 ["RETURN", null, ["register:0:8"]]
- 00b536b0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db2a6008ec3577056f9e9610489440f4"></a>

### [`00b536b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b536b4.md) → [`00b5377c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5377c.md) _ZN8firebase13remote_config8internal15config_settings19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFile

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b537a8",
      "incomplete_value": true,
      "site": "00b537a8",
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
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b536e0",
      "incomplete_value": true,
      "site": "00b536e0",
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
            "const:1d0:8"
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
      "definition_site": "00b53790",
      "incomplete_value": true,
      "site": "00b53790",
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
      "definition_site": "00b536c8",
      "incomplete_value": true,
      "site": "00b536c8",
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
      "definition_site": "00b53798",
      "incomplete_value": false,
      "site": "00b537a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a7000:8"
          ],
          [
            "leaf",
            "const:ea4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b536d0",
      "incomplete_value": false,
      "site": "00b536d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a7000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "00b5378c",
      "READ",
      [
        "storage",
        "010a11d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53798",
      "PARAM",
      [
        "storage",
        "002a7f38",
        null,
        "string"
      ]
    ],
    [
      "00b537a8",
      "WRITE",
      [
        "storage",
        "010a11d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5378c",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53798",
      "PARAM",
      [
        "storage",
        "002a7ea4",
        null,
        "string"
      ]
    ],
    [
      "00b537a8",
      "WRITE",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b536d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b536b4.md#insn-00b536d8) · [`00b536e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b536b4.md#insn-00b536e0) · [`00b536c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b536b4.md#insn-00b536c4)
- 新版 `00b537a0`（命令位置の公開資料なし） · `00b537a8`（命令位置の公開資料なし） · `00b5378c`（命令位置の公開資料なし）

~~~diff
- 00b536d8 ["INT_ADD", "register:40f0:8", ["const:b536d8:8", "const:4:8"]]
- 00b536d8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b537a0 ["INT_ADD", "register:40f0:8", ["const:b537a0:8", "const:4:8"]]
+ 00b537a0 ["CALL", null, ["callee:00bde040:8"]]
- 00b536d8 bytes 2e2a0294
+ 00b537a0 bytes 282a0294
- 00b536e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1d0:8"]]
- 00b536e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b537a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
+ 00b537a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b536e0 bytes 60ea00f9
+ 00b537a8 bytes 604a01f9
- 00b536c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1d0:8"]]
- 00b536c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5378c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
+ 00b5378c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b536c4 bytes 68ea40f9
+ 00b5378c bytes 684a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b6c8fa27b8659d83bc3ab7b5a6e6879"></a>

### [`00b53738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53738.md) → [`00b53800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53800.md) _ZN8firebase13remote_config8internal15config_settings10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 25.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53768"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b53830"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5374c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53748",
      "READ",
      [
        "storage",
        "010a11d0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5374c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53834"
      ]
    ],
    [
      "unmatched:00b53754",
      "PARAM",
      [
        "storage",
        "002a7f38",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b53810",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53814",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53834"
      ]
    ],
    [
      "00b5381c",
      "PARAM",
      [
        "storage",
        "002a7ea4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5374c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53738.md#insn-00b5374c) · [`00b53760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53738.md#insn-00b53760) · [`00b53768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53738.md#insn-00b53768)
- 新版 `00b53828`（命令位置の公開資料なし）

~~~diff
- 00b5374c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b5374c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5374c bytes 080100b5
- 00b53760 ["INT_ADD", "register:40f0:8", ["const:b53760:8", "const:4:8"]]
- 00b53760 ["CALL", null, ["callee:00bde040:8"]]
+ 00b53828 ["INT_ADD", "register:40f0:8", ["const:b53828:8", "const:4:8"]]
+ 00b53828 ["CALL", null, ["callee:00bde040:8"]]
- 00b53760 bytes 0c2a0294
+ 00b53828 bytes 062a0294
- 00b53768 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1d0:8"]]
- 00b53768 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53768 bytes 60ea00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5072379962378c0429027d77c5c3171"></a>

### [`00b53788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53788.md) → [`00b53850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53850.md) _ZN8firebase13remote_config8internal15config_settings15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b537e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b538a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53884",
      "incomplete_value": true,
      "site": "00b53890",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:290:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b537bc",
      "incomplete_value": true,
      "site": "00b537c8",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:1d0:8"
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
      "00b53864",
      "READ",
      [
        "storage",
        "010a11d8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b537bc",
      "READ",
      [
        "storage",
        "010a11d0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b537e0",
      "WRITE",
      [
        "storage",
        "010a11d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b53864",
      "READ",
      [
        "storage",
        "010a1298",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53884",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b538a8",
      "WRITE",
      [
        "storage",
        "010a1298",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b537c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53788.md#insn-00b537c8) · [`00b537e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53788.md#insn-00b537e0)
- 新版 `00b53890`（命令位置の公開資料なし） · `00b538a8`（命令位置の公開資料なし）

~~~diff
- 00b537c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b537c8 ["INT_ADD", "register:40f0:8", ["const:b537c8:8", "const:4:8"]]
- 00b537c8 ["CALLIND", null, ["register:0:8"]]
+ 00b53890 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b53890 ["INT_ADD", "register:40f0:8", ["const:b53890:8", "const:4:8"]]
+ 00b53890 ["CALLIND", null, ["register:0:8"]]
- 00b537c8 bytes 00013fd6
+ 00b53890 bytes 00013fd6
- 00b537e0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b537e0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:1d8:8"]]
- 00b537e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b537e0 bytes a0620739
+ 00b538a8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b538a8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:298:8"]]
+ 00b538a8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b538a8 bytes a0620a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2977e2e72a2ee956432127e350ceeddf"></a>

### [`00b537f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b537f4.md) → [`00b538bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b538bc.md) _ZN8firebase13remote_config8internal15config_settings12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 12.50% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53830"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53850"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b538f8"
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
      "00b538d0",
      "READ",
      [
        "storage",
        "010a11d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b538dc",
      "READ",
      [
        "storage",
        "010a11d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b538e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b53834"
      ]
    ]
  ],
  "added": [
    [
      "00b538d0",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b538dc",
      "READ",
      [
        "storage",
        "010a1298",
        null,
        "undefined1"
      ]
    ],
    [
      "00b538e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b538fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5380c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b537f4.md#insn-00b5380c) · [`00b53830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b537f4.md#insn-00b53830) · [`00b53838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b537f4.md#insn-00b53838)
- 新版 `00b538d4`（命令位置の公開資料なし）

~~~diff
- 00b5380c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b5380c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b538d4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b538d4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b5380c bytes 410200b4
+ 00b538d4 bytes 410200b4
- 00b53830 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b53830 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b53830 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:1d8:8"]]
- 00b53830 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b53830 bytes bf620739
- 00b53838 ["INT_ADD", "register:40f0:8", ["const:b53838:8", "const:4:8"]]
- 00b53838 ["CALL", null, ["callee:00bde090:8"]]
- 00b53838 bytes ea290294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-231f2338c3fdc3c8a66fae8c0ae68414"></a>

### [`00b53864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53864.md) → [`00b5392c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5392c.md) _ZN8firebase13remote_config8internal15config_settings14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b538a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5396c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53880"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53878",
      "READ",
      [
        "storage",
        "010a11d0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53880",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53970"
      ]
    ],
    [
      "unmatched:00b53888",
      "PARAM",
      [
        "storage",
        "002a7f38",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b53940",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53948",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53970"
      ]
    ],
    [
      "00b53950",
      "PARAM",
      [
        "storage",
        "002a7ea4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53864.md#insn-00b53880) · [`00b5389c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53864.md#insn-00b5389c) · [`00b538a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53864.md#insn-00b538a4)
- 新版 `00b53964`（命令位置の公開資料なし）

~~~diff
- 00b53880 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b53880 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b53880 bytes 410100b5
- 00b5389c ["INT_ADD", "register:40f0:8", ["const:b5389c:8", "const:4:8"]]
- 00b5389c ["CALL", null, ["callee:00bde040:8"]]
+ 00b53964 ["INT_ADD", "register:40f0:8", ["const:b53964:8", "const:4:8"]]
+ 00b53964 ["CALL", null, ["callee:00bde040:8"]]
- 00b5389c bytes bd290294
+ 00b53964 bytes b7290294
- 00b538a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1d0:8"]]
- 00b538a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b538a4 bytes 80ea00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

