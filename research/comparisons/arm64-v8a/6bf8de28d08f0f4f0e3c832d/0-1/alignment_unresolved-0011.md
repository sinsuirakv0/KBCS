# v16.0.0 → v16.0.1 · 命令位置の検査未完了 (11)

[一覧の目次](README.md)

<a id="compare-efc85bff0b743db216800df9d987b97e"></a>

### [`00bd291c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd291c.md) → [`00bd2d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2d44.md) _ZN8firebase4auth23firebase_auth_exception11GetMethodIdENS1_6MethodE

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
      "site": "00bd291c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2920"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2920"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd291c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd2920",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd2d58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd2940"
      ]
    ]
  ],
  "added": [
    [
      "00bd2d44",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd2d48",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd2d58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd2d68"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd291c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd291c.md#insn-00bd291c) · [`00bd2920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd291c.md#insn-00bd2920) · [`00bd293c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd291c.md#insn-00bd293c)

~~~diff
- 00bd291c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd291c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd291c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd291c bytes f30f1ef8
- 00bd2920 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd2920 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd2920 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd2920 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd2920 bytes fd7b01a9
- 00bd293c ["INT_ADD", "register:40f0:8", ["const:bd293c:8", "const:4:8"]]
- 00bd293c ["CALL", null, ["callee:00c5b000:8"]]
- 00bd293c bytes b1200294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8326899d26d12274c462b2e2d63ec09c"></a>

### [`00bd29c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd29c8.md) → [`00bd2df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2df0.md) _ZN8firebase4auth23firebase_auth_exception10GetFieldIdENS1_5FieldE

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
      "site": "00bd29e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd2e10"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2a00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd2e04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd29ec"
      ]
    ],
    [
      "unmatched:00bd29e4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd29e8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd2e04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd2e14"
      ]
    ],
    [
      "00bd2e0c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd2e10",
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

- 旧版 [`00bd29e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd29c8.md#insn-00bd29e8) · [`00bd2a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd29c8.md#insn-00bd2a00)
- 新版 [`00bd2e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2df0.md#insn-00bd2e10)

~~~diff
- 00bd29e8 ["INT_ADD", "register:40f0:8", ["const:bd29e8:8", "const:4:8"]]
- 00bd29e8 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd29e8 bytes 86200294
- 00bd2a00 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd2a00 ["RETURN", null, ["register:0:8"]]
- 00bd2a00 bytes c0035fd6
+ 00bd2e10 ["INT_ADD", "register:40f0:8", ["const:bd2e10:8", "const:4:8"]]
+ 00bd2e10 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd2e10 bytes 7c200294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e10eea790e92ae650f3842c6426e66b5"></a>

### [`00bd3114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3114.md) → [`00bd353c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd353c.md) _ZN8firebase4auth18firebase_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "site": "00bd3144"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd356c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3128"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd3124",
      "READ",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd3128",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd3570"
      ]
    ],
    [
      "unmatched:00bd3134",
      "PARAM",
      [
        "storage",
        "002a2c6a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd354c",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3550",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd3570"
      ]
    ],
    [
      "00bd355c",
      "PARAM",
      [
        "storage",
        "002a2d37",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd3128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3114.md#insn-00bd3128) · [`00bd313c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3114.md#insn-00bd313c) · [`00bd3144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3114.md#insn-00bd3144)

~~~diff
- 00bd3128 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd3128 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd3128 bytes 080100b5
- 00bd313c ["INT_ADD", "register:40f0:8", ["const:bd313c:8", "const:4:8"]]
- 00bd313c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd313c bytes 751e0294
- 00bd3144 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
- 00bd3144 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd3144 bytes 601603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76c4d8bdf4ae1e58d8f5046fa2ac8960"></a>

### [`00bd4250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4250.md) → [`00bd4678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4678.md) _ZN8firebase4auth30CheckAndClearJniAuthExceptionsEP7_JNIEnvPNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d910.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ab50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab50.md) [`00c5d980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d980.md)
- 新版 呼出元 1件 [`00c5dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd10.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5af50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af50.md) [`00c5dd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 44.44% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4254"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4258"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4258"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd4254",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd4258",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd4278",
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
      "00bd467c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bd4680",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd46a0",
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

- 旧版 [`00bd4254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4250.md#insn-00bd4254) · [`00bd4258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4250.md#insn-00bd4258) · [`00bd4278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4250.md#insn-00bd4278)

~~~diff
- 00bd4254 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00bd4254 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00bd4254 bytes f71300f9
- 00bd4258 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bd4258 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bd4258 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bd4258 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd4258 bytes f65703a9
- 00bd4278 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00bd4278 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bd4278 bytes e80f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a89bf8038dcf622cf0dd7e61fc353a82"></a>

### [`00bd4388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4388.md) → [`00bd47b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd47b0.md) _ZN8firebase4auth19SetImplFromLocalRefEP7_JNIEnvP8_jobjectPPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d880.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5dc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dc80.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.10% / 新版 87.10%

CFGの説明率　旧版 50.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4388"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4388"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd438c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd4388",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd438c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd4390",
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
      "00bd47b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd47b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd47b8",
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

- 旧版 [`00bd4388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4388.md#insn-00bd4388) · [`00bd438c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4388.md#insn-00bd438c) · [`00bd4390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4388.md#insn-00bd4390)

~~~diff
- 00bd4388 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bd4388 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bd4388 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd4388 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd4388 bytes f657bda9
- 00bd438c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd438c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd438c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd438c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd438c bytes f44f01a9
- 00bd4390 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd4390 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd4390 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd4390 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd4390 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a089a9911df2d82b71b8f2584457cfc4"></a>

### [`00bd4e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4e20.md) → [`00bd5248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5248.md) _ZN8firebase4auth9emailcred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "site": "00bd4e50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5278"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4e34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd4e30",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd4e34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd4e54"
      ]
    ],
    [
      "unmatched:00bd4e40",
      "PARAM",
      [
        "storage",
        "002ac3b3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd5258",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd525c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd527c"
      ]
    ],
    [
      "00bd5268",
      "PARAM",
      [
        "storage",
        "002ac3f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4e20.md#insn-00bd4e34) · [`00bd4e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4e20.md#insn-00bd4e48) · [`00bd4e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4e20.md#insn-00bd4e50)

~~~diff
- 00bd4e34 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd4e34 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd4e34 bytes 080100b5
- 00bd4e48 ["INT_ADD", "register:40f0:8", ["const:bd4e48:8", "const:4:8"]]
- 00bd4e48 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd4e48 bytes 32170294
- 00bd4e50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
- 00bd4e50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd4e50 bytes 603603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-013da31840355501e061b6cc6ae38ca2"></a>

### [`00bd5000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5000.md) → [`00bd5428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5428.md) _ZN8firebase4auth9emailcred11GetMethodIdENS1_6MethodE

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
      "site": "00bd5000"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5004"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5004"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd5000",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5004",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd543c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd5024"
      ]
    ]
  ],
  "added": [
    [
      "00bd5428",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd542c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd543c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd544c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5000.md#insn-00bd5000) · [`00bd5004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5000.md#insn-00bd5004) · [`00bd5020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5000.md#insn-00bd5020)

~~~diff
- 00bd5000 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd5000 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd5000 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd5000 bytes f30f1ef8
- 00bd5004 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd5004 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd5004 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd5004 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd5004 bytes fd7b01a9
- 00bd5020 ["INT_ADD", "register:40f0:8", ["const:bd5020:8", "const:4:8"]]
- 00bd5020 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd5020 bytes f8160294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c769131689bb782678a92bfee5649fe8"></a>

### [`00bd50ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd50ac.md) → [`00bd54d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd54d4.md) _ZN8firebase4auth9emailcred10GetFieldIdENS1_5FieldE

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
      "site": "00bd50c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd54e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd50cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd50c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd50d0"
      ]
    ],
    [
      "unmatched:00bd50c8",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd50cc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd54e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd54f8"
      ]
    ],
    [
      "00bd54f0",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd54f4",
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

- 旧版 [`00bd50c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd50ac.md#insn-00bd50c0) · [`00bd50cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd50ac.md#insn-00bd50cc) · [`00bd50e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd50ac.md#insn-00bd50e4)

~~~diff
- 00bd50c0 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd50c0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd50c0 bytes 8b000054
- 00bd50cc ["INT_ADD", "register:40f0:8", ["const:bd50cc:8", "const:4:8"]]
- 00bd50cc ["CALL", null, ["callee:00c5b000:8"]]
- 00bd50cc bytes cd160294
- 00bd50e4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd50e4 ["RETURN", null, ["register:0:8"]]
- 00bd50e4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6694db4a524bb2ff03be231cc023e7b3"></a>

### [`00bd5128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5128.md) → [`00bd5550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5550.md) _ZN8firebase4auth12facebookcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

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
      "site": "00bd5128"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd512c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd512c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd5128",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd512c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5138",
      "READ",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5550",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd5554",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd5560",
      "READ",
      [
        "storage",
        "01126a88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5128.md#insn-00bd5128) · [`00bd512c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5128.md#insn-00bd512c) · [`00bd513c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5128.md#insn-00bd513c)

~~~diff
- 00bd5128 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd5128 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd5128 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd5128 bytes f30f1ef8
- 00bd512c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd512c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd512c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd512c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd512c bytes fd7b01a9
- 00bd513c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd513c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd513c bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e16f09572cf28fbcb23f25f473a6f209"></a>

### [`00bd5168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5168.md) → [`00bd5590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5590.md) _ZN8firebase4auth12facebookcred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "site": "00bd5198"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd55c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd517c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd5178",
      "READ",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd517c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd519c"
      ]
    ],
    [
      "unmatched:00bd5188",
      "PARAM",
      [
        "storage",
        "002bd459",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd55a0",
      "READ",
      [
        "storage",
        "01126a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd55a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd55c4"
      ]
    ],
    [
      "00bd55b0",
      "PARAM",
      [
        "storage",
        "002bd499",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd517c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5168.md#insn-00bd517c) · [`00bd5190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5168.md#insn-00bd5190) · [`00bd5198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5168.md#insn-00bd5198)

~~~diff
- 00bd517c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd517c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd517c bytes 080100b5
- 00bd5190 ["INT_ADD", "register:40f0:8", ["const:bd5190:8", "const:4:8"]]
- 00bd5190 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd5190 bytes 60160294
- 00bd5198 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:688:8"]]
- 00bd5198 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd5198 bytes 604603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f8079f000c9154494e67480741715ba"></a>

### [`00bd51f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd51f0.md) → [`00bd5618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5618.md) _ZN8firebase4auth12facebookcred8GetClassEv

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
      "site": "00bd51f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bd5620"
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
      "unmatched:00bd51f4",
      "READ",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd561c",
      "READ",
      [
        "storage",
        "01126a88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd51f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd51f0.md#insn-00bd51f8) · [`00bd51f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd51f0.md#insn-00bd51f0)
- 新版 [`00bd5620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5618.md#insn-00bd5620)

~~~diff
- 00bd51f8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd51f8 ["RETURN", null, ["register:0:8"]]
- 00bd51f8 bytes c0035fd6
+ 00bd5620 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bd5620 ["RETURN", null, ["register:0:8"]]
+ 00bd5620 bytes c0035fd6
- 00bd51f0 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd51f0 bytes 882a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6a3e601ba1d27dce11ef5600d53e763"></a>

### [`00bd5348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5348.md) → [`00bd5770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5770.md) _ZN8firebase4auth12facebookcred11GetMethodIdENS1_6MethodE

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
      "site": "00bd535c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd5784"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5368"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd535c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd536c"
      ]
    ],
    [
      "unmatched:00bd5364",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd5368",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd5784",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5794"
      ]
    ],
    [
      "00bd578c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd5790",
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

- 旧版 [`00bd535c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5348.md#insn-00bd535c) · [`00bd5368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5348.md#insn-00bd5368) · [`00bd5380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5348.md#insn-00bd5380)

~~~diff
- 00bd535c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd535c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd535c bytes 8b000054
- 00bd5368 ["INT_ADD", "register:40f0:8", ["const:bd5368:8", "const:4:8"]]
- 00bd5368 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd5368 bytes 26160294
- 00bd5380 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd5380 ["RETURN", null, ["register:0:8"]]
- 00bd5380 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2462d3a130caa74288cdbc0acbb066a3"></a>

### [`00bd53f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd53f4.md) → [`00bd581c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd581c.md) _ZN8firebase4auth12facebookcred10GetFieldIdENS1_5FieldE

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
      "site": "00bd5414"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd583c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd542c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd5830",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd5418"
      ]
    ],
    [
      "unmatched:00bd5410",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd5414",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd5830",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5840"
      ]
    ],
    [
      "00bd5838",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd583c",
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

- 旧版 [`00bd5414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd53f4.md#insn-00bd5414) · [`00bd542c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd53f4.md#insn-00bd542c)
- 新版 [`00bd583c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd581c.md#insn-00bd583c)

~~~diff
- 00bd5414 ["INT_ADD", "register:40f0:8", ["const:bd5414:8", "const:4:8"]]
- 00bd5414 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd5414 bytes fb150294
- 00bd542c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd542c ["RETURN", null, ["register:0:8"]]
- 00bd542c bytes c0035fd6
+ 00bd583c ["INT_ADD", "register:40f0:8", ["const:bd583c:8", "const:4:8"]]
+ 00bd583c ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd583c bytes f1150294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07dcb14ab80aa8ce7dbbfe4a758b872d"></a>

### [`00bd5430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5430.md) → [`00bd5858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5858.md) _ZN8firebase4auth10githubcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
      "site": "00bd5430"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5434"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5434"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd5430",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5434",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5440",
      "READ",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5858",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd585c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd5868",
      "READ",
      [
        "storage",
        "01126aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5430.md#insn-00bd5430) · [`00bd5434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5430.md#insn-00bd5434) · [`00bd5444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5430.md#insn-00bd5444)

~~~diff
- 00bd5430 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd5430 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd5430 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd5430 bytes f30f1ef8
- 00bd5434 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd5434 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd5434 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd5434 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd5434 bytes fd7b01a9
- 00bd5444 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd5444 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bd5444 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2113bdb833796c38409fbcfe1e0eeb4"></a>

### [`00bd54b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd54b0.md) → [`00bd58d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd58d8.md) _ZN8firebase4auth10githubcred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "site": "00bd54e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5908"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd54c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd54c0",
      "READ",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd54c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd590c"
      ]
    ],
    [
      "unmatched:00bd54d0",
      "PARAM",
      [
        "storage",
        "002c1da2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd58e8",
      "READ",
      [
        "storage",
        "01126aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd58ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd590c"
      ]
    ],
    [
      "00bd58f8",
      "PARAM",
      [
        "storage",
        "002c1de2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd54c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd54b0.md#insn-00bd54c4) · [`00bd54d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd54b0.md#insn-00bd54d8) · [`00bd54e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd54b0.md#insn-00bd54e0)

~~~diff
- 00bd54c4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd54c4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd54c4 bytes 080100b5
- 00bd54d8 ["INT_ADD", "register:40f0:8", ["const:bd54d8:8", "const:4:8"]]
- 00bd54d8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd54d8 bytes 8e150294
- 00bd54e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00bd54e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd54e0 bytes 605603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea778bec06830176b033c20668c47ea0"></a>

### [`00bd5544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5544.md) → [`00bd596c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd596c.md) _ZN8firebase4auth10githubcred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.07% / 新版 74.07%

CFGの説明率　旧版 16.67% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5544"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5548"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5548"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd5544",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5548",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd5980",
      "READ",
      [
        "storage",
        "011266b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd596c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd5970",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd5980",
      "READ",
      [
        "storage",
        "01126ab0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5544.md#insn-00bd5544) · [`00bd5548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5544.md#insn-00bd5548) · [`00bd5584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5544.md#insn-00bd5584)

~~~diff
- 00bd5544 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bd5544 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd5544 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd5544 bytes f50f1df8
- 00bd5548 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd5548 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd5548 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd5548 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd5548 bytes f44f01a9
- 00bd5584 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd5584 ["INT_ADD", "register:40f0:8", ["const:bd5584:8", "const:4:8"]]
- 00bd5584 ["CALLIND", null, ["register:0:8"]]
- 00bd5584 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-758bccff4ab27b1168f3b7b8038ae0e7"></a>

### [`00bd5690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5690.md) → [`00bd5ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5ab8.md) _ZN8firebase4auth10githubcred11GetMethodIdENS1_6MethodE

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
      "site": "00bd56b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd5ad8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd56c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd5acc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd56b4"
      ]
    ],
    [
      "unmatched:00bd56ac",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd56b0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd5acc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5adc"
      ]
    ],
    [
      "00bd5ad4",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd5ad8",
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

- 旧版 [`00bd56b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5690.md#insn-00bd56b0) · [`00bd56c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5690.md#insn-00bd56c8)
- 新版 [`00bd5ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5ab8.md#insn-00bd5ad8)

~~~diff
- 00bd56b0 ["INT_ADD", "register:40f0:8", ["const:bd56b0:8", "const:4:8"]]
- 00bd56b0 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd56b0 bytes 54150294
- 00bd56c8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd56c8 ["RETURN", null, ["register:0:8"]]
- 00bd56c8 bytes c0035fd6
+ 00bd5ad8 ["INT_ADD", "register:40f0:8", ["const:bd5ad8:8", "const:4:8"]]
+ 00bd5ad8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd5ad8 bytes 4a150294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd71deeb99271b7992615c384aa4fcae"></a>

### [`00bd573c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd573c.md) → [`00bd5b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5b64.md) _ZN8firebase4auth10githubcred10GetFieldIdENS1_5FieldE

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
      "site": "00bd575c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd5b84"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5774"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd5b78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd5760"
      ]
    ],
    [
      "unmatched:00bd5758",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd575c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd5b78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5b88"
      ]
    ],
    [
      "00bd5b80",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd5b84",
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

- 旧版 [`00bd575c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd573c.md#insn-00bd575c) · [`00bd5774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd573c.md#insn-00bd5774)
- 新版 [`00bd5b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5b64.md#insn-00bd5b84)

~~~diff
- 00bd575c ["INT_ADD", "register:40f0:8", ["const:bd575c:8", "const:4:8"]]
- 00bd575c ["CALL", null, ["callee:00c5b000:8"]]
- 00bd575c bytes 29150294
- 00bd5774 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd5774 ["RETURN", null, ["register:0:8"]]
- 00bd5774 bytes c0035fd6
+ 00bd5b84 ["INT_ADD", "register:40f0:8", ["const:bd5b84:8", "const:4:8"]]
+ 00bd5b84 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd5b84 bytes 1f150294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b35bdea725ca1de247d41741155f8ca9"></a>

### [`00bd59d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd59d8.md) → [`00bd5e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5e00.md) _ZN8firebase4auth10googlecred11GetMethodIdENS1_6MethodE

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
      "site": "00bd59d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd59dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd59dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd59d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd59dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd5e14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd59fc"
      ]
    ]
  ],
  "added": [
    [
      "00bd5e00",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd5e04",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd5e14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5e24"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd59d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd59d8.md#insn-00bd59d8) · [`00bd59dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd59d8.md#insn-00bd59dc) · [`00bd59f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd59d8.md#insn-00bd59f8)

~~~diff
- 00bd59d8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd59d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd59d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd59d8 bytes f30f1ef8
- 00bd59dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd59dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd59dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd59dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd59dc bytes fd7b01a9
- 00bd59f8 ["INT_ADD", "register:40f0:8", ["const:bd59f8:8", "const:4:8"]]
- 00bd59f8 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd59f8 bytes 82140294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-861e1659cd0994468555ea4e5a324e88"></a>

### [`00bd6068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6068.md) → [`00bd6490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6490.md) _ZN8firebase4auth11twittercred11GetMethodIdENS1_6MethodE

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
      "site": "00bd6088"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd64b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd60a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd64a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd608c"
      ]
    ],
    [
      "unmatched:00bd6084",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd6088",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd64a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd64b4"
      ]
    ],
    [
      "00bd64ac",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd64b0",
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

- 旧版 [`00bd6088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6068.md#insn-00bd6088) · [`00bd60a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6068.md#insn-00bd60a0)
- 新版 [`00bd64b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6490.md#insn-00bd64b0)

~~~diff
- 00bd6088 ["INT_ADD", "register:40f0:8", ["const:bd6088:8", "const:4:8"]]
- 00bd6088 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd6088 bytes de120294
- 00bd60a0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd60a0 ["RETURN", null, ["register:0:8"]]
- 00bd60a0 bytes c0035fd6
+ 00bd64b0 ["INT_ADD", "register:40f0:8", ["const:bd64b0:8", "const:4:8"]]
+ 00bd64b0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd64b0 bytes d4120294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc3ef8cd96167a69efffb1be021421df"></a>

### [`00bd6114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6114.md) → [`00bd653c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd653c.md) _ZN8firebase4auth11twittercred10GetFieldIdENS1_5FieldE

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
      "site": "00bd6114"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6118"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6118"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6114",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6118",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6550",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd6138"
      ]
    ]
  ],
  "added": [
    [
      "00bd653c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd6540",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6550",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6560"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6114.md#insn-00bd6114) · [`00bd6118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6114.md#insn-00bd6118) · [`00bd6134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6114.md#insn-00bd6134)

~~~diff
- 00bd6114 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd6114 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd6114 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd6114 bytes f30f1ef8
- 00bd6118 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd6118 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd6118 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd6118 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd6118 bytes fd7b01a9
- 00bd6134 ["INT_ADD", "register:40f0:8", ["const:bd6134:8", "const:4:8"]]
- 00bd6134 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd6134 bytes b3120294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-561c03475e5a76171b66153e65085978"></a>

### [`00bd6150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6150.md) → [`00bd6578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6578.md) _ZN8firebase4auth13oauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "site": "00bd6150"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6154"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6154"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6150",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6154",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6160",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6578",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd657c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6588",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6150.md#insn-00bd6150) · [`00bd6154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6150.md#insn-00bd6154) · [`00bd6164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6150.md#insn-00bd6164)

~~~diff
- 00bd6150 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd6150 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd6150 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd6150 bytes f30f1ef8
- 00bd6154 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd6154 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd6154 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd6154 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd6154 bytes fd7b01a9
- 00bd6164 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd6164 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd6164 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d3df810ba732532c21d4f2c5411289c"></a>

### [`00bd6190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6190.md) → [`00bd65b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd65b8.md) _ZN8firebase4auth13oauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "site": "00bd6190"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6194"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6194"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6190",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6194",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd61a0",
      "READ",
      [
        "storage",
        "01126728",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd65b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd65bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd65c8",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6190.md#insn-00bd6190) · [`00bd6194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6190.md#insn-00bd6194) · [`00bd61a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6190.md#insn-00bd61a4)

~~~diff
- 00bd6190 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd6190 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd6190 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd6190 bytes f30f1ef8
- 00bd6194 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd6194 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd6194 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd6194 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd6194 bytes fd7b01a9
- 00bd61a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd61a4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd61a4 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1fb377eed43f929764c9d9737a92a68"></a>

### [`00bd6264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6264.md) → [`00bd668c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd668c.md) _ZN8firebase4auth13oauthprovider15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6264"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6268"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6268"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6264",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6268",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd626c",
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
      "00bd668c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd6690",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd6694",
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

- 旧版 [`00bd6264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6264.md#insn-00bd6264) · [`00bd6268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6264.md#insn-00bd6268) · [`00bd626c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6264.md#insn-00bd626c)

~~~diff
- 00bd6264 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bd6264 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd6264 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd6264 bytes f50f1df8
- 00bd6268 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd6268 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd6268 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd6268 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd6268 bytes f44f01a9
- 00bd626c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd626c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd626c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd626c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd626c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58c5161313557750a394ceccc7c48edc"></a>

### [`00bd63b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd63b0.md) → [`00bd67d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd67d8.md) _ZN8firebase4auth13oauthprovider11GetMethodIdENS1_6MethodE

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
      "site": "00bd63b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd63b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd63b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd63b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd63b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd63c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd63d4"
      ]
    ]
  ],
  "added": [
    [
      "00bd67d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd67dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd67ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd67fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd63b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd63b0.md#insn-00bd63b0) · [`00bd63b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd63b0.md#insn-00bd63b4) · [`00bd63c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd63b0.md#insn-00bd63c4)

~~~diff
- 00bd63b0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd63b0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd63b0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd63b0 bytes f30f1ef8
- 00bd63b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd63b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd63b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd63b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd63b4 bytes fd7b01a9
- 00bd63c4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd63c4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bd63c4 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-769403c6dd1a64d1f1e33254dec37eb4"></a>

### [`00bd645c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd645c.md) → [`00bd6884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6884.md) _ZN8firebase4auth13oauthprovider10GetFieldIdENS1_5FieldE

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
      "site": "00bd645c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6460"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6460"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd645c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6460",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6470",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd6480"
      ]
    ]
  ],
  "added": [
    [
      "00bd6884",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd6888",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6898",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd68a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd645c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd645c.md#insn-00bd645c) · [`00bd6460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd645c.md#insn-00bd6460) · [`00bd6470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd645c.md#insn-00bd6470)

~~~diff
- 00bd645c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd645c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd645c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd645c bytes f30f1ef8
- 00bd6460 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd6460 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd6460 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd6460 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd6460 bytes fd7b01a9
- 00bd6470 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd6470 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bd6470 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b10f677d896e4fe9056a17dbe03d796"></a>

### [`00bd6498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6498.md) → [`00bd68c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd68c0.md) _ZN8firebase4auth8timeunit19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
      "site": "00bd6498"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd649c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd649c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6498",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd649c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd64a8",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd68c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd68c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd68d0",
      "READ",
      [
        "storage",
        "01126b58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6498.md#insn-00bd6498) · [`00bd649c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6498.md#insn-00bd649c) · [`00bd64ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6498.md#insn-00bd64ac)

~~~diff
- 00bd6498 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd6498 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd6498 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd6498 bytes f30f1ef8
- 00bd649c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd649c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd649c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd649c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd649c bytes fd7b01a9
- 00bd64ac ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd64ac ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bd64ac bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86dc048ac55c9278e2735a03464f56d5"></a>

### [`00bd64d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd64d8.md) → [`00bd6900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6900.md) _ZN8firebase4auth8timeunit19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "site": "00bd64d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd64dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd64dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd64d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd64dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd64e8",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6900",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd6904",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6910",
      "READ",
      [
        "storage",
        "01126b58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd64d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd64d8.md#insn-00bd64d8) · [`00bd64dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd64d8.md#insn-00bd64dc) · [`00bd64ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd64d8.md#insn-00bd64ec)

~~~diff
- 00bd64d8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd64d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd64d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd64d8 bytes f30f1ef8
- 00bd64dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd64dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd64dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd64dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd64dc bytes fd7b01a9
- 00bd64ec ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd64ec ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00bd64ec bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bc0883cef582bffd54d3dad81b49849"></a>

### [`00bd6518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6518.md) → [`00bd6940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6940.md) _ZN8firebase4auth8timeunit10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "site": "00bd6548"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd6970"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd652c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6528",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd652c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd654c"
      ]
    ],
    [
      "unmatched:00bd6538",
      "PARAM",
      [
        "storage",
        "002b378a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd6950",
      "READ",
      [
        "storage",
        "01126b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6954",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6974"
      ]
    ],
    [
      "00bd6960",
      "PARAM",
      [
        "storage",
        "002b37ca",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd652c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6518.md#insn-00bd652c) · [`00bd6540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6518.md#insn-00bd6540) · [`00bd6548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6518.md#insn-00bd6548)

~~~diff
- 00bd652c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd652c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00bd652c bytes 080100b5
- 00bd6540 ["INT_ADD", "register:40f0:8", ["const:bd6540:8", "const:4:8"]]
- 00bd6540 ["CALL", null, ["callee:00c5af10:8"]]
- 00bd6540 bytes 74110294
- 00bd6548 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
- 00bd6548 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6548 bytes 60ae03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3764a44dc464cc858149885e75d2145"></a>

### [`00bd65a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd65a0.md) → [`00bd69c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd69c8.md) _ZN8firebase4auth8timeunit8GetClassEv

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
      "site": "00bd65a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bd69d0"
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
      "unmatched:00bd65a4",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd69cc",
      "READ",
      [
        "storage",
        "01126b58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd65a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd65a0.md#insn-00bd65a8) · [`00bd65a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd65a0.md#insn-00bd65a0)
- 新版 [`00bd69d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd69c8.md#insn-00bd69d0)

~~~diff
- 00bd65a8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd65a8 ["RETURN", null, ["register:0:8"]]
- 00bd65a8 bytes c0035fd6
+ 00bd69d0 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bd69d0 ["RETURN", null, ["register:0:8"]]
+ 00bd69d0 bytes c0035fd6
- 00bd65a0 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd65a0 bytes 882a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-640936656be772780b8963e07c3768ea"></a>

### [`00bd65ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd65ac.md) → [`00bd69d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd69d4.md) _ZN8firebase4auth8timeunit15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.96% / 新版 62.96%

CFGの説明率　旧版 11.11% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd65ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd65b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd65b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd65ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd65b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd65c0",
      "READ",
      [
        "storage",
        "01126760",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd69d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd69d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd69e8",
      "READ",
      [
        "storage",
        "01126b60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd65ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd65ac.md#insn-00bd65ac) · [`00bd65b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd65ac.md#insn-00bd65b0) · [`00bd65ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd65ac.md#insn-00bd65ec)

~~~diff
- 00bd65ac ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bd65ac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd65ac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd65ac bytes f50f1df8
- 00bd65b0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd65b0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd65b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd65b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd65b0 bytes f44f01a9
- 00bd65ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd65ec ["INT_ADD", "register:40f0:8", ["const:bd65ec:8", "const:4:8"]]
- 00bd65ec ["CALLIND", null, ["register:0:8"]]
- 00bd65ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8de6ae3ddf784d7cd88f9574a5e9d39f"></a>

### [`00bd66f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd66f8.md) → [`00bd6b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6b20.md) _ZN8firebase4auth8timeunit11GetMethodIdENS1_6MethodE

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
      "site": "00bd6718"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd6b40"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6730"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6b34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd671c"
      ]
    ],
    [
      "unmatched:00bd6714",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd6718",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd6b34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6b44"
      ]
    ],
    [
      "00bd6b3c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd6b40",
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

- 旧版 [`00bd6718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd66f8.md#insn-00bd6718) · [`00bd6730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd66f8.md#insn-00bd6730)
- 新版 [`00bd6b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6b20.md#insn-00bd6b40)

~~~diff
- 00bd6718 ["INT_ADD", "register:40f0:8", ["const:bd6718:8", "const:4:8"]]
- 00bd6718 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd6718 bytes 3a110294
- 00bd6730 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd6730 ["RETURN", null, ["register:0:8"]]
- 00bd6730 bytes c0035fd6
+ 00bd6b40 ["INT_ADD", "register:40f0:8", ["const:bd6b40:8", "const:4:8"]]
+ 00bd6b40 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd6b40 bytes 30110294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c717b484494e9c0f5e68645e8b8a4943"></a>

### [`00bd67a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd67a4.md) → [`00bd6bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6bcc.md) _ZN8firebase4auth8timeunit10GetFieldIdENS1_5FieldE

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
      "site": "00bd67a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd67a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd67a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd67a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd67a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd67b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd67c8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6bcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd6bd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6be0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6bf0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd67a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd67a4.md#insn-00bd67a4) · [`00bd67a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd67a4.md#insn-00bd67a8) · [`00bd67b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd67a4.md#insn-00bd67b8)

~~~diff
- 00bd67a4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd67a4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd67a4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd67a4 bytes f30f1ef8
- 00bd67a8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd67a8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd67a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd67a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd67a8 bytes fd7b01a9
- 00bd67b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd67b8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00bd67b8 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e54716df4b3c8955e472ca92057b1c4d"></a>

### [`00bd6aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6aec.md) → [`00bd6f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6f14.md) _ZN8firebase4auth26phone_auth_options_builder10GetFieldIdENS1_5FieldE

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
      "site": "00bd6b0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd6f34"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6b24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6f28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd6b10"
      ]
    ],
    [
      "unmatched:00bd6b08",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd6b0c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd6f28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6f38"
      ]
    ],
    [
      "00bd6f30",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd6f34",
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

- 旧版 [`00bd6b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6aec.md#insn-00bd6b0c) · [`00bd6b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd6/00bd6aec.md#insn-00bd6b24)
- 新版 [`00bd6f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6f14.md#insn-00bd6f34)

~~~diff
- 00bd6b0c ["INT_ADD", "register:40f0:8", ["const:bd6b0c:8", "const:4:8"]]
- 00bd6b0c ["CALL", null, ["callee:00c5b000:8"]]
- 00bd6b0c bytes 3d100294
- 00bd6b24 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd6b24 ["RETURN", null, ["register:0:8"]]
- 00bd6b24 bytes c0035fd6
+ 00bd6f34 ["INT_ADD", "register:40f0:8", ["const:bd6f34:8", "const:4:8"]]
+ 00bd6f34 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd6f34 bytes 33100294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88e6d5a420014447dee12852b286685d"></a>

### [`00bd7760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7760.md) → [`00bd7b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7b88.md) _ZN8firebase4auth8auth_idp11GetMethodIdENS1_6MethodE

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
      "site": "00bd7760"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7764"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7764"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd7760",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd7764",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd7b9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd7784"
      ]
    ]
  ],
  "added": [
    [
      "00bd7b88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd7b8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd7b9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7bac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7760.md#insn-00bd7760) · [`00bd7764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7760.md#insn-00bd7764) · [`00bd7780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7760.md#insn-00bd7780)

~~~diff
- 00bd7760 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd7760 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd7760 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd7760 bytes f30f1ef8
- 00bd7764 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd7764 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd7764 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd7764 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd7764 bytes fd7b01a9
- 00bd7780 ["INT_ADD", "register:40f0:8", ["const:bd7780:8", "const:4:8"]]
- 00bd7780 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd7780 bytes 200d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b4209f6accf9a79e8f42b4b2522d414"></a>

### [`00bd7848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7848.md) → [`00bd7c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7c70.md) _ZN8firebase4auth8user_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00bd7874"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd7c9c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd785c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7c80",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd785c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7ca0"
      ]
    ],
    [
      "unmatched:00bd7868",
      "PARAM",
      [
        "storage",
        "002a97ba",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd7c80",
      "READ",
      [
        "storage",
        "01126c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7c84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7ca0"
      ]
    ],
    [
      "00bd7c90",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd785c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7848.md#insn-00bd785c) · [`00bd786c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7848.md#insn-00bd786c) · [`00bd7874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7848.md#insn-00bd7874)

~~~diff
- 00bd785c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd785c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd785c bytes e80000b5
- 00bd786c ["INT_ADD", "register:40f0:8", ["const:bd786c:8", "const:4:8"]]
- 00bd786c ["CALL", null, ["callee:00c5af10:8"]]
- 00bd786c bytes a90c0294
- 00bd7874 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00bd7874 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd7874 bytes 604604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5cdc8f6c2dcbb7b3caeea3344aad3d7"></a>

### [`00bd795c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd795c.md) → [`00bd7d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7d84.md) _ZN8firebase4auth8user_idp15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

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
      "site": "00bd79b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd7ddc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd799c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7d98",
      "READ",
      [
        "storage",
        "01126890",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bd7990",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd79b4",
      "WRITE",
      [
        "storage",
        "01126890",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd7d98",
      "READ",
      [
        "storage",
        "01126c90",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd7db8",
      "READ",
      [
        "storage",
        "01126c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7ddc",
      "WRITE",
      [
        "storage",
        "01126c90",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd799c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd795c.md#insn-00bd799c) · [`00bd79b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd795c.md#insn-00bd79b4)
- 新版 [`00bd7dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7d84.md#insn-00bd7dc4)

~~~diff
- 00bd799c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd799c ["INT_ADD", "register:40f0:8", ["const:bd799c:8", "const:4:8"]]
- 00bd799c ["CALLIND", null, ["register:0:8"]]
- 00bd799c bytes 00013fd6
- 00bd79b4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd79b4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:890:8"]]
- 00bd79b4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd79b4 bytes a0422239
+ 00bd7dc4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7dc4 ["INT_ADD", "register:40f0:8", ["const:bd7dc4:8", "const:4:8"]]
+ 00bd7dc4 ["CALLIND", null, ["register:0:8"]]
+ 00bd7dc4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1bf677d3d3f495eac68d09f1375ff05"></a>

### [`00bd7b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7b54.md) → [`00bd7f7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7f7c.md) _ZN8firebase4auth8user_idp10GetFieldIdENS1_5FieldE

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
      "site": "00bd7b68"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd7f90"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7b74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd7b68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd7b78"
      ]
    ],
    [
      "unmatched:00bd7b70",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd7b74",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd7f90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7fa0"
      ]
    ],
    [
      "00bd7f98",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bd7f9c",
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

- 旧版 [`00bd7b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7b54.md#insn-00bd7b68) · [`00bd7b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7b54.md#insn-00bd7b74) · [`00bd7b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7b54.md#insn-00bd7b8c)

~~~diff
- 00bd7b68 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd7b68 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd7b68 bytes 8b000054
- 00bd7b74 ["INT_ADD", "register:40f0:8", ["const:bd7b74:8", "const:4:8"]]
- 00bd7b74 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd7b74 bytes 230c0294
- 00bd7b8c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd7b8c ["RETURN", null, ["register:0:8"]]
- 00bd7b8c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-721db20f509648e29cdeab1cbc46bc9c"></a>

### [`00bd7df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7df0.md) → [`00bd8218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8218.md) _ZN8firebase4auth8jniphone11GetMethodIdENS1_6MethodE

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
      "site": "00bd7e10"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd8238"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7e28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd822c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd7e14"
      ]
    ],
    [
      "unmatched:00bd7e0c",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd7e10",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00bd822c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd823c"
      ]
    ],
    [
      "00bd8234",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bd8238",
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

- 旧版 [`00bd7e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7df0.md#insn-00bd7e10) · [`00bd7e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7df0.md#insn-00bd7e28)
- 新版 [`00bd8238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8218.md#insn-00bd8238)

~~~diff
- 00bd7e10 ["INT_ADD", "register:40f0:8", ["const:bd7e10:8", "const:4:8"]]
- 00bd7e10 ["CALL", null, ["callee:00c5b000:8"]]
- 00bd7e10 bytes 7c0b0294
- 00bd7e28 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd7e28 ["RETURN", null, ["register:0:8"]]
- 00bd7e28 bytes c0035fd6
+ 00bd8238 ["INT_ADD", "register:40f0:8", ["const:bd8238:8", "const:4:8"]]
+ 00bd8238 ["CALL", null, ["callee:00c5b000:8"]]
+ 00bd8238 bytes 720b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-615345966f0fc92af7ea5d0130cabe0b"></a>

### [`00bd7e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7e9c.md) → [`00bd82c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd82c4.md) _ZN8firebase4auth8jniphone10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00bd7e9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7ea0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7ea0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd7e9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd7ea0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd7eb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd7ec0"
      ]
    ]
  ],
  "added": [
    [
      "00bd82c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd82c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd82d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd82e8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7e9c.md#insn-00bd7e9c) · [`00bd7ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7e9c.md#insn-00bd7ea0) · [`00bd7eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7e9c.md#insn-00bd7eb0)

~~~diff
- 00bd7e9c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd7e9c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd7e9c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd7e9c bytes f30f1ef8
- 00bd7ea0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd7ea0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd7ea0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd7ea0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd7ea0 bytes fd7b01a9
- 00bd7eb0 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd7eb0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd7eb0 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c64d16f1f3346a13ca8a79d3f564d4d5"></a>

### [`00bd7fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7fec.md) → [`00bd8414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8414.md) _ZN8firebase4auth15phonecredential15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 51.85% / 新版 51.85%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7fec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7ff0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7ff0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd7fec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd7ff0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd7ff4",
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
      "00bd8414",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd8418",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd841c",
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

- 旧版 [`00bd7fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7fec.md#insn-00bd7fec) · [`00bd7ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7fec.md#insn-00bd7ff0) · [`00bd7ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd7/00bd7fec.md#insn-00bd7ff4)

~~~diff
- 00bd7fec ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bd7fec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd7fec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd7fec bytes f50f1df8
- 00bd7ff0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd7ff0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd7ff0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd7ff0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd7ff0 bytes f44f01a9
- 00bd7ff4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd7ff4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd7ff4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd7ff4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd7ff4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e90fbdb6f381c6f7dea75db0a79450b"></a>

### [`00bd8058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8058.md) → [`00bd8480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8480.md) _ZN8firebase4auth15phonecredential12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00bd8094"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd80b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd84bc"
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
      "00bd8494",
      "READ",
      [
        "storage",
        "011268d8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd8070",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd80b8"
      ]
    ],
    [
      "00bd84a0",
      "READ",
      [
        "storage",
        "011268e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd8494",
      "READ",
      [
        "storage",
        "01126cd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd8498",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd84e0"
      ]
    ],
    [
      "00bd84a0",
      "READ",
      [
        "storage",
        "01126ce0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd8070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8058.md#insn-00bd8070) · [`00bd8094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8058.md#insn-00bd8094) · [`00bd809c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd8/00bd8058.md#insn-00bd809c)

~~~diff
- 00bd8070 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd8070 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bd8070 bytes 410200b4
- 00bd8094 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd8094 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd8094 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8e0:8"]]
- 00bd8094 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd8094 bytes bf822339
- 00bd809c ["INT_ADD", "register:40f0:8", ["const:bd809c:8", "const:4:8"]]
- 00bd809c ["CALL", null, ["callee:00c5af60:8"]]
- 00bd809c bytes b10a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9fafdf529b66f9dc99e95301c005198"></a>

### [`00bdd2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd2e0.md) → [`00bdd708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd708.md) _ZN8firebase4auth8userinfo11GetMethodIdENS1_6MethodE

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
      "site": "00bdd2e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdd2e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdd2e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd2e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdd2e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bdd71c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bdd304"
      ]
    ]
  ],
  "added": [
    [
      "00bdd708",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bdd70c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bdd71c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdd72c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd2e0.md#insn-00bdd2e0) · [`00bdd2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd2e0.md#insn-00bdd2e4) · [`00bdd300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd2e0.md#insn-00bdd300)

~~~diff
- 00bdd2e0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bdd2e0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bdd2e0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bdd2e0 bytes f30f1ef8
- 00bdd2e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bdd2e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bdd2e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bdd2e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdd2e4 bytes fd7b01a9
- 00bdd300 ["INT_ADD", "register:40f0:8", ["const:bdd300:8", "const:4:8"]]
- 00bdd300 ["CALL", null, ["callee:00c5b000:8"]]
- 00bdd300 bytes 40f60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b9ca500cf4f6e700ad3fc39d11a885c"></a>

### [`00bdd4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd4dc.md) → [`00bdd904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd904.md) _ZN8firebase4auth8metadata15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

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
      "site": "00bdd534"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdd95c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdd51c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdd918",
      "READ",
      [
        "storage",
        "01126a08",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bdd510",
      "READ",
      [
        "storage",
        "01126a00",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bdd534",
      "WRITE",
      [
        "storage",
        "01126a08",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bdd918",
      "READ",
      [
        "storage",
        "01126e08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd938",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bdd95c",
      "WRITE",
      [
        "storage",
        "01126e08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd4dc.md#insn-00bdd51c) · [`00bdd534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd4dc.md#insn-00bdd534)
- 新版 [`00bdd944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd904.md#insn-00bdd944)

~~~diff
- 00bdd51c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bdd51c ["INT_ADD", "register:40f0:8", ["const:bdd51c:8", "const:4:8"]]
- 00bdd51c ["CALLIND", null, ["register:0:8"]]
- 00bdd51c bytes 00013fd6
- 00bdd534 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bdd534 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a08:8"]]
- 00bdd534 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bdd534 bytes a0222839
+ 00bdd944 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bdd944 ["INT_ADD", "register:40f0:8", ["const:bdd944:8", "const:4:8"]]
+ 00bdd944 ["CALLIND", null, ["register:0:8"]]
+ 00bdd944 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-257909946328af859fbb6d4b894ba26a"></a>

### [`00bdd710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd710.md) → [`00bddb38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bddb38.md) _ZN8firebase4auth18userprofilebuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

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
      "site": "00bdd73c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bddb64"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdd724"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bddb48",
      "READ",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bdd724",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bdd740"
      ]
    ],
    [
      "unmatched:00bdd730",
      "PARAM",
      [
        "storage",
        "002ad448",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bddb48",
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bddb4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bddb68"
      ]
    ],
    [
      "00bddb58",
      "PARAM",
      [
        "storage",
        "002ad488",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd710.md#insn-00bdd724) · [`00bdd734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd710.md#insn-00bdd734) · [`00bdd73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd710.md#insn-00bdd73c)

~~~diff
- 00bdd724 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bdd724 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bdd724 bytes e80000b5
- 00bdd734 ["INT_ADD", "register:40f0:8", ["const:bdd734:8", "const:4:8"]]
- 00bdd734 ["CALL", null, ["callee:00c5af10:8"]]
- 00bdd734 bytes f7f40194
- 00bdd73c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a28:8"]]
- 00bdd73c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bdd73c bytes 601605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1049f33760fb9ca502967cc4d88c3c54"></a>

### [`00c30648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c30/00c30648.md) → [`00c30a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30a70.md) _ZNSt6__ndk118__time_get_storageIcE4initERKNS_5ctypeIcEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5e8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e8f0.md) · 呼出先 4件 [`00bf1b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1b70.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e260.md) [`00c5e8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e8d0.md)
- 新版 呼出元 1件 [`00c5ecf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ecf0.md) · 呼出先 4件 [`00bf1f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f98.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e660.md) [`00c5ecd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ecd0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.94% / 新版 94.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c30acc",
      "PARAM",
      [
        "storage",
        "002b27c1",
        null,
        null
      ]
    ],
    [
      "00c30af4",
      "PARAM",
      [
        "storage",
        "002ac4dd",
        null,
        null
      ]
    ],
    [
      "00c30b40",
      "PARAM",
      [
        "storage",
        "002af707",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c30acc",
      "PARAM",
      [
        "storage",
        "002b2801",
        null,
        null
      ]
    ],
    [
      "00c30af4",
      "PARAM",
      [
        "storage",
        "002ac51d",
        null,
        null
      ]
    ],
    [
      "00c30b40",
      "PARAM",
      [
        "storage",
        "002af747",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c30678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c30/00c30648.md#insn-00c30678) · [`00c30680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c30/00c30648.md#insn-00c30680) · [`00c30684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c30/00c30648.md#insn-00c30684)
- 新版 [`00c30aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30a70.md#insn-00c30aa0) · [`00c30aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30a70.md#insn-00c30aac)

~~~diff
- 00c30678 ["COPY", "tmp:0:8", ["const:7c1:8"]]
- 00c30678 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00c30678 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00c30678 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00c30aa0 ["COPY", "tmp:0:8", ["const:801:8"]]
+ 00c30aa0 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c30aa0 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c30aa0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00c30678 bytes b5061f91
+ 00c30aa0 bytes b5062091
- 00c30680 ["COPY", "register:40b8:8", ["const:2ac000:8"]]
- 00c30680 bytes f7b3ff90
- 00c30684 ["COPY", "tmp:0:8", ["const:4dd:8"]]
- 00c30684 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 00c30684 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 00c30684 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 00c30aac ["COPY", "tmp:0:8", ["const:51d:8"]]
+ 00c30aac ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 00c30aac ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 00c30aac ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 00c30684 bytes f7761391
+ 00c30aac bytes f7761491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79ea597234f84ee378d796745e36fbeb"></a>

### [`00c46cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46cb8.md) → [`00c470e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c470e0.md) FUN_00c470e0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c47158",
      "PARAM",
      [
        "storage",
        "002ae6ba",
        null,
        null
      ]
    ],
    [
      "00c47158",
      "PARAM",
      [
        "storage",
        "0029ed60",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c47158",
      "PARAM",
      [
        "storage",
        "002ae6fa",
        null,
        null
      ]
    ],
    [
      "00c47158",
      "PARAM",
      [
        "storage",
        "0029eda0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c46d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46cb8.md#insn-00c46d08) · [`00c46d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46cb8.md#insn-00c46d1c) · [`00c46d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46cb8.md#insn-00c46d24)
- 新版 [`00c47130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c470e0.md#insn-00c47130) · [`00c47144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c470e0.md#insn-00c47144)

~~~diff
- 00c46d08 ["INT_ADD", "register:40f0:8", ["const:c46d08:8", "const:4:8"]]
- 00c46d08 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00c47130 ["INT_ADD", "register:40f0:8", ["const:c47130:8", "const:4:8"]]
+ 00c47130 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00c46d08 bytes e64b0094
+ 00c47130 bytes dc4b0094
- 00c46d1c ["COPY", "tmp:0:8", ["const:6ba:8"]]
- 00c46d1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c46d1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c46d1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c47144 ["COPY", "tmp:0:8", ["const:6fa:8"]]
+ 00c47144 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c47144 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c47144 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c46d1c bytes 29e91a91
+ 00c47144 bytes 29e91b91
- 00c46d24 ["COPY", "register:4050:8", ["const:29e000:8"]]
- 00c46d24 bytes cab2ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-977a8dad31505de0458423072ab3597b"></a>

### [`00c51414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51414.md) → [`00c5183c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c5183c.md) FUN_00c5183c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c5174c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c5174c.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c51b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51b74.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c51a08",
      "PARAM",
      [
        "storage",
        "002a9915",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c51a08",
      "PARAM",
      [
        "storage",
        "002a99e2",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c51440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51414.md#insn-00c51440) · [`00c51460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51414.md#insn-00c51460) · [`00c51488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51414.md#insn-00c51488)
- 新版 [`00c51868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c5183c.md#insn-00c51868) · [`00c51888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c5183c.md#insn-00c51888) · [`00c518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c5183c.md#insn-00c518b0)

~~~diff
- 00c51440 ["INT_ADD", "register:40f0:8", ["const:c51440:8", "const:4:8"]]
- 00c51440 ["CALL", null, ["callee:00c51b74:8"]]
+ 00c51868 ["INT_ADD", "register:40f0:8", ["const:c51868:8", "const:4:8"]]
+ 00c51868 ["CALL", null, ["callee:00c51b74:8"]]
- 00c51440 bytes c3000094
+ 00c51868 bytes c3000094
- 00c51460 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51460 ["INT_ADD", "register:40f0:8", ["const:c51460:8", "const:4:8"]]
- 00c51460 ["CALLIND", null, ["register:0:8"]]
+ 00c51888 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51888 ["INT_ADD", "register:40f0:8", ["const:c51888:8", "const:4:8"]]
+ 00c51888 ["CALLIND", null, ["register:0:8"]]
- 00c51460 bytes 00013fd6
+ 00c51888 bytes 00013fd6
- 00c51488 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51488 ["INT_ADD", "register:40f0:8", ["const:c51488:8", "const:4:8"]]
- 00c51488 ["CALLIND", null, ["register:0:8"]]
+ 00c518b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c518b0 ["INT_ADD", "register:40f0:8", ["const:c518b0:8", "const:4:8"]]
+ 00c518b0 ["CALLIND", null, ["register:0:8"]]
- 00c51488 bytes 00013fd6
+ 00c518b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

