# v16.0.1 → v16.0.2 · 命令位置の検査未完了 (9)

[一覧の目次](README.md)

<a id="compare-febd758ad8ac34a23bfd158ed5456237"></a>

### [`00b55180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55180.md) → [`00b5521c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b5521c.md) _ZN8firebase4util20JFloatArrayToVariantEP7_JNIEnvP12_jfloatArray

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b450.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5b520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b520.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.82% / 新版 90.82%

CFGの説明率　旧版 50.00% / 新版 56.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55184"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55188"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5518c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55184",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55188",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5518c",
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
      "00b55220",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b55224",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b55228",
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

- 旧版 [`00b55184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55180.md#insn-00b55184) · [`00b55188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55180.md#insn-00b55188) · [`00b5518c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55180.md#insn-00b5518c)

~~~diff
- 00b55184 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b55184 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 00b55184 bytes e81300fd
- 00b55188 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b55188 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b55188 bytes fb1700f9
- 00b5518c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b5518c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b5518c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b5518c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5518c bytes fa6703a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d36ed1b468dc53045fffa002548ac67"></a>

### [`00b55a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55a10.md) → [`00b55aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55aac.md) _ZN8firebase4util25ByteBufferToJavaByteArrayEP7_JNIEnvPKhm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 72.00% / 新版 72.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55a5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b55af8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55a70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b55a5c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b55af8",
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

- 旧版 [`00b55a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55a10.md#insn-00b55a5c) · [`00b55a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55a10.md#insn-00b55a70)
- 新版 [`00b55af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55aac.md#insn-00b55af8)

~~~diff
- 00b55a5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55a5c ["INT_ADD", "register:40f0:8", ["const:b55a5c:8", "const:4:8"]]
- 00b55a5c ["CALLIND", null, ["register:0:8"]]
- 00b55a5c bytes 00013fd6
- 00b55a70 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b55a70 ["RETURN", null, ["register:0:8"]]
- 00b55a70 bytes c0035fd6
+ 00b55af8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b55af8 ["INT_ADD", "register:40f0:8", ["const:b55af8:8", "const:4:8"]]
+ 00b55af8 ["CALLIND", null, ["register:0:8"]]
+ 00b55af8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-369e4a3b868df65d892e3ec16623de2d"></a>

### [`00b55e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55e1c.md) → [`00b55eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55eb8.md) _ZN8firebase4util22LocalToGlobalReferenceEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_count, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.61% / 新版 82.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55e28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55e28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b55ec4"
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
      "unmatched:00b55e28",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55e58",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b55ec4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b55ef4",
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

- 旧版 [`00b55e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55e1c.md#insn-00b55e28) · [`00b55e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55e1c.md#insn-00b55e58)
- 新版 [`00b55ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55eb8.md#insn-00b55ec4)

~~~diff
- 00b55e28 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b55e28 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b55e28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b55e28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b55e28 bytes fd7b02a9
- 00b55e58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55e58 ["INT_ADD", "register:40f0:8", ["const:b55e58:8", "const:4:8"]]
- 00b55e58 ["CALLIND", null, ["register:0:8"]]
- 00b55e58 bytes 00013fd6
+ 00b55ec4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00b55ec4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00b55ec4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
+ 00b55ec4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b55ec4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f611ae7e3aa5b2d1ff2d15ad173cf50"></a>

### [`00b55e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55e78.md) → [`00b55f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55f14.md) _ZN8firebase4util15ContinueBuilderEP7_JNIEnvP8_jobjectS4_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_call_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b55e90"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b55f2c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00b55e98",
      "incomplete_value": true,
      "site": "00b55ea0",
      "value": [
        "live",
        "register:4098:8"
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
      "unmatched:00b55e94",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b55e90",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b55f30",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b55f2c",
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

- 旧版 [`00b55e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55e78.md#insn-00b55e90) · [`00b55e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b55/00b55e78.md#insn-00b55e94)
- 新版 [`00b55f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b55/00b55f14.md#insn-00b55f2c)

~~~diff
- 00b55e90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b55e90 ["INT_ADD", "register:40f0:8", ["const:b55e90:8", "const:4:8"]]
- 00b55e90 ["CALLIND", null, ["register:0:8"]]
- 00b55e90 bytes 00013fd6
+ 00b55f2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b55f2c ["INT_ADD", "register:40f0:8", ["const:b55f2c:8", "const:4:8"]]
+ 00b55f2c ["CALLIND", null, ["register:0:8"]]
+ 00b55f2c bytes 00013fd6
- 00b55e94 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b55e94 ["LOAD", "tmp:1:8", ["const:1b1:8", "tmp:0:8"]]
- 00b55e94 ["INT_ADD", "tmp:2:8", ["tmp:0:8", "const:8:8"]]
- 00b55e94 ["LOAD", "tmp:3:8", ["const:1b1:8", "tmp:2:8"]]
- 00b55e94 bytes fd7b41a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81d69f0e35b08666f2411392445551bd"></a>

### [`00b578a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b578a0.md) → [`00b5793c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b5793c.md) DetachJVMThreads

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b57918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57918.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00b579b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b579b4.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b578f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5798c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b57900"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b578f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b579a0"
      ]
    ],
    [
      "unmatched:00b578f4",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b578f8",
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
      "00b5798c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b579a0"
      ]
    ],
    [
      "00b57990",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b57994",
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

- 旧版 [`00b578f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b578a0.md#insn-00b578f0) · [`00b57900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b578a0.md#insn-00b57900)
- 新版 [`00b5798c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b5793c.md#insn-00b5798c)

~~~diff
- 00b578f0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b578f0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b578f0 bytes a1000054
- 00b57900 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b57900 ["RETURN", null, ["register:0:8"]]
- 00b57900 bytes c0035fd6
+ 00b5798c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b5798c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b5798c bytes a1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ce94c6ead5bb985cebdbfa44aae197f"></a>

### [`00b57918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57918.md) → [`00b579b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b579b4.md) SetupJvmDetachOnThreadDestruction

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b5792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b5792c.md) · 呼出先 2件 [`00b578a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b578a0.md) [`00c5a300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a300.md)
- 新版 呼出元 1件 [`00b579c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b579c8.md) · 呼出先 2件 [`00b5793c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b5793c.md) [`00c5a3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3d0.md)

変更の種類 constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 40.00% / 新版 40.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b57920",
      "READ",
      [
        "storage",
        "00c9b730",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b57920",
      "PARAM",
      [
        "storage",
        "01125fb4",
        "_ZN8firebase4util11jni_env_keyE",
        "undefined4"
      ]
    ],
    [
      "unmatched:00b57924",
      "READ",
      [
        "storage",
        "00c9b708",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b579bc",
      "READ",
      [
        "storage",
        "00c9b800",
        null,
        "pointer"
      ]
    ],
    [
      "00b579bc",
      "PARAM",
      [
        "storage",
        "011260b4",
        "_ZN8firebase4util11jni_env_keyE",
        "undefined4"
      ]
    ],
    [
      "00b579c0",
      "READ",
      [
        "storage",
        "00c9b7d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57918.md#insn-00b5791c) · [`00b57920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57918.md#insn-00b57920) · [`00b57924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57918.md#insn-00b57924)

~~~diff
- 00b5791c ["COPY", "register:4008:8", ["const:c9b000:8"]]
- 00b5791c bytes 210a0090
- 00b57920 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:730:8"]]
- 00b57920 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b57920 bytes 009843f9
- 00b57924 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:708:8"]]
- 00b57924 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b57924 bytes 218443f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-824f34bf82cd67eaaba3bd61f31f493b"></a>

### [`00b57cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57cb8.md) → [`00b57d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57d54.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

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
      "site": "00b57cf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b57d94"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b57dbc",
      "incomplete_value": true,
      "site": "00b57dc0",
      "value": [
        "INT_AND",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:fffffffffffffff0:8"
          ]
        ]
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
      "unmatched:00b57cf8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57df8"
      ]
    ]
  ],
  "added": [
    [
      "00b57d94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b57df8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b57cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57cb8.md#insn-00b57cf8) · [`00b57d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b57/00b57cb8.md#insn-00b57d24)
- 新版 [`00b57dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57d54.md#insn-00b57dc0) · [`00b57d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b57/00b57d54.md#insn-00b57d94)

~~~diff
- 00b57cf8 ["CBRANCH", null, ["local:b13:8", "register:102:1"]]
- 00b57cf8 bytes 22030054
- 00b57d24 ["INT_ADD", "register:40f0:8", ["const:b57d24:8", "const:4:8"]]
- 00b57d24 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b57dc0 ["INT_ADD", "register:40f0:8", ["const:b57dc0:8", "const:4:8"]]
+ 00b57dc0 ["CALL", null, ["callee:00c57f60:8"]]
- 00b57d24 bytes 5b000494
+ 00b57dc0 bytes 68000494
+ 00b57d94 ["CBRANCH", null, ["local:b13:8", "register:102:1"]]
+ 00b57d94 bytes 22030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac5f477cd7c2f1a1252f6d41c7e6c0c4"></a>

### [`00b58af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58af0.md) → [`00b58b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58b8c.md) _ZN8firebase8internal16JObjectReferenceC1EP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5b190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b190.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c5b260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b260.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "site": "00b58b40"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b58bdc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b58bac",
      "incomplete_value": true,
      "site": "00b58bc4",
      "value": [
        "live",
        "register:4040:8"
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
      "unmatched:00b58b40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58bf0"
      ]
    ]
  ],
  "added": [
    [
      "00b58bdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58bf0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58af0.md#insn-00b58b28) · [`00b58b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58af0.md#insn-00b58b40)
- 新版 [`00b58bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58b8c.md#insn-00b58bc4) · [`00b58bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58b8c.md#insn-00b58bdc)

~~~diff
- 00b58b28 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b58b28 ["INT_ADD", "register:40f0:8", ["const:b58b28:8", "const:4:8"]]
- 00b58b28 ["CALLIND", null, ["register:0:8"]]
+ 00b58bc4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b58bc4 ["INT_ADD", "register:40f0:8", ["const:b58bc4:8", "const:4:8"]]
+ 00b58bc4 ["CALLIND", null, ["register:0:8"]]
- 00b58b28 bytes 20013fd6
+ 00b58bc4 bytes 20013fd6
- 00b58b40 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b58b40 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b58b40 bytes a1000054
+ 00b58bdc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b58bdc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b58bdc bytes a1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64bf8850f70070a03361f820d8c13e93"></a>

### [`00b58b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58b58.md) → [`00b58bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58bf4.md) _ZN8firebase8internal16JObjectReference9GetJavaVMEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58b5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58b60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58b60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b58b5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58b60",
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
      "00b58bf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b58bfc",
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

- 旧版 [`00b58b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58b58.md#insn-00b58b5c) · [`00b58b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58b58.md#insn-00b58b60)
- 新版 [`00b58bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58bf4.md#insn-00b58bf8)

~~~diff
- 00b58b5c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b58b5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b58b5c bytes f30b00f9
- 00b58b60 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b58b60 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b58b60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b58b60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58b60 bytes fd7b02a9
+ 00b58bf8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 00b58bf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00b58bf8 bytes f30b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ecd14d27753eb44387ef4b54f268af3"></a>

### [`00b58bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58bb0.md) → [`00b58c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58c4c.md) _ZN8firebase8internal16JObjectReferenceC2EP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 80.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58c38"
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

- 旧版 [`00b58c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58bb0.md#insn-00b58c38) · [`00b58bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58bb0.md#insn-00b58bf0)
- 新版 [`00b58cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58c4c.md#insn-00b58cd4) · [`00b58c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58c4c.md#insn-00b58c8c)

~~~diff
- 00b58c38 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b58c38 ["RETURN", null, ["register:0:8"]]
- 00b58c38 bytes c0035fd6
+ 00b58cd4 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b58cd4 ["RETURN", null, ["register:0:8"]]
+ 00b58cd4 bytes c0035fd6
- 00b58bf0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58bf0 ["INT_ADD", "register:40f0:8", ["const:b58bf0:8", "const:4:8"]]
- 00b58bf0 ["CALLIND", null, ["register:0:8"]]
+ 00b58c8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b58c8c ["INT_ADD", "register:40f0:8", ["const:b58c8c:8", "const:4:8"]]
+ 00b58c8c ["CALLIND", null, ["register:0:8"]]
- 00b58bf0 bytes 00013fd6
+ 00b58c8c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c34c5ec71fd2360a8033aa5fd6bebeb"></a>

### [`00b58c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58c40.md) → [`00b58cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58cdc.md) _ZN8firebase8internal16JObjectReference10InitializeEP7_JavaVMP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58c68"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b58d04"
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
      "unmatched:00b58c68",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b58d04",
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

- 旧版 [`00b58c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58c40.md#insn-00b58c68) · [`00b58c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58c40.md#insn-00b58c64)
- 新版 [`00b58d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58cdc.md#insn-00b58d04)

~~~diff
- 00b58c68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58c68 ["INT_ADD", "register:40f0:8", ["const:b58c68:8", "const:4:8"]]
- 00b58c68 ["CALLIND", null, ["register:0:8"]]
- 00b58c68 bytes 00013fd6
+ 00b58d04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b58d04 ["INT_ADD", "register:40f0:8", ["const:b58d04:8", "const:4:8"]]
+ 00b58d04 ["CALLIND", null, ["register:0:8"]]
+ 00b58d04 bytes 00013fd6
- 00b58c64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a8:8"]]
- 00b58c64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b58c64 bytes 085540f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2de13e0e23a3b24d14d1a0fb3d4dcfe"></a>

### [`00b58c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58c7c.md) → [`00b58d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58d18.md) _ZN8firebase8internal16JObjectReferenceC2ERKS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1a0.md) · 呼出先 1件 [`00c5b3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3c0.md)
- 新版 呼出元 1件 [`00c5b270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b270.md) · 呼出先 1件 [`00c5b490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b490.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.61% / 新版 82.61%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58c7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58c80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58c80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b58c7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58c80",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58c84",
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
      "00b58d18",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b58d1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b58d20",
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

- 旧版 [`00b58c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58c7c.md#insn-00b58c7c) · [`00b58c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58c7c.md#insn-00b58c80) · [`00b58c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58c7c.md#insn-00b58c84)

~~~diff
- 00b58c7c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b58c7c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b58c7c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b58c7c bytes f50f1df8
- 00b58c80 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b58c80 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b58c80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b58c80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58c80 bytes f44f01a9
- 00b58c84 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b58c84 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b58c84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b58c84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58c84 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5950ed18f7c75426f7545fe6ade961e"></a>

### [`00b58d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58d08.md) → [`00b58da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58da4.md) _ZN8firebase8internal16JObjectReferenceD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00c5b1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1b0.md) [`00c5b1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1c0.md) · 呼出先 1件 [`00c5b3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3c0.md)
- 新版 呼出元 2件 [`00c5b280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b280.md) [`00c5b290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b290.md) · 呼出先 1件 [`00c5b490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b490.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58d38"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b58dd4"
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
      "unmatched:00b58d38",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b58dd4",
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

- 旧版 [`00b58d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58d08.md#insn-00b58d38) · [`00b58d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58d08.md#insn-00b58d1c)
- 新版 [`00b58dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58da4.md#insn-00b58dd4) · [`00b58db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58da4.md#insn-00b58db8)

~~~diff
- 00b58d38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58d38 ["INT_ADD", "register:40f0:8", ["const:b58d38:8", "const:4:8"]]
- 00b58d38 ["CALLIND", null, ["register:0:8"]]
- 00b58d38 bytes 00013fd6
+ 00b58dd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b58dd4 ["INT_ADD", "register:40f0:8", ["const:b58dd4:8", "const:4:8"]]
+ 00b58dd4 ["CALLIND", null, ["register:0:8"]]
+ 00b58dd4 bytes 00013fd6
- 00b58d1c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b58d1c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b58db8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b58db8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b58d1c bytes 000100b4
+ 00b58db8 bytes 000100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4361535d08693ac04b7721066bff99ab"></a>

### [`00b58d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58d4c.md) → [`00b58de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58de8.md) _ZN8firebase8internal16JObjectReference3SetEP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b180.md) · 呼出先 1件 [`00c5b3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3c0.md)
- 新版 呼出元 1件 [`00c5b250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b250.md) · 呼出先 1件 [`00c5b490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b490.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 25.00% / 新版 26.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58d4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58d50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58d50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b58d4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58d50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58d54",
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
      "00b58de8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b58dec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b58df0",
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

- 旧版 [`00b58d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58d4c.md#insn-00b58d4c) · [`00b58d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58d4c.md#insn-00b58d50) · [`00b58d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58d4c.md#insn-00b58d54)

~~~diff
- 00b58d4c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b58d4c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b58d4c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b58d4c bytes f50f1df8
- 00b58d50 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b58d50 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b58d50 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b58d50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58d50 bytes f44f01a9
- 00b58d54 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b58d54 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b58d54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b58d54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58d54 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bce047cefbd6d690c41d6795927896e7"></a>

### [`00b58ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58ea4.md) → [`00b58f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58f40.md) _ZN8firebase8internal16JObjectReference3SetEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.55% / 新版 79.55%

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
      "site": "00b58ecc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b58f68"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58f38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b58ecc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58f38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58fec"
      ]
    ],
    [
      "unmatched:00b58ee8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b58f68",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b58fd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b58fec"
      ]
    ],
    [
      "00b58f84",
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

- 旧版 [`00b58ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58ea4.md#insn-00b58ecc) · [`00b58ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58ea4.md#insn-00b58ee8) · [`00b58f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58ea4.md#insn-00b58f38)

~~~diff
- 00b58ecc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b58ecc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b58ecc bytes e80700f9
- 00b58ee8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58ee8 ["INT_ADD", "register:40f0:8", ["const:b58ee8:8", "const:4:8"]]
- 00b58ee8 ["CALLIND", null, ["register:0:8"]]
- 00b58ee8 bytes 00013fd6
- 00b58f38 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b58f38 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b58f38 bytes c1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2616efb6e60d2f63d61f473b3f75d95"></a>

### [`00b58f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58f54.md) → [`00b58ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58ff0.md) _ZNK8firebase8internal16JObjectReference11GetLocalRefEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1d0.md) · 呼出先 1件 [`00c5b3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3c0.md)
- 新版 呼出元 1件 [`00c5b2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b2a0.md) · 呼出先 1件 [`00c5b490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b490.md)

変更の種類 constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 42.86% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b58f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58f54.md#insn-00b58f6c) · [`00b58f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58f54.md#insn-00b58f84) · [`00b58f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58f54.md#insn-00b58f88)
- 新版 [`00b59008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58ff0.md#insn-00b59008)

~~~diff
- 00b58f6c ["INT_ADD", "register:40f0:8", ["const:b58f6c:8", "const:4:8"]]
- 00b58f6c ["CALL", null, ["callee:00c5b490:8"]]
+ 00b59008 ["INT_ADD", "register:40f0:8", ["const:b59008:8", "const:4:8"]]
+ 00b59008 ["CALL", null, ["callee:00c5b490:8"]]
- 00b58f6c bytes 15090494
+ 00b59008 bytes 22090494
- 00b58f84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c8:8"]]
- 00b58f84 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b58f84 bytes 026540f9
- 00b58f88 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b58f88 ["INT_ADD", "register:8:8", ["register:8:8", "const:20:8"]]
- 00b58f88 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00b58f88 bytes f30742f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38ecd69109fb2dac3f1dc854b15fc395"></a>

### [`00b58fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58fa0.md) → [`00b5903c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b59/00b5903c.md) _ZN8firebase8internal16JObjectReference18FromLocalReferenceEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b170.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c5b240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b240.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.50% / 新版 77.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58fa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58fa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b58fa8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b58fa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b58fa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b59024",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b590d8"
      ]
    ]
  ],
  "added": [
    [
      "00b59040",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b59044",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b590c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b590d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58fa0.md#insn-00b58fa4) · [`00b58fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58fa0.md#insn-00b58fa8) · [`00b58fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b58/00b58fa0.md#insn-00b58fdc)

~~~diff
- 00b58fa4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b58fa4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b58fa4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b58fa4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58fa4 bytes f65701a9
- 00b58fa8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b58fa8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b58fa8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b58fa8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b58fa8 bytes f44f02a9
- 00b58fdc ["COPY", "register:0:8", ["register:4048:8"]]
- 00b58fdc ["INT_ADD", "register:40f0:8", ["const:b58fdc:8", "const:4:8"]]
- 00b58fdc ["CALLIND", null, ["register:0:8"]]
- 00b58fdc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2c11cb2c1f76eea13e7de204035a7f2"></a>

### [`00b5a0d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5a0d8.md) → [`00b5a174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5a174.md) _ZN8firebase10app_common15LibraryRegistry15UpdateUserAgentEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b710.md) · 呼出先 5件 [`00b5abb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5abb4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c5b7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b7f0.md)
- 新版 呼出元 1件 [`00c5b7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b7e0.md) · 呼出先 5件 [`00b5ac50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ac50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c5b8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b8c0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 43.10% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a1c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5a260"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5a130"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5a130",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5a320"
      ]
    ],
    [
      "unmatched:00b5a14c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5a1f8"
      ]
    ],
    [
      "unmatched:00b5a158",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5a320"
      ]
    ]
  ],
  "added": [
    [
      "00b5a1cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5a320"
      ]
    ],
    [
      "00b5a1e8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5a1f8"
      ]
    ],
    [
      "00b5a1f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5a320"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5a0d8.md#insn-00b5a130) · [`00b5a158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5a0d8.md#insn-00b5a158) · [`00b5a184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5a0d8.md#insn-00b5a184)

~~~diff
- 00b5a130 ["CBRANCH", null, ["local:b24:8", "register:101:1"]]
- 00b5a130 bytes a00a0054
- 00b5a158 ["CBRANCH", null, ["local:b24:8", "register:101:1"]]
- 00b5a158 bytes 60090054
- 00b5a184 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b5a184 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b5a184 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b5a184 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b5a184 bytes 61018a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ead82e5d828a32c28ddbb33ad5e4f9c7"></a>

### [`00b5b37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b37c.md) → [`00b5b418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b418.md) _ZNK8firebase10LoggerBase7LogInfoEPKcz

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 57.69% / 新版 57.69%

CFGの説明率　旧版 37.50% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 25件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b380"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b380"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b384"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5b380",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5b384",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5b388",
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
      "00b5b41c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5b420",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5b424",
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

- 旧版 [`00b5b380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b37c.md#insn-00b5b380) · [`00b5b384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b37c.md#insn-00b5b384) · [`00b5b388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b37c.md#insn-00b5b388)

~~~diff
- 00b5b380 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b5b380 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5b380 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00b5b380 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b380 bytes fc5712a9
- 00b5b384 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5b384 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5b384 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00b5b384 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b384 bytes f44f13a9
- 00b5b388 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5b388 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5b388 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00b5b388 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b388 bytes fd7b14a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84307abaedeb86510822741452b058f8"></a>

### [`00b5b44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b44c.md) → [`00b5b4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b4e8.md) _ZNK8firebase10LoggerBase10LogWarningEPKcz

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 65.38% / 新版 65.38%

CFGの説明率　旧版 13.33% / 新版 11.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b450"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b450"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b454"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5b450",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5b454",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5b458",
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
      "00b5b4ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5b4f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5b4f4",
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

- 旧版 [`00b5b450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b44c.md#insn-00b5b450) · [`00b5b454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b44c.md#insn-00b5b454) · [`00b5b458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b44c.md#insn-00b5b458)

~~~diff
- 00b5b450 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b5b450 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5b450 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00b5b450 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b450 bytes fc5712a9
- 00b5b454 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5b454 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5b454 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00b5b454 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b454 bytes f44f13a9
- 00b5b458 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5b458 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5b458 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00b5b458 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b458 bytes fd7b14a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7f11f5ecae6df27ccad8cd9ed154615"></a>

### [`00b5b51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b51c.md) → [`00b5b5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b5b8.md) _ZNK8firebase10LoggerBase8LogErrorEPKcz

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 46.15% / 新版 46.15%

CFGの説明率　旧版 37.50% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 27件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b520"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b520"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5b524"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5b520",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5b524",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5b528",
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
      "00b5b5bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5b5c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5b5c4",
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

- 旧版 [`00b5b520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b51c.md#insn-00b5b520) · [`00b5b524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b51c.md#insn-00b5b524) · [`00b5b528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5b51c.md#insn-00b5b528)

~~~diff
- 00b5b520 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b5b520 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5b520 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00b5b520 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b520 bytes fc5712a9
- 00b5b524 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5b524 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5b524 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00b5b524 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b524 bytes f44f13a9
- 00b5b528 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5b528 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5b528 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00b5b528 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5b528 bytes fd7b14a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9cc09c8e90c69c3969c570210348013"></a>

### [`00b5c3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c3f4.md) → [`00b5c490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c490.md) _ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEED2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 67.74% / 新版 67.74%

CFGの説明率　旧版 25.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c3f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c3f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c3f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5c3f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c3f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c3fc",
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
      "00b5c490",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5c494",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5c498",
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

- 旧版 [`00b5c3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c3f4.md#insn-00b5c3f4) · [`00b5c3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c3f4.md#insn-00b5c3f8) · [`00b5c3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c3f4.md#insn-00b5c3fc)

~~~diff
- 00b5c3f4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b5c3f4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b5c3f4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5c3f4 bytes f50f1df8
- 00b5c3f8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5c3f8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5c3f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5c3f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c3f8 bytes f44f01a9
- 00b5c3fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5c3fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5c3fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5c3fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c3fc bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15b1d5815b76fb99cbe62edac8151de3"></a>

### [`00b5c4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c4f4.md) → [`00b5c590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c590.md) _ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEE16__on_zero_sharedEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b5bcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5b/00b5bcac.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00b5bd48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bd48.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 74.07% / 新版 74.07%

CFGの説明率　旧版 12.50% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c4f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c4f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c4f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5c4f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c4f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c4fc",
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
      "00b5c590",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5c594",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5c598",
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

- 旧版 [`00b5c4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c4f4.md#insn-00b5c4f4) · [`00b5c4f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c4f4.md#insn-00b5c4f8) · [`00b5c4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c4f4.md#insn-00b5c4fc)

~~~diff
- 00b5c4f4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b5c4f4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b5c4f4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5c4f4 bytes f50f1df8
- 00b5c4f8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5c4f8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5c4f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5c4f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c4f8 bytes f44f01a9
- 00b5c4fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5c4fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5c4fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5c4fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c4fc bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acb2dd38cab8d56b0fa2678a11a9d189"></a>

### [`00b5c5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c5b8.md) → [`00b5c654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c654.md) _ZN8firebase8callback16BlockingCallbackD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5bb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bb80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bc50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 35.00% / 新版 35.00%

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
      "site": "00b5c5b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c5bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c5bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5c5b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c5bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c5cc",
      "READ",
      [
        "storage",
        "00c9b780",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5c654",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5c658",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b5c668",
      "READ",
      [
        "storage",
        "00c9b850",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c5b8.md#insn-00b5c5b8) · [`00b5c5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c5b8.md#insn-00b5c5bc) · [`00b5c5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c5b8.md#insn-00b5c5d8)

~~~diff
- 00b5c5b8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b5c5b8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b5c5b8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5c5b8 bytes f30f1ef8
- 00b5c5bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5c5bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5c5bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5c5bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c5bc bytes fd7b01a9
- 00b5c5d8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b5c5d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b5c5d8 bytes 090000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42ac430c9a81f1ba6befb4e753a707a3"></a>

### [`00b5c884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c884.md) → [`00b5c920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c920.md) _ZN8firebase15CleanupNotifier10CleanupAllEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b790.md) · 呼出先 3件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md)
- 新版 呼出元 1件 [`00c5b860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b860.md) · 呼出先 3件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ace0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 10.00% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c884"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c888"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c888"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5c884",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c888",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c88c",
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
      "00b5c920",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5c924",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5c928",
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

- 旧版 [`00b5c884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c884.md#insn-00b5c884) · [`00b5c888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c884.md#insn-00b5c888) · [`00b5c88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c884.md#insn-00b5c88c)

~~~diff
- 00b5c884 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b5c884 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b5c884 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5c884 bytes f50f1df8
- 00b5c888 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5c888 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5c888 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5c888 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c888 bytes f44f01a9
- 00b5c88c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5c88c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5c88c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5c88c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c88c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0463361021d89da35c5e1b5631a4979d"></a>

### [`00b5c8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c8f4.md) → [`00b5c990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c990.md) _ZN8firebase15CleanupNotifier19UnregisterAllOwnersEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bbb0.md) · 呼出先 3件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5bba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bba0.md)
- 新版 呼出元 1件 [`00c5bc80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bc80.md) · 呼出先 3件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5bc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bc70.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 38.89% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c8f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c8f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5c8f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5c8f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c8f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5c8fc",
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
      "00b5c990",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b5c994",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5c998",
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

- 旧版 [`00b5c8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c8f4.md#insn-00b5c8f4) · [`00b5c8f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c8f4.md#insn-00b5c8f8) · [`00b5c8fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c8f4.md#insn-00b5c8fc)

~~~diff
- 00b5c8f4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5c8f4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5c8f4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b5c8f4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5c8f4 bytes f85fbca9
- 00b5c8f8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5c8f8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5c8f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5c8f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c8f8 bytes f65701a9
- 00b5c8fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5c8fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5c8fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5c8fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5c8fc bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26dae70be2371da879ef48e258496dd3"></a>

### [`00b5cbc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5cbc8.md) → [`00b5cc64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5cc64.md) _ZN8firebase15CleanupNotifier15UnregisterOwnerEPS0_Pv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5bba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bba0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5bc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bc70.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 77.42% / 新版 77.42%

CFGの説明率　旧版 60.71% / 新版 58.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5cbfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5cc20"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5cc98"
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
      "00b5cc74",
      "READ",
      [
        "storage",
        "00c9b798",
        null,
        "pointer"
      ]
    ],
    [
      "00b5cc7c",
      "READ",
      [
        "storage",
        "01126008",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5cbf0",
      "READ",
      [
        "storage",
        "00c9b790",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5cc74",
      "READ",
      [
        "storage",
        "00c9b868",
        null,
        "pointer"
      ]
    ],
    [
      "00b5cc7c",
      "READ",
      [
        "storage",
        "01126108",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b5cc8c",
      "READ",
      [
        "storage",
        "00c9b860",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5cbc8.md#insn-00b5cbfc) · [`00b5cc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5cbc8.md#insn-00b5cc20)
- 新版 [`00b5cc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5cc64.md#insn-00b5cc98)

~~~diff
- 00b5cbfc ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b5cbfc ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
- 00b5cbfc bytes c90100b4
- 00b5cc20 ["CBRANCH", null, ["local:b21:8", "register:101:1"]]
- 00b5cc20 bytes a0000054
+ 00b5cc98 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00b5cc98 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
+ 00b5cc98 bytes c90100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b485abad25476daa56cb0e547e6a264"></a>

### [`00b5cff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5cff0.md) → [`00b5d08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d08c.md) _ZNSt6__ndk16__treeINS_12__value_typeIPvPFvS2_EEENS_19__map_value_compareIS2_S5_NS_4lessIS2_EELb1EEENS_9allocatorIS5_EEE7destroyEPNS_11__tre

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5bbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bbc0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5bbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bbc0.md)
- 新版 呼出元 1件 [`00c5bc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bc90.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bc90.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "00b5cff8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5cff8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5d094"
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
      "unmatched:00b5cff8",
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
      "00b5d094",
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

- 旧版 [`00b5cff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5cff0.md#insn-00b5cff8) · [`00b5d018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5cff0.md#insn-00b5d018)
- 新版 [`00b5d0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d08c.md#insn-00b5d0b4) · [`00b5d094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d08c.md#insn-00b5d094)

~~~diff
- 00b5cff8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5cff8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5cff8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5cff8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5cff8 bytes fd7b01a9
- 00b5d018 ["INT_ADD", "register:40f0:8", ["const:b5d018:8", "const:4:8"]]
- 00b5d018 ["CALL", null, ["callee:00c5bc90:8"]]
+ 00b5d0b4 ["INT_ADD", "register:40f0:8", ["const:b5d0b4:8", "const:4:8"]]
+ 00b5d0b4 ["CALL", null, ["callee:00c5bc90:8"]]
- 00b5d018 bytes eafa0394
+ 00b5d0b4 bytes f7fa0394
+ 00b5d094 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00b5d094 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00b5d094 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
+ 00b5d094 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b5d094 bytes fd7b01a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29e85708ec892e09fb91d019d6c3e05e"></a>

### [`00b5d030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d030.md) → [`00b5d0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d0cc.md) _ZNSt6__ndk16__treeINS_12__value_typeIPvPN8firebase15CleanupNotifierEEENS_19__map_value_compareIS2_S6_NS_4lessIS2_EELb1EEENS_9allocatorIS6_E

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5bbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bbd0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5bbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bbd0.md)
- 新版 呼出元 1件 [`00c5bca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bca0.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bca0.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "00b5d038"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d038"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5d0d4"
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
      "unmatched:00b5d038",
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
      "00b5d0d4",
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

- 旧版 [`00b5d038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d030.md#insn-00b5d038) · [`00b5d058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d030.md#insn-00b5d058)
- 新版 [`00b5d0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d0cc.md#insn-00b5d0f4) · [`00b5d0d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d0cc.md#insn-00b5d0d4)

~~~diff
- 00b5d038 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5d038 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5d038 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5d038 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5d038 bytes fd7b01a9
- 00b5d058 ["INT_ADD", "register:40f0:8", ["const:b5d058:8", "const:4:8"]]
- 00b5d058 ["CALL", null, ["callee:00c5bca0:8"]]
+ 00b5d0f4 ["INT_ADD", "register:40f0:8", ["const:b5d0f4:8", "const:4:8"]]
+ 00b5d0f4 ["CALL", null, ["callee:00c5bca0:8"]]
- 00b5d058 bytes defa0394
+ 00b5d0f4 bytes ebfa0394
+ 00b5d0d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00b5d0d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00b5d0d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
+ 00b5d0d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b5d0d4 bytes fd7b01a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b9d51d45d35ab03d17ee1cd62df217f"></a>

### [`00b5d070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d070.md) → [`00b5d10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d10c.md) _INIT_281

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5ad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad50.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d070"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d074"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d074"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5d070",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5d074",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5d094",
      "READ",
      [
        "storage",
        "00c9b798",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5d10c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5d110",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b5d130",
      "READ",
      [
        "storage",
        "00c9b868",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d070.md#insn-00b5d070) · [`00b5d074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d070.md#insn-00b5d074)
- 新版 [`00b5d10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d10c.md#insn-00b5d10c)

~~~diff
- 00b5d070 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b5d070 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b5d070 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5d070 bytes f30f1ef8
- 00b5d074 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5d074 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5d074 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5d074 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5d074 bytes fd7b01a9
+ 00b5d10c ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 00b5d10c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00b5d10c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b5d10c bytes f30f1ef8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9ab6fa868730eb2d2129fcb5b34b11c"></a>

### [`00b5d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d7c0.md) → [`00b5d85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d85c.md) _ZNK8firebase4Path9GetParentEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) [`00c5b7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b7f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5b8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b8c0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 12.50% / 新版 12.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d7e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5d880"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d844"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5d7e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5d844",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d908"
      ]
    ],
    [
      "unmatched:00b5d894",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d948"
      ]
    ]
  ],
  "added": [
    [
      "00b5d880",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b5d8e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d908"
      ]
    ],
    [
      "00b5d930",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d948"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d7e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d7c0.md#insn-00b5d7e4) · [`00b5d7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d7c0.md#insn-00b5d7f8) · [`00b5d844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d7c0.md#insn-00b5d844)
- 新版 [`00b5d894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d85c.md#insn-00b5d894)

~~~diff
- 00b5d7e4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b5d7e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b5d7e4 bytes e90f00f9
- 00b5d7f8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4018:8", "const:0:8"]]
- 00b5d7f8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b5d894 ["INT_NOTEQUAL", "tmp:0:1", ["register:4018:8", "const:0:8"]]
+ 00b5d894 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b5d7f8 bytes 830000b5
+ 00b5d894 bytes 830000b5
- 00b5d844 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 00b5d844 bytes 40010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a136db332dec3849d428338b42ad33b"></a>

### [`00b5d8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d8f0.md) → [`00b5d98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d98c.md) _ZNK8firebase4Path11GetBaseNameEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 31.58% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d944"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5d9e0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d948"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d8f0.md#insn-00b5d944) · [`00b5d948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d8f0.md#insn-00b5d948)
- 新版 [`00b5d9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d98c.md#insn-00b5d9e0)

~~~diff
- 00b5d944 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b5d944 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b5d944 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:1:8"]]
- 00b5d944 ["COPY", "register:4000:8", ["tmp:0:8"]]
- 00b5d944 bytes 20058a9a
- 00b5d948 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b5d948 ["RETURN", null, ["register:0:8"]]
- 00b5d948 bytes c0035fd6
+ 00b5d9e0 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b5d9e0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00b5d9e0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:1:8"]]
+ 00b5d9e0 ["COPY", "register:4000:8", ["tmp:0:8"]]
+ 00b5d9e0 bytes 20058a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40cf9728653031e32bacf92407cca4d3"></a>

### [`00b5d94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d94c.md) → [`00b5d9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d9e8.md) _ZNK8firebase4Path8IsParentERKS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 36.59% / 新版 36.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d9a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d9dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5d9ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5d9dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5daac"
      ]
    ],
    [
      "unmatched:00b5d9ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5daac"
      ]
    ],
    [
      "00b5da78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5dac8"
      ]
    ]
  ],
  "added": [
    [
      "00b5da78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5daac"
      ]
    ],
    [
      "00b5da88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5daac"
      ]
    ],
    [
      "00b5dab4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5dac8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d9a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d94c.md#insn-00b5d9a4) · [`00b5d9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d94c.md#insn-00b5d9dc) · [`00b5d9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5d/00b5d94c.md#insn-00b5d9ec)

~~~diff
- 00b5d9a4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b5d9a4 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b5d9a4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b5d9a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b5d9a4 bytes 4a15819a
- 00b5d9dc ["CBRANCH", null, ["local:b23:8", "register:101:1"]]
- 00b5d9dc bytes a0010054
- 00b5d9ec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b5d9ec ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 00b5d9ec bytes 21010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9cc8feeeacfb2d6eb1c0cd09ee0e221"></a>

### [`00b5e208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5e208.md) → [`00b5e2a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e2a4.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertINS_11__wrap_iterIPKcEEEENS_9enable_ifIXaasr21__is_forward_iterator

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bc10.md) · 呼出先 7件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md)
- 新版 呼出元 1件 [`00c5bce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bce0.md) · 呼出先 7件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 61.80% / 新版 60.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e4b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e4b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5e550"
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
      "unmatched:00b5e468",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e5bc"
      ]
    ],
    [
      "unmatched:00b5e4bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e544"
      ]
    ],
    [
      "unmatched:00b5e4c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e574"
      ]
    ]
  ],
  "added": [
    [
      "00b5e504",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e5bc"
      ]
    ],
    [
      "00b5e558",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e544"
      ]
    ],
    [
      "00b5e560",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e574"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5e428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5e208.md#insn-00b5e428) · [`00b5e468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5e208.md#insn-00b5e468) · [`00b5e48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5e208.md#insn-00b5e48c)
- 新版 [`00b5e4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e2a4.md#insn-00b5e4c4)

~~~diff
- 00b5e428 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b5e428 ["CBRANCH", null, ["local:b39:8", "tmp:0:1"]]
+ 00b5e4c4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b5e4c4 ["CBRANCH", null, ["local:b40:8", "tmp:0:1"]]
- 00b5e428 bytes 61ffff54
+ 00b5e4c4 bytes 61ffff54
- 00b5e468 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b5e468 ["CBRANCH", null, ["local:b58:8", "tmp:0:1"]]
- 00b5e468 bytes c1050054
- 00b5e48c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b5e48c ["RETURN", null, ["register:0:8"]]
- 00b5e48c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce6e89154022f0da9863ef21122f2428"></a>

### [`00b5e528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5e528.md) → [`00b5e5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e5c4.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7reserveEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c585f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585f0.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c586c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586c0.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 55.00% / 新版 56.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e584"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e58c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5e620"
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
      "unmatched:00b5e584",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e6dc"
      ]
    ],
    [
      "unmatched:00b5e58c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e65c"
      ]
    ],
    [
      "00b5e628",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b5e588"
      ]
    ]
  ],
  "added": [
    [
      "00b5e620",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e6dc"
      ]
    ],
    [
      "00b5e628",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e65c"
      ]
    ],
    [
      "00b5e654",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e624"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5e584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5e528.md#insn-00b5e584) · [`00b5e58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5e528.md#insn-00b5e58c)
- 新版 [`00b5e620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e5c4.md#insn-00b5e620)

~~~diff
- 00b5e584 ["CBRANCH", null, ["local:b27:8", "register:101:1"]]
- 00b5e584 bytes e0050054
- 00b5e58c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b5e58c ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 00b5e58c bytes a1010054
+ 00b5e620 ["CBRANCH", null, ["local:b26:8", "register:101:1"]]
+ 00b5e620 bytes e0050054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-856c3a57aa27983cd530fb4e77f79305"></a>

### [`00b5f954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5f954.md) → [`00b5f9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f9f0.md) _ZN8firebase26ReferenceCountedFutureImpl11RunCallbackEPNS_10FutureBaseEPFvRKS1_PvES5_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f954"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f958"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f958"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5f954",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5f958",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5f95c",
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
      "00b5f9f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b5f9f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5f9f8",
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

- 旧版 [`00b5f954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5f954.md#insn-00b5f954) · [`00b5f958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5f954.md#insn-00b5f958) · [`00b5f95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5f954.md#insn-00b5f95c)

~~~diff
- 00b5f954 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00b5f954 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b5f954 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b5f954 bytes f70f1cf8
- 00b5f958 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5f958 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5f958 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b5f958 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5f958 bytes f65701a9
- 00b5f95c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5f95c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5f95c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b5f95c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5f95c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98a39b097bdb3d24a775cd6de6b94141"></a>

### [`00b5fa5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5fa5c.md) → [`00b5faf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5faf8.md) _ZN8firebase26ReferenceCountedFutureImpl15ReferenceFutureERKNS_12FutureHandleE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5faac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5fb48"
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
      "unmatched:00b5faac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5fb34"
      ]
    ]
  ],
  "added": [
    [
      "00b5fb48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5fb34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5faac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5fa5c.md#insn-00b5faac) · [`00b5fa7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5f/00b5fa5c.md#insn-00b5fa7c)
- 新版 [`00b5fb48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5faf8.md#insn-00b5fb48) · [`00b5fb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5faf8.md#insn-00b5fb18)

~~~diff
- 00b5faac ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b5faac ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b5faac bytes 69ffffb5
+ 00b5fb48 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00b5fb48 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b5fb48 bytes 69ffffb5
- 00b5fa7c ["INT_ADD", "register:40f0:8", ["const:b5fa7c:8", "const:4:8"]]
- 00b5fa7c ["CALL", null, ["callee:00c5aad0:8"]]
+ 00b5fb18 ["INT_ADD", "register:40f0:8", ["const:b5fb18:8", "const:4:8"]]
+ 00b5fb18 ["CALL", null, ["callee:00c5aad0:8"]]
- 00b5fa7c bytes e1eb0394
+ 00b5fb18 bytes eeeb0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d78626507502c2dd03d9350b52e00e2"></a>

### [`00b60e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60e18.md) → [`00b60eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60eb4.md) _ZN8firebase26ReferenceCountedFutureImpl12MarkOrphanedEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60e18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60e18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60e1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b60e18",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b60e1c",
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
      "00b60eb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b60eb8",
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

- 旧版 [`00b60e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60e18.md#insn-00b60e18) · [`00b60e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60e18.md#insn-00b60e1c)
- 新版 [`00b60eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60eb4.md#insn-00b60eb4)

~~~diff
- 00b60e18 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b60e18 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b60e18 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b60e18 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b60e18 bytes f44fbea9
- 00b60e1c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b60e1c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b60e1c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b60e1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b60e1c bytes fd7b01a9
+ 00b60eb4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00b60eb4 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00b60eb4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00b60eb4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b60eb4 bytes f44fbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb1dbb6e69d7a03bbf190c8c1ba722b4"></a>

### [`00b60e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60e54.md) → [`00b60ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60ef0.md) _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) · 呼出先 2件 [`00b60eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60eac.md) [`00c5ac00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) · 呼出先 2件 [`00b60f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60f48.md) [`00c5acd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acd0.md)

変更の種類 call, call_count, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60e7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b60f18"
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
      "00b60f28",
      "PARAM",
      [
        "storage",
        "00b60eac",
        null,
        null
      ]
    ],
    [
      "unmatched:00b60e7c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b60f28",
      "PARAM",
      [
        "storage",
        "00b60f48",
        null,
        null
      ]
    ],
    [
      "00b60f18",
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

- 旧版 [`00b60e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60e54.md#insn-00b60e7c) · [`00b60e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60e54.md#insn-00b60e74)
- 新版 [`00b60f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60ef0.md#insn-00b60f18)

~~~diff
- 00b60e7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b60e7c ["INT_ADD", "register:40f0:8", ["const:b60e7c:8", "const:4:8"]]
- 00b60e7c ["CALLIND", null, ["register:0:8"]]
- 00b60e7c bytes 00013fd6
+ 00b60f18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b60f18 ["INT_ADD", "register:40f0:8", ["const:b60f18:8", "const:4:8"]]
+ 00b60f18 ["CALLIND", null, ["register:0:8"]]
+ 00b60f18 bytes 00013fd6
- 00b60e74 ["COPY", "register:4008:8", ["register:4098:8"]]
- 00b60e74 bytes e10313aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ff7817f0e1397b76beb5ee40d8b02c8"></a>

### [`00b60eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60eb4.md) → [`00b60f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60f50.md) _ZN8firebase12FutureHandleD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b613b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b613b0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) · 呼出先 1件 [`00c5ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md)
- 新版 呼出元 2件 [`00b6144c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b6144c.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) · 呼出先 1件 [`00c5ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ace0.md)

変更の種類 constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b60ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60eb4.md#insn-00b60ed4) · [`00b60eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60eb4.md#insn-00b60eec) · [`00b60ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60eb4.md#insn-00b60ef0)
- 新版 [`00b60f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60f50.md#insn-00b60f70)

~~~diff
- 00b60ed4 ["INT_ADD", "register:40f0:8", ["const:b60ed4:8", "const:4:8"]]
- 00b60ed4 ["CALL", null, ["callee:00c5ace0:8"]]
+ 00b60f70 ["INT_ADD", "register:40f0:8", ["const:b60f70:8", "const:4:8"]]
+ 00b60f70 ["CALL", null, ["callee:00c5ace0:8"]]
- 00b60ed4 bytes 4fe70394
+ 00b60f70 bytes 5ce70394
- 00b60eec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:18:8"]]
- 00b60eec ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b60eec bytes 020d40f9
- 00b60ef0 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b60ef0 ["INT_ADD", "register:8:8", ["register:8:8", "const:20:8"]]
- 00b60ef0 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00b60ef0 bytes f30742f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d39633c0e58ff1d20ca6e6365684b71a"></a>

### [`00b60f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60f04.md) → [`00b60fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60fa0.md) _ZN8firebase12FutureHandleC1ERKS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md) · 呼出先 2件 [`00b60eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60eac.md) [`00c5ac00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md) · 呼出先 2件 [`00b60f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60f48.md) [`00c5acd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acd0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 79.17% / 新版 79.17%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60f18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60f20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b60fb4"
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
      "unmatched:00b60f24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b60ff4"
      ]
    ],
    [
      "00b60fe0",
      "PARAM",
      [
        "storage",
        "00b60eac",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b60fc0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b60ff4"
      ]
    ],
    [
      "00b60fe0",
      "PARAM",
      [
        "storage",
        "00b60f48",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60f04.md#insn-00b60f18) · [`00b60f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60f04.md#insn-00b60f20) · [`00b60f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60f04.md#insn-00b60f24)

~~~diff
- 00b60f18 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b60f18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b60f18 bytes 080000f9
- 00b60f20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00b60f20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b60f20 bytes 600600f9
- 00b60f24 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b60f24 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b60f24 bytes a00100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4edeee9941a606a3cbc450507d284a4"></a>

### [`00b6112c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b6112c.md) → [`00b611c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b611c8.md) FUN_00b611c8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`00b60494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60494.md) [`00b68240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68240.md) [`00bb4010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb4/00bb4010.md) [`00bc9490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9490.md) [`00bc9654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9654.md) · 呼出先 1件 [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 7件 [`00b60530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60530.md) [`00b682dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b682dc.md) [`00bb40ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb4/00bb40ac.md) [`00bc952c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc952c.md) [`00bc96f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc96f0.md) · 呼出先 1件 [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6112c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6112c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b611c8"
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
      "unmatched:00b6112c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b61134",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b210"
      ]
    ]
  ],
  "added": [
    [
      "00b611c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b611d0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b210"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6112c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b6112c.md#insn-00b6112c) · [`00b61134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b6112c.md#insn-00b61134)
- 新版 [`00b611c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b611c8.md#insn-00b611c8)

~~~diff
- 00b6112c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6112c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6112c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00b6112c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6112c bytes fd7bbfa9
- 00b61134 ["INT_ADD", "register:40f0:8", ["const:b61134:8", "const:4:8"]]
- 00b61134 ["CALL", null, ["callee:00c5b210:8"]]
- 00b61134 bytes 03e80394
+ 00b611c8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00b611c8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00b611c8 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00b611c8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b611c8 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0f6b02ff456333669981fea57f8c9ef"></a>

### [`00b61320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b61320.md) → [`00b613bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b613bc.md) FUN_00b613bc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b5ecd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5e/00b5ecd0.md) · 呼出先 4件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5aaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aaa0.md) [`00c5ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md)
- 新版 呼出元 1件 [`00b5ed6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ed6c.md) · 呼出先 4件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab70.md) [`00c5ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ace0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61320"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61320"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61324"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61320",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b61324",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6139c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b613bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b613c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b61438",
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

- 旧版 [`00b61320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b61320.md#insn-00b61320) · [`00b61324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b61320.md#insn-00b61324) · [`00b6139c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b61320.md#insn-00b6139c)

~~~diff
- 00b61320 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b61320 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b61320 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b61320 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b61320 bytes f44fbea9
- 00b61324 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b61324 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b61324 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b61324 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b61324 bytes fd7b01a9
- 00b6139c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6139c ["INT_ADD", "register:40f0:8", ["const:b6139c:8", "const:4:8"]]
- 00b6139c ["CALLIND", null, ["register:0:8"]]
- 00b6139c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e12a527f7adacd519b1ddee6d9e7032"></a>

### [`00b613b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b613b0.md) → [`00b6144c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b6144c.md) _INIT_282

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b60eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b60/00b60eb4.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b60f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60f50.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00b613c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b613c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b61464"
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
      "unmatched:00b613b8",
      "READ",
      [
        "storage",
        "00c9b7a8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b613b8",
      "PARAM",
      [
        "storage",
        "01126018",
        "_ZN8firebase26ReferenceCountedFutureImpl14kInvalidHandleE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b613bc",
      "READ",
      [
        "storage",
        "00c9b7a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b61454",
      "READ",
      [
        "storage",
        "00c9b878",
        null,
        "pointer"
      ]
    ],
    [
      "00b61454",
      "PARAM",
      [
        "storage",
        "01126118",
        "_ZN8firebase26ReferenceCountedFutureImpl14kInvalidHandleE",
        "undefined8"
      ]
    ],
    [
      "00b61458",
      "READ",
      [
        "storage",
        "00c9b870",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b613c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b613b0.md#insn-00b613c8) · [`00b613b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b613b0.md#insn-00b613b0)
- 新版 [`00b61464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b6144c.md#insn-00b61464)

~~~diff
- 00b613c8 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b613c8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b613c8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b613c8 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b613c8 bytes 3f7c00a9
+ 00b61464 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 00b61464 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b61464 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00b61464 ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 00b61464 bytes 3f7c00a9
- 00b613b0 ["COPY", "register:4008:8", ["const:c9b000:8"]]
- 00b613b0 bytes c10900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-800c9a459caab403666fb67835a7dcd1"></a>

### [`00b61494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b61494.md) → [`00b61530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61530.md) _ZN8firebase17ModuleInitializerD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ac50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 10.00% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b614a8",
      "READ",
      [
        "storage",
        "00c9b7e8",
        null,
        "pointer"
      ]
    ],
    [
      "00b61550",
      "DATA",
      [
        "storage",
        "00c904d8",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00b61544",
      "READ",
      [
        "storage",
        "00c9b8b8",
        null,
        "pointer"
      ]
    ],
    [
      "00b61550",
      "DATA",
      [
        "storage",
        "00c905a8",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b614a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b61494.md#insn-00b614a8) · [`00b614b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b61494.md#insn-00b614b8) · [`00b614c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b61494.md#insn-00b614c0)
- 新版 [`00b61554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61530.md#insn-00b61554) · [`00b6155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61530.md#insn-00b6155c)

~~~diff
- 00b614a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7e8:8"]]
- 00b614a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b614a8 bytes 08f543f9
- 00b614b8 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00b614b8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b61554 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00b61554 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b614b8 bytes 740100b4
+ 00b61554 bytes 740100b4
- 00b614c0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b614c0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b6155c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b6155c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b614c0 bytes 600000b4
+ 00b6155c bytes 600000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea056a13de21033db9a5ec80803479f1"></a>

### [`00b614f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b614f4.md) → [`00b61590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61590.md) _ZN8firebase17ModuleInitializer10InitializeEPNS_3AppEPvPFNS_10InitResultES2_S3_E

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5bd50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5be20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5be20.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.44% / 新版 67.44%

CFGの説明率　旧版 38.46% / 新版 35.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b614f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b614f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b614fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b614f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b614fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b61500",
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
      "00b61594",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b61598",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6159c",
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

- 旧版 [`00b614f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b614f4.md#insn-00b614f8) · [`00b614fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b614f4.md#insn-00b614fc) · [`00b61500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b61/00b614f4.md#insn-00b61500)

~~~diff
- 00b614f8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b614f8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b614f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b614f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b614f8 bytes f85f01a9
- 00b614fc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b614fc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b614fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b614fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b614fc bytes f65702a9
- 00b61500 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b61500 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b61500 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b61500 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b61500 bytes f44f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d739839a807b0787c9ec23d4d4e2bb52"></a>

### [`00b625a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b625a0.md) → [`00b6263c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b6263c.md) _ZN8firebase11SplitStringERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md) [`00c5b650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b650.md) [`00c5b7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b7f0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md) [`00c5b720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b720.md) [`00c5b8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b8c0.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 60.98% / 新版 60.98%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b626a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b626ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b626b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b62674",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b627b0"
      ]
    ],
    [
      "unmatched:00b6268c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b8c0"
      ]
    ],
    [
      "unmatched:00b62698",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b626c0"
      ]
    ]
  ],
  "added": [
    [
      "00b62710",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b627b0"
      ]
    ],
    [
      "00b62728",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b8c0"
      ]
    ],
    [
      "00b62734",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6275c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b625a0.md#insn-00b62674) · [`00b6268c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b625a0.md#insn-00b6268c) · [`00b62698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b625a0.md#insn-00b62698)

~~~diff
- 00b62674 ["CBRANCH", null, ["local:b19:8", "register:101:1"]]
- 00b62674 bytes 00050054
- 00b6268c ["INT_ADD", "register:40f0:8", ["const:b6268c:8", "const:4:8"]]
- 00b6268c ["CALL", null, ["callee:00c5b8c0:8"]]
- 00b6268c bytes 59e40394
- 00b62698 ["CBRANCH", null, ["local:b13:8", "register:102:1"]]
- 00b62698 bytes 42010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f515963f099bc0f0cd1add1781f5715"></a>

### [`00b62cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62cb4.md) → [`00b62d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62d50.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN8firebase11AppCallbackEEENS_19__map_value_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bda0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5be70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5be70.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 89.86% / 新版 89.86%

CFGの説明率　旧版 48.00% / 新版 48.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62ce8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62cec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62d74"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b62ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62cb4.md#insn-00b62ce8) · [`00b62cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62cb4.md#insn-00b62cec) · [`00b62d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62cb4.md#insn-00b62d74)

~~~diff
- 00b62ce8 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b62ce8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b62ce8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b62ce8 ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00b62ce8 bytes 7601899a
- 00b62cec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b62cec ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b62cec ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b62cec ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b62cec bytes 5515819a
- 00b62d74 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b62d74 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b62d74 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b62d74 ["COPY", "register:40b8:8", ["tmp:0:8"]]
- 00b62d74 bytes 77018a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fb554362bfe31671a5b5cd846d06054"></a>

### [`00b64688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64688.md) → [`00b64724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64724.md) _ZNK8firebase7Variant16assert_is_stringEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ab20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ab20.md) · 呼出先 2件 [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5abf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5abf0.md) · 呼出先 2件 [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 59.26% / 新版 59.26%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b646cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b64768"
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
      "unmatched:00b646c8",
      "PARAM",
      [
        "storage",
        "002be63f",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b646cc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ad70"
      ]
    ],
    [
      "unmatched:00b646d8",
      "READ",
      [
        "storage",
        "00c9b7f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b64764",
      "PARAM",
      [
        "storage",
        "002be5eb",
        null,
        "string"
      ]
    ],
    [
      "00b64768",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ad70"
      ]
    ],
    [
      "00b64774",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b646cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64688.md#insn-00b646cc) · [`00b646c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64688.md#insn-00b646c8)
- 新版 [`00b64768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64724.md#insn-00b64768)

~~~diff
- 00b646cc ["INT_ADD", "register:40f0:8", ["const:b646cc:8", "const:4:8"]]
- 00b646cc ["CALL", null, ["callee:00c5ad70:8"]]
- 00b646cc bytes 75d90394
+ 00b64768 ["INT_ADD", "register:40f0:8", ["const:b64768:8", "const:4:8"]]
+ 00b64768 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00b64768 bytes 82d90394
- 00b646c8 ["COPY", "tmp:0:8", ["const:63f:8"]]
- 00b646c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b646c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b646c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b646c8 bytes 00fc1891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93c0c09e31f1a79470c7fdaa61ec92e1"></a>

### [`00b646f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b646f4.md) → [`00b64790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64790.md) _ZNK8firebase7Variant14assert_is_blobEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b590.md) · 呼出先 2件 [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5b660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b660.md) · 呼出先 2件 [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 52.17% / 新版 52.17%

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
      "site": "00b64728"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b647c4"
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
      "unmatched:00b64724",
      "PARAM",
      [
        "storage",
        "002bbe48",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b64728",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ad70"
      ]
    ],
    [
      "unmatched:00b64734",
      "READ",
      [
        "storage",
        "00c9b7f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b647c0",
      "PARAM",
      [
        "storage",
        "002bbdf4",
        null,
        "string"
      ]
    ],
    [
      "00b647c4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ad70"
      ]
    ],
    [
      "00b647d0",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b64728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b646f4.md#insn-00b64728) · [`00b6470c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b646f4.md#insn-00b6470c)
- 新版 [`00b647c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64790.md#insn-00b647c4) · [`00b647a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64790.md#insn-00b647a8)

~~~diff
- 00b64728 ["INT_ADD", "register:40f0:8", ["const:b64728:8", "const:4:8"]]
- 00b64728 ["CALL", null, ["callee:00c5ad70:8"]]
- 00b64728 bytes 5ed90394
+ 00b647c4 ["INT_ADD", "register:40f0:8", ["const:b647c4:8", "const:4:8"]]
+ 00b647c4 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00b647c4 bytes 6bd90394
- 00b6470c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b6470c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b647a8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b647a8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6470c bytes 81000054
+ 00b647a8 bytes 81000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c21068d699bd0c672bf16ad88b63d13b"></a>

### [`00b6498c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b6498c.md) → [`00b64a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64a28.md) _ZNK8firebase7Variant7AsInt64Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5aaf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aaf0.md) · 呼出先 3件 [`00c58590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58590.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8f0.md)
- 新版 呼出元 1件 [`00c5abc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5abc0.md) · 呼出先 3件 [`00c58660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58660.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9c0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.44% / 新版 93.44%

CFGの説明率　旧版 92.00% / 新版 88.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b64a54",
      "DATA",
      [
        "storage",
        "0030bc62",
        "switchD_00b649c4::switchdataD_0030bc62",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00b64a54",
      "DATA",
      [
        "storage",
        "0030bca2",
        "switchD_00b64a60::switchdataD_0030bca2",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b649a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b6498c.md#insn-00b649a8) · [`00b649b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b6498c.md#insn-00b649b0) · [`00b649b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b6498c.md#insn-00b649b4)
- 新版 [`00b64a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64a28.md#insn-00b64a44) · [`00b64a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64a28.md#insn-00b64a4c)

~~~diff
- 00b649a8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b649a8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b649a8 ["CBRANCH", null, ["local:b11:8", "tmp:1:1"]]
+ 00b64a44 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b64a44 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00b64a44 ["CBRANCH", null, ["local:b12:8", "tmp:1:1"]]
- 00b649a8 bytes 68040054
+ 00b64a44 bytes 68040054
- 00b649b0 ["COPY", "tmp:0:8", ["const:c62:8"]]
- 00b649b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b649b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b649b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b64a4c ["COPY", "tmp:0:8", ["const:ca2:8"]]
+ 00b64a4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b64a4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b64a4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b649b0 bytes 08893191
+ 00b64a4c bytes 08893291
- 00b649b4 ["COPY", "register:4058:8", ["const:b649c8:8"]]
- 00b649b4 bytes ab000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-015913b90793f794605378cda8a1787d"></a>

### [`00b65510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65510.md) → [`00b655ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b655ac.md) _ZN8firebase5MutexD1Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00bb8bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8bdc.md) [`00bbd6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd6c0.md) [`00bc1ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1ad8.md) [`00c5aaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aaa0.md) · 呼出先 2件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b690.md)
- 新版 呼出元 4件 [`00bb8c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8c78.md) [`00bbd75c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd75c.md) [`00bc1b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b74.md) [`00c5ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab70.md) · 呼出先 2件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b760.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b65524",
      "PARAM",
      [
        "storage",
        "002ad11b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b655c0",
      "PARAM",
      [
        "storage",
        "002ad0bf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65510.md#insn-00b65518) · [`00b6551c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65510.md#insn-00b6551c) · [`00b65524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65510.md#insn-00b65524)
- 新版 [`00b655b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b655ac.md#insn-00b655b4) · [`00b655b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b655ac.md#insn-00b655b8)

~~~diff
- 00b65518 ["INT_ADD", "register:40f0:8", ["const:b65518:8", "const:4:8"]]
- 00b65518 ["CALL", null, ["callee:00c5b760:8"]]
+ 00b655b4 ["INT_ADD", "register:40f0:8", ["const:b655b4:8", "const:4:8"]]
+ 00b655b4 ["CALL", null, ["callee:00c5b760:8"]]
- 00b65518 bytes 5ed80394
+ 00b655b4 bytes 6bd80394
- 00b6551c ["INT_EQUAL", "tmp:0:1", ["register:4000:4", "const:0:4"]]
- 00b6551c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b655b8 ["INT_EQUAL", "tmp:0:1", ["register:4000:4", "const:0:4"]]
+ 00b655b8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b6551c bytes a0000034
+ 00b655b8 bytes a0000034
- 00b65524 ["COPY", "tmp:0:8", ["const:11b:8"]]
- 00b65524 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65524 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65524 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65524 bytes 006c0491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d64c45b85730f20871e7f6179b97f33d"></a>

### [`00b65698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65698.md) → [`00b65734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65734.md) _ZN8firebase3app8GetClassEv

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
      "site": "00b656a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b6573c"
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
      "unmatched:00b6569c",
      "READ",
      [
        "storage",
        "01126050",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65738",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b656a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65698.md#insn-00b656a0) · [`00b65698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65698.md#insn-00b65698)
- 新版 [`00b6573c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65734.md#insn-00b6573c)

~~~diff
- 00b656a0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b656a0 ["RETURN", null, ["register:0:8"]]
- 00b656a0 bytes c0035fd6
+ 00b6573c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b6573c ["RETURN", null, ["register:0:8"]]
+ 00b6573c bytes c0035fd6
- 00b65698 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b65698 bytes 082e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53a82ccd81ebcf696c5b5d75a6cd7233"></a>

### [`00b65710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65710.md) → [`00b657ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b657ac.md) _ZN8firebase3app12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 46.43% / 新版 46.43%

CFGの説明率　旧版 15.38% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6574c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6576c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b657e8"
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
      "unmatched:00b65724",
      "READ",
      [
        "storage",
        "01126050",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b65728",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6580c"
      ]
    ],
    [
      "unmatched:00b65730",
      "READ",
      [
        "storage",
        "01126058",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b657c0",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ],
    [
      "00b657c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6580c"
      ]
    ],
    [
      "00b657cc",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65710.md#insn-00b65728) · [`00b65748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65710.md#insn-00b65748) · [`00b6574c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65710.md#insn-00b6574c)

~~~diff
- 00b65728 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b65728 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b65728 bytes 410200b4
- 00b65748 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65748 ["INT_ADD", "register:40f0:8", ["const:b65748:8", "const:4:8"]]
- 00b65748 ["CALLIND", null, ["register:0:8"]]
- 00b65748 bytes 00013fd6
- 00b6574c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6574c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6574c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:58:8"]]
- 00b6574c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6574c bytes bf620139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-740e723055bdbac11d4e48082d5caadd"></a>

### [`00b65be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65be4.md) → [`00b65c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65c80.md) _ZN8firebase15options_builder10GetFieldIdENS0_5FieldE

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
      "site": "00b65c04"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b65ca0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65c1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65c94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b65c08"
      ]
    ],
    [
      "unmatched:00b65c00",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b65c04",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ],
  "added": [
    [
      "00b65c94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65ca4"
      ]
    ],
    [
      "00b65c9c",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b65ca0",
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

- 旧版 [`00b65c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65be4.md#insn-00b65c04) · [`00b65c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65be4.md#insn-00b65c1c)
- 新版 [`00b65ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65c80.md#insn-00b65ca0)

~~~diff
- 00b65c04 ["INT_ADD", "register:40f0:8", ["const:b65c04:8", "const:4:8"]]
- 00b65c04 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b65c04 bytes ffd40394
- 00b65c1c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b65c1c ["RETURN", null, ["register:0:8"]]
- 00b65c1c bytes c0035fd6
+ 00b65ca0 ["INT_ADD", "register:40f0:8", ["const:b65ca0:8", "const:4:8"]]
+ 00b65ca0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b65ca0 bytes 0cd50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27bb8d50a268c8498fb13d970a4c505f"></a>

### [`00b68290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68290.md) → [`00b6832c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b6832c.md) _ZNK8firebase10AppOptionseqERKS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bee0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5bfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bfb0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 72.65% / 新版 72.65%

CFGの説明率　旧版 42.71% / 新版 42.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 31件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68378"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68384"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6838c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6838c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b68850"
      ]
    ],
    [
      "00b68444",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b683d8"
      ]
    ],
    [
      "unmatched:00b683c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b68850"
      ]
    ]
  ],
  "added": [
    [
      "00b68428",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b68850"
      ]
    ],
    [
      "00b68444",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b68474"
      ]
    ],
    [
      "00b6845c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b68850"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68290.md#insn-00b68378) · [`00b68384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68290.md#insn-00b68384) · [`00b6838c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68290.md#insn-00b6838c)

~~~diff
- 00b68378 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b68378 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b68378 ["COPY", "tmp:0:8", ["register:4068:8"]]
- 00b68378 ["COPY", "register:4010:8", ["tmp:0:8"]]
- 00b68378 bytes 02018d9a
- 00b68384 ["COPY", "tmp:0:8", ["register:4068:8"]]
- 00b68384 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b68384 ["COPY", "tmp:0:8", ["register:4070:8"]]
- 00b68384 ["COPY", "register:4068:8", ["tmp:0:8"]]
- 00b68384 bytes ad018e9a
- 00b6838c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b6838c ["CBRANCH", null, ["local:b109:8", "tmp:0:1"]]
- 00b6838c bytes 41210054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0184679e488e045da26769b98d364155"></a>

### [`00b6a83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6a83c.md) → [`00b6a8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6a/00b6a8d8.md) _ZN11flatbuffers6ParserD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b910.md) · 呼出先 13件 [`005408d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005408d0.md) [`0073a304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a304.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b8a0.md) [`00c5b8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b8b0.md)
- 新版 呼出元 1件 [`00c5b9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b9e0.md) · 呼出先 13件 [`00540910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540910.md) [`0073a35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073a35c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b970.md) [`00c5b980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b980.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.32% / 新版 96.32%

CFGの説明率　旧版 71.00% / 新版 68.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6a8b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6aaa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6aab0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6a8b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6a900"
      ]
    ],
    [
      "unmatched:00b6aaa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ab88"
      ]
    ],
    [
      "unmatched:00b6aab0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6aaa0"
      ]
    ]
  ],
  "added": [
    [
      "00b6a954",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6a900"
      ]
    ],
    [
      "00b6ab44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ab88"
      ]
    ],
    [
      "00b6ab4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ab3c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6a8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6a83c.md#insn-00b6a8b8) · [`00b6aa0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6a83c.md#insn-00b6aa0c)
- 新版 [`00b6a954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6a/00b6a8d8.md#insn-00b6a954) · [`00b6aaa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6a/00b6a8d8.md#insn-00b6aaa8)

~~~diff
- 00b6a8b8 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00b6a8b8 bytes 60fdff54
+ 00b6a954 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
+ 00b6a954 bytes 60fdff54
- 00b6aa0c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b6aa0c ["CBRANCH", null, ["local:b42:8", "tmp:0:1"]]
+ 00b6aaa8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b6aaa8 ["CBRANCH", null, ["local:b43:8", "tmp:0:1"]]
- 00b6aa0c bytes 600000b4
+ 00b6aaa8 bytes 600000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e062f1fd7909fcdccfac6b26b232edd"></a>

### [`00b6b2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6b2a8.md) → [`00b6b344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b344.md) _ZNSt6__ndk16vectorIPN11flatbuffers9NamespaceENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bae0.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5bbb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bbb0.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 64.71% / 新版 64.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b2d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b2fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b300"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6b2d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6b3a8"
      ]
    ],
    [
      "unmatched:00b6b300",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6b424"
      ]
    ]
  ],
  "added": [
    [
      "00b6b370",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6b3a8"
      ]
    ],
    [
      "00b6b39c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6b424"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6b2a8.md#insn-00b6b2d4) · [`00b6b2fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6b2a8.md#insn-00b6b2fc) · [`00b6b300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6b2a8.md#insn-00b6b300)

~~~diff
- 00b6b2d4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b6b2d4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b6b2d4 bytes c90100b5
- 00b6b2fc ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6b2fc ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b6b2fc ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b6b2fc ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b6b2fc bytes 1931899a
- 00b6b300 ["INT_EQUAL", "tmp:0:1", ["register:40c8:8", "const:0:8"]]
- 00b6b300 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00b6b300 bytes 590400b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bab5084744c97b9c6e6b5d434dc8c025"></a>

### [`00b6b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6b390.md) → [`00b6b42c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b42c.md) _ZNK8firebase3fbs14GoogleServices6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b990.md) · 呼出先 2件 [`00c5b980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b980.md) [`00c5b9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9e0.md)
- 新版 呼出元 1件 [`00c5ba60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba60.md) · 呼出先 2件 [`00c5ba50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba50.md) [`00c5bab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bab0.md)

変更の種類 branch_condition_or_target, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 99.16% / 新版 99.16%

CFGの説明率　旧版 95.62% / 新版 95.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b4b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6b550"
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
      "unmatched:00b6b4b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6b7b8"
      ]
    ]
  ],
  "added": [
    [
      "00b6b550",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6b7b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b4b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6b390.md#insn-00b6b4b4) · [`00b6b46c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6b390.md#insn-00b6b46c)
- 新版 [`00b6b550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b42c.md#insn-00b6b550) · [`00b6b508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b42c.md#insn-00b6b508)

~~~diff
- 00b6b4b4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6b4b4 ["CBRANCH", null, ["local:b70:8", "tmp:0:1"]]
- 00b6b4b4 bytes 43130054
+ 00b6b550 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b6b550 ["CBRANCH", null, ["local:b70:8", "tmp:0:1"]]
+ 00b6b550 bytes 43130054
- 00b6b46c ["INT_EQUAL", "tmp:0:1", ["register:4070:8", "const:0:8"]]
- 00b6b46c ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
+ 00b6b508 ["INT_EQUAL", "tmp:0:1", ["register:4070:8", "const:0:8"]]
+ 00b6b508 ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
- 00b6b46c bytes 6e0200b4
+ 00b6b508 bytes 6e0200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-743b91d8c74f311e38f7f39bd2294d2b"></a>

### [`00b6b748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6b748.md) → [`00b6b7e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b7e4.md) _ZNK8firebase3fbs11ProjectInfo6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b980.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5ba50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba50.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 52.92% / 新版 52.92%

CFGの説明率　旧版 20.73% / 新版 20.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 42件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b7e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b81c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b824"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6b7e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6bc24"
      ]
    ],
    [
      "00b6b8ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6b82c"
      ]
    ],
    [
      "unmatched:00b6b81c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6bc24"
      ]
    ]
  ],
  "added": [
    [
      "00b6b87c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6bc24"
      ]
    ],
    [
      "00b6b8ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6b8c8"
      ]
    ],
    [
      "00b6b8b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6bc24"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b7c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6b748.md#insn-00b6b7c8) · [`00b6b7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6b748.md#insn-00b6b7d4) · [`00b6b7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6b748.md#insn-00b6b7e0)
- 新版 [`00b6b864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b7e4.md#insn-00b6b864) · [`00b6b870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b7e4.md#insn-00b6b870)

~~~diff
- 00b6b7c8 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b6b7c8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b6b7c8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b6b7c8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00b6b864 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00b6b864 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b6b864 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b6b864 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b6b7c8 bytes 68000036
+ 00b6b864 bytes 68000036
- 00b6b7d4 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b6b7d4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b6b7d4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b6b7d4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b6b870 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00b6b870 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b6b870 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b6b870 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b6b7d4 bytes 281d0037
+ 00b6b870 bytes 281d0037
- 00b6b7e0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6b7e0 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b6b7e0 ["CBRANCH", null, ["local:b104:8", "tmp:1:1"]]
- 00b6b7e0 bytes 491d0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1443d698adb4a39e406381337852597e"></a>

### [`00b6bb90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6bb90.md) → [`00b6bc2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6bc2c.md) _ZNK8firebase3fbs6Client6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9e0.md) · 呼出先 4件 [`00c5b950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b950.md) [`00c5b970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b970.md) [`00c5b9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9d0.md) [`00c5b9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9f0.md)
- 新版 呼出元 1件 [`00c5bab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bab0.md) · 呼出先 4件 [`00c5ba20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba20.md) [`00c5ba40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba40.md) [`00c5baa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5baa0.md) [`00c5bac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bac0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 63.10% / 新版 63.10%

CFGの説明率　旧版 44.12% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 35件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6bd0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6bd14"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6bd24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6bd0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6bd18"
      ]
    ],
    [
      "unmatched:00b6bd14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c09c"
      ]
    ],
    [
      "unmatched:00b6bd24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c0a0"
      ]
    ]
  ],
  "added": [
    [
      "00b6bda8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6bdb4"
      ]
    ],
    [
      "00b6bdb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c09c"
      ]
    ],
    [
      "00b6bdc0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c0a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6bcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6bb90.md#insn-00b6bcd8) · [`00b6bd0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6bb90.md#insn-00b6bd0c) · [`00b6bd14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6bb90.md#insn-00b6bd14)
- 新版 [`00b6bd74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6bc2c.md#insn-00b6bd74)

~~~diff
- 00b6bcd8 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00b6bcd8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b6bcd8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b6bcd8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00b6bd74 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00b6bd74 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b6bd74 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b6bd74 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b6bcd8 bytes 40190036
+ 00b6bd74 bytes 40190036
- 00b6bd0c ["CBRANCH", null, ["local:b31:8", "register:101:1"]]
- 00b6bd0c bytes 60000054
- 00b6bd14 ["INT_NOTEQUAL", "tmp:0:1", ["register:4060:4", "const:0:4"]]
- 00b6bd14 ["CBRANCH", null, ["local:b90:8", "tmp:0:1"]]
- 00b6bd14 bytes 6c170035
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e7a1733927bdd04383992cf8dd2e14e"></a>

### [`00b6c25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c25c.md) → [`00b6c2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6c2f8.md) _ZNK8firebase3fbs17AndroidClientInfo6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9c0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5ba90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba90.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.51% / 新版 91.51%

CFGの説明率　旧版 63.38% / 新版 64.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c2f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c318"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c338"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6c2f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c498"
      ]
    ],
    [
      "unmatched:00b6c318",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c400"
      ]
    ],
    [
      "00b6c3c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6c340"
      ]
    ]
  ],
  "added": [
    [
      "00b6c390",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c498"
      ]
    ],
    [
      "00b6c3b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c400"
      ]
    ],
    [
      "00b6c3c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c3dc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6c2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c25c.md#insn-00b6c2f4) · [`00b6c2fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c25c.md#insn-00b6c2fc) · [`00b6c318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c25c.md#insn-00b6c318)
- 新版 [`00b6c398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6c2f8.md#insn-00b6c398)

~~~diff
- 00b6c2f4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6c2f4 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b6c2f4 ["CBRANCH", null, ["local:b39:8", "tmp:1:1"]]
- 00b6c2f4 bytes 49080054
- 00b6c2fc ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6c2fc ["CBRANCH", null, ["local:b39:8", "tmp:0:1"]]
+ 00b6c398 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b6c398 ["CBRANCH", null, ["local:b38:8", "tmp:0:1"]]
- 00b6c2fc bytes 03080054
+ 00b6c398 bytes 03080054
- 00b6c318 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6c318 ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
- 00b6c318 bytes 680200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2ce34253794c76cdf2c205f303c255c"></a>

### [`00b6c404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c404.md) → [`00b6c4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6c4a0.md) _ZNK8firebase3fbs11OAuthClient6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b970.md) · 呼出先 1件 [`00c5b960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b960.md)
- 新版 呼出元 1件 [`00c5ba40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba40.md) · 呼出先 1件 [`00c5ba30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 88.75% / 新版 88.75%

CFGの説明率　旧版 75.23% / 新版 75.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c420"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c4e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c4f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6c420",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c4c8"
      ]
    ],
    [
      "unmatched:00b6c4e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c710"
      ]
    ],
    [
      "unmatched:00b6c4f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c59c"
      ]
    ]
  ],
  "added": [
    [
      "00b6c4bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c4c8"
      ]
    ],
    [
      "00b6c584",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c710"
      ]
    ],
    [
      "00b6c58c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c59c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6c420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c404.md#insn-00b6c420) · [`00b6c4e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c404.md#insn-00b6c4e8)
- 新版 [`00b6c4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6c4a0.md#insn-00b6c4bc)

~~~diff
- 00b6c420 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00b6c420 bytes 60000054
+ 00b6c4bc ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
+ 00b6c4bc bytes 60000054
- 00b6c4e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4088:4", "const:0:4"]]
- 00b6c4e8 ["CBRANCH", null, ["local:b59:8", "tmp:0:1"]]
- 00b6c4e8 bytes 710c0035
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a59b29f00b8d8860aad97a1fec45778"></a>

### [`00b6c684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c684.md) → [`00b6c720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6c720.md) _ZNK8firebase3fbs11AndroidInfo6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b960.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5ba30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba30.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.91% / 新版 96.91%

CFGの説明率　旧版 76.36% / 新版 76.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c790"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c840"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c8a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6c790",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c8b0"
      ]
    ],
    [
      "unmatched:00b6c840",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c8ec"
      ]
    ],
    [
      "unmatched:00b6c8a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c94c"
      ]
    ]
  ],
  "added": [
    [
      "00b6c82c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c8b0"
      ]
    ],
    [
      "00b6c8dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c8ec"
      ]
    ],
    [
      "00b6c93c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c94c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6c790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c684.md#insn-00b6c790) · [`00b6c840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c684.md#insn-00b6c840)
- 新版 [`00b6c82c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6c720.md#insn-00b6c82c)

~~~diff
- 00b6c790 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6c790 ["CBRANCH", null, ["local:b36:8", "tmp:0:1"]]
- 00b6c790 bytes 280400b4
+ 00b6c82c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b6c82c ["CBRANCH", null, ["local:b36:8", "tmp:0:1"]]
+ 00b6c82c bytes 280400b4
- 00b6c840 ["CBRANCH", null, ["local:b43:8", "register:102:1"]]
- 00b6c840 bytes 82000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c03d295ceac82b67fdaaeec8c1b72da3"></a>

### [`00b6c90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c90c.md) → [`00b6c9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6c9a8.md) _ZNK8firebase3fbs6ApiKey6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9d0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5baa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5baa0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 68.57% / 新版 69.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c9e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ca48"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ca7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6c9e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ca94"
      ]
    ],
    [
      "unmatched:00b6ca48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6caf4"
      ]
    ],
    [
      "unmatched:00b6ca7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6cb48"
      ]
    ]
  ],
  "added": [
    [
      "00b6ca84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ca94"
      ]
    ],
    [
      "00b6cae4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6caf4"
      ]
    ],
    [
      "00b6cb18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6cb48"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6c9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c90c.md#insn-00b6c9ac) · [`00b6c9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c90c.md#insn-00b6c9e0) · [`00b6c9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c90c.md#insn-00b6c9e8)
- 新版 [`00b6ca48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6c9a8.md#insn-00b6ca48) · [`00b6ca7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6c9a8.md#insn-00b6ca7c)

~~~diff
- 00b6c9ac ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6c9ac ["CBRANCH", null, ["local:b38:8", "tmp:0:1"]]
+ 00b6ca48 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b6ca48 ["CBRANCH", null, ["local:b37:8", "tmp:0:1"]]
- 00b6c9ac bytes 03080054
+ 00b6ca48 bytes 03080054
- 00b6c9e0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4078:4", "const:0:4"]]
- 00b6c9e0 ["CBRANCH", null, ["local:b38:8", "tmp:0:1"]]
+ 00b6ca7c ["INT_NOTEQUAL", "tmp:0:1", ["register:4078:4", "const:0:4"]]
+ 00b6ca7c ["CBRANCH", null, ["local:b37:8", "tmp:0:1"]]
- 00b6c9e0 bytes 6f060035
+ 00b6ca7c bytes 6f060035
- 00b6c9e8 ["CBRANCH", null, ["local:b21:8", "register:102:1"]]
- 00b6c9e8 bytes 82000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-161492a8e4a1157b8d0b3941537505e7"></a>

### [`00b6cab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6cab4.md) → [`00b6cb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6cb50.md) _ZNK8firebase3fbs8Services6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9f0.md) · 呼出先 2件 [`00c5b940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b940.md) [`00c5b9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9a0.md)
- 新版 呼出元 1件 [`00c5bac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bac0.md) · 呼出先 2件 [`00c5ba10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba10.md) [`00c5ba70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba70.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 82.27% / 新版 82.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6cca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6cd00"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6cd28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6cca8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6cec4"
      ]
    ],
    [
      "unmatched:00b6cd00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6cec0"
      ]
    ],
    [
      "unmatched:00b6cd28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6cec4"
      ]
    ]
  ],
  "added": [
    [
      "00b6cd44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6cec4"
      ]
    ],
    [
      "00b6cd9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6cec0"
      ]
    ],
    [
      "00b6cdc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6cec4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6cca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6cab4.md#insn-00b6cca8) · [`00b6cd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6cab4.md#insn-00b6cd00) · [`00b6cd28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6cab4.md#insn-00b6cd28)

~~~diff
- 00b6cca8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6cca8 ["CBRANCH", null, ["local:b75:8", "tmp:0:1"]]
- 00b6cca8 bytes 030c0054
- 00b6cd00 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6cd00 ["CBRANCH", null, ["local:b74:8", "tmp:0:1"]]
- 00b6cd00 bytes 23090054
- 00b6cd28 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6cd28 ["CBRANCH", null, ["local:b75:8", "tmp:0:1"]]
- 00b6cd28 bytes 03080054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fef8219a0cd38b264a4db44129672026"></a>

### [`00b6ce34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6ce34.md) → [`00b6ced0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6ced0.md) _ZNK8firebase3fbs16AnalyticsService6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9a0.md) · 呼出先 1件 [`00c5b9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9b0.md)
- 新版 呼出元 1件 [`00c5ba70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba70.md) · 呼出先 1件 [`00c5ba80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba80.md)

変更の種類 branch_condition_or_target, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 72.46% / 新版 72.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6cf80"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6d01c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6cfd0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6cf80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d05c"
      ]
    ]
  ],
  "added": [
    [
      "00b6d01c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d05c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6cf80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6ce34.md#insn-00b6cf80) · [`00b6cfd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6ce34.md#insn-00b6cfd0)
- 新版 [`00b6d01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6ced0.md#insn-00b6d01c)

~~~diff
- 00b6cf80 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6cf80 ["CBRANCH", null, ["local:b36:8", "tmp:0:1"]]
- 00b6cf80 bytes 03020054
- 00b6cfd0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6cfd0 ["RETURN", null, ["register:0:8"]]
- 00b6cfd0 bytes c0035fd6
+ 00b6d01c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b6d01c ["CBRANCH", null, ["local:b37:8", "tmp:0:1"]]
+ 00b6d01c bytes 03020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fdccee9814eab10dc81433fa55c9a82"></a>

### [`00b6cfd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6cfd4.md) → [`00b6d070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d070.md) _ZNK8firebase3fbs17AnalyticsProperty6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9b0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5ba80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba80.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 89.62% / 新版 89.62%

CFGの説明率　旧版 65.71% / 新版 63.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d09c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d0a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d0b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6d09c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d154"
      ]
    ],
    [
      "unmatched:00b6d0a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d210"
      ]
    ],
    [
      "unmatched:00b6d0b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d15c"
      ]
    ]
  ],
  "added": [
    [
      "00b6d138",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d154"
      ]
    ],
    [
      "00b6d144",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d210"
      ]
    ],
    [
      "00b6d14c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d15c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6cfd4.md#insn-00b6d074) · [`00b6d090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6cfd4.md#insn-00b6d090) · [`00b6d09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6cfd4.md#insn-00b6d09c)
- 新版 [`00b6d110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d070.md#insn-00b6d110) · [`00b6d12c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d070.md#insn-00b6d12c)

~~~diff
- 00b6d074 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6d074 ["CBRANCH", null, ["local:b38:8", "tmp:0:1"]]
+ 00b6d110 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b6d110 ["CBRANCH", null, ["local:b40:8", "tmp:0:1"]]
- 00b6d074 bytes 03080054
+ 00b6d110 bytes 03080054
- 00b6d090 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6d090 ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
+ 00b6d12c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b6d12c ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
- 00b6d090 bytes 680200b4
+ 00b6d12c bytes 680200b4
- 00b6d09c ["CBRANCH", null, ["local:b20:8", "register:101:1"]]
- 00b6d09c bytes e0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be7a2b6ad6a155b4b80f3d386ea90c1b"></a>

### [`00b6d17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d17c.md) → [`00b6d218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d218.md) _ZNK8firebase3fbs10AdsService6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b940.md) · 呼出先 1件 [`00c5b9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9a0.md)
- 新版 呼出元 1件 [`00c5ba10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba10.md) · 呼出先 1件 [`00c5ba70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba70.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 59.26% / 新版 59.26%

CFGの説明率　旧版 34.00% / 新版 34.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 31件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d204"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d260"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d268"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6d204",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d564"
      ]
    ],
    [
      "unmatched:00b6d260",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d568"
      ]
    ],
    [
      "unmatched:00b6d268",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d314"
      ]
    ]
  ],
  "added": [
    [
      "00b6d2a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d564"
      ]
    ],
    [
      "00b6d2fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d568"
      ]
    ],
    [
      "00b6d304",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d314"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d17c.md#insn-00b6d204) · [`00b6d248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d17c.md#insn-00b6d248) · [`00b6d254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d17c.md#insn-00b6d254)
- 新版 [`00b6d2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d218.md#insn-00b6d2e4) · [`00b6d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d218.md#insn-00b6d2f0)

~~~diff
- 00b6d204 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6d204 ["CBRANCH", null, ["local:b80:8", "tmp:0:1"]]
- 00b6d204 bytes 23160054
- 00b6d248 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6d248 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
+ 00b6d2e4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b6d2e4 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 00b6d248 bytes 880100b4
+ 00b6d2e4 bytes 880100b4
- 00b6d254 ["CBRANCH", null, ["local:b20:8", "register:101:1"]]
+ 00b6d2f0 ["CBRANCH", null, ["local:b21:8", "register:101:1"]]
- 00b6d254 bytes e0000054
+ 00b6d2f0 bytes e0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20bef496bfb6cba61b64d7ecc7c6d3b6"></a>

### [`00b6d4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d4dc.md) → [`00b6d578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d578.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EED2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b8f0.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba10.md) [`00c5be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be40.md)
- 新版 呼出元 1件 [`00c5b9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b9c0.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bae0.md) [`00c5bf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 33.33% / 新版 31.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d524"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d550"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b6d5c0"
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
      "unmatched:00b6d524",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00b6d550",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6d5c0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00b6d5ec",
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

- 旧版 [`00b6d524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d4dc.md#insn-00b6d524) · [`00b6d550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d4dc.md#insn-00b6d550)
- 新版 [`00b6d5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d578.md#insn-00b6d5c0)

~~~diff
- 00b6d524 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6d524 ["INT_ADD", "register:40f0:8", ["const:b6d524:8", "const:4:8"]]
- 00b6d524 ["CALLIND", null, ["register:0:8"]]
- 00b6d524 bytes 00013fd6
- 00b6d550 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6d550 ["INT_ADD", "register:40f0:8", ["const:b6d550:8", "const:4:8"]]
- 00b6d550 ["CALLIND", null, ["register:0:8"]]
- 00b6d550 bytes 00013fd6
+ 00b6d5c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6d5c0 ["INT_ADD", "register:40f0:8", ["const:b6d5c0:8", "const:4:8"]]
+ 00b6d5c0 ["CALLIND", null, ["register:0:8"]]
+ 00b6d5c0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00485d9974027a02650631f6de10d193"></a>

### [`00b6d650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d650.md) → [`00b6d6ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d6ec.md) _ZN11flatbuffers11SymbolTableINS_7EnumDefEED2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b8c0.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b870.md) [`00c5b920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b920.md) [`00c5ba60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba60.md) [`00c5ba70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba70.md)
- 新版 呼出元 1件 [`00c5b990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b990.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b940.md) [`00c5b9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b9f0.md) [`00c5bb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb30.md) [`00c5bb40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 72.41% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d670"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6d70c"
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
      "unmatched:00b6d670",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d768"
      ]
    ]
  ],
  "added": [
    [
      "00b6d70c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d768"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d650.md#insn-00b6d670) · [`00b6d66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d650.md#insn-00b6d66c)
- 新版 [`00b6d70c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d6ec.md#insn-00b6d70c)

~~~diff
- 00b6d670 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b6d670 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b6d670 bytes e1020054
+ 00b6d70c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b6d70c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b6d70c bytes e1020054
- 00b6d66c ["INT_LESSEQUAL", "register:105:1", ["register:4040:8", "register:40a0:8"]]
- 00b6d66c ["INT_SBORROW", "register:106:1", ["register:40a0:8", "register:4040:8"]]
- 00b6d66c ["INT_SUB", "tmp:0:8", ["register:40a0:8", "register:4040:8"]]
- 00b6d66c ["INT_SLESS", "register:107:1", ["tmp:0:8", "const:0:8"]]
- 00b6d66c bytes 9f0208eb
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f43c3479e7aee5de4fa61a1cbe1d6ee9"></a>

### [`00b6d738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d738.md) → [`00b6d7d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d7d4.md) _ZN11flatbuffers11SymbolTableINS_9StructDefEED2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b8e0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b870.md) [`00c5b8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b8d0.md) [`00c5baa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5baa0.md)
- 新版 呼出元 1件 [`00c5b9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b9b0.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b940.md) [`00c5b9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b9a0.md) [`00c5bb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb70.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 81.82% / 新版 78.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d7d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6d86c"
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
      "unmatched:00b6d7d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d824"
      ]
    ]
  ],
  "added": [
    [
      "00b6d86c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d824"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d738.md#insn-00b6d7d0) · [`00b6d764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d738.md#insn-00b6d764)
- 新版 [`00b6d86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d7d4.md#insn-00b6d86c) · [`00b6d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d7d4.md#insn-00b6d800)

~~~diff
- 00b6d7d0 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00b6d7d0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b6d7d0 bytes d6fdffb4
+ 00b6d86c ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
+ 00b6d86c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b6d86c bytes d6fdffb4
- 00b6d764 ["INT_ADD", "register:40f0:8", ["const:b6d764:8", "const:4:8"]]
- 00b6d764 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6d800 ["INT_ADD", "register:40f0:8", ["const:b6d800:8", "const:4:8"]]
+ 00b6d800 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6d764 bytes d3a90394
+ 00b6d800 bytes e0a90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e34aad611573f46d1987719bf054211"></a>

### [`00b70efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b70/00b70efc.md) → [`00b70f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b70/00b70f98.md) _ZN11flatbuffers6ToUTF8EjPNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c7f0.md) · 呼出先 1件 [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md)
- 新版 呼出元 1件 [`00c5c8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c8c0.md) · 呼出先 1件 [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.49% / 新版 94.49%

CFGの説明率　旧版 61.54% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70f20"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70f5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b70fbc"
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
      "unmatched:00b70f20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b70fcc"
      ]
    ],
    [
      "unmatched:00b70f5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b71008"
      ]
    ],
    [
      "unmatched:00b70f68",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b71028"
      ]
    ]
  ],
  "added": [
    [
      "00b70fbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b70fcc"
      ]
    ],
    [
      "00b70ff8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b71008"
      ]
    ],
    [
      "00b71018",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b71028"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b70f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b70/00b70efc.md#insn-00b70f20) · [`00b70f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b70/00b70efc.md#insn-00b70f5c)
- 新版 [`00b70fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b70/00b70f98.md#insn-00b70fbc)

~~~diff
- 00b70f20 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b70f20 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b70f20 ["CBRANCH", null, ["local:b2:8", "tmp:1:1"]]
- 00b70f20 bytes 88000054
- 00b70f5c ["CBRANCH", null, ["local:b10:8", "register:102:1"]]
- 00b70f5c bytes 82000054
+ 00b70fbc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b70fbc ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00b70fbc ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
+ 00b70fbc bytes 88000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9e23f5a51dd0fd5de36f5cdfab2669e"></a>

### [`00b72da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b72da4.md) → [`00b72e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b72e40.md) _ZN11flatbuffers11SymbolTableINS_8FieldDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c0a0.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5c170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c170.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.73% / 新版 92.73%

CFGの説明率　旧版 58.33% / 新版 56.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72dbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72dbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72dd8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b72dbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b72dd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b72fa0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72f1c"
      ]
    ]
  ],
  "added": [
    [
      "00b72e58",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b72e74",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b72e8c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72f1c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b72da4.md#insn-00b72dbc) · [`00b72dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b72da4.md#insn-00b72dd8) · [`00b72dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b72da4.md#insn-00b72dec)

~~~diff
- 00b72dbc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b72dbc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b72dbc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b72dbc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b72dbc bytes fd7b06a9
- 00b72dd8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b72dd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b72dd8 bytes e80700f9
- 00b72dec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:20:8"]]
- 00b72dec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b72dec bytes 891200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9634eb38c0da081f9b9d60ea5e3e2a4f"></a>

### [`00b7ca48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7c/00b7ca48.md) → [`00b7cae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7c/00b7cae4.md) _ZN11flatbuffers6Parser9ParseHashERNS_5ValueEPNS_8FieldDefE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c7b0.md) · 呼出先 11件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md) [`00c5bfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfe0.md) [`00c5bff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bff0.md)
- 新版 呼出元 1件 [`00c5c880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c880.md) · 呼出先 11件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md) [`00c5c0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0b0.md) [`00c5c0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0c0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 46.05% / 新版 46.05%

CFGの説明率　旧版 8.97% / 新版 9.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 22件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7ce80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7ce84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b7cf1c"
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
      "unmatched:00b7cae4",
      "DATA",
      [
        "storage",
        "0030e186",
        "switchD_00b7caec::switchdataD_0030e186",
        "byte"
      ]
    ],
    [
      "00b7cb88",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00b7cb50"
      ]
    ],
    [
      "00b7cb88",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00b7cb28"
      ]
    ]
  ],
  "added": [
    [
      "00b7cb80",
      "DATA",
      [
        "storage",
        "0030e1c6",
        "switchD_00b7cb88::switchdataD_0030e1c6",
        "byte"
      ]
    ],
    [
      "00b7cb88",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00b7cbec"
      ]
    ],
    [
      "00b7cb88",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00b7cbc4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7cb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7c/00b7ca48.md#insn-00b7cb1c) · [`00b7cb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7c/00b7ca48.md#insn-00b7cb30) · [`00b7cb44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7c/00b7ca48.md#insn-00b7cb44)

~~~diff
- 00b7cb1c ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00b7cb1c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b7cb1c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b7cb1c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b7cb1c bytes e9020037
- 00b7cb30 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00b7cb30 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b7cb30 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b7cb30 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b7cb30 bytes e9030037
- 00b7cb44 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00b7cb44 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b7cb44 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b7cb44 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b7cb44 bytes e9040037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a1adefec69cb325f1773c9ce7075b10"></a>

### [`00b7d04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7d04c.md) → [`00b7d0e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d0e8.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementIhEEvtT_S3_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1e0.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)
- 新版 呼出元 1件 [`00c5c2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c2b0.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.98% / 新版 92.98%

CFGの説明率　旧版 45.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7d110"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b7d1ac"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7d04c.md#insn-00b7d110) · [`00b7d078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7d04c.md#insn-00b7d078)
- 新版 [`00b7d1ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d0e8.md#insn-00b7d1ac) · [`00b7d114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7d/00b7d0e8.md#insn-00b7d114)

~~~diff
- 00b7d110 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:48:8"]]
- 00b7d110 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b7d110 bytes 882600f9
+ 00b7d1ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:48:8"]]
+ 00b7d1ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b7d1ac bytes 882600f9
- 00b7d078 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b7d078 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 00b7d114 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00b7d114 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00b7d078 bytes 48050034
+ 00b7d114 bytes 48050034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-deabf76c758259d5b51eb656d3eca32a"></a>

### [`00b7e2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7e/00b7e2c0.md) → [`00b7e35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b7e/00b7e35c.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIijEET0_T_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c240.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)
- 新版 呼出元 1件 [`00c5c310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c310.md) · 呼出先 1件 [`00c5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c270.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.93% / 新版 87.93%

CFGの説明率　旧版 11.11% / 新版 10.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e338"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e348"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b7e3d4"
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
      "unmatched:00b7e2f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7e3f4"
      ]
    ],
    [
      "unmatched:00b7e33c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7e3f4"
      ]
    ],
    [
      "00b7e3f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b7e344"
      ]
    ]
  ],
  "added": [
    [
      "00b7e394",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7e3f4"
      ]
    ],
    [
      "00b7e3d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7e3f4"
      ]
    ],
    [
      "00b7e3f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7e3e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7e/00b7e2c0.md#insn-00b7e2f8) · [`00b7e338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7e/00b7e2c0.md#insn-00b7e338) · [`00b7e33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7e/00b7e2c0.md#insn-00b7e33c)

~~~diff
- 00b7e2f8 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00b7e2f8 bytes 00030054
- 00b7e338 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b7e338 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b7e338 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00b7e338 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b7e338 bytes 3f010039
- 00b7e33c ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00b7e33c bytes e0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-354ec2ea324a12a043b704a52a24a99e"></a>

### [`00b8126c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b81/00b8126c.md) → [`00b81308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b81/00b81308.md) _ZN11flatbuffers11NumToStringIsEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c020.md) · 呼出先 8件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c581b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581b0.md) [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)
- 新版 呼出元 1件 [`00c5c0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0f0.md) · 呼出先 8件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58280.md) [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.22% / 新版 80.22%

CFGの説明率　旧版 33.33% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b812dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b812e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81354"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b812a0",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b812a4",
      "READ",
      [
        "storage",
        "00c9b840",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b812dc",
      "DATA",
      [
        "storage",
        "00c90bd0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b8133c",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00b81340",
      "READ",
      [
        "storage",
        "00c9b910",
        null,
        "pointer"
      ]
    ],
    [
      "00b81378",
      "DATA",
      [
        "storage",
        "00c90ca0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b812dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b81/00b8126c.md#insn-00b812dc) · [`00b812e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b81/00b8126c.md#insn-00b812e0) · [`00b81354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b81/00b8126c.md#insn-00b81354)

~~~diff
- 00b812dc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 00b812dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b812dc bytes e84b00f9
- 00b812e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b812e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b812e0 bytes fb1300f9
- 00b81354 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:68:8"]]
- 00b81354 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b81354 bytes e083863c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a767ef37d83bb7ee1e60ca0a3983f7b8"></a>

### [`00b82b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b82/00b82b78.md) → [`00b82c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82c14.md) _ZN11flatbuffers7EnumDef16RemoveDuplicatesEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c810.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5b920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b920.md)
- 新版 呼出元 1件 [`00c5c8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c8e0.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5b9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b9f0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 82.93% / 新版 82.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82c6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b82d08"
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
      "unmatched:00b82c6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b82cf4"
      ]
    ]
  ],
  "added": [
    [
      "00b82d08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b82cf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b82/00b82b78.md#insn-00b82c6c) · [`00b82bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b82/00b82b78.md#insn-00b82bec)
- 新版 [`00b82d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82c14.md#insn-00b82d08) · [`00b82c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b82/00b82c14.md#insn-00b82c88)

~~~diff
- 00b82c6c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b82c6c ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00b82c6c bytes 61ffff54
+ 00b82d08 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b82d08 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
+ 00b82d08 bytes 61ffff54
- 00b82bec ["INT_ADD", "register:40f0:8", ["const:b82bec:8", "const:4:8"]]
- 00b82bec ["CALL", null, ["callee:00c5b9f0:8"]]
+ 00b82c88 ["INT_ADD", "register:40f0:8", ["const:b82c88:8", "const:4:8"]]
+ 00b82c88 ["CALL", null, ["callee:00c5b9f0:8"]]
- 00b82bec bytes 4d630394
+ 00b82c88 bytes 5a630394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e583e8022d92107a69dcacce1f0e7b0"></a>

### [`00b84808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b84/00b84808.md) → [`00b848a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b848a4.md) _ZN11flatbuffers11SymbolTableINS_4TypeEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c050.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5c120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c120.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 71.43% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8483c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b848d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8486c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8483c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8486c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b84934"
      ]
    ]
  ],
  "added": [
    [
      "00b848d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b84908",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b84934"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8483c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b84/00b84808.md#insn-00b8483c) · [`00b8486c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b84/00b84808.md#insn-00b8486c)
- 新版 [`00b848d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b84/00b848a4.md#insn-00b848d8)

~~~diff
- 00b8483c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b8483c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b8483c bytes e80700f9
- 00b8486c ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00b8486c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b8486c bytes 6a0100b5
+ 00b848d8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
+ 00b848d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b848d8 bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6ad8b5fa5927d4065a1181d7426783e"></a>

### [`00b8505c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b85/00b8505c.md) → [`00b850f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b85/00b850f8.md) _ZN11flatbuffers6Parser15UniqueNamespaceEPNS_9NamespaceE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c5d0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5c6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c6a0.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 46.58% / 新版 45.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 8件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b85234"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b852d0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b850ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b850ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b85208"
      ]
    ],
    [
      "unmatched:00b85110",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b85140"
      ]
    ],
    [
      "unmatched:00b85154",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b851d4"
      ]
    ]
  ],
  "added": [
    [
      "00b85148",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b85208"
      ]
    ],
    [
      "00b851ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b85140"
      ]
    ],
    [
      "00b851f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b851d4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8508c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b85/00b8505c.md#insn-00b8508c) · [`00b850ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b85/00b8505c.md#insn-00b850ac) · [`00b85100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b85/00b8505c.md#insn-00b85100)
- 新版 [`00b85128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b85/00b850f8.md#insn-00b85128)

~~~diff
- 00b8508c ["CBRANCH", null, ["local:b19:8", "register:101:1"]]
+ 00b85128 ["CBRANCH", null, ["local:b21:8", "register:101:1"]]
- 00b8508c bytes 00070054
+ 00b85128 bytes 00070054
- 00b850ac ["CBRANCH", null, ["local:b19:8", "register:101:1"]]
- 00b850ac bytes 00060054
- 00b85100 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b85100 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b85100 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b85100 ["COPY", "register:4010:8", ["tmp:0:8"]]
- 00b85100 bytes 02018b9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc9da482c09459b10293f17ab2656e97"></a>

### [`00b873cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b87/00b873cc.md) → [`00b87468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b87/00b87468.md) _ZN11flatbuffers6Parser13MarkGeneratedEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 37.50% / 新版 36.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b87414"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b87418"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b874b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b8748c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b87428"
      ]
    ],
    [
      "unmatched:00b8741c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b87408"
      ]
    ],
    [
      "unmatched:00b87424",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b874d8"
      ]
    ]
  ],
  "added": [
    [
      "00b8748c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b874c4"
      ]
    ],
    [
      "00b874b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b874a4"
      ]
    ],
    [
      "00b874c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b874d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b87414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b87/00b873cc.md#insn-00b87414) · [`00b87418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b87/00b873cc.md#insn-00b87418) · [`00b8741c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b87/00b873cc.md#insn-00b8741c)

~~~diff
- 00b87414 ["COPY", "tmp:0:4", ["register:4060:4"]]
- 00b87414 ["INT_ADD", "tmp:1:8", ["register:4078:8", "const:78:8"]]
- 00b87414 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b87414 bytes ece10139
- 00b87418 ["COPY", "tmp:0:4", ["register:4060:4"]]
- 00b87418 ["INT_ADD", "tmp:1:8", ["register:4080:8", "const:78:8"]]
- 00b87418 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b87418 bytes 0ce20139
- 00b8741c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b8741c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b8741c bytes 61ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6e2e91522924f5ad07aac5fdaccfeda"></a>

### [`00b89970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b89/00b89970.md) → [`00b89a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b89/00b89a0c.md) _ZN11flatbuffers6Parser24ParseProtoCurliesOrIdentEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5c6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c7c0.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 76.19% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b89a08"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b89aa4"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b89a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b89/00b89970.md#insn-00b89a08) · [`00b8998c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b89/00b89970.md#insn-00b8998c)
- 新版 [`00b89aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b89/00b89a0c.md#insn-00b89aa4) · [`00b89a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b89/00b89a0c.md#insn-00b89a28)

~~~diff
- 00b89a08 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b89a08 ["RETURN", null, ["register:0:8"]]
- 00b89a08 bytes c0035fd6
+ 00b89aa4 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b89aa4 ["RETURN", null, ["register:0:8"]]
+ 00b89aa4 bytes c0035fd6
- 00b8998c ["INT_ADD", "register:40f0:8", ["const:b8998c:8", "const:4:8"]]
- 00b8998c ["CALL", null, ["callee:00c5c7c0:8"]]
+ 00b89a28 ["INT_ADD", "register:40f0:8", ["const:b89a28:8", "const:4:8"]]
+ 00b89a28 ["CALL", null, ["callee:00c5c7c0:8"]]
- 00b8998c bytes 594b0394
+ 00b89a28 bytes 664b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8440501a0cc38416ac114360e76a0c2"></a>

### [`00b8a1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8a/00b8a1f8.md) → [`00b8a294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8a/00b8a294.md) _ZN11flatbuffers6Parser13ParseProtoKeyEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c560.md) · 呼出先 2件 [`00c5c6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6f0.md) [`00c5c750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c750.md)
- 新版 呼出元 1件 [`00c5c630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c630.md) · 呼出先 2件 [`00c5c7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c7c0.md) [`00c5c820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c820.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 92.42% / 新版 92.42%

CFGの説明率　旧版 48.00% / 新版 46.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8a1f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8a1fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8a1fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8a1f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8a1fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8a200",
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
      "00b8a294",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b8a298",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b8a29c",
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

- 旧版 [`00b8a1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8a/00b8a1f8.md#insn-00b8a1f8) · [`00b8a1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8a/00b8a1f8.md#insn-00b8a1fc) · [`00b8a200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8a/00b8a1f8.md#insn-00b8a200)

~~~diff
- 00b8a1f8 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b8a1f8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b8a1f8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b8a1f8 bytes f50f1df8
- 00b8a1fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b8a1fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b8a1fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b8a1fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8a1fc bytes f44f01a9
- 00b8a200 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b8a200 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b8a200 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b8a200 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8a200 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d21026a583acce4707eb3083a0b95f2"></a>

### [`00b8b010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8b010.md) → [`00b8b0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b0ac.md) _ZN11flexbuffers7Builder9EndVectorEmbb

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c910.md) · 呼出先 6件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5c8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c8b0.md)
- 新版 呼出元 1件 [`00c5c9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c9e0.md) · 呼出先 6件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5c980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c980.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 82.14% / 新版 85.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8b118"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8b118"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b8b1b4"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b8b118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8b010.md#insn-00b8b118) · [`00b8b05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8b010.md#insn-00b8b05c)
- 新版 [`00b8b1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b0ac.md#insn-00b8b1b4) · [`00b8b0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8b0ac.md#insn-00b8b0f8)

~~~diff
- 00b8b118 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b8b118 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b8b118 ["COPY", "tmp:2:8", ["register:4040:8"]]
- 00b8b118 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8b118 bytes 145500a9
+ 00b8b1b4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00b8b1b4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
+ 00b8b1b4 ["COPY", "tmp:2:8", ["register:4040:8"]]
+ 00b8b1b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b8b1b4 bytes 145500a9
- 00b8b05c ["INT_ADD", "register:40f0:8", ["const:b8b05c:8", "const:4:8"]]
- 00b8b05c ["CALL", null, ["callee:00c5c980:8"]]
+ 00b8b0f8 ["INT_ADD", "register:40f0:8", ["const:b8b0f8:8", "const:4:8"]]
+ 00b8b0f8 ["CALL", null, ["callee:00c5c980:8"]]
- 00b8b05c bytes 15460394
+ 00b8b0f8 bytes 22460394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67ae826397793577cff1fc95ffa7d4d0"></a>

### [`00b8bb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8bb6c.md) → [`00b8bc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8b/00b8bc08.md) _ZN11flatbuffers6Parser9ParseJsonEPKcS2_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5ba10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba10.md) [`00c5c4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c4b0.md) [`00c5c5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c5b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5bae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bae0.md) [`00c5c580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c580.md) [`00c5c680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c680.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 46.67% / 新版 46.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8bb7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8bb7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8bb80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8bb7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8bb80",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8bb9c",
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
      "00b8bc18",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b8bc1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b8bc38",
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

- 旧版 [`00b8bb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8bb6c.md#insn-00b8bb7c) · [`00b8bb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8bb6c.md#insn-00b8bb80) · [`00b8bb9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8bb6c.md#insn-00b8bb9c)

~~~diff
- 00b8bb7c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b8bb7c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b8bb7c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b8bb7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8bb7c bytes f44f05a9
- 00b8bb80 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b8bb80 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b8bb80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b8bb80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8bb80 bytes fd7b06a9
- 00b8bb9c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b8bb9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b8bb9c bytes e80f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52807317c8454de25fef7d89fb28eecf"></a>

### [`00b8d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8d/00b8d7c0.md) → [`00b8d85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8d85c.md) _ZN11flatbuffers6Parser16CheckPrivateLeakEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c5f0.md) · 呼出先 1件 [`00c5c6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6d0.md)
- 新版 呼出元 1件 [`00c5c6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c6c0.md) · 呼出先 1件 [`00c5c7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c7a0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 79.49% / 新版 77.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8d8c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b8d960"
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
      "unmatched:00b8d8c4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5c7a0"
      ]
    ]
  ],
  "added": [
    [
      "00b8d960",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5c7a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8d828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8d/00b8d7c0.md#insn-00b8d828) · [`00b8d8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8d/00b8d7c0.md#insn-00b8d8c4)
- 新版 [`00b8d8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8d85c.md#insn-00b8d8c4) · [`00b8d960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b8d/00b8d85c.md#insn-00b8d960)

~~~diff
- 00b8d828 ["INT_ADD", "register:40f0:8", ["const:b8d828:8", "const:4:8"]]
- 00b8d828 ["CALL", null, ["callee:00c5c7a0:8"]]
+ 00b8d8c4 ["INT_ADD", "register:40f0:8", ["const:b8d8c4:8", "const:4:8"]]
+ 00b8d8c4 ["CALL", null, ["callee:00c5c7a0:8"]]
- 00b8d828 bytes aa3b0394
+ 00b8d8c4 bytes b73b0394
- 00b8d8c4 ["INT_ADD", "register:40f0:8", ["const:b8d8c4:8", "const:4:8"]]
- 00b8d8c4 ["CALL", null, ["callee:00c5c7a0:8"]]
- 00b8d8c4 bytes 833b0394
+ 00b8d960 ["INT_ADD", "register:40f0:8", ["const:b8d960:8", "const:4:8"]]
+ 00b8d960 ["CALL", null, ["callee:00c5c7a0:8"]]
+ 00b8d960 bytes 903b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b47f0a760b7ca2e518fb6a9f91dc06ad"></a>

### [`00b9062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b90/00b9062c.md) → [`00b906c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b906c8.md) _ZNK11flatbuffers10Definition19SerializeAttributesEPNS_21FlatBufferBuilderImplILb0EEERKNS_6ParserE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b92e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92e98.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b92f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92f34.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9062c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9062c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b906c8"
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
      "unmatched:00b9062c",
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
      "00b906c8",
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

- 旧版 [`00b9062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b90/00b9062c.md#insn-00b9062c) · [`00b90630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b90/00b9062c.md#insn-00b90630)
- 新版 [`00b906c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b90/00b906c8.md#insn-00b906c8)

~~~diff
- 00b9062c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b9062c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b9062c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00b9062c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b9062c bytes fd7bbfa9
+ 00b906c8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00b906c8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00b906c8 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00b906c8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b906c8 bytes fd7bbfa9
- 00b90630 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00b90630 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17e8110898694b6fa1fcbfc9bd3a34a0"></a>

### [`00b914a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b91/00b914a8.md) → [`00b91544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b91/00b91544.md) _ZNK11flatbuffers4Type9SerializeEPNS_21FlatBufferBuilderImplILb0EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c9d0.md) · 呼出先 1件 [`00c5bf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bf50.md)
- 新版 呼出元 1件 [`00c5caa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5caa0.md) · 呼出先 1件 [`00c5c020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c020.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 73.53% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b914c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b914ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b9155c"
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
      "unmatched:00b914c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b915ec"
      ]
    ],
    [
      "00b9156c",
      "DATA",
      [
        "storage",
        "0030e1aa",
        "switchD_00b914dc::switchdataD_0030e1aa",
        "byte"
      ]
    ],
    [
      "unmatched:00b914ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b915fc"
      ]
    ]
  ],
  "added": [
    [
      "00b9155c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b915ec"
      ]
    ],
    [
      "00b9156c",
      "DATA",
      [
        "storage",
        "0030e1ea",
        "switchD_00b91578::switchdataD_0030e1ea",
        "byte"
      ]
    ],
    [
      "00b91588",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b915fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b914c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b91/00b914a8.md#insn-00b914c0) · [`00b914ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b91/00b914a8.md#insn-00b914ec)
- 新版 [`00b9155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b91/00b91544.md#insn-00b9155c)

~~~diff
- 00b914c0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b914c0 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b914c0 ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
- 00b914c0 bytes 88040054
- 00b914ec ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b914ec ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00b914ec bytes a90300b5
+ 00b9155c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b9155c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00b9155c ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
+ 00b9155c bytes 88040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-157fef2026bf3daeb61d1077525b970c"></a>

### [`00b92cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92cc4.md) → [`00b92d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92d60.md) _ZN11flatbuffers11SymbolTableINS_7EnumValEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c080.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5c150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c150.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 50.00% / 新版 48.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92d28"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92d48"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b92dc4"
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
      "unmatched:00b92d28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b92df0"
      ]
    ],
    [
      "unmatched:00b92d48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b92ebc"
      ]
    ]
  ],
  "added": [
    [
      "00b92dc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b92df0"
      ]
    ],
    [
      "00b92de4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b92ebc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b92d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92cc4.md#insn-00b92d28) · [`00b92d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92cc4.md#insn-00b92d48)
- 新版 [`00b92dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92d60.md#insn-00b92dc4)

~~~diff
- 00b92d28 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00b92d28 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b92d28 bytes 6a0100b5
- 00b92d48 ["INT_EQUAL", "tmp:0:1", ["register:40d8:8", "const:0:8"]]
- 00b92d48 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00b92d48 bytes db0600b4
+ 00b92dc4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
+ 00b92dc4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b92dc4 bytes 6a0100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dfa69c32aa71408cccf4bbbfc2f85f0"></a>

### [`00b92e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92e7c.md) → [`00b92f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92f18.md) _ZNK11flatbuffers7EnumVal19SerializeAttributesEPNS_21FlatBufferBuilderImplILb0EEERKNS_6ParserE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b92e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92e98.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b92f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92f34.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92e7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92e7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b92f18"
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
      "unmatched:00b92e7c",
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
      "00b92f18",
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

- 旧版 [`00b92e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92e7c.md#insn-00b92e7c) · [`00b92e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92e7c.md#insn-00b92e80)
- 新版 [`00b92f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b92/00b92f18.md#insn-00b92f18)

~~~diff
- 00b92e7c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b92e7c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b92e7c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00b92e7c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b92e7c bytes fd7bbfa9
+ 00b92f18 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00b92f18 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00b92f18 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00b92f18 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b92f18 bytes fd7bbfa9
- 00b92e80 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00b92e80 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0200dda118f54833b033e5e8c3aadd02"></a>

### [`00b959b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b959b0.md) → [`00b95a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95a4c.md) _ZN11flatbuffers11EqualByNameERKNS_4TypeES2_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bfd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfd0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5c0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0a0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 86.00% / 新版 86.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b95ac4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b95acc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b95b60"
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
      "unmatched:00b95acc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b95bb8"
      ]
    ]
  ],
  "added": [
    [
      "00b95b68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b95bb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b95ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b959b0.md#insn-00b95ac4) · [`00b95acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b959b0.md#insn-00b95acc)
- 新版 [`00b95b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95a4c.md#insn-00b95b60)

~~~diff
- 00b95ac4 ["COPY", "tmp:0:8", ["register:4078:8"]]
- 00b95ac4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b95ac4 ["COPY", "tmp:0:8", ["register:4070:8"]]
- 00b95ac4 ["COPY", "register:4068:8", ["tmp:0:8"]]
- 00b95ac4 bytes ed018e9a
- 00b95acc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b95acc ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
- 00b95acc bytes 81020054
+ 00b95b60 ["COPY", "tmp:0:8", ["register:4078:8"]]
+ 00b95b60 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00b95b60 ["COPY", "tmp:0:8", ["register:4070:8"]]
+ 00b95b60 ["COPY", "register:4068:8", ["tmp:0:8"]]
+ 00b95b60 bytes ed018e9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ba015f6b13a827b9d14c108a6e1deb9"></a>

### [`00b95c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95c14.md) → [`00b95cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95cb0.md) _ZN11flatbuffers19StringToIntegerImplImEEbPT_PKcib

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1c0.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5d160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d160.md)
- 新版 呼出元 1件 [`00c5c290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c290.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5d230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d230.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.95% / 新版 91.95%

CFGの説明率　旧版 30.23% / 新版 28.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b95c44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b95ce0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b95d10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b95c44",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b95cfc",
      "READ",
      [
        "storage",
        "00c9b830",
        null,
        "pointer"
      ]
    ],
    [
      "00b95d54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b95cc4"
      ]
    ]
  ],
  "added": [
    [
      "00b95ce0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b95cf0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58190"
      ]
    ],
    [
      "00b95cfc",
      "READ",
      [
        "storage",
        "00c9b900",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b95c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95c14.md#insn-00b95c44) · [`00b95cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95c14.md#insn-00b95cb4)
- 新版 [`00b95d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95cb0.md#insn-00b95d50) · [`00b95ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95cb0.md#insn-00b95ce0)

~~~diff
- 00b95c44 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b95c44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b95c44 bytes e80700f9
- 00b95cb4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b95cb4 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 00b95d50 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b95d50 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00b95cb4 bytes 21010054
+ 00b95d50 bytes 21010054
+ 00b95ce0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
+ 00b95ce0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b95ce0 bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6d6b8d8e66eb2d905f49db32a5aeddb"></a>

### [`00b95e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95e50.md) → [`00b95eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95eec.md) _ZN11flatbuffers8HashFnv1ImEET_PKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b95e88"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b95f24"
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
      "unmatched:00b95e88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b95f14"
      ]
    ]
  ],
  "added": [
    [
      "00b95f24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b95f14"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b95e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95e50.md#insn-00b95e88) · [`00b95e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95e50.md#insn-00b95e60)
- 新版 [`00b95f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95eec.md#insn-00b95f24)

~~~diff
- 00b95e88 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
- 00b95e88 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b95e88 bytes 89ffff35
+ 00b95f24 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
+ 00b95f24 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b95f24 bytes 89ffff35
- 00b95e60 ["INT_AND", "register:4000:8", ["register:4000:8", "const:ffff0000ffffffff:8"]]
- 00b95e60 ["INT_OR", "register:4000:8", ["register:4000:8", "const:9ce400000000:8"]]
- 00b95e60 bytes 809cd3f2
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d59dacd8b09982846a6c877745e8ec3b"></a>

### [`00b95e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95e90.md) → [`00b95f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95f2c.md) _ZN11flatbuffers9HashFnv1aImEET_PKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 37.50% / 新版 37.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b95ea8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b95ec8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b95f44"
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
      "unmatched:00b95ea8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b95f68"
      ]
    ],
    [
      "unmatched:00b95ec8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b95eb8"
      ]
    ]
  ],
  "added": [
    [
      "00b95f44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b95f68"
      ]
    ],
    [
      "00b95f64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b95f54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b95ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95e90.md#insn-00b95ea8) · [`00b95ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95e90.md#insn-00b95ec8)
- 新版 [`00b95f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b95/00b95f2c.md#insn-00b95f44)

~~~diff
- 00b95ea8 ["INT_EQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
- 00b95ea8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b95ea8 bytes 29010034
- 00b95ec8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
- 00b95ec8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b95ec8 bytes 89ffff35
+ 00b95f44 ["INT_EQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
+ 00b95f44 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b95f44 bytes 29010034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab0c4e80e8a2712df6e9f34380798e12"></a>

### [`00b964a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b964a4.md) → [`00b96540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96540.md) _ZNSt6__ndk16vectorIPN11flatbuffers7EnumDefENS_9allocatorIS3_EEE6assignIPS3_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_co

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d060.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5d130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d130.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.21% / 新版 87.21%

CFGの説明率　旧版 62.50% / 新版 64.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b964a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b964a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b964a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b964a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b964a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b964ac",
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
      "00b96540",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b96544",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b96548",
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

- 旧版 [`00b964a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b964a4.md#insn-00b964a4) · [`00b964a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b964a4.md#insn-00b964a8) · [`00b964ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b964a4.md#insn-00b964ac)

~~~diff
- 00b964a4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b964a4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b964a4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b964a4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b964a4 bytes fa67bba9
- 00b964a8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b964a8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b964a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b964a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b964a8 bytes f85f01a9
- 00b964ac ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b964ac ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b964ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b964ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b964ac bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebf7cd4516a3e9e51f735c0895973cea"></a>

### [`00b965fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b965fc.md) → [`00b96698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b96/00b96698.md) _ZN11flatbuffers19StringToIntegerImplIlEEbPT_PKcib

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1b0.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5d150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d150.md)
- 新版 呼出元 1件 [`00c5c280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c280.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5d220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d220.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 91.95% / 新版 91.95%

CFGの説明率　旧版 76.74% / 新版 78.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b96600"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b96604"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b96604"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b96600",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b96604",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b96608",
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
      "00b9669c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b966a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b966a4",
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

- 旧版 [`00b96600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b965fc.md#insn-00b96600) · [`00b96604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b965fc.md#insn-00b96604) · [`00b96608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b965fc.md#insn-00b96608)

~~~diff
- 00b96600 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b96600 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00b96600 bytes f70b00f9
- 00b96604 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b96604 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b96604 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b96604 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b96604 bytes f65702a9
- 00b96608 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b96608 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b96608 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b96608 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b96608 bytes f44f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aab09fee6acdce4d586431c09590f6b8"></a>

### [`00b99354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b99354.md) → [`00b993f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b993f0.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE8overflowEi

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.81% / 新版 97.81%

CFGの説明率　旧版 89.58% / 新版 87.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b99548"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b995e4"
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
      "unmatched:00b99540",
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
      "00b995dc",
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

- 旧版 [`00b99548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b99354.md#insn-00b99548) · [`00b99404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b99354.md#insn-00b99404)
- 新版 [`00b995e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b993f0.md#insn-00b995e4) · [`00b994a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b993f0.md#insn-00b994a0)

~~~diff
- 00b99548 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b99548 ["RETURN", null, ["register:0:8"]]
- 00b99548 bytes c0035fd6
+ 00b995e4 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b995e4 ["RETURN", null, ["register:0:8"]]
+ 00b995e4 bytes c0035fd6
- 00b99404 ["INT_ADD", "register:40f0:8", ["const:b99404:8", "const:4:8"]]
- 00b99404 ["CALL", null, ["callee:00c5a9b0:8"]]
+ 00b994a0 ["INT_ADD", "register:40f0:8", ["const:b994a0:8", "const:4:8"]]
+ 00b994a0 ["CALL", null, ["callee:00c5a9b0:8"]]
- 00b99404 bytes 37050394
+ 00b994a0 bytes 44050394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2f97b214d2a8e8e39a00acb2bf8bf90"></a>

### [`00b9958c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b9958c.md) → [`00b99628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b99628.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

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
      "site": "00b9958c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b99590"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b99590"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9958c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b99590",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b99638",
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b99628",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b9962c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b99638",
      "READ",
      [
        "storage",
        "00c9b918",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9958c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b9958c.md#insn-00b9958c) · [`00b99590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b9958c.md#insn-00b99590) · [`00b995a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b9958c.md#insn-00b995a8)

~~~diff
- 00b9958c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b9958c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b9958c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b9958c bytes f30f1ef8
- 00b99590 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b99590 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b99590 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b99590 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b99590 bytes fd7b01a9
- 00b995a8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b995a8 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b995a8 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
- 00b995a8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b995a8 bytes 088400f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54f1378c1c895db0f3f4b1d254e0535e"></a>

### [`00b996e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b996e0.md) → [`00b9977c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b99/00b9977c.md) _ZNKSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c581b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581b0.md) · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c58280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58280.md) · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 60.31% / 新版 60.31%

CFGの説明率　旧版 25.40% / 新版 27.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9974c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b99790"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b997c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9973c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b99984"
      ]
    ],
    [
      "unmatched:00b99744",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b99848"
      ]
    ],
    [
      "unmatched:00b99754",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9996c"
      ]
    ]
  ],
  "added": [
    [
      "00b997d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b99984"
      ]
    ],
    [
      "00b997e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b99848"
      ]
    ],
    [
      "00b997f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9996c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9973c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b996e0.md#insn-00b9973c) · [`00b99744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b996e0.md#insn-00b99744) · [`00b9974c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b996e0.md#insn-00b9974c)

~~~diff
- 00b9973c ["CBRANCH", null, ["local:b41:8", "register:102:1"]]
- 00b9973c bytes 620d0054
- 00b99744 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b99744 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b99744 ["CBRANCH", null, ["local:b18:8", "tmp:1:1"]]
- 00b99744 bytes 48030054
- 00b9974c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b9974c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b9974c ["INT_ADD", "register:4098:8", ["register:4098:8", "const:1:8"]]
- 00b9974c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b9974c bytes 68160038
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

