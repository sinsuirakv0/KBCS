# v15.7.2 → v15.7.3 · 命令位置の検査未完了 (4)

[一覧の目次](README.md)

<a id="compare-e6ffef8534a51dd7010a9d9248d0c015"></a>

### [`00b4aacc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aacc.md) → [`00b4ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ab94.md) _ZN8firebase9messaging18firebase_messaging10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 52.94% / 新版 52.94%

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
      "site": "00b4aafc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4abc4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aae0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4aba4",
      "READ",
      [
        "storage",
        "010a0ef8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4aae0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4ab00"
      ]
    ],
    [
      "unmatched:00b4aae8",
      "PARAM",
      [
        "storage",
        "002aa0dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4aba4",
      "READ",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aba8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4abc8"
      ]
    ],
    [
      "00b4abb0",
      "PARAM",
      [
        "storage",
        "002aa0e2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aacc.md#insn-00b4aae0) · [`00b4aafc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aacc.md#insn-00b4aafc) · [`00b4ab0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aacc.md#insn-00b4ab0c)

~~~diff
- 00b4aae0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4aae0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b4aae0 bytes 080100b5
- 00b4aafc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ef8:8"]]
- 00b4aafc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4aafc bytes 607e07f9
- 00b4ab0c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4ab0c ["RETURN", null, ["register:0:8"]]
- 00b4ab0c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f282eb3ceb65752eea098bc9508ae84"></a>

### [`00b4ab10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ab10.md) → [`00b4abd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4abd8.md) _ZN8firebase9messaging18firebase_messaging8GetClassEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b4ab18"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b4abe0"
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
      "unmatched:00b4ab14",
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
      "00b4abdc",
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

- 旧版 [`00b4ab18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ab10.md#insn-00b4ab18) · [`00b4ab10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ab10.md#insn-00b4ab10)
- 新版 [`00b4abe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4abd8.md#insn-00b4abe0)

~~~diff
- 00b4ab18 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4ab18 ["RETURN", null, ["register:0:8"]]
- 00b4ab18 bytes c0035fd6
+ 00b4abe0 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b4abe0 ["RETURN", null, ["register:0:8"]]
+ 00b4abe0 bytes c0035fd6
- 00b4ab10 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00b4ab10 bytes a82a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25905b2a727572234ce0f503743cb6cc"></a>

### [`00b4ac68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ac68.md) → [`00b4ad30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ad30.md) _ZN8firebase9messaging18firebase_messaging11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b4ac88"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b4ad50"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aca0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4ad44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4ac8c"
      ]
    ],
    [
      "unmatched:00b4ac84",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4ac88",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b4ad44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4ad54"
      ]
    ],
    [
      "00b4ad4c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b4ad50",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ac88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ac68.md#insn-00b4ac88) · [`00b4aca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ac68.md#insn-00b4aca0)
- 新版 [`00b4ad50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ad30.md#insn-00b4ad50)

~~~diff
- 00b4ac88 ["INT_ADD", "register:40f0:8", ["const:b4ac88:8", "const:4:8"]]
- 00b4ac88 ["CALL", null, ["callee:00bde130:8"]]
- 00b4ac88 bytes fe4c0294
- 00b4aca0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4aca0 ["RETURN", null, ["register:0:8"]]
- 00b4aca0 bytes c0035fd6
+ 00b4ad50 ["INT_ADD", "register:40f0:8", ["const:b4ad50:8", "const:4:8"]]
+ 00b4ad50 ["CALL", null, ["callee:00bde130:8"]]
+ 00b4ad50 bytes f84c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d404ab9d22d6cfd6aeb42898f5a41340"></a>

### [`00b4ad14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ad14.md) → [`00b4addc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4addc.md) _ZN8firebase9messaging18firebase_messaging10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b4ad34"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b4adfc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ad4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4adf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4ad38"
      ]
    ],
    [
      "unmatched:00b4ad30",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4ad34",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b4adf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4ae00"
      ]
    ],
    [
      "00b4adf8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b4adfc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ad34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ad14.md#insn-00b4ad34) · [`00b4ad4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ad14.md#insn-00b4ad4c)
- 新版 [`00b4adfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4addc.md#insn-00b4adfc)

~~~diff
- 00b4ad34 ["INT_ADD", "register:40f0:8", ["const:b4ad34:8", "const:4:8"]]
- 00b4ad34 ["CALL", null, ["callee:00bde130:8"]]
- 00b4ad34 bytes d34c0294
- 00b4ad4c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4ad4c ["RETURN", null, ["register:0:8"]]
- 00b4ad4c bytes c0035fd6
+ 00b4adfc ["INT_ADD", "register:40f0:8", ["const:b4adfc:8", "const:4:8"]]
+ 00b4adfc ["CALL", null, ["callee:00bde130:8"]]
+ 00b4adfc bytes cd4c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a02cc69447e154c2e5f5d7a7201aa5c4"></a>

### [`00b4ae58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ae58.md) → [`00b4af20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4af20.md) _ZN8firebase9messaging27registration_intent_service8GetClassEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b4ae60"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b4af28"
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
      "unmatched:00b4ae5c",
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
      "00b4af24",
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

- 旧版 [`00b4ae60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ae58.md#insn-00b4ae60) · [`00b4ae58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ae58.md#insn-00b4ae58)
- 新版 [`00b4af28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4af20.md#insn-00b4af28)

~~~diff
- 00b4ae60 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4ae60 ["RETURN", null, ["register:0:8"]]
- 00b4ae60 bytes c0035fd6
+ 00b4af28 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b4af28 ["RETURN", null, ["register:0:8"]]
+ 00b4af28 bytes c0035fd6
- 00b4ae58 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00b4ae58 bytes a82a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d6209ec3c0cfd2570dba3704c7b6f68"></a>

### [`00b4ae64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ae64.md) → [`00b4af2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4af2c.md) _ZN8firebase9messaging27registration_intent_service15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aebc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4af84"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aea4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4af40",
      "READ",
      [
        "storage",
        "010a0f60",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b4ae98",
      "READ",
      [
        "storage",
        "010a0f58",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4aebc",
      "WRITE",
      [
        "storage",
        "010a0f60",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4af40",
      "READ",
      [
        "storage",
        "010a1020",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4af60",
      "READ",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4af84",
      "WRITE",
      [
        "storage",
        "010a1020",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ae64.md#insn-00b4aea4) · [`00b4aebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4ae64.md#insn-00b4aebc)
- 新版 [`00b4af6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4af2c.md#insn-00b4af6c)

~~~diff
- 00b4aea4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4aea4 ["INT_ADD", "register:40f0:8", ["const:b4aea4:8", "const:4:8"]]
- 00b4aea4 ["CALLIND", null, ["register:0:8"]]
- 00b4aea4 bytes 00013fd6
- 00b4aebc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4aebc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:f60:8"]]
- 00b4aebc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4aebc bytes a0823d39
+ 00b4af6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4af6c ["INT_ADD", "register:40f0:8", ["const:b4af6c:8", "const:4:8"]]
+ 00b4af6c ["CALLIND", null, ["register:0:8"]]
+ 00b4af6c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de6ae0306daf247cc0ce147f81416d8f"></a>

### [`00b4aed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aed0.md) → [`00b4af98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4af98.md) _ZN8firebase9messaging27registration_intent_service12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 28.57% / 新版 28.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aed0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aed4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aed4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4aed0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4aed4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4aed8",
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
      "00b4af98",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4af9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4afa0",
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

- 旧版 [`00b4aed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aed0.md#insn-00b4aed0) · [`00b4aed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aed0.md#insn-00b4aed4) · [`00b4aed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aed0.md#insn-00b4aed8)

~~~diff
- 00b4aed0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b4aed0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b4aed0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4aed0 bytes f50f1df8
- 00b4aed4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4aed4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4aed4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4aed4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4aed4 bytes f44f01a9
- 00b4aed8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4aed8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4aed8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b4aed8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4aed8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e4d63b29bc9673335ea5f3290886007"></a>

### [`00b4afb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4afb0.md) → [`00b4b078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b078.md) _ZN8firebase9messaging27registration_intent_service11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b4afd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b4b098"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4afe8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b08c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4afd4"
      ]
    ],
    [
      "unmatched:00b4afcc",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4afd0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b4b08c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b09c"
      ]
    ],
    [
      "00b4b094",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b4b098",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4afd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4afb0.md#insn-00b4afd0) · [`00b4afe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4afb0.md#insn-00b4afe8)
- 新版 [`00b4b098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b078.md#insn-00b4b098)

~~~diff
- 00b4afd0 ["INT_ADD", "register:40f0:8", ["const:b4afd0:8", "const:4:8"]]
- 00b4afd0 ["CALL", null, ["callee:00bde130:8"]]
- 00b4afd0 bytes 2c4c0294
- 00b4afe8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4afe8 ["RETURN", null, ["register:0:8"]]
- 00b4afe8 bytes c0035fd6
+ 00b4b098 ["INT_ADD", "register:40f0:8", ["const:b4b098:8", "const:4:8"]]
+ 00b4b098 ["CALL", null, ["callee:00bde130:8"]]
+ 00b4b098 bytes 264c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb63c2b48707d525d393d17d57abfa3f"></a>

### [`00b4b05c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b05c.md) → [`00b4b124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b124.md) _ZN8firebase9messaging27registration_intent_service10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b4b070"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b4b138"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b07c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4b070",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4b080"
      ]
    ],
    [
      "unmatched:00b4b078",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4b07c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b4b138",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b148"
      ]
    ],
    [
      "00b4b140",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b4b144",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b05c.md#insn-00b4b070) · [`00b4b07c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b05c.md#insn-00b4b07c) · [`00b4b094`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b05c.md#insn-00b4b094)

~~~diff
- 00b4b070 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b4b070 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4b070 bytes 8b000054
- 00b4b07c ["INT_ADD", "register:40f0:8", ["const:b4b07c:8", "const:4:8"]]
- 00b4b07c ["CALL", null, ["callee:00bde130:8"]]
- 00b4b07c bytes 014c0294
- 00b4b094 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4b094 ["RETURN", null, ["register:0:8"]]
- 00b4b094 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59dcea10d074ff5b451f1a77b79ffb54"></a>

### [`00b4b098`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b098.md) → [`00b4b160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b160.md) _ZN8firebase9messaging26illegal_argument_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

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
      "site": "00b4b0c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4b18c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b0ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4b0a8",
      "READ",
      [
        "storage",
        "010a0f78",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4b0ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4b0c8"
      ]
    ],
    [
      "unmatched:00b4b0b8",
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
      "00b4b170",
      "READ",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b174",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b190"
      ]
    ],
    [
      "00b4b180",
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

- 旧版 [`00b4b0ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b098.md#insn-00b4b0ac) · [`00b4b0bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b098.md#insn-00b4b0bc) · [`00b4b0c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b098.md#insn-00b4b0c4)

~~~diff
- 00b4b0ac ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4b0ac ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4b0ac bytes e80000b5
- 00b4b0bc ["INT_ADD", "register:40f0:8", ["const:b4b0bc:8", "const:4:8"]]
- 00b4b0bc ["CALL", null, ["callee:00bde040:8"]]
- 00b4b0bc bytes b54b0294
- 00b4b0c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f78:8"]]
- 00b4b0c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b0c4 bytes 60be07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29fffee611d257b50608a0ba74309964"></a>

### [`00b4b2f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b2f8.md) → [`00b4b3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b3c0.md) _ZN8firebase9messaging26illegal_argument_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b4b2f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b2fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b2fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4b2f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4b2fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4b3d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4b31c"
      ]
    ]
  ],
  "added": [
    [
      "00b4b3c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4b3c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4b3d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b3e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b2f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b2f8.md#insn-00b4b2f8) · [`00b4b2fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b2f8.md#insn-00b4b2fc) · [`00b4b318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b2f8.md#insn-00b4b318)

~~~diff
- 00b4b2f8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4b2f8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4b2f8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4b2f8 bytes f30f1ef8
- 00b4b2fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4b2fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4b2fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4b2fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4b2fc bytes fd7b01a9
- 00b4b318 ["INT_ADD", "register:40f0:8", ["const:b4b318:8", "const:4:8"]]
- 00b4b318 ["CALL", null, ["callee:00bde130:8"]]
- 00b4b318 bytes 5a4b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5dc5767a159d241a25fb04daa653dc0"></a>

### [`00b4b3a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b3a4.md) → [`00b4b46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b46c.md) _ZN8firebase9messaging26illegal_argument_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b4b3c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b4b48c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b3dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b480",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4b3c8"
      ]
    ],
    [
      "unmatched:00b4b3c0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4b3c4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b4b480",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b490"
      ]
    ],
    [
      "00b4b488",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b4b48c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b3c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b3a4.md#insn-00b4b3c4) · [`00b4b3dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b3a4.md#insn-00b4b3dc)
- 新版 [`00b4b48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b46c.md#insn-00b4b48c)

~~~diff
- 00b4b3c4 ["INT_ADD", "register:40f0:8", ["const:b4b3c4:8", "const:4:8"]]
- 00b4b3c4 ["CALL", null, ["callee:00bde130:8"]]
- 00b4b3c4 bytes 2f4b0294
- 00b4b3dc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4b3dc ["RETURN", null, ["register:0:8"]]
- 00b4b3dc bytes c0035fd6
+ 00b4b48c ["INT_ADD", "register:40f0:8", ["const:b4b48c:8", "const:4:8"]]
+ 00b4b48c ["CALL", null, ["callee:00bde130:8"]]
+ 00b4b48c bytes 294b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e05f4ac56f37898ffd5a0b77809b7b3"></a>

### [`00b4e7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e7d4.md) → [`00b4e89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e89c.md) FUN_00b4e89c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4b7bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b7bc.md) · 呼出先 4件 [`00b4e83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e83c.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00be0300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0300.md)
- 新版 呼出元 1件 [`00b4b884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b884.md) · 呼出先 4件 [`00b4e904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e904.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00be03b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 57.89% / 新版 57.89%

CFGの説明率　旧版 20.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e7d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e7d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e7d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4e7d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4e7d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4e7e4",
      "READ",
      [
        "storage",
        "010a0fb0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e89c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4e8a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4e8ac",
      "READ",
      [
        "storage",
        "010a1070",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e7d4.md#insn-00b4e7d4) · [`00b4e7d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e7d4.md#insn-00b4e7d8) · [`00b4e7ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e7d4.md#insn-00b4e7ec)

~~~diff
- 00b4e7d4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4e7d4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4e7d4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4e7d4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4e7d4 bytes f44fbea9
- 00b4e7d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4e7d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4e7d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4e7d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4e7d8 bytes fd7b01a9
- 00b4e7ec ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00b4e7ec ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b4e7ec bytes 340100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4c5cf348b22f37730d94bbde7c6da2f"></a>

### [`00b4e984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e984.md) → [`00b4ea4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ea4c.md) FUN_00b4ea4c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4cce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cce0.md) · 呼出先 4件 [`00b4e83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e83c.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00be0300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0300.md)
- 新版 呼出元 1件 [`00b4cda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cda8.md) · 呼出先 4件 [`00b4e904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e904.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00be03b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03b0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 26.67% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e9b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4ea78"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e99c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4ea5c",
      "READ",
      [
        "storage",
        "010a0fb0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4e99c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4ea88"
      ]
    ],
    [
      "unmatched:00b4e9b0",
      "WRITE",
      [
        "storage",
        "010a1048",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4ea5c",
      "READ",
      [
        "storage",
        "010a1070",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ea64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4ea88"
      ]
    ],
    [
      "00b4ea78",
      "WRITE",
      [
        "storage",
        "010a1108",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e99c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e984.md#insn-00b4e99c) · [`00b4e9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e984.md#insn-00b4e9b0) · [`00b4e9dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4e984.md#insn-00b4e9dc)

~~~diff
- 00b4e99c ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00b4e99c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b4e99c bytes 340100b4
- 00b4e9b0 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b4e9b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:48:8"]]
- 00b4e9b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4e9b0 bytes 09210139
- 00b4e9dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4e9dc ["INT_ADD", "register:40f0:8", ["const:b4e9dc:8", "const:4:8"]]
- 00b4e9dc ["CALLIND", null, ["register:0:8"]]
- 00b4e9dc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0057be306391ff0874ab8bdc2a8c61a3"></a>

### [`00b4fe98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4f/00b4fe98.md) → [`00b4ff60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4f/00b4ff60.md) _ZNK8firebase9messaging8internal13MessageReader20ConsumeTokenReceivedEPKN3com6google8firebase9messaging3cpp23SerializedTokenReceivedE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 73.68% / 新版 73.68%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4fe98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4f/00b4fe98.md#insn-00b4fe98) · [`00b4fe9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4f/00b4fe98.md#insn-00b4fe9c) · [`00b4fea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4f/00b4fe98.md#insn-00b4fea0)

~~~diff
- 00b4fe98 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00b4fe98 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00b4fe98 ["INT_SEXT", "register:4040:8", ["tmp:1:4"]]
- 00b4fe98 bytes 280080b9
- 00b4fe9c ["INT_SUB", "register:4040:8", ["register:4008:8", "register:4040:8"]]
- 00b4fe9c bytes 280008cb
- 00b4fea0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b4fea0 ["LOAD", "tmp:1:2", ["const:1b1:8", "tmp:0:8"]]
- 00b4fea0 ["INT_ZEXT", "register:4048:8", ["tmp:1:2"]]
- 00b4fea0 bytes 09014079
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b0accc5b91c547f503b5e6587b3a5dc"></a>

### [`00b4fee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4f/00b4fee4.md) → [`00b4ffac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4f/00b4ffac.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIN11flatbuffers14VectorIteratorIhhEEEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr1

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0480.md) · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdddb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00be0530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0530.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 73.61% / 新版 74.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ff68"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ffa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b50000"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4ffa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b500e4"
      ]
    ],
    [
      "unmatched:00b50000",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b500e8"
      ]
    ],
    [
      "unmatched:00b50074",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b50128"
      ]
    ]
  ],
  "added": [
    [
      "00b50070",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b500e4"
      ]
    ],
    [
      "00b500c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b500e8"
      ]
    ],
    [
      "00b5013c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b50128"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ff38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4f/00b4fee4.md#insn-00b4ff38) · [`00b4ff68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4f/00b4fee4.md#insn-00b4ff68) · [`00b4ffa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4f/00b4fee4.md#insn-00b4ffa8)
- 新版 [`00b50000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4f/00b4ffac.md#insn-00b50000)

~~~diff
- 00b4ff38 ["INT_RIGHT", "tmp:0:8", ["register:40b0:8", "const:3f:4"]]
- 00b4ff38 ["INT_AND", "tmp:1:8", ["tmp:0:8", "const:1:8"]]
- 00b4ff38 ["INT_EQUAL", "tmp:2:1", ["tmp:1:8", "const:0:8"]]
- 00b4ff38 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b50000 ["INT_RIGHT", "tmp:0:8", ["register:40b0:8", "const:3f:4"]]
+ 00b50000 ["INT_AND", "tmp:1:8", ["tmp:0:8", "const:1:8"]]
+ 00b50000 ["INT_EQUAL", "tmp:2:1", ["tmp:1:8", "const:0:8"]]
+ 00b50000 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b4ff38 bytes 3610f8b7
+ 00b50000 bytes 3610f8b7
- 00b4ff68 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b4ff68 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b4ff68 ["COPY", "tmp:2:8", ["register:4040:8"]]
- 00b4ff68 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00b4ff68 bytes 08818a9a
- 00b4ffa8 ["CBRANCH", null, ["local:b22:8", "register:101:1"]]
- 00b4ffa8 bytes a0030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21a2ee58c3c820a3b9731f79d94c407c"></a>

### [`00b50310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b50/00b50310.md) → [`00b503d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b50/00b503d8.md) _ZNK3com6google8firebase9messaging3cpp17SerializedMessage6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0410.md) · 呼出先 2件 [`00be0420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0420.md) [`00be0440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0440.md)
- 新版 呼出元 1件 [`00be04c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04c0.md) · 呼出先 2件 [`00be04d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04d0.md) [`00be04f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 59.52% / 新版 59.52%

CFGの説明率　旧版 40.77% / 新版 40.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 109件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b50380"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5041c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b50424"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b50380",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b50484"
      ]
    ],
    [
      "00b504d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b5042c"
      ]
    ],
    [
      "unmatched:00b5041c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b50488"
      ]
    ]
  ],
  "added": [
    [
      "00b50448",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b50484"
      ]
    ],
    [
      "00b504d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b504f4"
      ]
    ],
    [
      "00b504e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b50488"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5035c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b50/00b50310.md#insn-00b5035c) · [`00b50380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b50/00b50310.md#insn-00b50380) · [`00b5039c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b50/00b50310.md#insn-00b5039c)
- 新版 [`00b50424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b50/00b503d8.md#insn-00b50424) · [`00b50464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b50/00b503d8.md#insn-00b50464)

~~~diff
- 00b5035c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b5035c ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00b50424 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b50424 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00b5035c bytes 23030054
+ 00b50424 bytes 23030054
- 00b50380 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b50380 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b50380 ["CBRANCH", null, ["local:b11:8", "tmp:1:1"]]
- 00b50380 bytes e8010054
- 00b5039c ["INT_NOTEQUAL", "tmp:0:1", ["register:4068:4", "const:0:4"]]
- 00b5039c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00b50464 ["INT_NOTEQUAL", "tmp:0:1", ["register:4068:4", "const:0:4"]]
+ 00b50464 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00b5039c bytes 0d010035
+ 00b50464 bytes 0d010035
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b72da6673b23b86a11d9bbd0ed944281"></a>

### [`00b51324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b51/00b51324.md) → [`00b513ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b51/00b513ec.md) _ZNK3com6google8firebase9messaging3cpp22SerializedNotification6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0420.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be04d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04d0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 37.15% / 新版 37.15%

CFGの説明率　旧版 15.14% / 新版 15.07%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 169件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b51400"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b51408"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b51414"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b514bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b51410"
      ]
    ],
    [
      "unmatched:00b51400",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b52124"
      ]
    ],
    [
      "unmatched:00b51408",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b51418"
      ]
    ]
  ],
  "added": [
    [
      "00b514bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b514d8"
      ]
    ],
    [
      "00b514c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b52124"
      ]
    ],
    [
      "00b514d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b514e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b51400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b51/00b51324.md#insn-00b51400) · [`00b51408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b51/00b51324.md#insn-00b51408) · [`00b51414`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b51/00b51324.md#insn-00b51414)

~~~diff
- 00b51400 ["INT_NOTEQUAL", "tmp:0:1", ["register:4088:4", "const:0:4"]]
- 00b51400 ["CBRANCH", null, ["local:b322:8", "tmp:0:1"]]
- 00b51400 bytes f1620035
- 00b51408 ["CBRANCH", null, ["local:b21:8", "register:102:1"]]
- 00b51408 bytes 82000054
- 00b51414 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b51414 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b51414 bytes 03fdff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d5809949044f28790fd9fd677c64e88"></a>

### [`00b52ab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52ab0.md) → [`00b52b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52b78.md) _ZN8firebase13remote_config12RemoteConfig25AddOnConfigUpdateListenerENSt6__ndk18functionIFvONS0_12ConfigUpdateENS0_17RemoteConfigErrorEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00be06a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be06a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00be0750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0750.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 82.35% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b52ad4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b52b9c"
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
      "unmatched:00b52ad4",
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
      "00b52b9c",
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

- 旧版 [`00b52ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52ab0.md#insn-00b52ad4) · [`00b52ae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b52/00b52ab0.md#insn-00b52ae0)
- 新版 [`00b52b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52b78.md#insn-00b52b9c) · [`00b52ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52b78.md#insn-00b52ba8)

~~~diff
- 00b52ad4 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b52ad4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b52ad4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b52ad4 bytes aa831df8
+ 00b52b9c ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 00b52b9c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
+ 00b52b9c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00b52b9c bytes aa831df8
- 00b52ae0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b52ae0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b52ba8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b52ba8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b52ae0 bytes 000100b4
+ 00b52ba8 bytes 000100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2e9e5a720446473d34c353c9acad721"></a>

### [`00b536f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b536f4.md) → [`00b537bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b537bc.md) _ZN8firebase13remote_config8internal15config_settings10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00b53724"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b537ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53708"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b537cc",
      "READ",
      [
        "storage",
        "010a11d0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53708",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b537f0"
      ]
    ],
    [
      "unmatched:00b53714",
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
      "00b537cc",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b537d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b537f0"
      ]
    ],
    [
      "00b537dc",
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

- 旧版 [`00b53708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b536f4.md#insn-00b53708) · [`00b5371c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b536f4.md#insn-00b5371c) · [`00b53724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b536f4.md#insn-00b53724)

~~~diff
- 00b53708 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b53708 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b53708 bytes 080100b5
- 00b5371c ["INT_ADD", "register:40f0:8", ["const:b5371c:8", "const:4:8"]]
- 00b5371c ["CALL", null, ["callee:00bde040:8"]]
- 00b5371c bytes 1d2a0294
- 00b53724 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1d0:8"]]
- 00b53724 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53724 bytes 60ea00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8883e1d06689a880566bb696732ee349"></a>

### [`00b53980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53980.md) → [`00b53a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53a48.md) _ZN8firebase13remote_config8internal15config_settings10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b53994"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b53a5c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b539a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53994",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b539a4"
      ]
    ],
    [
      "unmatched:00b5399c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b539a0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b53a5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53a6c"
      ]
    ],
    [
      "00b53a64",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b53a68",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53980.md#insn-00b53994) · [`00b539a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53980.md#insn-00b539a0) · [`00b539b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53980.md#insn-00b539b8)

~~~diff
- 00b53994 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b53994 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b53994 bytes 8b000054
- 00b539a0 ["INT_ADD", "register:40f0:8", ["const:b539a0:8", "const:4:8"]]
- 00b539a0 ["CALL", null, ["callee:00bde130:8"]]
- 00b539a0 bytes b8290294
- 00b539b8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b539b8 ["RETURN", null, ["register:0:8"]]
- 00b539b8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e14221772cdbfd1de7e29940e65f9f6"></a>

### [`00b53cc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53cc8.md) → [`00b53d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53d90.md) _ZN8firebase13remote_config8internal23config_settings_builder10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b53ce8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b53db0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53d00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b53da4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b53cec"
      ]
    ],
    [
      "unmatched:00b53ce4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b53ce8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b53da4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b53db4"
      ]
    ],
    [
      "00b53dac",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b53db0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53ce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53cc8.md#insn-00b53ce8) · [`00b53d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53cc8.md#insn-00b53d00)
- 新版 [`00b53db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53d90.md#insn-00b53db0)

~~~diff
- 00b53ce8 ["INT_ADD", "register:40f0:8", ["const:b53ce8:8", "const:4:8"]]
- 00b53ce8 ["CALL", null, ["callee:00bde130:8"]]
- 00b53ce8 bytes e6280294
- 00b53d00 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b53d00 ["RETURN", null, ["register:0:8"]]
- 00b53d00 bytes c0035fd6
+ 00b53db0 ["INT_ADD", "register:40f0:8", ["const:b53db0:8", "const:4:8"]]
+ 00b53db0 ["CALL", null, ["callee:00bde130:8"]]
+ 00b53db0 bytes e0280294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3df323944c3f6bb335479bf19d26dfe3"></a>

### [`00b53f64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53f64.md) → [`00b5402c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5402c.md) _ZN8firebase13remote_config8internal19throttled_exception11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b53f84"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b5404c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53f9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b54040",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b53f88"
      ]
    ],
    [
      "unmatched:00b53f80",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b53f84",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b54040",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b54050"
      ]
    ],
    [
      "00b54048",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b5404c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53f84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53f64.md#insn-00b53f84) · [`00b53f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b53/00b53f64.md#insn-00b53f9c)
- 新版 [`00b5404c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5402c.md#insn-00b5404c)

~~~diff
- 00b53f84 ["INT_ADD", "register:40f0:8", ["const:b53f84:8", "const:4:8"]]
- 00b53f84 ["CALL", null, ["callee:00bde130:8"]]
- 00b53f84 bytes 3f280294
- 00b53f9c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b53f9c ["RETURN", null, ["register:0:8"]]
- 00b53f9c bytes c0035fd6
+ 00b5404c ["INT_ADD", "register:40f0:8", ["const:b5404c:8", "const:4:8"]]
+ 00b5404c ["CALL", null, ["callee:00bde130:8"]]
+ 00b5404c bytes 39280294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0c9d95cee9f4f20623e17b986b24280"></a>

### [`00b54010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54010.md) → [`00b540d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b540d8.md) _ZN8firebase13remote_config8internal19throttled_exception10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b54010"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54014"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54014"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b54010",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b54014",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b540ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b54034"
      ]
    ]
  ],
  "added": [
    [
      "00b540d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b540dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b540ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b540fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54010.md#insn-00b54010) · [`00b54014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54010.md#insn-00b54014) · [`00b54030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54010.md#insn-00b54030)

~~~diff
- 00b54010 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b54010 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b54010 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b54010 bytes f30f1ef8
- 00b54014 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b54014 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b54014 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b54014 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b54014 bytes fd7b01a9
- 00b54030 ["INT_ADD", "register:40f0:8", ["const:b54030:8", "const:4:8"]]
- 00b54030 ["CALL", null, ["callee:00bde130:8"]]
- 00b54030 bytes 14280294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-756ae150e003ab0e693d3f825e60bab8"></a>

### [`00b5404c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5404c.md) → [`00b54114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54114.md) _ZN8firebase13remote_config8internal26jni_config_update_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12E

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00b54078"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b54140"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54060"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5405c",
      "READ",
      [
        "storage",
        "010a1250",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b54060",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b54144"
      ]
    ],
    [
      "unmatched:00b5406c",
      "PARAM",
      [
        "storage",
        "002a629a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b54124",
      "READ",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54128",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b54144"
      ]
    ],
    [
      "00b54134",
      "PARAM",
      [
        "storage",
        "002a6293",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5404c.md#insn-00b54060) · [`00b54070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5404c.md#insn-00b54070) · [`00b54078`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5404c.md#insn-00b54078)

~~~diff
- 00b54060 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b54060 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b54060 bytes e80000b5
- 00b54070 ["INT_ADD", "register:40f0:8", ["const:b54070:8", "const:4:8"]]
- 00b54070 ["CALL", null, ["callee:00bde040:8"]]
- 00b54070 bytes c8270294
- 00b54078 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:250:8"]]
- 00b54078 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54078 bytes 602a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13ebfb88258a2d4609bbd8ac41ff2035"></a>

### [`00b540cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b540cc.md) → [`00b54194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54194.md) _ZN8firebase13remote_config8internal26jni_config_update_listener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00b540fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b541c4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b540e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b540dc",
      "READ",
      [
        "storage",
        "010a1250",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b540e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b541c8"
      ]
    ],
    [
      "unmatched:00b540ec",
      "PARAM",
      [
        "storage",
        "002a629a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b541a4",
      "READ",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ],
    [
      "00b541a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b541c8"
      ]
    ],
    [
      "00b541b4",
      "PARAM",
      [
        "storage",
        "002a6293",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b540e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b540cc.md#insn-00b540e0) · [`00b540f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b540cc.md#insn-00b540f4) · [`00b540fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b540cc.md#insn-00b540fc)

~~~diff
- 00b540e0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b540e0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b540e0 bytes 080100b5
- 00b540f4 ["INT_ADD", "register:40f0:8", ["const:b540f4:8", "const:4:8"]]
- 00b540f4 ["CALL", null, ["callee:00bde040:8"]]
- 00b540f4 bytes a7270294
- 00b540fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:250:8"]]
- 00b540fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b540fc bytes 602a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-902dcb8315cf4e0f333fbf855c9eb693"></a>

### [`00b54160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54160.md) → [`00b54228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54228.md) _ZN8firebase13remote_config8internal26jni_config_update_listener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "site": "00b541b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b54280"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b541a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5423c",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b54194",
      "READ",
      [
        "storage",
        "010a1250",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b541b8",
      "WRITE",
      [
        "storage",
        "010a1258",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5423c",
      "READ",
      [
        "storage",
        "010a1318",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5425c",
      "READ",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54280",
      "WRITE",
      [
        "storage",
        "010a1318",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b541a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54160.md#insn-00b541a0) · [`00b541b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54160.md#insn-00b541b8)
- 新版 [`00b54268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54228.md#insn-00b54268)

~~~diff
- 00b541a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b541a0 ["INT_ADD", "register:40f0:8", ["const:b541a0:8", "const:4:8"]]
- 00b541a0 ["CALLIND", null, ["register:0:8"]]
- 00b541a0 bytes 00013fd6
- 00b541b8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b541b8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:258:8"]]
- 00b541b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b541b8 bytes a0620939
+ 00b54268 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b54268 ["INT_ADD", "register:40f0:8", ["const:b54268:8", "const:4:8"]]
+ 00b54268 ["CALLIND", null, ["register:0:8"]]
+ 00b54268 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-566dca61fc19ad31358e8a225ff8668d"></a>

### [`00b542ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b542ac.md) → [`00b54374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54374.md) _ZN8firebase13remote_config8internal26jni_config_update_listener11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b542cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b54394"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b542e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b54388",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b542d0"
      ]
    ],
    [
      "unmatched:00b542c8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b542cc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b54388",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b54398"
      ]
    ],
    [
      "00b54390",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b54394",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b542cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b542ac.md#insn-00b542cc) · [`00b542e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b542ac.md#insn-00b542e4)
- 新版 [`00b54394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54374.md#insn-00b54394)

~~~diff
- 00b542cc ["INT_ADD", "register:40f0:8", ["const:b542cc:8", "const:4:8"]]
- 00b542cc ["CALL", null, ["callee:00bde130:8"]]
- 00b542cc bytes 6d270294
- 00b542e4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b542e4 ["RETURN", null, ["register:0:8"]]
- 00b542e4 bytes c0035fd6
+ 00b54394 ["INT_ADD", "register:40f0:8", ["const:b54394:8", "const:4:8"]]
+ 00b54394 ["CALL", null, ["callee:00bde130:8"]]
+ 00b54394 bytes 67270294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-490f69ad4ef1bb68727c6ca4d7e909c7"></a>

### [`00b54394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54394.md) → [`00b5445c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5445c.md) _ZN8firebase13remote_config8internal13config_update19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00b543c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b54488"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b543a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5446c",
      "READ",
      [
        "storage",
        "010a1270",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b543a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5448c"
      ]
    ],
    [
      "unmatched:00b543b4",
      "PARAM",
      [
        "storage",
        "002ab173",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5446c",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54470",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5448c"
      ]
    ],
    [
      "00b5447c",
      "PARAM",
      [
        "storage",
        "002ab179",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b543a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54394.md#insn-00b543a8) · [`00b543b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54394.md#insn-00b543b8) · [`00b543c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b54394.md#insn-00b543c0)

~~~diff
- 00b543a8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b543a8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b543a8 bytes e80000b5
- 00b543b8 ["INT_ADD", "register:40f0:8", ["const:b543b8:8", "const:4:8"]]
- 00b543b8 ["CALL", null, ["callee:00bde040:8"]]
- 00b543b8 bytes f6260294
- 00b543c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:270:8"]]
- 00b543c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b543c0 bytes 603a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d17491f14e93fde31bece2744f5874b"></a>

### [`00b5471c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5471c.md) → [`00b547e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b547e4.md) _ZN8firebase13remote_config8internal35config_update_listener_registration19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8in

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00b54748"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b54810"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b54730"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5472c",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b54730",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b54814"
      ]
    ],
    [
      "unmatched:00b54738",
      "PARAM",
      [
        "storage",
        "00299889",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b547f4",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b547f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b54814"
      ]
    ],
    [
      "00b54800",
      "PARAM",
      [
        "storage",
        "00299916",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5471c.md#insn-00b54730) · [`00b54740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5471c.md#insn-00b54740) · [`00b54748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b54/00b5471c.md#insn-00b54748)

~~~diff
- 00b54730 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b54730 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b54730 bytes e80000b5
- 00b54740 ["INT_ADD", "register:40f0:8", ["const:b54740:8", "const:4:8"]]
- 00b54740 ["CALL", null, ["callee:00bde040:8"]]
- 00b54740 bytes 14260294
- 00b54748 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00b54748 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54748 bytes 604a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d77e3dbd7ddf98fd392ab8dbc6d20c4d"></a>

### [`00b55e34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55e34.md) → [`00b55efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55efc.md) _ZN8firebase13remote_config8internal18BoolResultCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b56714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56714.md) [`00b56a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b56/00b56a40.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md) [`00bde360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde360.md)
- 新版 呼出元 2件 [`00b567dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b567dc.md) [`00b56b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56b08.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00bde410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde410.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.55% / 新版 91.55%

CFGの説明率　旧版 54.55% / 新版 52.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55e68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b55f30"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55ed8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55e68",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55ed8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b55fb8"
      ]
    ],
    [
      "unmatched:00b55ee4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b55fc4"
      ]
    ]
  ],
  "added": [
    [
      "00b55f30",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b55fa0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b55fb8"
      ]
    ],
    [
      "00b55fac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b55fc4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b55e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55e34.md#insn-00b55e68) · [`00b55ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55e34.md#insn-00b55ed8) · [`00b55ee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55e34.md#insn-00b55ee4)

~~~diff
- 00b55e68 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b55e68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b55e68 bytes e80f00f9
- 00b55ed8 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00b55ed8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b55ed8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b55ed8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b55ed8 bytes c9000037
- 00b55ee4 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 00b55ee4 bytes c0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f28e4321ce7fa8c99d0c1f7facf07c5"></a>

### [`00b5a784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a784.md) → [`00b5a84c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a84c.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddcb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a7a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5a86c"
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
      "unmatched:00b5a798",
      "READ",
      [
        "storage",
        "00c1b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b5a7a4",
      "DATA",
      [
        "storage",
        "00c11a00",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00b5a860",
      "READ",
      [
        "storage",
        "00c1baa8",
        null,
        "pointer"
      ]
    ],
    [
      "00b5a86c",
      "DATA",
      [
        "storage",
        "00c11ab0",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a7a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a784.md#insn-00b5a7a4) · [`00b5a798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a784.md#insn-00b5a798)
- 新版 [`00b5a86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a84c.md#insn-00b5a86c)

~~~diff
- 00b5a7a4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b5a7a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b5a7a4 bytes 090000f9
+ 00b5a86c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00b5a86c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00b5a86c bytes 090000f9
- 00b5a798 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9f8:8"]]
- 00b5a798 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5a798 bytes 29fd44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a4951b3fcb8a40a361a79c91b712320"></a>

### [`00b5a8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a8f0.md) → [`00b5a9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a9b8.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistration6RemoveEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0590.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be0640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0640.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 40.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a920"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b5a9e8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a8f0.md#insn-00b5a920) · [`00b5a910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a8f0.md#insn-00b5a910)
- 新版 [`00b5a9e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a9b8.md#insn-00b5a9e8) · [`00b5a9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a9b8.md#insn-00b5a9d8)

~~~diff
- 00b5a920 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b5a920 ["RETURN", null, ["register:0:8"]]
- 00b5a920 bytes c0035fd6
+ 00b5a9e8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b5a9e8 ["RETURN", null, ["register:0:8"]]
+ 00b5a9e8 bytes c0035fd6
- 00b5a910 ["INT_ADD", "register:40f0:8", ["const:b5a910:8", "const:4:8"]]
- 00b5a910 ["CALL", null, ["callee:00be0640:8"]]
+ 00b5a9d8 ["INT_ADD", "register:40f0:8", ["const:b5a9d8:8", "const:4:8"]]
+ 00b5a9d8 ["CALL", null, ["callee:00be0640:8"]]
- 00b5a910 bytes 20170294
+ 00b5a9d8 bytes 1a170294
~~~


<a id="compare-7bb3c0ff345044367cb2cf6b011347b2"></a>

### [`00b5a934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a934.md) → [`00b5a9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a9fc.md) _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalC2EPNS1_20RemoteConfigInternalENSt6__ndk18functionIFvvEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be05a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be05a0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be0650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0650.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 57.14% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a99c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b5aa64"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a99c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a934.md#insn-00b5a99c) · [`00b5a968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a934.md#insn-00b5a968)
- 新版 [`00b5aa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a9fc.md#insn-00b5aa64) · [`00b5aa30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a9fc.md#insn-00b5aa30)

~~~diff
- 00b5a99c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b5a99c ["RETURN", null, ["register:0:8"]]
- 00b5a99c bytes c0035fd6
+ 00b5aa64 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b5aa64 ["RETURN", null, ["register:0:8"]]
+ 00b5aa64 bytes c0035fd6
- 00b5a968 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5a968 ["INT_ADD", "register:40f0:8", ["const:b5a968:8", "const:4:8"]]
- 00b5a968 ["CALLIND", null, ["register:0:8"]]
+ 00b5aa30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5aa30 ["INT_ADD", "register:40f0:8", ["const:b5aa30:8", "const:4:8"]]
+ 00b5aa30 ["CALLIND", null, ["register:0:8"]]
- 00b5a968 bytes 00013fd6
+ 00b5aa30 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0643376421a0611ce8ed466238ca392e"></a>

### [`00b5a9a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a9a0.md) → [`00b5aa68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5aa68.md) _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be05b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be05b0.md) · 呼出先 1件 [`00b00fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00fe0.md)
- 新版 呼出元 1件 [`00be0660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0660.md) · 呼出先 1件 [`00b010a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b010a8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 75.00% / 新版 81.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a9a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a9a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a9a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5a9a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5a9a4",
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
      "00b5aa68",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5aa6c",
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

- 旧版 [`00b5a9a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a9a0.md#insn-00b5a9a0) · [`00b5a9a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5a9a0.md#insn-00b5a9a4)
- 新版 [`00b5aa68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5aa68.md#insn-00b5aa68)

~~~diff
- 00b5a9a0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5a9a0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5a9a0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b5a9a0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5a9a0 bytes f44fbea9
- 00b5a9a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5a9a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5a9a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5a9a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5a9a4 bytes fd7b01a9
+ 00b5aa68 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00b5aa68 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00b5aa68 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00b5aa68 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b5aa68 bytes f44fbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6df609830b37a7feffa173812cf1b5c7"></a>

### [`00b5aa2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5aa2c.md) → [`00b5aaf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5aaf4.md) _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternal6RemoveEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0590.md) · 呼出先 1件 [`00b00fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00fe0.md)
- 新版 呼出元 1件 [`00be0640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0640.md) · 呼出先 1件 [`00b010a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b010a8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 60.00% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5aa50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5aa2c.md#insn-00b5aa50) · [`00b5aa64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5aa2c.md#insn-00b5aa64) · [`00b5aa68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5a/00b5aa2c.md#insn-00b5aa68)
- 新版 [`00b5ab18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5aaf4.md#insn-00b5ab18) · [`00b5ab30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5aaf4.md#insn-00b5ab30)

~~~diff
- 00b5aa50 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b5aa50 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b5ab18 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b5ab18 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b5aa50 bytes c80000b4
+ 00b5ab18 bytes c80000b4
- 00b5aa64 ["COPY", "register:0:8", ["register:4008:8"]]
- 00b5aa64 ["BRANCHIND", null, ["register:0:8"]]
- 00b5aa64 bytes 20001fd6
- 00b5aa68 ["INT_ADD", "register:40f0:8", ["const:b5aa68:8", "const:4:8"]]
- 00b5aa68 ["CALL", null, ["callee:00b010a8:8"]]
+ 00b5ab30 ["INT_ADD", "register:40f0:8", ["const:b5ab30:8", "const:4:8"]]
+ 00b5ab30 ["CALL", null, ["callee:00b010a8:8"]]
- 00b5aa68 bytes 5e99fe97
+ 00b5ab30 bytes 5e99fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-178610075ffbe47a8b3850eacde34e32"></a>

### [`00b5b7a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b7a8.md) → [`00b5b870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b870.md) _ZN8firebase4auth4Auth23RemoveAuthStateListenerEPNS0_17AuthStateListenerE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0970.md) · 呼出先 2件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00be0a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a20.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 77.94% / 新版 77.94%

CFGの説明率　旧版 22.22% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b838"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5b900"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b7fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5b8b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b5b814"
      ]
    ],
    [
      "unmatched:00b5b7fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5b904"
      ]
    ],
    [
      "unmatched:00b5b810",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5b8c0"
      ]
    ]
  ],
  "added": [
    [
      "00b5b8b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5b8dc"
      ]
    ],
    [
      "00b5b8c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5b904"
      ]
    ],
    [
      "00b5b8d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5b8c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b7fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b7a8.md#insn-00b5b7fc) · [`00b5b810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b7a8.md#insn-00b5b810) · [`00b5b818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5b7a8.md#insn-00b5b818)

~~~diff
- 00b5b7fc ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 00b5b7fc bytes 00020054
- 00b5b810 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b5b810 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b5b810 bytes 41ffff54
- 00b5b818 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 00b5b818 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-067261a4a703f216c5a5b8f1ed863e92"></a>

### [`00b5bc88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5bc88.md) → [`00b5bd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bd50.md) _ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEEC2ERKS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0a00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0a00.md) · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdddb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00be0ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ab0.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 25.00% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5bccc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5bd94"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5bd0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5bd80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b5bd08"
      ]
    ],
    [
      "unmatched:00b5bd0c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdde60"
      ]
    ]
  ],
  "added": [
    [
      "00b5bd80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5bdd0"
      ]
    ],
    [
      "00b5bdd4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdde60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5bccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5bc88.md#insn-00b5bccc) · [`00b5bd04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5bc88.md#insn-00b5bd04) · [`00b5bd0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5bc88.md#insn-00b5bd0c)

~~~diff
- 00b5bccc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00b5bccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5bccc bytes 680a00f9
- 00b5bd04 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b5bd04 ["RETURN", null, ["register:0:8"]]
- 00b5bd04 bytes c0035fd6
- 00b5bd0c ["INT_ADD", "register:40f0:8", ["const:b5bd0c:8", "const:4:8"]]
- 00b5bd0c ["CALL", null, ["callee:00bdde60:8"]]
- 00b5bd0c bytes 29080294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a339b89e3acd40fefdbb338bae1c73a3"></a>

### [`00b5beb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5beb0.md) → [`00b5bf78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bf78.md) _ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEEC2ERKS7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be09e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be09e0.md) · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdddb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00be0a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a90.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 33.33% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5bed4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5bf9c"
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
      "unmatched:00b5bed4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5bfe8"
      ]
    ]
  ],
  "added": [
    [
      "00b5bf9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5bfe8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5bed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5beb0.md#insn-00b5bed4) · [`00b5bed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5b/00b5beb0.md#insn-00b5bed0)
- 新版 [`00b5bf9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5bf78.md#insn-00b5bf9c)

~~~diff
- 00b5bed4 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00b5bed4 bytes 60020054
+ 00b5bf9c ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 00b5bf9c bytes 60020054
- 00b5bed0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b5bed0 ["INT_LESSEQUAL", "register:105:1", ["tmp:0:8", "register:4048:8"]]
- 00b5bed0 ["INT_SBORROW", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b5bed0 ["INT_SUB", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b5bed0 bytes 200108eb
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b78ce1b578db2feb6d8f612d2c7b2b6"></a>

### [`00b5c79c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c79c.md) → [`00b5c864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c864.md) _ZN8firebase4auth14ClearUserInfosEPNS0_8AuthDataE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be08a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be08a0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be0950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0950.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 20.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c7b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5c880"
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
      "unmatched:00b5c7b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5c8cc"
      ]
    ]
  ],
  "added": [
    [
      "00b5c880",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5c8cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c7b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c79c.md#insn-00b5c7b8) · [`00b5c7b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c79c.md#insn-00b5c7b4)
- 新版 [`00b5c880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c864.md#insn-00b5c880)

~~~diff
- 00b5c7b8 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00b5c7b8 bytes 60020054
+ 00b5c880 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 00b5c880 bytes 60020054
- 00b5c7b4 ["INT_LESSEQUAL", "register:105:1", ["register:4048:8", "register:4040:8"]]
- 00b5c7b4 ["INT_SBORROW", "register:106:1", ["register:4040:8", "register:4048:8"]]
- 00b5c7b4 ["INT_SUB", "tmp:0:8", ["register:4040:8", "register:4048:8"]]
- 00b5c7b4 ["INT_SLESS", "register:107:1", ["tmp:0:8", "const:0:8"]]
- 00b5c7b4 bytes 1f0109eb
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4503004955e7ac95006177c2ed1ca98"></a>

### [`00b5c870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c870.md) → [`00b5c938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c938.md) _ZNK8firebase4auth4UsereqERKS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddaf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddaf0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bddba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddba0.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

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
      "site": "00b5c8a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b5c968"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c8a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c870.md#insn-00b5c8a0) · [`00b5c880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c870.md#insn-00b5c880)
- 新版 [`00b5c968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c938.md#insn-00b5c968) · [`00b5c948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c938.md#insn-00b5c948)

~~~diff
- 00b5c8a0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b5c8a0 ["RETURN", null, ["register:0:8"]]
- 00b5c8a0 bytes c0035fd6
+ 00b5c968 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b5c968 ["RETURN", null, ["register:0:8"]]
+ 00b5c968 bytes c0035fd6
- 00b5c880 ["INT_ADD", "register:40f0:8", ["const:b5c880:8", "const:4:8"]]
- 00b5c880 ["CALL", null, ["callee:00bddba0:8"]]
+ 00b5c948 ["INT_ADD", "register:40f0:8", ["const:b5c948:8", "const:4:8"]]
+ 00b5c948 ["CALL", null, ["callee:00bddba0:8"]]
- 00b5c880 bytes 9c040294
+ 00b5c948 bytes 96040294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fa883f1d5a49978266367c553b32519"></a>

### [`00b5cf2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cf2c.md) → [`00b5cff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cff4.md) _ZN8firebase4auth17signinmethodquery10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b5cf4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b5d014"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5cf64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d008",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b5cf50"
      ]
    ],
    [
      "unmatched:00b5cf48",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b5cf4c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b5d008",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d018"
      ]
    ],
    [
      "00b5d010",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b5d014",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cf4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cf2c.md#insn-00b5cf4c) · [`00b5cf64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cf2c.md#insn-00b5cf64)
- 新版 [`00b5d014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cff4.md#insn-00b5d014)

~~~diff
- 00b5cf4c ["INT_ADD", "register:40f0:8", ["const:b5cf4c:8", "const:4:8"]]
- 00b5cf4c ["CALL", null, ["callee:00bde130:8"]]
- 00b5cf4c bytes 4d040294
- 00b5cf64 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b5cf64 ["RETURN", null, ["register:0:8"]]
- 00b5cf64 bytes c0035fd6
+ 00b5d014 ["INT_ADD", "register:40f0:8", ["const:b5d014:8", "const:4:8"]]
+ 00b5d014 ["CALL", null, ["callee:00bde130:8"]]
+ 00b5d014 bytes 47040294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebafdd8ed99b203c6cba0476cce350b8"></a>

### [`00b5d1c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d1c8.md) → [`00b5d290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d290.md) _ZN8firebase4auth11jnilistener11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b5d1e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b5d2b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d200"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5d2a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b5d1ec"
      ]
    ],
    [
      "unmatched:00b5d1e4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b5d1e8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b5d2a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d2b4"
      ]
    ],
    [
      "00b5d2ac",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b5d2b0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d1e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d1c8.md#insn-00b5d1e8) · [`00b5d200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5d/00b5d1c8.md#insn-00b5d200)
- 新版 [`00b5d2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d290.md#insn-00b5d2b0)

~~~diff
- 00b5d1e8 ["INT_ADD", "register:40f0:8", ["const:b5d1e8:8", "const:4:8"]]
- 00b5d1e8 ["CALL", null, ["callee:00bde130:8"]]
- 00b5d1e8 bytes a6030294
- 00b5d200 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b5d200 ["RETURN", null, ["register:0:8"]]
- 00b5d200 bytes c0035fd6
+ 00b5d2b0 ["INT_ADD", "register:40f0:8", ["const:b5d2b0:8", "const:4:8"]]
+ 00b5d2b0 ["CALL", null, ["callee:00bde130:8"]]
+ 00b5d2b0 bytes a0030294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6650db08881c31286f342b261c2cfcba"></a>

### [`00b5e37c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e37c.md) → [`00b5e444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e444.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4Auth20FetchProvidersResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFut

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0be0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0be0.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md) [`00be0ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0ad0.md)
- 新版 呼出元 1件 [`00be0c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c90.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 27.27% / 新版 23.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e41c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5e4e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e434"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5e41c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e510"
      ]
    ]
  ],
  "added": [
    [
      "00b5e4e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e510"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5e41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e37c.md#insn-00b5e41c) · [`00b5e434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e37c.md#insn-00b5e434)
- 新版 [`00b5e4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e444.md#insn-00b5e4e4)

~~~diff
- 00b5e41c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b5e41c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b5e41c bytes 61010054
- 00b5e434 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b5e434 ["RETURN", null, ["register:0:8"]]
- 00b5e434 bytes c0035fd6
+ 00b5e4e4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b5e4e4 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00b5e4e4 bytes 61010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-002d2de3b908a256e098a67e8b44e9cc"></a>

### [`00b608e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b608e4.md) → [`00b609ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b609ac.md) _ZN8firebase6FutureINS_4auth4UserEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0c50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c50.md) · 呼出先 3件 [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdde70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde70.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md)
- 新版 呼出元 1件 [`00be0d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d00.md) · 呼出先 3件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 83.87% / 新版 83.87%

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
      "site": "00b6092c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b609f4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6095c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6092c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b609f4",
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

- 旧版 [`00b6092c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b608e4.md#insn-00b6092c) · [`00b6095c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b608e4.md#insn-00b6095c)
- 新版 [`00b609f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b609ac.md#insn-00b609f4)

~~~diff
- 00b6092c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6092c ["INT_ADD", "register:40f0:8", ["const:b6092c:8", "const:4:8"]]
- 00b6092c ["CALLIND", null, ["register:0:8"]]
- 00b6092c bytes 00013fd6
- 00b6095c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6095c ["RETURN", null, ["register:0:8"]]
- 00b6095c bytes c0035fd6
+ 00b609f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b609f4 ["INT_ADD", "register:40f0:8", ["const:b609f4:8", "const:4:8"]]
+ 00b609f4 ["CALLIND", null, ["register:0:8"]]
+ 00b609f4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66f8000f82e81cbdb8dde82d0a952bd5"></a>

### [`00b60a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60a8c.md) → [`00b60b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60b54.md) _ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`00b5fa7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5fa7c.md) [`00b6fd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fd1c.md) [`00b6ff44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6ff44.md) [`00b70a1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70a1c.md) [`00b70c0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70c0c.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md) [`00be0af0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0af0.md)
- 新版 呼出元 8件 [`00b5fb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fb44.md) [`00b6fde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fde4.md) [`00b7000c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b7000c.md) [`00b70ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70ae4.md) [`00b70cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70cd4.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ba0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 50.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60b44"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b60c0c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b60b44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60a8c.md#insn-00b60b44) · [`00b60ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60a8c.md#insn-00b60ac4)
- 新版 [`00b60c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60b54.md#insn-00b60c0c) · [`00b60b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60b54.md#insn-00b60b8c)

~~~diff
- 00b60b44 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b60b44 ["RETURN", null, ["register:0:8"]]
- 00b60b44 bytes c0035fd6
+ 00b60c0c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b60c0c ["RETURN", null, ["register:0:8"]]
+ 00b60c0c bytes c0035fd6
- 00b60ac4 ["INT_ADD", "register:40f0:8", ["const:b60ac4:8", "const:4:8"]]
- 00b60ac4 ["CALL", null, ["callee:00be0cd0:8"]]
+ 00b60b8c ["INT_ADD", "register:40f0:8", ["const:b60b8c:8", "const:4:8"]]
+ 00b60b8c ["CALL", null, ["callee:00be0cd0:8"]]
- 00b60ac4 bytes 57000294
+ 00b60b8c bytes 51000294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45bae516d177f92fa025f346c26e8d6b"></a>

### [`00b60ef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60ef8.md) → [`00b60fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60fc0.md) _ZN8firebase4auth10authresult11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b60ef8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60efc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60efc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b60ef8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b60efc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b60fd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b60f1c"
      ]
    ]
  ],
  "added": [
    [
      "00b60fc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b60fc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b60fd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b60fe4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60ef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60ef8.md#insn-00b60ef8) · [`00b60efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60ef8.md#insn-00b60efc) · [`00b60f18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60ef8.md#insn-00b60f18)

~~~diff
- 00b60ef8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b60ef8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b60ef8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b60ef8 bytes f30f1ef8
- 00b60efc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b60efc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b60efc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b60efc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b60efc bytes fd7b01a9
- 00b60f18 ["INT_ADD", "register:40f0:8", ["const:b60f18:8", "const:4:8"]]
- 00b60f18 ["CALL", null, ["callee:00bde130:8"]]
- 00b60f18 bytes 5af40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6463bb3dd06ea535c0a13ad2e9747e3"></a>

### [`00b610e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b610e8.md) → [`00b611b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b611b0.md) _ZN8firebase4auth20additional_user_info8GetClassEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b610f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b611b8"
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
      "unmatched:00b610ec",
      "READ",
      [
        "storage",
        "010a1470",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b611b4",
      "READ",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b610f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b610e8.md#insn-00b610f0) · [`00b610e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b610e8.md#insn-00b610e8)
- 新版 [`00b611b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b611b0.md#insn-00b611b8)

~~~diff
- 00b610f0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b610f0 ["RETURN", null, ["register:0:8"]]
- 00b610f0 bytes c0035fd6
+ 00b611b8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b611b8 ["RETURN", null, ["register:0:8"]]
+ 00b611b8 bytes c0035fd6
- 00b610e8 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b610e8 bytes 082a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-222d3084827d44e089d9b7f381d9b2cf"></a>

### [`00b610f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b610f4.md) → [`00b611bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b611bc.md) _ZN8firebase4auth20additional_user_info15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "site": "00b610f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b610f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b610f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b610f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b610f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b610fc",
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
      "00b611bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b611c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b611c4",
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

- 旧版 [`00b610f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b610f4.md#insn-00b610f4) · [`00b610f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b610f4.md#insn-00b610f8) · [`00b610fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b610f4.md#insn-00b610fc)

~~~diff
- 00b610f4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b610f4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b610f4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b610f4 bytes f50f1df8
- 00b610f8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b610f8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b610f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b610f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b610f8 bytes f44f01a9
- 00b610fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b610fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b610fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b610fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b610fc bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3099075f7ccb638e66bd8b56eab817b0"></a>

### [`00b61240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61240.md) → [`00b61308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61308.md) _ZN8firebase4auth20additional_user_info11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b61240"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61244"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61244"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61240",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b61244",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b6131c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b61264"
      ]
    ]
  ],
  "added": [
    [
      "00b61308",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6130c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b6131c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6132c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61240.md#insn-00b61240) · [`00b61244`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61240.md#insn-00b61244) · [`00b61260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61240.md#insn-00b61260)

~~~diff
- 00b61240 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b61240 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b61240 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b61240 bytes f30f1ef8
- 00b61244 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b61244 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b61244 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b61244 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b61244 bytes fd7b01a9
- 00b61260 ["INT_ADD", "register:40f0:8", ["const:b61260:8", "const:4:8"]]
- 00b61260 ["CALL", null, ["callee:00bde130:8"]]
- 00b61260 bytes 88f30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1247ad3f9e08d13efa60d13008b7f6e5"></a>

### [`00b61588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61588.md) → [`00b61650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61650.md) _ZN8firebase4auth27api_not_available_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b61588"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6158c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6158c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61588",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6158c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b61664",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b615ac"
      ]
    ]
  ],
  "added": [
    [
      "00b61650",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b61654",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b61664",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61674"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61588.md#insn-00b61588) · [`00b6158c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61588.md#insn-00b6158c) · [`00b615a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61588.md#insn-00b615a8)

~~~diff
- 00b61588 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b61588 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b61588 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b61588 bytes f30f1ef8
- 00b6158c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6158c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6158c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6158c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6158c bytes fd7b01a9
- 00b615a8 ["INT_ADD", "register:40f0:8", ["const:b615a8:8", "const:4:8"]]
- 00b615a8 ["CALL", null, ["callee:00bde130:8"]]
- 00b615a8 bytes b6f20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc5269af943dc7374ed78589cdab6fe2"></a>

### [`00b61784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61784.md) → [`00b6184c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6184c.md) _ZN8firebase4auth21action_code_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 25.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b617dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b618a4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b617c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b61860",
      "READ",
      [
        "storage",
        "010a14c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6186c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b617e0"
      ]
    ],
    [
      "unmatched:00b617b8",
      "READ",
      [
        "storage",
        "010a14c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61860",
      "READ",
      [
        "storage",
        "010a1588",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6186c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b618a8"
      ]
    ],
    [
      "00b61880",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b617c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61784.md#insn-00b617c4) · [`00b617dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61784.md#insn-00b617dc) · [`00b617ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61784.md#insn-00b617ec)

~~~diff
- 00b617c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b617c4 ["INT_ADD", "register:40f0:8", ["const:b617c4:8", "const:4:8"]]
- 00b617c4 ["CALLIND", null, ["register:0:8"]]
- 00b617c4 bytes 00013fd6
- 00b617dc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b617dc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4c8:8"]]
- 00b617dc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b617dc bytes a0221339
- 00b617ec ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b617ec ["RETURN", null, ["register:0:8"]]
- 00b617ec bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49d68fd8a5902fd85366cad25483c260"></a>

### [`00b6197c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b6197c.md) → [`00b61a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61a44.md) _ZN8firebase4auth21action_code_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b6199c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b61a64"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b619b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b61a58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b619a0"
      ]
    ],
    [
      "unmatched:00b61998",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6199c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b61a58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61a68"
      ]
    ],
    [
      "00b61a60",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b61a64",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6199c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b6197c.md#insn-00b6199c) · [`00b619b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b6197c.md#insn-00b619b4)
- 新版 [`00b61a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61a44.md#insn-00b61a64)

~~~diff
- 00b6199c ["INT_ADD", "register:40f0:8", ["const:b6199c:8", "const:4:8"]]
- 00b6199c ["CALL", null, ["callee:00bde130:8"]]
- 00b6199c bytes b9f10194
- 00b619b4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b619b4 ["RETURN", null, ["register:0:8"]]
- 00b619b4 bytes c0035fd6
+ 00b61a64 ["INT_ADD", "register:40f0:8", ["const:b61a64:8", "const:4:8"]]
+ 00b61a64 ["CALL", null, ["callee:00bde130:8"]]
+ 00b61a64 bytes b3f10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e5ada87e08921a5c2b24f44c6f14688"></a>

### [`00b61ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61ac0.md) → [`00b61b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b88.md) _ZN8firebase4auth15email_exception8GetClassEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b61ac8"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b61b90"
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
      "unmatched:00b61ac4",
      "READ",
      [
        "storage",
        "010a14e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61b8c",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61ac0.md#insn-00b61ac8) · [`00b61ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61ac0.md#insn-00b61ac0)
- 新版 [`00b61b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b88.md#insn-00b61b90)

~~~diff
- 00b61ac8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b61ac8 ["RETURN", null, ["register:0:8"]]
- 00b61ac8 bytes c0035fd6
+ 00b61b90 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b61b90 ["RETURN", null, ["register:0:8"]]
+ 00b61b90 bytes c0035fd6
- 00b61ac0 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b61ac0 bytes 082a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b80479522098e1c09700dde4e8dd8653"></a>

### [`00b61b38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61b38.md) → [`00b61c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61c00.md) _ZN8firebase4auth15email_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 11.11% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61b74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61b94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b61c3c"
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
      "00b61c14",
      "READ",
      [
        "storage",
        "010a14e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b61b50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b61b98"
      ]
    ],
    [
      "00b61c20",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b61c14",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61c18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61c60"
      ]
    ],
    [
      "00b61c20",
      "READ",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61b50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61b38.md#insn-00b61b50) · [`00b61b74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61b38.md#insn-00b61b74) · [`00b61b7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61b38.md#insn-00b61b7c)

~~~diff
- 00b61b50 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b61b50 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b61b50 bytes 410200b4
- 00b61b74 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b61b74 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b61b74 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4e8:8"]]
- 00b61b74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b61b74 bytes bfa21339
- 00b61b7c ["INT_ADD", "register:40f0:8", ["const:b61b7c:8", "const:4:8"]]
- 00b61b7c ["CALL", null, ["callee:00bde090:8"]]
- 00b61b7c bytes 19f10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c4da846e94c2b56470311e97c0b5db5"></a>

### [`00b61c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61c18.md) → [`00b61ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61ce0.md) _ZN8firebase4auth15email_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

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
      "site": "00b61c38"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b61d00"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61c50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b61cf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b61c3c"
      ]
    ],
    [
      "unmatched:00b61c34",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b61c38",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b61cf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61d04"
      ]
    ],
    [
      "00b61cfc",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b61d00",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61c18.md#insn-00b61c38) · [`00b61c50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61c18.md#insn-00b61c50)
- 新版 [`00b61d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61ce0.md#insn-00b61d00)

~~~diff
- 00b61c38 ["INT_ADD", "register:40f0:8", ["const:b61c38:8", "const:4:8"]]
- 00b61c38 ["CALL", null, ["callee:00bde130:8"]]
- 00b61c38 bytes 12f10194
- 00b61c50 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b61c50 ["RETURN", null, ["register:0:8"]]
- 00b61c50 bytes c0035fd6
+ 00b61d00 ["INT_ADD", "register:40f0:8", ["const:b61d00:8", "const:4:8"]]
+ 00b61d00 ["CALL", null, ["callee:00bde130:8"]]
+ 00b61d00 bytes 0cf10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a909b47999afab4f039377d71cb37bf"></a>

### [`00b61cc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61cc4.md) → [`00b61d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61d8c.md) _ZN8firebase4auth15email_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b61cd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b61da0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61ce4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61cd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b61ce8"
      ]
    ],
    [
      "unmatched:00b61ce0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b61ce4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b61da0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61db0"
      ]
    ],
    [
      "00b61da8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b61dac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61cd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61cc4.md#insn-00b61cd8) · [`00b61ce4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61cc4.md#insn-00b61ce4) · [`00b61cfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61cc4.md#insn-00b61cfc)

~~~diff
- 00b61cd8 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b61cd8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b61cd8 bytes 8b000054
- 00b61ce4 ["INT_ADD", "register:40f0:8", ["const:b61ce4:8", "const:4:8"]]
- 00b61ce4 ["CALL", null, ["callee:00bde130:8"]]
- 00b61ce4 bytes e7f00194
- 00b61cfc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b61cfc ["RETURN", null, ["register:0:8"]]
- 00b61cfc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97e14cac77e582f71f44de10c413aba9"></a>

### [`00b6200c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6200c.md) → [`00b620d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b620d4.md) _ZN8firebase4auth23weak_password_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b6200c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62010"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62010"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6200c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b62010",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b62020",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b62030"
      ]
    ]
  ],
  "added": [
    [
      "00b620d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b620d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b620e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b620f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6200c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6200c.md#insn-00b6200c) · [`00b62010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6200c.md#insn-00b62010) · [`00b62020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6200c.md#insn-00b62020)

~~~diff
- 00b6200c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b6200c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b6200c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6200c bytes f30f1ef8
- 00b62010 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b62010 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b62010 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b62010 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b62010 bytes fd7b01a9
- 00b62020 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b62020 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b62020 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc58325bb7350b454185a7f3f33ee57b"></a>

### [`00b620c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b620c8.md) → [`00b62190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62190.md) _ZN8firebase4auth29invalid_credentials_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00b620f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b621c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b620dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b621a0",
      "READ",
      [
        "storage",
        "010a1520",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b620dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b621c4"
      ]
    ],
    [
      "unmatched:00b620e8",
      "PARAM",
      [
        "storage",
        "002a8fb1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b621a0",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b621a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b621c4"
      ]
    ],
    [
      "00b621b0",
      "PARAM",
      [
        "storage",
        "002a8f1d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b620dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b620c8.md#insn-00b620dc) · [`00b620f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b620c8.md#insn-00b620f0) · [`00b620f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b620c8.md#insn-00b620f8)

~~~diff
- 00b620dc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b620dc ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b620dc bytes 080100b5
- 00b620f0 ["INT_ADD", "register:40f0:8", ["const:b620f0:8", "const:4:8"]]
- 00b620f0 ["CALL", null, ["callee:00bde040:8"]]
- 00b620f0 bytes a8ef0194
- 00b620f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:520:8"]]
- 00b620f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b620f8 bytes 609202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d25e101cdef2d6cf7b51d0ada8cddaa3"></a>

### [`00b62150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62150.md) → [`00b62218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62218.md) _ZN8firebase4auth29invalid_credentials_exception8GetClassEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00b62158"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b62220"
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
      "unmatched:00b62154",
      "READ",
      [
        "storage",
        "010a1520",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6221c",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62150.md#insn-00b62158) · [`00b62150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62150.md#insn-00b62150)
- 新版 [`00b62220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62218.md#insn-00b62220)

~~~diff
- 00b62158 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b62158 ["RETURN", null, ["register:0:8"]]
- 00b62158 bytes c0035fd6
+ 00b62220 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b62220 ["RETURN", null, ["register:0:8"]]
+ 00b62220 bytes c0035fd6
- 00b62150 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b62150 bytes e82900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df750c6bb96012866259662910aa9c70"></a>

### [`00b6215c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6215c.md) → [`00b62224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62224.md) _ZN8firebase4auth29invalid_credentials_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b621b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6227c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6219c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b62238",
      "READ",
      [
        "storage",
        "010a1528",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b62190",
      "READ",
      [
        "storage",
        "010a1520",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b621b4",
      "WRITE",
      [
        "storage",
        "010a1528",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b62238",
      "READ",
      [
        "storage",
        "010a15e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62258",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6227c",
      "WRITE",
      [
        "storage",
        "010a15e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6219c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6215c.md#insn-00b6219c) · [`00b621b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6215c.md#insn-00b621b4)
- 新版 [`00b62264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62224.md#insn-00b62264)

~~~diff
- 00b6219c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6219c ["INT_ADD", "register:40f0:8", ["const:b6219c:8", "const:4:8"]]
- 00b6219c ["CALLIND", null, ["register:0:8"]]
- 00b6219c bytes 00013fd6
- 00b621b4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b621b4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:528:8"]]
- 00b621b4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b621b4 bytes a0a21439
+ 00b62264 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b62264 ["INT_ADD", "register:40f0:8", ["const:b62264:8", "const:4:8"]]
+ 00b62264 ["CALLIND", null, ["register:0:8"]]
+ 00b62264 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e80998dd51a45aecc991999c20d76b0"></a>

### [`00b621c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b621c8.md) → [`00b62290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62290.md) _ZN8firebase4auth29invalid_credentials_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

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
      "site": "00b62204"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62224"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b622cc"
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
      "00b622a4",
      "READ",
      [
        "storage",
        "010a1520",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b621e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b622f0"
      ]
    ],
    [
      "unmatched:00b621e8",
      "READ",
      [
        "storage",
        "010a1528",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b622a4",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b622a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b622f0"
      ]
    ],
    [
      "00b622b0",
      "READ",
      [
        "storage",
        "010a15e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b621e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b621c8.md#insn-00b621e0) · [`00b62204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b621c8.md#insn-00b62204) · [`00b6220c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b621c8.md#insn-00b6220c)

~~~diff
- 00b621e0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b621e0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b621e0 bytes 410200b4
- 00b62204 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b62204 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b62204 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:528:8"]]
- 00b62204 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b62204 bytes bfa21439
- 00b6220c ["INT_ADD", "register:40f0:8", ["const:b6220c:8", "const:4:8"]]
- 00b6220c ["CALL", null, ["callee:00bde090:8"]]
- 00b6220c bytes 75ef0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-697ab7b54270cf7c6a10ee47b7dacbb2"></a>

### [`00b622a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b622a8.md) → [`00b62370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62370.md) _ZN8firebase4auth29invalid_credentials_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b622a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b622ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b622ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b622a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b622ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b62384",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b622cc"
      ]
    ]
  ],
  "added": [
    [
      "00b62370",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b62374",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b62384",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b62394"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b622a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b622a8.md#insn-00b622a8) · [`00b622ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b622a8.md#insn-00b622ac) · [`00b622c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b622a8.md#insn-00b622c8)

~~~diff
- 00b622a8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b622a8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b622a8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b622a8 bytes f30f1ef8
- 00b622ac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b622ac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b622ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b622ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b622ac bytes fd7b01a9
- 00b622c8 ["INT_ADD", "register:40f0:8", ["const:b622c8:8", "const:4:8"]]
- 00b622c8 ["CALL", null, ["callee:00bde130:8"]]
- 00b622c8 bytes 6eef0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0885da852f44be5aa4635fff7e0c914d"></a>

### [`00b62354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62354.md) → [`00b6241c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6241c.md) _ZN8firebase4auth29invalid_credentials_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b62374"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b6243c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6238c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b62430",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b62378"
      ]
    ],
    [
      "unmatched:00b62370",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b62374",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b62430",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b62440"
      ]
    ],
    [
      "00b62438",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b6243c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62354.md#insn-00b62374) · [`00b6238c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62354.md#insn-00b6238c)
- 新版 [`00b6243c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6241c.md#insn-00b6243c)

~~~diff
- 00b62374 ["INT_ADD", "register:40f0:8", ["const:b62374:8", "const:4:8"]]
- 00b62374 ["CALL", null, ["callee:00bde130:8"]]
- 00b62374 bytes 43ef0194
- 00b6238c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6238c ["RETURN", null, ["register:0:8"]]
- 00b6238c bytes c0035fd6
+ 00b6243c ["INT_ADD", "register:40f0:8", ["const:b6243c:8", "const:4:8"]]
+ 00b6243c ["CALL", null, ["callee:00bde130:8"]]
+ 00b6243c bytes 3def0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64f1b96cb1f721fd70256850befbcb16"></a>

### [`00b62410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62410.md) → [`00b624d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b624d8.md) _ZN8firebase4auth22invalid_user_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00b62440"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b62508"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62424"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b62420",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b62424",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b62444"
      ]
    ],
    [
      "unmatched:00b62430",
      "PARAM",
      [
        "storage",
        "002924df",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b624e8",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b624ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6250c"
      ]
    ],
    [
      "00b624f8",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62410.md#insn-00b62424) · [`00b62438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62410.md#insn-00b62438) · [`00b62440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62410.md#insn-00b62440)

~~~diff
- 00b62424 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b62424 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b62424 bytes 080100b5
- 00b62438 ["INT_ADD", "register:40f0:8", ["const:b62438:8", "const:4:8"]]
- 00b62438 ["CALL", null, ["callee:00bde040:8"]]
- 00b62438 bytes d6ee0194
- 00b62440 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:540:8"]]
- 00b62440 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62440 bytes 60a202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e49233cd463ecbcc98455d9f0a7dc5e"></a>

### [`00b6269c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6269c.md) → [`00b62764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62764.md) _ZN8firebase4auth22invalid_user_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b6269c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b626a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b626a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6269c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b626a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b62778",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b626c0"
      ]
    ]
  ],
  "added": [
    [
      "00b62764",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b62768",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b62778",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b62788"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6269c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6269c.md#insn-00b6269c) · [`00b626a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6269c.md#insn-00b626a0) · [`00b626bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6269c.md#insn-00b626bc)

~~~diff
- 00b6269c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b6269c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b6269c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6269c bytes f30f1ef8
- 00b626a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b626a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b626a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b626a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b626a0 bytes fd7b01a9
- 00b626bc ["INT_ADD", "register:40f0:8", ["const:b626bc:8", "const:4:8"]]
- 00b626bc ["CALL", null, ["callee:00bde130:8"]]
- 00b626bc bytes 71ee0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e62ec96546c0beceb6de9f80453bd56"></a>

### [`00b63a4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63a4c.md) → [`00b63b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63b14.md) _ZN8firebase4auth27too_many_requests_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b63a6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b63b34"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63a84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b63b28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b63a70"
      ]
    ],
    [
      "unmatched:00b63a68",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b63a6c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b63b28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b63b38"
      ]
    ],
    [
      "00b63b30",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b63b34",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63a4c.md#insn-00b63a6c) · [`00b63a84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63a4c.md#insn-00b63a84)
- 新版 [`00b63b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63b14.md#insn-00b63b34)

~~~diff
- 00b63a6c ["INT_ADD", "register:40f0:8", ["const:b63a6c:8", "const:4:8"]]
- 00b63a6c ["CALL", null, ["callee:00bde130:8"]]
- 00b63a6c bytes 85e90194
- 00b63a84 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b63a84 ["RETURN", null, ["register:0:8"]]
- 00b63a84 bytes c0035fd6
+ 00b63b34 ["INT_ADD", "register:40f0:8", ["const:b63b34:8", "const:4:8"]]
+ 00b63b34 ["CALL", null, ["callee:00bde130:8"]]
+ 00b63b34 bytes 7fe90194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2be76260b4cd35d24a9ae043eae55d71"></a>

### [`00b63ce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63ce8.md) → [`00b63db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63db0.md) _ZN8firebase4auth18firebase_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b63d08"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b63dd0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63d20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b63dc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b63d0c"
      ]
    ],
    [
      "unmatched:00b63d04",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b63d08",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b63dc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b63dd4"
      ]
    ],
    [
      "00b63dcc",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b63dd0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63d08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63ce8.md#insn-00b63d08) · [`00b63d20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63ce8.md#insn-00b63d20)
- 新版 [`00b63dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63db0.md#insn-00b63dd0)

~~~diff
- 00b63d08 ["INT_ADD", "register:40f0:8", ["const:b63d08:8", "const:4:8"]]
- 00b63d08 ["CALL", null, ["callee:00bde130:8"]]
- 00b63d08 bytes dee80194
- 00b63d20 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b63d20 ["RETURN", null, ["register:0:8"]]
- 00b63d20 bytes c0035fd6
+ 00b63dd0 ["INT_ADD", "register:40f0:8", ["const:b63dd0:8", "const:4:8"]]
+ 00b63dd0 ["CALL", null, ["callee:00bde130:8"]]
+ 00b63dd0 bytes d8e80194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4f6e169f360d1cfa8a009fa16e188e3"></a>

### [`00b64c44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64c44.md) → [`00b64d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64d0c.md) _ZN8firebase4auth30CheckAndClearJniAuthExceptionsEP7_JNIEnvPNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c10.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddfd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfd0.md) [`00be0c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c80.md)
- 新版 呼出元 1件 [`00be0cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0cc0.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde080.md) [`00be0d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d30.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.30% / 新版 87.30%

CFGの説明率　旧版 52.94% / 新版 45.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b64c6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b64d34"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b64c78"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b64c6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b64c78",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b64d34",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b64d40",
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

- 旧版 [`00b64c6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64c44.md#insn-00b64c6c) · [`00b64c78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64c44.md#insn-00b64c78)
- 新版 [`00b64d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64d0c.md#insn-00b64d34)

~~~diff
- 00b64c6c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b64c6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b64c6c bytes e80f00f9
- 00b64c78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b64c78 ["INT_ADD", "register:40f0:8", ["const:b64c78:8", "const:4:8"]]
- 00b64c78 ["CALLIND", null, ["register:0:8"]]
- 00b64c78 bytes 00013fd6
+ 00b64d34 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
+ 00b64d34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b64d34 bytes e80f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc89dce090b60672795137d30e66f5e9"></a>

### [`00b64d40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64d40.md) → [`00b64e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64e08.md) _ZN8firebase4auth34MapFutureCallbackResultToAuthErrorEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0c20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c20.md) · 呼出先 1件 [`00be0c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c80.md)
- 新版 呼出元 1件 [`00be0cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0cd0.md) · 呼出先 1件 [`00be0d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 50.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b64d44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b64e0c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b64d48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b64d48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b64e30"
      ]
    ]
  ],
  "added": [
    [
      "00b64e10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b64e30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b64d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64d40.md#insn-00b64d44) · [`00b64d48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64d40.md#insn-00b64d48)
- 新版 [`00b64e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64e08.md#insn-00b64e0c)

~~~diff
- 00b64d44 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b64d44 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b64d44 ["COPY", "tmp:2:8", ["register:4018:8"]]
- 00b64d44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b64d44 bytes 7f000039
- 00b64d48 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00b64d48 bytes 00010054
+ 00b64e0c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b64e0c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b64e0c ["COPY", "tmp:2:8", ["register:4018:8"]]
+ 00b64e0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b64e0c bytes 7f000039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b596c00d4a7eff184760eac1dfe01f2"></a>

### [`00b65758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65758.md) → [`00b65820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65820.md) _ZN8firebase4auth10credential10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b65778"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b65840"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65790"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65834",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6577c"
      ]
    ],
    [
      "unmatched:00b65774",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b65778",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b65834",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65844"
      ]
    ],
    [
      "00b6583c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b65840",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65758.md#insn-00b65778) · [`00b65790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65758.md#insn-00b65790)
- 新版 [`00b65840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65820.md#insn-00b65840)

~~~diff
- 00b65778 ["INT_ADD", "register:40f0:8", ["const:b65778:8", "const:4:8"]]
- 00b65778 ["CALL", null, ["callee:00bde130:8"]]
- 00b65778 bytes 42e20194
- 00b65790 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b65790 ["RETURN", null, ["register:0:8"]]
- 00b65790 bytes c0035fd6
+ 00b65840 ["INT_ADD", "register:40f0:8", ["const:b65840:8", "const:4:8"]]
+ 00b65840 ["CALL", null, ["callee:00bde130:8"]]
+ 00b65840 bytes 3ce20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26c538f017b79d31fe7dcea4cae8a4b9"></a>

### [`00b65f2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65f2c.md) → [`00b65ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65ff4.md) _ZN8firebase4auth10githubcred8GetClassEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b65f34"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b65ffc"
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
      "unmatched:00b65f30",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65ff8",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65f2c.md#insn-00b65f34) · [`00b65f2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65f2c.md#insn-00b65f2c)
- 新版 [`00b65ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65ff4.md#insn-00b65ffc)

~~~diff
- 00b65f34 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b65f34 ["RETURN", null, ["register:0:8"]]
- 00b65f34 bytes c0035fd6
+ 00b65ffc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b65ffc ["RETURN", null, ["register:0:8"]]
+ 00b65ffc bytes c0035fd6
- 00b65f2c ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b65f2c bytes e8290090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8a54072328d1f002d58747c6ad3bd0e"></a>

### [`00b66274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66274.md) → [`00b6633c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6633c.md) _ZN8firebase4auth10googlecred8GetClassEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b6627c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b66344"
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
      "unmatched:00b66278",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66340",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6627c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66274.md#insn-00b6627c) · [`00b66274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66274.md#insn-00b66274)
- 新版 [`00b66344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6633c.md#insn-00b66344)

~~~diff
- 00b6627c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6627c ["RETURN", null, ["register:0:8"]]
- 00b6627c bytes c0035fd6
+ 00b66344 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b66344 ["RETURN", null, ["register:0:8"]]
+ 00b66344 bytes c0035fd6
- 00b66274 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b66274 bytes c82900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2742c4262bcfaa4ecaf466ed8b64fb56"></a>

### [`00b663cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b663cc.md) → [`00b66494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66494.md) _ZN8firebase4auth10googlecred11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b663ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b664b4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66404"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b664a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b663f0"
      ]
    ],
    [
      "unmatched:00b663e8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b663ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b664a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b664b8"
      ]
    ],
    [
      "00b664b0",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b664b4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b663ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b663cc.md#insn-00b663ec) · [`00b66404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b663cc.md#insn-00b66404)
- 新版 [`00b664b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66494.md#insn-00b664b4)

~~~diff
- 00b663ec ["INT_ADD", "register:40f0:8", ["const:b663ec:8", "const:4:8"]]
- 00b663ec ["CALL", null, ["callee:00bde130:8"]]
- 00b663ec bytes 25df0194
- 00b66404 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b66404 ["RETURN", null, ["register:0:8"]]
- 00b66404 bytes c0035fd6
+ 00b664b4 ["INT_ADD", "register:40f0:8", ["const:b664b4:8", "const:4:8"]]
+ 00b664b4 ["CALL", null, ["callee:00bde130:8"]]
+ 00b664b4 bytes 1fdf0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7d650630c9ab848e517056c96a064bf"></a>

### [`00b664b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b664b4.md) → [`00b6657c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6657c.md) _ZN8firebase4auth13playgamescred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00b664e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b665a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b664c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b664c4",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b664c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b665ac"
      ]
    ],
    [
      "unmatched:00b664d4",
      "PARAM",
      [
        "storage",
        "002a2ff4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6658c",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66590",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b665ac"
      ]
    ],
    [
      "00b6659c",
      "PARAM",
      [
        "storage",
        "002a2fed",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b664c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b664b4.md#insn-00b664c8) · [`00b664d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b664b4.md#insn-00b664d8) · [`00b664e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b664b4.md#insn-00b664e0)

~~~diff
- 00b664c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b664c8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b664c8 bytes e80000b5
- 00b664d8 ["INT_ADD", "register:40f0:8", ["const:b664d8:8", "const:4:8"]]
- 00b664d8 ["CALL", null, ["callee:00bde040:8"]]
- 00b664d8 bytes aede0194
- 00b664e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 00b664e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b664e0 bytes 607203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83b41b0a1617bf1f8d8bb41001dd2efb"></a>

### [`00b66714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66714.md) → [`00b667dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b667dc.md) _ZN8firebase4auth13playgamescred11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b66728"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b667f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66734"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b66728",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b66738"
      ]
    ],
    [
      "unmatched:00b66730",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b66734",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b667f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b66800"
      ]
    ],
    [
      "00b667f8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b667fc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66714.md#insn-00b66728) · [`00b66734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66714.md#insn-00b66734) · [`00b6674c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66714.md#insn-00b6674c)

~~~diff
- 00b66728 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b66728 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b66728 bytes 8b000054
- 00b66734 ["INT_ADD", "register:40f0:8", ["const:b66734:8", "const:4:8"]]
- 00b66734 ["CALL", null, ["callee:00bde130:8"]]
- 00b66734 bytes 53de0194
- 00b6674c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6674c ["RETURN", null, ["register:0:8"]]
- 00b6674c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-782dc30a64e8309b70eb34ed4e63fed2"></a>

### [`00b667c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b667c0.md) → [`00b66888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66888.md) _ZN8firebase4auth13playgamescred10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b667e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b668a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b667f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6689c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b667e4"
      ]
    ],
    [
      "unmatched:00b667dc",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b667e0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b6689c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b668ac"
      ]
    ],
    [
      "00b668a4",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b668a8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b667e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b667c0.md#insn-00b667e0) · [`00b667f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b667c0.md#insn-00b667f8)
- 新版 [`00b668a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66888.md#insn-00b668a8)

~~~diff
- 00b667e0 ["INT_ADD", "register:40f0:8", ["const:b667e0:8", "const:4:8"]]
- 00b667e0 ["CALL", null, ["callee:00bde130:8"]]
- 00b667e0 bytes 28de0194
- 00b667f8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b667f8 ["RETURN", null, ["register:0:8"]]
- 00b667f8 bytes c0035fd6
+ 00b668a8 ["INT_ADD", "register:40f0:8", ["const:b668a8:8", "const:4:8"]]
+ 00b668a8 ["CALL", null, ["callee:00bde130:8"]]
+ 00b668a8 bytes 22de0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcf6f5a8fec07fc31cb27896be138a7b"></a>

### [`00b66e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66e50.md) → [`00b66f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66f18.md) _ZN8firebase4auth13oauthprovider10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b66e50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66e54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66e54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b66e50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b66e54",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b66f2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b66e74"
      ]
    ]
  ],
  "added": [
    [
      "00b66f18",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b66f1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b66f2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b66f3c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66e50.md#insn-00b66e50) · [`00b66e54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66e50.md#insn-00b66e54) · [`00b66e70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66e50.md#insn-00b66e70)

~~~diff
- 00b66e50 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b66e50 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b66e50 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b66e50 bytes f30f1ef8
- 00b66e54 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b66e54 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b66e54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b66e54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b66e54 bytes fd7b01a9
- 00b66e70 ["INT_ADD", "register:40f0:8", ["const:b66e70:8", "const:4:8"]]
- 00b66e70 ["CALL", null, ["callee:00bde130:8"]]
- 00b66e70 bytes 84dc0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79e9b9fef9c86296fd36bb0f27e68b27"></a>

### [`00b66fa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66fa0.md) → [`00b67068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67068.md) _ZN8firebase4auth8timeunit15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 16.67% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66ff8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b670c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66fe0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6707c",
      "READ",
      [
        "storage",
        "010a1758",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b66fd4",
      "READ",
      [
        "storage",
        "010a1750",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b66ff8",
      "WRITE",
      [
        "storage",
        "010a1758",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6707c",
      "READ",
      [
        "storage",
        "010a1818",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6709c",
      "READ",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b670c0",
      "WRITE",
      [
        "storage",
        "010a1818",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66fa0.md#insn-00b66fe0) · [`00b66ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66fa0.md#insn-00b66ff8)
- 新版 [`00b670a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67068.md#insn-00b670a8)

~~~diff
- 00b66fe0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b66fe0 ["INT_ADD", "register:40f0:8", ["const:b66fe0:8", "const:4:8"]]
- 00b66fe0 ["CALLIND", null, ["register:0:8"]]
- 00b66fe0 bytes 00013fd6
- 00b66ff8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b66ff8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:758:8"]]
- 00b66ff8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b66ff8 bytes a0621d39
+ 00b670a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b670a8 ["INT_ADD", "register:40f0:8", ["const:b670a8:8", "const:4:8"]]
+ 00b670a8 ["CALLIND", null, ["register:0:8"]]
+ 00b670a8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03fcbf75c59683ca292ab06bb6b68d5f"></a>

### [`00b6700c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6700c.md) → [`00b670d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b670d4.md) _ZN8firebase4auth8timeunit12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67048"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67068"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b67110"
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
      "00b670e8",
      "READ",
      [
        "storage",
        "010a1750",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b67024",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6706c"
      ]
    ],
    [
      "00b670f4",
      "READ",
      [
        "storage",
        "010a1758",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b670e8",
      "READ",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b670ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b67134"
      ]
    ],
    [
      "00b670f4",
      "READ",
      [
        "storage",
        "010a1818",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6700c.md#insn-00b67024) · [`00b67048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6700c.md#insn-00b67048) · [`00b67050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6700c.md#insn-00b67050)

~~~diff
- 00b67024 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b67024 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b67024 bytes 410200b4
- 00b67048 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b67048 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b67048 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:758:8"]]
- 00b67048 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b67048 bytes bf621d39
- 00b67050 ["INT_ADD", "register:40f0:8", ["const:b67050:8", "const:4:8"]]
- 00b67050 ["CALL", null, ["callee:00bde090:8"]]
- 00b67050 bytes e4db0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-345e575960ffd9438f3c74551cb4a39e"></a>

### [`00b670ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b670ec.md) → [`00b671b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b671b4.md) _ZN8firebase4auth8timeunit11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b6710c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b671d4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67124"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b671c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b67110"
      ]
    ],
    [
      "unmatched:00b67108",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6710c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b671c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b671d8"
      ]
    ],
    [
      "00b671d0",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b671d4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6710c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b670ec.md#insn-00b6710c) · [`00b67124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b670ec.md#insn-00b67124)
- 新版 [`00b671d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b671b4.md#insn-00b671d4)

~~~diff
- 00b6710c ["INT_ADD", "register:40f0:8", ["const:b6710c:8", "const:4:8"]]
- 00b6710c ["CALL", null, ["callee:00bde130:8"]]
- 00b6710c bytes dddb0194
- 00b67124 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b67124 ["RETURN", null, ["register:0:8"]]
- 00b67124 bytes c0035fd6
+ 00b671d4 ["INT_ADD", "register:40f0:8", ["const:b671d4:8", "const:4:8"]]
+ 00b671d4 ["CALL", null, ["callee:00bde130:8"]]
+ 00b671d4 bytes d7db0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f95e21c6abebb7b209cdabfbe4a214c"></a>

### [`00b671d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b671d4.md) → [`00b6729c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6729c.md) _ZN8firebase4auth26phone_auth_options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 31.25% / 新版 31.25%

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
      "site": "00b671d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b671d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b671d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b671d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b671d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b671e4",
      "READ",
      [
        "storage",
        "010a1770",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6729c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b672a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b672ac",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b671d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b671d4.md#insn-00b671d4) · [`00b671d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b671d4.md#insn-00b671d8) · [`00b671e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b671d4.md#insn-00b671e8)

~~~diff
- 00b671d4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b671d4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b671d4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b671d4 bytes f30f1ef8
- 00b671d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b671d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b671d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b671d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b671d8 bytes fd7b01a9
- 00b671e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b671e8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b671e8 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d54f24b6b95c9dd27274929fbc12fae"></a>

### [`00b672dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b672dc.md) → [`00b673a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b673a4.md) _ZN8firebase4auth26phone_auth_options_builder8GetClassEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b672e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b673ac"
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
      "unmatched:00b672e0",
      "READ",
      [
        "storage",
        "010a1770",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b673a8",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b672e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b672dc.md#insn-00b672e4) · [`00b672dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b672dc.md#insn-00b672dc)
- 新版 [`00b673ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b673a4.md#insn-00b673ac)

~~~diff
- 00b672e4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b672e4 ["RETURN", null, ["register:0:8"]]
- 00b672e4 bytes c0035fd6
+ 00b673ac ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b673ac ["RETURN", null, ["register:0:8"]]
+ 00b673ac bytes c0035fd6
- 00b672dc ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b672dc bytes c82900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e51b2e2a62026f9b4bc385d7ea1b1d2f"></a>

### [`00b6b8ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b8ac.md) → [`00b6b974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b974.md) _ZN8firebase4auth20JniAuthPhoneListener26nativeOnVerificationFailedEP7_JNIEnvP8_jobjectlP8_jstring

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddfa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfa0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 66.67% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b918"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b6b9e0"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b8ac.md#insn-00b6b918) · [`00b6b8d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b8ac.md#insn-00b6b8d4)
- 新版 [`00b6b9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b974.md#insn-00b6b9e0) · [`00b6b99c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b974.md#insn-00b6b99c)

~~~diff
- 00b6b918 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6b918 ["RETURN", null, ["register:0:8"]]
- 00b6b918 bytes c0035fd6
+ 00b6b9e0 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b6b9e0 ["RETURN", null, ["register:0:8"]]
+ 00b6b9e0 bytes c0035fd6
- 00b6b8d4 ["INT_ADD", "register:40f0:8", ["const:b6b8d4:8", "const:4:8"]]
- 00b6b8d4 ["CALL", null, ["callee:00bde050:8"]]
+ 00b6b99c ["INT_ADD", "register:40f0:8", ["const:b6b99c:8", "const:4:8"]]
+ 00b6b99c ["CALL", null, ["callee:00bde050:8"]]
- 00b6b8d4 bytes b3c90194
+ 00b6b99c bytes adc90194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6425b5871f118e5d25922731dc172a1e"></a>

### [`00b6babc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6babc.md) → [`00b6bb84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bb84.md) _ZN8firebase4auth20JniAuthPhoneListener32nativeOnCodeAutoRetrievalTimeOutEP7_JNIEnvP8_jobjectlP8_jstring

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde410.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4c0.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 75.86% / 新版 75.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6bb18"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6bbe0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6baf8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6bb18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6bbf4"
      ]
    ],
    [
      "unmatched:00b6bb1c",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6bb20",
      "READ",
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
      "00b6bbe0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6bbf4"
      ]
    ],
    [
      "00b6bbe4",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b6bbe8",
      "READ",
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

- 旧版 [`00b6baf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6babc.md#insn-00b6baf8) · [`00b6bb18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6babc.md#insn-00b6bb18) · [`00b6bb28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6babc.md#insn-00b6bb28)

~~~diff
- 00b6baf8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6baf8 ["INT_ADD", "register:40f0:8", ["const:b6baf8:8", "const:4:8"]]
- 00b6baf8 ["CALLIND", null, ["register:0:8"]]
- 00b6baf8 bytes 00013fd6
- 00b6bb18 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b6bb18 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b6bb18 bytes a1000054
- 00b6bb28 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6bb28 ["RETURN", null, ["register:0:8"]]
- 00b6bb28 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4bc2659313f17d0e76d5efc0f14c1c6"></a>

### [`00b6bb4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bb4c.md) → [`00b6bc14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bc14.md) _ZN8firebase4auth22FederatedOAuthProviderC2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

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
      "site": "00b6bb64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6bc2c"
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
      "00b6bc18",
      "READ",
      [
        "storage",
        "00c1bb18",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b6bb64",
      "DATA",
      [
        "storage",
        "00c126d8",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00b6bc18",
      "READ",
      [
        "storage",
        "00c1bbc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b6bc2c",
      "DATA",
      [
        "storage",
        "00c12788",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6bb64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bb4c.md#insn-00b6bb64) · [`00b6bb50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bb4c.md#insn-00b6bb50)
- 新版 [`00b6bc2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bc14.md#insn-00b6bc2c) · [`00b6bc18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bc14.md#insn-00b6bc18)

~~~diff
- 00b6bb64 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b6bb64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b6bb64 bytes 080000f9
+ 00b6bc2c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00b6bc2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b6bc2c bytes 080000f9
- 00b6bb50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b18:8"]]
- 00b6bb50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6bc18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bc8:8"]]
+ 00b6bc18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6bb50 bytes 088d45f9
+ 00b6bc18 bytes 08e545f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bc3b12a0327b294d09be5b285790fab"></a>

### [`00b6bdf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bdf4.md) → [`00b6bebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bebc.md) _ZN8firebase4auth22FederatedOAuthProvider15SetProviderDataERKNS0_26FederatedOAuthProviderDataE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`005188a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/005188a4.md) [`00bde130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde130.md) [`00bdff90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdff90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005188a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/005188a4.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00be0040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0040.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6be0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6be24"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6be28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6be0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6bf1c"
      ]
    ]
  ],
  "added": [
    [
      "00b6bed4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6bf1c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6be0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bdf4.md#insn-00b6be0c) · [`00b6be24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bdf4.md#insn-00b6be24) · [`00b6be28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bdf4.md#insn-00b6be28)

~~~diff
- 00b6be0c ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00b6be0c bytes 40020054
- 00b6be24 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b6be24 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b6be24 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b6be24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b6be24 bytes 2115819a
- 00b6be28 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b6be28 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b6be28 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b6be28 ["COPY", "register:4010:8", ["tmp:0:8"]]
- 00b6be28 bytes 62018a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be14c10ce39592627bffa515736a3f10"></a>

### [`00b6d4ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d4ec.md) → [`00b6d5b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d5b4.md) _ZN8firebase4auth11tokenresult8GetClassEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00b6d4f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b6d5bc"
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
      "unmatched:00b6d4f0",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d5b8",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d4f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d4ec.md#insn-00b6d4f4) · [`00b6d4ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d4ec.md#insn-00b6d4ec)
- 新版 [`00b6d5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d5b4.md#insn-00b6d5bc)

~~~diff
- 00b6d4f4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6d4f4 ["RETURN", null, ["register:0:8"]]
- 00b6d4f4 bytes c0035fd6
+ 00b6d5bc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b6d5bc ["RETURN", null, ["register:0:8"]]
+ 00b6d5bc bytes c0035fd6
- 00b6d4ec ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b6d4ec bytes a8290090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44ad49bbc1f7df7656ee33ee9b4afd11"></a>

### [`00b6d644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d644.md) → [`00b6d70c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d70c.md) _ZN8firebase4auth11tokenresult11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b6d644"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d648"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d648"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6d644",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6d648",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b6d720",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6d668"
      ]
    ]
  ],
  "added": [
    [
      "00b6d70c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6d710",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b6d720",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d730"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d644.md#insn-00b6d644) · [`00b6d648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d644.md#insn-00b6d648) · [`00b6d664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d644.md#insn-00b6d664)

~~~diff
- 00b6d644 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b6d644 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b6d644 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6d644 bytes f30f1ef8
- 00b6d648 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6d648 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6d648 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6d648 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6d648 bytes fd7b01a9
- 00b6d664 ["INT_ADD", "register:40f0:8", ["const:b6d664:8", "const:4:8"]]
- 00b6d664 ["CALL", null, ["callee:00bde130:8"]]
- 00b6d664 bytes 87c20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c29523453cad66ec4f6678baa0861db"></a>

### [`00b6d8ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d8ac.md) → [`00b6d974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d974.md) _ZN8firebase4auth4user12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 60.71% / 新版 60.71%

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
      "site": "00b6d8e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d908"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6d9b0"
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
      "unmatched:00b6d8c0",
      "READ",
      [
        "storage",
        "010a1918",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6d8c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d9d4"
      ]
    ],
    [
      "00b6d994",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6d988",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d98c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d9d4"
      ]
    ],
    [
      "00b6d994",
      "READ",
      [
        "storage",
        "010a19e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d8ac.md#insn-00b6d8c4) · [`00b6d8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d8ac.md#insn-00b6d8e8) · [`00b6d8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d8ac.md#insn-00b6d8f0)

~~~diff
- 00b6d8c4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6d8c4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b6d8c4 bytes 410200b4
- 00b6d8e8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6d8e8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6d8e8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:920:8"]]
- 00b6d8e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6d8e8 bytes bf822439
- 00b6d8f0 ["INT_ADD", "register:40f0:8", ["const:b6d8f0:8", "const:4:8"]]
- 00b6d8f0 ["CALL", null, ["callee:00bde090:8"]]
- 00b6d8f0 bytes bcc10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d808737b8e018f9f37372dc2ae9305a3"></a>

### [`00b6d98c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d98c.md) → [`00b6da54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6da54.md) _ZN8firebase4auth4user11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b6d98c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d990"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d990"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6d98c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6d990",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b6da68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6d9b0"
      ]
    ]
  ],
  "added": [
    [
      "00b6da54",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6da58",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b6da68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6da78"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d98c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d98c.md#insn-00b6d98c) · [`00b6d990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d98c.md#insn-00b6d990) · [`00b6d9ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d98c.md#insn-00b6d9ac)

~~~diff
- 00b6d98c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b6d98c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b6d98c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6d98c bytes f30f1ef8
- 00b6d990 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6d990 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6d990 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6d990 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6d990 bytes fd7b01a9
- 00b6d9ac ["INT_ADD", "register:40f0:8", ["const:b6d9ac:8", "const:4:8"]]
- 00b6d9ac ["CALL", null, ["callee:00bde130:8"]]
- 00b6d9ac bytes b5c10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a7d0fda1e1b7d073a6429011bdaa588"></a>

### [`00b6da38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6da38.md) → [`00b6db00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6db00.md) _ZN8firebase4auth4user10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b6da58"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b6db20"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6da70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6db14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6da5c"
      ]
    ],
    [
      "unmatched:00b6da54",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6da58",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b6db14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6db24"
      ]
    ],
    [
      "00b6db1c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b6db20",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6da58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6da38.md#insn-00b6da58) · [`00b6da70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6da38.md#insn-00b6da70)
- 新版 [`00b6db20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6db00.md#insn-00b6db20)

~~~diff
- 00b6da58 ["INT_ADD", "register:40f0:8", ["const:b6da58:8", "const:4:8"]]
- 00b6da58 ["CALL", null, ["callee:00bde130:8"]]
- 00b6da58 bytes 8ac10194
- 00b6da70 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6da70 ["RETURN", null, ["register:0:8"]]
- 00b6da70 bytes c0035fd6
+ 00b6db20 ["INT_ADD", "register:40f0:8", ["const:b6db20:8", "const:4:8"]]
+ 00b6db20 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6db20 bytes 84c10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dbcaf88b06475a53758d1de363cf286"></a>

### [`00b6da74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6da74.md) → [`00b6db3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6db3c.md) _ZN8firebase4auth8userinfo19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00b6daa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6db68"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6da88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6db4c",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6da88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6daa4"
      ]
    ],
    [
      "unmatched:00b6da94",
      "PARAM",
      [
        "storage",
        "002a0fd8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6db4c",
      "READ",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6db50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6db6c"
      ]
    ],
    [
      "00b6db5c",
      "PARAM",
      [
        "storage",
        "002a1065",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6da88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6da74.md#insn-00b6da88) · [`00b6da98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6da74.md#insn-00b6da98) · [`00b6daa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6da74.md#insn-00b6daa0)

~~~diff
- 00b6da88 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6da88 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b6da88 bytes e80000b5
- 00b6da98 ["INT_ADD", "register:40f0:8", ["const:b6da98:8", "const:4:8"]]
- 00b6da98 ["CALL", null, ["callee:00bde040:8"]]
- 00b6da98 bytes 3ec10194
- 00b6daa0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b6daa0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6daa0 bytes 60d604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45aca1877460bcede07384d657dab3a2"></a>

### [`00b6db88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6db88.md) → [`00b6dc50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dc50.md) _ZN8firebase4auth8userinfo15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 33.33% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6dbe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6dca8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6dbc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6dc64",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b6dbbc",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6dbe0",
      "WRITE",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6dc64",
      "READ",
      [
        "storage",
        "010a1a70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6dc84",
      "READ",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dca8",
      "WRITE",
      [
        "storage",
        "010a1a70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dbc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6db88.md#insn-00b6dbc8) · [`00b6dbe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6db88.md#insn-00b6dbe0)
- 新版 [`00b6dc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dc50.md#insn-00b6dc90)

~~~diff
- 00b6dbc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6dbc8 ["INT_ADD", "register:40f0:8", ["const:b6dbc8:8", "const:4:8"]]
- 00b6dbc8 ["CALLIND", null, ["register:0:8"]]
- 00b6dbc8 bytes 00013fd6
- 00b6dbe0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6dbe0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9b0:8"]]
- 00b6dbe0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6dbe0 bytes a0c22639
+ 00b6dc90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6dc90 ["INT_ADD", "register:40f0:8", ["const:b6dc90:8", "const:4:8"]]
+ 00b6dc90 ["CALLIND", null, ["register:0:8"]]
+ 00b6dc90 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0604e80e9133b2f66f5b0fe77fdb8dcd"></a>

### [`00b6dcd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dcd4.md) → [`00b6dd9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dd9c.md) _ZN8firebase4auth8userinfo11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b6dcf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b6ddbc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6dd0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6ddb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6dcf8"
      ]
    ],
    [
      "unmatched:00b6dcf0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6dcf4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b6ddb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ddc0"
      ]
    ],
    [
      "00b6ddb8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b6ddbc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dcf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dcd4.md#insn-00b6dcf4) · [`00b6dd0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dcd4.md#insn-00b6dd0c)
- 新版 [`00b6ddbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dd9c.md#insn-00b6ddbc)

~~~diff
- 00b6dcf4 ["INT_ADD", "register:40f0:8", ["const:b6dcf4:8", "const:4:8"]]
- 00b6dcf4 ["CALL", null, ["callee:00bde130:8"]]
- 00b6dcf4 bytes e3c00194
- 00b6dd0c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6dd0c ["RETURN", null, ["register:0:8"]]
- 00b6dd0c bytes c0035fd6
+ 00b6ddbc ["INT_ADD", "register:40f0:8", ["const:b6ddbc:8", "const:4:8"]]
+ 00b6ddbc ["CALL", null, ["callee:00bde130:8"]]
+ 00b6ddbc bytes ddc00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b28dccd4af66e4afd9f3b1dc96ea80fe"></a>

### [`00b6dd80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dd80.md) → [`00b6de48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6de48.md) _ZN8firebase4auth8userinfo10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b6dda0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b6de68"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ddb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6de5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6dda4"
      ]
    ],
    [
      "unmatched:00b6dd9c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6dda0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b6de5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6de6c"
      ]
    ],
    [
      "00b6de64",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b6de68",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dda0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dd80.md#insn-00b6dda0) · [`00b6ddb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dd80.md#insn-00b6ddb8)
- 新版 [`00b6de68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6de48.md#insn-00b6de68)

~~~diff
- 00b6dda0 ["INT_ADD", "register:40f0:8", ["const:b6dda0:8", "const:4:8"]]
- 00b6dda0 ["CALL", null, ["callee:00bde130:8"]]
- 00b6dda0 bytes b8c00194
- 00b6ddb8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6ddb8 ["RETURN", null, ["register:0:8"]]
- 00b6ddb8 bytes c0035fd6
+ 00b6de68 ["INT_ADD", "register:40f0:8", ["const:b6de68:8", "const:4:8"]]
+ 00b6de68 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6de68 bytes b2c00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16c2241858574eb59776cd26fd024b2f"></a>

### [`00b6e0c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e0c8.md) → [`00b6e190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e190.md) _ZN8firebase4auth8metadata10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "site": "00b6e0e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b6e1b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e100"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6e1a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6e0ec"
      ]
    ],
    [
      "unmatched:00b6e0e4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6e0e8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00b6e1a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e1b4"
      ]
    ],
    [
      "00b6e1ac",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b6e1b0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e0e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e0c8.md#insn-00b6e0e8) · [`00b6e100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e0c8.md#insn-00b6e100)
- 新版 [`00b6e1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e190.md#insn-00b6e1b0)

~~~diff
- 00b6e0e8 ["INT_ADD", "register:40f0:8", ["const:b6e0e8:8", "const:4:8"]]
- 00b6e0e8 ["CALL", null, ["callee:00bde130:8"]]
- 00b6e0e8 bytes e6bf0194
- 00b6e100 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6e100 ["RETURN", null, ["register:0:8"]]
- 00b6e100 bytes c0035fd6
+ 00b6e1b0 ["INT_ADD", "register:40f0:8", ["const:b6e1b0:8", "const:4:8"]]
+ 00b6e1b0 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6e1b0 bytes e0bf0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ddd21b9bbfa6ffc2728cea3f1e48c89"></a>

### [`00b6f044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6f044.md) → [`00b6f10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6f10c.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEbP7_JNIEnvPNS_26Refere

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0db0.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md) [`00be0c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c10.md)
- 新版 呼出元 1件 [`00be0e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e60.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0cc0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 25.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6f0a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6f0e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6f16c"
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
      "unmatched:00b6f0e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6f1d8"
      ]
    ]
  ],
  "added": [
    [
      "00b6f1ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6f1d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6f0a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6f044.md#insn-00b6f0a4) · [`00b6f0e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6f044.md#insn-00b6f0e4) · [`00b6f0fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6f044.md#insn-00b6f0fc)

~~~diff
- 00b6f0a4 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b6f0a4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b6f0a4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b6f0a4 ["COPY", "register:4018:8", ["tmp:0:8"]]
- 00b6f0a4 bytes 4301899a
- 00b6f0e4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b6f0e4 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b6f0e4 bytes 61010054
- 00b6f0fc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6f0fc ["RETURN", null, ["register:0:8"]]
- 00b6f0fc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22f61c868be8c216533afb05e47ff807"></a>

### [`00b720e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b720e4.md) → [`00b721ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b721ac.md) _ZNK8firebase4auth4User39ReauthenticateAndRetrieveDataLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b720e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b720e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b720e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b720e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b720e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b720ec",
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
      "00b721ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b721b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b721b4",
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

- 旧版 [`00b720e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b720e4.md#insn-00b720e4) · [`00b720e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b720e4.md#insn-00b720e8) · [`00b720ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b720e4.md#insn-00b720ec)

~~~diff
- 00b720e4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b720e4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b720e4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b720e4 bytes f50f1df8
- 00b720e8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b720e8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b720e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b720e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b720e8 bytes f44f01a9
- 00b720ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b720ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b720ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b720ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b720ec bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe4f2a6f215b5fac7714350143371f68"></a>

### [`00b72818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72818.md) → [`00b728e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b728e0.md) _ZNSt6__ndk16chrono12system_clock3nowEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb630.md) · 呼出先 3件 [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00bdb1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1d0.md) [`00bdc7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc7b0.md)
- 新版 呼出元 1件 [`00bdb6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb6e0.md) · 呼出先 3件 [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bdc860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc860.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 79.31% / 新版 79.31%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72878"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72888"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b72940"
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
      "00b728fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b72878"
      ]
    ],
    [
      "unmatched:00b72878",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb220"
      ]
    ],
    [
      "unmatched:00b72884",
      "PARAM",
      [
        "storage",
        "002a40ac",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b728fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72940"
      ]
    ],
    [
      "00b72940",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb220"
      ]
    ],
    [
      "00b7294c",
      "PARAM",
      [
        "storage",
        "002a40a5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72874`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72818.md#insn-00b72874) · [`00b72878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72818.md#insn-00b72878) · [`00b72888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72818.md#insn-00b72888)

~~~diff
- 00b72874 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b72874 ["RETURN", null, ["register:0:8"]]
- 00b72874 bytes c0035fd6
- 00b72878 ["INT_ADD", "register:40f0:8", ["const:b72878:8", "const:4:8"]]
- 00b72878 ["CALL", null, ["callee:00bdb220:8"]]
- 00b72878 bytes 3ea20194
- 00b72888 ["INT_ADD", "register:40f0:8", ["const:b72888:8", "const:4:8"]]
- 00b72888 ["CALL", null, ["callee:00bdb280:8"]]
- 00b72888 bytes 52a20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

