# v16.0.1 → v16.0.2 · 最優先の変更候補 (51)

[一覧の目次](README.md)

<a id="compare-8487bdb34d38406169aaa991bc8e4ce2"></a>

### [`008c8e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c8/008c8e0c.md) → [`008c8e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c8/008c8e60.md) FUN_008c8e60

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008cf91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf91c.md) · 呼出先 14件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008c4290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c4/008c4290.md) [`008c7b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c7/008c7b40.md)
- 新版 呼出元 1件 [`008cf970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf970.md) · 呼出先 14件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008c42e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c4/008c42e4.md) [`008c7b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c7/008c7b94.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 38.12% / 新版 39.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008c8e10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008c8e14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008c8e14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008c8e10",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:008c8e14",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008c8f28",
      "DATA",
      [
        "storage",
        "0039b97c",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "008c8e64",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "008c8e68",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008c8f28",
      "DATA",
      [
        "storage",
        "0039b97c",
        null,
        "byte[23]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c8e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c8/008c8e0c.md#insn-008c8e10) · [`008c8e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c8/008c8e0c.md#insn-008c8e14)
- 新版 [`008c8e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c8/008c8e60.md#insn-008c8e64)

~~~diff
- 008c8e10 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 008c8e10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 008c8e10 bytes e83300fd
- 008c8e14 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008c8e14 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008c8e14 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 008c8e14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008c8e14 bytes fd7b07a9
+ 008c8e64 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
+ 008c8e64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
+ 008c8e64 bytes e83300fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80c5468d4006807a87ce9bfd954d91be"></a>

### [`008c990c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c9/008c990c.md) → [`008c9960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c9/008c9960.md) FUN_008c9960

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008cb644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb644.md) · 呼出先 15件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)
- 新版 呼出元 1件 [`008cb698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb698.md) · 呼出先 15件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00468844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468844.md) [`0046969c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/0046969c.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 84.07% / 新版 84.07%

CFGの説明率　旧版 17.78% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 2件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008c9934"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008c9b0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008c9b18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008c9930",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:008c9934",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008c99b0"
      ]
    ],
    [
      "unmatched:008c993c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008c9984",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008c9988",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008c99b0"
      ]
    ],
    [
      "008c9990",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c9934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c9/008c990c.md#insn-008c9934) · [`008c9950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c9/008c990c.md#insn-008c9950) · [`008c9988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c9/008c990c.md#insn-008c9988)
- 新版 [`008c99a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c9/008c9960.md#insn-008c99a4) · [`008c99dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c9/008c9960.md#insn-008c99dc)

~~~diff
- 008c9934 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008c9934 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 008c9934 bytes 480100b4
- 008c9950 ["INT_ADD", "register:40f0:8", ["const:8c9950:8", "const:4:8"]]
- 008c9950 ["CALL", null, ["callee:00c586e0:8"]]
+ 008c99a4 ["INT_ADD", "register:40f0:8", ["const:8c99a4:8", "const:4:8"]]
+ 008c99a4 ["CALL", null, ["callee:00c586e0:8"]]
- 008c9950 bytes 303b0e94
+ 008c99a4 bytes 4f3b0e94
- 008c9988 ["INT_ADD", "register:40f0:8", ["const:8c9988:8", "const:4:8"]]
- 008c9988 ["CALL", null, ["callee:00851550:8"]]
+ 008c99dc ["INT_ADD", "register:40f0:8", ["const:8c99dc:8", "const:4:8"]]
+ 008c99dc ["CALL", null, ["callee:00851550:8"]]
- 008c9988 bytes dc1efe97
+ 008c99dc bytes dd1efe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a67d944079de1d68e35a9d67f08bafb1"></a>

### [`008ca33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008ca33c.md) → [`008ca390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ca/008ca390.md) FUN_008ca390

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b1e088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1e088.md) · 呼出先 17件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487b80.md)
- 新版 呼出元 1件 [`00b1e124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1e/00b1e124.md) · 呼出先 17件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048796c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487bc0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.46% / 新版 82.46%

CFGの説明率　旧版 44.87% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_condition` 3件, `store_value` 1件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ca340"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ca340"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ca344"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ca340",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ca344",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ca348",
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
      "008ca394",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008ca398",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008ca39c",
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

- 旧版 [`008ca340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008ca33c.md#insn-008ca340) · [`008ca344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008ca33c.md#insn-008ca344) · [`008ca348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008ca33c.md#insn-008ca348)

~~~diff
- 008ca340 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008ca340 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008ca340 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:190:8"]]
- 008ca340 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ca340 bytes fd7b19a9
- 008ca344 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008ca344 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008ca344 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1a0:8"]]
- 008ca344 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ca344 bytes fc6f1aa9
- 008ca348 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 008ca348 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 008ca348 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1b0:8"]]
- 008ca348 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ca348 bytes fa671ba9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07edae947d1d8205c849823158988c94"></a>

### [`008ca754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008ca754.md) → [`008ca7a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ca/008ca7a8.md) FUN_008ca7a8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b1e088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1e088.md) · 呼出先 16件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)
- 新版 呼出元 1件 [`00b1e124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1e/00b1e124.md) · 呼出先 16件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048796c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.91% / 新版 89.91%

CFGの説明率　旧版 48.81% / 新版 51.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 1件, `store_value` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ca758"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ca758"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ca75c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ca758",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ca75c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ca798",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ca7ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008ca7b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008ca7ec",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ca758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008ca754.md#insn-008ca758) · [`008ca75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008ca754.md#insn-008ca75c) · [`008ca798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008ca754.md#insn-008ca798)

~~~diff
- 008ca758 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008ca758 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008ca758 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:190:8"]]
- 008ca758 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ca758 bytes fd7b19a9
- 008ca75c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008ca75c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008ca75c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1a0:8"]]
- 008ca75c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ca75c bytes fc6f1aa9
- 008ca798 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 008ca798 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008ca798 bytes e81700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bf6d69b356ddf2ac55e565ea8f56aa1"></a>

### [`008cb434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb434.md) → [`008cb488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb488.md) FUN_008cb488

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 13件 [`0044c884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c884.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048dc4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dc4c.md) [`0048eef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048eef0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 13件 [`0044c8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c8c4.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048dc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048dc8c.md) [`0048ef30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048ef30.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.05% / 新版 82.05%

CFGの説明率　旧版 31.91% / 新版 31.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_condition` 2件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cb4e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cb4e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cb4e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cb4d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008cb494"
      ]
    ],
    [
      "unmatched:008cb490",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cb5fc"
      ]
    ],
    [
      "unmatched:008cb49c",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "008cb4d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cb4e8"
      ]
    ],
    [
      "008cb4e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cb5fc"
      ]
    ],
    [
      "008cb4f0",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb47c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb434.md#insn-008cb47c) · [`008cb490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb434.md#insn-008cb490) · [`008cb4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb434.md#insn-008cb4a4)
- 新版 [`008cb4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb488.md#insn-008cb4d0)

~~~diff
- 008cb47c ["INT_ADD", "register:40f0:8", ["const:8cb47c:8", "const:4:8"]]
- 008cb47c ["CALL", null, ["callee:00ac84d4:8"]]
+ 008cb4d0 ["INT_ADD", "register:40f0:8", ["const:8cb4d0:8", "const:4:8"]]
+ 008cb4d0 ["CALL", null, ["callee:00ac84d4:8"]]
- 008cb47c bytes faf30794
+ 008cb4d0 bytes 01f40794
- 008cb490 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 008cb490 ["CBRANCH", null, ["local:b31:8", "tmp:0:1"]]
- 008cb490 bytes c8080034
- 008cb4a4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008cb4a4 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 008cb4a4 bytes 21040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eb3d12106d05083b4fefd6737b7a3d9"></a>

### [`008cb644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb644.md) → [`008cb698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb698.md) FUN_008cb698

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 18件 [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00859bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859bb0.md) · 呼出先 18件 [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046cac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cac4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.62% / 新版 89.62%

CFGの説明率　旧版 5.26% / 新版 5.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cb644"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cb644"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cb648"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008cb644",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:008cb648",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:008cb664",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008cb698",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008cb69c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "008cb6b8",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb644.md#insn-008cb644) · [`008cb648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb644.md#insn-008cb648) · [`008cb670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb644.md#insn-008cb670)

~~~diff
- 008cb644 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008cb644 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008cb644 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 008cb644 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008cb644 bytes fd7bbca9
- 008cb648 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008cb648 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 008cb648 bytes f70b00f9
- 008cb670 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008cb670 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 008cb670 bytes 200100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1897be49b8a5263b918c57d0f234ede2"></a>

### [`008cb7ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb7ec.md) → [`008cb840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb840.md) FUN_008cb840

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008cb8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb8b0.md) · 呼出先 5件 [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) [`006b21e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b21e4.md) [`0078dcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078dcac.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`008cb904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb904.md) · 呼出先 5件 [`00682364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682364.md) [`006b223c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b223c.md) [`0078dd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dd04.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 69.39% / 新版 69.39%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cb804"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cb834"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cb870"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008cb804",
      "DATA",
      [
        "storage",
        "00c83d30",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:008cb834",
      "DATA",
      [
        "storage",
        "00c78330",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:008cb848",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cb8b8"
      ]
    ]
  ],
  "added": [
    [
      "008cb858",
      "DATA",
      [
        "storage",
        "00c83e00",
        null,
        "pointer"
      ]
    ],
    [
      "008cb888",
      "DATA",
      [
        "storage",
        "00c78400",
        null,
        "pointer"
      ]
    ],
    [
      "008cb89c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cb8b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb7ec.md#insn-008cb804) · [`008cb80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb7ec.md#insn-008cb80c) · [`008cb81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb7ec.md#insn-008cb81c)
- 新版 [`008cb860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb840.md#insn-008cb860) · [`008cb870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb840.md#insn-008cb870)

~~~diff
- 008cb804 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008cb804 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008cb804 bytes 080000f9
- 008cb80c ["INT_ADD", "register:40f0:8", ["const:8cb80c:8", "const:4:8"]]
- 008cb80c ["CALL", null, ["callee:0078dd04:8"]]
+ 008cb860 ["INT_ADD", "register:40f0:8", ["const:8cb860:8", "const:4:8"]]
+ 008cb860 ["CALL", null, ["callee:0078dd04:8"]]
- 008cb80c bytes 2809fb97
+ 008cb860 bytes 2909fb97
- 008cb81c ["INT_ADD", "register:40f0:8", ["const:8cb81c:8", "const:4:8"]]
- 008cb81c ["CALL", null, ["callee:006b223c:8"]]
+ 008cb870 ["INT_ADD", "register:40f0:8", ["const:8cb870:8", "const:4:8"]]
+ 008cb870 ["CALL", null, ["callee:006b223c:8"]]
- 008cb81c bytes 729af797
+ 008cb870 bytes 739af797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b3847b819895ff09959c3cb2e0ef6e4"></a>

### [`008cb8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb8d8.md) → [`008cb92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb92c.md) FUN_008cb92c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cb94c",
      "incomplete_value": false,
      "site": "008cb950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb8f8",
      "incomplete_value": false,
      "site": "008cb8fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cb950",
      "DATA",
      [
        "storage",
        "00c83d68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cb950",
      "DATA",
      [
        "storage",
        "00c83e38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb8d8.md#insn-008cb8ec) · [`008cb8f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb8d8.md#insn-008cb8f8)
- 新版 [`008cb940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb92c.md#insn-008cb940) · [`008cb94c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb92c.md#insn-008cb94c)

~~~diff
- 008cb8ec ["INT_ADD", "register:40f0:8", ["const:8cb8ec:8", "const:4:8"]]
- 008cb8ec ["CALL", null, ["callee:00c57f60:8"]]
+ 008cb940 ["INT_ADD", "register:40f0:8", ["const:8cb940:8", "const:4:8"]]
+ 008cb940 ["CALL", null, ["callee:00c57f60:8"]]
- 008cb8ec bytes 69310e94
+ 008cb940 bytes 88310e94
- 008cb8f8 ["COPY", "tmp:0:8", ["const:d68:8"]]
- 008cb8f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cb8f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cb8f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cb94c ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 008cb94c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb94c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb94c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cb8f8 bytes 08a13591
+ 008cb94c bytes 08e13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30a5295bd03cbc0e58b0f3d62834cc02"></a>

### [`008cb910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb910.md) → [`008cb964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb964.md) FUN_008cb964

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cb968",
      "incomplete_value": false,
      "site": "008cb96c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb914",
      "incomplete_value": false,
      "site": "008cb918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "008cb96c",
      "DATA",
      [
        "storage",
        "00c83d68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cb96c",
      "DATA",
      [
        "storage",
        "00c83e38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb910.md#insn-008cb914)
- 新版 [`008cb968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb964.md#insn-008cb968)

~~~diff
- 008cb914 ["COPY", "tmp:0:8", ["const:d68:8"]]
- 008cb914 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cb914 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cb914 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cb968 ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 008cb968 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb968 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb968 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cb914 bytes 08a13591
+ 008cb968 bytes 08e13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90a600f6b35a9a6b280afc8248130beb"></a>

### [`008cb930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb930.md) → [`008cb984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb984.md) FUN_008cb984

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`00a46bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46bb8.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md) [`00a46c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46c0c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 94.58% / 新版 94.58%

CFGの説明率　旧版 59.02% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008cba7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008cba84"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbb0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008cb964",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "unmatched:008cb96c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "008cb9cc"
      ]
    ],
    [
      "008cb9c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "008cb9b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008cb9c0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "008cb9cc"
      ]
    ],
    [
      "008cb9c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb930.md#insn-008cb964) · [`008cb970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb930.md#insn-008cb970) · [`008cb9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb930.md#insn-008cb9b8)
- 新版 [`008cb9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb984.md#insn-008cb9c4) · [`008cba0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb984.md#insn-008cba0c)

~~~diff
- 008cb964 ["INT_ADD", "register:40f0:8", ["const:8cb964:8", "const:4:8"]]
- 008cb964 ["CALL", null, ["ram:47acf4:8"]]
- 008cb964 bytes e4bcee97
- 008cb970 ["INT_ADD", "register:40f0:8", ["const:8cb970:8", "const:4:8"]]
- 008cb970 ["CALL", null, ["ram:47acf4:8"]]
+ 008cb9c4 ["INT_ADD", "register:40f0:8", ["const:8cb9c4:8", "const:4:8"]]
+ 008cb9c4 ["CALL", null, ["ram:47ad34:8"]]
- 008cb970 bytes e1bcee97
+ 008cb9c4 bytes dcbcee97
- 008cb9b8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008cb9b8 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 008cba0c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 008cba0c ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 008cb9b8 bytes e80100b4
+ 008cba0c bytes e80100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07affff3ded7d749f5fa8f051845b1ae"></a>

### [`008cbbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbbf0.md) → [`008cbc44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbc44.md) FUN_008cbc44

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008bdb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bd/008bdb00.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`008bdb58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bd/008bdb58.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008cbc50",
      "incomplete_value": false,
      "site": "008cbc54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cbbfc",
      "incomplete_value": false,
      "site": "008cbc00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f4c:8"
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
      "008cbc50",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008cbc50",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cbc00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbbf0.md#insn-008cbc00) · [`008cbbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbbf0.md#insn-008cbbfc)
- 新版 [`008cbc54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbc44.md#insn-008cbc54) · [`008cbc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbc44.md#insn-008cbc50)

~~~diff
- 008cbc00 ["INT_ADD", "register:40f0:8", ["const:8cbc00:8", "const:4:8"]]
- 008cbc00 ["CALL", null, ["callee:0043b7b8:8"]]
+ 008cbc54 ["INT_ADD", "register:40f0:8", ["const:8cbc54:8", "const:4:8"]]
+ 008cbc54 ["CALL", null, ["callee:0043b7b8:8"]]
- 008cbc00 bytes debeed97
+ 008cbc54 bytes d9beed97
- 008cbbfc ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 008cbbfc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008cbbfc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008cbbfc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008cbc50 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 008cbc50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008cbc50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008cbc50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008cbbfc bytes 00303d91
+ 008cbc50 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47c22a5806e70127da9c11552ad44a07"></a>

### [`008cbc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbc58.md) → [`008cbcac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbcac.md) FUN_008cbcac

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.26% / 新版 98.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008cbce4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008cbc90",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008cbcf0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008cbc9c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008cbe08",
      "incomplete_value": true,
      "site": "008cbe0c",
      "value": [
        "INT_LEFT",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:2:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 5,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cbce4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008cbcf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008cbef8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008c385c"
      ]
    ]
  ],
  "added": [
    [
      "008cbce4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008cbcf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008cbd44",
      "DATA",
      [
        "storage",
        "0044ded0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cbc90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbc58.md#insn-008cbc90) · [`008cbc9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbc58.md#insn-008cbc9c) · [`008cbdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbc58.md#insn-008cbdb8)
- 新版 [`008cbce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbcac.md#insn-008cbce4) · [`008cbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbcac.md#insn-008cbcf0) · [`008cbe0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbcac.md#insn-008cbe0c)

~~~diff
- 008cbc90 ["INT_ADD", "register:40f0:8", ["const:8cbc90:8", "const:4:8"]]
- 008cbc90 ["CALL", null, ["ram:47acf4:8"]]
+ 008cbce4 ["INT_ADD", "register:40f0:8", ["const:8cbce4:8", "const:4:8"]]
+ 008cbce4 ["CALL", null, ["ram:47ad34:8"]]
- 008cbc90 bytes 19bcee97
+ 008cbce4 bytes 14bcee97
- 008cbc9c ["INT_ADD", "register:40f0:8", ["const:8cbc9c:8", "const:4:8"]]
- 008cbc9c ["CALL", null, ["ram:47acf4:8"]]
+ 008cbcf0 ["INT_ADD", "register:40f0:8", ["const:8cbcf0:8", "const:4:8"]]
+ 008cbcf0 ["CALL", null, ["ram:47ad34:8"]]
- 008cbc9c bytes 16bcee97
+ 008cbcf0 bytes 11bcee97
- 008cbdb8 ["INT_ADD", "register:40f0:8", ["const:8cbdb8:8", "const:4:8"]]
- 008cbdb8 ["CALL", null, ["callee:00c57f60:8"]]
+ 008cbe0c ["INT_ADD", "register:40f0:8", ["const:8cbe0c:8", "const:4:8"]]
+ 008cbe0c ["CALL", null, ["callee:00c57f60:8"]]
- 008cbdb8 bytes 36300e94
+ 008cbe0c bytes 55300e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bdbf243f8245ecb3e454343345c4195"></a>

### [`008cbf34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbf34.md) → [`008cbf88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbf88.md) FUN_008cbf88

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cbfac",
      "incomplete_value": false,
      "site": "008cbfac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cbf58",
      "incomplete_value": false,
      "site": "008cbf58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cbfac",
      "DATA",
      [
        "storage",
        "00c83e68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cbfac",
      "DATA",
      [
        "storage",
        "00c83f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cbf48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbf34.md#insn-008cbf48) · [`008cbf54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbf34.md#insn-008cbf54)
- 新版 [`008cbf9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbf88.md#insn-008cbf9c) · [`008cbfa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbf88.md#insn-008cbfa8)

~~~diff
- 008cbf48 ["INT_ADD", "register:40f0:8", ["const:8cbf48:8", "const:4:8"]]
- 008cbf48 ["CALL", null, ["callee:00c57f60:8"]]
+ 008cbf9c ["INT_ADD", "register:40f0:8", ["const:8cbf9c:8", "const:4:8"]]
+ 008cbf9c ["CALL", null, ["callee:00c57f60:8"]]
- 008cbf48 bytes d22f0e94
+ 008cbf9c bytes f12f0e94
- 008cbf54 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 008cbf54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cbf54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cbf54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cbfa8 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 008cbfa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cbfa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cbfa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cbf54 bytes 08a13991
+ 008cbfa8 bytes 08e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9568a6e15c735971f62b24fd82e2a39"></a>

### [`008cbf84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbf84.md) → [`008cbfd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbfd8.md) FUN_008cbfd8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.41% / 新版 79.41%

CFGの説明率　旧版 31.25% / 新版 30.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbf88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbf88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbfe0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008cbf88",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008cc024",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008cc2dc"
      ]
    ],
    [
      "unmatched:008cbfe0",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008cbfdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008cc024",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "008cc330"
      ]
    ],
    [
      "008cc034",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cbf88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbf84.md#insn-008cbf88) · [`008cbfdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbf84.md#insn-008cbfdc)
- 新版 [`008cbfdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cbfd8.md#insn-008cbfdc)

~~~diff
- 008cbf88 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008cbf88 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008cbf88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 008cbf88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008cbf88 bytes fd7b04a9
- 008cbfdc ["COPY", "tmp:0:8", ["const:18:8"]]
- 008cbfdc ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 008cbfdc ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 008cbfdc ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 008cbfdc bytes 08630091
+ 008cbfdc ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 008cbfdc ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 008cbfdc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
+ 008cbfdc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008cbfdc bytes fd7b04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b2cd02e33146350e2528925ac1502db"></a>

### [`008cc3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc3ac.md) → [`008cc400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc400.md) FUN_008cc400

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc3b0"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cc424",
      "incomplete_value": false,
      "site": "008cc424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cc3d0",
      "incomplete_value": false,
      "site": "008cc3d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008cc404"
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
      "unmatched:008cc3b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008cc424",
      "DATA",
      [
        "storage",
        "00c83ee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cc404",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008cc424",
      "DATA",
      [
        "storage",
        "00c83fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cc3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc3ac.md#insn-008cc3b0) · [`008cc3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc3ac.md#insn-008cc3c0)
- 新版 [`008cc404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc400.md#insn-008cc404) · [`008cc414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc400.md#insn-008cc414)

~~~diff
- 008cc3b0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008cc3b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008cc3b0 bytes f30b00f9
+ 008cc404 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 008cc404 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 008cc404 bytes f30b00f9
- 008cc3c0 ["INT_ADD", "register:40f0:8", ["const:8cc3c0:8", "const:4:8"]]
- 008cc3c0 ["CALL", null, ["callee:00c57f60:8"]]
+ 008cc414 ["INT_ADD", "register:40f0:8", ["const:8cc414:8", "const:4:8"]]
+ 008cc414 ["CALL", null, ["callee:00c57f60:8"]]
- 008cc3c0 bytes b42e0e94
+ 008cc414 bytes d32e0e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70566035fa52a60470b797af4570eb24"></a>

### [`008cc3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc3e0.md) → [`008cc434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc434.md) FUN_008cc434

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cc440",
      "incomplete_value": false,
      "site": "008cc440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cc3ec",
      "incomplete_value": false,
      "site": "008cc3ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
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
      "008cc440",
      "DATA",
      [
        "storage",
        "00c83ee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cc440",
      "DATA",
      [
        "storage",
        "00c83fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cc3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc3e0.md#insn-008cc3e8)
- 新版 [`008cc43c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc434.md#insn-008cc43c)

~~~diff
- 008cc3e8 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 008cc3e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008cc3e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008cc3e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008cc43c ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 008cc43c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008cc43c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008cc43c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008cc3e8 bytes 29a13b91
+ 008cc43c bytes 29e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bf2e8a043064d98f5de25e605618d5e"></a>

### [`008cc3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc3fc.md) → [`008cc450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc450.md) FUN_008cc450

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008bf5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bf/008bf5ac.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008bf604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bf/008bf604.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 30.00% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc3fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc3fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008cc450"
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
      "unmatched:008cc3fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008cc414",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008cc428"
      ]
    ],
    [
      "008cc470",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "008cc450",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008cc468",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cc47c"
      ]
    ],
    [
      "008cc470",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cc3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc3fc.md#insn-008cc3fc) · [`008cc414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc3fc.md#insn-008cc414) · [`008cc41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc3fc.md#insn-008cc41c)
- 新版 [`008cc470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc450.md#insn-008cc470)

~~~diff
- 008cc3fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008cc3fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008cc3fc ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 008cc3fc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008cc3fc bytes fd7bbfa9
- 008cc414 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 008cc414 bytes a0000054
- 008cc41c ["INT_ADD", "register:40f0:8", ["const:8cc41c:8", "const:4:8"]]
- 008cc41c ["CALL", null, ["ram:47acf4:8"]]
+ 008cc470 ["INT_ADD", "register:40f0:8", ["const:8cc470:8", "const:4:8"]]
+ 008cc470 ["CALL", null, ["ram:47ad34:8"]]
- 008cc41c bytes 36baee97
+ 008cc470 bytes 31baee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c97e37cb2864695d890c8c38d5b04d8"></a>

### [`008cc478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc478.md) → [`008cc4cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc4cc.md) FUN_008cc4cc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cc4d0",
      "incomplete_value": false,
      "site": "008cc4d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cc47c",
      "incomplete_value": false,
      "site": "008cc480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:f68:8"
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
      "008cc4d4",
      "DATA",
      [
        "storage",
        "00c83f68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008cc4d4",
      "DATA",
      [
        "storage",
        "00c84038",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cc478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc478.md#insn-008cc478) · [`008cc47c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc478.md#insn-008cc47c)
- 新版 [`008cc4cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc4cc.md#insn-008cc4cc) · [`008cc4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc4cc.md#insn-008cc4d0)

~~~diff
- 008cc478 ["COPY", "register:4040:8", ["const:c83000:8"]]
+ 008cc4cc ["COPY", "register:4040:8", ["const:c84000:8"]]
- 008cc478 bytes a81d00f0
+ 008cc4cc bytes c81d0090
- 008cc47c ["COPY", "tmp:0:8", ["const:f68:8"]]
- 008cc47c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cc47c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cc47c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cc4d0 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008cc4d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cc4d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cc4d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cc47c bytes 08a13d91
+ 008cc4d0 bytes 08e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5997f767c1c146c15df2fd051e60da3e"></a>

### [`008cc488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc488.md) → [`008cc4dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc4dc.md) FUN_008cc4dc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cc4ec",
      "incomplete_value": false,
      "site": "008cc4f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cc498",
      "incomplete_value": false,
      "site": "008cc4a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cc4f4",
      "DATA",
      [
        "storage",
        "00c83f68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008cc4f4",
      "DATA",
      [
        "storage",
        "00c84038",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cc494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc488.md#insn-008cc494) · [`008cc498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc488.md#insn-008cc498) · [`008cc4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc488.md#insn-008cc4a4)
- 新版 [`008cc4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc4dc.md#insn-008cc4e8) · [`008cc4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc4dc.md#insn-008cc4ec) · [`008cc4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc4dc.md#insn-008cc4f8)

~~~diff
- 008cc494 ["COPY", "register:4040:8", ["const:c83000:8"]]
+ 008cc4e8 ["COPY", "register:4040:8", ["const:c84000:8"]]
- 008cc494 bytes a81d00f0
+ 008cc4e8 bytes c81d0090
- 008cc498 ["COPY", "tmp:0:8", ["const:f68:8"]]
- 008cc498 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cc498 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cc498 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cc4ec ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008cc4ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cc4ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cc4ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cc498 bytes 08a13d91
+ 008cc4ec bytes 08e10091
- 008cc4a4 ["INT_ADD", "register:40f0:8", ["const:8cc4a4:8", "const:4:8"]]
- 008cc4a4 ["CALL", null, ["callee:00c57f70:8"]]
+ 008cc4f8 ["INT_ADD", "register:40f0:8", ["const:8cc4f8:8", "const:4:8"]]
+ 008cc4f8 ["CALL", null, ["callee:00c57f70:8"]]
- 008cc4a4 bytes 7f2e0e94
+ 008cc4f8 bytes 9e2e0e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89f19d0eca08ab031a456a065eb5bf82"></a>

### [`008cc600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc600.md) → [`008cc654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc654.md) FUN_008cc654

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008cc4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc4c0.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`008cc514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc514.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008cc660",
      "incomplete_value": false,
      "site": "008cc664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cc60c",
      "incomplete_value": false,
      "site": "008cc610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f4c:8"
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
      "008cc660",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008cc660",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cc610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc600.md#insn-008cc610) · [`008cc60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc600.md#insn-008cc60c)
- 新版 [`008cc664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc654.md#insn-008cc664) · [`008cc660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc654.md#insn-008cc660)

~~~diff
- 008cc610 ["INT_ADD", "register:40f0:8", ["const:8cc610:8", "const:4:8"]]
- 008cc610 ["CALL", null, ["callee:0043b7b8:8"]]
+ 008cc664 ["INT_ADD", "register:40f0:8", ["const:8cc664:8", "const:4:8"]]
+ 008cc664 ["CALL", null, ["callee:0043b7b8:8"]]
- 008cc610 bytes 5abced97
+ 008cc664 bytes 55bced97
- 008cc60c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 008cc60c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008cc60c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008cc60c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008cc660 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 008cc660 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008cc660 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008cc660 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008cc60c bytes 00303d91
+ 008cc660 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c62e3b06800b7eb19b17dd06502666c"></a>

### [`008cc614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc614.md) → [`008cc668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc668.md) FUN_008cc668

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`008c385c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c3/008c385c.md) [`008cc614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc614.md) [`008ccac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008ccac4.md) · 呼出先 6件 [`008cc614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc614.md) [`008ccac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008ccac4.md) [`008cce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cce50.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 3件 [`008c38b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c3/008c38b4.md) [`008cc668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc668.md) [`008ccb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008ccb18.md) · 呼出先 6件 [`008cc668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc668.md) [`008ccb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008ccb18.md) [`008ccea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008ccea4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 93.13% / 新版 93.13%

CFGの説明率　旧版 61.32% / 新版 59.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc618"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc618"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc61c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008cc618",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008cc61c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008cc620",
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
      "008cc66c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008cc670",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008cc674",
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

- 旧版 [`008cc618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc614.md#insn-008cc618) · [`008cc61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc614.md#insn-008cc61c) · [`008cc620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc614.md#insn-008cc620)

~~~diff
- 008cc618 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008cc618 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008cc618 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008cc618 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008cc618 bytes fd7b02a9
- 008cc61c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 008cc61c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 008cc61c bytes fb1b00f9
- 008cc620 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 008cc620 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 008cc620 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 008cc620 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008cc620 bytes fa6704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccd22aabdecd43c430b2fef1a5548223"></a>

### [`008ccac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008ccac4.md) → [`008ccb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008ccb18.md) FUN_008ccb18

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008cc614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc614.md) · 呼出先 3件 [`008cc614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc614.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`008cc668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc668.md) · 呼出先 3件 [`008cc668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc668.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 67.71% / 新版 67.71%

CFGの説明率　旧版 10.58% / 新版 10.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 6件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ccac4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ccac4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ccac8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ccac4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ccac8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ccacc",
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
      "008ccb18",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008ccb1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008ccb20",
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

- 旧版 [`008ccac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008ccac4.md#insn-008ccac4) · [`008ccac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008ccac4.md#insn-008ccac8) · [`008ccacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008ccac4.md#insn-008ccacc)

~~~diff
- 008ccac4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008ccac4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008ccac4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 008ccac4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008ccac4 bytes fd7bbba9
- 008ccac8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008ccac8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 008ccac8 bytes f90b00f9
- 008ccacc ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 008ccacc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 008ccacc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008ccacc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ccacc bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a0f85086b3fcd3e8b1112929636adb8"></a>

### [`008cce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cce50.md) → [`008ccea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008ccea4.md) FUN_008ccea4

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008cc614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc614.md) [`008cce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cce50.md) · 呼出先 3件 [`008cce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cce50.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 2件 [`008cc668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008cc668.md) [`008ccea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008ccea4.md) · 呼出先 3件 [`008ccea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008ccea4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 91.72% / 新版 93.01%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008cceec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008ccf40"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008cd454"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008cceec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ccf7c"
      ]
    ],
    [
      "unmatched:008cd454",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "008ccf40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ccf7c"
      ]
    ],
    [
      "008cd4a8",
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

- 旧版 [`008cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cce50.md#insn-008cceec) · [`008ccf40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cce50.md#insn-008ccf40)
- 新版 [`008ccf94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008ccea4.md#insn-008ccf94) · [`008ccf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cc/008ccea4.md#insn-008ccf40)

~~~diff
- 008cceec ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 008cceec bytes e0010054
- 008ccf40 ["CBRANCH", null, ["local:b34:8", "register:101:1"]]
+ 008ccf94 ["CBRANCH", null, ["local:b33:8", "register:101:1"]]
- 008ccf40 bytes 200c0054
+ 008ccf94 bytes 200c0054
+ 008ccf40 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
+ 008ccf40 bytes e0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dd06efbaa8cb15d8c6927b900983735"></a>

### [`008cd4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cd4cc.md) → [`008cd520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cd520.md) FUN_008cd520

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`008c385c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c3/008c385c.md) [`008cd4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cd4cc.md) [`008cdb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cdb30.md) · 呼出先 7件 [`008cd4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cd4cc.md) [`008cd9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cd9b4.md) [`008cdb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cdb30.md) [`008cdec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cdec4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 3件 [`008c38b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c3/008c38b4.md) [`008cd520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cd520.md) [`008cdb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cdb84.md) · 呼出先 7件 [`008cd520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cd520.md) [`008cda08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cda08.md) [`008cdb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cdb84.md) [`008cdf18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cdf18.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.67% / 新版 88.67%

CFGの説明率　旧版 34.51% / 新版 34.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cd568"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cd6e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008cd5bc"
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
      "unmatched:008cd4fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cd584"
      ]
    ],
    [
      "unmatched:008cd504",
      "READ",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:008cd50c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cda04"
      ]
    ]
  ],
  "added": [
    [
      "008cd550",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cd584"
      ]
    ],
    [
      "008cd558",
      "READ",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "008cd560",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cda04"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cd4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cd4cc.md#insn-008cd4fc) · [`008cd50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cd4cc.md#insn-008cd50c) · [`008cd544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cd4cc.md#insn-008cd544)

~~~diff
- 008cd4fc ["CBRANCH", null, ["local:b5:8", "register:102:1"]]
- 008cd4fc bytes a2010054
- 008cd50c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008cd50c ["CBRANCH", null, ["local:b76:8", "tmp:0:1"]]
- 008cd50c bytes 21250054
- 008cd544 ["INT_ADD", "register:40f0:8", ["const:8cd544:8", "const:4:8"]]
- 008cd544 ["CALL", null, ["ram:8cd9b4:8"]]
- 008cd544 bytes 1c010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b51e83d6031f0d6877931f44fee34b4"></a>

### [`008cdb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cdb30.md) → [`008cdb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cdb84.md) FUN_008cdb84

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008cd4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cd4cc.md) · 呼出先 5件 [`008cd4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cd4cc.md) [`008cd9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cd9b4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`008cd520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cd520.md) · 呼出先 5件 [`008cd520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cd520.md) [`008cda08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cda08.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.24% / 新版 91.24%

CFGの説明率　旧版 57.14% / 新版 55.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 4件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cdbf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cdbf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cdc04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cdc08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008cd9b4"
      ]
    ],
    [
      "unmatched:008cdbf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "008cdca8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008cd9b4"
      ]
    ]
  ],
  "added": [
    [
      "008cdc08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008cda08"
      ]
    ],
    [
      "008cdc48",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "008cdca8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008cda08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cdbb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cdb30.md#insn-008cdbb4) · [`008cdbf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cdb30.md#insn-008cdbf4) · [`008cdc04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cdb30.md#insn-008cdc04)
- 新版 [`008cdc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cdb84.md#insn-008cdc08)

~~~diff
- 008cdbb4 ["INT_ADD", "register:40f0:8", ["const:8cdbb4:8", "const:4:8"]]
- 008cdbb4 ["CALL", null, ["ram:8cd9b4:8"]]
+ 008cdc08 ["INT_ADD", "register:40f0:8", ["const:8cdc08:8", "const:4:8"]]
+ 008cdc08 ["CALL", null, ["ram:8cda08:8"]]
- 008cdbb4 bytes 80ffff97
+ 008cdc08 bytes 80ffff97
- 008cdbf4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 008cdbf4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 008cdbf4 ["COPY", "tmp:2:8", ["register:8:8"]]
- 008cdbf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008cdbf4 bytes f32300a9
- 008cdc04 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 008cdc04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008cdc04 bytes 6002803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b039f783ce2d6ef940bb1bf9e658d0b3"></a>

### [`008cdec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cdec4.md) → [`008cdf18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cdf18.md) FUN_008cdf18

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008cd4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cd4cc.md) [`008cdec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cdec4.md) · 呼出先 5件 [`008cd9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cd9b4.md) [`008cdec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cdec4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`008cd520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cd520.md) [`008cdf18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cdf18.md) · 呼出先 5件 [`008cda08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cda08.md) [`008cdf18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cdf18.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 97.49% / 新版 97.49%

CFGの説明率　旧版 81.58% / 新版 82.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 5件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ce07c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ce0bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008ce0d0"
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
      "008cdf90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008cd9b4"
      ]
    ],
    [
      "unmatched:008cdf68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ce148"
      ]
    ],
    [
      "008cdffc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008cd9b4"
      ]
    ]
  ],
  "added": [
    [
      "008cdf90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008cda08"
      ]
    ],
    [
      "008cdfbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ce148"
      ]
    ],
    [
      "008cdffc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008cda08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cdf3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cdec4.md#insn-008cdf3c) · [`008cdf68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cdec4.md#insn-008cdf68) · [`008cdfa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cdec4.md#insn-008cdfa8)
- 新版 [`008cdf90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cdf18.md#insn-008cdf90) · [`008cdffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cd/008cdf18.md#insn-008cdffc)

~~~diff
- 008cdf3c ["INT_ADD", "register:40f0:8", ["const:8cdf3c:8", "const:4:8"]]
- 008cdf3c ["CALL", null, ["ram:8cd9b4:8"]]
+ 008cdf90 ["INT_ADD", "register:40f0:8", ["const:8cdf90:8", "const:4:8"]]
+ 008cdf90 ["CALL", null, ["ram:8cda08:8"]]
- 008cdf3c bytes 9efeff97
+ 008cdf90 bytes 9efeff97
- 008cdf68 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008cdf68 ["CBRANCH", null, ["local:b32:8", "tmp:0:1"]]
- 008cdf68 bytes 6a0c0054
- 008cdfa8 ["INT_ADD", "register:40f0:8", ["const:8cdfa8:8", "const:4:8"]]
- 008cdfa8 ["CALL", null, ["ram:8cd9b4:8"]]
+ 008cdffc ["INT_ADD", "register:40f0:8", ["const:8cdffc:8", "const:4:8"]]
+ 008cdffc ["CALL", null, ["ram:8cda08:8"]]
- 008cdfa8 bytes 83feff97
+ 008cdffc bytes 83feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a34b5b5c58f74edf07f8f89a88e8c172"></a>

### [`008ce5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008ce5c4.md) → [`008ce618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008ce618.md) FUN_008ce618

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`008c5208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c5/008c5208.md) [`008ce5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008ce5c4.md) [`008cea74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008cea74.md) · 呼出先 6件 [`008ce5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008ce5c4.md) [`008cea74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008cea74.md) [`008ced74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008ced74.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 3件 [`008c525c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c5/008c525c.md) [`008ce618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008ce618.md) [`008ceac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008ceac8.md) · 呼出先 6件 [`008ce618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008ce618.md) [`008ceac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008ceac8.md) [`008cedc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008cedc8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 74.75% / 新版 77.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008ce914"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008ce92c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008ce968"
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
      "unmatched:008ce914",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cea34"
      ]
    ],
    [
      "unmatched:008ce92c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cea34"
      ]
    ],
    [
      "unmatched:008ce8bc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "008ce968",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cea34"
      ]
    ],
    [
      "008ce980",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cea34"
      ]
    ],
    [
      "008ce910",
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

- 旧版 [`008ce868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008ce5c4.md#insn-008ce868) · [`008ce8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008ce5c4.md#insn-008ce8ac) · [`008ce8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ce/008ce5c4.md#insn-008ce8bc)
- 新版 [`008ce8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008ce618.md#insn-008ce8bc) · [`008ce900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ce/008ce618.md#insn-008ce900)

~~~diff
- 008ce868 ["CBRANCH", null, ["local:b51:8", "register:101:1"]]
+ 008ce8bc ["CBRANCH", null, ["local:b48:8", "register:101:1"]]
- 008ce868 bytes 80080054
+ 008ce8bc bytes 80080054
- 008ce8ac ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008ce8ac ["CBRANCH", null, ["local:b38:8", "tmp:0:1"]]
+ 008ce900 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 008ce900 ["CBRANCH", null, ["local:b37:8", "tmp:0:1"]]
- 008ce8ac bytes e00000b5
+ 008ce900 bytes e00000b5
- 008ce8bc ["COPY", "register:0:8", ["register:4040:8"]]
- 008ce8bc ["INT_ADD", "register:40f0:8", ["const:8ce8bc:8", "const:4:8"]]
- 008ce8bc ["CALLIND", null, ["register:0:8"]]
- 008ce8bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5d005a6ec1155b04475b460981f40a0"></a>

### [`008cf3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf3f4.md) → [`008cf448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf448.md) FUN_008cf448

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cf46c",
      "incomplete_value": false,
      "site": "008cf46c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cf418",
      "incomplete_value": false,
      "site": "008cf418",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c83000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cf46c",
      "DATA",
      [
        "storage",
        "00c83fb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cf46c",
      "DATA",
      [
        "storage",
        "00c84088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cf408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf3f4.md#insn-008cf408) · [`008cf410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf3f4.md#insn-008cf410) · [`008cf414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf3f4.md#insn-008cf414)
- 新版 [`008cf45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf448.md#insn-008cf45c) · [`008cf464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf448.md#insn-008cf464) · [`008cf468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf448.md#insn-008cf468)

~~~diff
- 008cf408 ["INT_ADD", "register:40f0:8", ["const:8cf408:8", "const:4:8"]]
- 008cf408 ["CALL", null, ["callee:00c57f60:8"]]
+ 008cf45c ["INT_ADD", "register:40f0:8", ["const:8cf45c:8", "const:4:8"]]
+ 008cf45c ["CALL", null, ["callee:00c57f60:8"]]
- 008cf408 bytes a2220e94
+ 008cf45c bytes c1220e94
- 008cf410 ["COPY", "register:4040:8", ["const:c83000:8"]]
+ 008cf464 ["COPY", "register:4040:8", ["const:c84000:8"]]
- 008cf410 bytes a81d0090
+ 008cf464 bytes a81d00b0
- 008cf414 ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 008cf414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cf414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cf414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cf468 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 008cf468 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cf468 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cf468 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cf414 bytes 08e13e91
+ 008cf468 bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f97010f689ef930a24dc5706af6d1ed"></a>

### [`008cf444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf444.md) → [`008cf498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf498.md) FUN_008cf498

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008bf8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bf/008bf8c4.md) [`008c28bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c2/008c28bc.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008bf91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008bf/008bf91c.md) [`008c2914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2914.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008cf4b8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008cf464",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008cf4c4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008cf470",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "008cf4b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008cf4c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "008cf4b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008cf4c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cf464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf444.md#insn-008cf464) · [`008cf470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf444.md#insn-008cf470) · [`008cf48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf444.md#insn-008cf48c)
- 新版 [`008cf4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf498.md#insn-008cf4b8) · [`008cf4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf498.md#insn-008cf4c4) · [`008cf4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf498.md#insn-008cf4e0)

~~~diff
- 008cf464 ["INT_ADD", "register:40f0:8", ["const:8cf464:8", "const:4:8"]]
- 008cf464 ["CALL", null, ["ram:47acf4:8"]]
+ 008cf4b8 ["INT_ADD", "register:40f0:8", ["const:8cf4b8:8", "const:4:8"]]
+ 008cf4b8 ["CALL", null, ["ram:47ad34:8"]]
- 008cf464 bytes 24aeee97
+ 008cf4b8 bytes 1faeee97
- 008cf470 ["INT_ADD", "register:40f0:8", ["const:8cf470:8", "const:4:8"]]
- 008cf470 ["CALL", null, ["ram:47acf4:8"]]
+ 008cf4c4 ["INT_ADD", "register:40f0:8", ["const:8cf4c4:8", "const:4:8"]]
+ 008cf4c4 ["CALL", null, ["ram:47ad34:8"]]
- 008cf470 bytes 21aeee97
+ 008cf4c4 bytes 1caeee97
- 008cf48c ["INT_ADD", "register:40f0:8", ["const:8cf48c:8", "const:4:8"]]
- 008cf48c ["CALL", null, ["callee:008bf91c:8"]]
+ 008cf4e0 ["INT_ADD", "register:40f0:8", ["const:8cf4e0:8", "const:4:8"]]
+ 008cf4e0 ["CALL", null, ["callee:008bf91c:8"]]
- 008cf48c bytes 0ec1ff97
+ 008cf4e0 bytes 0fc1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd5932a355784d7eedb2311cb065829f"></a>

### [`008cf4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf4d0.md) → [`008cf524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf524.md) FUN_008cf524

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cf548",
      "incomplete_value": false,
      "site": "008cf548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cf4f4",
      "incomplete_value": false,
      "site": "008cf4f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cf548",
      "DATA",
      [
        "storage",
        "00c84038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cf548",
      "DATA",
      [
        "storage",
        "00c84108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cf4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf4d0.md#insn-008cf4e4) · [`008cf4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf4d0.md#insn-008cf4f0)
- 新版 [`008cf538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf524.md#insn-008cf538) · [`008cf544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf524.md#insn-008cf544)

~~~diff
- 008cf4e4 ["INT_ADD", "register:40f0:8", ["const:8cf4e4:8", "const:4:8"]]
- 008cf4e4 ["CALL", null, ["callee:00c57f60:8"]]
+ 008cf538 ["INT_ADD", "register:40f0:8", ["const:8cf538:8", "const:4:8"]]
+ 008cf538 ["CALL", null, ["callee:00c57f60:8"]]
- 008cf4e4 bytes 6b220e94
+ 008cf538 bytes 8a220e94
- 008cf4f0 ["COPY", "tmp:0:8", ["const:38:8"]]
- 008cf4f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cf4f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cf4f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cf544 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 008cf544 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cf544 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cf544 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cf4f0 bytes 08e10091
+ 008cf544 bytes 08210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d7fa31b2d8acf11e722695573a74cc0"></a>

### [`008cf6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf6c0.md) → [`008cf714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf714.md) FUN_008cf714

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cf728",
      "incomplete_value": false,
      "site": "008cf72c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cf6d4",
      "incomplete_value": false,
      "site": "008cf6d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:b8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cf72c",
      "DATA",
      [
        "storage",
        "00c840b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cf72c",
      "DATA",
      [
        "storage",
        "00c84188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cf6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf6c0.md#insn-008cf6cc) · [`008cf6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf6c0.md#insn-008cf6d4)
- 新版 [`008cf720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf714.md#insn-008cf720) · [`008cf728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf714.md#insn-008cf728)

~~~diff
- 008cf6cc ["INT_ADD", "register:40f0:8", ["const:8cf6cc:8", "const:4:8"]]
- 008cf6cc ["CALL", null, ["callee:00c57f60:8"]]
+ 008cf720 ["INT_ADD", "register:40f0:8", ["const:8cf720:8", "const:4:8"]]
+ 008cf720 ["CALL", null, ["callee:00c57f60:8"]]
- 008cf6cc bytes f1210e94
+ 008cf720 bytes 10220e94
- 008cf6d4 ["COPY", "tmp:0:8", ["const:b8:8"]]
- 008cf6d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cf6d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cf6d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cf728 ["COPY", "tmp:0:8", ["const:188:8"]]
+ 008cf728 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cf728 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cf728 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cf6d4 bytes 08e10291
+ 008cf728 bytes 08210691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c4044a9bdaa7dc991d4f801d30f0a03"></a>

### [`008cf6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf6fc.md) → [`008cf750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf750.md) FUN_008cf750

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008c28bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c2/008c28bc.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008c2914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2914.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008cf770",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008cf71c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008cf77c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008cf728",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "008cf770",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008cf77c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "008cf770",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008cf77c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cf71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf6fc.md#insn-008cf71c) · [`008cf728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf6fc.md#insn-008cf728) · [`008cf73c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf6fc.md#insn-008cf73c)
- 新版 [`008cf770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf750.md#insn-008cf770) · [`008cf77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf750.md#insn-008cf77c) · [`008cf790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf750.md#insn-008cf790)

~~~diff
- 008cf71c ["INT_ADD", "register:40f0:8", ["const:8cf71c:8", "const:4:8"]]
- 008cf71c ["CALL", null, ["ram:47acf4:8"]]
+ 008cf770 ["INT_ADD", "register:40f0:8", ["const:8cf770:8", "const:4:8"]]
+ 008cf770 ["CALL", null, ["ram:47ad34:8"]]
- 008cf71c bytes 76adee97
+ 008cf770 bytes 71adee97
- 008cf728 ["INT_ADD", "register:40f0:8", ["const:8cf728:8", "const:4:8"]]
- 008cf728 ["CALL", null, ["ram:47acf4:8"]]
+ 008cf77c ["INT_ADD", "register:40f0:8", ["const:8cf77c:8", "const:4:8"]]
+ 008cf77c ["CALL", null, ["ram:47ad34:8"]]
- 008cf728 bytes 73adee97
+ 008cf77c bytes 6eadee97
- 008cf73c ["INT_ADD", "register:40f0:8", ["const:8cf73c:8", "const:4:8"]]
- 008cf73c ["CALL", null, ["callee:00851550:8"]]
+ 008cf790 ["INT_ADD", "register:40f0:8", ["const:8cf790:8", "const:4:8"]]
+ 008cf790 ["CALL", null, ["callee:00851550:8"]]
- 008cf73c bytes 6f07fe97
+ 008cf790 bytes 7007fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaddba3f1a26334a5795a728e086e00d"></a>

### [`008cf790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf790.md) → [`008cf7e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf7e4.md) FUN_008cf7e4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cf7f8",
      "incomplete_value": false,
      "site": "008cf7fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cf7a4",
      "incomplete_value": false,
      "site": "008cf7a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cf7fc",
      "DATA",
      [
        "storage",
        "00c84138",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cf7fc",
      "DATA",
      [
        "storage",
        "00c84208",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cf79c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf790.md#insn-008cf79c) · [`008cf7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf790.md#insn-008cf7a4)
- 新版 [`008cf7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf7e4.md#insn-008cf7f0) · [`008cf7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf7e4.md#insn-008cf7f8)

~~~diff
- 008cf79c ["INT_ADD", "register:40f0:8", ["const:8cf79c:8", "const:4:8"]]
- 008cf79c ["CALL", null, ["callee:00c57f60:8"]]
+ 008cf7f0 ["INT_ADD", "register:40f0:8", ["const:8cf7f0:8", "const:4:8"]]
+ 008cf7f0 ["CALL", null, ["callee:00c57f60:8"]]
- 008cf79c bytes bd210e94
+ 008cf7f0 bytes dc210e94
- 008cf7a4 ["COPY", "tmp:0:8", ["const:138:8"]]
- 008cf7a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cf7a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cf7a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cf7f8 ["COPY", "tmp:0:8", ["const:208:8"]]
+ 008cf7f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cf7f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cf7f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cf7a4 bytes 08e10491
+ 008cf7f8 bytes 08210891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a3a2b96c9b7d1adf72ea3c6da7a893d"></a>

### [`008cf7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf7cc.md) → [`008cf820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf820.md) FUN_008cf820

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008cf83c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008cf7e8",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "008cf83c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "008cf83c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cf7e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf7cc.md#insn-008cf7e8) · [`008cf7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf7cc.md#insn-008cf7f4)
- 新版 [`008cf83c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf820.md#insn-008cf83c) · [`008cf848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf820.md#insn-008cf848)

~~~diff
- 008cf7e8 ["INT_ADD", "register:40f0:8", ["const:8cf7e8:8", "const:4:8"]]
- 008cf7e8 ["CALL", null, ["ram:47acf4:8"]]
+ 008cf83c ["INT_ADD", "register:40f0:8", ["const:8cf83c:8", "const:4:8"]]
+ 008cf83c ["CALL", null, ["ram:47ad34:8"]]
- 008cf7e8 bytes 43adee97
+ 008cf83c bytes 3eadee97
- 008cf7f4 ["INT_ADD", "register:40f0:8", ["const:8cf7f4:8", "const:4:8"]]
- 008cf7f4 ["CALL", null, ["callee:0047ce14:8"]]
+ 008cf848 ["INT_ADD", "register:40f0:8", ["const:8cf848:8", "const:4:8"]]
+ 008cf848 ["CALL", null, ["callee:0047ce14:8"]]
- 008cf7f4 bytes 78b5ee97
+ 008cf848 bytes 73b5ee97
~~~


<a id="compare-86278319b90ffd6cdc2c90946774736b"></a>

### [`008cf838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf838.md) → [`008cf88c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf88c.md) FUN_008cf88c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cf8a0",
      "incomplete_value": false,
      "site": "008cf8a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cf84c",
      "incomplete_value": false,
      "site": "008cf850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cf8a4",
      "DATA",
      [
        "storage",
        "00c841b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cf8a4",
      "DATA",
      [
        "storage",
        "00c84288",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cf844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf838.md#insn-008cf844) · [`008cf84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf838.md#insn-008cf84c)
- 新版 [`008cf898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf88c.md#insn-008cf898) · [`008cf8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf88c.md#insn-008cf8a0)

~~~diff
- 008cf844 ["INT_ADD", "register:40f0:8", ["const:8cf844:8", "const:4:8"]]
- 008cf844 ["CALL", null, ["callee:00c57f60:8"]]
+ 008cf898 ["INT_ADD", "register:40f0:8", ["const:8cf898:8", "const:4:8"]]
+ 008cf898 ["CALL", null, ["callee:00c57f60:8"]]
- 008cf844 bytes 93210e94
+ 008cf898 bytes b2210e94
- 008cf84c ["COPY", "tmp:0:8", ["const:1b8:8"]]
- 008cf84c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cf84c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cf84c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cf8a0 ["COPY", "tmp:0:8", ["const:288:8"]]
+ 008cf8a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cf8a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cf8a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cf84c bytes 08e10691
+ 008cf8a0 bytes 08210a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b6463a1793a1199fd9a1beba728084f"></a>

### [`008cf874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf874.md) → [`008cf8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf8c8.md) FUN_008cf8c8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008cf8e4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008cf890",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "008cf8e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "008cf8e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cf890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf874.md#insn-008cf890) · [`008cf89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf874.md#insn-008cf89c)
- 新版 [`008cf8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf8c8.md#insn-008cf8e4) · [`008cf8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf8c8.md#insn-008cf8f0)

~~~diff
- 008cf890 ["INT_ADD", "register:40f0:8", ["const:8cf890:8", "const:4:8"]]
- 008cf890 ["CALL", null, ["ram:47acf4:8"]]
+ 008cf8e4 ["INT_ADD", "register:40f0:8", ["const:8cf8e4:8", "const:4:8"]]
+ 008cf8e4 ["CALL", null, ["ram:47ad34:8"]]
- 008cf890 bytes 19adee97
+ 008cf8e4 bytes 14adee97
- 008cf89c ["INT_ADD", "register:40f0:8", ["const:8cf89c:8", "const:4:8"]]
- 008cf89c ["CALL", null, ["callee:0047ce14:8"]]
+ 008cf8f0 ["INT_ADD", "register:40f0:8", ["const:8cf8f0:8", "const:4:8"]]
+ 008cf8f0 ["CALL", null, ["callee:0047ce14:8"]]
- 008cf89c bytes 4eb5ee97
+ 008cf8f0 bytes 49b5ee97
~~~


<a id="compare-5d9a5825904d537f99f3b7884d309cdd"></a>

### [`008cf8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf8e0.md) → [`008cf934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf934.md) FUN_008cf934

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cf948",
      "incomplete_value": false,
      "site": "008cf94c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cf8f4",
      "incomplete_value": false,
      "site": "008cf8f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:238:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cf94c",
      "DATA",
      [
        "storage",
        "00c84238",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cf94c",
      "DATA",
      [
        "storage",
        "00c84308",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cf8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf8e0.md#insn-008cf8ec) · [`008cf8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf8e0.md#insn-008cf8f4)
- 新版 [`008cf940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf934.md#insn-008cf940) · [`008cf948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf934.md#insn-008cf948)

~~~diff
- 008cf8ec ["INT_ADD", "register:40f0:8", ["const:8cf8ec:8", "const:4:8"]]
- 008cf8ec ["CALL", null, ["callee:00c57f60:8"]]
+ 008cf940 ["INT_ADD", "register:40f0:8", ["const:8cf940:8", "const:4:8"]]
+ 008cf940 ["CALL", null, ["callee:00c57f60:8"]]
- 008cf8ec bytes 69210e94
+ 008cf940 bytes 88210e94
- 008cf8f4 ["COPY", "tmp:0:8", ["const:238:8"]]
- 008cf8f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cf8f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cf8f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cf948 ["COPY", "tmp:0:8", ["const:308:8"]]
+ 008cf948 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cf948 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cf948 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cf8f4 bytes 08e10891
+ 008cf948 bytes 08210c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f0efc6c5fba5ba5220db4d9c5852818"></a>

### [`008cf91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf91c.md) → [`008cf970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf970.md) FUN_008cf970

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`008c28bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c2/008c28bc.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`008c2914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2914.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.03% / 新版 97.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cfa94",
      "incomplete_value": false,
      "site": "008cfa9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cfa40",
      "incomplete_value": false,
      "site": "008cfa48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008cf9a8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008cf954",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "008cf9a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008cfa9c",
      "DATA",
      [
        "storage",
        "00c842a8",
        null,
        "undefined *"
      ]
    ],
    [
      "008cfad8",
      "READ",
      [
        "storage",
        "00c842c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008cf9a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008cfa30",
      "DATA",
      [
        "storage",
        "0044deac",
        null,
        null
      ]
    ],
    [
      "008cfa60",
      "DATA",
      [
        "storage",
        "0044deac",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cf954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf91c.md#insn-008cf954) · [`008cf960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf91c.md#insn-008cf960) · [`008cf964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cf91c.md#insn-008cf964)
- 新版 [`008cf9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf970.md#insn-008cf9a8) · [`008cf9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf970.md#insn-008cf9b4) · [`008cf9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cf970.md#insn-008cf9b8)

~~~diff
- 008cf954 ["INT_ADD", "register:40f0:8", ["const:8cf954:8", "const:4:8"]]
- 008cf954 ["CALL", null, ["ram:47acf4:8"]]
+ 008cf9a8 ["INT_ADD", "register:40f0:8", ["const:8cf9a8:8", "const:4:8"]]
+ 008cf9a8 ["CALL", null, ["ram:47ad34:8"]]
- 008cf954 bytes e8acee97
+ 008cf9a8 bytes e3acee97
- 008cf960 ["INT_ADD", "register:40f0:8", ["const:8cf960:8", "const:4:8"]]
- 008cf960 ["CALL", null, ["callee:0047ce14:8"]]
+ 008cf9b4 ["INT_ADD", "register:40f0:8", ["const:8cf9b4:8", "const:4:8"]]
+ 008cf9b4 ["CALL", null, ["callee:0047ce14:8"]]
- 008cf960 bytes 1db5ee97
+ 008cf9b4 bytes 18b5ee97
- 008cf964 ["INT_ADD", "register:40f0:8", ["const:8cf964:8", "const:4:8"]]
- 008cf964 ["CALL", null, ["callee:00851550:8"]]
+ 008cf9b8 ["INT_ADD", "register:40f0:8", ["const:8cf9b8:8", "const:4:8"]]
+ 008cf9b8 ["CALL", null, ["callee:00851550:8"]]
- 008cf964 bytes e506fe97
+ 008cf9b8 bytes e606fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e020fd1b156136c485770a3fd9d297c3"></a>

### [`008cfb28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cfb28.md) → [`008cfb7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfb7c.md) FUN_008cfb7c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cfb90",
      "incomplete_value": false,
      "site": "008cfb94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cfb3c",
      "incomplete_value": false,
      "site": "008cfb40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008cfb94",
      "DATA",
      [
        "storage",
        "00c842a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cfb94",
      "DATA",
      [
        "storage",
        "00c84378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cfb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cfb28.md#insn-008cfb34) · [`008cfb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cfb28.md#insn-008cfb3c)
- 新版 [`008cfb88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfb7c.md#insn-008cfb88) · [`008cfb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfb7c.md#insn-008cfb90)

~~~diff
- 008cfb34 ["INT_ADD", "register:40f0:8", ["const:8cfb34:8", "const:4:8"]]
- 008cfb34 ["CALL", null, ["callee:00c57f60:8"]]
+ 008cfb88 ["INT_ADD", "register:40f0:8", ["const:8cfb88:8", "const:4:8"]]
+ 008cfb88 ["CALL", null, ["callee:00c57f60:8"]]
- 008cfb34 bytes d7200e94
+ 008cfb88 bytes f6200e94
- 008cfb3c ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 008cfb3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cfb3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cfb3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cfb90 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 008cfb90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cfb90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cfb90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cfb3c bytes 08a10a91
+ 008cfb90 bytes 08e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b92aa5b5b88bc363df0c6135550c7eed"></a>

### [`008cfb4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cfb4c.md) → [`008cfba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfba0.md) FUN_008cfba0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cfba4",
      "incomplete_value": false,
      "site": "008cfba8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cfb50",
      "incomplete_value": false,
      "site": "008cfb54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
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
      "008cfba8",
      "DATA",
      [
        "storage",
        "00c842a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cfba8",
      "DATA",
      [
        "storage",
        "00c84378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cfb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cfb4c.md#insn-008cfb50)
- 新版 [`008cfba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfba0.md#insn-008cfba4)

~~~diff
- 008cfb50 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 008cfb50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cfb50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cfb50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cfba4 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 008cfba4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cfba4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cfba4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cfb50 bytes 08a10a91
+ 008cfba4 bytes 08e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e57a68ccc5416f399f6f91d818bba5fe"></a>

### [`008cfc1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cfc1c.md) → [`008cfc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfc70.md) FUN_008cfc70

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cfc7c",
      "incomplete_value": false,
      "site": "008cfc80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cfc28",
      "incomplete_value": false,
      "site": "008cfc2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:338:8"
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
      "008cfc80",
      "DATA",
      [
        "storage",
        "00c84338",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cfc80",
      "DATA",
      [
        "storage",
        "00c84408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cfc28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cfc1c.md#insn-008cfc28)
- 新版 [`008cfc7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfc70.md#insn-008cfc7c)

~~~diff
- 008cfc28 ["COPY", "tmp:0:8", ["const:338:8"]]
- 008cfc28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008cfc28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008cfc28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008cfc7c ["COPY", "tmp:0:8", ["const:408:8"]]
+ 008cfc7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008cfc7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008cfc7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008cfc28 bytes 29e10c91
+ 008cfc7c bytes 29211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e79ee354097a19679c255a1c3fa772b3"></a>

### [`008cfc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cfc40.md) → [`008cfc94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfc94.md) FUN_008cfc94

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cfc9c",
      "incomplete_value": false,
      "site": "008cfca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cfc48",
      "incomplete_value": false,
      "site": "008cfc4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:338:8"
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
      "008cfca0",
      "DATA",
      [
        "storage",
        "00c84338",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cfca0",
      "DATA",
      [
        "storage",
        "00c84408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cfc48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cfc40.md#insn-008cfc48) · [`008cfc6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cfc40.md#insn-008cfc6c)
- 新版 [`008cfc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfc94.md#insn-008cfc9c) · [`008cfcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfc94.md#insn-008cfcc0)

~~~diff
- 008cfc48 ["COPY", "tmp:0:8", ["const:338:8"]]
- 008cfc48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008cfc48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008cfc48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008cfc9c ["COPY", "tmp:0:8", ["const:408:8"]]
+ 008cfc9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008cfc9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008cfc9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008cfc48 bytes 29e10c91
+ 008cfc9c bytes 29211091
- 008cfc6c ["INT_ADD", "register:40f0:8", ["const:8cfc6c:8", "const:4:8"]]
- 008cfc6c ["CALL", null, ["callee:00c57f80:8"]]
+ 008cfcc0 ["INT_ADD", "register:40f0:8", ["const:8cfcc0:8", "const:4:8"]]
+ 008cfcc0 ["CALL", null, ["callee:00c57f80:8"]]
- 008cfc6c bytes 91200e94
+ 008cfcc0 bytes b0200e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6fa77b8ecda5925705cd328897eb3d1"></a>

### [`008cfc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cfc80.md) → [`008cfcd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfcd4.md) FUN_008cfcd4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cfcf4",
      "incomplete_value": false,
      "site": "008cfcfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cfca0",
      "incomplete_value": false,
      "site": "008cfca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:338:8"
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
      "008cfcfc",
      "DATA",
      [
        "storage",
        "00c84338",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cfcfc",
      "DATA",
      [
        "storage",
        "00c84408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cfc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cfc80.md#insn-008cfc98) · [`008cfca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cfc80.md#insn-008cfca0) · [`008cfcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cfc80.md#insn-008cfcd4)
- 新版 [`008cfcec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfcd4.md#insn-008cfcec) · [`008cfcf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfcd4.md#insn-008cfcf4) · [`008cfd28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfcd4.md#insn-008cfd28)

~~~diff
- 008cfc98 ["INT_ADD", "register:40f0:8", ["const:8cfc98:8", "const:4:8"]]
- 008cfc98 ["CALL", null, ["callee:00c57f60:8"]]
+ 008cfcec ["INT_ADD", "register:40f0:8", ["const:8cfcec:8", "const:4:8"]]
+ 008cfcec ["CALL", null, ["callee:00c57f60:8"]]
- 008cfc98 bytes 7e200e94
+ 008cfcec bytes 9d200e94
- 008cfca0 ["COPY", "tmp:0:8", ["const:338:8"]]
- 008cfca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cfca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cfca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cfcf4 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 008cfcf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cfcf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cfcf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cfca0 bytes 08e10c91
+ 008cfcf4 bytes 08211091
- 008cfcd4 ["INT_ADD", "register:40f0:8", ["const:8cfcd4:8", "const:4:8"]]
- 008cfcd4 ["CALL", null, ["callee:00c57f60:8"]]
+ 008cfd28 ["INT_ADD", "register:40f0:8", ["const:8cfd28:8", "const:4:8"]]
+ 008cfd28 ["CALL", null, ["callee:00c57f60:8"]]
- 008cfcd4 bytes 6f200e94
+ 008cfd28 bytes 8e200e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df67f9c383a91020d2c54aac1591e1fe"></a>

### [`008cfd38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cfd38.md) → [`008cfd8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfd8c.md) FUN_008cfd8c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cfda0",
      "incomplete_value": false,
      "site": "008cfda8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cfd4c",
      "incomplete_value": false,
      "site": "008cfd54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:338:8"
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
      "008cfda8",
      "DATA",
      [
        "storage",
        "00c84338",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cfda8",
      "DATA",
      [
        "storage",
        "00c84408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cfd4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cfd38.md#insn-008cfd4c) · [`008cfd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cfd38.md#insn-008cfd80) · [`008cfd98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cf/008cfd38.md#insn-008cfd98)
- 新版 [`008cfda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfd8c.md#insn-008cfda0) · [`008cfdd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfd8c.md#insn-008cfdd4) · [`008cfdec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cf/008cfd8c.md#insn-008cfdec)

~~~diff
- 008cfd4c ["COPY", "tmp:0:8", ["const:338:8"]]
- 008cfd4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cfd4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cfd4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cfda0 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 008cfda0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cfda0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cfda0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cfd4c bytes 08e10c91
+ 008cfda0 bytes 08211091
- 008cfd80 ["INT_ADD", "register:40f0:8", ["const:8cfd80:8", "const:4:8"]]
- 008cfd80 ["CALL", null, ["callee:00c57f60:8"]]
+ 008cfdd4 ["INT_ADD", "register:40f0:8", ["const:8cfdd4:8", "const:4:8"]]
+ 008cfdd4 ["CALL", null, ["callee:00c57f60:8"]]
- 008cfd80 bytes 44200e94
+ 008cfdd4 bytes 63200e94
- 008cfd98 ["INT_ADD", "register:40f0:8", ["const:8cfd98:8", "const:4:8"]]
- 008cfd98 ["CALL", null, ["callee:00c580d0:8"]]
+ 008cfdec ["INT_ADD", "register:40f0:8", ["const:8cfdec:8", "const:4:8"]]
+ 008cfdec ["CALL", null, ["callee:00c580d0:8"]]
- 008cfd98 bytes 9a200e94
+ 008cfdec bytes b9200e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9ad4bf4108b8bca7c7f2c4d2ef5114e"></a>

### [`008d053c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d053c.md) → [`008d0590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0590.md) FUN_008d0590

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d05a4",
      "incomplete_value": false,
      "site": "008d05a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d0550",
      "incomplete_value": false,
      "site": "008d0554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d05a8",
      "DATA",
      [
        "storage",
        "00c843b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d05a8",
      "DATA",
      [
        "storage",
        "00c84488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d0548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d053c.md#insn-008d0548) · [`008d0550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d053c.md#insn-008d0550)
- 新版 [`008d059c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0590.md#insn-008d059c) · [`008d05a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0590.md#insn-008d05a4)

~~~diff
- 008d0548 ["INT_ADD", "register:40f0:8", ["const:8d0548:8", "const:4:8"]]
- 008d0548 ["CALL", null, ["callee:00c57f60:8"]]
+ 008d059c ["INT_ADD", "register:40f0:8", ["const:8d059c:8", "const:4:8"]]
+ 008d059c ["CALL", null, ["callee:00c57f60:8"]]
- 008d0548 bytes 521e0e94
+ 008d059c bytes 711e0e94
- 008d0550 ["COPY", "tmp:0:8", ["const:3b8:8"]]
- 008d0550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d0550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d0550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d05a4 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 008d05a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d05a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d05a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d0550 bytes 08e10e91
+ 008d05a4 bytes 08211291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e7f6cdfcc0fbacf07b44a70d124f95e"></a>

### [`008d05b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d05b8.md) → [`008d060c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d060c.md) FUN_008d060c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d0620",
      "incomplete_value": false,
      "site": "008d0624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d05cc",
      "incomplete_value": false,
      "site": "008d05d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d0624",
      "DATA",
      [
        "storage",
        "00c84438",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d0624",
      "DATA",
      [
        "storage",
        "00c84508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d05c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d05b8.md#insn-008d05c4) · [`008d05cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d05b8.md#insn-008d05cc)
- 新版 [`008d0618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d060c.md#insn-008d0618) · [`008d0620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d060c.md#insn-008d0620)

~~~diff
- 008d05c4 ["INT_ADD", "register:40f0:8", ["const:8d05c4:8", "const:4:8"]]
- 008d05c4 ["CALL", null, ["callee:00c57f60:8"]]
+ 008d0618 ["INT_ADD", "register:40f0:8", ["const:8d0618:8", "const:4:8"]]
+ 008d0618 ["CALL", null, ["callee:00c57f60:8"]]
- 008d05c4 bytes 331e0e94
+ 008d0618 bytes 521e0e94
- 008d05cc ["COPY", "tmp:0:8", ["const:438:8"]]
- 008d05cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d05cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d05cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d0620 ["COPY", "tmp:0:8", ["const:508:8"]]
+ 008d0620 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d0620 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d0620 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d05cc bytes 08e11091
+ 008d0620 bytes 08211491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-815004dd5f30b5b313b1aeba53bb567f"></a>

### [`008d06d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d06d4.md) → [`008d0728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0728.md) FUN_008d0728

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d073c",
      "incomplete_value": false,
      "site": "008d0740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d06e8",
      "incomplete_value": false,
      "site": "008d06ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:4b8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d0740",
      "DATA",
      [
        "storage",
        "00c844b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d0740",
      "DATA",
      [
        "storage",
        "00c84588",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d06e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d06d4.md#insn-008d06e0) · [`008d06e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d06d4.md#insn-008d06e8)
- 新版 [`008d0734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0728.md#insn-008d0734) · [`008d073c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0728.md#insn-008d073c)

~~~diff
- 008d06e0 ["INT_ADD", "register:40f0:8", ["const:8d06e0:8", "const:4:8"]]
- 008d06e0 ["CALL", null, ["callee:00c57f60:8"]]
+ 008d0734 ["INT_ADD", "register:40f0:8", ["const:8d0734:8", "const:4:8"]]
+ 008d0734 ["CALL", null, ["callee:00c57f60:8"]]
- 008d06e0 bytes ec1d0e94
+ 008d0734 bytes 0b1e0e94
- 008d06e8 ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 008d06e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d06e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d06e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d073c ["COPY", "tmp:0:8", ["const:588:8"]]
+ 008d073c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d073c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d073c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d06e8 bytes 08e11291
+ 008d073c bytes 08211691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1602ac010498b01886d9e590e0dfca39"></a>

### [`008d0710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0710.md) → [`008d0764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0764.md) FUN_008d0764

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008c28bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c2/008c28bc.md) [`008d0858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0858.md) [`008d085c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d085c.md) [`00acabd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00acabd4.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008c2914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2914.md) [`008d08ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d08ac.md) [`008d08b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d08b0.md) [`00acac44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aca/00acac44.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.05% / 新版 82.05%

CFGの説明率　旧版 54.55% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d0744"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d0748"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008d0798"
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
      "unmatched:008d0744",
      "DATA",
      [
        "storage",
        "00c84528",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008d0744",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d0748",
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
      "008d0798",
      "DATA",
      [
        "storage",
        "00c845f8",
        null,
        "undefined *"
      ]
    ],
    [
      "008d0798",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008d079c",
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

- 旧版 [`008d0744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0710.md#insn-008d0744) · [`008d0748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0710.md#insn-008d0748) · [`008d0758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0710.md#insn-008d0758)
- 新版 [`008d07ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0764.md#insn-008d07ac)

~~~diff
- 008d0744 ["COPY", "tmp:0:8", ["register:8:8"]]
- 008d0744 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008d0744 bytes e80300f9
- 008d0748 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 008d0748 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008d0748 bytes f31300f9
- 008d0758 ["INT_ADD", "register:40f0:8", ["const:8d0758:8", "const:4:8"]]
- 008d0758 ["CALL", null, ["callee:00acac44:8"]]
+ 008d07ac ["INT_ADD", "register:40f0:8", ["const:8d07ac:8", "const:4:8"]]
+ 008d07ac ["CALL", null, ["callee:00acac44:8"]]
- 008d0758 bytes 1fe90794
+ 008d07ac bytes 26e90794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d157caee8ec446fd4964aa98fde6b58c"></a>

### [`008d0824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0824.md) → [`008d0878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0878.md) FUN_008d0878

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d088c",
      "incomplete_value": false,
      "site": "008d0890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d0838",
      "incomplete_value": false,
      "site": "008d083c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:528:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d0890",
      "DATA",
      [
        "storage",
        "00c84528",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d0890",
      "DATA",
      [
        "storage",
        "00c845f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d0830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0824.md#insn-008d0830) · [`008d0838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0824.md#insn-008d0838)
- 新版 [`008d0884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0878.md#insn-008d0884) · [`008d088c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0878.md#insn-008d088c)

~~~diff
- 008d0830 ["INT_ADD", "register:40f0:8", ["const:8d0830:8", "const:4:8"]]
- 008d0830 ["CALL", null, ["callee:00c57f60:8"]]
+ 008d0884 ["INT_ADD", "register:40f0:8", ["const:8d0884:8", "const:4:8"]]
+ 008d0884 ["CALL", null, ["callee:00c57f60:8"]]
- 008d0830 bytes 981d0e94
+ 008d0884 bytes b71d0e94
- 008d0838 ["COPY", "tmp:0:8", ["const:528:8"]]
- 008d0838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d0838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d0838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d088c ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 008d088c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d088c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d088c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d0838 bytes 08a11491
+ 008d088c bytes 08e11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e677f77574c9a0c5a4f634f1af618854"></a>

### [`008d0928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0928.md) → [`008d097c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d097c.md) _INIT_171

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 85.31% / 新版 85.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d09b8",
      "incomplete_value": true,
      "site": "008d09d4",
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
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d0964",
      "incomplete_value": true,
      "site": "008d0980",
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
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f26:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d09dc",
      "incomplete_value": true,
      "site": "008d09f8",
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
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d0988",
      "incomplete_value": true,
      "site": "008d09a4",
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
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f39:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d09c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d09b8",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "008d09dc",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "008d09fc",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008d09b8",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "008d09dc",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "008d09fc",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d09c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0928.md#insn-008d09c4) · [`008d09cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0928.md#insn-008d09cc)
- 新版 [`008d0a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d097c.md#insn-008d0a18)

~~~diff
- 008d09c4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:51:8"]]
- 008d09c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008d09c4 bytes e013853c
- 008d09cc ["COPY", "tmp:0:4", ["register:4048:4"]]
- 008d09cc ["INT_ADD", "tmp:1:8", ["register:8:8", "const:81:8"]]
- 008d09cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 008d09cc bytes e9130878
+ 008d0a18 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:51:8"]]
+ 008d0a18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 008d0a18 bytes e013853c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14e2c0dcd828f14313eea2a95a3ff8dc"></a>

### [`008d0cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0cb8.md) → [`008d0d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0d0c.md) FUN_008d0d0c

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008d1c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1c40.md) · 呼出先 20件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 1件 [`008d1c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d1/008d1c94.md) · 呼出先 20件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 84.81% / 新版 84.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 31件, `call_target` 1件, `store_destination` 7件, `store_value` 24件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d0d54",
      "incomplete_value": false,
      "site": "008d0d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d0d00",
      "incomplete_value": false,
      "site": "008d0d04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d0e4c",
      "incomplete_value": true,
      "site": "008d0e4c",
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
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:3ce:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d0df8",
      "incomplete_value": true,
      "site": "008d0df8",
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
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:38e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d0e64",
      "incomplete_value": true,
      "site": "008d0e64",
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
                "const:2b1000:8"
              ],
              [
                "leaf",
                "const:f47:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d0e10",
      "incomplete_value": true,
      "site": "008d0e10",
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
                "const:2b1000:8"
              ],
              [
                "leaf",
                "const:f16:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d0d58",
      "DATA",
      [
        "storage",
        "00c845b8",
        null,
        "undefined *"
      ]
    ],
    [
      "008d0e1c",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "008d0e3c",
      "READ",
      [
        "storage",
        "002b638e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008d0d58",
      "DATA",
      [
        "storage",
        "00c84688",
        null,
        "undefined *"
      ]
    ],
    [
      "008d0e1c",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "008d0e3c",
      "READ",
      [
        "storage",
        "002b63ce",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d0dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0cb8.md#insn-008d0dbc) · [`008d0dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0cb8.md#insn-008d0dc0) · [`008d0e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0cb8.md#insn-008d0e34)
- 新版 [`008d0e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0d0c.md#insn-008d0e10) · [`008d0e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0d0c.md#insn-008d0e14) · [`008d0e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0d0c.md#insn-008d0e88)

~~~diff
- 008d0dbc ["INT_ADD", "register:40f0:8", ["const:8d0dbc:8", "const:4:8"]]
- 008d0dbc ["CALL", null, ["callee:00c57f50:8"]]
+ 008d0e10 ["INT_ADD", "register:40f0:8", ["const:8d0e10:8", "const:4:8"]]
+ 008d0e10 ["CALL", null, ["callee:00c57f50:8"]]
- 008d0dbc bytes 311c0e94
+ 008d0e10 bytes 501c0e94
- 008d0dc0 ["COPY", "register:40e0:8", ["const:ca4000:8"]]
+ 008d0e14 ["COPY", "register:40e0:8", ["const:ca5000:8"]]
- 008d0dc0 bytes bc1e0090
+ 008d0e14 bytes bc1e00b0
- 008d0e34 ["INT_ADD", "register:40f0:8", ["const:8d0e34:8", "const:4:8"]]
- 008d0e34 ["CALL", null, ["callee:006333b4:8"]]
+ 008d0e88 ["INT_ADD", "register:40f0:8", ["const:8d0e88:8", "const:4:8"]]
+ 008d0e88 ["CALL", null, ["callee:006333b4:8"]]
- 008d0e34 bytes 5089f597
+ 008d0e88 bytes 4b89f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cef86ca1e4aee467ee2cfd36e20934c0"></a>

### [`008d1a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1a28.md) → [`008d1a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d1/008d1a7c.md) FUN_008d1a7c

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008d0cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0cb8.md) [`00a95ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a95/00a95ffc.md) · 呼出先 10件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00b3cad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3c/00b3cad8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)
- 新版 呼出元 2件 [`008d0d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0d0c.md) [`00a9606c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a96/00a9606c.md) · 呼出先 10件 [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`00b3cb74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3c/00b3cb74.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 74.78% / 新版 74.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d1aa8",
      "incomplete_value": false,
      "site": "008d1ab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d1a54",
      "incomplete_value": false,
      "site": "008d1a5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d1af4",
      "incomplete_value": true,
      "site": "008d1af4",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:769:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d1aa0",
      "incomplete_value": true,
      "site": "008d1aa0",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:7c5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d1b0c",
      "incomplete_value": true,
      "site": "008d1b0c",
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
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:fa8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d1ab8",
      "incomplete_value": true,
      "site": "008d1ab8",
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
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:ffc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d1ab0",
      "DATA",
      [
        "storage",
        "00c84608",
        null,
        "pointer"
      ]
    ],
    [
      "008d1ac4",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "008d1ae4",
      "READ",
      [
        "storage",
        "002ab7c5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008d1ab0",
      "DATA",
      [
        "storage",
        "00c846d8",
        null,
        "pointer"
      ]
    ],
    [
      "008d1ac4",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "008d1ae4",
      "READ",
      [
        "storage",
        "002ab769",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d1a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1a28.md#insn-008d1a4c) · [`008d1a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1a28.md#insn-008d1a64) · [`008d1ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1a28.md#insn-008d1ad8)
- 新版 [`008d1aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d1/008d1a7c.md#insn-008d1aa0) · [`008d1ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d1/008d1a7c.md#insn-008d1ab8) · [`008d1b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d1/008d1a7c.md#insn-008d1b2c)

~~~diff
- 008d1a4c ["INT_ADD", "register:40f0:8", ["const:8d1a4c:8", "const:4:8"]]
- 008d1a4c ["CALL", null, ["callee:00b3cb74:8"]]
+ 008d1aa0 ["INT_ADD", "register:40f0:8", ["const:8d1aa0:8", "const:4:8"]]
+ 008d1aa0 ["CALL", null, ["callee:00b3cb74:8"]]
- 008d1a4c bytes 23ac0994
+ 008d1aa0 bytes 35ac0994
- 008d1a64 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 008d1a64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d1a64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d1a64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d1ab8 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008d1ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d1ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d1ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d1a64 bytes 08e13c91
+ 008d1ab8 bytes 08e10091
- 008d1ad8 ["INT_ADD", "register:40f0:8", ["const:8d1ad8:8", "const:4:8"]]
- 008d1ad8 ["CALL", null, ["callee:0047e64c:8"]]
+ 008d1b2c ["INT_ADD", "register:40f0:8", ["const:8d1b2c:8", "const:4:8"]]
+ 008d1b2c ["CALL", null, ["callee:0047e64c:8"]]
- 008d1ad8 bytes cdb2ee97
+ 008d1b2c bytes c8b2ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f16f1a3fee9d1a9d62aa000bc8f01d1"></a>

### [`008d1c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1c40.md) → [`008d1c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d1/008d1c94.md) FUN_008d1c94

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 16件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`0066d0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d0dc.md) [`008b7994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7994.md) [`008d0cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0cb8.md) [`008d83fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d83fc.md)
- 新版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 16件 [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`0066d11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066d/0066d11c.md) [`008b79ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b79ec.md) [`008d0d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0d0c.md) [`008d8450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8450.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008d1cd8",
      "incomplete_value": false,
      "site": "008d1cd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d1c84",
      "incomplete_value": false,
      "site": "008d1c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d1cd0",
      "incomplete_value": true,
      "site": "008d1cd8",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d1c7c",
      "incomplete_value": true,
      "site": "008d1c84",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:978:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008d1cdc",
      "incomplete_value": false,
      "site": "008d1cdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d1c88",
      "incomplete_value": false,
      "site": "008d1c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d1cd0",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008d1cd4",
      "READ",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ],
    [
      "008d1cd8",
      "WRITE",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008d1cd0",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008d1cd4",
      "READ",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined8"
      ]
    ],
    [
      "008d1cd8",
      "WRITE",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d1c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1c40.md#insn-008d1c84) · [`008d1c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1c40.md#insn-008d1c88) · [`008d1c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1c40.md#insn-008d1c8c)
- 新版 [`008d1cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d1/008d1c94.md#insn-008d1cd8) · [`008d1cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d1/008d1c94.md#insn-008d1cdc) · [`008d1ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d1/008d1c94.md#insn-008d1ce0)

~~~diff
- 008d1c84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:968:8"]]
- 008d1c84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008d1cd8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
+ 008d1cd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008d1c84 bytes 09b504f9
+ 008d1cd8 bytes 093505f9
- 008d1c88 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:978:8"]]
- 008d1c88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 008d1cdc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
+ 008d1cdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 008d1c88 bytes aabe04f9
+ 008d1cdc bytes aa3e05f9
- 008d1c8c ["INT_ADD", "register:40f0:8", ["const:8d1c8c:8", "const:4:8"]]
- 008d1c8c ["CALL", null, ["callee:00c57f60:8"]]
+ 008d1ce0 ["INT_ADD", "register:40f0:8", ["const:8d1ce0:8", "const:4:8"]]
+ 008d1ce0 ["CALL", null, ["callee:00c57f60:8"]]
- 008d1c8c bytes 81180e94
+ 008d1ce0 bytes a0180e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65eac82eaa9c7538afaf4a266633354f"></a>

### [`008d1eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1eb0.md) → [`008d1f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d1/008d1f04.md) FUN_008d1f04

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) [`008ad7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008ad7a4.md) [`008d31f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d31f8.md) [`008d9c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9c04.md) · 呼出先 28件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`008b6f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f10.md)
- 新版 呼出元 4件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) [`008ad7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ad/008ad7fc.md) [`008d324c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d3/008d324c.md) [`008d9c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9c58.md) · 呼出先 28件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`008b6f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f68.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.16% / 新版 76.16%

CFGの説明率　旧版 38.69% / 新版 38.97%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_condition` 1件, `store_value` 3件, `unresolved_branch_alignment` 18件, `unresolved_call_alignment` 23件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 23件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d2014",
      "incomplete_value": false,
      "site": "008d2014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d1fc0",
      "incomplete_value": false,
      "site": "008d1fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d2034"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d2050"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d1f40",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008d1f4c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008d1f54",
      "PARAM",
      [
        "storage",
        "00c845e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008d1f40",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008d1f4c",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008d1f54",
      "PARAM",
      [
        "storage",
        "00c846b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d2014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1eb0.md#insn-008d2014) · [`008d2034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1eb0.md#insn-008d2034) · [`008d2050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1eb0.md#insn-008d2050)
- 新版 [`008d2068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d1/008d1f04.md#insn-008d2068)

~~~diff
- 008d2014 ["COPY", "register:0:8", ["register:4040:8"]]
- 008d2014 ["INT_ADD", "register:40f0:8", ["const:8d2014:8", "const:4:8"]]
- 008d2014 ["CALLIND", null, ["register:0:8"]]
+ 008d2068 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008d2068 ["INT_ADD", "register:40f0:8", ["const:8d2068:8", "const:4:8"]]
+ 008d2068 ["CALLIND", null, ["register:0:8"]]
- 008d2014 bytes 00013fd6
+ 008d2068 bytes 00013fd6
- 008d2034 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d2034 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 008d2034 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:50:8"]]
- 008d2034 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008d2034 bytes 080405f8
- 008d2050 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 008d2050 ["COPY", "tmp:1:8", ["const:0:8"]]
- 008d2050 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 008d2050 bytes ff0f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5763138608e41a9abeb541df94a611d"></a>

### [`008d29a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d2/008d29a8.md) → [`008d29fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d2/008d29fc.md) FUN_008d29fc

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00732ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732ecc.md) [`008d1eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1eb0.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00732f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00732/00732f24.md) [`008d1f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d1/008d1f04.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 45.83% / 新版 42.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

アドレスに依存する影響 `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d2a20"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d2a3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d2a40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d2a20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d2ac8"
      ]
    ],
    [
      "unmatched:008d2a40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d2aa4"
      ]
    ],
    [
      "unmatched:008d2a4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d2aa8"
      ]
    ]
  ],
  "added": [
    [
      "008d2a74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d2ac8"
      ]
    ],
    [
      "008d2a94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d2aa4"
      ]
    ],
    [
      "008d2aa0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d2aa8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d2a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d2/008d29a8.md#insn-008d2a20) · [`008d2a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d2/008d29a8.md#insn-008d2a3c) · [`008d2a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d2/008d29a8.md#insn-008d2a40)

~~~diff
- 008d2a20 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008d2a20 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 008d2a20 ["CBRANCH", null, ["local:b13:8", "tmp:1:1"]]
- 008d2a20 bytes a8020054
- 008d2a3c ["COPY", "register:100:1", ["const:0:1"]]
- 008d2a3c ["COPY", "register:101:1", ["const:0:1"]]
- 008d2a3c ["COPY", "register:102:1", ["const:1:1"]]
- 008d2a3c ["COPY", "register:103:1", ["const:1:1"]]
- 008d2a3c bytes 4020601e
- 008d2a40 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008d2a40 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 008d2a40 ["CBRANCH", null, ["local:b10:8", "tmp:1:1"]]
- 008d2a40 bytes 88000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d781f82c1e65cc2e6db7a56bd6843852"></a>

### [`008d2b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d2/008d2b38.md) → [`008d2b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d2/008d2b8c.md) FUN_008d2b8c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`008d2aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d2/008d2aa4.md) [`008d870c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d870c.md) [`008d9a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9a40.md) [`008d9c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9c04.md) · 呼出先 19件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`005dbd14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005db/005dbd14.md) [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md) [`0071ec1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071ec1c.md)
- 新版 呼出元 5件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`008d2af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d2/008d2af8.md) [`008d8760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8760.md) [`008d9a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9a94.md) [`008d9c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9c58.md) · 呼出先 19件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`005dbd54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005db/005dbd54.md) [`0071bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bf30.md) [`0071ec74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071ec74.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 96.18% / 新版 96.18%

CFGの説明率　旧版 74.78% / 新版 74.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d2b3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d2b3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d2b40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d2b3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d2b40",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d2c64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d2d00"
      ]
    ]
  ],
  "added": [
    [
      "008d2b90",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008d2b94",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008d2cb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d2d00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d2b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d2/008d2b38.md#insn-008d2b3c) · [`008d2b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d2/008d2b38.md#insn-008d2b40)
- 新版 [`008d2b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d2/008d2b8c.md#insn-008d2b90)

~~~diff
- 008d2b3c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d2b3c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d2b3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 008d2b3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d2b3c bytes fd7b15a9
- 008d2b40 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008d2b40 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008d2b40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:160:8"]]
- 008d2b40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d2b40 bytes fc6f16a9
+ 008d2b90 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 008d2b90 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 008d2b90 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
+ 008d2b90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008d2b90 bytes fd7b15a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c74bef6729b4d91161694ddd30f757c"></a>

### [`008d31f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d31f8.md) → [`008d324c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d3/008d324c.md) FUN_008d324c

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 17件 [`0044da38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044da38.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`0048eef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048eef0.md)
- 新版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 17件 [`0044da78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044da78.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`0048ef30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048ef30.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.56% / 新版 76.56%

CFGの説明率　旧版 47.27% / 新版 46.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 10件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d3228"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d3448",
      "incomplete_value": true,
      "site": "008d3448",
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
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:20f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d33f4",
      "incomplete_value": true,
      "site": "008d33f4",
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
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:263:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d34b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d3228",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d322c",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "008d328c",
      "READ",
      [
        "storage",
        "00ca4f30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008d327c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "008d3280",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "008d328c",
      "READ",
      [
        "storage",
        "00ca5030",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d3228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d31f8.md#insn-008d3228) · [`008d3258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d31f8.md#insn-008d3258)
- 新版 [`008d327c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d3/008d324c.md#insn-008d327c)

~~~diff
- 008d3228 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d3228 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008d3228 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008d3228 bytes a8831ff8
- 008d3258 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008d3258 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 008d3258 bytes 600000b4
+ 008d327c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008d327c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
+ 008d327c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 008d327c bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-389233a57bd9b12e3ec359d9bfcb25d2"></a>

### [`008d35ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d35ac.md) → [`008d3600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d3/008d3600.md) FUN_008d3600

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 4件 [`0075b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b9c4.md) [`00a06510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06510.md) [`00a065dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a065dc.md) [`00a06674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06674.md) · 呼出先 0件 
- 新版 呼出元 4件 [`0075ba1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075ba1c.md) [`00a06564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06564.md) [`00a06630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06630.md) [`00a066c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a066c8.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-e81df939a13dc8375c4c13502bb82597"></a>

### [`008d35f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d35f0.md) → [`008d3644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d3/008d3644.md) FUN_008d3644

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) [`008ad7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008ad7a4.md) [`008d31f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d31f8.md) · 呼出先 4件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00865af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865af4.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 6件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) [`008ad7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ad/008ad7fc.md) [`008d324c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d3/008d324c.md) · 呼出先 4件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00865b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865b4c.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 43.75% / 新版 41.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d35f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d35f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d35f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d35f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d35f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d35fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x18]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008d3648",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "008d364c",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "008d3650",
      "WRITE",
      [
        "storage",
        "Stack[-0x18]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d35f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d35f0.md#insn-008d35f4) · [`008d35f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d35f0.md#insn-008d35f8) · [`008d35fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d35f0.md#insn-008d35fc)

~~~diff
- 008d35f4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008d35f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 008d35f4 bytes e80b00fd
- 008d35f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d35f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d35f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:18:8"]]
- 008d35f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d35f8 bytes fdfb01a9
- 008d35fc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 008d35fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 008d35fc bytes f51700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e51cb5f10b1149cc23415b6f28084ced"></a>

### [`008d389c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d389c.md) → [`008d38f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d3/008d38f0.md) FUN_008d38f0

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 39件 [`00467a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467a88.md) [`00467af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467af0.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md)
- 新版 呼出元 1件 [`00859bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859bb0.md) · 呼出先 39件 [`00467ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ac8.md) [`00467b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b30.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.33% / 新版 87.33%

CFGの説明率　旧版 30.65% / 新版 29.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 49件, `call_target` 1件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d38a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d38a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d38a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d38a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d38a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008d3924",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008d38f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "008d38f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008d3924",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d38a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d389c.md#insn-008d38a0) · [`008d38a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d389c.md#insn-008d38a4) · [`008d38d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d389c.md#insn-008d38d4)
- 新版 [`008d3928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d3/008d38f0.md#insn-008d3928)

~~~diff
- 008d38a0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:a0:8"]]
- 008d38a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 008d38a0 bytes e85300fd
- 008d38a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d38a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d38a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 008d38a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d38a4 bytes fd7b0ba9
- 008d38d4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008d38d4 ["CBRANCH", null, ["local:b146:8", "tmp:0:1"]]
+ 008d3928 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 008d3928 ["CBRANCH", null, ["local:b151:8", "tmp:0:1"]]
- 008d38d4 bytes 489d00b4
+ 008d3928 bytes 489d00b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afa2db51ad284d0f578b1a5be25a92e4"></a>

### [`008d4d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d4/008d4d5c.md) → [`008d4db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d4/008d4db0.md) FUN_008d4db0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008d2b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d2/008d2b38.md) · 呼出先 9件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005dc300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005dc/005dc300.md) [`008d8238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8238.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)
- 新版 呼出元 1件 [`008d2b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d2/008d2b8c.md) · 呼出先 9件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`005dc340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005dc/005dc340.md) [`008d828c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d828c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.49% / 新版 89.49%

CFGの説明率　旧版 52.13% / 新版 51.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 3件, `unresolved_branch_alignment` 10件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d4d60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d4d60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d4d64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d4d60",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d4d64",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d4d68",
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
      "008d4db4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008d4db8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008d4dbc",
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

- 旧版 [`008d4d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d4/008d4d5c.md#insn-008d4d60) · [`008d4d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d4/008d4d5c.md#insn-008d4d64) · [`008d4d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d4/008d4d5c.md#insn-008d4d68)

~~~diff
- 008d4d60 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d4d60 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d4d60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 008d4d60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d4d60 bytes fd7b05a9
- 008d4d64 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008d4d64 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008d4d64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 008d4d64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d4d64 bytes fc6f06a9
- 008d4d68 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 008d4d68 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 008d4d68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 008d4d68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d4d68 bytes fa6707a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-119a9f2ee4a6f04063b261d9512603b6"></a>

### [`008d51a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d51a4.md) → [`008d51f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d51f8.md) FUN_008d51f8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`008d8b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8b5c.md) · 呼出先 12件 [`0048ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce50.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008ba868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ba/008ba868.md) [`008d548c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d548c.md) [`008d9af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9af4.md)
- 新版 呼出元 2件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`008d8bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8bb0.md) · 呼出先 12件 [`0048ce90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce90.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`008ba8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008ba8c0.md) [`008d54e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d54e0.md) [`008d9b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9b48.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.04% / 新版 77.04%

CFGの説明率　旧版 15.22% / 新版 15.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d51c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5210"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5270"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d51c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d51cc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0048ce90"
      ]
    ],
    [
      "unmatched:008d51d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d52a4"
      ]
    ]
  ],
  "added": [
    [
      "008d521c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008d5220",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0048ce90"
      ]
    ],
    [
      "008d5224",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d52a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d51c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d51a4.md#insn-008d51c8) · [`008d51cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d51a4.md#insn-008d51cc) · [`008d51d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d51a4.md#insn-008d51d0)

~~~diff
- 008d51c8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d51c8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008d51c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008d51c8 bytes a8831ff8
- 008d51cc ["INT_ADD", "register:40f0:8", ["const:8d51cc:8", "const:4:8"]]
- 008d51cc ["CALL", null, ["callee:0048ce90:8"]]
- 008d51cc bytes 21dfee97
- 008d51d0 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 008d51d0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 008d51d0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 008d51d0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 008d51d0 bytes 00040036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd0b5936f0fafda1246d0ce880e9ac30"></a>

### [`008d548c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d548c.md) → [`008d54e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d54e0.md) FUN_008d54e0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`008d51a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d51a4.md) · 呼出先 17件 [`0044b7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b7a4.md) [`005618ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618ec.md) [`00561b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561b24.md) [`00561cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561cec.md) [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md)
- 新版 呼出元 2件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`008d51f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d51f8.md) · 呼出先 17件 [`0044b7e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b7e4.md) [`0056192c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/0056192c.md) [`00561b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561b64.md) [`00561d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d2c.md) [`00561d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d74.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.11% / 新版 92.11%

CFGの説明率　旧版 59.79% / 新版 61.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d551c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d552c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5530"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d5520",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007683d8"
      ]
    ],
    [
      "unmatched:008d551c",
      "WRITE",
      [
        "storage",
        "Stack[-0x87]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d5528",
      "READ",
      [
        "storage",
        "002c1801",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008d5520",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768430"
      ]
    ],
    [
      "008d5570",
      "WRITE",
      [
        "storage",
        "Stack[-0x87]",
        null,
        null
      ]
    ],
    [
      "008d557c",
      "READ",
      [
        "storage",
        "002c1841",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d54c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d548c.md#insn-008d54c8) · [`008d54cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d548c.md#insn-008d54cc) · [`008d551c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d548c.md#insn-008d551c)
- 新版 [`008d551c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d54e0.md#insn-008d551c) · [`008d5520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d54e0.md#insn-008d5520)

~~~diff
- 008d54c8 ["INT_ADD", "register:40f0:8", ["const:8d54c8:8", "const:4:8"]]
- 008d54c8 ["CALL", null, ["callee:00851550:8"]]
+ 008d551c ["INT_ADD", "register:40f0:8", ["const:8d551c:8", "const:4:8"]]
+ 008d551c ["CALL", null, ["callee:00851550:8"]]
- 008d54c8 bytes 0cf0fd97
+ 008d551c bytes 0df0fd97
- 008d54cc ["INT_ADD", "register:40f0:8", ["const:8d54cc:8", "const:4:8"]]
- 008d54cc ["CALL", null, ["ram:7683d8:8"]]
+ 008d5520 ["INT_ADD", "register:40f0:8", ["const:8d5520:8", "const:4:8"]]
+ 008d5520 ["CALL", null, ["ram:768430:8"]]
- 008d54cc bytes c34bfa97
+ 008d5520 bytes c44bfa97
- 008d551c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008d551c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:39:8"]]
- 008d551c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008d551c bytes a99203f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a576d888e1f17ecc8187cb67b912559"></a>

### [`008d5c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5c7c.md) → [`008d5cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d5cd0.md) FUN_008d5cd0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) [`00480744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)
- 新版 呼出元 1件 [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00480338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480338.md) [`00480430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480430.md) [`00480784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480784.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 18.18% / 新版 17.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_condition` 2件, `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5dc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5de0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5e14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d5dc0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5e3c"
      ]
    ],
    [
      "unmatched:008d5de0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5e18"
      ]
    ],
    [
      "unmatched:008d5e14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5db8"
      ]
    ]
  ],
  "added": [
    [
      "008d5e14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5e3c"
      ]
    ],
    [
      "008d5e34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5e18"
      ]
    ],
    [
      "008d5e68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5db8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d5cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5c7c.md#insn-008d5cf4) · [`008d5d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5c7c.md#insn-008d5d18) · [`008d5d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5c7c.md#insn-008d5d3c)
- 新版 [`008d5d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d5cd0.md#insn-008d5d48) · [`008d5d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d5cd0.md#insn-008d5d6c) · [`008d5d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d5cd0.md#insn-008d5d90)

~~~diff
- 008d5cf4 ["INT_ADD", "register:40f0:8", ["const:8d5cf4:8", "const:4:8"]]
- 008d5cf4 ["CALL", null, ["callee:00480784:8"]]
+ 008d5d48 ["INT_ADD", "register:40f0:8", ["const:8d5d48:8", "const:4:8"]]
+ 008d5d48 ["CALL", null, ["callee:00480784:8"]]
- 008d5cf4 bytes 94aaee97
+ 008d5d48 bytes 8faaee97
- 008d5d18 ["INT_ADD", "register:40f0:8", ["const:8d5d18:8", "const:4:8"]]
- 008d5d18 ["CALL", null, ["callee:00480430:8"]]
+ 008d5d6c ["INT_ADD", "register:40f0:8", ["const:8d5d6c:8", "const:4:8"]]
+ 008d5d6c ["CALL", null, ["callee:00480430:8"]]
- 008d5d18 bytes b6a9ee97
+ 008d5d6c bytes b1a9ee97
- 008d5d3c ["INT_ADD", "register:40f0:8", ["const:8d5d3c:8", "const:4:8"]]
- 008d5d3c ["CALL", null, ["callee:005c17dc:8"]]
+ 008d5d90 ["INT_ADD", "register:40f0:8", ["const:8d5d90:8", "const:4:8"]]
+ 008d5d90 ["CALL", null, ["callee:005c17dc:8"]]
- 008d5d3c bytes 98aef397
+ 008d5d90 bytes 93aef397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69af53a1267f4d7307cf30998587a4ca"></a>

### [`008d5e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5e84.md) → [`008d5ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d5ed8.md) FUN_008d5ed8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 85.51% / 新版 85.51%

CFGの説明率　旧版 34.48% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

アドレスに依存する影響 `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5ef0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5f18"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008d5f1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d5ef0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5f54"
      ]
    ],
    [
      "unmatched:008d5f1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5fa0"
      ]
    ],
    [
      "unmatched:008d5f60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5fc8"
      ]
    ]
  ],
  "added": [
    [
      "008d5f44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5f54"
      ]
    ],
    [
      "008d5f70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5fa0"
      ]
    ],
    [
      "008d5fb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d5fc8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d5ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5e84.md#insn-008d5ec8) · [`008d5ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5e84.md#insn-008d5ef0) · [`008d5f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d5e84.md#insn-008d5f18)
- 新版 [`008d5f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d5ed8.md#insn-008d5f1c)

~~~diff
- 008d5ec8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008d5ec8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 008d5ec8 ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
+ 008d5f1c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008d5f1c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 008d5f1c ["CBRANCH", null, ["local:b16:8", "tmp:1:1"]]
- 008d5ec8 bytes e8030054
+ 008d5f1c bytes e8030054
- 008d5ef0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008d5ef0 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 008d5ef0 ["CBRANCH", null, ["local:b9:8", "tmp:1:1"]]
- 008d5ef0 bytes 88000054
- 008d5f18 ["COPY", "register:100:1", ["const:0:1"]]
- 008d5f18 ["COPY", "register:101:1", ["const:0:1"]]
- 008d5f18 ["COPY", "register:102:1", ["const:1:1"]]
- 008d5f18 ["COPY", "register:103:1", ["const:1:1"]]
- 008d5f18 bytes 6020601e
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0eca99557a13dbbcb34d0ab3d79f4731"></a>

### [`008d6108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6108.md) → [`008d615c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d615c.md) FUN_008d615c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`008da7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008da7a4.md) [`008daea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008da/008daea8.md) · 呼出先 3件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`008da7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008da/008da7f8.md) [`008daefc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008da/008daefc.md) · 呼出先 3件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 53.11% / 新版 53.11%

CFGの説明率　旧版 10.12% / 新版 9.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 45件, `unresolved_call_alignment` 29件, `unresolved_store_alignment` 33件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d62bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d6310"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d6314"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d61dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008d61fc"
      ]
    ],
    [
      "008d6244",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008d61fc"
      ]
    ],
    [
      "unmatched:008d6208",
      "READ",
      [
        "storage",
        "002b5e99",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008d61dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d6250"
      ]
    ],
    [
      "008d6244",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d6250"
      ]
    ],
    [
      "008d625c",
      "READ",
      [
        "storage",
        "002b5ed9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d62bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6108.md#insn-008d62bc) · [`008d6310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6108.md#insn-008d6310)
- 新版 [`008d6310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d615c.md#insn-008d6310)

~~~diff
- 008d62bc ["COPY", "tmp:0:4", ["register:4040:4"]]
- 008d62bc ["INT_ADD", "tmp:1:8", ["register:8:8", "const:18:8"]]
- 008d62bc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 008d62bc bytes e8630039
- 008d6310 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 008d6310 ["COPY", "tmp:1:8", ["register:8:8"]]
- 008d6310 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 008d6310 bytes e8030039
+ 008d6310 ["COPY", "tmp:0:4", ["register:4040:4"]]
+ 008d6310 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:18:8"]]
+ 008d6310 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 008d6310 bytes e8630039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-885b5bee454f5cab6565d6842d64b5ac"></a>

### [`008d6c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6c90.md) → [`008d6ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6ce4.md) FUN_008d6ce4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d6c90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d6c90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d6c94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d6c90",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d6c94",
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
      "008d6ce4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008d6ce8",
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

- 旧版 [`008d6c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6c90.md#insn-008d6c90) · [`008d6c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6c90.md#insn-008d6c94) · [`008d6cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6c90.md#insn-008d6cac)
- 新版 [`008d6d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6ce4.md#insn-008d6d00)

~~~diff
- 008d6c90 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d6c90 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d6c90 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008d6c90 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008d6c90 bytes fd7bbea9
- 008d6c94 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008d6c94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008d6c94 bytes f30b00f9
- 008d6cac ["INT_ADD", "register:40f0:8", ["const:8d6cac:8", "const:4:8"]]
- 008d6cac ["CALL", null, ["callee:00c53da0:8"]]
+ 008d6d00 ["INT_ADD", "register:40f0:8", ["const:8d6d00:8", "const:4:8"]]
+ 008d6d00 ["CALL", null, ["callee:00c53da0:8"]]
- 008d6cac bytes 15f40d94
+ 008d6d00 bytes 28f40d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b112a09839bca8caad8fa80ebfed092"></a>

### [`008d6ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6ce0.md) → [`008d6d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6d34.md) FUN_008d6d34

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0089d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md) · 呼出先 19件 [`0044b7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b7a4.md) [`005618ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618ec.md) [`00561b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561b24.md) [`00561cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561cec.md) [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md)
- 新版 呼出元 1件 [`0089d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089d/0089d520.md) · 呼出先 19件 [`0044b7e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b7e4.md) [`0056192c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/0056192c.md) [`00561b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561b64.md) [`00561d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d2c.md) [`00561d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d74.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.95% / 新版 71.95%

CFGの説明率　旧版 30.38% / 新版 30.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d6ce4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d6ce4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d6d00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d6ce4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d6d00",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d6d18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007683d8"
      ]
    ]
  ],
  "added": [
    [
      "008d6d38",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008d6d54",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "008d6d6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768430"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d6ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6ce0.md#insn-008d6ce4) · [`008d6d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d6/008d6ce0.md#insn-008d6d00)
- 新版 [`008d6d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d6/008d6d34.md#insn-008d6d38)

~~~diff
- 008d6ce4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d6ce4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d6ce4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 008d6ce4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d6ce4 bytes fd7b0ea9
- 008d6d00 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d6d00 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008d6d00 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008d6d00 bytes a8831ff8
+ 008d6d38 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 008d6d38 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 008d6d38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
+ 008d6d38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008d6d38 bytes fd7b0ea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df14285a5d40ee03ac3118e11f35e7ee"></a>

### [`008d71f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d71f4.md) → [`008d7248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d7/008d7248.md) FUN_008d7248

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 18件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md)
- 新版 呼出元 1件 [`00b28ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28ff0.md) · 呼出先 18件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 77.92% / 新版 76.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d7220"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d7248"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d7278"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d7220",
      "WRITE",
      [
        "storage",
        "Stack[-0x210]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d7248",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008d7248",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008d7274",
      "WRITE",
      [
        "storage",
        "Stack[-0x210]",
        null,
        null
      ]
    ],
    [
      "008d729c",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "008d729c",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d7220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d71f4.md#insn-008d7220) · [`008d7248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d71f4.md#insn-008d7248) · [`008d724c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d71f4.md#insn-008d724c)

~~~diff
- 008d7220 ["COPY", "tmp:0:8", ["register:8:8"]]
- 008d7220 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008d7220 bytes e80300f9
- 008d7248 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:48:8"]]
- 008d7248 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008d7248 bytes e82700f9
- 008d724c ["INT_ADD", "register:40f0:8", ["const:8d724c:8", "const:4:8"]]
- 008d724c ["CALL", null, ["callee:0086a0bc:8"]]
- 008d724c bytes 864bfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c76ecddc285bf968b1a109b6f04f68c2"></a>

### [`008d76e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d76e8.md) → [`008d773c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d7/008d773c.md) FUN_008d773c

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007c7ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7ef0.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) · 呼出先 6件 [`008d8238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8238.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 6件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007c7f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007c7/007c7f48.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) [`007efd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007efd00.md) · 呼出先 6件 [`008d828c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d828c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.94% / 新版 92.94%

CFGの説明率　旧版 36.78% / 新版 35.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d76ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d76ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d77b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d76ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d7788",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d795c"
      ]
    ],
    [
      "unmatched:008d77b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008d7740",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008d77c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d795c"
      ]
    ],
    [
      "008d7804",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d76ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d76e8.md#insn-008d76ec) · [`008d7760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d76e8.md#insn-008d7760)
- 新版 [`008d7740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d7/008d773c.md#insn-008d7740) · [`008d77b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d7/008d773c.md#insn-008d77b4)

~~~diff
- 008d76ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d76ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d76ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 008d76ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d76ec bytes fd7b04a9
+ 008d7740 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 008d7740 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 008d7740 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
+ 008d7740 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008d7740 bytes fd7b04a9
- 008d7760 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008d7760 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 008d7760 ["CBRANCH", null, ["local:b48:8", "tmp:1:1"]]
+ 008d77b4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008d77b4 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 008d77b4 ["CBRANCH", null, ["local:b50:8", "tmp:1:1"]]
- 008d7760 bytes 480d0054
+ 008d77b4 bytes 480d0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71dc35aefd5c51e6df7fe2af5a19266b"></a>

### [`008d7990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d7990.md) → [`008d79e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d7/008d79e4.md) FUN_008d79e4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008d9a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9a40.md) · 呼出先 9件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0071c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071c/0071c460.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008783f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/008783f0.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)
- 新版 呼出元 1件 [`008d9a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9a94.md) · 呼出先 9件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0071c4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c4b8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00878448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878448.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.10% / 新版 83.10%

CFGの説明率　旧版 24.69% / 新版 25.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d79a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d79a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d7bb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d79a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d79dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d7a44"
      ]
    ],
    [
      "unmatched:008d79e0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "008d7a64"
      ]
    ]
  ],
  "added": [
    [
      "008d79f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008d7a30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d7a44"
      ]
    ],
    [
      "008d7a34",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "008d7a64"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d79a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d7990.md#insn-008d79a4) · [`008d79dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d7990.md#insn-008d79dc)
- 新版 [`008d79f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d7/008d79e4.md#insn-008d79f8)

~~~diff
- 008d79a4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 008d79a4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 008d79a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 008d79a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d79a4 bytes f65712a9
- 008d79dc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 008d79dc ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 008d79dc bytes a80000b5
+ 008d79f8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
+ 008d79f8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
+ 008d79f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
+ 008d79f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008d79f8 bytes f65712a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ed84fa6499d34cafbad8fec761ae5c5"></a>

### [`008d7edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d7edc.md) → [`008d7f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d7/008d7f30.md) FUN_008d7f30

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008d8154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8154.md) · 呼出先 3件 [`00672b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672b48.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`008d81a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d81a8.md) · 呼出先 3件 [`00672b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00672/00672b88.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.15% / 新版 72.15%

CFGの説明率　旧版 30.88% / 新版 31.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d7ef8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8114"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008d7f4c"
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
      "unmatched:008d7ef8",
      "DATA",
      [
        "storage",
        "00c845b8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008d7f0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d7f7c"
      ]
    ],
    [
      "unmatched:008d7f6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d7fdc"
      ]
    ]
  ],
  "added": [
    [
      "008d7f4c",
      "DATA",
      [
        "storage",
        "00c84688",
        null,
        "undefined *"
      ]
    ],
    [
      "008d7f60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d7f7c"
      ]
    ],
    [
      "008d7fc0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008d7fdc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d7ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d7edc.md#insn-008d7ef8) · [`008d7f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d7edc.md#insn-008d7f0c) · [`008d7f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d7edc.md#insn-008d7f38)
- 新版 [`008d7f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d7/008d7f30.md#insn-008d7f8c)

~~~diff
- 008d7ef8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008d7ef8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008d7ef8 bytes 080000f9
- 008d7f0c ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008d7f0c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 008d7f0c bytes e00000b5
- 008d7f38 ["INT_ADD", "register:40f0:8", ["const:8d7f38:8", "const:4:8"]]
- 008d7f38 ["CALL", null, ["callee:00c53da0:8"]]
+ 008d7f8c ["INT_ADD", "register:40f0:8", ["const:8d7f8c:8", "const:4:8"]]
+ 008d7f8c ["CALL", null, ["callee:00c53da0:8"]]
- 008d7f38 bytes 72ef0d94
+ 008d7f8c bytes 85ef0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca750a62610ca568dbcb463f471b8026"></a>

### [`008d8178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8178.md) → [`008d81cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d81cc.md) FUN_008d81cc

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00672b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672b48.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00672b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00672/00672b88.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d81e4",
      "incomplete_value": false,
      "site": "008d81e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8190",
      "incomplete_value": false,
      "site": "008d8194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "008d81e8",
      "DATA",
      [
        "storage",
        "00c84608",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008d81e8",
      "DATA",
      [
        "storage",
        "00c846d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8178.md#insn-008d8190) · [`008d81a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8178.md#insn-008d81a4) · [`008d81b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8178.md#insn-008d81b8)
- 新版 [`008d81e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d81cc.md#insn-008d81e4) · [`008d81f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d81cc.md#insn-008d81f8) · [`008d820c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d81cc.md#insn-008d820c)

~~~diff
- 008d8190 ["COPY", "tmp:0:8", ["const:608:8"]]
- 008d8190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d8190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d8190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d81e4 ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 008d81e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d81e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d81e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d8190 bytes 08211891
+ 008d81e4 bytes 08611b91
- 008d81a4 ["INT_ADD", "register:40f0:8", ["const:8d81a4:8", "const:4:8"]]
- 008d81a4 ["CALL", null, ["callee:00c53da0:8"]]
+ 008d81f8 ["INT_ADD", "register:40f0:8", ["const:8d81f8:8", "const:4:8"]]
+ 008d81f8 ["CALL", null, ["callee:00c53da0:8"]]
- 008d81a4 bytes d7ee0d94
+ 008d81f8 bytes eaee0d94
- 008d81b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008d81b8 ["INT_ADD", "register:40f0:8", ["const:8d81b8:8", "const:4:8"]]
- 008d81b8 ["CALLIND", null, ["register:0:8"]]
+ 008d820c ["COPY", "register:0:8", ["register:4040:8"]]
+ 008d820c ["INT_ADD", "register:40f0:8", ["const:8d820c:8", "const:4:8"]]
+ 008d820c ["CALLIND", null, ["register:0:8"]]
- 008d81b8 bytes 00013fd6
+ 008d820c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0344cad3cc775317cfdd62bd709e91c"></a>

### [`008d81d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d81d4.md) → [`008d8228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8228.md) FUN_008d8228

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00672b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672b48.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00672b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00672/00672b88.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d81d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d81d8"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8240",
      "incomplete_value": false,
      "site": "008d8244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d81ec",
      "incomplete_value": false,
      "site": "008d81f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "unmatched:008d81d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008d8244",
      "DATA",
      [
        "storage",
        "00c84608",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008d822c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008d8244",
      "DATA",
      [
        "storage",
        "00c846d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d81d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d81d4.md#insn-008d81d8) · [`008d8200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d81d4.md#insn-008d8200)
- 新版 [`008d8254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8228.md#insn-008d8254) · [`008d822c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8228.md#insn-008d822c)

~~~diff
- 008d81d8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008d81d8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008d81d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 008d81d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d81d8 bytes f44f01a9
- 008d8200 ["INT_ADD", "register:40f0:8", ["const:8d8200:8", "const:4:8"]]
- 008d8200 ["CALL", null, ["callee:00c53da0:8"]]
+ 008d8254 ["INT_ADD", "register:40f0:8", ["const:8d8254:8", "const:4:8"]]
+ 008d8254 ["CALL", null, ["callee:00c53da0:8"]]
- 008d8200 bytes c0ee0d94
+ 008d8254 bytes d3ee0d94
+ 008d822c ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 008d822c ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 008d822c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
+ 008d822c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008d822c bytes f44f01a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7afd78fb4911f1420dc83579a94b453"></a>

### [`008d8238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8238.md) → [`008d828c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d828c.md) FUN_008d828c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`008d2b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d2/008d2b38.md) [`008d4d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d4/008d4d5c.md) [`008d71f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d71f4.md) [`008d76e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d7/008d76e8.md) [`008d824c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d824c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 7件 [`008d2b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d2/008d2b8c.md) [`008d4db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d4/008d4db0.md) [`008d7248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d7/008d7248.md) [`008d773c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d7/008d773c.md) [`008d82a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d82a0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008d8298",
      "incomplete_value": false,
      "site": "008d829c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8244",
      "incomplete_value": false,
      "site": "008d8248",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f4c:8"
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
      "008d8298",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008d8298",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8238.md#insn-008d8248) · [`008d8244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8238.md#insn-008d8244)
- 新版 [`008d829c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d828c.md#insn-008d829c) · [`008d8298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d828c.md#insn-008d8298)

~~~diff
- 008d8248 ["INT_ADD", "register:40f0:8", ["const:8d8248:8", "const:4:8"]]
- 008d8248 ["CALL", null, ["callee:0043b7b8:8"]]
+ 008d829c ["INT_ADD", "register:40f0:8", ["const:8d829c:8", "const:4:8"]]
+ 008d829c ["CALL", null, ["callee:0043b7b8:8"]]
- 008d8248 bytes 4c8ded97
+ 008d829c bytes 478ded97
- 008d8244 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 008d8244 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008d8244 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008d8244 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008d8298 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 008d8298 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008d8298 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008d8298 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008d8244 bytes 00303d91
+ 008d8298 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e2cdc87d28a8bec58aa5ae883809247"></a>

### [`008d83b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d83b4.md) → [`008d8408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8408.md) FUN_008d8408

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d842c",
      "incomplete_value": false,
      "site": "008d842c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d83d8",
      "incomplete_value": false,
      "site": "008d83d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d842c",
      "DATA",
      [
        "storage",
        "00c84628",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008d842c",
      "DATA",
      [
        "storage",
        "00c846f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d83c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d83b4.md#insn-008d83c8) · [`008d83d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d83b4.md#insn-008d83d4)
- 新版 [`008d841c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8408.md#insn-008d841c) · [`008d8428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8408.md#insn-008d8428)

~~~diff
- 008d83c8 ["INT_ADD", "register:40f0:8", ["const:8d83c8:8", "const:4:8"]]
- 008d83c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 008d841c ["INT_ADD", "register:40f0:8", ["const:8d841c:8", "const:4:8"]]
+ 008d841c ["CALL", null, ["callee:00c57f60:8"]]
- 008d83c8 bytes b2fe0d94
+ 008d841c bytes d1fe0d94
- 008d83d4 ["COPY", "tmp:0:8", ["const:628:8"]]
- 008d83d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d83d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d83d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d8428 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 008d8428 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8428 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8428 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d83d4 bytes 08a11891
+ 008d8428 bytes 08e11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b456399696a3f5e09a8a4113282186fa"></a>

### [`008d83e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d83e8.md) → [`008d843c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d843c.md) FUN_008d843c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8448",
      "incomplete_value": false,
      "site": "008d8448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d83f4",
      "incomplete_value": false,
      "site": "008d83f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:628:8"
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
      "008d8448",
      "DATA",
      [
        "storage",
        "00c84628",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008d8448",
      "DATA",
      [
        "storage",
        "00c846f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d83f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d83e8.md#insn-008d83f0)
- 新版 [`008d8444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d843c.md#insn-008d8444)

~~~diff
- 008d83f0 ["COPY", "tmp:0:8", ["const:628:8"]]
- 008d83f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008d83f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008d83f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008d8444 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 008d8444 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008d8444 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008d8444 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008d83f0 bytes 29a11891
+ 008d8444 bytes 29e11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bbbf96e4c93d279e8dea1c61fe00b05"></a>

### [`008d8404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8404.md) → [`008d8458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8458.md) FUN_008d8458

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md) [`008d8570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8570.md) [`008d8574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8574.md) [`00acabd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00acabd4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`008b7a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a68.md) [`008d85c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d85c4.md) [`008d85c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d85c8.md) [`00acac44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aca/00acac44.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d848c",
      "incomplete_value": false,
      "site": "008d848c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8438",
      "incomplete_value": false,
      "site": "008d8438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d848c",
      "DATA",
      [
        "storage",
        "00c84698",
        null,
        "undefined *"
      ]
    ],
    [
      "008d84c4",
      "READ",
      [
        "storage",
        "00c846b8",
        null,
        "pointer"
      ]
    ],
    [
      "008d84c4",
      "READ",
      [
        "storage",
        "00c846c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d848c",
      "DATA",
      [
        "storage",
        "00c84768",
        null,
        "undefined *"
      ]
    ],
    [
      "008d84c4",
      "READ",
      [
        "storage",
        "00c84788",
        null,
        "pointer"
      ]
    ],
    [
      "008d84c4",
      "READ",
      [
        "storage",
        "00c84790",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d842c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8404.md#insn-008d842c) · [`008d8448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8404.md#insn-008d8448) · [`008d8474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8404.md#insn-008d8474)
- 新版 [`008d8480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8458.md#insn-008d8480) · [`008d849c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8458.md#insn-008d849c) · [`008d84c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8458.md#insn-008d84c8)

~~~diff
- 008d842c ["COPY", "tmp:0:8", ["const:698:8"]]
- 008d842c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d842c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d842c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d8480 ["COPY", "tmp:0:8", ["const:768:8"]]
+ 008d8480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d842c bytes 08611a91
+ 008d8480 bytes 08a11d91
- 008d8448 ["INT_ADD", "register:40f0:8", ["const:8d8448:8", "const:4:8"]]
- 008d8448 ["CALL", null, ["callee:00acac44:8"]]
+ 008d849c ["INT_ADD", "register:40f0:8", ["const:8d849c:8", "const:4:8"]]
+ 008d849c ["CALL", null, ["callee:00acac44:8"]]
- 008d8448 bytes e3c90794
+ 008d849c bytes eac90794
- 008d8474 ["COPY", "register:0:8", ["register:4040:8"]]
- 008d8474 ["INT_ADD", "register:40f0:8", ["const:8d8474:8", "const:4:8"]]
- 008d8474 ["CALLIND", null, ["register:0:8"]]
+ 008d84c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008d84c8 ["INT_ADD", "register:40f0:8", ["const:8d84c8:8", "const:4:8"]]
+ 008d84c8 ["CALLIND", null, ["register:0:8"]]
- 008d8474 bytes 00013fd6
+ 008d84c8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-734a433a0f4c0d71d8d1f78974fca2f1"></a>

### [`008d8528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8528.md) → [`008d857c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d857c.md) FUN_008d857c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d85a0",
      "incomplete_value": false,
      "site": "008d85a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d854c",
      "incomplete_value": false,
      "site": "008d854c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d85a0",
      "DATA",
      [
        "storage",
        "00c84698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d85a0",
      "DATA",
      [
        "storage",
        "00c84768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d853c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8528.md#insn-008d853c) · [`008d8548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8528.md#insn-008d8548)
- 新版 [`008d8590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d857c.md#insn-008d8590) · [`008d859c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d857c.md#insn-008d859c)

~~~diff
- 008d853c ["INT_ADD", "register:40f0:8", ["const:8d853c:8", "const:4:8"]]
- 008d853c ["CALL", null, ["callee:00c57f60:8"]]
+ 008d8590 ["INT_ADD", "register:40f0:8", ["const:8d8590:8", "const:4:8"]]
+ 008d8590 ["CALL", null, ["callee:00c57f60:8"]]
- 008d853c bytes 55fe0d94
+ 008d8590 bytes 74fe0d94
- 008d8548 ["COPY", "tmp:0:8", ["const:698:8"]]
- 008d8548 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d8548 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d8548 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d859c ["COPY", "tmp:0:8", ["const:768:8"]]
+ 008d859c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d859c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d859c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d8548 bytes 08611a91
+ 008d859c bytes 08a11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d6d3e71bb6e4cd8ee765de2f66cd985"></a>

### [`008d855c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d855c.md) → [`008d85b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d85b0.md) FUN_008d85b0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d85bc",
      "incomplete_value": false,
      "site": "008d85bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8568",
      "incomplete_value": false,
      "site": "008d8568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "008d85bc",
      "DATA",
      [
        "storage",
        "00c84698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d85bc",
      "DATA",
      [
        "storage",
        "00c84768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d855c.md#insn-008d8564)
- 新版 [`008d85b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d85b0.md#insn-008d85b8)

~~~diff
- 008d8564 ["COPY", "tmp:0:8", ["const:698:8"]]
- 008d8564 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008d8564 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008d8564 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008d85b8 ["COPY", "tmp:0:8", ["const:768:8"]]
+ 008d85b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008d85b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008d85b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008d8564 bytes 29611a91
+ 008d85b8 bytes 29a11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cefef791adb5e5155b8b18173dd7b51"></a>

### [`008d8578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8578.md) → [`008d85cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d85cc.md) FUN_008d85cc

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`007562a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00756/007562a4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b7994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7994.md) [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md) [`00ac863c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac863c.md)
- 新版 呼出元 0件  · 呼出先 6件 [`007562fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00756/007562fc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b79ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b79ec.md) [`008b7a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a68.md) [`00ac86ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac86ac.md)

変更の種類 branch_value, call, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 87.69% / 新版 87.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_target` 1件, `store_destination` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008d864c",
      "incomplete_value": false,
      "site": "008d864c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d85f8",
      "incomplete_value": false,
      "site": "008d85f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8640",
      "incomplete_value": true,
      "site": "008d864c",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d85ec",
      "incomplete_value": true,
      "site": "008d85f8",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:978:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008d8650",
      "incomplete_value": false,
      "site": "008d8650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d85fc",
      "incomplete_value": false,
      "site": "008d85fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:978:8"
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
      "008d8640",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "008d8644",
      "READ",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ],
    [
      "008d864c",
      "WRITE",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008d85f0",
      "DATA",
      [
        "storage",
        "0044e330",
        null,
        null
      ]
    ],
    [
      "008d8640",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008d8644",
      "READ",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d85a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8578.md#insn-008d85a4) · [`008d85a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8578.md#insn-008d85a8) · [`008d85cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8578.md#insn-008d85cc)
- 新版 [`008d85f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d85cc.md#insn-008d85f8) · [`008d85fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d85cc.md#insn-008d85fc) · [`008d8620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d85cc.md#insn-008d8620)

~~~diff
- 008d85a4 ["INT_ADD", "register:40f0:8", ["const:8d85a4:8", "const:4:8"]]
- 008d85a4 ["CALL", null, ["callee:00851550:8"]]
+ 008d85f8 ["INT_ADD", "register:40f0:8", ["const:8d85f8:8", "const:4:8"]]
+ 008d85f8 ["CALL", null, ["callee:00851550:8"]]
- 008d85a4 bytes d5e3fd97
+ 008d85f8 bytes d6e3fd97
- 008d85a8 ["INT_ADD", "register:40f0:8", ["const:8d85a8:8", "const:4:8"]]
- 008d85a8 ["CALL", null, ["callee:00851550:8"]]
+ 008d85fc ["INT_ADD", "register:40f0:8", ["const:8d85fc:8", "const:4:8"]]
+ 008d85fc ["CALL", null, ["callee:00851550:8"]]
- 008d85a8 bytes d4e3fd97
+ 008d85fc bytes d5e3fd97
- 008d85cc ["INT_ADD", "register:40f0:8", ["const:8d85cc:8", "const:4:8"]]
- 008d85cc ["CALL", null, ["callee:00851550:8"]]
+ 008d8620 ["INT_ADD", "register:40f0:8", ["const:8d8620:8", "const:4:8"]]
+ 008d8620 ["CALL", null, ["callee:00851550:8"]]
- 008d85cc bytes cbe3fd97
+ 008d8620 bytes cce3fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-577227c57e9e3561f1c723df3c279092"></a>

### [`008d86bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d86bc.md) → [`008d8710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8710.md) FUN_008d8710

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8734",
      "incomplete_value": false,
      "site": "008d8734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d86e0",
      "incomplete_value": false,
      "site": "008d86e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d8734",
      "DATA",
      [
        "storage",
        "00c84728",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8734",
      "DATA",
      [
        "storage",
        "00c847f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d86d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d86bc.md#insn-008d86d0) · [`008d86dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d86bc.md#insn-008d86dc)
- 新版 [`008d8724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8710.md#insn-008d8724) · [`008d8730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8710.md#insn-008d8730)

~~~diff
- 008d86d0 ["INT_ADD", "register:40f0:8", ["const:8d86d0:8", "const:4:8"]]
- 008d86d0 ["CALL", null, ["callee:00c57f60:8"]]
+ 008d8724 ["INT_ADD", "register:40f0:8", ["const:8d8724:8", "const:4:8"]]
+ 008d8724 ["CALL", null, ["callee:00c57f60:8"]]
- 008d86d0 bytes f0fd0d94
+ 008d8724 bytes 0ffe0d94
- 008d86dc ["COPY", "tmp:0:8", ["const:728:8"]]
- 008d86dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d86dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d86dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d8730 ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 008d8730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d86dc bytes 08a11c91
+ 008d8730 bytes 08e11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c703658553b30fab00060e26ddc1f01"></a>

### [`008d86f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d86f0.md) → [`008d8744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8744.md) FUN_008d8744

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8750",
      "incomplete_value": false,
      "site": "008d8750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d86fc",
      "incomplete_value": false,
      "site": "008d86fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:728:8"
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
      "008d8750",
      "DATA",
      [
        "storage",
        "00c84728",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8750",
      "DATA",
      [
        "storage",
        "00c847f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d86f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d86f0.md#insn-008d86f8)
- 新版 [`008d874c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8744.md#insn-008d874c)

~~~diff
- 008d86f8 ["COPY", "tmp:0:8", ["const:728:8"]]
- 008d86f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008d86f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008d86f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008d874c ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 008d874c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008d874c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008d874c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008d86f8 bytes 29a11c91
+ 008d874c bytes 29e11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a65a6db01d3f46417ce8a03049a6a39d"></a>

### [`008d87cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d87cc.md) → [`008d8820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8820.md) FUN_008d8820

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8844",
      "incomplete_value": false,
      "site": "008d8844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d87f0",
      "incomplete_value": false,
      "site": "008d87f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d8844",
      "DATA",
      [
        "storage",
        "00c847a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8844",
      "DATA",
      [
        "storage",
        "00c84878",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d87e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d87cc.md#insn-008d87e0) · [`008d87ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d87cc.md#insn-008d87ec)
- 新版 [`008d8834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8820.md#insn-008d8834) · [`008d8840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8820.md#insn-008d8840)

~~~diff
- 008d87e0 ["INT_ADD", "register:40f0:8", ["const:8d87e0:8", "const:4:8"]]
- 008d87e0 ["CALL", null, ["callee:00c57f60:8"]]
+ 008d8834 ["INT_ADD", "register:40f0:8", ["const:8d8834:8", "const:4:8"]]
+ 008d8834 ["CALL", null, ["callee:00c57f60:8"]]
- 008d87e0 bytes acfd0d94
+ 008d8834 bytes cbfd0d94
- 008d87ec ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 008d87ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d87ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d87ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d8840 ["COPY", "tmp:0:8", ["const:878:8"]]
+ 008d8840 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8840 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8840 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d87ec bytes 08a11e91
+ 008d8840 bytes 08e12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f33db179a6826335e2ef9b275e9f8175"></a>

### [`008d8800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8800.md) → [`008d8854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8854.md) FUN_008d8854

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8860",
      "incomplete_value": false,
      "site": "008d8860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d880c",
      "incomplete_value": false,
      "site": "008d880c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
      "008d8860",
      "DATA",
      [
        "storage",
        "00c847a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8860",
      "DATA",
      [
        "storage",
        "00c84878",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8800.md#insn-008d8808)
- 新版 [`008d885c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8854.md#insn-008d885c)

~~~diff
- 008d8808 ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 008d8808 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008d8808 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008d8808 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008d885c ["COPY", "tmp:0:8", ["const:878:8"]]
+ 008d885c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008d885c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008d885c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008d8808 bytes 29a11e91
+ 008d885c bytes 29e12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c73b9ce5c94db747bde5e442aa06be8a"></a>

### [`008d881c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d881c.md) → [`008d8870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8870.md) FUN_008d8870

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce50.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce90.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`008b7a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a68.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.58% / 新版 93.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8954",
      "incomplete_value": true,
      "site": "008d8968",
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
                "leaf",
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:bdb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8900",
      "incomplete_value": true,
      "site": "008d8914",
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
                "leaf",
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:baa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8980",
      "incomplete_value": false,
      "site": "008d8988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d892c",
      "incomplete_value": false,
      "site": "008d8934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008d88a8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008d8854",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "008d88a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008d88c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008d8954",
      "READ",
      [
        "storage",
        "002b4baa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008d88a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008d88c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008d8954",
      "READ",
      [
        "storage",
        "002b4bdb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d881c.md#insn-008d8854) · [`008d8870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d881c.md#insn-008d8870) · [`008d88a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d881c.md#insn-008d88a4)
- 新版 [`008d88a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8870.md#insn-008d88a8) · [`008d88c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8870.md#insn-008d88c4) · [`008d88f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8870.md#insn-008d88f8)

~~~diff
- 008d8854 ["INT_ADD", "register:40f0:8", ["const:8d8854:8", "const:4:8"]]
- 008d8854 ["CALL", null, ["ram:47acf4:8"]]
+ 008d88a8 ["INT_ADD", "register:40f0:8", ["const:8d88a8:8", "const:4:8"]]
+ 008d88a8 ["CALL", null, ["ram:47ad34:8"]]
- 008d8854 bytes 2889ee97
+ 008d88a8 bytes 2389ee97
- 008d8870 ["INT_ADD", "register:40f0:8", ["const:8d8870:8", "const:4:8"]]
- 008d8870 ["CALL", null, ["ram:47acf4:8"]]
+ 008d88c4 ["INT_ADD", "register:40f0:8", ["const:8d88c4:8", "const:4:8"]]
+ 008d88c4 ["CALL", null, ["ram:47ad34:8"]]
- 008d8870 bytes 2189ee97
+ 008d88c4 bytes 1c89ee97
- 008d88a4 ["INT_ADD", "register:40f0:8", ["const:8d88a4:8", "const:4:8"]]
- 008d88a4 ["CALL", null, ["callee:0048ce90:8"]]
+ 008d88f8 ["INT_ADD", "register:40f0:8", ["const:8d88f8:8", "const:4:8"]]
+ 008d88f8 ["CALL", null, ["callee:0048ce90:8"]]
- 008d88a4 bytes 6bd1ee97
+ 008d88f8 bytes 66d1ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cd452ba71699759c0bd577a5fcf2a2a"></a>

### [`008d8a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8a8c.md) → [`008d8ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8ae0.md) FUN_008d8ae0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8af4",
      "incomplete_value": false,
      "site": "008d8af8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8aa0",
      "incomplete_value": false,
      "site": "008d8aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d8af8",
      "DATA",
      [
        "storage",
        "00c84818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8af8",
      "DATA",
      [
        "storage",
        "00c848e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8a8c.md#insn-008d8a98) · [`008d8aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8a8c.md#insn-008d8aa0)
- 新版 [`008d8aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8ae0.md#insn-008d8aec) · [`008d8af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8ae0.md#insn-008d8af4)

~~~diff
- 008d8a98 ["INT_ADD", "register:40f0:8", ["const:8d8a98:8", "const:4:8"]]
- 008d8a98 ["CALL", null, ["callee:00c57f60:8"]]
+ 008d8aec ["INT_ADD", "register:40f0:8", ["const:8d8aec:8", "const:4:8"]]
+ 008d8aec ["CALL", null, ["callee:00c57f60:8"]]
- 008d8a98 bytes fefc0d94
+ 008d8aec bytes 1dfd0d94
- 008d8aa0 ["COPY", "tmp:0:8", ["const:818:8"]]
- 008d8aa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d8aa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d8aa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d8af4 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 008d8af4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8af4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8af4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d8aa0 bytes 08612091
+ 008d8af4 bytes 08a12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-857690e71d8fd1a530029708cbb98c11"></a>

### [`008d8ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8ab0.md) → [`008d8b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8b04.md) FUN_008d8b04

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8b08",
      "incomplete_value": false,
      "site": "008d8b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8ab4",
      "incomplete_value": false,
      "site": "008d8ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:818:8"
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
      "008d8b0c",
      "DATA",
      [
        "storage",
        "00c84818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8b0c",
      "DATA",
      [
        "storage",
        "00c848e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8ab0.md#insn-008d8ab4)
- 新版 [`008d8b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8b04.md#insn-008d8b08)

~~~diff
- 008d8ab4 ["COPY", "tmp:0:8", ["const:818:8"]]
- 008d8ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d8ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d8ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d8b08 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 008d8b08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8b08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8b08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d8ab4 bytes 08612091
+ 008d8b08 bytes 08a12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8720dc9086785c1e6c605e868b269dd"></a>

### [`008d8b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8b0c.md) → [`008d8b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8b60.md) FUN_008d8b60

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8b84",
      "incomplete_value": false,
      "site": "008d8b84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8b30",
      "incomplete_value": false,
      "site": "008d8b30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d8b84",
      "DATA",
      [
        "storage",
        "00c848a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8b84",
      "DATA",
      [
        "storage",
        "00c84978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8b0c.md#insn-008d8b20) · [`008d8b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8b0c.md#insn-008d8b2c)
- 新版 [`008d8b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8b60.md#insn-008d8b74) · [`008d8b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8b60.md#insn-008d8b80)

~~~diff
- 008d8b20 ["INT_ADD", "register:40f0:8", ["const:8d8b20:8", "const:4:8"]]
- 008d8b20 ["CALL", null, ["callee:00c57f60:8"]]
+ 008d8b74 ["INT_ADD", "register:40f0:8", ["const:8d8b74:8", "const:4:8"]]
+ 008d8b74 ["CALL", null, ["callee:00c57f60:8"]]
- 008d8b20 bytes dcfc0d94
+ 008d8b74 bytes fbfc0d94
- 008d8b2c ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 008d8b2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d8b2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d8b2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d8b80 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 008d8b80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8b80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8b80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d8b2c bytes 08a12291
+ 008d8b80 bytes 08e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4daacdbd4252e34492e742ebc9113f82"></a>

### [`008d8b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8b40.md) → [`008d8b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8b94.md) FUN_008d8b94

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8ba0",
      "incomplete_value": false,
      "site": "008d8ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8b4c",
      "incomplete_value": false,
      "site": "008d8b4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
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
      "008d8ba0",
      "DATA",
      [
        "storage",
        "00c848a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8ba0",
      "DATA",
      [
        "storage",
        "00c84978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8b40.md#insn-008d8b48)
- 新版 [`008d8b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8b94.md#insn-008d8b9c)

~~~diff
- 008d8b48 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 008d8b48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008d8b48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008d8b48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008d8b9c ["COPY", "tmp:0:8", ["const:978:8"]]
+ 008d8b9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008d8b9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008d8b9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008d8b48 bytes 29a12291
+ 008d8b9c bytes 29e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-555e1c2930fc431c7aec5de1298ce510"></a>

### [`008d8b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8b5c.md) → [`008d8bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8bb0.md) FUN_008d8bb0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008d51a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d5/008d51a4.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008d51f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d5/008d51f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008d8bd0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008d8b7c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008d8bdc",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008d8b88",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "008d8bd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008d8bdc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "008d8bd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008d8bdc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8b5c.md#insn-008d8b7c) · [`008d8b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8b5c.md#insn-008d8b88)
- 新版 [`008d8bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8bb0.md#insn-008d8bd0) · [`008d8bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8bb0.md#insn-008d8bdc)

~~~diff
- 008d8b7c ["INT_ADD", "register:40f0:8", ["const:8d8b7c:8", "const:4:8"]]
- 008d8b7c ["CALL", null, ["ram:47acf4:8"]]
+ 008d8bd0 ["INT_ADD", "register:40f0:8", ["const:8d8bd0:8", "const:4:8"]]
+ 008d8bd0 ["CALL", null, ["ram:47ad34:8"]]
- 008d8b7c bytes 5e88ee97
+ 008d8bd0 bytes 5988ee97
- 008d8b88 ["INT_ADD", "register:40f0:8", ["const:8d8b88:8", "const:4:8"]]
- 008d8b88 ["CALL", null, ["ram:47acf4:8"]]
+ 008d8bdc ["INT_ADD", "register:40f0:8", ["const:8d8bdc:8", "const:4:8"]]
+ 008d8bdc ["CALL", null, ["ram:47ad34:8"]]
- 008d8b88 bytes 5b88ee97
+ 008d8bdc bytes 5688ee97
~~~


<a id="compare-14580958110e7974fea18dfd12c5de32"></a>

### [`008d8be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8be0.md) → [`008d8c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8c34.md) FUN_008d8c34

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8c58",
      "incomplete_value": false,
      "site": "008d8c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8c04",
      "incomplete_value": false,
      "site": "008d8c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d8c58",
      "DATA",
      [
        "storage",
        "00c84928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8c58",
      "DATA",
      [
        "storage",
        "00c849f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8be0.md#insn-008d8bf4) · [`008d8c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8be0.md#insn-008d8c00)
- 新版 [`008d8c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8c34.md#insn-008d8c48) · [`008d8c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8c34.md#insn-008d8c54)

~~~diff
- 008d8bf4 ["INT_ADD", "register:40f0:8", ["const:8d8bf4:8", "const:4:8"]]
- 008d8bf4 ["CALL", null, ["callee:00c57f60:8"]]
+ 008d8c48 ["INT_ADD", "register:40f0:8", ["const:8d8c48:8", "const:4:8"]]
+ 008d8c48 ["CALL", null, ["callee:00c57f60:8"]]
- 008d8bf4 bytes a7fc0d94
+ 008d8c48 bytes c6fc0d94
- 008d8c00 ["COPY", "tmp:0:8", ["const:928:8"]]
- 008d8c00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d8c00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d8c00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d8c54 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 008d8c54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8c54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8c54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d8c00 bytes 08a12491
+ 008d8c54 bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8986b1cf3292f3f16fa9b30b9de37790"></a>

### [`008d8c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8c14.md) → [`008d8c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8c68.md) FUN_008d8c68

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8c74",
      "incomplete_value": false,
      "site": "008d8c74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8c20",
      "incomplete_value": false,
      "site": "008d8c20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "008d8c74",
      "DATA",
      [
        "storage",
        "00c84928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8c74",
      "DATA",
      [
        "storage",
        "00c849f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8c14.md#insn-008d8c1c)
- 新版 [`008d8c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8c68.md#insn-008d8c70)

~~~diff
- 008d8c1c ["COPY", "tmp:0:8", ["const:928:8"]]
- 008d8c1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008d8c1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008d8c1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008d8c70 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 008d8c70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008d8c70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008d8c70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008d8c1c bytes 29a12491
+ 008d8c70 bytes 29e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2001edce1497f5bd7d727fbf156af359"></a>

### [`008d8c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8c30.md) → [`008d8c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8c84.md) FUN_008d8c84

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 11件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00597644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597644.md) [`008b6e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6e58.md) [`008b6e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6e60.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00597684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597684.md) [`008b6eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6eb0.md) [`008b6eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6eb8.md)

変更の種類 call, call_argument_candidate, call_target, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8c34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8c34"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8d74",
      "incomplete_value": false,
      "site": "008d8d74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8d20",
      "incomplete_value": false,
      "site": "008d8d20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d8c34",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008d8cc0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008d8cdc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "008d8c88",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008d8cc0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008d8cdc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8c30.md#insn-008d8c34) · [`008d8c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8c30.md#insn-008d8c6c) · [`008d8c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8c30.md#insn-008d8c88)
- 新版 [`008d8cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8c84.md#insn-008d8cc0) · [`008d8cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8c84.md#insn-008d8cdc)

~~~diff
- 008d8c34 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d8c34 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d8c34 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 008d8c34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d8c34 bytes fd7b04a9
- 008d8c6c ["INT_ADD", "register:40f0:8", ["const:8d8c6c:8", "const:4:8"]]
- 008d8c6c ["CALL", null, ["ram:47acf4:8"]]
+ 008d8cc0 ["INT_ADD", "register:40f0:8", ["const:8d8cc0:8", "const:4:8"]]
+ 008d8cc0 ["CALL", null, ["ram:47ad34:8"]]
- 008d8c6c bytes 2288ee97
+ 008d8cc0 bytes 1d88ee97
- 008d8c88 ["INT_ADD", "register:40f0:8", ["const:8d8c88:8", "const:4:8"]]
- 008d8c88 ["CALL", null, ["ram:47acf4:8"]]
+ 008d8cdc ["INT_ADD", "register:40f0:8", ["const:8d8cdc:8", "const:4:8"]]
+ 008d8cdc ["CALL", null, ["ram:47ad34:8"]]
- 008d8c88 bytes 1b88ee97
+ 008d8cdc bytes 1688ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a17b0f8df66f9e0097111b35c760a79d"></a>

### [`008d8e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8e04.md) → [`008d8e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8e58.md) FUN_008d8e58

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8e7c",
      "incomplete_value": false,
      "site": "008d8e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8e28",
      "incomplete_value": false,
      "site": "008d8e2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008d8e80",
      "DATA",
      [
        "storage",
        "00c84998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8e80",
      "DATA",
      [
        "storage",
        "00c84a68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8e04.md#insn-008d8e18) · [`008d8e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8e04.md#insn-008d8e28)
- 新版 [`008d8e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8e58.md#insn-008d8e6c) · [`008d8e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8e58.md#insn-008d8e7c)

~~~diff
- 008d8e18 ["INT_ADD", "register:40f0:8", ["const:8d8e18:8", "const:4:8"]]
- 008d8e18 ["CALL", null, ["callee:00c57f60:8"]]
+ 008d8e6c ["INT_ADD", "register:40f0:8", ["const:8d8e6c:8", "const:4:8"]]
+ 008d8e6c ["CALL", null, ["callee:00c57f60:8"]]
- 008d8e18 bytes 1efc0d94
+ 008d8e6c bytes 3dfc0d94
- 008d8e28 ["COPY", "tmp:0:8", ["const:998:8"]]
- 008d8e28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d8e28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d8e28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d8e7c ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 008d8e7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8e7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8e7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d8e28 bytes 08612691
+ 008d8e7c bytes 08a12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7699a911763ebbedd0bbd7c84153d4d7"></a>

### [`008d8e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8e44.md) → [`008d8e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8e98.md) FUN_008d8e98

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d8e9c",
      "incomplete_value": false,
      "site": "008d8ea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d8e48",
      "incomplete_value": false,
      "site": "008d8e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "008d8ea0",
      "DATA",
      [
        "storage",
        "00c84998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d8ea0",
      "DATA",
      [
        "storage",
        "00c84a68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8e44.md#insn-008d8e48)
- 新版 [`008d8e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8e98.md#insn-008d8e9c)

~~~diff
- 008d8e48 ["COPY", "tmp:0:8", ["const:998:8"]]
- 008d8e48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d8e48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d8e48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d8e9c ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 008d8e9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8e9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d8e9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d8e48 bytes 08612691
+ 008d8e9c bytes 08a12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8272db45eb9b0ab1e65449a6af3d81b6"></a>

### [`008d8e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8e6c.md) → [`008d8ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d8/008d8ec0.md) FUN_008d8ec0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 22件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca54.md) [`0046cb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cb0c.md) [`00550c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c28.md)
- 新版 呼出元 0件  · 呼出先 22件 [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046ca94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca94.md) [`0046cb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cb4c.md) [`00550c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c68.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.21% / 新版 85.21%

CFGの説明率　旧版 45.95% / 新版 46.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8e70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8e70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d8e74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008d8e70",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d8e74",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:008d8e9c",
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008d8ec4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "008d8ec8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008d8ef0",
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d8e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8e6c.md#insn-008d8e70) · [`008d8e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8e6c.md#insn-008d8e74) · [`008d8ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d8e6c.md#insn-008d8ea0)

~~~diff
- 008d8e70 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008d8e70 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008d8e70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 008d8e70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d8e70 bytes fd7b0ba9
- 008d8e74 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 008d8e74 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 008d8e74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 008d8e74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008d8e74 bytes fc6f0ca9
- 008d8ea0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008d8ea0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 008d8ea0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008d8ea0 bytes a8031ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c459eedd200d3d36e2316197e7fe44a"></a>

### [`008d940c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d940c.md) → [`008d9460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9460.md) FUN_008d9460

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008d9410"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d9480",
      "incomplete_value": false,
      "site": "008d9484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d942c",
      "incomplete_value": false,
      "site": "008d9430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008d9464"
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
      "unmatched:008d9410",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008d9484",
      "DATA",
      [
        "storage",
        "00c84a08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d9464",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008d9484",
      "DATA",
      [
        "storage",
        "00c84ad8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d9410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d940c.md#insn-008d9410) · [`008d9420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d940c.md#insn-008d9420)
- 新版 [`008d9464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9460.md#insn-008d9464) · [`008d9474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9460.md#insn-008d9474)

~~~diff
- 008d9410 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008d9410 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008d9410 bytes f30b00f9
+ 008d9464 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 008d9464 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 008d9464 bytes f30b00f9
- 008d9420 ["INT_ADD", "register:40f0:8", ["const:8d9420:8", "const:4:8"]]
- 008d9420 ["CALL", null, ["callee:00c57f60:8"]]
+ 008d9474 ["INT_ADD", "register:40f0:8", ["const:8d9474:8", "const:4:8"]]
+ 008d9474 ["CALL", null, ["callee:00c57f60:8"]]
- 008d9420 bytes 9cfa0d94
+ 008d9474 bytes bbfa0d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ba067af504915478977ed04bd3174c0"></a>

### [`008d9444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9444.md) → [`008d9498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9498.md) FUN_008d9498

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d949c",
      "incomplete_value": false,
      "site": "008d94a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d9448",
      "incomplete_value": false,
      "site": "008d944c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:a08:8"
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
      "008d94a0",
      "DATA",
      [
        "storage",
        "00c84a08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d94a0",
      "DATA",
      [
        "storage",
        "00c84ad8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d9448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9444.md#insn-008d9448)
- 新版 [`008d949c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9498.md#insn-008d949c)

~~~diff
- 008d9448 ["COPY", "tmp:0:8", ["const:a08:8"]]
- 008d9448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008d9448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008d9448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008d949c ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 008d949c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008d949c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008d949c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008d9448 bytes 08212891
+ 008d949c bytes 08612b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f325c4cc8a09cdee86fa3e0ddce93900"></a>

### [`008d9518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9518.md) → [`008d956c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d956c.md) FUN_008d956c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008d9578",
      "incomplete_value": false,
      "site": "008d9578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008d9524",
      "incomplete_value": false,
      "site": "008d9524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c84000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
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
      "008d9578",
      "DATA",
      [
        "storage",
        "00c84aa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008d9578",
      "DATA",
      [
        "storage",
        "00c84b78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008d9520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9518.md#insn-008d9520)
- 新版 [`008d9574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d956c.md#insn-008d9574)

~~~diff
- 008d9520 ["COPY", "tmp:0:8", ["const:aa8:8"]]
- 008d9520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008d9520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008d9520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008d9574 ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 008d9574 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008d9574 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008d9574 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008d9520 bytes 29a12a91
+ 008d9574 bytes 29e12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

