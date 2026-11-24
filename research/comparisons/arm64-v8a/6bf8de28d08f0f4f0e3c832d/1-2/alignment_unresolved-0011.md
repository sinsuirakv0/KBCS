# v16.0.1 → v16.0.2 · 命令位置の検査未完了 (11)

[一覧の目次](README.md)

<a id="compare-ff2152a85550e0e5a89ba5f7773c0cb2"></a>

### [`00bc49cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc49cc.md) → [`00bc4a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4a68.md) _ZN8firebase13remote_config8internal20RemoteConfigInternalD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d880.md) · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aaa0.md) [`00c5ac30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac30.md) [`00c5ac50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac50.md) [`00c5af00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af00.md)
- 新版 呼出元 1件 [`00c5d950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d950.md) · 呼出先 7件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab70.md) [`00c5ad00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad00.md) [`00c5ad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad20.md) [`00c5afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afd0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 89.19% / 新版 94.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc49cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc49cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc49d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc49cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc49d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc49d4",
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
      "00bc4a68",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bc4a6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc4a70",
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

- 旧版 [`00bc49cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc49cc.md#insn-00bc49cc) · [`00bc49d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc49cc.md#insn-00bc49d0) · [`00bc49d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc49cc.md#insn-00bc49d4)

~~~diff
- 00bc49cc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bc49cc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bc49cc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bc49cc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc49cc bytes f657bda9
- 00bc49d0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc49d0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc49d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc49d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc49d0 bytes f44f01a9
- 00bc49d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc49d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc49d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bc49d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc49d4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16281dae0307235c1920e2eaff631882"></a>

### [`00bc9d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9d28.md) → [`00bc9dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9dc4.md) _ZN8firebase6FutureINS_13remote_config10ConfigInfoEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d910.md) · 呼出先 3件 [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5adf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5adf0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)
- 新版 呼出元 1件 [`00c5d9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d9e0.md) · 呼出先 3件 [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aec0.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 93.55% / 新版 93.55%

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
      "site": "00bc9d70"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bc9e0c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9da0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc9d70",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc9e0c",
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

- 旧版 [`00bc9d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9d28.md#insn-00bc9d70) · [`00bc9da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9d28.md#insn-00bc9da0)
- 新版 [`00bc9e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9dc4.md#insn-00bc9e0c)

~~~diff
- 00bc9d70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc9d70 ["INT_ADD", "register:40f0:8", ["const:bc9d70:8", "const:4:8"]]
- 00bc9d70 ["CALLIND", null, ["register:0:8"]]
- 00bc9d70 bytes 00013fd6
- 00bc9da0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc9da0 ["RETURN", null, ["register:0:8"]]
- 00bc9da0 bytes c0035fd6
+ 00bc9e0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc9e0c ["INT_ADD", "register:40f0:8", ["const:bc9e0c:8", "const:4:8"]]
+ 00bc9e0c ["CALLIND", null, ["register:0:8"]]
+ 00bc9e0c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e34126ebd15de82c8c72f33fac402dbd"></a>

### [`00bc9edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9edc.md) → [`00bc9f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9f78.md) _ZN8firebase6FutureIbEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5d920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d920.md) · 呼出先 3件 [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5adf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5adf0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)
- 新版 呼出元 1件 [`00c5d9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d9f0.md) · 呼出先 3件 [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aec0.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.19% / 新版 74.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9ee0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9ee0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9ee4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc9ee0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc9ee4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc9f2c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5aec0"
      ]
    ]
  ],
  "added": [
    [
      "00bc9f7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc9f80",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc9fc8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5aec0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9edc.md#insn-00bc9ee0) · [`00bc9ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9edc.md#insn-00bc9ee4) · [`00bc9efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9edc.md#insn-00bc9efc)
- 新版 [`00bc9f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9f78.md#insn-00bc9f98)

~~~diff
- 00bc9ee0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc9ee0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc9ee0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc9ee0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc9ee0 bytes f44f01a9
- 00bc9ee4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc9ee4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc9ee4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bc9ee4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc9ee4 bytes fd7b02a9
- 00bc9efc ["INT_ADD", "register:40f0:8", ["const:bc9efc:8", "const:4:8"]]
- 00bc9efc ["CALL", null, ["callee:00c5ad40:8"]]
+ 00bc9f98 ["INT_ADD", "register:40f0:8", ["const:bc9f98:8", "const:4:8"]]
+ 00bc9f98 ["CALL", null, ["callee:00c5ad40:8"]]
- 00bc9efc bytes 5d430294
+ 00bc9f98 bytes 6a430294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4a0eafbcc3fc61144cee8bc8b972c9c"></a>

### [`00bc9f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9f80.md) → [`00bca01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca01c.md) FUN_00bca01c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

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
      "site": "00bc9fa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bca03c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9fb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc9fa0",
      "DATA",
      [
        "storage",
        "00c91828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bca03c",
      "DATA",
      [
        "storage",
        "00c918f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9f80.md#insn-00bc9fa0) · [`00bc9fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9f80.md#insn-00bc9fb4)
- 新版 [`00bca03c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca01c.md#insn-00bca03c)

~~~diff
- 00bc9fa0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00bc9fa0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bc9fa0 bytes 080000f9
- 00bc9fb4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc9fb4 ["RETURN", null, ["register:0:8"]]
- 00bc9fb4 bytes c0035fd6
+ 00bca03c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00bca03c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00bca03c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec72da2498390a788fda72e467aa89c0"></a>

### [`00bc9fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9fb8.md) → [`00bca054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca054.md) FUN_00bca054

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00bc9fc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc9fc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bca05c"
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
      "unmatched:00bc9fc0",
      "DATA",
      [
        "storage",
        "00c91828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bca05c",
      "DATA",
      [
        "storage",
        "00c918f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9fb8.md#insn-00bc9fc0) · [`00bc9fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9fb8.md#insn-00bc9fc8) · [`00bc9fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9fb8.md#insn-00bc9fcc)

~~~diff
- 00bc9fc0 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00bc9fc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bc9fc0 bytes 280000f9
- 00bc9fc8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 00bc9fc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bc9fc8 bytes 280400f9
- 00bc9fcc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc9fcc ["RETURN", null, ["register:0:8"]]
- 00bc9fcc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d82c42ecee06d8ceba19d4e14512942f"></a>

### [`00bca0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca0b8.md) → [`00bca154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca154.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationC1ERKS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bca360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca360.md) [`00c5ac00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bca3fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca3fc.md) [`00c5acd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acd0.md)

変更の種類 constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bca158",
      "READ",
      [
        "storage",
        "00c9b928",
        null,
        "pointer"
      ]
    ],
    [
      "00bca160",
      "DATA",
      [
        "storage",
        "00c918a8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00bca178",
      "READ",
      [
        "storage",
        "00c9b920",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bca158",
      "READ",
      [
        "storage",
        "00c9b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00bca160",
      "DATA",
      [
        "storage",
        "00c91978",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00bca178",
      "READ",
      [
        "storage",
        "00c9b9f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca0b8.md#insn-00bca0bc) · [`00bca0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca0b8.md#insn-00bca0dc) · [`00bca0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca0b8.md#insn-00bca0e8)
- 新版 [`00bca158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca154.md#insn-00bca158) · [`00bca178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca154.md#insn-00bca178)

~~~diff
- 00bca0bc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:928:8"]]
- 00bca0bc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bca158 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9f8:8"]]
+ 00bca158 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bca0bc bytes 299544f9
+ 00bca158 bytes 29fd44f9
- 00bca0dc ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:920:8"]]
- 00bca0dc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bca178 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:9f0:8"]]
+ 00bca178 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00bca0dc bytes 429044f9
+ 00bca178 bytes 42f844f9
- 00bca0e8 ["COPY", "register:4008:8", ["register:4040:8"]]
- 00bca0e8 bytes e10308aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06937bab2b8584c16324334c0dc7d7e9"></a>

### [`00bca0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca0f4.md) → [`00bca190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca190.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationC1EOS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bca360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca360.md) [`00c5ac00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac00.md) [`00c5ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bca3fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca3fc.md) [`00c5acd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acd0.md) [`00c5ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ace0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bca114"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bca1b0"
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
      "00bca1a0",
      "READ",
      [
        "storage",
        "00c9b928",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bca114",
      "DATA",
      [
        "storage",
        "00c918a8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00bca1ec",
      "READ",
      [
        "storage",
        "00c9b920",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bca1a0",
      "READ",
      [
        "storage",
        "00c9b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00bca1b0",
      "DATA",
      [
        "storage",
        "00c91978",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00bca1ec",
      "READ",
      [
        "storage",
        "00c9b9f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca0f4.md#insn-00bca114) · [`00bca104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca0f4.md#insn-00bca104)
- 新版 [`00bca1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca190.md#insn-00bca1b0) · [`00bca1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca190.md#insn-00bca1a0)

~~~diff
- 00bca114 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00bca114 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bca114 bytes 080000f9
+ 00bca1b0 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00bca1b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00bca1b0 bytes 080000f9
- 00bca104 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:928:8"]]
- 00bca104 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bca1a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9f8:8"]]
+ 00bca1a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bca104 bytes 089544f9
+ 00bca1a0 bytes 08fd44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eba5a37491d7d5d5a9c59d3d876c6b92"></a>

### [`00bca1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca1b8.md) → [`00bca254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bca254.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ace0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

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
      "site": "00bca1b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bca1bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bca1bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bca1b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bca1bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bca1cc",
      "READ",
      [
        "storage",
        "00c9b928",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bca254",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bca258",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bca268",
      "READ",
      [
        "storage",
        "00c9b9f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca1b8.md#insn-00bca1b8) · [`00bca1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca1b8.md#insn-00bca1bc) · [`00bca1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca1b8.md#insn-00bca1d8)

~~~diff
- 00bca1b8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bca1b8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bca1b8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bca1b8 bytes f30f1ef8
- 00bca1bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bca1bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bca1bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bca1bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bca1bc bytes fd7b01a9
- 00bca1d8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00bca1d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bca1d8 bytes 090000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0b86d1c9cdd5d02efe43db52fb5a1e9"></a>

### [`00bcb1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb1dc.md) → [`00bcb278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb278.md) _ZN8firebase4auth4Auth23RemoveAuthStateListenerEPNS0_17AuthStateListenerE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5da70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5da70.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5db40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5db40.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 69.12% / 新版 69.12%

CFGの説明率　旧版 29.73% / 新版 28.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb214"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb244"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb278"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcb214",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb30c"
      ]
    ],
    [
      "unmatched:00bcb244",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb2c8"
      ]
    ],
    [
      "unmatched:00bcb278",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb370"
      ]
    ]
  ],
  "added": [
    [
      "00bcb2b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb30c"
      ]
    ],
    [
      "00bcb2e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb2c8"
      ]
    ],
    [
      "00bcb314",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcb370"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb1dc.md#insn-00bcb214) · [`00bcb244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb1dc.md#insn-00bcb244) · [`00bcb278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb1dc.md#insn-00bcb278)

~~~diff
- 00bcb214 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00bcb214 bytes e0020054
- 00bcb244 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bcb244 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bcb244 bytes 41ffff54
- 00bcb278 ["CBRANCH", null, ["local:b22:8", "register:101:1"]]
- 00bcb278 bytes e0020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80ceb01c58959475974031d4670fb122"></a>

### [`00bcb6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb6bc.md) → [`00bcb758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb758.md) _ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEEC2ERKS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db00.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)
- 新版 呼出元 1件 [`00c5dbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dbd0.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb6bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb6bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb6c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcb6bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcb6c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcb6c4",
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
      "00bcb758",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcb75c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcb760",
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

- 旧版 [`00bcb6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb6bc.md#insn-00bcb6bc) · [`00bcb6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb6bc.md#insn-00bcb6c0) · [`00bcb6c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb6bc.md#insn-00bcb6c4)

~~~diff
- 00bcb6bc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bcb6bc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bcb6bc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bcb6bc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcb6bc bytes f657bda9
- 00bcb6c0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcb6c0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcb6c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcb6c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcb6c0 bytes f44f01a9
- 00bcb6c4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcb6c4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcb6c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bcb6c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcb6c4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97978a0577c88e84c2c99d38247032c8"></a>

### [`00bcb8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb8e4.md) → [`00bcb980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb980.md) _ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEEC2ERKS7_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5dae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dae0.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)
- 新版 呼出元 1件 [`00c5dbb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dbb0.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 75.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb960"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bcb9fc"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb8e4.md#insn-00bcb960) · [`00bcb914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb8e4.md#insn-00bcb914)
- 新版 [`00bcb9fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb980.md#insn-00bcb9fc) · [`00bcb9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb980.md#insn-00bcb9b0)

~~~diff
- 00bcb960 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bcb960 ["RETURN", null, ["register:0:8"]]
- 00bcb960 bytes c0035fd6
+ 00bcb9fc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bcb9fc ["RETURN", null, ["register:0:8"]]
+ 00bcb9fc bytes c0035fd6
- 00bcb914 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcb914 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00bcb9b0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bcb9b0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00bcb914 bytes 880200b5
+ 00bcb9b0 bytes 880200b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e096af0935b52a752feaad1dce91547"></a>

### [`00bcc1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc1d0.md) → [`00bcc26c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc26c.md) _ZN8firebase4auth14ClearUserInfosEPNS0_8AuthDataE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d9a0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5da70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da70.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 30.00% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc218"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bcc2b4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc244"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc218",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc2d4"
      ]
    ]
  ],
  "added": [
    [
      "00bcc2b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc2d4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc1d0.md#insn-00bcc218) · [`00bcc244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc1d0.md#insn-00bcc244)
- 新版 [`00bcc2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc26c.md#insn-00bcc2b4)

~~~diff
- 00bcc218 ["CBRANCH", null, ["local:b5:8", "register:102:1"]]
- 00bcc218 bytes 02010054
- 00bcc244 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bcc244 ["RETURN", null, ["register:0:8"]]
- 00bcc244 bytes c0035fd6
+ 00bcc2b4 ["CBRANCH", null, ["local:b6:8", "register:102:1"]]
+ 00bcc2b4 bytes 02010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a53dfdb59805acb4d4f37c4b3ae758d"></a>

### [`00bcc414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc414.md) → [`00bcc4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc4b0.md) _ZN8firebase4auth4auth8GetClassEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00bcc41c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bcc4b8"
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
      "unmatched:00bcc418",
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
      "00bcc4b4",
      "READ",
      [
        "storage",
        "01126828",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc414.md#insn-00bcc41c) · [`00bcc414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc414.md#insn-00bcc414)
- 新版 [`00bcc4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc4b0.md#insn-00bcc4b8)

~~~diff
- 00bcc41c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bcc41c ["RETURN", null, ["register:0:8"]]
- 00bcc41c bytes c0035fd6
+ 00bcc4b8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bcc4b8 ["RETURN", null, ["register:0:8"]]
+ 00bcc4b8 bytes c0035fd6
- 00bcc414 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bcc414 bytes c82a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5fb1ac3fbab8e93f799b59d6574ae69"></a>

### [`00bcc56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc56c.md) → [`00bcc608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc608.md) _ZN8firebase4auth4auth11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bcc58c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bcc628"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc5a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcc61c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcc590"
      ]
    ],
    [
      "unmatched:00bcc588",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcc58c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ],
  "added": [
    [
      "00bcc61c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcc62c"
      ]
    ],
    [
      "00bcc624",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bcc628",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc56c.md#insn-00bcc58c) · [`00bcc5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc56c.md#insn-00bcc5a4)
- 新版 [`00bcc628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc608.md#insn-00bcc628)

~~~diff
- 00bcc58c ["INT_ADD", "register:40f0:8", ["const:bcc58c:8", "const:4:8"]]
- 00bcc58c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bcc58c bytes 9d3a0294
- 00bcc5a4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bcc5a4 ["RETURN", null, ["register:0:8"]]
- 00bcc5a4 bytes c0035fd6
+ 00bcc628 ["INT_ADD", "register:40f0:8", ["const:bcc628:8", "const:4:8"]]
+ 00bcc628 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bcc628 bytes aa3a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8032f4780840c2c3bff77244426469d0"></a>

### [`00bcc960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc960.md) → [`00bcc9fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc9fc.md) _ZN8firebase4auth17signinmethodquery10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bcc980"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bcca1c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc998"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcca10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcc984"
      ]
    ],
    [
      "unmatched:00bcc97c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcc980",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ],
  "added": [
    [
      "00bcca10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcca20"
      ]
    ],
    [
      "00bcca18",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bcca1c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc960.md#insn-00bcc980) · [`00bcc998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc960.md#insn-00bcc998)
- 新版 [`00bcca1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc9fc.md#insn-00bcca1c)

~~~diff
- 00bcc980 ["INT_ADD", "register:40f0:8", ["const:bcc980:8", "const:4:8"]]
- 00bcc980 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bcc980 bytes a0390294
- 00bcc998 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bcc998 ["RETURN", null, ["register:0:8"]]
- 00bcc998 bytes c0035fd6
+ 00bcca1c ["INT_ADD", "register:40f0:8", ["const:bcca1c:8", "const:4:8"]]
+ 00bcca1c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bcca1c bytes ad390294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a775bfa83135a0e75e33fba3769e691c"></a>

### [`00bccab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccab0.md) → [`00bccb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccb4c.md) _ZN8firebase4auth11jnilistener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 16.67% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccb08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bccba4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccaf0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bccac4",
      "READ",
      [
        "storage",
        "011267f8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bccae4",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bccb08",
      "WRITE",
      [
        "storage",
        "011267f8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bccb60",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bccb80",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccba4",
      "WRITE",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bccaf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccab0.md#insn-00bccaf0) · [`00bccb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccab0.md#insn-00bccb08)
- 新版 [`00bccb8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccb4c.md#insn-00bccb8c)

~~~diff
- 00bccaf0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bccaf0 ["INT_ADD", "register:40f0:8", ["const:bccaf0:8", "const:4:8"]]
- 00bccaf0 ["CALLIND", null, ["register:0:8"]]
- 00bccaf0 bytes 00013fd6
- 00bccb08 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bccb08 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7f8:8"]]
- 00bccb08 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bccb08 bytes a0e21f39
+ 00bccb8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bccb8c ["INT_ADD", "register:40f0:8", ["const:bccb8c:8", "const:4:8"]]
+ 00bccb8c ["CALLIND", null, ["register:0:8"]]
+ 00bccb8c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b630de1dbf1878e9399e260b9255282"></a>

### [`00bccbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccbfc.md) → [`00bccc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccc98.md) _ZN8firebase4auth11jnilistener11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bccbfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccc00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccc00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bccbfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bccc00",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bccc10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bccc20"
      ]
    ]
  ],
  "added": [
    [
      "00bccc98",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bccc9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bcccac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcccbc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bccbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccbfc.md#insn-00bccbfc) · [`00bccc00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccbfc.md#insn-00bccc00) · [`00bccc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccbfc.md#insn-00bccc10)

~~~diff
- 00bccbfc ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bccbfc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bccbfc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bccbfc bytes f30f1ef8
- 00bccc00 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bccc00 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bccc00 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bccc00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bccc00 bytes fd7b01a9
- 00bccc10 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bccc10 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bccc10 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64b20ff26122be8787c8abd8686c1f71"></a>

### [`00bccca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccca8.md) → [`00bccd44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccd44.md) _ZN8firebase4auth11jnilistener10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bcccc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bccd64"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccce0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bccd58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bccccc"
      ]
    ],
    [
      "unmatched:00bcccc4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bcccc8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ],
  "added": [
    [
      "00bccd58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccd68"
      ]
    ],
    [
      "00bccd60",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bccd64",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcccc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccca8.md#insn-00bcccc8) · [`00bccce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccca8.md#insn-00bccce0)
- 新版 [`00bccd64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccd44.md#insn-00bccd64)

~~~diff
- 00bcccc8 ["INT_ADD", "register:40f0:8", ["const:bcccc8:8", "const:4:8"]]
- 00bcccc8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bcccc8 bytes ce380294
- 00bccce0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bccce0 ["RETURN", null, ["register:0:8"]]
- 00bccce0 bytes c0035fd6
+ 00bccd64 ["INT_ADD", "register:40f0:8", ["const:bccd64:8", "const:4:8"]]
+ 00bccd64 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bccd64 bytes db380294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-935dc192d4963e37ff02a59bd59affa7"></a>

### [`00bcce64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcce64.md) → [`00bccf00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccf00.md) _ZN8firebase4auth21jni_id_token_listener12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00bccea0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccec0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bccf3c"
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
      "00bccf14",
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bcce7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccf60"
      ]
    ],
    [
      "00bccf20",
      "READ",
      [
        "storage",
        "01126820",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bccf14",
      "READ",
      [
        "storage",
        "01126918",
        null,
        "undefined8"
      ]
    ],
    [
      "00bccf18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bccf60"
      ]
    ],
    [
      "00bccf20",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcce7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcce64.md#insn-00bcce7c) · [`00bccea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcce64.md#insn-00bccea0) · [`00bccea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcce64.md#insn-00bccea8)

~~~diff
- 00bcce7c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bcce7c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bcce7c bytes 410200b4
- 00bccea0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bccea0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bccea0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:820:8"]]
- 00bccea0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bccea0 bytes bf822039
- 00bccea8 ["INT_ADD", "register:40f0:8", ["const:bccea8:8", "const:4:8"]]
- 00bccea8 ["CALL", null, ["callee:00c5b030:8"]]
- 00bccea8 bytes 2e380294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60b8190d917505ee5b7839b22ccf99fa"></a>

### [`00bccf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccf44.md) → [`00bccfe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccfe0.md) _ZN8firebase4auth21jni_id_token_listener11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bccf44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccf48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bccf48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bccf44",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bccf48",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bccff4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bccf68"
      ]
    ]
  ],
  "added": [
    [
      "00bccfe0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bccfe4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bccff4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcd004"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bccf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccf44.md#insn-00bccf44) · [`00bccf48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccf44.md#insn-00bccf48) · [`00bccf64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccf44.md#insn-00bccf64)

~~~diff
- 00bccf44 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bccf44 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bccf44 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bccf44 bytes f30f1ef8
- 00bccf48 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bccf48 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bccf48 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bccf48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bccf48 bytes fd7b01a9
- 00bccf64 ["INT_ADD", "register:40f0:8", ["const:bccf64:8", "const:4:8"]]
- 00bccf64 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bccf64 bytes 27380294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71daaa300681da18ef1c47089db9261d"></a>

### [`00bd07e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd07e0.md) → [`00bd087c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd087c.md) _ZN8firebase4auth10authresult15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0838"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd08d4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0820"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd0890",
      "READ",
      [
        "storage",
        "01126850",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd089c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd083c"
      ]
    ],
    [
      "unmatched:00bd0814",
      "READ",
      [
        "storage",
        "01126848",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0890",
      "READ",
      [
        "storage",
        "01126950",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd089c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd08d8"
      ]
    ],
    [
      "00bd08b0",
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

- 旧版 [`00bd0820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd07e0.md#insn-00bd0820) · [`00bd0838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd07e0.md#insn-00bd0838) · [`00bd0848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd07e0.md#insn-00bd0848)

~~~diff
- 00bd0820 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0820 ["INT_ADD", "register:40f0:8", ["const:bd0820:8", "const:4:8"]]
- 00bd0820 ["CALLIND", null, ["register:0:8"]]
- 00bd0820 bytes 00013fd6
- 00bd0838 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd0838 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:850:8"]]
- 00bd0838 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd0838 bytes a0422139
- 00bd0848 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd0848 ["RETURN", null, ["register:0:8"]]
- 00bd0848 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ea391c8b6264fd9d3fefa46ca49bb33"></a>

### [`00bd092c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd092c.md) → [`00bd09c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd09c8.md) _ZN8firebase4auth10authresult11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bd094c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd09e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0964"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd09dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd0950"
      ]
    ],
    [
      "unmatched:00bd0948",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd094c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ],
  "added": [
    [
      "00bd09dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd09ec"
      ]
    ],
    [
      "00bd09e4",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bd09e8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd094c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd092c.md#insn-00bd094c) · [`00bd0964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd092c.md#insn-00bd0964)
- 新版 [`00bd09e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd09c8.md#insn-00bd09e8)

~~~diff
- 00bd094c ["INT_ADD", "register:40f0:8", ["const:bd094c:8", "const:4:8"]]
- 00bd094c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd094c bytes ad290294
- 00bd0964 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd0964 ["RETURN", null, ["register:0:8"]]
- 00bd0964 bytes c0035fd6
+ 00bd09e8 ["INT_ADD", "register:40f0:8", ["const:bd09e8:8", "const:4:8"]]
+ 00bd09e8 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd09e8 bytes ba290294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84f775391011025a50c223969c525375"></a>

### [`00bd0fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0fbc.md) → [`00bd1058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd1/00bd1058.md) _ZN8firebase4auth27api_not_available_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bd0fd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd106c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0fdc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0fd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd0fe0"
      ]
    ],
    [
      "unmatched:00bd0fd8",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd0fdc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ],
  "added": [
    [
      "00bd106c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd107c"
      ]
    ],
    [
      "00bd1074",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bd1078",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0fbc.md#insn-00bd0fd0) · [`00bd0fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0fbc.md#insn-00bd0fdc) · [`00bd0ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0fbc.md#insn-00bd0ff4)

~~~diff
- 00bd0fd0 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd0fd0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd0fd0 bytes 8b000054
- 00bd0fdc ["INT_ADD", "register:40f0:8", ["const:bd0fdc:8", "const:4:8"]]
- 00bd0fdc ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd0fdc bytes 09280294
- 00bd0ff4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd0ff4 ["RETURN", null, ["register:0:8"]]
- 00bd0ff4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9eb4d5f518cb7c3db92ddc6589a0cee"></a>

### [`00bd1124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1124.md) → [`00bd11c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd1/00bd11c0.md) _ZN8firebase4auth21action_code_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bd1154"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd11f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1138"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd1134",
      "READ",
      [
        "storage",
        "011268c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd1138",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd11f4"
      ]
    ],
    [
      "unmatched:00bd1144",
      "PARAM",
      [
        "storage",
        "002a500f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd11d0",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd11d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd11f4"
      ]
    ],
    [
      "00bd11e0",
      "PARAM",
      [
        "storage",
        "002a4fb3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1124.md#insn-00bd1138) · [`00bd114c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1124.md#insn-00bd114c) · [`00bd1154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1124.md#insn-00bd1154)

~~~diff
- 00bd1138 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd1138 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd1138 bytes 080100b5
- 00bd114c ["INT_ADD", "register:40f0:8", ["const:bd114c:8", "const:4:8"]]
- 00bd114c ["CALL", null, ["callee:00c5afe0:8"]]
- 00bd114c bytes 71270294
- 00bd1154 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
- 00bd1154 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd1154 bytes 606604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5ea3500dfb94f198eef923100b5d7ac"></a>

### [`00bd11b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd11b8.md) → [`00bd1254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd1/00bd1254.md) _ZN8firebase4auth21action_code_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "site": "00bd1210"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd12ac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd11f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd1268",
      "READ",
      [
        "storage",
        "011268d0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bd11ec",
      "READ",
      [
        "storage",
        "011268c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd1210",
      "WRITE",
      [
        "storage",
        "011268d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd1268",
      "READ",
      [
        "storage",
        "011269d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1288",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd12ac",
      "WRITE",
      [
        "storage",
        "011269d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd11f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd11b8.md#insn-00bd11f8) · [`00bd1210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd11b8.md#insn-00bd1210)
- 新版 [`00bd1294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd1/00bd1254.md#insn-00bd1294)

~~~diff
- 00bd11f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd11f8 ["INT_ADD", "register:40f0:8", ["const:bd11f8:8", "const:4:8"]]
- 00bd11f8 ["CALLIND", null, ["register:0:8"]]
- 00bd11f8 bytes 00013fd6
- 00bd1210 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd1210 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8d0:8"]]
- 00bd1210 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd1210 bytes a0422339
+ 00bd1294 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd1294 ["INT_ADD", "register:40f0:8", ["const:bd1294:8", "const:4:8"]]
+ 00bd1294 ["CALLIND", null, ["register:0:8"]]
+ 00bd1294 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1afea210ef7eaf43849c07b4b7aebfa"></a>

### [`00bd13b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd13b0.md) → [`00bd144c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd1/00bd144c.md) _ZN8firebase4auth21action_code_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bd13b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd13b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd13b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd13b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd13b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd13c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd13d4"
      ]
    ]
  ],
  "added": [
    [
      "00bd144c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd1450",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd1460",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1470"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd13b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd13b0.md#insn-00bd13b0) · [`00bd13b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd13b0.md#insn-00bd13b4) · [`00bd13c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd13b0.md#insn-00bd13c4)

~~~diff
- 00bd13b0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd13b0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd13b0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd13b0 bytes f30f1ef8
- 00bd13b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd13b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd13b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd13b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd13b4 bytes fd7b01a9
- 00bd13c4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd13c4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd13c4 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bbcadae558f8da4b4851de90b7c1b50"></a>

### [`00bd1ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1ecc.md) → [`00bd1f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd1/00bd1f68.md) _ZN8firebase4auth22invalid_user_exception8GetClassEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00bd1ed4"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bd1f70"
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
      "unmatched:00bd1ed0",
      "READ",
      [
        "storage",
        "01126948",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1f6c",
      "READ",
      [
        "storage",
        "01126a48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1ecc.md#insn-00bd1ed4) · [`00bd1ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1ecc.md#insn-00bd1ecc)
- 新版 [`00bd1f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd1/00bd1f68.md#insn-00bd1f70)

~~~diff
- 00bd1ed4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd1ed4 ["RETURN", null, ["register:0:8"]]
- 00bd1ed4 bytes c0035fd6
+ 00bd1f70 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bd1f70 ["RETURN", null, ["register:0:8"]]
+ 00bd1f70 bytes c0035fd6
- 00bd1ecc ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd1ecc bytes a82a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4da649491977ef9beb4490db8329357f"></a>

### [`00bd1ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1ed8.md) → [`00bd1f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd1/00bd1f74.md) _ZN8firebase4auth22invalid_user_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "site": "00bd1f30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1fcc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1f18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd1f88",
      "READ",
      [
        "storage",
        "01126950",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bd1f0c",
      "READ",
      [
        "storage",
        "01126948",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd1f30",
      "WRITE",
      [
        "storage",
        "01126950",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd1f88",
      "READ",
      [
        "storage",
        "01126a50",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1fa8",
      "READ",
      [
        "storage",
        "01126a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1fcc",
      "WRITE",
      [
        "storage",
        "01126a50",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1ed8.md#insn-00bd1f18) · [`00bd1f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1ed8.md#insn-00bd1f30)
- 新版 [`00bd1fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd1/00bd1f74.md#insn-00bd1fb4)

~~~diff
- 00bd1f18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd1f18 ["INT_ADD", "register:40f0:8", ["const:bd1f18:8", "const:4:8"]]
- 00bd1f18 ["CALLIND", null, ["register:0:8"]]
- 00bd1f18 bytes 00013fd6
- 00bd1f30 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd1f30 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:950:8"]]
- 00bd1f30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd1f30 bytes a0422539
+ 00bd1fb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd1fb4 ["INT_ADD", "register:40f0:8", ["const:bd1fb4:8", "const:4:8"]]
+ 00bd1fb4 ["CALLIND", null, ["register:0:8"]]
+ 00bd1fb4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e205337d6425e7449434c5734b6a7e20"></a>

### [`00bd2220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2220.md) → [`00bd22bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd2/00bd22bc.md) _ZN8firebase4auth31recent_login_required_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 40.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2278"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd2314"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2260"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd22d0",
      "READ",
      [
        "storage",
        "01126970",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bd2254",
      "READ",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd2278",
      "WRITE",
      [
        "storage",
        "01126970",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd22d0",
      "READ",
      [
        "storage",
        "01126a70",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd22f0",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2314",
      "WRITE",
      [
        "storage",
        "01126a70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2220.md#insn-00bd2260) · [`00bd2278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2220.md#insn-00bd2278)
- 新版 [`00bd22fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd2/00bd22bc.md#insn-00bd22fc)

~~~diff
- 00bd2260 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd2260 ["INT_ADD", "register:40f0:8", ["const:bd2260:8", "const:4:8"]]
- 00bd2260 ["CALLIND", null, ["register:0:8"]]
- 00bd2260 bytes 00013fd6
- 00bd2278 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd2278 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:970:8"]]
- 00bd2278 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd2278 bytes a0c22539
+ 00bd22fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd22fc ["INT_ADD", "register:40f0:8", ["const:bd22fc:8", "const:4:8"]]
+ 00bd22fc ["CALLIND", null, ["register:0:8"]]
+ 00bd22fc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d46696c24a0cebae256dad42994b8ecd"></a>

### [`00bd236c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd236c.md) → [`00bd2408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd2/00bd2408.md) _ZN8firebase4auth31recent_login_required_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bd2380"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd241c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd238c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd2380",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd2390"
      ]
    ],
    [
      "unmatched:00bd2388",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd238c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ],
  "added": [
    [
      "00bd241c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd242c"
      ]
    ],
    [
      "00bd2424",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bd2428",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd236c.md#insn-00bd2380) · [`00bd238c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd236c.md#insn-00bd238c) · [`00bd23a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd236c.md#insn-00bd23a4)

~~~diff
- 00bd2380 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd2380 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd2380 bytes 8b000054
- 00bd238c ["INT_ADD", "register:40f0:8", ["const:bd238c:8", "const:4:8"]]
- 00bd238c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd238c bytes 1d230294
- 00bd23a4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd23a4 ["RETURN", null, ["register:0:8"]]
- 00bd23a4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c73a72b36ac8349e7678c7a81e2a3c8b"></a>

### [`00bd24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd24d4.md) → [`00bd2570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd2/00bd2570.md) _ZN8firebase4auth24user_collision_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bd2504"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd25a0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd24e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd24e4",
      "READ",
      [
        "storage",
        "01126988",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd24e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd25a4"
      ]
    ],
    [
      "unmatched:00bd24f4",
      "PARAM",
      [
        "storage",
        "002a2cf7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd2580",
      "READ",
      [
        "storage",
        "01126a88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2584",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd25a4"
      ]
    ],
    [
      "00bd2590",
      "PARAM",
      [
        "storage",
        "002a2caa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd24e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd24d4.md#insn-00bd24e8) · [`00bd24fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd24d4.md#insn-00bd24fc) · [`00bd2504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd24d4.md#insn-00bd2504)

~~~diff
- 00bd24e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd24e8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd24e8 bytes 080100b5
- 00bd24fc ["INT_ADD", "register:40f0:8", ["const:bd24fc:8", "const:4:8"]]
- 00bd24fc ["CALL", null, ["callee:00c5afe0:8"]]
- 00bd24fc bytes 85220294
- 00bd2504 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00bd2504 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd2504 bytes 60c604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2201d8c3e809c7eee3f415686aa07ff"></a>

### [`00bd2aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2aa8.md) → [`00bd2b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd2/00bd2b44.md) _ZN8firebase4auth21android_web_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bd2ac8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd2b64"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2ae0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd2b58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd2acc"
      ]
    ],
    [
      "unmatched:00bd2ac4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd2ac8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ],
  "added": [
    [
      "00bd2b58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd2b68"
      ]
    ],
    [
      "00bd2b60",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bd2b64",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2aa8.md#insn-00bd2ac8) · [`00bd2ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2aa8.md#insn-00bd2ae0)
- 新版 [`00bd2b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd2/00bd2b44.md#insn-00bd2b64)

~~~diff
- 00bd2ac8 ["INT_ADD", "register:40f0:8", ["const:bd2ac8:8", "const:4:8"]]
- 00bd2ac8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd2ac8 bytes 4e210294
- 00bd2ae0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd2ae0 ["RETURN", null, ["register:0:8"]]
- 00bd2ae0 bytes c0035fd6
+ 00bd2b64 ["INT_ADD", "register:40f0:8", ["const:bd2b64:8", "const:4:8"]]
+ 00bd2b64 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd2b64 bytes 5b210294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f633375a1e8ea138f7ab91bf94b8e2b"></a>

### [`00bd2df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2df0.md) → [`00bd2e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd2/00bd2e8c.md) _ZN8firebase4auth23firebase_auth_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bd2e10"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd2eac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2e28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd2ea0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd2e14"
      ]
    ],
    [
      "unmatched:00bd2e0c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd2e10",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ],
  "added": [
    [
      "00bd2ea0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd2eb0"
      ]
    ],
    [
      "00bd2ea8",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bd2eac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2df0.md#insn-00bd2e10) · [`00bd2e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd2/00bd2df0.md#insn-00bd2e28)
- 新版 [`00bd2eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd2/00bd2e8c.md#insn-00bd2eac)

~~~diff
- 00bd2e10 ["INT_ADD", "register:40f0:8", ["const:bd2e10:8", "const:4:8"]]
- 00bd2e10 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd2e10 bytes 7c200294
- 00bd2e28 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd2e28 ["RETURN", null, ["register:0:8"]]
- 00bd2e28 bytes c0035fd6
+ 00bd2eac ["INT_ADD", "register:40f0:8", ["const:bd2eac:8", "const:4:8"]]
+ 00bd2eac ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd2eac bytes 89200294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-424f7bc9169d07267584a53c34db90f1"></a>

### [`00bd4678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4678.md) → [`00bd4714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd4714.md) _ZN8firebase4auth30CheckAndClearJniAuthExceptionsEP7_JNIEnvPNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd10.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5af50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af50.md) [`00c5dd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd80.md)
- 新版 呼出元 1件 [`00c5dde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dde0.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b020.md) [`00c5de50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 76.92% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd467c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4680"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4680"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd467c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd4680",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd4684",
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
      "00bd4718",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bd471c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd4720",
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

- 旧版 [`00bd467c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4678.md#insn-00bd467c) · [`00bd4680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4678.md#insn-00bd4680) · [`00bd4684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd4/00bd4678.md#insn-00bd4684)

~~~diff
- 00bd467c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00bd467c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00bd467c bytes f71300f9
- 00bd4680 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bd4680 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bd4680 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bd4680 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd4680 bytes f65703a9
- 00bd4684 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd4684 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd4684 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bd4684 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd4684 bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0b24af5ff926cc23acade7e2aafa8da"></a>

### [`00bd5248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5248.md) → [`00bd52e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd5/00bd52e4.md) _ZN8firebase4auth9emailcred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bd5278"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5314"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd525c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd5258",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd525c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd527c"
      ]
    ],
    [
      "unmatched:00bd5268",
      "PARAM",
      [
        "storage",
        "002ac3f3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd52f4",
      "READ",
      [
        "storage",
        "01126b68",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd52f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5318"
      ]
    ],
    [
      "00bd5304",
      "PARAM",
      [
        "storage",
        "002ac397",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd525c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5248.md#insn-00bd525c) · [`00bd5270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5248.md#insn-00bd5270) · [`00bd5278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5248.md#insn-00bd5278)

~~~diff
- 00bd525c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd525c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd525c bytes 080100b5
- 00bd5270 ["INT_ADD", "register:40f0:8", ["const:bd5270:8", "const:4:8"]]
- 00bd5270 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bd5270 bytes 28170294
- 00bd5278 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
- 00bd5278 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd5278 bytes 603605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cf049b13172b44dbec3b72081dadbec"></a>

### [`00bd52dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd52dc.md) → [`00bd5378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd5/00bd5378.md) _ZN8firebase4auth9emailcred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5334"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd53d0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd531c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd538c",
      "READ",
      [
        "storage",
        "01126a70",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd5398",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd5338"
      ]
    ],
    [
      "unmatched:00bd5310",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd538c",
      "READ",
      [
        "storage",
        "01126b70",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd5398",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd53d4"
      ]
    ],
    [
      "00bd53ac",
      "READ",
      [
        "storage",
        "01126b68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd531c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd52dc.md#insn-00bd531c) · [`00bd5334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd52dc.md#insn-00bd5334) · [`00bd5344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd52dc.md#insn-00bd5344)

~~~diff
- 00bd531c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd531c ["INT_ADD", "register:40f0:8", ["const:bd531c:8", "const:4:8"]]
- 00bd531c ["CALLIND", null, ["register:0:8"]]
- 00bd531c bytes 00013fd6
- 00bd5334 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd5334 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a70:8"]]
- 00bd5334 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd5334 bytes a0c22939
- 00bd5344 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd5344 ["RETURN", null, ["register:0:8"]]
- 00bd5344 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be58984067b53a11559af64bc9e76b42"></a>

### [`00bd5428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5428.md) → [`00bd54c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd5/00bd54c4.md) _ZN8firebase4auth9emailcred11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00bd5428"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd542c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
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
      "unmatched:00bd5428",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd542c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd54d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd544c"
      ]
    ]
  ],
  "added": [
    [
      "00bd54c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd54c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd54d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd54e8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5428.md#insn-00bd5428) · [`00bd542c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5428.md#insn-00bd542c) · [`00bd5448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5428.md#insn-00bd5448)

~~~diff
- 00bd5428 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd5428 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd5428 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd5428 bytes f30f1ef8
- 00bd542c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd542c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd542c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd542c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd542c bytes fd7b01a9
- 00bd5448 ["INT_ADD", "register:40f0:8", ["const:bd5448:8", "const:4:8"]]
- 00bd5448 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd5448 bytes ee160294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc298edb718ce9f03c13fb5bc7de9571"></a>

### [`00bd54d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd54d4.md) → [`00bd5570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd5/00bd5570.md) _ZN8firebase4auth9emailcred10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bd54d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd54d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd54d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd54d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd54d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd54e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd54f8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5570",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd5574",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd5584",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5594"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd54d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd54d4.md#insn-00bd54d4) · [`00bd54d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd54d4.md#insn-00bd54d8) · [`00bd54e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd54d4.md#insn-00bd54e8)

~~~diff
- 00bd54d4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd54d4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd54d4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd54d4 bytes f30f1ef8
- 00bd54d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd54d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd54d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd54d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd54d8 bytes fd7b01a9
- 00bd54e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd54e8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd54e8 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9863653baa40e5a8dc6f0a5060f1480c"></a>

### [`00bd5550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5550.md) → [`00bd55ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd5/00bd55ec.md) _ZN8firebase4auth12facebookcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bd5550"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5554"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5554"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd5550",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5554",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5560",
      "READ",
      [
        "storage",
        "01126a88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd55ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd55f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd55fc",
      "READ",
      [
        "storage",
        "01126b88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5550.md#insn-00bd5550) · [`00bd5554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5550.md#insn-00bd5554) · [`00bd5564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5550.md#insn-00bd5564)

~~~diff
- 00bd5550 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd5550 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd5550 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd5550 bytes f30f1ef8
- 00bd5554 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd5554 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd5554 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd5554 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd5554 bytes fd7b01a9
- 00bd5564 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd5564 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd5564 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4cdcfb39597a5b52a835bfbfe5e7de0"></a>

### [`00bd5590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5590.md) → [`00bd562c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd5/00bd562c.md) _ZN8firebase4auth12facebookcred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00bd55c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd565c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd55a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd55a0",
      "READ",
      [
        "storage",
        "01126a88",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd55a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd55c4"
      ]
    ],
    [
      "unmatched:00bd55b0",
      "PARAM",
      [
        "storage",
        "002bd499",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd563c",
      "READ",
      [
        "storage",
        "01126b88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5640",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5660"
      ]
    ],
    [
      "00bd564c",
      "PARAM",
      [
        "storage",
        "002bd445",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd55a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5590.md#insn-00bd55a4) · [`00bd55b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5590.md#insn-00bd55b8) · [`00bd55c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5590.md#insn-00bd55c0)

~~~diff
- 00bd55a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd55a4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd55a4 bytes 080100b5
- 00bd55b8 ["INT_ADD", "register:40f0:8", ["const:bd55b8:8", "const:4:8"]]
- 00bd55b8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bd55b8 bytes 56160294
- 00bd55c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a88:8"]]
- 00bd55c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd55c0 bytes 604605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2096cd630cf24e662639309f6d8a29a"></a>

### [`00bd5618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5618.md) → [`00bd56b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd5/00bd56b4.md) _ZN8firebase4auth12facebookcred8GetClassEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00bd5620"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bd56bc"
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
      "unmatched:00bd561c",
      "READ",
      [
        "storage",
        "01126a88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd56b8",
      "READ",
      [
        "storage",
        "01126b88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5618.md#insn-00bd5620) · [`00bd5618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5618.md#insn-00bd5618)
- 新版 [`00bd56bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd5/00bd56b4.md#insn-00bd56bc)

~~~diff
- 00bd5620 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd5620 ["RETURN", null, ["register:0:8"]]
- 00bd5620 bytes c0035fd6
+ 00bd56bc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bd56bc ["RETURN", null, ["register:0:8"]]
+ 00bd56bc bytes c0035fd6
- 00bd5618 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd5618 bytes 882a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e09ee1e2fbfce63fb684a4cdc8af059"></a>

### [`00bd5624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5624.md) → [`00bd56c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd5/00bd56c0.md) _ZN8firebase4auth12facebookcred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 42.86% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd567c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5718"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5664"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd56d4",
      "READ",
      [
        "storage",
        "01126a90",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bd5658",
      "READ",
      [
        "storage",
        "01126a88",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd567c",
      "WRITE",
      [
        "storage",
        "01126a90",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd56d4",
      "READ",
      [
        "storage",
        "01126b90",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd56f4",
      "READ",
      [
        "storage",
        "01126b88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5718",
      "WRITE",
      [
        "storage",
        "01126b90",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5624.md#insn-00bd5664) · [`00bd567c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5624.md#insn-00bd567c)
- 新版 [`00bd5700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd5/00bd56c0.md#insn-00bd5700)

~~~diff
- 00bd5664 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd5664 ["INT_ADD", "register:40f0:8", ["const:bd5664:8", "const:4:8"]]
- 00bd5664 ["CALLIND", null, ["register:0:8"]]
- 00bd5664 bytes 00013fd6
- 00bd567c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd567c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a90:8"]]
- 00bd567c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd567c bytes a0422a39
+ 00bd5700 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd5700 ["INT_ADD", "register:40f0:8", ["const:bd5700:8", "const:4:8"]]
+ 00bd5700 ["CALLIND", null, ["register:0:8"]]
+ 00bd5700 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad0c1b5c553607c72a60a52e2aece90b"></a>

### [`00bd5770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5770.md) → [`00bd580c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd5/00bd580c.md) _ZN8firebase4auth12facebookcred11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bd5790"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd582c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd57a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd5820",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd5794"
      ]
    ],
    [
      "unmatched:00bd578c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd5790",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ],
  "added": [
    [
      "00bd5820",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5830"
      ]
    ],
    [
      "00bd5828",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bd582c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5770.md#insn-00bd5790) · [`00bd57a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5770.md#insn-00bd57a8)
- 新版 [`00bd582c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd5/00bd580c.md#insn-00bd582c)

~~~diff
- 00bd5790 ["INT_ADD", "register:40f0:8", ["const:bd5790:8", "const:4:8"]]
- 00bd5790 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd5790 bytes 1c160294
- 00bd57a8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd57a8 ["RETURN", null, ["register:0:8"]]
- 00bd57a8 bytes c0035fd6
+ 00bd582c ["INT_ADD", "register:40f0:8", ["const:bd582c:8", "const:4:8"]]
+ 00bd582c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd582c bytes 29160294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bad1458df4218c5e27c3872f914fd46d"></a>

### [`00bd58d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd58d8.md) → [`00bd5974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd5/00bd5974.md) _ZN8firebase4auth10githubcred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bd5908"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd59a4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd58ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd58e8",
      "READ",
      [
        "storage",
        "01126aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd58ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd59a8"
      ]
    ],
    [
      "unmatched:00bd58f8",
      "PARAM",
      [
        "storage",
        "002c1de2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd5984",
      "READ",
      [
        "storage",
        "01126ba8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5988",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd59a8"
      ]
    ],
    [
      "00bd5994",
      "PARAM",
      [
        "storage",
        "002c1e22",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd58ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd58d8.md#insn-00bd58ec) · [`00bd5900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd58d8.md#insn-00bd5900) · [`00bd5908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd58d8.md#insn-00bd5908)

~~~diff
- 00bd58ec ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd58ec ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd58ec bytes 080100b5
- 00bd5900 ["INT_ADD", "register:40f0:8", ["const:bd5900:8", "const:4:8"]]
- 00bd5900 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bd5900 bytes 84150294
- 00bd5908 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
- 00bd5908 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd5908 bytes 605605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97cfc1b90cf12f9c57fbd1f87d52e96b"></a>

### [`00bd5ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5ba0.md) → [`00bd5c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd5/00bd5c3c.md) _ZN8firebase4auth10googlecred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00bd5bcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5c68"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5bb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd5bb0",
      "READ",
      [
        "storage",
        "01126ac8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd5bb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd5bd0"
      ]
    ],
    [
      "unmatched:00bd5bc0",
      "PARAM",
      [
        "storage",
        "002c1e12",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd5c4c",
      "READ",
      [
        "storage",
        "01126bc8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5c50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5c6c"
      ]
    ],
    [
      "00bd5c5c",
      "PARAM",
      [
        "storage",
        "002c1e52",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5ba0.md#insn-00bd5bb4) · [`00bd5bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5ba0.md#insn-00bd5bc4) · [`00bd5bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5ba0.md#insn-00bd5bcc)

~~~diff
- 00bd5bb4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd5bb4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd5bb4 bytes e80000b5
- 00bd5bc4 ["INT_ADD", "register:40f0:8", ["const:bd5bc4:8", "const:4:8"]]
- 00bd5bc4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bd5bc4 bytes d3140294
- 00bd5bcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ac8:8"]]
- 00bd5bcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd5bcc bytes 606605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7d1e97c1b52eafd709637c1d9f4f067"></a>

### [`00bd5e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5e00.md) → [`00bd5e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd5/00bd5e9c.md) _ZN8firebase4auth10googlecred11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

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
      "site": "00bd5e20"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd5ebc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5e38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd5eb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd5e24"
      ]
    ],
    [
      "unmatched:00bd5e1c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd5e20",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ],
  "added": [
    [
      "00bd5eb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5ec0"
      ]
    ],
    [
      "00bd5eb8",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bd5ebc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5e00.md#insn-00bd5e20) · [`00bd5e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd5/00bd5e00.md#insn-00bd5e38)
- 新版 [`00bd5ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd5/00bd5e9c.md#insn-00bd5ebc)

~~~diff
- 00bd5e20 ["INT_ADD", "register:40f0:8", ["const:bd5e20:8", "const:4:8"]]
- 00bd5e20 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd5e20 bytes 78140294
- 00bd5e38 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd5e38 ["RETURN", null, ["register:0:8"]]
- 00bd5e38 bytes c0035fd6
+ 00bd5ebc ["INT_ADD", "register:40f0:8", ["const:bd5ebc:8", "const:4:8"]]
+ 00bd5ebc ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd5ebc bytes 85140294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d8d44e981f3c4432a75a69d0bb2a89e"></a>

### [`00bd61f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd61f4.md) → [`00bd6290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6290.md) _ZN8firebase4auth13playgamescred10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bd6214"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd62b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd622c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd62a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd6218"
      ]
    ],
    [
      "unmatched:00bd6210",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd6214",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ],
  "added": [
    [
      "00bd62a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd62b4"
      ]
    ],
    [
      "00bd62ac",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bd62b0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd61f4.md#insn-00bd6214) · [`00bd622c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd61f4.md#insn-00bd622c)
- 新版 [`00bd62b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6290.md#insn-00bd62b0)

~~~diff
- 00bd6214 ["INT_ADD", "register:40f0:8", ["const:bd6214:8", "const:4:8"]]
- 00bd6214 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd6214 bytes 7b130294
- 00bd622c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd622c ["RETURN", null, ["register:0:8"]]
- 00bd622c bytes c0035fd6
+ 00bd62b0 ["INT_ADD", "register:40f0:8", ["const:bd62b0:8", "const:4:8"]]
+ 00bd62b0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd62b0 bytes 88130294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-855de853bca9a4460a5fe6bd49cc6545"></a>

### [`00bd6490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6490.md) → [`00bd652c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd652c.md) _ZN8firebase4auth11twittercred11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bd6490"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6494"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6494"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6490",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6494",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd64a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd64b4"
      ]
    ]
  ],
  "added": [
    [
      "00bd652c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd6530",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6540",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6550"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6490.md#insn-00bd6490) · [`00bd6494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6490.md#insn-00bd6494) · [`00bd64a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6490.md#insn-00bd64a4)

~~~diff
- 00bd6490 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd6490 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd6490 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd6490 bytes f30f1ef8
- 00bd6494 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd6494 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd6494 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd6494 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd6494 bytes fd7b01a9
- 00bd64a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd64a4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd64a4 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bee79a5c694cbbeb57395309c9a5fa84"></a>

### [`00bd653c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd653c.md) → [`00bd65d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd65d8.md) _ZN8firebase4auth11twittercred10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 26.67% / 新版 26.67%

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
      "site": "00bd653c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6540"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6540"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd653c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6540",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6550",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd6560"
      ]
    ]
  ],
  "added": [
    [
      "00bd65d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd65dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd65ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd65fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd653c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd653c.md#insn-00bd653c) · [`00bd6540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd653c.md#insn-00bd6540) · [`00bd6550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd653c.md#insn-00bd6550)

~~~diff
- 00bd653c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd653c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd653c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd653c bytes f30f1ef8
- 00bd6540 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd6540 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd6540 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd6540 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd6540 bytes fd7b01a9
- 00bd6550 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd6550 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bd6550 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b30aca19f4c30ff5de56a9b9d5ae89ed"></a>

### [`00bd6578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6578.md) → [`00bd6614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6614.md) _ZN8firebase4auth13oauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bd6578"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd657c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd657c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6578",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd657c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6588",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6614",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd6618",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6624",
      "READ",
      [
        "storage",
        "01126c28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6578.md#insn-00bd6578) · [`00bd657c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6578.md#insn-00bd657c) · [`00bd658c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6578.md#insn-00bd658c)

~~~diff
- 00bd6578 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd6578 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd6578 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd6578 bytes f30f1ef8
- 00bd657c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd657c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd657c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd657c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd657c bytes fd7b01a9
- 00bd658c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd658c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00bd658c bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5211e8e99799bf88f7d05f2441f6ae43"></a>

### [`00bd65b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd65b8.md) → [`00bd6654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6654.md) _ZN8firebase4auth13oauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bd65b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd65bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd65bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd65b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd65bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd65c8",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6654",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd6658",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6664",
      "READ",
      [
        "storage",
        "01126c28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd65b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd65b8.md#insn-00bd65b8) · [`00bd65bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd65b8.md#insn-00bd65bc) · [`00bd65cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd65b8.md#insn-00bd65cc)

~~~diff
- 00bd65b8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd65b8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd65b8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd65b8 bytes f30f1ef8
- 00bd65bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd65bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd65bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd65bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd65bc bytes fd7b01a9
- 00bd65cc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd65cc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00bd65cc bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7829793bb573dd2cfde7645d882f9b17"></a>

### [`00bd65f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd65f8.md) → [`00bd6694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6694.md) _ZN8firebase4auth13oauthprovider10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bd6628"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd66c4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd660c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd66a4",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd660c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd66c8"
      ]
    ],
    [
      "unmatched:00bd6618",
      "PARAM",
      [
        "storage",
        "002b9d48",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd66a4",
      "READ",
      [
        "storage",
        "01126c28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd66a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd66c8"
      ]
    ],
    [
      "00bd66b4",
      "PARAM",
      [
        "storage",
        "002b9cf4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd660c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd65f8.md#insn-00bd660c) · [`00bd6620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd65f8.md#insn-00bd6620) · [`00bd6628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd65f8.md#insn-00bd6628)

~~~diff
- 00bd660c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd660c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd660c bytes 080100b5
- 00bd6620 ["INT_ADD", "register:40f0:8", ["const:bd6620:8", "const:4:8"]]
- 00bd6620 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bd6620 bytes 3c120294
- 00bd6628 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b28:8"]]
- 00bd6628 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6628 bytes 609605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1f74ef082f528224fd45a61803c59aa"></a>

### [`00bd66f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd66f8.md) → [`00bd6794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6794.md) _ZN8firebase4auth13oauthprovider12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 6.67% / 新版 6.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6734"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6754"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd67d0"
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
      "unmatched:00bd670c",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd6710",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd67f4"
      ]
    ],
    [
      "00bd67b4",
      "READ",
      [
        "storage",
        "01126b30",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd67a8",
      "READ",
      [
        "storage",
        "01126c28",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd67ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd67f4"
      ]
    ],
    [
      "00bd67b4",
      "READ",
      [
        "storage",
        "01126c30",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd66f8.md#insn-00bd6710) · [`00bd6730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd66f8.md#insn-00bd6730) · [`00bd6734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd66f8.md#insn-00bd6734)

~~~diff
- 00bd6710 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd6710 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00bd6710 bytes 410200b4
- 00bd6730 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd6730 ["INT_ADD", "register:40f0:8", ["const:bd6730:8", "const:4:8"]]
- 00bd6730 ["CALLIND", null, ["register:0:8"]]
- 00bd6730 bytes 00013fd6
- 00bd6734 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd6734 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd6734 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b30:8"]]
- 00bd6734 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd6734 bytes bfc22c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bda70baed66ca6f880ac6082aa6796c"></a>

### [`00bd67d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd67d8.md) → [`00bd6874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6874.md) _ZN8firebase4auth13oauthprovider11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bd67ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd6888"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd67f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd67ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd67fc"
      ]
    ],
    [
      "unmatched:00bd67f4",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd67f8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ],
  "added": [
    [
      "00bd6888",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6898"
      ]
    ],
    [
      "00bd6890",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bd6894",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd67ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd67d8.md#insn-00bd67ec) · [`00bd67f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd67d8.md#insn-00bd67f8) · [`00bd6810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd67d8.md#insn-00bd6810)

~~~diff
- 00bd67ec ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd67ec ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd67ec bytes 8b000054
- 00bd67f8 ["INT_ADD", "register:40f0:8", ["const:bd67f8:8", "const:4:8"]]
- 00bd67f8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd67f8 bytes 02120294
- 00bd6810 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd6810 ["RETURN", null, ["register:0:8"]]
- 00bd6810 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1ef23bb9098b303a18ced4b8c809977"></a>

### [`00bd6884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6884.md) → [`00bd6920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6920.md) _ZN8firebase4auth13oauthprovider10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bd6884"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6888"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6888"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6884",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6888",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6898",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd68a8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6920",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd6924",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd6934",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6944"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6884.md#insn-00bd6884) · [`00bd6888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6884.md#insn-00bd6888) · [`00bd6898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6884.md#insn-00bd6898)

~~~diff
- 00bd6884 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd6884 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd6884 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd6884 bytes f30f1ef8
- 00bd6888 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd6888 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd6888 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd6888 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd6888 bytes fd7b01a9
- 00bd6898 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd6898 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd6898 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2400e4a888787b15c04f83d60ca1f58"></a>

### [`00bd6940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6940.md) → [`00bd69dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd69dc.md) _ZN8firebase4auth8timeunit10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bd6970"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd6a0c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6954"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6950",
      "READ",
      [
        "storage",
        "01126b58",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd6954",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd6974"
      ]
    ],
    [
      "unmatched:00bd6960",
      "PARAM",
      [
        "storage",
        "002b37ca",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd69ec",
      "READ",
      [
        "storage",
        "01126c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd69f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6a10"
      ]
    ],
    [
      "00bd69fc",
      "PARAM",
      [
        "storage",
        "002b37fb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6940.md#insn-00bd6954) · [`00bd6968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6940.md#insn-00bd6968) · [`00bd6970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6940.md#insn-00bd6970)

~~~diff
- 00bd6954 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd6954 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd6954 bytes 080100b5
- 00bd6968 ["INT_ADD", "register:40f0:8", ["const:bd6968:8", "const:4:8"]]
- 00bd6968 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bd6968 bytes 6a110294
- 00bd6970 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b58:8"]]
- 00bd6970 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd6970 bytes 60ae05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14fb2f0400ba3a78c8497a79d9ac886d"></a>

### [`00bd69c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd69c8.md) → [`00bd6a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6a64.md) _ZN8firebase4auth8timeunit8GetClassEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00bd69d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bd6a6c"
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
      "unmatched:00bd69cc",
      "READ",
      [
        "storage",
        "01126b58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd6a68",
      "READ",
      [
        "storage",
        "01126c58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd69d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd69c8.md#insn-00bd69d0) · [`00bd69c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd69c8.md#insn-00bd69c8)
- 新版 [`00bd6a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6a64.md#insn-00bd6a6c)

~~~diff
- 00bd69d0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd69d0 ["RETURN", null, ["register:0:8"]]
- 00bd69d0 bytes c0035fd6
+ 00bd6a6c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bd6a6c ["RETURN", null, ["register:0:8"]]
+ 00bd6a6c bytes c0035fd6
- 00bd69c8 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd69c8 bytes 882a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7b7281e4d9e316cb9816d13109e81d9"></a>

### [`00bd6f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6f14.md) → [`00bd6fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6fb0.md) _ZN8firebase4auth26phone_auth_options_builder10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

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
      "site": "00bd6f34"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd6fd0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6f4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6fc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd6f38"
      ]
    ],
    [
      "unmatched:00bd6f30",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd6f34",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ],
  "added": [
    [
      "00bd6fc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6fd4"
      ]
    ],
    [
      "00bd6fcc",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bd6fd0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6f14.md#insn-00bd6f34) · [`00bd6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6f14.md#insn-00bd6f4c)
- 新版 [`00bd6fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6fb0.md#insn-00bd6fd0)

~~~diff
- 00bd6f34 ["INT_ADD", "register:40f0:8", ["const:bd6f34:8", "const:4:8"]]
- 00bd6f34 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd6f34 bytes 33100294
- 00bd6f4c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd6f4c ["RETURN", null, ["register:0:8"]]
- 00bd6f4c bytes c0035fd6
+ 00bd6fd0 ["INT_ADD", "register:40f0:8", ["const:bd6fd0:8", "const:4:8"]]
+ 00bd6fd0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd6fd0 bytes 40100294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-048f6bab3b958558bf70fcbe06184b21"></a>

### [`00bd7b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7b88.md) → [`00bd7c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7c24.md) _ZN8firebase4auth8auth_idp11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bd7b88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7b8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7b8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd7b88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd7b8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd7c38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd7bac"
      ]
    ]
  ],
  "added": [
    [
      "00bd7c24",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd7c28",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd7c38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7c48"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7b88.md#insn-00bd7b88) · [`00bd7b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7b88.md#insn-00bd7b8c) · [`00bd7ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7b88.md#insn-00bd7ba8)

~~~diff
- 00bd7b88 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd7b88 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd7b88 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd7b88 bytes f30f1ef8
- 00bd7b8c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd7b8c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd7b8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd7b8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd7b8c bytes fd7b01a9
- 00bd7ba8 ["INT_ADD", "register:40f0:8", ["const:bd7ba8:8", "const:4:8"]]
- 00bd7ba8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd7ba8 bytes 160d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b98ff168c0a1574cfe2618a6cde73a5"></a>

### [`00bd7c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7c70.md) → [`00bd7d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7d0c.md) _ZN8firebase4auth8user_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bd7c9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd7d38"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7c84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7d1c",
      "READ",
      [
        "storage",
        "01126c88",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd7c84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7d3c"
      ]
    ],
    [
      "unmatched:00bd7c90",
      "PARAM",
      [
        "storage",
        "002a9887",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd7d1c",
      "READ",
      [
        "storage",
        "01126d88",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd7d20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7d3c"
      ]
    ],
    [
      "00bd7d2c",
      "PARAM",
      [
        "storage",
        "002a98b6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7c70.md#insn-00bd7c84) · [`00bd7c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7c70.md#insn-00bd7c94) · [`00bd7c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7c70.md#insn-00bd7c9c)

~~~diff
- 00bd7c84 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd7c84 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd7c84 bytes e80000b5
- 00bd7c94 ["INT_ADD", "register:40f0:8", ["const:bd7c94:8", "const:4:8"]]
- 00bd7c94 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bd7c94 bytes 9f0c0294
- 00bd7c9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
- 00bd7c9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd7c9c bytes 604606f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5f1b43ac7484e30277c9878b280bd9d"></a>

### [`00bd8038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8038.md) → [`00bd80d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd80d4.md) _ZN8firebase4auth8jniphone10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00bd8068"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd8104"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd804c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd8048",
      "READ",
      [
        "storage",
        "01126cb0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bd804c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd806c"
      ]
    ],
    [
      "unmatched:00bd8058",
      "PARAM",
      [
        "storage",
        "002b27b7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd80e4",
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd80e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd8108"
      ]
    ],
    [
      "00bd80f4",
      "PARAM",
      [
        "storage",
        "002b27e8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd804c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8038.md#insn-00bd804c) · [`00bd8060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8038.md#insn-00bd8060) · [`00bd8068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8038.md#insn-00bd8068)

~~~diff
- 00bd804c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd804c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd804c bytes 080100b5
- 00bd8060 ["INT_ADD", "register:40f0:8", ["const:bd8060:8", "const:4:8"]]
- 00bd8060 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bd8060 bytes ac0b0294
- 00bd8068 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cb0:8"]]
- 00bd8068 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd8068 bytes 605a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad60a0302e1663500a58ac12d9755362"></a>

### [`00bd80cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd80cc.md) → [`00bd8168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd8168.md) _ZN8firebase4auth8jniphone15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 call, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 62.96% / 新版 62.96%

CFGの説明率　旧版 14.29% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8124"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd81c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd810c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd817c",
      "READ",
      [
        "storage",
        "01126cb8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd8188",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd8128"
      ]
    ],
    [
      "unmatched:00bd8100",
      "READ",
      [
        "storage",
        "01126cb0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd817c",
      "READ",
      [
        "storage",
        "01126db8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd8188",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd81c4"
      ]
    ],
    [
      "00bd819c",
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd810c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd80cc.md#insn-00bd810c) · [`00bd8124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd80cc.md#insn-00bd8124) · [`00bd8134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd80cc.md#insn-00bd8134)

~~~diff
- 00bd810c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd810c ["INT_ADD", "register:40f0:8", ["const:bd810c:8", "const:4:8"]]
- 00bd810c ["CALLIND", null, ["register:0:8"]]
- 00bd810c bytes 00013fd6
- 00bd8124 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bd8124 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:cb8:8"]]
- 00bd8124 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd8124 bytes a0e23239
- 00bd8134 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd8134 ["RETURN", null, ["register:0:8"]]
- 00bd8134 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e76e8d186cb17bae39fb40cf490ef152"></a>

### [`00bd8218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8218.md) → [`00bd82b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd82b4.md) _ZN8firebase4auth8jniphone11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bd8238"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd82d4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8250"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd82c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd823c"
      ]
    ],
    [
      "unmatched:00bd8234",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd8238",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ],
  "added": [
    [
      "00bd82c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd82d8"
      ]
    ],
    [
      "00bd82d0",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bd82d4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd8238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8218.md#insn-00bd8238) · [`00bd8250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8218.md#insn-00bd8250)
- 新版 [`00bd82d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd82b4.md#insn-00bd82d4)

~~~diff
- 00bd8238 ["INT_ADD", "register:40f0:8", ["const:bd8238:8", "const:4:8"]]
- 00bd8238 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd8238 bytes 720b0294
- 00bd8250 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd8250 ["RETURN", null, ["register:0:8"]]
- 00bd8250 bytes c0035fd6
+ 00bd82d4 ["INT_ADD", "register:40f0:8", ["const:bd82d4:8", "const:4:8"]]
+ 00bd82d4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bd82d4 bytes 7f0b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4180af7b1a1f9a3f6dbcf41b07e819a6"></a>

### [`00bd82c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd82c4.md) → [`00bd8360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd8360.md) _ZN8firebase4auth8jniphone10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "site": "00bd82c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd82c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd82c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd82c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd82c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd8374",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd82e8"
      ]
    ]
  ],
  "added": [
    [
      "00bd8360",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd8364",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd8374",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd8384"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd82c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd82c4.md#insn-00bd82c4) · [`00bd82c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd82c4.md#insn-00bd82c8) · [`00bd82e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd82c4.md#insn-00bd82e4)

~~~diff
- 00bd82c4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd82c4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd82c4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd82c4 bytes f30f1ef8
- 00bd82c8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd82c8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd82c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd82c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd82c8 bytes fd7b01a9
- 00bd82e4 ["INT_ADD", "register:40f0:8", ["const:bd82e4:8", "const:4:8"]]
- 00bd82e4 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bd82e4 bytes 470b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ce59b07ecee2b6d5b0477b933f85296"></a>

### [`00bd8408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8408.md) → [`00bd84a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd84a4.md) _ZN8firebase4auth15phonecredential8GetClassEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5de10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de10.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5dee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dee0.md) · 呼出先 0件 

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
      "site": "00bd8410"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bd84ac"
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
      "unmatched:00bd840c",
      "READ",
      [
        "storage",
        "01126cd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd84a8",
      "READ",
      [
        "storage",
        "01126dd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd8410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8408.md#insn-00bd8410) · [`00bd8408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8408.md#insn-00bd8408)
- 新版 [`00bd84ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd84a4.md#insn-00bd84ac)

~~~diff
- 00bd8410 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd8410 ["RETURN", null, ["register:0:8"]]
- 00bd8410 bytes c0035fd6
+ 00bd84ac ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bd84ac ["RETURN", null, ["register:0:8"]]
+ 00bd84ac bytes c0035fd6
- 00bd8408 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd8408 bytes 682a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44b43bfa0369e5ff7e38589fedebb523"></a>

### [`00bd8414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8414.md) → [`00bd84b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd84b0.md) _ZN8firebase4auth15phonecredential15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 16.67% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8414"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8418"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8418"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd8414",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd8418",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd841c",
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
      "00bd84b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd84b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd84b8",
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

- 旧版 [`00bd8414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8414.md#insn-00bd8414) · [`00bd8418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8414.md#insn-00bd8418) · [`00bd841c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8414.md#insn-00bd841c)

~~~diff
- 00bd8414 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bd8414 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd8414 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd8414 bytes f50f1df8
- 00bd8418 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd8418 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd8418 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd8418 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd8418 bytes f44f01a9
- 00bd841c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd841c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd841c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd841c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd841c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f88f6c6cd42d16f76ce390092d4b2bb5"></a>

### [`00bdc5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc5fc.md) → [`00bdc698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc698.md) _ZN8firebase4auth10AuthResultC2ERKS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5ddf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5ddf0.md) · 呼出先 3件 [`00c5aa40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa40.md) [`00c5dd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dd60.md) [`00c5de20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5de20.md)
- 新版 呼出元 1件 [`00c5dec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dec0.md) · 呼出先 3件 [`00c5ab10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab10.md) [`00c5de30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de30.md) [`00c5def0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5def0.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.26% / 新版 78.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc628"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc62c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdc630"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc5fc.md#insn-00bdc628) · [`00bdc62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc5fc.md#insn-00bdc62c) · [`00bdc630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc5fc.md#insn-00bdc630)

~~~diff
- 00bdc628 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8:8"]]
- 00bdc628 ["COPY", "tmp:1:4", ["const:0:4"]]
- 00bdc628 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
- 00bdc628 bytes 9f0a00b9
- 00bdc62c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00bdc62c ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00bdc62c ["INT_ADD", "register:40b0:8", ["register:40b0:8", "const:10:8"]]
- 00bdc62c ["STORE", null, ["const:1b1:8", "register:40b0:8", "tmp:1:8"]]
- 00bdc62c bytes df0e01f8
- 00bdc630 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00bdc630 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bdc630 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00bdc630 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00bdc630 bytes 9ffe01a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bc02fe56f603ddcc378266d1ce08df8"></a>

### [`00bdd708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd708.md) → [`00bdd7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd7a4.md) _ZN8firebase4auth8userinfo11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 20.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdd728"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bdd7c4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdd740"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdd7b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bdd72c"
      ]
    ],
    [
      "unmatched:00bdd724",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bdd728",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ],
  "added": [
    [
      "00bdd7b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdd7c8"
      ]
    ],
    [
      "00bdd7c0",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bdd7c4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd708.md#insn-00bdd728) · [`00bdd740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd708.md#insn-00bdd740)
- 新版 [`00bdd7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd7a4.md#insn-00bdd7c4)

~~~diff
- 00bdd728 ["INT_ADD", "register:40f0:8", ["const:bdd728:8", "const:4:8"]]
- 00bdd728 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bdd728 bytes 36f60194
- 00bdd740 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bdd740 ["RETURN", null, ["register:0:8"]]
- 00bdd740 bytes c0035fd6
+ 00bdd7c4 ["INT_ADD", "register:40f0:8", ["const:bdd7c4:8", "const:4:8"]]
+ 00bdd7c4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bdd7c4 bytes 43f60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-065683a33e6f8508ce76a79ab7b47433"></a>

### [`00bdd904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd904.md) → [`00bdd9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd9a0.md) _ZN8firebase4auth8metadata15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

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
      "site": "00bdd95c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdd9f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdd96c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdd9b4",
      "READ",
      [
        "storage",
        "01126e08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd9c0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bdd960"
      ]
    ],
    [
      "unmatched:00bdd938",
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd9b4",
      "READ",
      [
        "storage",
        "01126f08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bdd9c0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdd9fc"
      ]
    ],
    [
      "00bdd9d4",
      "READ",
      [
        "storage",
        "01126f00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd904.md#insn-00bdd95c) · [`00bdd96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd904.md#insn-00bdd96c)
- 新版 [`00bdd9f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd9a0.md#insn-00bdd9f8)

~~~diff
- 00bdd95c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bdd95c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:e08:8"]]
- 00bdd95c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bdd95c bytes a0223839
- 00bdd96c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bdd96c ["RETURN", null, ["register:0:8"]]
- 00bdd96c bytes c0035fd6
+ 00bdd9f8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bdd9f8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:f08:8"]]
+ 00bdd9f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bdd9f8 bytes a0223c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b7c46a4bdb8cccc41c0848fbef12b09"></a>

### [`00bdf288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf288.md) → [`00bdf324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf324.md) _ZNSt6__ndk16vectorIN8firebase4auth17UserInfoInterfaceENS_9allocatorIS3_EEE7reserveEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ded0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5ded0.md) · 呼出先 4件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5dea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dea0.md)
- 新版 呼出元 1件 [`00c5dfa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfa0.md) · 呼出先 4件 [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5df70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df70.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 50.00% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdf288"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdf28c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdf28c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf288",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdf28c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdf290",
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
      "00bdf324",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bdf328",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bdf32c",
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

- 旧版 [`00bdf288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf288.md#insn-00bdf288) · [`00bdf28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf288.md#insn-00bdf28c) · [`00bdf290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf288.md#insn-00bdf290)

~~~diff
- 00bdf288 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00bdf288 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00bdf288 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bdf288 bytes f90f1bf8
- 00bdf28c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bdf28c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bdf28c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bdf28c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdf28c bytes f85f01a9
- 00bdf290 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bdf290 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bdf290 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bdf290 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdf290 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-087dc3fb32f29a993e55d4f3f208c271"></a>

### [`00bdf6ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf6ec.md) → [`00bdf788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf788.md) _ZN8firebase4auth22AndroidWrappedUserInfoD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md) [`00c5db80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5dc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc50.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

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
      "site": "00bdf70c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bdf7a8"
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
      "unmatched:00bdf700",
      "READ",
      [
        "storage",
        "00c9ba60",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf70c",
      "DATA",
      [
        "storage",
        "00c92910",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00bdf79c",
      "READ",
      [
        "storage",
        "00c9bb30",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf7a8",
      "DATA",
      [
        "storage",
        "00c929e0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf6ec.md#insn-00bdf70c) · [`00bdf700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf6ec.md#insn-00bdf700)
- 新版 [`00bdf7a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf788.md#insn-00bdf7a8)

~~~diff
- 00bdf70c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00bdf70c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bdf70c bytes 090000f9
+ 00bdf7a8 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00bdf7a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00bdf7a8 bytes 090000f9
- 00bdf700 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a60:8"]]
- 00bdf700 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf700 bytes 293145f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afd1bb913a4bda7af7e75baa8e9cb640"></a>

### [`00c30a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30a70.md) → [`00c30b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c30b0c.md) _ZNSt6__ndk118__time_get_storageIcE4initERKNS_5ctypeIcEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5ecf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ecf0.md) · 呼出先 4件 [`00bf1f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f98.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5e660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e660.md) [`00c5ecd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ecd0.md)
- 新版 呼出元 1件 [`00c5edc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5edc0.md) · 呼出先 4件 [`00bf2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2034.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e730.md) [`00c5eda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eda0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.94% / 新版 94.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c30b68",
      "PARAM",
      [
        "storage",
        "002b2801",
        null,
        null
      ]
    ],
    [
      "00c30b90",
      "PARAM",
      [
        "storage",
        "002ac51d",
        null,
        null
      ]
    ],
    [
      "00c30bdc",
      "PARAM",
      [
        "storage",
        "002af747",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c30b68",
      "PARAM",
      [
        "storage",
        "002b2832",
        null,
        null
      ]
    ],
    [
      "00c30b90",
      "PARAM",
      [
        "storage",
        "002ac4c1",
        null,
        null
      ]
    ],
    [
      "00c30bdc",
      "PARAM",
      [
        "storage",
        "002af6eb",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c30aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30a70.md#insn-00c30aa0) · [`00c30aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30a70.md#insn-00c30aa8) · [`00c30aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30a70.md#insn-00c30aac)
- 新版 [`00c30b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c30b0c.md#insn-00c30b3c) · [`00c30b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c30b0c.md#insn-00c30b48)

~~~diff
- 00c30aa0 ["COPY", "tmp:0:8", ["const:801:8"]]
- 00c30aa0 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00c30aa0 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00c30aa0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00c30b3c ["COPY", "tmp:0:8", ["const:832:8"]]
+ 00c30b3c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c30b3c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c30b3c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00c30aa0 bytes b5062091
+ 00c30b3c bytes b5ca2091
- 00c30aa8 ["COPY", "register:40b8:8", ["const:2ac000:8"]]
- 00c30aa8 bytes f7b3ff90
- 00c30aac ["COPY", "tmp:0:8", ["const:51d:8"]]
- 00c30aac ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 00c30aac ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 00c30aac ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 00c30b48 ["COPY", "tmp:0:8", ["const:4c1:8"]]
+ 00c30b48 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 00c30b48 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 00c30b48 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 00c30aac bytes f7761491
+ 00c30b48 bytes f7061391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67240dfd005d1a41c91811a090ef1464"></a>

### [`00c470e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c470e0.md) → [`00c4717c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c4717c.md) FUN_00c4717c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c471f4",
      "PARAM",
      [
        "storage",
        "002ae6fa",
        null,
        null
      ]
    ],
    [
      "00c471f4",
      "PARAM",
      [
        "storage",
        "0029eda0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c471f4",
      "PARAM",
      [
        "storage",
        "002ae69e",
        null,
        null
      ]
    ],
    [
      "00c471f4",
      "PARAM",
      [
        "storage",
        "0029ede0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c47130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c470e0.md#insn-00c47130) · [`00c47144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c470e0.md#insn-00c47144) · [`00c4714c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c470e0.md#insn-00c4714c)
- 新版 [`00c471cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c4717c.md#insn-00c471cc) · [`00c471e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c4717c.md#insn-00c471e0)

~~~diff
- 00c47130 ["INT_ADD", "register:40f0:8", ["const:c47130:8", "const:4:8"]]
- 00c47130 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c471cc ["INT_ADD", "register:40f0:8", ["const:c471cc:8", "const:4:8"]]
+ 00c471cc ["CALL", null, ["callee:00c5a170:8"]]
- 00c47130 bytes dc4b0094
+ 00c471cc bytes e94b0094
- 00c47144 ["COPY", "tmp:0:8", ["const:6fa:8"]]
- 00c47144 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c47144 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c47144 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c471e0 ["COPY", "tmp:0:8", ["const:69e:8"]]
+ 00c471e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c471e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c471e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c47144 bytes 29e91b91
+ 00c471e0 bytes 29791a91
- 00c4714c ["COPY", "register:4050:8", ["const:29e000:8"]]
- 00c4714c bytes aab2fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ce99b6d650339fdc941d269ce62e1bb"></a>

### [`00c5183c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c5183c.md) → [`00c518d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c518d8.md) FUN_00c518d8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c51b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51b74.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c51c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51c10.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c51aa4",
      "PARAM",
      [
        "storage",
        "002a99e2",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c51aa4",
      "PARAM",
      [
        "storage",
        "002a9a11",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c51868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c5183c.md#insn-00c51868) · [`00c51888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c5183c.md#insn-00c51888) · [`00c518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c5183c.md#insn-00c518b0)
- 新版 [`00c51904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c518d8.md#insn-00c51904) · [`00c51924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c518d8.md#insn-00c51924) · [`00c5194c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c518d8.md#insn-00c5194c)

~~~diff
- 00c51868 ["INT_ADD", "register:40f0:8", ["const:c51868:8", "const:4:8"]]
- 00c51868 ["CALL", null, ["callee:00c51c10:8"]]
+ 00c51904 ["INT_ADD", "register:40f0:8", ["const:c51904:8", "const:4:8"]]
+ 00c51904 ["CALL", null, ["callee:00c51c10:8"]]
- 00c51868 bytes c3000094
+ 00c51904 bytes c3000094
- 00c51888 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51888 ["INT_ADD", "register:40f0:8", ["const:c51888:8", "const:4:8"]]
- 00c51888 ["CALLIND", null, ["register:0:8"]]
+ 00c51924 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51924 ["INT_ADD", "register:40f0:8", ["const:c51924:8", "const:4:8"]]
+ 00c51924 ["CALLIND", null, ["register:0:8"]]
- 00c51888 bytes 00013fd6
+ 00c51924 bytes 00013fd6
- 00c518b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c518b0 ["INT_ADD", "register:40f0:8", ["const:c518b0:8", "const:4:8"]]
- 00c518b0 ["CALLIND", null, ["register:0:8"]]
+ 00c5194c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c5194c ["INT_ADD", "register:40f0:8", ["const:c5194c:8", "const:4:8"]]
+ 00c5194c ["CALLIND", null, ["register:0:8"]]
- 00c518b0 bytes 00013fd6
+ 00c5194c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

