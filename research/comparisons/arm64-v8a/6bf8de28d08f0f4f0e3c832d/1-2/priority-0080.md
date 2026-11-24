# v16.0.1 → v16.0.2 · 最優先の変更候補 (80)

[一覧の目次](README.md)

<a id="compare-74528cde0186b1efb5b7e51d6627ecf8"></a>

### [`00bbd734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd734.md) → [`00bbd7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd7d0.md) _ZNK8firebase9messaging8internal13MessageReader14ReadFromBufferERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d550.md) · 呼出先 4件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5d4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d4d0.md) [`00c5d540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d540.md)
- 新版 呼出元 1件 [`00c5d620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d620.md) · 呼出先 4件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5d5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d5a0.md) [`00c5d610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d610.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 73.74% / 新版 73.74%

CFGの説明率　旧版 58.70% / 新版 60.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 7件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd738"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd73c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd73c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbd738",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbd73c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbd740",
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
      "00bbd7d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00bbd7d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00bbd7dc",
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

- 旧版 [`00bbd738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd734.md#insn-00bbd738) · [`00bbd73c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd734.md#insn-00bbd73c) · [`00bbd740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd734.md#insn-00bbd740)

~~~diff
- 00bbd738 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 00bbd738 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 00bbd738 bytes e82b00fd
- 00bbd73c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00bbd73c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00bbd73c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00bbd73c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbd73c bytes fc6f06a9
- 00bbd740 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bbd740 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bbd740 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00bbd740 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbd740 bytes fa6707a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ac594f18f4fe61e92243c74c76710b9"></a>

### [`00bbda4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbda4c.md) → [`00bbdae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbdae8.md) _ZNK8firebase9messaging8internal13MessageReader14ConsumeMessageEPKN3com6google8firebase9messaging3cpp17SerializedMessageE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d540.md) · 呼出先 13件 [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c5d610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d610.md) · 呼出先 13件 [`0046d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d5e8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.06% / 新版 89.06%

CFGの説明率　旧版 42.28% / 新版 42.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbda84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbda88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbda88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbda84",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbda88",
      "WRITE",
      [
        "storage",
        "Stack[-0x170]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbda8c",
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
      "00bbdb20",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00bbdb24",
      "WRITE",
      [
        "storage",
        "Stack[-0x170]",
        null,
        null
      ]
    ],
    [
      "00bbdb28",
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

- 旧版 [`00bbda84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbda4c.md#insn-00bbda84) · [`00bbda88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbda4c.md#insn-00bbda88) · [`00bbda8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbda4c.md#insn-00bbda8c)

~~~diff
- 00bbda84 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bbda84 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffff98:8"]]
- 00bbda84 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bbda84 bytes a88319f8
- 00bbda88 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00bbda88 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bbda88 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00bbda88 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00bbda88 bytes ff7f1da9
- 00bbda8c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:180:8"]]
- 00bbda8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00bbda8c ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00bbda8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00bbda8c bytes e0030cad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb028551d2f0c83cc08a3a0d2f1fdcf5"></a>

### [`00bbec1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbe/00bbec1c.md) → [`00bbecb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbe/00bbecb8.md) _ZNK3com6google8firebase9messaging3cpp15SerializedEvent6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d4d0.md) · 呼出先 4件 [`00c5d4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d4e0.md) [`00c5d500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d500.md) [`00c5d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d510.md) [`00c5d520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d520.md)
- 新版 呼出元 1件 [`00c5d5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d5a0.md) · 呼出先 4件 [`00c5d5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d5b0.md) [`00c5d5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d5d0.md) [`00c5d5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d5e0.md) [`00c5d5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d5f0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 69.23% / 新版 69.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbec38"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbec5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbec88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbec38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbece0"
      ]
    ],
    [
      "unmatched:00bbec5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbed9c"
      ]
    ],
    [
      "unmatched:00bbec88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbed98"
      ]
    ]
  ],
  "added": [
    [
      "00bbecd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbece0"
      ]
    ],
    [
      "00bbecf8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbed9c"
      ]
    ],
    [
      "00bbed24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbed98"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbec38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbe/00bbec1c.md#insn-00bbec38) · [`00bbec5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbe/00bbec1c.md#insn-00bbec5c) · [`00bbec88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbe/00bbec1c.md#insn-00bbec88)

~~~diff
- 00bbec38 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00bbec38 bytes 60000054
- 00bbec5c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bbec5c ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
- 00bbec5c bytes 23050054
- 00bbec88 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bbec88 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bbec88 ["CBRANCH", null, ["local:b20:8", "tmp:1:1"]]
- 00bbec88 bytes a8030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba924b89c65554ff2b6386d5e02637eb"></a>

### [`00bbfe5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbf/00bbfe5c.md) → [`00bbfef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbf/00bbfef8.md) _ZNK3com6google8firebase9messaging3cpp22SerializedNotification6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d4f0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5d5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d5c0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 33.57% / 新版 33.57%

CFGの説明率　旧版 8.75% / 新版 8.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件

アドレスに依存する影響 `unresolved_branch_alignment` 182件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbfe84"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbfe90"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbfeb0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbfe84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc0c30"
      ]
    ],
    [
      "unmatched:00bbfe90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc0c30"
      ]
    ],
    [
      "unmatched:00bbfeb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc0c2c"
      ]
    ]
  ],
  "added": [
    [
      "00bbff20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc0c30"
      ]
    ],
    [
      "00bbff2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc0c30"
      ]
    ],
    [
      "00bbff4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc0c2c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbfe84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbf/00bbfe5c.md#insn-00bbfe84) · [`00bbfe90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbf/00bbfe5c.md#insn-00bbfe90) · [`00bbfeb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbf/00bbfe5c.md#insn-00bbfeb0)

~~~diff
- 00bbfe84 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bbfe84 ["CBRANCH", null, ["local:b328:8", "tmp:0:1"]]
- 00bbfe84 bytes 83680054
- 00bbfe90 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bbfe90 ["CBRANCH", null, ["local:b328:8", "tmp:0:1"]]
- 00bbfe90 bytes 23680054
- 00bbfeb0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bbfeb0 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bbfeb0 ["CBRANCH", null, ["local:b327:8", "tmp:1:1"]]
- 00bbfeb0 bytes 08670054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7d08f7fc0919c318d48bf593ee2b885"></a>

### [`00bc1314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1314.md) → [`00bc13b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13b0.md) _INIT_287

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc126c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc126c.md) [`00bc1274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1274.md) [`00c5abc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abc0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc1308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1308.md) [`00bc1310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1310.md) [`00c5ac90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac90.md)

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
      "definition_site": "00bc13d0",
      "incomplete_value": false,
      "site": "00bc13d0",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc13d0",
      "incomplete_value": false,
      "site": "00bc13d0",
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
            "const:844:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc13d0",
      "incomplete_value": false,
      "site": "00bc13d0",
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
                "const:510:8"
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
      "00bc13c0",
      "PARAM",
      [
        "storage",
        "01126410",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc13d0",
      "WRITE",
      [
        "storage",
        "01126410",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc13d0",
      "DATA",
      [
        "storage",
        "002a9815",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc13c0",
      "PARAM",
      [
        "storage",
        "01126510",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc13d0",
      "WRITE",
      [
        "storage",
        "01126510",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc13d0",
      "DATA",
      [
        "storage",
        "002a9844",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1314.md#insn-00bc1324) · [`00bc1328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1314.md#insn-00bc1328) · [`00bc132c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1314.md#insn-00bc132c)
- 新版 [`00bc13c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13b0.md#insn-00bc13c0) · [`00bc13c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13b0.md#insn-00bc13c4) · [`00bc13c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13b0.md#insn-00bc13c8)

~~~diff
- 00bc1324 ["COPY", "tmp:0:8", ["const:410:8"]]
- 00bc1324 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc1324 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc1324 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc13c0 ["COPY", "tmp:0:8", ["const:510:8"]]
+ 00bc13c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc13c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc13c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc1324 bytes 00401091
+ 00bc13c0 bytes 00401491
- 00bc1328 ["COPY", "tmp:0:8", ["const:815:8"]]
- 00bc1328 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1328 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1328 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc13c4 ["COPY", "tmp:0:8", ["const:844:8"]]
+ 00bc13c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc13c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc13c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc1328 bytes 08552091
+ 00bc13c4 bytes 08112191
- 00bc132c ["COPY", "tmp:0:8", ["const:26c:8"]]
- 00bc132c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bc132c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bc132c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bc13c8 ["COPY", "tmp:0:8", ["const:308:8"]]
+ 00bc13c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc13c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc13c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bc132c bytes 29b10991
+ 00bc13c8 bytes 29210c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26a7378af46a6c2150f568921cbd57ad"></a>

### [`00bc134c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc134c.md) → [`00bc13e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13e8.md) _ZN8firebase13remote_config12RemoteConfig11GetInstanceEPNS_3AppE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ab30.md) · 呼出先 11件 [`00bc1a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1a64.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abf0.md)
- 新版 呼出元 1件 [`00c5ac00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac00.md) · 呼出先 11件 [`00bc1b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acc0.md)

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
      "definition_site": "00bc1424",
      "incomplete_value": true,
      "site": "00bc1424",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc1408",
      "incomplete_value": true,
      "site": "00bc140c",
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
                "const:a00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc1464",
      "incomplete_value": true,
      "site": "00bc1468",
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
                "const:a00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00bc1400",
      "READ",
      [
        "storage",
        "00c9b930",
        null,
        "pointer"
      ]
    ],
    [
      "00bc1408",
      "PARAM",
      [
        "storage",
        "01126450",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ],
    [
      "00bc1410",
      "PARAM",
      [
        "storage",
        "01126450",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bc1400",
      "READ",
      [
        "storage",
        "00c9ba00",
        null,
        "pointer"
      ]
    ],
    [
      "00bc1408",
      "PARAM",
      [
        "storage",
        "01126550",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ],
    [
      "00bc1410",
      "PARAM",
      [
        "storage",
        "01126550",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc134c.md#insn-00bc1370) · [`00bc13cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc134c.md#insn-00bc13cc) · [`00bc13ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc134c.md#insn-00bc13ec)
- 新版 [`00bc140c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13e8.md#insn-00bc140c) · [`00bc1468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13e8.md#insn-00bc1468) · [`00bc1488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13e8.md#insn-00bc1488)

~~~diff
- 00bc1370 ["INT_ADD", "register:40f0:8", ["const:bc1370:8", "const:4:8"]]
- 00bc1370 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bc140c ["INT_ADD", "register:40f0:8", ["const:bc140c:8", "const:4:8"]]
+ 00bc140c ["CALL", null, ["callee:00c5aad0:8"]]
- 00bc1370 bytes a4650294
+ 00bc140c bytes b1650294
- 00bc13cc ["INT_ADD", "register:40f0:8", ["const:bc13cc:8", "const:4:8"]]
- 00bc13cc ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bc1468 ["INT_ADD", "register:40f0:8", ["const:bc1468:8", "const:4:8"]]
+ 00bc1468 ["CALL", null, ["callee:00c5aae0:8"]]
- 00bc13cc bytes 91650294
+ 00bc1468 bytes 9e650294
- 00bc13ec ["INT_ADD", "register:40f0:8", ["const:bc13ec:8", "const:4:8"]]
- 00bc13ec ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bc1488 ["INT_ADD", "register:40f0:8", ["const:bc1488:8", "const:4:8"]]
+ 00bc1488 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bc13ec bytes 05670294
+ 00bc1488 bytes 12670294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e143bd7b331fd76181c1fa601d843259"></a>

### [`00bc1780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1780.md) → [`00bc181c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc181c.md) _ZN8firebase13remote_config12RemoteConfigC2EPNS_3AppE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5d870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d870.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5d940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d940.md)

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
      "definition_site": "00bc183c",
      "incomplete_value": false,
      "site": "00bc1840",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bc183c",
      "PARAM",
      [
        "storage",
        "002b25d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc183c",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc17a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1780.md#insn-00bc17a4) · [`00bc17a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1780.md#insn-00bc17a0) · [`00bc17b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1780.md#insn-00bc17b0)
- 新版 [`00bc1840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc181c.md#insn-00bc1840) · [`00bc183c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc181c.md#insn-00bc183c) · [`00bc184c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc181c.md#insn-00bc184c)

~~~diff
- 00bc17a4 ["INT_ADD", "register:40f0:8", ["const:bc17a4:8", "const:4:8"]]
- 00bc17a4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bc1840 ["INT_ADD", "register:40f0:8", ["const:bc1840:8", "const:4:8"]]
+ 00bc1840 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bc17a4 bytes 17660294
+ 00bc1840 bytes 24660294
- 00bc17a0 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00bc17a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc17a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc17a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc183c ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bc183c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc183c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc183c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc17a0 bytes 00601791
+ 00bc183c bytes 00241891
- 00bc17b0 ["INT_ADD", "register:40f0:8", ["const:bc17b0:8", "const:4:8"]]
- 00bc17b0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bc184c ["INT_ADD", "register:40f0:8", ["const:bc184c:8", "const:4:8"]]
+ 00bc184c ["CALL", null, ["callee:00c57f60:8"]]
- 00bc17b0 bytes b8590294
+ 00bc184c bytes c5590294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67a145714c789d7ab44974f249eb4037"></a>

### [`00bc1a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1a64.md) → [`00bc1b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b00.md) FUN_00bc1b00

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc134c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc134c.md) · 呼出先 2件 [`00c5ade0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ade0.md) [`00c5d6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d6b0.md)
- 新版 呼出元 1件 [`00bc13e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13e8.md) · 呼出先 2件 [`00c5aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aeb0.md) [`00c5d780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d780.md)

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
      "definition_site": "00bc1b18",
      "incomplete_value": false,
      "site": "00bc1b20",
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
            "const:175:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bc1b18",
      "PARAM",
      [
        "storage",
        "002ac1d1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc1b18",
      "PARAM",
      [
        "storage",
        "002ac175",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1a64.md#insn-00bc1a84) · [`00bc1a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1a64.md#insn-00bc1a7c)
- 新版 [`00bc1b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b00.md#insn-00bc1b20) · [`00bc1b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b00.md#insn-00bc1b18)

~~~diff
- 00bc1a84 ["INT_ADD", "register:40f0:8", ["const:bc1a84:8", "const:4:8"]]
- 00bc1a84 ["CALL", null, ["callee:00c5aeb0:8"]]
+ 00bc1b20 ["INT_ADD", "register:40f0:8", ["const:bc1b20:8", "const:4:8"]]
+ 00bc1b20 ["CALL", null, ["callee:00c5aeb0:8"]]
- 00bc1a84 bytes d7640294
+ 00bc1b20 bytes e4640294
- 00bc1a7c ["COPY", "tmp:0:8", ["const:1d1:8"]]
- 00bc1a7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc1a7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc1a7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc1b18 ["COPY", "tmp:0:8", ["const:175:8"]]
+ 00bc1b18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1b18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1b18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc1a7c bytes 00440791
+ 00bc1b18 bytes 00d40591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21679f51d6e1c28d68c5441eb80c6894"></a>

### [`00bc1ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1ad8.md) → [`00bc1b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b74.md) _INIT_288

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b65510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65510.md) [`00bc1344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1344.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c5ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b655ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b655ac.md) [`00bc13e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13e0.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c5ad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad50.md)

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
      "definition_site": "00bc1b98",
      "incomplete_value": true,
      "site": "00bc1b98",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc1ba4",
      "incomplete_value": true,
      "site": "00bc1ba4",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc1ba8",
      "incomplete_value": true,
      "site": "00bc1ba8",
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
                "const:a08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00bc1b84",
      "READ",
      [
        "storage",
        "00c9b938",
        null,
        "pointer"
      ]
    ],
    [
      "00bc1b84",
      "PARAM",
      [
        "storage",
        "01126438",
        "_ZN8firebase13remote_config5g_rcsE",
        "undefined8"
      ]
    ],
    [
      "00bc1b98",
      "WRITE",
      [
        "storage",
        "01126440",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1b84",
      "READ",
      [
        "storage",
        "00c9ba08",
        null,
        "pointer"
      ]
    ],
    [
      "00bc1b84",
      "PARAM",
      [
        "storage",
        "01126538",
        "_ZN8firebase13remote_config5g_rcsE",
        "undefined8"
      ]
    ],
    [
      "00bc1b98",
      "WRITE",
      [
        "storage",
        "01126540",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1ad8.md#insn-00bc1b10) · [`00bc1b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1ad8.md#insn-00bc1b24) · [`00bc1ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1ad8.md#insn-00bc1ae8)
- 新版 [`00bc1bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b74.md#insn-00bc1bac) · [`00bc1bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b74.md#insn-00bc1bc0) · [`00bc1b84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b74.md#insn-00bc1b84)

~~~diff
- 00bc1b10 ["INT_ADD", "register:40f0:8", ["const:bc1b10:8", "const:4:8"]]
- 00bc1b10 ["CALL", null, ["callee:00c57f00:8"]]
+ 00bc1bac ["INT_ADD", "register:40f0:8", ["const:bc1bac:8", "const:4:8"]]
+ 00bc1bac ["CALL", null, ["callee:00c57f00:8"]]
- 00bc1b10 bytes c8580294
+ 00bc1bac bytes d5580294
- 00bc1b24 ["INT_ADD", "register:40f0:8", ["const:bc1b24:8", "const:4:8"]]
- 00bc1b24 ["CALL", null, ["callee:00c5ad50:8"]]
+ 00bc1bc0 ["INT_ADD", "register:40f0:8", ["const:bc1bc0:8", "const:4:8"]]
+ 00bc1bc0 ["CALL", null, ["callee:00c5ad50:8"]]
- 00bc1b24 bytes 57640294
+ 00bc1bc0 bytes 64640294
- 00bc1ae8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:938:8"]]
- 00bc1ae8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc1b84 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:a08:8"]]
+ 00bc1b84 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc1ae8 bytes 219c44f9
+ 00bc1b84 bytes 210445f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-787146448d6636ed355ab6c2ced274d1"></a>

### [`00bc1b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1b44.md) → [`00bc1be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1be0.md) _ZN8firebase13remote_config8internal6config19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allo

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc1c0c",
      "incomplete_value": true,
      "site": "00bc1c0c",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc1bf4",
      "incomplete_value": true,
      "site": "00bc1bf4",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc1c00",
      "incomplete_value": false,
      "site": "00bc1c04",
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
            "const:63a:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bc1bf0",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1c00",
      "PARAM",
      [
        "storage",
        "002b1696",
        null,
        "string"
      ]
    ],
    [
      "00bc1c0c",
      "WRITE",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1bf0",
      "READ",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1c00",
      "PARAM",
      [
        "storage",
        "002b163a",
        null,
        "string"
      ]
    ],
    [
      "00bc1c0c",
      "WRITE",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1b44.md#insn-00bc1b68) · [`00bc1b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1b44.md#insn-00bc1b70) · [`00bc1b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1b44.md#insn-00bc1b54)
- 新版 [`00bc1c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1be0.md#insn-00bc1c04) · [`00bc1c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1be0.md#insn-00bc1c0c) · [`00bc1bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1be0.md#insn-00bc1bf0)

~~~diff
- 00bc1b68 ["INT_ADD", "register:40f0:8", ["const:bc1b68:8", "const:4:8"]]
- 00bc1b68 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc1c04 ["INT_ADD", "register:40f0:8", ["const:bc1c04:8", "const:4:8"]]
+ 00bc1c04 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc1b68 bytes ea640294
+ 00bc1c04 bytes f7640294
- 00bc1b70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
- 00bc1b70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1c0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:578:8"]]
+ 00bc1c0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1b70 bytes 603e02f9
+ 00bc1c0c bytes 60be02f9
- 00bc1b54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
- 00bc1b54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc1bf0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:578:8"]]
+ 00bc1bf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc1b54 bytes 683e42f9
+ 00bc1bf0 bytes 68be42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-072612a89bcd4367a90985a236c4299e"></a>

### [`00bc1b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1b84.md) → [`00bc1c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1c20.md) _ZN8firebase13remote_config8internal6config19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allo

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc1c4c",
      "incomplete_value": true,
      "site": "00bc1c4c",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc1c34",
      "incomplete_value": true,
      "site": "00bc1c34",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc1c3c",
      "incomplete_value": false,
      "site": "00bc1c44",
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
            "const:63a:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bc1c30",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1c3c",
      "PARAM",
      [
        "storage",
        "002b1696",
        null,
        "string"
      ]
    ],
    [
      "00bc1c4c",
      "WRITE",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1c30",
      "READ",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1c3c",
      "PARAM",
      [
        "storage",
        "002b163a",
        null,
        "string"
      ]
    ],
    [
      "00bc1c4c",
      "WRITE",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1b84.md#insn-00bc1ba8) · [`00bc1bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1b84.md#insn-00bc1bb0) · [`00bc1b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1b84.md#insn-00bc1b94)
- 新版 [`00bc1c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1c20.md#insn-00bc1c44) · [`00bc1c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1c20.md#insn-00bc1c4c) · [`00bc1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1c20.md#insn-00bc1c30)

~~~diff
- 00bc1ba8 ["INT_ADD", "register:40f0:8", ["const:bc1ba8:8", "const:4:8"]]
- 00bc1ba8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc1c44 ["INT_ADD", "register:40f0:8", ["const:bc1c44:8", "const:4:8"]]
+ 00bc1c44 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc1ba8 bytes da640294
+ 00bc1c44 bytes e7640294
- 00bc1bb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
- 00bc1bb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1c4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:578:8"]]
+ 00bc1c4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1bb0 bytes 603e02f9
+ 00bc1c4c bytes 60be02f9
- 00bc1b94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
- 00bc1b94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc1c30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:578:8"]]
+ 00bc1c30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc1b94 bytes 683e42f9
+ 00bc1c30 bytes 68be42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-330f163acc2840b04a708cfd2e01ede3"></a>

### [`00bc1bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1bc4.md) → [`00bc1c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1c60.md) _ZN8firebase13remote_config8internal6config10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc1c90",
      "incomplete_value": true,
      "site": "00bc1c90",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc1c74",
      "incomplete_value": true,
      "site": "00bc1c74",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc1c80",
      "incomplete_value": false,
      "site": "00bc1c88",
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
            "const:63a:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bc1c70",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1c80",
      "PARAM",
      [
        "storage",
        "002b1696",
        null,
        "string"
      ]
    ],
    [
      "00bc1c90",
      "WRITE",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1c70",
      "READ",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1c80",
      "PARAM",
      [
        "storage",
        "002b163a",
        null,
        "string"
      ]
    ],
    [
      "00bc1c90",
      "WRITE",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1bc4.md#insn-00bc1bec) · [`00bc1bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1bc4.md#insn-00bc1bf4) · [`00bc1bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1bc4.md#insn-00bc1bd4)
- 新版 [`00bc1c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1c60.md#insn-00bc1c88) · [`00bc1c90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1c60.md#insn-00bc1c90) · [`00bc1c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1c60.md#insn-00bc1c70)

~~~diff
- 00bc1bec ["INT_ADD", "register:40f0:8", ["const:bc1bec:8", "const:4:8"]]
- 00bc1bec ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc1c88 ["INT_ADD", "register:40f0:8", ["const:bc1c88:8", "const:4:8"]]
+ 00bc1c88 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc1bec bytes c9640294
+ 00bc1c88 bytes d6640294
- 00bc1bf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
- 00bc1bf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1c90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:578:8"]]
+ 00bc1c90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1bf4 bytes 603e02f9
+ 00bc1c90 bytes 60be02f9
- 00bc1bd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
- 00bc1bd4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc1c70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:578:8"]]
+ 00bc1c70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc1bd4 bytes 683e42f9
+ 00bc1c70 bytes 68be42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc1c241de68421ce767b0a00f6b238e1"></a>

### [`00bc1c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1c08.md) → [`00bc1ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1ca4.md) _ZN8firebase13remote_config8internal6config10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc1cd4",
      "incomplete_value": true,
      "site": "00bc1cd4",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc1cb8",
      "incomplete_value": true,
      "site": "00bc1cb8",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc1cc0",
      "incomplete_value": false,
      "site": "00bc1ccc",
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
            "const:63a:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bc1cb4",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1cc0",
      "PARAM",
      [
        "storage",
        "002b1696",
        null,
        "string"
      ]
    ],
    [
      "00bc1cd4",
      "WRITE",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1cb4",
      "READ",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1cc0",
      "PARAM",
      [
        "storage",
        "002b163a",
        null,
        "string"
      ]
    ],
    [
      "00bc1cd4",
      "WRITE",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1c08.md#insn-00bc1c30) · [`00bc1c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1c08.md#insn-00bc1c38) · [`00bc1c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1c08.md#insn-00bc1c18)
- 新版 [`00bc1ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1ca4.md#insn-00bc1ccc) · [`00bc1cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1ca4.md#insn-00bc1cd4) · [`00bc1cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1ca4.md#insn-00bc1cb4)

~~~diff
- 00bc1c30 ["INT_ADD", "register:40f0:8", ["const:bc1c30:8", "const:4:8"]]
- 00bc1c30 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc1ccc ["INT_ADD", "register:40f0:8", ["const:bc1ccc:8", "const:4:8"]]
+ 00bc1ccc ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc1c30 bytes b8640294
+ 00bc1ccc bytes c5640294
- 00bc1c38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
- 00bc1c38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1cd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:578:8"]]
+ 00bc1cd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1c38 bytes 603e02f9
+ 00bc1cd4 bytes 60be02f9
- 00bc1c18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
- 00bc1c18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc1cb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:578:8"]]
+ 00bc1cb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc1c18 bytes 683e42f9
+ 00bc1cb4 bytes 68be42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34b5e386733b48246aea88e42eaf1aa2"></a>

### [`00bc1c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1c58.md) → [`00bc1cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1cf4.md) _ZN8firebase13remote_config8internal6config15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "definition_site": "00bc1d4c",
      "incomplete_value": true,
      "site": "00bc1d4c",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1cb0",
      "incomplete_value": true,
      "site": "00bc1cb0",
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
            "const:480:8"
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
      "definition_site": "00bc1d28",
      "incomplete_value": true,
      "site": "00bc1d34",
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
                "const:578:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1c8c",
      "incomplete_value": true,
      "site": "00bc1c98",
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
                "const:478:8"
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
      "00bc1d08",
      "READ",
      [
        "storage",
        "01126480",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1d28",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1d4c",
      "WRITE",
      [
        "storage",
        "01126480",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc1d08",
      "READ",
      [
        "storage",
        "01126580",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1d28",
      "READ",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1d4c",
      "WRITE",
      [
        "storage",
        "01126580",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1c58.md#insn-00bc1c98) · [`00bc1cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1c58.md#insn-00bc1cb0) · [`00bc1c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1c58.md#insn-00bc1c6c)
- 新版 [`00bc1d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1cf4.md#insn-00bc1d34) · [`00bc1d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1cf4.md#insn-00bc1d4c) · [`00bc1d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1cf4.md#insn-00bc1d08)

~~~diff
- 00bc1c98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc1c98 ["INT_ADD", "register:40f0:8", ["const:bc1c98:8", "const:4:8"]]
- 00bc1c98 ["CALLIND", null, ["register:0:8"]]
+ 00bc1d34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc1d34 ["INT_ADD", "register:40f0:8", ["const:bc1d34:8", "const:4:8"]]
+ 00bc1d34 ["CALLIND", null, ["register:0:8"]]
- 00bc1c98 bytes 00013fd6
+ 00bc1d34 bytes 00013fd6
- 00bc1cb0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bc1cb0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:480:8"]]
- 00bc1cb0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc1d4c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc1d4c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:580:8"]]
+ 00bc1d4c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc1cb0 bytes a0021239
+ 00bc1d4c bytes a0021639
- 00bc1c6c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:480:8"]]
- 00bc1c6c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bc1c6c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bc1d08 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:580:8"]]
+ 00bc1d08 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bc1d08 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bc1c6c bytes a8025239
+ 00bc1d08 bytes a8025639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff788814208d58815c9d6ea083cd6f19"></a>

### [`00bc1cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1cc4.md) → [`00bc1d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1d60.md) _ZN8firebase13remote_config8internal6config12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "site": "00bc1d00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1d20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc1d9c"
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
      "00bc1d74",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1d80",
      "READ",
      [
        "storage",
        "01126480",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1d88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc1d04"
      ]
    ]
  ],
  "added": [
    [
      "00bc1d74",
      "READ",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1d80",
      "READ",
      [
        "storage",
        "01126580",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc1d88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc1da0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1cc4.md#insn-00bc1cdc) · [`00bc1d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1cc4.md#insn-00bc1d00) · [`00bc1d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1cc4.md#insn-00bc1d08)
- 新版 [`00bc1d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1d60.md#insn-00bc1d78)

~~~diff
- 00bc1cdc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc1cdc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bc1d78 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bc1d78 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bc1cdc bytes 410200b4
+ 00bc1d78 bytes 410200b4
- 00bc1d00 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc1d00 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc1d00 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:480:8"]]
- 00bc1d00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc1d00 bytes bf021239
- 00bc1d08 ["INT_ADD", "register:40f0:8", ["const:bc1d08:8", "const:4:8"]]
- 00bc1d08 ["CALL", null, ["callee:00c5b030:8"]]
- 00bc1d08 bytes 96640294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6ae97b630cf6443b48cc1d9f894b6e9"></a>

### [`00bc1d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1d34.md) → [`00bc1dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1dd0.md) _ZN8firebase13remote_config8internal6config14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bc1d74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc1e10"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1d50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc1d48",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc1d50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc1e14"
      ]
    ],
    [
      "unmatched:00bc1d58",
      "PARAM",
      [
        "storage",
        "002b1696",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc1de4",
      "READ",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1dec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc1e14"
      ]
    ],
    [
      "00bc1df4",
      "PARAM",
      [
        "storage",
        "002b163a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1d34.md#insn-00bc1d50) · [`00bc1d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1d34.md#insn-00bc1d6c) · [`00bc1d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1d34.md#insn-00bc1d74)
- 新版 [`00bc1e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1dd0.md#insn-00bc1e08)

~~~diff
- 00bc1d50 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc1d50 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc1d50 bytes 410100b5
- 00bc1d6c ["INT_ADD", "register:40f0:8", ["const:bc1d6c:8", "const:4:8"]]
- 00bc1d6c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc1e08 ["INT_ADD", "register:40f0:8", ["const:bc1e08:8", "const:4:8"]]
+ 00bc1e08 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc1d6c bytes 69640294
+ 00bc1e08 bytes 76640294
- 00bc1d74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:478:8"]]
- 00bc1d74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1d74 bytes 803e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-390f6dac96285d3b7334edbaddda4693"></a>

### [`00bc1da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1da4.md) → [`00bc1e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1e40.md) _ZN8firebase13remote_config8internal6config11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00bc1e5c",
      "incomplete_value": false,
      "site": "00bc1e60",
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
            "const:30b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1dc0",
      "incomplete_value": false,
      "site": "00bc1dc4",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc1e6c",
      "incomplete_value": true,
      "site": "00bc1e78",
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
      "definition_site": "00bc1dd0",
      "incomplete_value": true,
      "site": "00bc1ddc",
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
      "00bc1e5c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bc1e6c",
      "DATA",
      [
        "storage",
        "01126488",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1e5c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bc1e6c",
      "DATA",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1da4.md#insn-00bc1dc4) · [`00bc1dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1da4.md#insn-00bc1dc0) · [`00bc1dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1da4.md#insn-00bc1dcc)
- 新版 [`00bc1e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1e40.md#insn-00bc1e60) · [`00bc1e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1e40.md#insn-00bc1e5c) · [`00bc1e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1e40.md#insn-00bc1e68)

~~~diff
- 00bc1dc4 ["INT_ADD", "register:40f0:8", ["const:bc1dc4:8", "const:4:8"]]
- 00bc1dc4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bc1e60 ["INT_ADD", "register:40f0:8", ["const:bc1e60:8", "const:4:8"]]
+ 00bc1e60 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bc1dc4 bytes 8f640294
+ 00bc1e60 bytes 9c640294
- 00bc1dc0 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00bc1dc0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc1dc0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc1dc0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc1e5c ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bc1e5c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1e5c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1e5c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc1dc0 bytes 009c0d91
+ 00bc1e5c bytes 002c0c91
- 00bc1dcc ["COPY", "tmp:0:8", ["const:488:8"]]
- 00bc1dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc1e68 ["COPY", "tmp:0:8", ["const:588:8"]]
+ 00bc1e68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1e68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1e68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc1dcc bytes 08211291
+ 00bc1e68 bytes 08211691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd9d6856b21f1d5a65a6fbcc2a767b08"></a>

### [`00bc1de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1de0.md) → [`00bc1e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1e7c.md) _ZN8firebase13remote_config8internal6config13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc1ebc",
      "incomplete_value": true,
      "site": "00bc1ebc",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1e20",
      "incomplete_value": true,
      "site": "00bc1e20",
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
            "const:478:8"
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
      "definition_site": "00bc1e98",
      "incomplete_value": true,
      "site": "00bc1e98",
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
      "definition_site": "00bc1dfc",
      "incomplete_value": true,
      "site": "00bc1dfc",
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
      "definition_site": "00bc1ea0",
      "incomplete_value": false,
      "site": "00bc1eb4",
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
            "const:63a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1e04",
      "incomplete_value": false,
      "site": "00bc1e18",
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
      "00bc1e90",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1ea0",
      "PARAM",
      [
        "storage",
        "002b1696",
        null,
        "string"
      ]
    ],
    [
      "00bc1ebc",
      "WRITE",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1e90",
      "READ",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1ea0",
      "PARAM",
      [
        "storage",
        "002b163a",
        null,
        "string"
      ]
    ],
    [
      "00bc1ebc",
      "WRITE",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1de0.md#insn-00bc1e18) · [`00bc1e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1de0.md#insn-00bc1e20) · [`00bc1df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1de0.md#insn-00bc1df4)
- 新版 [`00bc1eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1e7c.md#insn-00bc1eb4) · [`00bc1ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1e7c.md#insn-00bc1ebc) · [`00bc1e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1e7c.md#insn-00bc1e90)

~~~diff
- 00bc1e18 ["INT_ADD", "register:40f0:8", ["const:bc1e18:8", "const:4:8"]]
- 00bc1e18 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc1eb4 ["INT_ADD", "register:40f0:8", ["const:bc1eb4:8", "const:4:8"]]
+ 00bc1eb4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc1e18 bytes 3e640294
+ 00bc1eb4 bytes 4b640294
- 00bc1e20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:478:8"]]
- 00bc1e20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc1ebc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:578:8"]]
+ 00bc1ebc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1e20 bytes 803e02f9
+ 00bc1ebc bytes 80be02f9
- 00bc1df4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:478:8"]]
- 00bc1df4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc1e90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:578:8"]]
+ 00bc1e90 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc1df4 bytes 813e42f9
+ 00bc1e90 bytes 81be42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d27ed271fe1332acf1c25e548886e9ea"></a>

### [`00bc1e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1e50.md) → [`00bc1eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1eec.md) _ZN8firebase13remote_config8internal6config10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00bc1f08",
      "incomplete_value": false,
      "site": "00bc1f0c",
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
            "const:54d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1e6c",
      "incomplete_value": false,
      "site": "00bc1e70",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc1f18",
      "incomplete_value": true,
      "site": "00bc1f24",
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
      "definition_site": "00bc1e7c",
      "incomplete_value": true,
      "site": "00bc1e88",
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
      "00bc1f08",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bc1f18",
      "DATA",
      [
        "storage",
        "01126518",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc1f08",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bc1f18",
      "DATA",
      [
        "storage",
        "01126618",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1e50.md#insn-00bc1e70) · [`00bc1e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1e50.md#insn-00bc1e6c) · [`00bc1e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1e50.md#insn-00bc1e78)
- 新版 [`00bc1f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1eec.md#insn-00bc1f0c) · [`00bc1f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1eec.md#insn-00bc1f08) · [`00bc1f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1eec.md#insn-00bc1f14)

~~~diff
- 00bc1e70 ["INT_ADD", "register:40f0:8", ["const:bc1e70:8", "const:4:8"]]
- 00bc1e70 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bc1f0c ["INT_ADD", "register:40f0:8", ["const:bc1f0c:8", "const:4:8"]]
+ 00bc1f0c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bc1e70 bytes 64640294
+ 00bc1f0c bytes 71640294
- 00bc1e6c ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00bc1e6c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc1e6c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc1e6c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc1f08 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bc1f08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1f08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc1f08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc1e6c bytes 00781491
+ 00bc1f08 bytes 00341591
- 00bc1e78 ["COPY", "tmp:0:8", ["const:518:8"]]
- 00bc1e78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1e78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1e78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc1f14 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 00bc1f14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1f14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1f14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc1e78 bytes 08611491
+ 00bc1f14 bytes 08611891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b09b7c28f814b64639fca81fe0df6a4d"></a>

### [`00bc1e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1e8c.md) → [`00bc1f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1f28.md) _ZN8firebase13remote_config8internal12config_value19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bc1eb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc1f54"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc1f3c",
      "incomplete_value": true,
      "site": "00bc1f3c",
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
      "definition_site": "00bc1ea0",
      "incomplete_value": true,
      "site": "00bc1ea0",
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
      "00bc1f38",
      "READ",
      [
        "storage",
        "01126520",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc1eac",
      "PARAM",
      [
        "storage",
        "002c1cca",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bc1eb0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00bc1f38",
      "READ",
      [
        "storage",
        "01126620",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc1f48",
      "PARAM",
      [
        "storage",
        "002c1d0a",
        null,
        "string"
      ]
    ],
    [
      "00bc1f4c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1e8c.md#insn-00bc1ea0) · [`00bc1eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1e8c.md#insn-00bc1eb0) · [`00bc1eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1e8c.md#insn-00bc1eb8)
- 新版 [`00bc1f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1f28.md#insn-00bc1f3c)

~~~diff
- 00bc1ea0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc1ea0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bc1f3c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc1f3c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc1ea0 bytes e80000b5
+ 00bc1f3c bytes e80000b5
- 00bc1eb0 ["INT_ADD", "register:40f0:8", ["const:bc1eb0:8", "const:4:8"]]
- 00bc1eb0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc1eb0 bytes 18640294
- 00bc1eb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:520:8"]]
- 00bc1eb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1eb8 bytes 609202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5298ca89f1ed2609c9531b80876c872"></a>

### [`00bc1ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1ecc.md) → [`00bc1f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1f68.md) _ZN8firebase13remote_config8internal12config_value19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bc1ecc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1ed0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1ed0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc1ecc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc1ed0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc1f78",
      "READ",
      [
        "storage",
        "01126520",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1f68",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc1f6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc1f78",
      "READ",
      [
        "storage",
        "01126620",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1ecc.md#insn-00bc1ecc) · [`00bc1ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1ecc.md#insn-00bc1ed0) · [`00bc1ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1ecc.md#insn-00bc1ee0)
- 新版 [`00bc1f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1f68.md#insn-00bc1f7c)

~~~diff
- 00bc1ecc ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc1ecc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc1ecc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc1ecc bytes f30f1ef8
- 00bc1ed0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc1ed0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc1ed0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc1ed0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc1ed0 bytes fd7b01a9
- 00bc1ee0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc1ee0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bc1f7c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc1f7c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc1ee0 bytes e80000b5
+ 00bc1f7c bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0dbc0e1e6f1ab0cbbcdd43d2803ea10"></a>

### [`00bc1f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1f0c.md) → [`00bc1fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1fa8.md) _ZN8firebase13remote_config8internal12config_value10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_value, call, call_count, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 52.94% / 新版 52.94%

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
      "site": "00bc1f0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1f10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1f10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc1f0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc1f10",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc1fb8",
      "READ",
      [
        "storage",
        "01126520",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1fa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc1fac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc1fb8",
      "READ",
      [
        "storage",
        "01126620",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1f0c.md#insn-00bc1f0c) · [`00bc1f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1f0c.md#insn-00bc1f10) · [`00bc1f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1f0c.md#insn-00bc1f34)

~~~diff
- 00bc1f0c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc1f0c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc1f0c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc1f0c bytes f30f1ef8
- 00bc1f10 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc1f10 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc1f10 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc1f10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc1f10 bytes fd7b01a9
- 00bc1f34 ["INT_ADD", "register:40f0:8", ["const:bc1f34:8", "const:4:8"]]
- 00bc1f34 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc1f34 bytes f7630294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c5dc7a0710cb50d1989cfe078d4d5a7"></a>

### [`00bc1f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1f50.md) → [`00bc1fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1fec.md) _ZN8firebase13remote_config8internal12config_value10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 23.53% / 新版 23.53%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1f50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1f54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc1f54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc1f50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc1f54",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc1f60",
      "READ",
      [
        "storage",
        "01126520",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1fec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc1ff0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc1ffc",
      "READ",
      [
        "storage",
        "01126620",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1f50.md#insn-00bc1f50) · [`00bc1f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1f50.md#insn-00bc1f54) · [`00bc1f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1f50.md#insn-00bc1f64)

~~~diff
- 00bc1f50 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc1f50 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc1f50 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc1f50 bytes f30f1ef8
- 00bc1f54 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc1f54 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc1f54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc1f54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc1f54 bytes fd7b01a9
- 00bc1f64 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc1f64 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc1f64 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d4df9a7605c779a1a4d0c32e33bae5f"></a>

### [`00bc200c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc200c.md) → [`00bc20a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc20a8.md) _ZN8firebase13remote_config8internal12config_value12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "definition_site": "00bc20e4",
      "incomplete_value": true,
      "site": "00bc20e4",
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
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2048",
      "incomplete_value": true,
      "site": "00bc2048",
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
            "const:528:8"
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
      "definition_site": "00bc2104",
      "incomplete_value": true,
      "site": "00bc2104",
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
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2068",
      "incomplete_value": true,
      "site": "00bc2068",
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
            "const:520:8"
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
      "definition_site": "00bc20c0",
      "incomplete_value": true,
      "site": "00bc20c0",
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
      "definition_site": "00bc2024",
      "incomplete_value": true,
      "site": "00bc2024",
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
      "00bc20bc",
      "READ",
      [
        "storage",
        "01126520",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc20c8",
      "READ",
      [
        "storage",
        "01126528",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc20e4",
      "WRITE",
      [
        "storage",
        "01126528",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc20bc",
      "READ",
      [
        "storage",
        "01126620",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc20c8",
      "READ",
      [
        "storage",
        "01126628",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc20e4",
      "WRITE",
      [
        "storage",
        "01126628",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc200c.md#insn-00bc2048) · [`00bc2064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc200c.md#insn-00bc2064) · [`00bc2068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc200c.md#insn-00bc2068)
- 新版 [`00bc20e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc20a8.md#insn-00bc20e4) · [`00bc2100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc20a8.md#insn-00bc2100) · [`00bc2104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc20a8.md#insn-00bc2104)

~~~diff
- 00bc2048 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc2048 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc2048 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:528:8"]]
- 00bc2048 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bc20e4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bc20e4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bc20e4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:628:8"]]
+ 00bc20e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc2048 bytes bfa21439
+ 00bc20e4 bytes bfa21839
- 00bc2064 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc2064 ["INT_ADD", "register:40f0:8", ["const:bc2064:8", "const:4:8"]]
- 00bc2064 ["CALLIND", null, ["register:0:8"]]
+ 00bc2100 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2100 ["INT_ADD", "register:40f0:8", ["const:bc2100:8", "const:4:8"]]
+ 00bc2100 ["CALLIND", null, ["register:0:8"]]
- 00bc2064 bytes 00013fd6
+ 00bc2100 bytes 00013fd6
- 00bc2068 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:520:8"]]
- 00bc2068 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bc2068 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bc2104 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
+ 00bc2104 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bc2104 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bc2068 bytes 9f9202f9
+ 00bc2104 bytes 9f1203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c00c0797a896f4e385a883406f909c9"></a>

### [`00bc207c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc207c.md) → [`00bc2118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2118.md) _ZN8firebase13remote_config8internal12config_value14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bc20bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2158"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2098"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc2090",
      "READ",
      [
        "storage",
        "01126520",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc2098",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc215c"
      ]
    ],
    [
      "unmatched:00bc20a0",
      "PARAM",
      [
        "storage",
        "002c1cca",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc212c",
      "READ",
      [
        "storage",
        "01126620",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2134",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc215c"
      ]
    ],
    [
      "00bc213c",
      "PARAM",
      [
        "storage",
        "002c1d0a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc207c.md#insn-00bc2098) · [`00bc20b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc207c.md#insn-00bc20b4) · [`00bc20bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc207c.md#insn-00bc20bc)
- 新版 [`00bc2150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2118.md#insn-00bc2150)

~~~diff
- 00bc2098 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc2098 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc2098 bytes 410100b5
- 00bc20b4 ["INT_ADD", "register:40f0:8", ["const:bc20b4:8", "const:4:8"]]
- 00bc20b4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc2150 ["INT_ADD", "register:40f0:8", ["const:bc2150:8", "const:4:8"]]
+ 00bc2150 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc20b4 bytes 97630294
+ 00bc2150 bytes a4630294
- 00bc20bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:520:8"]]
- 00bc20bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc20bc bytes 809202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a425ce9139bc7da409dc8fe0da8aaab"></a>

### [`00bc2128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2128.md) → [`00bc21c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc21c4.md) _ZN8firebase13remote_config8internal12config_value13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bc2168"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2204"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2144"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc213c",
      "READ",
      [
        "storage",
        "01126520",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc2144",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2208"
      ]
    ],
    [
      "unmatched:00bc214c",
      "PARAM",
      [
        "storage",
        "002c1cca",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc21d8",
      "READ",
      [
        "storage",
        "01126620",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc21e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2208"
      ]
    ],
    [
      "00bc21e8",
      "PARAM",
      [
        "storage",
        "002c1d0a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2128.md#insn-00bc2144) · [`00bc2160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2128.md#insn-00bc2160) · [`00bc2168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2128.md#insn-00bc2168)
- 新版 [`00bc21fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc21c4.md#insn-00bc21fc)

~~~diff
- 00bc2144 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc2144 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc2144 bytes 410100b5
- 00bc2160 ["INT_ADD", "register:40f0:8", ["const:bc2160:8", "const:4:8"]]
- 00bc2160 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc21fc ["INT_ADD", "register:40f0:8", ["const:bc21fc:8", "const:4:8"]]
+ 00bc21fc ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc2160 bytes 6c630294
+ 00bc21fc bytes 79630294
- 00bc2168 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:520:8"]]
- 00bc2168 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2168 bytes 809202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95396db9b5d4f32e53446f1508d29111"></a>

### [`00bc21d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc21d4.md) → [`00bc2270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2270.md) _ZN8firebase13remote_config8internal11config_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

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
      "site": "00bc21d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc21d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc21d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc21d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc21d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc2280",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2270",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc2274",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc2280",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc21d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc21d4.md#insn-00bc21d4) · [`00bc21d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc21d4.md#insn-00bc21d8) · [`00bc21e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc21d4.md#insn-00bc21e8)
- 新版 [`00bc2284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2270.md#insn-00bc2284)

~~~diff
- 00bc21d4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc21d4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc21d4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc21d4 bytes f30f1ef8
- 00bc21d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc21d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc21d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc21d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc21d8 bytes fd7b01a9
- 00bc21e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc21e8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bc2284 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc2284 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc21e8 bytes e80000b5
+ 00bc2284 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40eace49f7c6dfa40f645eb5e58a0a1b"></a>

### [`00bc2214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2214.md) → [`00bc22b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc22b0.md) _ZN8firebase13remote_config8internal11config_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc22dc",
      "incomplete_value": true,
      "site": "00bc22dc",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2240",
      "incomplete_value": true,
      "site": "00bc2240",
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
            "const:568:8"
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
      "definition_site": "00bc22c4",
      "incomplete_value": true,
      "site": "00bc22c4",
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
      "definition_site": "00bc2228",
      "incomplete_value": true,
      "site": "00bc2228",
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
      "definition_site": "00bc22cc",
      "incomplete_value": false,
      "site": "00bc22d4",
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
            "const:38c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2230",
      "incomplete_value": false,
      "site": "00bc2238",
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
            "const:3e8:8"
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
      "00bc22c0",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc22cc",
      "PARAM",
      [
        "storage",
        "002a73e8",
        null,
        "string"
      ]
    ],
    [
      "00bc22dc",
      "WRITE",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc22c0",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc22cc",
      "PARAM",
      [
        "storage",
        "002a738c",
        null,
        "string"
      ]
    ],
    [
      "00bc22dc",
      "WRITE",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2214.md#insn-00bc2238) · [`00bc2240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2214.md#insn-00bc2240) · [`00bc2224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2214.md#insn-00bc2224)
- 新版 [`00bc22d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc22b0.md#insn-00bc22d4) · [`00bc22dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc22b0.md#insn-00bc22dc) · [`00bc22c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc22b0.md#insn-00bc22c0)

~~~diff
- 00bc2238 ["INT_ADD", "register:40f0:8", ["const:bc2238:8", "const:4:8"]]
- 00bc2238 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc22d4 ["INT_ADD", "register:40f0:8", ["const:bc22d4:8", "const:4:8"]]
+ 00bc22d4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc2238 bytes 36630294
+ 00bc22d4 bytes 43630294
- 00bc2240 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
- 00bc2240 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc22dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
+ 00bc22dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2240 bytes 60b602f9
+ 00bc22dc bytes 603603f9
- 00bc2224 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
- 00bc2224 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc22c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
+ 00bc22c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2224 bytes 68b642f9
+ 00bc22c0 bytes 683643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e554dec934ea5b5a7ee8db1b32ed0b7"></a>

### [`00bc2254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2254.md) → [`00bc22f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc22f0.md) _ZN8firebase13remote_config8internal11config_info10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc2320",
      "incomplete_value": true,
      "site": "00bc2320",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2284",
      "incomplete_value": true,
      "site": "00bc2284",
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
            "const:568:8"
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
      "definition_site": "00bc2304",
      "incomplete_value": true,
      "site": "00bc2304",
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
      "definition_site": "00bc2268",
      "incomplete_value": true,
      "site": "00bc2268",
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
      "definition_site": "00bc2310",
      "incomplete_value": false,
      "site": "00bc2318",
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
            "const:38c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2274",
      "incomplete_value": false,
      "site": "00bc227c",
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
            "const:3e8:8"
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
      "00bc2300",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2310",
      "PARAM",
      [
        "storage",
        "002a73e8",
        null,
        "string"
      ]
    ],
    [
      "00bc2320",
      "WRITE",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2300",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2310",
      "PARAM",
      [
        "storage",
        "002a738c",
        null,
        "string"
      ]
    ],
    [
      "00bc2320",
      "WRITE",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc227c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2254.md#insn-00bc227c) · [`00bc2284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2254.md#insn-00bc2284) · [`00bc2264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2254.md#insn-00bc2264)
- 新版 [`00bc2318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc22f0.md#insn-00bc2318) · [`00bc2320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc22f0.md#insn-00bc2320) · [`00bc2300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc22f0.md#insn-00bc2300)

~~~diff
- 00bc227c ["INT_ADD", "register:40f0:8", ["const:bc227c:8", "const:4:8"]]
- 00bc227c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc2318 ["INT_ADD", "register:40f0:8", ["const:bc2318:8", "const:4:8"]]
+ 00bc2318 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc227c bytes 25630294
+ 00bc2318 bytes 32630294
- 00bc2284 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
- 00bc2284 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2320 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
+ 00bc2320 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2284 bytes 60b602f9
+ 00bc2320 bytes 603603f9
- 00bc2264 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
- 00bc2264 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2300 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
+ 00bc2300 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2264 bytes 68b642f9
+ 00bc2300 bytes 683643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e94289e1c078f19b7206c6fb27094b6b"></a>

### [`00bc2298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2298.md) → [`00bc2334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2334.md) _ZN8firebase13remote_config8internal11config_info10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc2364",
      "incomplete_value": true,
      "site": "00bc2364",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc22c8",
      "incomplete_value": true,
      "site": "00bc22c8",
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
            "const:568:8"
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
      "definition_site": "00bc2348",
      "incomplete_value": true,
      "site": "00bc2348",
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
      "definition_site": "00bc22ac",
      "incomplete_value": true,
      "site": "00bc22ac",
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
      "definition_site": "00bc2350",
      "incomplete_value": false,
      "site": "00bc235c",
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
            "const:38c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc22b4",
      "incomplete_value": false,
      "site": "00bc22c0",
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
            "const:3e8:8"
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
      "00bc2344",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2350",
      "PARAM",
      [
        "storage",
        "002a73e8",
        null,
        "string"
      ]
    ],
    [
      "00bc2364",
      "WRITE",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2344",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2350",
      "PARAM",
      [
        "storage",
        "002a738c",
        null,
        "string"
      ]
    ],
    [
      "00bc2364",
      "WRITE",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc22c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2298.md#insn-00bc22c0) · [`00bc22c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2298.md#insn-00bc22c8) · [`00bc22a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2298.md#insn-00bc22a8)
- 新版 [`00bc235c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2334.md#insn-00bc235c) · [`00bc2364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2334.md#insn-00bc2364) · [`00bc2344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2334.md#insn-00bc2344)

~~~diff
- 00bc22c0 ["INT_ADD", "register:40f0:8", ["const:bc22c0:8", "const:4:8"]]
- 00bc22c0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc235c ["INT_ADD", "register:40f0:8", ["const:bc235c:8", "const:4:8"]]
+ 00bc235c ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc22c0 bytes 14630294
+ 00bc235c bytes 21630294
- 00bc22c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
- 00bc22c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2364 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
+ 00bc2364 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc22c8 bytes 60b602f9
+ 00bc2364 bytes 603603f9
- 00bc22a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
- 00bc22a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2344 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
+ 00bc2344 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc22a8 bytes 68b642f9
+ 00bc2344 bytes 683643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c31afaab10c4b0e2e32d2966268aeec1"></a>

### [`00bc22e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc22e8.md) → [`00bc2384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2384.md) _ZN8firebase13remote_config8internal11config_info15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "definition_site": "00bc23dc",
      "incomplete_value": true,
      "site": "00bc23dc",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2340",
      "incomplete_value": true,
      "site": "00bc2340",
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
            "const:570:8"
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
      "definition_site": "00bc23b8",
      "incomplete_value": true,
      "site": "00bc23c4",
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
                "const:668:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc231c",
      "incomplete_value": true,
      "site": "00bc2328",
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
                "const:568:8"
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
      "00bc2398",
      "READ",
      [
        "storage",
        "01126570",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc23b8",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc23dc",
      "WRITE",
      [
        "storage",
        "01126570",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc2398",
      "READ",
      [
        "storage",
        "01126670",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc23b8",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc23dc",
      "WRITE",
      [
        "storage",
        "01126670",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc22e8.md#insn-00bc2328) · [`00bc2340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc22e8.md#insn-00bc2340) · [`00bc22fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc22e8.md#insn-00bc22fc)
- 新版 [`00bc23c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2384.md#insn-00bc23c4) · [`00bc23dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2384.md#insn-00bc23dc) · [`00bc2398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2384.md#insn-00bc2398)

~~~diff
- 00bc2328 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc2328 ["INT_ADD", "register:40f0:8", ["const:bc2328:8", "const:4:8"]]
- 00bc2328 ["CALLIND", null, ["register:0:8"]]
+ 00bc23c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc23c4 ["INT_ADD", "register:40f0:8", ["const:bc23c4:8", "const:4:8"]]
+ 00bc23c4 ["CALLIND", null, ["register:0:8"]]
- 00bc2328 bytes 00013fd6
+ 00bc23c4 bytes 00013fd6
- 00bc2340 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bc2340 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:570:8"]]
- 00bc2340 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc23dc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc23dc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:670:8"]]
+ 00bc23dc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc2340 bytes a0c21539
+ 00bc23dc bytes a0c21939
- 00bc22fc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:570:8"]]
- 00bc22fc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bc22fc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bc2398 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:670:8"]]
+ 00bc2398 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2398 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bc22fc bytes a8c25539
+ 00bc2398 bytes a8c25939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8edac1716479db480ecf764ecadf39de"></a>

### [`00bc2354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2354.md) → [`00bc23f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc23f0.md) _ZN8firebase13remote_config8internal11config_info12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 14.29% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2390"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc23b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc242c"
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
      "00bc2404",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2408",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc23b4"
      ]
    ],
    [
      "00bc2410",
      "READ",
      [
        "storage",
        "01126570",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc2404",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2408",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2450"
      ]
    ],
    [
      "00bc2410",
      "READ",
      [
        "storage",
        "01126670",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc236c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2354.md#insn-00bc236c) · [`00bc238c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2354.md#insn-00bc238c) · [`00bc2390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2354.md#insn-00bc2390)
- 新版 [`00bc2408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc23f0.md#insn-00bc2408)

~~~diff
- 00bc236c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc236c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bc2408 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bc2408 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00bc236c bytes 410200b4
+ 00bc2408 bytes 410200b4
- 00bc238c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc238c ["INT_ADD", "register:40f0:8", ["const:bc238c:8", "const:4:8"]]
- 00bc238c ["CALLIND", null, ["register:0:8"]]
- 00bc238c bytes 00013fd6
- 00bc2390 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc2390 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc2390 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:570:8"]]
- 00bc2390 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc2390 bytes bfc21539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08ba6fbb784c19c68d8966e1582d965d"></a>

### [`00bc23c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc23c4.md) → [`00bc2460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2460.md) _ZN8firebase13remote_config8internal11config_info14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
      "site": "00bc2404"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc24a0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc23e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc23d8",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc23e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc24a4"
      ]
    ],
    [
      "unmatched:00bc23e8",
      "PARAM",
      [
        "storage",
        "002a73e8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2474",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc247c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc24a4"
      ]
    ],
    [
      "00bc2484",
      "PARAM",
      [
        "storage",
        "002a738c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc23e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc23c4.md#insn-00bc23e0) · [`00bc23fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc23c4.md#insn-00bc23fc) · [`00bc2404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc23c4.md#insn-00bc2404)
- 新版 [`00bc2498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2460.md#insn-00bc2498)

~~~diff
- 00bc23e0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc23e0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc23e0 bytes 410100b5
- 00bc23fc ["INT_ADD", "register:40f0:8", ["const:bc23fc:8", "const:4:8"]]
- 00bc23fc ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc2498 ["INT_ADD", "register:40f0:8", ["const:bc2498:8", "const:4:8"]]
+ 00bc2498 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc23fc bytes c5620294
+ 00bc2498 bytes d2620294
- 00bc2404 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:568:8"]]
- 00bc2404 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2404 bytes 80b602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f53b7ef58bb7fb467ecb50656278359"></a>

### [`00bc2434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2434.md) → [`00bc24d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc24d0.md) _ZN8firebase13remote_config8internal11config_info11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00bc24ec",
      "incomplete_value": false,
      "site": "00bc24f0",
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
            "const:30b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2450",
      "incomplete_value": false,
      "site": "00bc2454",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc24fc",
      "incomplete_value": true,
      "site": "00bc2508",
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
      "definition_site": "00bc2460",
      "incomplete_value": true,
      "site": "00bc246c",
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
      "00bc24ec",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bc24fc",
      "DATA",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc24ec",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bc24fc",
      "DATA",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2434.md#insn-00bc2454) · [`00bc2450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2434.md#insn-00bc2450) · [`00bc245c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2434.md#insn-00bc245c)
- 新版 [`00bc24f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc24d0.md#insn-00bc24f0) · [`00bc24ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc24d0.md#insn-00bc24ec) · [`00bc24f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc24d0.md#insn-00bc24f8)

~~~diff
- 00bc2454 ["INT_ADD", "register:40f0:8", ["const:bc2454:8", "const:4:8"]]
- 00bc2454 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bc24f0 ["INT_ADD", "register:40f0:8", ["const:bc24f0:8", "const:4:8"]]
+ 00bc24f0 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bc2454 bytes eb620294
+ 00bc24f0 bytes f8620294
- 00bc2450 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00bc2450 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2450 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2450 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc24ec ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bc24ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc24ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc24ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc2450 bytes 009c0d91
+ 00bc24ec bytes 002c0c91
- 00bc245c ["COPY", "tmp:0:8", ["const:578:8"]]
- 00bc245c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc245c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc245c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc24f8 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 00bc24f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc24f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc24f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc245c bytes 08e11591
+ 00bc24f8 bytes 08e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff681d4a131ab5420621bec6fc3b46a2"></a>

### [`00bc2470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2470.md) → [`00bc250c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc250c.md) _ZN8firebase13remote_config8internal11config_info13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bc24b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc254c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc248c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc2484",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc248c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2550"
      ]
    ],
    [
      "unmatched:00bc2494",
      "PARAM",
      [
        "storage",
        "002a73e8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2520",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2528",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2550"
      ]
    ],
    [
      "00bc2530",
      "PARAM",
      [
        "storage",
        "002a738c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc248c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2470.md#insn-00bc248c) · [`00bc24a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2470.md#insn-00bc24a8) · [`00bc24b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2470.md#insn-00bc24b0)
- 新版 [`00bc2544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc250c.md#insn-00bc2544)

~~~diff
- 00bc248c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc248c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc248c bytes 410100b5
- 00bc24a8 ["INT_ADD", "register:40f0:8", ["const:bc24a8:8", "const:4:8"]]
- 00bc24a8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc2544 ["INT_ADD", "register:40f0:8", ["const:bc2544:8", "const:4:8"]]
+ 00bc2544 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc24a8 bytes 9a620294
+ 00bc2544 bytes a7620294
- 00bc24b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:568:8"]]
- 00bc24b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc24b0 bytes 80b602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b612eeceda6acfa0b197130b234d2612"></a>

### [`00bc251c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc251c.md) → [`00bc25b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc25b8.md) _ZN8firebase13remote_config8internal15config_settings19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFile

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc25e4",
      "incomplete_value": true,
      "site": "00bc25e4",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2548",
      "incomplete_value": true,
      "site": "00bc2548",
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
            "const:598:8"
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
      "definition_site": "00bc25cc",
      "incomplete_value": true,
      "site": "00bc25cc",
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
      "definition_site": "00bc2530",
      "incomplete_value": true,
      "site": "00bc2530",
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
      "definition_site": "00bc25d8",
      "incomplete_value": false,
      "site": "00bc25dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:bcc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc253c",
      "incomplete_value": false,
      "site": "00bc2540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "00bc25c8",
      "READ",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc25d8",
      "PARAM",
      [
        "storage",
        "002b8c20",
        null,
        "string"
      ]
    ],
    [
      "00bc25e4",
      "WRITE",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc25c8",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc25d8",
      "PARAM",
      [
        "storage",
        "002b8bcc",
        null,
        "string"
      ]
    ],
    [
      "00bc25e4",
      "WRITE",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc251c.md#insn-00bc2540) · [`00bc2548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc251c.md#insn-00bc2548) · [`00bc252c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc251c.md#insn-00bc252c)
- 新版 [`00bc25dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc25b8.md#insn-00bc25dc) · [`00bc25e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc25b8.md#insn-00bc25e4) · [`00bc25c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc25b8.md#insn-00bc25c8)

~~~diff
- 00bc2540 ["INT_ADD", "register:40f0:8", ["const:bc2540:8", "const:4:8"]]
- 00bc2540 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc25dc ["INT_ADD", "register:40f0:8", ["const:bc25dc:8", "const:4:8"]]
+ 00bc25dc ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc2540 bytes 74620294
+ 00bc25dc bytes 81620294
- 00bc2548 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:598:8"]]
- 00bc2548 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc25e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00bc25e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2548 bytes 60ce02f9
+ 00bc25e4 bytes 604e03f9
- 00bc252c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:598:8"]]
- 00bc252c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc25c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00bc25c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc252c bytes 68ce42f9
+ 00bc25c8 bytes 684e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62fb08fab98633d2dccbf130a1bc8d36"></a>

### [`00bc255c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc255c.md) → [`00bc25f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc25f8.md) _ZN8firebase13remote_config8internal15config_settings19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFile

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc2624",
      "incomplete_value": true,
      "site": "00bc2624",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2588",
      "incomplete_value": true,
      "site": "00bc2588",
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
            "const:598:8"
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
      "definition_site": "00bc260c",
      "incomplete_value": true,
      "site": "00bc260c",
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
      "definition_site": "00bc2570",
      "incomplete_value": true,
      "site": "00bc2570",
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
      "definition_site": "00bc2614",
      "incomplete_value": false,
      "site": "00bc261c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:bcc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2578",
      "incomplete_value": false,
      "site": "00bc2580",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "00bc2608",
      "READ",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2614",
      "PARAM",
      [
        "storage",
        "002b8c20",
        null,
        "string"
      ]
    ],
    [
      "00bc2624",
      "WRITE",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2608",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2614",
      "PARAM",
      [
        "storage",
        "002b8bcc",
        null,
        "string"
      ]
    ],
    [
      "00bc2624",
      "WRITE",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc255c.md#insn-00bc2580) · [`00bc2588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc255c.md#insn-00bc2588) · [`00bc256c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc255c.md#insn-00bc256c)
- 新版 [`00bc261c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc25f8.md#insn-00bc261c) · [`00bc2624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc25f8.md#insn-00bc2624) · [`00bc2608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc25f8.md#insn-00bc2608)

~~~diff
- 00bc2580 ["INT_ADD", "register:40f0:8", ["const:bc2580:8", "const:4:8"]]
- 00bc2580 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc261c ["INT_ADD", "register:40f0:8", ["const:bc261c:8", "const:4:8"]]
+ 00bc261c ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc2580 bytes 64620294
+ 00bc261c bytes 71620294
- 00bc2588 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:598:8"]]
- 00bc2588 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2624 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00bc2624 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2588 bytes 60ce02f9
+ 00bc2624 bytes 604e03f9
- 00bc256c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:598:8"]]
- 00bc256c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2608 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00bc2608 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc256c bytes 68ce42f9
+ 00bc2608 bytes 684e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b7ebf94121f198e175eb541a2b18413"></a>

### [`00bc259c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc259c.md) → [`00bc2638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2638.md) _ZN8firebase13remote_config8internal15config_settings10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

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
      "site": "00bc25cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2668"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc264c",
      "incomplete_value": true,
      "site": "00bc264c",
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
      "definition_site": "00bc25b0",
      "incomplete_value": true,
      "site": "00bc25b0",
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
      "00bc2648",
      "READ",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc25bc",
      "PARAM",
      [
        "storage",
        "002b8c20",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bc25c4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00bc2648",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2658",
      "PARAM",
      [
        "storage",
        "002b8bcc",
        null,
        "string"
      ]
    ],
    [
      "00bc2660",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc25b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc259c.md#insn-00bc25b0) · [`00bc25c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc259c.md#insn-00bc25c4) · [`00bc25cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc259c.md#insn-00bc25cc)
- 新版 [`00bc264c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2638.md#insn-00bc264c)

~~~diff
- 00bc25b0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc25b0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bc264c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc264c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc25b0 bytes 080100b5
+ 00bc264c bytes 080100b5
- 00bc25c4 ["INT_ADD", "register:40f0:8", ["const:bc25c4:8", "const:4:8"]]
- 00bc25c4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc25c4 bytes 53620294
- 00bc25cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:598:8"]]
- 00bc25cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc25cc bytes 60ce02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11b0276c13a4cd733a98db52f9cfb795"></a>

### [`00bc25e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc25e0.md) → [`00bc267c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc267c.md) _ZN8firebase13remote_config8internal15config_settings10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc26ac",
      "incomplete_value": true,
      "site": "00bc26ac",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2610",
      "incomplete_value": true,
      "site": "00bc2610",
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
            "const:598:8"
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
      "definition_site": "00bc2690",
      "incomplete_value": true,
      "site": "00bc2690",
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
      "definition_site": "00bc25f4",
      "incomplete_value": true,
      "site": "00bc25f4",
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
      "definition_site": "00bc2698",
      "incomplete_value": false,
      "site": "00bc26a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:bcc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc25fc",
      "incomplete_value": false,
      "site": "00bc2608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "00bc268c",
      "READ",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2698",
      "PARAM",
      [
        "storage",
        "002b8c20",
        null,
        "string"
      ]
    ],
    [
      "00bc26ac",
      "WRITE",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc268c",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2698",
      "PARAM",
      [
        "storage",
        "002b8bcc",
        null,
        "string"
      ]
    ],
    [
      "00bc26ac",
      "WRITE",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc25e0.md#insn-00bc2608) · [`00bc2610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc25e0.md#insn-00bc2610) · [`00bc25f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc25e0.md#insn-00bc25f0)
- 新版 [`00bc26a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc267c.md#insn-00bc26a4) · [`00bc26ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc267c.md#insn-00bc26ac) · [`00bc268c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc267c.md#insn-00bc268c)

~~~diff
- 00bc2608 ["INT_ADD", "register:40f0:8", ["const:bc2608:8", "const:4:8"]]
- 00bc2608 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc26a4 ["INT_ADD", "register:40f0:8", ["const:bc26a4:8", "const:4:8"]]
+ 00bc26a4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc2608 bytes 42620294
+ 00bc26a4 bytes 4f620294
- 00bc2610 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:598:8"]]
- 00bc2610 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc26ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00bc26ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2610 bytes 60ce02f9
+ 00bc26ac bytes 604e03f9
- 00bc25f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:598:8"]]
- 00bc25f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc268c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00bc268c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc25f0 bytes 68ce42f9
+ 00bc268c bytes 684e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f191863afd47107351f083a01d96fcc"></a>

### [`00bc2630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2630.md) → [`00bc26cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc26cc.md) _ZN8firebase13remote_config8internal15config_settings15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "definition_site": "00bc2724",
      "incomplete_value": true,
      "site": "00bc2724",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2688",
      "incomplete_value": true,
      "site": "00bc2688",
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
            "const:5a0:8"
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
      "definition_site": "00bc2700",
      "incomplete_value": true,
      "site": "00bc270c",
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
                "const:698:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2664",
      "incomplete_value": true,
      "site": "00bc2670",
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
                "const:598:8"
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
      "00bc26e0",
      "READ",
      [
        "storage",
        "011265a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2700",
      "READ",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2724",
      "WRITE",
      [
        "storage",
        "011265a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc26e0",
      "READ",
      [
        "storage",
        "011266a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2700",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2724",
      "WRITE",
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

- 旧版 [`00bc2670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2630.md#insn-00bc2670) · [`00bc2688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2630.md#insn-00bc2688) · [`00bc2644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2630.md#insn-00bc2644)
- 新版 [`00bc270c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc26cc.md#insn-00bc270c) · [`00bc2724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc26cc.md#insn-00bc2724) · [`00bc26e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc26cc.md#insn-00bc26e0)

~~~diff
- 00bc2670 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc2670 ["INT_ADD", "register:40f0:8", ["const:bc2670:8", "const:4:8"]]
- 00bc2670 ["CALLIND", null, ["register:0:8"]]
+ 00bc270c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc270c ["INT_ADD", "register:40f0:8", ["const:bc270c:8", "const:4:8"]]
+ 00bc270c ["CALLIND", null, ["register:0:8"]]
- 00bc2670 bytes 00013fd6
+ 00bc270c bytes 00013fd6
- 00bc2688 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bc2688 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5a0:8"]]
- 00bc2688 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc2724 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc2724 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6a0:8"]]
+ 00bc2724 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc2688 bytes a0821639
+ 00bc2724 bytes a0821a39
- 00bc2644 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5a0:8"]]
- 00bc2644 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bc2644 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bc26e0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6a0:8"]]
+ 00bc26e0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bc26e0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bc2644 bytes a8825639
+ 00bc26e0 bytes a8825a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-878e951086b5d5294815efcccdbb4d12"></a>

### [`00bc269c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc269c.md) → [`00bc2738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2738.md) _ZN8firebase13remote_config8internal15config_settings12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc26d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc26f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2774"
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
      "00bc274c",
      "READ",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2750",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc26fc"
      ]
    ],
    [
      "00bc2758",
      "READ",
      [
        "storage",
        "011265a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc274c",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2750",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2798"
      ]
    ],
    [
      "00bc2758",
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

- 旧版 [`00bc26d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc269c.md#insn-00bc26d8) · [`00bc26e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc269c.md#insn-00bc26e0) · [`00bc26f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc269c.md#insn-00bc26f4)

~~~diff
- 00bc26d8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc26d8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc26d8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5a0:8"]]
- 00bc26d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc26d8 bytes bf821639
- 00bc26e0 ["INT_ADD", "register:40f0:8", ["const:bc26e0:8", "const:4:8"]]
- 00bc26e0 ["CALL", null, ["callee:00c5b030:8"]]
- 00bc26e0 bytes 20620294
- 00bc26f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc26f4 ["INT_ADD", "register:40f0:8", ["const:bc26f4:8", "const:4:8"]]
- 00bc26f4 ["CALLIND", null, ["register:0:8"]]
- 00bc26f4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6be7d6476700302d9ff0bf1b9c402a68"></a>

### [`00bc270c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc270c.md) → [`00bc27a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc27a8.md) _ZN8firebase13remote_config8internal15config_settings14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
      "definition_site": "00bc27e8",
      "incomplete_value": true,
      "site": "00bc27e8",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc274c",
      "incomplete_value": true,
      "site": "00bc274c",
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
            "const:598:8"
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
      "definition_site": "00bc27c4",
      "incomplete_value": true,
      "site": "00bc27c4",
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
      "definition_site": "00bc2728",
      "incomplete_value": true,
      "site": "00bc2728",
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
      "definition_site": "00bc27cc",
      "incomplete_value": false,
      "site": "00bc27e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:bcc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2730",
      "incomplete_value": false,
      "site": "00bc2744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "00bc27bc",
      "READ",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc27cc",
      "PARAM",
      [
        "storage",
        "002b8c20",
        null,
        "string"
      ]
    ],
    [
      "00bc27e8",
      "WRITE",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc27bc",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc27cc",
      "PARAM",
      [
        "storage",
        "002b8bcc",
        null,
        "string"
      ]
    ],
    [
      "00bc27e8",
      "WRITE",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc270c.md#insn-00bc2744) · [`00bc274c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc270c.md#insn-00bc274c) · [`00bc2720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc270c.md#insn-00bc2720)
- 新版 [`00bc27e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc27a8.md#insn-00bc27e0) · [`00bc27e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc27a8.md#insn-00bc27e8) · [`00bc27bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc27a8.md#insn-00bc27bc)

~~~diff
- 00bc2744 ["INT_ADD", "register:40f0:8", ["const:bc2744:8", "const:4:8"]]
- 00bc2744 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc27e0 ["INT_ADD", "register:40f0:8", ["const:bc27e0:8", "const:4:8"]]
+ 00bc27e0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc2744 bytes f3610294
+ 00bc27e0 bytes 00620294
- 00bc274c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:598:8"]]
- 00bc274c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc27e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:698:8"]]
+ 00bc27e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc274c bytes 80ce02f9
+ 00bc27e8 bytes 804e03f9
- 00bc2720 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:598:8"]]
- 00bc2720 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc27bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:698:8"]]
+ 00bc27bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2720 bytes 81ce42f9
+ 00bc27bc bytes 814e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbba532534afcc5ef78954eb072fa4d4"></a>

### [`00bc277c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc277c.md) → [`00bc2818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2818.md) _ZN8firebase13remote_config8internal15config_settings11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00bc2834",
      "incomplete_value": false,
      "site": "00bc2838",
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
            "const:30b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2798",
      "incomplete_value": false,
      "site": "00bc279c",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc2844",
      "incomplete_value": true,
      "site": "00bc2850",
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
      "definition_site": "00bc27a8",
      "incomplete_value": true,
      "site": "00bc27b4",
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
      "00bc2834",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bc2844",
      "DATA",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2834",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bc2844",
      "DATA",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc279c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc277c.md#insn-00bc279c) · [`00bc2798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc277c.md#insn-00bc2798) · [`00bc27a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc277c.md#insn-00bc27a4)
- 新版 [`00bc2838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2818.md#insn-00bc2838) · [`00bc2834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2818.md#insn-00bc2834) · [`00bc2840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2818.md#insn-00bc2840)

~~~diff
- 00bc279c ["INT_ADD", "register:40f0:8", ["const:bc279c:8", "const:4:8"]]
- 00bc279c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bc2838 ["INT_ADD", "register:40f0:8", ["const:bc2838:8", "const:4:8"]]
+ 00bc2838 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bc279c bytes 19620294
+ 00bc2838 bytes 26620294
- 00bc2798 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00bc2798 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2798 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2798 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc2834 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bc2834 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2834 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2834 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc2798 bytes 009c0d91
+ 00bc2834 bytes 002c0c91
- 00bc27a4 ["COPY", "tmp:0:8", ["const:5a8:8"]]
- 00bc27a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc27a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc27a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc2840 ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 00bc2840 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc2840 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc2840 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc27a4 bytes 08a11691
+ 00bc2840 bytes 08a11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dae24a74f53ad956b9b3156be41a9487"></a>

### [`00bc27b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc27b8.md) → [`00bc2854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2854.md) _ZN8firebase13remote_config8internal15config_settings13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bc27f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2894"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc27d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc27cc",
      "READ",
      [
        "storage",
        "01126598",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc27d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2898"
      ]
    ],
    [
      "unmatched:00bc27dc",
      "PARAM",
      [
        "storage",
        "002b8c20",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2868",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2870",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2898"
      ]
    ],
    [
      "00bc2878",
      "PARAM",
      [
        "storage",
        "002b8bcc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc27d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc27b8.md#insn-00bc27d4) · [`00bc27f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc27b8.md#insn-00bc27f0) · [`00bc27f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc27b8.md#insn-00bc27f8)
- 新版 [`00bc288c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2854.md#insn-00bc288c)

~~~diff
- 00bc27d4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc27d4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc27d4 bytes 410100b5
- 00bc27f0 ["INT_ADD", "register:40f0:8", ["const:bc27f0:8", "const:4:8"]]
- 00bc27f0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc288c ["INT_ADD", "register:40f0:8", ["const:bc288c:8", "const:4:8"]]
+ 00bc288c ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc27f0 bytes c8610294
+ 00bc288c bytes d5610294
- 00bc27f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:598:8"]]
- 00bc27f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc27f8 bytes 80ce02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8a75800e211cf77a5a061f996f035ff"></a>

### [`00bc2828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2828.md) → [`00bc28c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc28c4.md) _ZN8firebase13remote_config8internal15config_settings10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00bc28e0",
      "incomplete_value": false,
      "site": "00bc28e4",
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
            "const:54d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2844",
      "incomplete_value": false,
      "site": "00bc2848",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc28f0",
      "incomplete_value": true,
      "site": "00bc28fc",
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
      "definition_site": "00bc2854",
      "incomplete_value": true,
      "site": "00bc2860",
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
      "00bc28e0",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bc28f0",
      "DATA",
      [
        "storage",
        "011265b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc28e0",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bc28f0",
      "DATA",
      [
        "storage",
        "011266b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2828.md#insn-00bc2848) · [`00bc2844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2828.md#insn-00bc2844) · [`00bc2850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2828.md#insn-00bc2850)
- 新版 [`00bc28e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc28c4.md#insn-00bc28e4) · [`00bc28e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc28c4.md#insn-00bc28e0) · [`00bc28ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc28c4.md#insn-00bc28ec)

~~~diff
- 00bc2848 ["INT_ADD", "register:40f0:8", ["const:bc2848:8", "const:4:8"]]
- 00bc2848 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bc28e4 ["INT_ADD", "register:40f0:8", ["const:bc28e4:8", "const:4:8"]]
+ 00bc28e4 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bc2848 bytes ee610294
+ 00bc28e4 bytes fb610294
- 00bc2844 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00bc2844 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2844 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2844 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc28e0 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bc28e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc28e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc28e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc2844 bytes 00781491
+ 00bc28e0 bytes 00341591
- 00bc2850 ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 00bc2850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc28ec ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00bc28ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc28ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc28ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc2850 bytes 08e11691
+ 00bc28ec bytes 08e11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77763ada33a7710213c86c26875bf6a0"></a>

### [`00bc2864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2864.md) → [`00bc2900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2900.md) _ZN8firebase13remote_config8internal23config_settings_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embe

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bc2890"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc292c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc2914",
      "incomplete_value": true,
      "site": "00bc2914",
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
      "definition_site": "00bc2878",
      "incomplete_value": true,
      "site": "00bc2878",
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
      "00bc2910",
      "READ",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2914",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc2894"
      ]
    ],
    [
      "unmatched:00bc2884",
      "PARAM",
      [
        "storage",
        "002b9bde",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2910",
      "READ",
      [
        "storage",
        "011266c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2914",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2930"
      ]
    ],
    [
      "00bc2920",
      "PARAM",
      [
        "storage",
        "002b9b8a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2864.md#insn-00bc2888) · [`00bc2890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2864.md#insn-00bc2890) · [`00bc28a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2864.md#insn-00bc28a0)

~~~diff
- 00bc2888 ["INT_ADD", "register:40f0:8", ["const:bc2888:8", "const:4:8"]]
- 00bc2888 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc2888 bytes a2610294
- 00bc2890 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00bc2890 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2890 bytes 60e202f9
- 00bc28a0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bc28a0 ["RETURN", null, ["register:0:8"]]
- 00bc28a0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d775b64d2421068d621c60298d79ff9c"></a>

### [`00bc28a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc28a4.md) → [`00bc2940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2940.md) _ZN8firebase13remote_config8internal23config_settings_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embe

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc296c",
      "incomplete_value": true,
      "site": "00bc296c",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc28d0",
      "incomplete_value": true,
      "site": "00bc28d0",
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
            "const:5c0:8"
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
      "definition_site": "00bc2954",
      "incomplete_value": true,
      "site": "00bc2954",
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
      "definition_site": "00bc28b8",
      "incomplete_value": true,
      "site": "00bc28b8",
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
      "definition_site": "00bc295c",
      "incomplete_value": false,
      "site": "00bc2964",
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
            "const:b8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc28c0",
      "incomplete_value": false,
      "site": "00bc28c8",
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
            "const:bde:8"
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
      "00bc2950",
      "READ",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc295c",
      "PARAM",
      [
        "storage",
        "002b9bde",
        null,
        "string"
      ]
    ],
    [
      "00bc296c",
      "WRITE",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2950",
      "READ",
      [
        "storage",
        "011266c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc295c",
      "PARAM",
      [
        "storage",
        "002b9b8a",
        null,
        "string"
      ]
    ],
    [
      "00bc296c",
      "WRITE",
      [
        "storage",
        "011266c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc28c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc28a4.md#insn-00bc28c8) · [`00bc28d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc28a4.md#insn-00bc28d0) · [`00bc28b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc28a4.md#insn-00bc28b4)
- 新版 [`00bc2964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2940.md#insn-00bc2964) · [`00bc296c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2940.md#insn-00bc296c) · [`00bc2950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2940.md#insn-00bc2950)

~~~diff
- 00bc28c8 ["INT_ADD", "register:40f0:8", ["const:bc28c8:8", "const:4:8"]]
- 00bc28c8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc2964 ["INT_ADD", "register:40f0:8", ["const:bc2964:8", "const:4:8"]]
+ 00bc2964 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc28c8 bytes 92610294
+ 00bc2964 bytes 9f610294
- 00bc28d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00bc28d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc296c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00bc296c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc28d0 bytes 60e202f9
+ 00bc296c bytes 606203f9
- 00bc28b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00bc28b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2950 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00bc2950 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc28b4 bytes 68e242f9
+ 00bc2950 bytes 686243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a883fc50a92a06c6711546837b5e665"></a>

### [`00bc28e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc28e4.md) → [`00bc2980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2980.md) _ZN8firebase13remote_config8internal23config_settings_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc29b0",
      "incomplete_value": true,
      "site": "00bc29b0",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2914",
      "incomplete_value": true,
      "site": "00bc2914",
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
            "const:5c0:8"
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
      "definition_site": "00bc2994",
      "incomplete_value": true,
      "site": "00bc2994",
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
      "definition_site": "00bc28f8",
      "incomplete_value": true,
      "site": "00bc28f8",
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
      "definition_site": "00bc29a0",
      "incomplete_value": false,
      "site": "00bc29a8",
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
            "const:b8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2904",
      "incomplete_value": false,
      "site": "00bc290c",
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
            "const:bde:8"
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
      "00bc2990",
      "READ",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc29a0",
      "PARAM",
      [
        "storage",
        "002b9bde",
        null,
        "string"
      ]
    ],
    [
      "00bc29b0",
      "WRITE",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2990",
      "READ",
      [
        "storage",
        "011266c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc29a0",
      "PARAM",
      [
        "storage",
        "002b9b8a",
        null,
        "string"
      ]
    ],
    [
      "00bc29b0",
      "WRITE",
      [
        "storage",
        "011266c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc290c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc28e4.md#insn-00bc290c) · [`00bc2914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc28e4.md#insn-00bc2914) · [`00bc28f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc28e4.md#insn-00bc28f4)
- 新版 [`00bc29a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2980.md#insn-00bc29a8) · [`00bc29b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2980.md#insn-00bc29b0) · [`00bc2990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2980.md#insn-00bc2990)

~~~diff
- 00bc290c ["INT_ADD", "register:40f0:8", ["const:bc290c:8", "const:4:8"]]
- 00bc290c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc29a8 ["INT_ADD", "register:40f0:8", ["const:bc29a8:8", "const:4:8"]]
+ 00bc29a8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc290c bytes 81610294
+ 00bc29a8 bytes 8e610294
- 00bc2914 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00bc2914 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc29b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00bc29b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2914 bytes 60e202f9
+ 00bc29b0 bytes 606203f9
- 00bc28f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00bc28f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2990 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00bc2990 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc28f4 bytes 68e242f9
+ 00bc2990 bytes 686243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bbfd1ccf8cf7d8254940e7ec896ce27"></a>

### [`00bc2928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2928.md) → [`00bc29c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc29c4.md) _ZN8firebase13remote_config8internal23config_settings_builder10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2928"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc292c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc292c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc2928",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc292c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc29d4",
      "READ",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc29c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc29c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc29d4",
      "READ",
      [
        "storage",
        "011266c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2928.md#insn-00bc2928) · [`00bc292c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2928.md#insn-00bc292c) · [`00bc293c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2928.md#insn-00bc293c)
- 新版 [`00bc29d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc29c4.md#insn-00bc29d8)

~~~diff
- 00bc2928 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc2928 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc2928 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc2928 bytes f30f1ef8
- 00bc292c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc292c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc292c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc292c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc292c bytes fd7b01a9
- 00bc293c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc293c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bc29d8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc29d8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bc293c bytes 080100b5
+ 00bc29d8 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ebb2605d76c1539ea67c8e0a6c8417f"></a>

### [`00bc2978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2978.md) → [`00bc2a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2a14.md) _ZN8firebase13remote_config8internal23config_settings_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "definition_site": "00bc2a6c",
      "incomplete_value": true,
      "site": "00bc2a6c",
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
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc29d0",
      "incomplete_value": true,
      "site": "00bc29d0",
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
            "const:5c8:8"
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
      "definition_site": "00bc2a48",
      "incomplete_value": true,
      "site": "00bc2a54",
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
                "const:6c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc29ac",
      "incomplete_value": true,
      "site": "00bc29b8",
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
                "const:5c0:8"
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
      "00bc2a28",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2a48",
      "READ",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2a6c",
      "WRITE",
      [
        "storage",
        "011265c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc2a28",
      "READ",
      [
        "storage",
        "011266c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2a48",
      "READ",
      [
        "storage",
        "011266c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2a6c",
      "WRITE",
      [
        "storage",
        "011266c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc29b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2978.md#insn-00bc29b8) · [`00bc29d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2978.md#insn-00bc29d0) · [`00bc298c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2978.md#insn-00bc298c)
- 新版 [`00bc2a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2a14.md#insn-00bc2a54) · [`00bc2a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2a14.md#insn-00bc2a6c) · [`00bc2a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2a14.md#insn-00bc2a28)

~~~diff
- 00bc29b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc29b8 ["INT_ADD", "register:40f0:8", ["const:bc29b8:8", "const:4:8"]]
- 00bc29b8 ["CALLIND", null, ["register:0:8"]]
+ 00bc2a54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2a54 ["INT_ADD", "register:40f0:8", ["const:bc2a54:8", "const:4:8"]]
+ 00bc2a54 ["CALLIND", null, ["register:0:8"]]
- 00bc29b8 bytes 00013fd6
+ 00bc2a54 bytes 00013fd6
- 00bc29d0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bc29d0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5c8:8"]]
- 00bc29d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc2a6c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc2a6c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6c8:8"]]
+ 00bc2a6c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc29d0 bytes a0221739
+ 00bc2a6c bytes a0221b39
- 00bc298c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5c8:8"]]
- 00bc298c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bc298c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bc2a28 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6c8:8"]]
+ 00bc2a28 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2a28 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bc298c bytes a8225739
+ 00bc2a28 bytes a8225b39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f1b494fabc0935e51d313c1802c0ca5"></a>

### [`00bc29e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc29e4.md) → [`00bc2a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2a80.md) _ZN8firebase13remote_config8internal23config_settings_builder12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "definition_site": "00bc2abc",
      "incomplete_value": true,
      "site": "00bc2abc",
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
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2a20",
      "incomplete_value": true,
      "site": "00bc2a20",
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
            "const:5c8:8"
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
      "definition_site": "00bc2adc",
      "incomplete_value": true,
      "site": "00bc2adc",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2a40",
      "incomplete_value": true,
      "site": "00bc2a40",
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
            "const:5c0:8"
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
      "definition_site": "00bc2a98",
      "incomplete_value": true,
      "site": "00bc2a98",
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
      "definition_site": "00bc29fc",
      "incomplete_value": true,
      "site": "00bc29fc",
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
      "00bc2a94",
      "READ",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2aa0",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2abc",
      "WRITE",
      [
        "storage",
        "011265c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc2a94",
      "READ",
      [
        "storage",
        "011266c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2aa0",
      "READ",
      [
        "storage",
        "011266c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2abc",
      "WRITE",
      [
        "storage",
        "011266c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc29e4.md#insn-00bc2a20) · [`00bc2a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc29e4.md#insn-00bc2a3c) · [`00bc2a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc29e4.md#insn-00bc2a40)
- 新版 [`00bc2abc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2a80.md#insn-00bc2abc) · [`00bc2ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2a80.md#insn-00bc2ad8) · [`00bc2adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2a80.md#insn-00bc2adc)

~~~diff
- 00bc2a20 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc2a20 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc2a20 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5c8:8"]]
- 00bc2a20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bc2abc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bc2abc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bc2abc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6c8:8"]]
+ 00bc2abc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc2a20 bytes bf221739
+ 00bc2abc bytes bf221b39
- 00bc2a3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc2a3c ["INT_ADD", "register:40f0:8", ["const:bc2a3c:8", "const:4:8"]]
- 00bc2a3c ["CALLIND", null, ["register:0:8"]]
+ 00bc2ad8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2ad8 ["INT_ADD", "register:40f0:8", ["const:bc2ad8:8", "const:4:8"]]
+ 00bc2ad8 ["CALLIND", null, ["register:0:8"]]
- 00bc2a3c bytes 00013fd6
+ 00bc2ad8 bytes 00013fd6
- 00bc2a40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00bc2a40 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bc2a40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bc2adc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00bc2adc ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bc2adc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bc2a40 bytes 9fe202f9
+ 00bc2adc bytes 9f6203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ac8f0fcb17fbec3d14bc9b2361913a1"></a>

### [`00bc2a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2a54.md) → [`00bc2af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2af0.md) _ZN8firebase13remote_config8internal23config_settings_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bc2a94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2b30"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2a70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc2a68",
      "READ",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc2a70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2b34"
      ]
    ],
    [
      "unmatched:00bc2a78",
      "PARAM",
      [
        "storage",
        "002b9bde",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2b04",
      "READ",
      [
        "storage",
        "011266c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2b0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2b34"
      ]
    ],
    [
      "00bc2b14",
      "PARAM",
      [
        "storage",
        "002b9b8a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2a54.md#insn-00bc2a70) · [`00bc2a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2a54.md#insn-00bc2a8c) · [`00bc2a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2a54.md#insn-00bc2a94)
- 新版 [`00bc2b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2af0.md#insn-00bc2b28)

~~~diff
- 00bc2a70 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc2a70 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc2a70 bytes 410100b5
- 00bc2a8c ["INT_ADD", "register:40f0:8", ["const:bc2a8c:8", "const:4:8"]]
- 00bc2a8c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc2b28 ["INT_ADD", "register:40f0:8", ["const:bc2b28:8", "const:4:8"]]
+ 00bc2b28 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc2a8c bytes 21610294
+ 00bc2b28 bytes 2e610294
- 00bc2a94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00bc2a94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2a94 bytes 80e202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dd33770d1b2e20f1a05712f9279cd32"></a>

### [`00bc2ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2ac4.md) → [`00bc2b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2b60.md) _ZN8firebase13remote_config8internal23config_settings_builder11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00bc2b7c",
      "incomplete_value": false,
      "site": "00bc2b80",
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
            "const:30b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2ae0",
      "incomplete_value": false,
      "site": "00bc2ae4",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc2b8c",
      "incomplete_value": true,
      "site": "00bc2b98",
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
      "definition_site": "00bc2af0",
      "incomplete_value": true,
      "site": "00bc2afc",
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
      "00bc2b7c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bc2b8c",
      "DATA",
      [
        "storage",
        "011265d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2b7c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bc2b8c",
      "DATA",
      [
        "storage",
        "011266d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2ac4.md#insn-00bc2ae4) · [`00bc2ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2ac4.md#insn-00bc2ae0) · [`00bc2aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2ac4.md#insn-00bc2aec)
- 新版 [`00bc2b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2b60.md#insn-00bc2b80) · [`00bc2b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2b60.md#insn-00bc2b7c) · [`00bc2b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2b60.md#insn-00bc2b88)

~~~diff
- 00bc2ae4 ["INT_ADD", "register:40f0:8", ["const:bc2ae4:8", "const:4:8"]]
- 00bc2ae4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bc2b80 ["INT_ADD", "register:40f0:8", ["const:bc2b80:8", "const:4:8"]]
+ 00bc2b80 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bc2ae4 bytes 47610294
+ 00bc2b80 bytes 54610294
- 00bc2ae0 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00bc2ae0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2ae0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2ae0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc2b7c ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bc2b7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2b7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2b7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc2ae0 bytes 009c0d91
+ 00bc2b7c bytes 002c0c91
- 00bc2aec ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 00bc2aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc2b88 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 00bc2b88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc2b88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc2b88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc2aec bytes 08411791
+ 00bc2b88 bytes 08411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2eb1612ad6c8a9b52398c5d1cf7d6694"></a>

### [`00bc2b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2b00.md) → [`00bc2b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2b9c.md) _ZN8firebase13remote_config8internal23config_settings_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bc2b40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc2bdc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2b1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc2b14",
      "READ",
      [
        "storage",
        "011265c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc2b1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2be0"
      ]
    ],
    [
      "unmatched:00bc2b24",
      "PARAM",
      [
        "storage",
        "002b9bde",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2bb0",
      "READ",
      [
        "storage",
        "011266c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2bb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc2be0"
      ]
    ],
    [
      "00bc2bc0",
      "PARAM",
      [
        "storage",
        "002b9b8a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2b00.md#insn-00bc2b1c) · [`00bc2b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2b00.md#insn-00bc2b38) · [`00bc2b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2b00.md#insn-00bc2b40)
- 新版 [`00bc2bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2b9c.md#insn-00bc2bd4)

~~~diff
- 00bc2b1c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc2b1c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc2b1c bytes 410100b5
- 00bc2b38 ["INT_ADD", "register:40f0:8", ["const:bc2b38:8", "const:4:8"]]
- 00bc2b38 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc2bd4 ["INT_ADD", "register:40f0:8", ["const:bc2bd4:8", "const:4:8"]]
+ 00bc2bd4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc2b38 bytes f6600294
+ 00bc2bd4 bytes 03610294
- 00bc2b40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00bc2b40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2b40 bytes 80e202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff04a6135aec3abe84844702b1d79b25"></a>

### [`00bc2bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2bac.md) → [`00bc2c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2c48.md) _ZN8firebase13remote_config8internal22custom_signals_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embed

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

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
      "site": "00bc2bac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2bb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2bb0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc2bac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc2bb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc2c58",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2c48",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc2c4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc2c58",
      "READ",
      [
        "storage",
        "011266f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2bac.md#insn-00bc2bac) · [`00bc2bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2bac.md#insn-00bc2bb0) · [`00bc2bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2bac.md#insn-00bc2bc0)
- 新版 [`00bc2c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2c48.md#insn-00bc2c5c)

~~~diff
- 00bc2bac ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc2bac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc2bac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc2bac bytes f30f1ef8
- 00bc2bb0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc2bb0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc2bb0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc2bb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc2bb0 bytes fd7b01a9
- 00bc2bc0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc2bc0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bc2c5c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc2c5c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc2bc0 bytes e80000b5
+ 00bc2c5c bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c20f61230394ebc5c443701591e8187"></a>

### [`00bc2bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2bec.md) → [`00bc2c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2c88.md) _ZN8firebase13remote_config8internal22custom_signals_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embed

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc2cb4",
      "incomplete_value": true,
      "site": "00bc2cb4",
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
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2c18",
      "incomplete_value": true,
      "site": "00bc2c18",
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
            "const:5f8:8"
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
      "definition_site": "00bc2c9c",
      "incomplete_value": true,
      "site": "00bc2c9c",
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
      "definition_site": "00bc2c00",
      "incomplete_value": true,
      "site": "00bc2c00",
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
      "definition_site": "00bc2ca4",
      "incomplete_value": false,
      "site": "00bc2cac",
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
            "const:38f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2c08",
      "incomplete_value": false,
      "site": "00bc2c10",
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
            "const:3eb:8"
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
      "00bc2c98",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2ca4",
      "PARAM",
      [
        "storage",
        "002ae3eb",
        null,
        "string"
      ]
    ],
    [
      "00bc2cb4",
      "WRITE",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2c98",
      "READ",
      [
        "storage",
        "011266f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2ca4",
      "PARAM",
      [
        "storage",
        "002ae38f",
        null,
        "string"
      ]
    ],
    [
      "00bc2cb4",
      "WRITE",
      [
        "storage",
        "011266f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2bec.md#insn-00bc2c10) · [`00bc2c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2bec.md#insn-00bc2c18) · [`00bc2bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2bec.md#insn-00bc2bfc)
- 新版 [`00bc2cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2c88.md#insn-00bc2cac) · [`00bc2cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2c88.md#insn-00bc2cb4) · [`00bc2c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2c88.md#insn-00bc2c98)

~~~diff
- 00bc2c10 ["INT_ADD", "register:40f0:8", ["const:bc2c10:8", "const:4:8"]]
- 00bc2c10 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc2cac ["INT_ADD", "register:40f0:8", ["const:bc2cac:8", "const:4:8"]]
+ 00bc2cac ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc2c10 bytes c0600294
+ 00bc2cac bytes cd600294
- 00bc2c18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5f8:8"]]
- 00bc2c18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2cb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6f8:8"]]
+ 00bc2cb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2c18 bytes 60fe02f9
+ 00bc2cb4 bytes 607e03f9
- 00bc2bfc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5f8:8"]]
- 00bc2bfc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2c98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6f8:8"]]
+ 00bc2c98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2bfc bytes 68fe42f9
+ 00bc2c98 bytes 687e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0ef36195600e3c19c2a3c5af0cdd56e"></a>

### [`00bc2c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2c2c.md) → [`00bc2cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2cc8.md) _ZN8firebase13remote_config8internal22custom_signals_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc2cf8",
      "incomplete_value": true,
      "site": "00bc2cf8",
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
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2c5c",
      "incomplete_value": true,
      "site": "00bc2c5c",
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
            "const:5f8:8"
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
      "definition_site": "00bc2cdc",
      "incomplete_value": true,
      "site": "00bc2cdc",
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
      "definition_site": "00bc2c40",
      "incomplete_value": true,
      "site": "00bc2c40",
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
      "definition_site": "00bc2ce8",
      "incomplete_value": false,
      "site": "00bc2cf0",
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
            "const:38f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2c4c",
      "incomplete_value": false,
      "site": "00bc2c54",
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
            "const:3eb:8"
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
      "00bc2cd8",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2ce8",
      "PARAM",
      [
        "storage",
        "002ae3eb",
        null,
        "string"
      ]
    ],
    [
      "00bc2cf8",
      "WRITE",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2cd8",
      "READ",
      [
        "storage",
        "011266f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2ce8",
      "PARAM",
      [
        "storage",
        "002ae38f",
        null,
        "string"
      ]
    ],
    [
      "00bc2cf8",
      "WRITE",
      [
        "storage",
        "011266f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2c2c.md#insn-00bc2c54) · [`00bc2c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2c2c.md#insn-00bc2c5c) · [`00bc2c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2c2c.md#insn-00bc2c3c)
- 新版 [`00bc2cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2cc8.md#insn-00bc2cf0) · [`00bc2cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2cc8.md#insn-00bc2cf8) · [`00bc2cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2cc8.md#insn-00bc2cd8)

~~~diff
- 00bc2c54 ["INT_ADD", "register:40f0:8", ["const:bc2c54:8", "const:4:8"]]
- 00bc2c54 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc2cf0 ["INT_ADD", "register:40f0:8", ["const:bc2cf0:8", "const:4:8"]]
+ 00bc2cf0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc2c54 bytes af600294
+ 00bc2cf0 bytes bc600294
- 00bc2c5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5f8:8"]]
- 00bc2c5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2cf8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6f8:8"]]
+ 00bc2cf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2c5c bytes 60fe02f9
+ 00bc2cf8 bytes 607e03f9
- 00bc2c3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5f8:8"]]
- 00bc2c3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2cd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6f8:8"]]
+ 00bc2cd8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2c3c bytes 68fe42f9
+ 00bc2cd8 bytes 687e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26b875439f0dc6f670f15b224bafb2d9"></a>

### [`00bc2c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2c70.md) → [`00bc2d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2d0c.md) _ZN8firebase13remote_config8internal22custom_signals_builder10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc2d3c",
      "incomplete_value": true,
      "site": "00bc2d3c",
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
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2ca0",
      "incomplete_value": true,
      "site": "00bc2ca0",
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
            "const:5f8:8"
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
      "definition_site": "00bc2d20",
      "incomplete_value": true,
      "site": "00bc2d20",
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
      "definition_site": "00bc2c84",
      "incomplete_value": true,
      "site": "00bc2c84",
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
      "definition_site": "00bc2d28",
      "incomplete_value": false,
      "site": "00bc2d34",
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
            "const:38f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2c8c",
      "incomplete_value": false,
      "site": "00bc2c98",
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
            "const:3eb:8"
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
      "00bc2d1c",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2d28",
      "PARAM",
      [
        "storage",
        "002ae3eb",
        null,
        "string"
      ]
    ],
    [
      "00bc2d3c",
      "WRITE",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2d1c",
      "READ",
      [
        "storage",
        "011266f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2d28",
      "PARAM",
      [
        "storage",
        "002ae38f",
        null,
        "string"
      ]
    ],
    [
      "00bc2d3c",
      "WRITE",
      [
        "storage",
        "011266f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2c70.md#insn-00bc2c98) · [`00bc2ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2c70.md#insn-00bc2ca0) · [`00bc2c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2c70.md#insn-00bc2c80)
- 新版 [`00bc2d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2d0c.md#insn-00bc2d34) · [`00bc2d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2d0c.md#insn-00bc2d3c) · [`00bc2d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2d0c.md#insn-00bc2d1c)

~~~diff
- 00bc2c98 ["INT_ADD", "register:40f0:8", ["const:bc2c98:8", "const:4:8"]]
- 00bc2c98 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc2d34 ["INT_ADD", "register:40f0:8", ["const:bc2d34:8", "const:4:8"]]
+ 00bc2d34 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc2c98 bytes 9e600294
+ 00bc2d34 bytes ab600294
- 00bc2ca0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5f8:8"]]
- 00bc2ca0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2d3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6f8:8"]]
+ 00bc2d3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2ca0 bytes 60fe02f9
+ 00bc2d3c bytes 607e03f9
- 00bc2c80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5f8:8"]]
- 00bc2c80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2d1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6f8:8"]]
+ 00bc2d1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2c80 bytes 68fe42f9
+ 00bc2d1c bytes 687e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f093b95f76a4e82af1bcd9b9e828d35"></a>

### [`00bc2cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2cc0.md) → [`00bc2d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2d5c.md) _ZN8firebase13remote_config8internal22custom_signals_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "definition_site": "00bc2db4",
      "incomplete_value": true,
      "site": "00bc2db4",
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
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2d18",
      "incomplete_value": true,
      "site": "00bc2d18",
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
            "const:600:8"
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
      "definition_site": "00bc2d90",
      "incomplete_value": true,
      "site": "00bc2d9c",
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
                "const:6f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2cf4",
      "incomplete_value": true,
      "site": "00bc2d00",
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
                "const:5f8:8"
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
      "00bc2d70",
      "READ",
      [
        "storage",
        "01126600",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2d90",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2db4",
      "WRITE",
      [
        "storage",
        "01126600",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc2d70",
      "READ",
      [
        "storage",
        "01126700",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2d90",
      "READ",
      [
        "storage",
        "011266f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2db4",
      "WRITE",
      [
        "storage",
        "01126700",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2cc0.md#insn-00bc2d00) · [`00bc2d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2cc0.md#insn-00bc2d18) · [`00bc2cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2cc0.md#insn-00bc2cd4)
- 新版 [`00bc2d9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2d5c.md#insn-00bc2d9c) · [`00bc2db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2d5c.md#insn-00bc2db4) · [`00bc2d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2d5c.md#insn-00bc2d70)

~~~diff
- 00bc2d00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc2d00 ["INT_ADD", "register:40f0:8", ["const:bc2d00:8", "const:4:8"]]
- 00bc2d00 ["CALLIND", null, ["register:0:8"]]
+ 00bc2d9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2d9c ["INT_ADD", "register:40f0:8", ["const:bc2d9c:8", "const:4:8"]]
+ 00bc2d9c ["CALLIND", null, ["register:0:8"]]
- 00bc2d00 bytes 00013fd6
+ 00bc2d9c bytes 00013fd6
- 00bc2d18 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bc2d18 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:600:8"]]
- 00bc2d18 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc2db4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc2db4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:700:8"]]
+ 00bc2db4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc2d18 bytes a0021839
+ 00bc2db4 bytes a0021c39
- 00bc2cd4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:600:8"]]
- 00bc2cd4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bc2cd4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bc2d70 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:700:8"]]
+ 00bc2d70 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2d70 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bc2cd4 bytes a8025839
+ 00bc2d70 bytes a8025c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee4b3e3c8cfcf64fa424bb2f33bd9b19"></a>

### [`00bc2d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2d2c.md) → [`00bc2dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2dc8.md) _ZN8firebase13remote_config8internal22custom_signals_builder12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "definition_site": "00bc2e04",
      "incomplete_value": true,
      "site": "00bc2e04",
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
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2d68",
      "incomplete_value": true,
      "site": "00bc2d68",
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
            "const:600:8"
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
      "definition_site": "00bc2e24",
      "incomplete_value": true,
      "site": "00bc2e24",
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
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2d88",
      "incomplete_value": true,
      "site": "00bc2d88",
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
            "const:5f8:8"
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
      "definition_site": "00bc2de0",
      "incomplete_value": true,
      "site": "00bc2de0",
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
      "definition_site": "00bc2d44",
      "incomplete_value": true,
      "site": "00bc2d44",
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
      "00bc2ddc",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2de8",
      "READ",
      [
        "storage",
        "01126600",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2e04",
      "WRITE",
      [
        "storage",
        "01126600",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc2ddc",
      "READ",
      [
        "storage",
        "011266f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2de8",
      "READ",
      [
        "storage",
        "01126700",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2e04",
      "WRITE",
      [
        "storage",
        "01126700",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2d2c.md#insn-00bc2d68) · [`00bc2d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2d2c.md#insn-00bc2d84) · [`00bc2d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2d2c.md#insn-00bc2d88)
- 新版 [`00bc2e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2dc8.md#insn-00bc2e04) · [`00bc2e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2dc8.md#insn-00bc2e20) · [`00bc2e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2dc8.md#insn-00bc2e24)

~~~diff
- 00bc2d68 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc2d68 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc2d68 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:600:8"]]
- 00bc2d68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bc2e04 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bc2e04 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bc2e04 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:700:8"]]
+ 00bc2e04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc2d68 bytes bf021839
+ 00bc2e04 bytes bf021c39
- 00bc2d84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc2d84 ["INT_ADD", "register:40f0:8", ["const:bc2d84:8", "const:4:8"]]
- 00bc2d84 ["CALLIND", null, ["register:0:8"]]
+ 00bc2e20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2e20 ["INT_ADD", "register:40f0:8", ["const:bc2e20:8", "const:4:8"]]
+ 00bc2e20 ["CALLIND", null, ["register:0:8"]]
- 00bc2d84 bytes 00013fd6
+ 00bc2e20 bytes 00013fd6
- 00bc2d88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5f8:8"]]
- 00bc2d88 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bc2d88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bc2e24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6f8:8"]]
+ 00bc2e24 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bc2e24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bc2d88 bytes 9ffe02f9
+ 00bc2e24 bytes 9f7e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c505fcb9ebfe9128d9b60903ae40c18"></a>

### [`00bc2d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2d9c.md) → [`00bc2e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2e38.md) _ZN8firebase13remote_config8internal22custom_signals_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
      "definition_site": "00bc2e78",
      "incomplete_value": true,
      "site": "00bc2e78",
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
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2ddc",
      "incomplete_value": true,
      "site": "00bc2ddc",
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
            "const:5f8:8"
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
      "definition_site": "00bc2e54",
      "incomplete_value": true,
      "site": "00bc2e54",
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
      "definition_site": "00bc2db8",
      "incomplete_value": true,
      "site": "00bc2db8",
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
      "definition_site": "00bc2e5c",
      "incomplete_value": false,
      "site": "00bc2e70",
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
            "const:38f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2dc0",
      "incomplete_value": false,
      "site": "00bc2dd4",
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
            "const:3eb:8"
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
      "00bc2e4c",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2e5c",
      "PARAM",
      [
        "storage",
        "002ae3eb",
        null,
        "string"
      ]
    ],
    [
      "00bc2e78",
      "WRITE",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2e4c",
      "READ",
      [
        "storage",
        "011266f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2e5c",
      "PARAM",
      [
        "storage",
        "002ae38f",
        null,
        "string"
      ]
    ],
    [
      "00bc2e78",
      "WRITE",
      [
        "storage",
        "011266f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2d9c.md#insn-00bc2dd4) · [`00bc2ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2d9c.md#insn-00bc2ddc) · [`00bc2db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2d9c.md#insn-00bc2db0)
- 新版 [`00bc2e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2e38.md#insn-00bc2e70) · [`00bc2e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2e38.md#insn-00bc2e78) · [`00bc2e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2e38.md#insn-00bc2e4c)

~~~diff
- 00bc2dd4 ["INT_ADD", "register:40f0:8", ["const:bc2dd4:8", "const:4:8"]]
- 00bc2dd4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc2e70 ["INT_ADD", "register:40f0:8", ["const:bc2e70:8", "const:4:8"]]
+ 00bc2e70 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc2dd4 bytes 4f600294
+ 00bc2e70 bytes 5c600294
- 00bc2ddc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5f8:8"]]
- 00bc2ddc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2e78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6f8:8"]]
+ 00bc2e78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2ddc bytes 80fe02f9
+ 00bc2e78 bytes 807e03f9
- 00bc2db0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5f8:8"]]
- 00bc2db0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2e4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6f8:8"]]
+ 00bc2e4c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2db0 bytes 81fe42f9
+ 00bc2e4c bytes 817e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dde790c354b061625acc7619de4fba3"></a>

### [`00bc2e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2e0c.md) → [`00bc2ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2ea8.md) _ZN8firebase13remote_config8internal22custom_signals_builder11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00bc2ec4",
      "incomplete_value": false,
      "site": "00bc2ec8",
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
            "const:30b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2e28",
      "incomplete_value": false,
      "site": "00bc2e2c",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc2ed4",
      "incomplete_value": true,
      "site": "00bc2ee0",
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
      "definition_site": "00bc2e38",
      "incomplete_value": true,
      "site": "00bc2e44",
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
      "00bc2ec4",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bc2ed4",
      "DATA",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2ec4",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bc2ed4",
      "DATA",
      [
        "storage",
        "01126708",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2e0c.md#insn-00bc2e2c) · [`00bc2e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2e0c.md#insn-00bc2e28) · [`00bc2e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2e0c.md#insn-00bc2e34)
- 新版 [`00bc2ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2ea8.md#insn-00bc2ec8) · [`00bc2ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2ea8.md#insn-00bc2ec4) · [`00bc2ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2ea8.md#insn-00bc2ed0)

~~~diff
- 00bc2e2c ["INT_ADD", "register:40f0:8", ["const:bc2e2c:8", "const:4:8"]]
- 00bc2e2c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bc2ec8 ["INT_ADD", "register:40f0:8", ["const:bc2ec8:8", "const:4:8"]]
+ 00bc2ec8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bc2e2c bytes 75600294
+ 00bc2ec8 bytes 82600294
- 00bc2e28 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00bc2e28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2e28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc2e28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc2ec4 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bc2ec4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2ec4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2ec4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc2e28 bytes 009c0d91
+ 00bc2ec4 bytes 002c0c91
- 00bc2e34 ["COPY", "tmp:0:8", ["const:608:8"]]
- 00bc2e34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2e34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2e34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc2ed0 ["COPY", "tmp:0:8", ["const:708:8"]]
+ 00bc2ed0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc2ed0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc2ed0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc2e34 bytes 08211891
+ 00bc2ed0 bytes 08211c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2275c27693228f0040085c5722e7f8a"></a>

### [`00bc2e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2e48.md) → [`00bc2ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2ee4.md) _ZN8firebase13remote_config8internal22custom_signals_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc2f24",
      "incomplete_value": true,
      "site": "00bc2f24",
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
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2e88",
      "incomplete_value": true,
      "site": "00bc2e88",
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
            "const:5f8:8"
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
      "definition_site": "00bc2f00",
      "incomplete_value": true,
      "site": "00bc2f00",
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
      "definition_site": "00bc2e64",
      "incomplete_value": true,
      "site": "00bc2e64",
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
      "definition_site": "00bc2f08",
      "incomplete_value": false,
      "site": "00bc2f1c",
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
            "const:38f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2e6c",
      "incomplete_value": false,
      "site": "00bc2e80",
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
            "const:3eb:8"
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
      "00bc2ef8",
      "READ",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2f08",
      "PARAM",
      [
        "storage",
        "002ae3eb",
        null,
        "string"
      ]
    ],
    [
      "00bc2f24",
      "WRITE",
      [
        "storage",
        "011265f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2ef8",
      "READ",
      [
        "storage",
        "011266f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2f08",
      "PARAM",
      [
        "storage",
        "002ae38f",
        null,
        "string"
      ]
    ],
    [
      "00bc2f24",
      "WRITE",
      [
        "storage",
        "011266f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2e48.md#insn-00bc2e80) · [`00bc2e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2e48.md#insn-00bc2e88) · [`00bc2e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2e48.md#insn-00bc2e5c)
- 新版 [`00bc2f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2ee4.md#insn-00bc2f1c) · [`00bc2f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2ee4.md#insn-00bc2f24) · [`00bc2ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2ee4.md#insn-00bc2ef8)

~~~diff
- 00bc2e80 ["INT_ADD", "register:40f0:8", ["const:bc2e80:8", "const:4:8"]]
- 00bc2e80 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc2f1c ["INT_ADD", "register:40f0:8", ["const:bc2f1c:8", "const:4:8"]]
+ 00bc2f1c ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc2e80 bytes 24600294
+ 00bc2f1c bytes 31600294
- 00bc2e88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5f8:8"]]
- 00bc2e88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2f24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6f8:8"]]
+ 00bc2f24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2e88 bytes 80fe02f9
+ 00bc2f24 bytes 807e03f9
- 00bc2e5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5f8:8"]]
- 00bc2e5c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc2ef8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6f8:8"]]
+ 00bc2ef8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2e5c bytes 81fe42f9
+ 00bc2ef8 bytes 817e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-028be9f8b705b2d0f483791cdd2a0ac4"></a>

### [`00bc2f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2f34.md) → [`00bc2fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2fd0.md) _ZN8firebase13remote_config8internal19throttled_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embedded

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bc2f34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2f38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc2f38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc2f34",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc2f38",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc2fe0",
      "READ",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2fd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc2fd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc2fe0",
      "READ",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2f34.md#insn-00bc2f34) · [`00bc2f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2f34.md#insn-00bc2f38) · [`00bc2f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2f34.md#insn-00bc2f48)
- 新版 [`00bc2fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc2/00bc2fd0.md#insn-00bc2fe4)

~~~diff
- 00bc2f34 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc2f34 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc2f34 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc2f34 bytes f30f1ef8
- 00bc2f38 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc2f38 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc2f38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc2f38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc2f38 bytes fd7b01a9
- 00bc2f48 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc2f48 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bc2fe4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc2fe4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc2f48 bytes e80000b5
+ 00bc2fe4 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26cf89006bfc70c333070de55cfe3988"></a>

### [`00bc2f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2f74.md) → [`00bc3010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3010.md) _ZN8firebase13remote_config8internal19throttled_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc3040",
      "incomplete_value": true,
      "site": "00bc3040",
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
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2fa4",
      "incomplete_value": true,
      "site": "00bc2fa4",
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
            "const:638:8"
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
      "definition_site": "00bc3024",
      "incomplete_value": true,
      "site": "00bc3024",
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
      "definition_site": "00bc2f88",
      "incomplete_value": true,
      "site": "00bc2f88",
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
      "definition_site": "00bc3030",
      "incomplete_value": false,
      "site": "00bc3038",
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
            "const:bd4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2f94",
      "incomplete_value": false,
      "site": "00bc2f9c",
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
            "const:c28:8"
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
      "00bc3020",
      "READ",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3030",
      "PARAM",
      [
        "storage",
        "002b9c28",
        null,
        "string"
      ]
    ],
    [
      "00bc3040",
      "WRITE",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3020",
      "READ",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3030",
      "PARAM",
      [
        "storage",
        "002b9bd4",
        null,
        "string"
      ]
    ],
    [
      "00bc3040",
      "WRITE",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2f74.md#insn-00bc2f9c) · [`00bc2fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2f74.md#insn-00bc2fa4) · [`00bc2f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2f74.md#insn-00bc2f84)
- 新版 [`00bc3038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3010.md#insn-00bc3038) · [`00bc3040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3010.md#insn-00bc3040) · [`00bc3020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3010.md#insn-00bc3020)

~~~diff
- 00bc2f9c ["INT_ADD", "register:40f0:8", ["const:bc2f9c:8", "const:4:8"]]
- 00bc2f9c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc3038 ["INT_ADD", "register:40f0:8", ["const:bc3038:8", "const:4:8"]]
+ 00bc3038 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc2f9c bytes dd5f0294
+ 00bc3038 bytes ea5f0294
- 00bc2fa4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:638:8"]]
- 00bc2fa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc3040 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:738:8"]]
+ 00bc3040 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2fa4 bytes 601e03f9
+ 00bc3040 bytes 609e03f9
- 00bc2f84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:638:8"]]
- 00bc2f84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc3020 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:738:8"]]
+ 00bc3020 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2f84 bytes 681e43f9
+ 00bc3020 bytes 689e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f676af4e5c0bb9581e02157eff672a02"></a>

### [`00bc2fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2fb8.md) → [`00bc3054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3054.md) _ZN8firebase13remote_config8internal19throttled_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc3084",
      "incomplete_value": true,
      "site": "00bc3084",
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
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2fe8",
      "incomplete_value": true,
      "site": "00bc2fe8",
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
            "const:638:8"
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
      "definition_site": "00bc3068",
      "incomplete_value": true,
      "site": "00bc3068",
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
      "definition_site": "00bc2fcc",
      "incomplete_value": true,
      "site": "00bc2fcc",
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
      "definition_site": "00bc3070",
      "incomplete_value": false,
      "site": "00bc307c",
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
            "const:bd4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2fd4",
      "incomplete_value": false,
      "site": "00bc2fe0",
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
            "const:c28:8"
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
      "00bc3064",
      "READ",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3070",
      "PARAM",
      [
        "storage",
        "002b9c28",
        null,
        "string"
      ]
    ],
    [
      "00bc3084",
      "WRITE",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3064",
      "READ",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3070",
      "PARAM",
      [
        "storage",
        "002b9bd4",
        null,
        "string"
      ]
    ],
    [
      "00bc3084",
      "WRITE",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2fb8.md#insn-00bc2fe0) · [`00bc2fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2fb8.md#insn-00bc2fe8) · [`00bc2fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2fb8.md#insn-00bc2fc8)
- 新版 [`00bc307c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3054.md#insn-00bc307c) · [`00bc3084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3054.md#insn-00bc3084) · [`00bc3064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3054.md#insn-00bc3064)

~~~diff
- 00bc2fe0 ["INT_ADD", "register:40f0:8", ["const:bc2fe0:8", "const:4:8"]]
- 00bc2fe0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc307c ["INT_ADD", "register:40f0:8", ["const:bc307c:8", "const:4:8"]]
+ 00bc307c ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc2fe0 bytes cc5f0294
+ 00bc307c bytes d95f0294
- 00bc2fe8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:638:8"]]
- 00bc2fe8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc3084 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:738:8"]]
+ 00bc3084 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc2fe8 bytes 601e03f9
+ 00bc3084 bytes 609e03f9
- 00bc2fc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:638:8"]]
- 00bc2fc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc3064 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:738:8"]]
+ 00bc3064 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc2fc8 bytes 681e43f9
+ 00bc3064 bytes 689e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c50ef12979cd33cbb043d5c3a548ca10"></a>

### [`00bc3008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3008.md) → [`00bc30a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc30a4.md) _ZN8firebase13remote_config8internal19throttled_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "definition_site": "00bc30fc",
      "incomplete_value": true,
      "site": "00bc30fc",
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
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3060",
      "incomplete_value": true,
      "site": "00bc3060",
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
            "const:640:8"
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
      "definition_site": "00bc30d8",
      "incomplete_value": true,
      "site": "00bc30e4",
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc303c",
      "incomplete_value": true,
      "site": "00bc3048",
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
                "const:638:8"
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
      "00bc30b8",
      "READ",
      [
        "storage",
        "01126640",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc30d8",
      "READ",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc30fc",
      "WRITE",
      [
        "storage",
        "01126640",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc30b8",
      "READ",
      [
        "storage",
        "01126740",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc30d8",
      "READ",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc30fc",
      "WRITE",
      [
        "storage",
        "01126740",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3008.md#insn-00bc3048) · [`00bc3060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3008.md#insn-00bc3060) · [`00bc301c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3008.md#insn-00bc301c)
- 新版 [`00bc30e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc30a4.md#insn-00bc30e4) · [`00bc30fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc30a4.md#insn-00bc30fc) · [`00bc30b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc30a4.md#insn-00bc30b8)

~~~diff
- 00bc3048 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc3048 ["INT_ADD", "register:40f0:8", ["const:bc3048:8", "const:4:8"]]
- 00bc3048 ["CALLIND", null, ["register:0:8"]]
+ 00bc30e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc30e4 ["INT_ADD", "register:40f0:8", ["const:bc30e4:8", "const:4:8"]]
+ 00bc30e4 ["CALLIND", null, ["register:0:8"]]
- 00bc3048 bytes 00013fd6
+ 00bc30e4 bytes 00013fd6
- 00bc3060 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bc3060 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:640:8"]]
- 00bc3060 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bc30fc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bc30fc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:740:8"]]
+ 00bc30fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bc3060 bytes a0021939
+ 00bc30fc bytes a0021d39
- 00bc301c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:640:8"]]
- 00bc301c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bc301c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bc30b8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:740:8"]]
+ 00bc30b8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bc30b8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bc301c bytes a8025939
+ 00bc30b8 bytes a8025d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7522a9cc520488edd02b004c9d842855"></a>

### [`00bc3074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3074.md) → [`00bc3110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3110.md) _ZN8firebase13remote_config8internal19throttled_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "definition_site": "00bc314c",
      "incomplete_value": true,
      "site": "00bc314c",
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
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc30b0",
      "incomplete_value": true,
      "site": "00bc30b0",
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
            "const:640:8"
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
      "definition_site": "00bc316c",
      "incomplete_value": true,
      "site": "00bc316c",
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
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc30d0",
      "incomplete_value": true,
      "site": "00bc30d0",
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
            "const:638:8"
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
      "definition_site": "00bc3128",
      "incomplete_value": true,
      "site": "00bc3128",
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
      "definition_site": "00bc308c",
      "incomplete_value": true,
      "site": "00bc308c",
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
      "00bc3124",
      "READ",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3130",
      "READ",
      [
        "storage",
        "01126640",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc314c",
      "WRITE",
      [
        "storage",
        "01126640",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc3124",
      "READ",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3130",
      "READ",
      [
        "storage",
        "01126740",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc314c",
      "WRITE",
      [
        "storage",
        "01126740",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc30b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3074.md#insn-00bc30b0) · [`00bc30cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3074.md#insn-00bc30cc) · [`00bc30d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3074.md#insn-00bc30d0)
- 新版 [`00bc314c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3110.md#insn-00bc314c) · [`00bc3168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3110.md#insn-00bc3168) · [`00bc316c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3110.md#insn-00bc316c)

~~~diff
- 00bc30b0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc30b0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc30b0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:640:8"]]
- 00bc30b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bc314c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bc314c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bc314c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:740:8"]]
+ 00bc314c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc30b0 bytes bf021939
+ 00bc314c bytes bf021d39
- 00bc30cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc30cc ["INT_ADD", "register:40f0:8", ["const:bc30cc:8", "const:4:8"]]
- 00bc30cc ["CALLIND", null, ["register:0:8"]]
+ 00bc3168 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc3168 ["INT_ADD", "register:40f0:8", ["const:bc3168:8", "const:4:8"]]
+ 00bc3168 ["CALLIND", null, ["register:0:8"]]
- 00bc30cc bytes 00013fd6
+ 00bc3168 bytes 00013fd6
- 00bc30d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:638:8"]]
- 00bc30d0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bc30d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bc316c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:738:8"]]
+ 00bc316c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bc316c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bc30d0 bytes 9f1e03f9
+ 00bc316c bytes 9f9e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18265d1d271e63c0ea80a83b447dca2e"></a>

### [`00bc30e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc30e4.md) → [`00bc3180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3180.md) _ZN8firebase13remote_config8internal19throttled_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
      "definition_site": "00bc31c0",
      "incomplete_value": true,
      "site": "00bc31c0",
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
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3124",
      "incomplete_value": true,
      "site": "00bc3124",
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
            "const:638:8"
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
      "definition_site": "00bc319c",
      "incomplete_value": true,
      "site": "00bc319c",
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
      "definition_site": "00bc3100",
      "incomplete_value": true,
      "site": "00bc3100",
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
      "definition_site": "00bc31a4",
      "incomplete_value": false,
      "site": "00bc31b8",
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
            "const:bd4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3108",
      "incomplete_value": false,
      "site": "00bc311c",
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
            "const:c28:8"
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
      "00bc3194",
      "READ",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc31a4",
      "PARAM",
      [
        "storage",
        "002b9c28",
        null,
        "string"
      ]
    ],
    [
      "00bc31c0",
      "WRITE",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3194",
      "READ",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc31a4",
      "PARAM",
      [
        "storage",
        "002b9bd4",
        null,
        "string"
      ]
    ],
    [
      "00bc31c0",
      "WRITE",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc311c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc30e4.md#insn-00bc311c) · [`00bc3124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc30e4.md#insn-00bc3124) · [`00bc30f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc30e4.md#insn-00bc30f8)
- 新版 [`00bc31b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3180.md#insn-00bc31b8) · [`00bc31c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3180.md#insn-00bc31c0) · [`00bc3194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3180.md#insn-00bc3194)

~~~diff
- 00bc311c ["INT_ADD", "register:40f0:8", ["const:bc311c:8", "const:4:8"]]
- 00bc311c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc31b8 ["INT_ADD", "register:40f0:8", ["const:bc31b8:8", "const:4:8"]]
+ 00bc31b8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc311c bytes 7d5f0294
+ 00bc31b8 bytes 8a5f0294
- 00bc3124 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:638:8"]]
- 00bc3124 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc31c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:738:8"]]
+ 00bc31c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc3124 bytes 801e03f9
+ 00bc31c0 bytes 809e03f9
- 00bc30f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:638:8"]]
- 00bc30f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc3194 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:738:8"]]
+ 00bc3194 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc30f8 bytes 811e43f9
+ 00bc3194 bytes 819e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf12aabb41d72adc0ffb9777d29bbc78"></a>

### [`00bc3154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3154.md) → [`00bc31f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc31f0.md) _ZN8firebase13remote_config8internal19throttled_exception11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00bc320c",
      "incomplete_value": false,
      "site": "00bc3210",
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
            "const:30b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3170",
      "incomplete_value": false,
      "site": "00bc3174",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc321c",
      "incomplete_value": true,
      "site": "00bc3228",
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
      "definition_site": "00bc3180",
      "incomplete_value": true,
      "site": "00bc318c",
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
      "00bc320c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bc321c",
      "DATA",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc320c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bc321c",
      "DATA",
      [
        "storage",
        "01126748",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3154.md#insn-00bc3174) · [`00bc3170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3154.md#insn-00bc3170) · [`00bc317c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3154.md#insn-00bc317c)
- 新版 [`00bc3210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc31f0.md#insn-00bc3210) · [`00bc320c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc31f0.md#insn-00bc320c) · [`00bc3218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc31f0.md#insn-00bc3218)

~~~diff
- 00bc3174 ["INT_ADD", "register:40f0:8", ["const:bc3174:8", "const:4:8"]]
- 00bc3174 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bc3210 ["INT_ADD", "register:40f0:8", ["const:bc3210:8", "const:4:8"]]
+ 00bc3210 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bc3174 bytes a35f0294
+ 00bc3210 bytes b05f0294
- 00bc3170 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00bc3170 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc3170 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc3170 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc320c ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bc320c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc320c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc320c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc3170 bytes 009c0d91
+ 00bc320c bytes 002c0c91
- 00bc317c ["COPY", "tmp:0:8", ["const:648:8"]]
- 00bc317c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc317c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc317c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc3218 ["COPY", "tmp:0:8", ["const:748:8"]]
+ 00bc3218 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc3218 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc3218 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc317c bytes 08211991
+ 00bc3218 bytes 08211d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e8addd54c24350c9b878f588ff1f24c"></a>

### [`00bc3190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3190.md) → [`00bc322c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc322c.md) _ZN8firebase13remote_config8internal19throttled_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc326c",
      "incomplete_value": true,
      "site": "00bc326c",
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
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc31d0",
      "incomplete_value": true,
      "site": "00bc31d0",
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
            "const:638:8"
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
      "definition_site": "00bc3248",
      "incomplete_value": true,
      "site": "00bc3248",
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
      "definition_site": "00bc31ac",
      "incomplete_value": true,
      "site": "00bc31ac",
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
      "definition_site": "00bc3250",
      "incomplete_value": false,
      "site": "00bc3264",
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
            "const:bd4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc31b4",
      "incomplete_value": false,
      "site": "00bc31c8",
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
            "const:c28:8"
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
      "00bc3240",
      "READ",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3250",
      "PARAM",
      [
        "storage",
        "002b9c28",
        null,
        "string"
      ]
    ],
    [
      "00bc326c",
      "WRITE",
      [
        "storage",
        "01126638",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3240",
      "READ",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3250",
      "PARAM",
      [
        "storage",
        "002b9bd4",
        null,
        "string"
      ]
    ],
    [
      "00bc326c",
      "WRITE",
      [
        "storage",
        "01126738",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc31c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3190.md#insn-00bc31c8) · [`00bc31d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3190.md#insn-00bc31d0) · [`00bc31a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3190.md#insn-00bc31a4)
- 新版 [`00bc3264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc322c.md#insn-00bc3264) · [`00bc326c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc322c.md#insn-00bc326c) · [`00bc3240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc322c.md#insn-00bc3240)

~~~diff
- 00bc31c8 ["INT_ADD", "register:40f0:8", ["const:bc31c8:8", "const:4:8"]]
- 00bc31c8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc3264 ["INT_ADD", "register:40f0:8", ["const:bc3264:8", "const:4:8"]]
+ 00bc3264 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc31c8 bytes 525f0294
+ 00bc3264 bytes 5f5f0294
- 00bc31d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:638:8"]]
- 00bc31d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc326c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:738:8"]]
+ 00bc326c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc31d0 bytes 801e03f9
+ 00bc326c bytes 809e03f9
- 00bc31a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:638:8"]]
- 00bc31a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc3240 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:738:8"]]
+ 00bc3240 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc31a4 bytes 811e43f9
+ 00bc3240 bytes 819e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a79528c72d68a2f390042482cd0eb1b"></a>

### [`00bc3200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3200.md) → [`00bc329c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc329c.md) _ZN8firebase13remote_config8internal19throttled_exception10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00bc32b8",
      "incomplete_value": false,
      "site": "00bc32bc",
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
            "const:54d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc321c",
      "incomplete_value": false,
      "site": "00bc3220",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc32c8",
      "incomplete_value": true,
      "site": "00bc32d4",
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
      "definition_site": "00bc322c",
      "incomplete_value": true,
      "site": "00bc3238",
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
      "00bc32b8",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bc32c8",
      "DATA",
      [
        "storage",
        "01126650",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc32b8",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bc32c8",
      "DATA",
      [
        "storage",
        "01126750",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3200.md#insn-00bc3220) · [`00bc321c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3200.md#insn-00bc321c) · [`00bc3228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3200.md#insn-00bc3228)
- 新版 [`00bc32bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc329c.md#insn-00bc32bc) · [`00bc32b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc329c.md#insn-00bc32b8) · [`00bc32c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc329c.md#insn-00bc32c4)

~~~diff
- 00bc3220 ["INT_ADD", "register:40f0:8", ["const:bc3220:8", "const:4:8"]]
- 00bc3220 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bc32bc ["INT_ADD", "register:40f0:8", ["const:bc32bc:8", "const:4:8"]]
+ 00bc32bc ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bc3220 bytes 785f0294
+ 00bc32bc bytes 855f0294
- 00bc321c ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00bc321c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc321c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc321c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc32b8 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bc32b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc32b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc32b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc321c bytes 00781491
+ 00bc32b8 bytes 00341591
- 00bc3228 ["COPY", "tmp:0:8", ["const:650:8"]]
- 00bc3228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc3228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc3228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc32c4 ["COPY", "tmp:0:8", ["const:750:8"]]
+ 00bc32c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc32c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc32c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc3228 bytes 08411991
+ 00bc32c4 bytes 08411d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff0d2e4342953f199c270f79fe01b0eb"></a>

### [`00bc323c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc323c.md) → [`00bc32d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc32d8.md) _ZN8firebase13remote_config8internal26jni_config_update_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12E

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc3304",
      "incomplete_value": true,
      "site": "00bc3304",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3268",
      "incomplete_value": true,
      "site": "00bc3268",
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
            "const:658:8"
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
      "definition_site": "00bc32ec",
      "incomplete_value": true,
      "site": "00bc32ec",
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
      "definition_site": "00bc3250",
      "incomplete_value": true,
      "site": "00bc3250",
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
      "definition_site": "00bc32f8",
      "incomplete_value": false,
      "site": "00bc32fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:e9e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc325c",
      "incomplete_value": false,
      "site": "00bc3260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
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
      "00bc32e8",
      "READ",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc32f8",
      "PARAM",
      [
        "storage",
        "002b6e5e",
        null,
        "string"
      ]
    ],
    [
      "00bc3304",
      "WRITE",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc32e8",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc32f8",
      "PARAM",
      [
        "storage",
        "002b6e9e",
        null,
        "string"
      ]
    ],
    [
      "00bc3304",
      "WRITE",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc323c.md#insn-00bc3260) · [`00bc3268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc323c.md#insn-00bc3268) · [`00bc324c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc323c.md#insn-00bc324c)
- 新版 [`00bc32fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc32d8.md#insn-00bc32fc) · [`00bc3304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc32d8.md#insn-00bc3304) · [`00bc32e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc32d8.md#insn-00bc32e8)

~~~diff
- 00bc3260 ["INT_ADD", "register:40f0:8", ["const:bc3260:8", "const:4:8"]]
- 00bc3260 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc32fc ["INT_ADD", "register:40f0:8", ["const:bc32fc:8", "const:4:8"]]
+ 00bc32fc ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc3260 bytes 2c5f0294
+ 00bc32fc bytes 395f0294
- 00bc3268 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
- 00bc3268 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc3304 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
+ 00bc3304 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc3268 bytes 602e03f9
+ 00bc3304 bytes 60ae03f9
- 00bc324c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
- 00bc324c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc32e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
+ 00bc32e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc324c bytes 682e43f9
+ 00bc32e8 bytes 68ae43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aaddcb6089a9fd03518dabeb91c10c7a"></a>

### [`00bc327c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc327c.md) → [`00bc3318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3318.md) _ZN8firebase13remote_config8internal26jni_config_update_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12E

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc3344",
      "incomplete_value": true,
      "site": "00bc3344",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc32a8",
      "incomplete_value": true,
      "site": "00bc32a8",
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
            "const:658:8"
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
      "definition_site": "00bc332c",
      "incomplete_value": true,
      "site": "00bc332c",
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
      "definition_site": "00bc3290",
      "incomplete_value": true,
      "site": "00bc3290",
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
      "definition_site": "00bc3334",
      "incomplete_value": false,
      "site": "00bc333c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:e9e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3298",
      "incomplete_value": false,
      "site": "00bc32a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
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
      "00bc3328",
      "READ",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3334",
      "PARAM",
      [
        "storage",
        "002b6e5e",
        null,
        "string"
      ]
    ],
    [
      "00bc3344",
      "WRITE",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3328",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3334",
      "PARAM",
      [
        "storage",
        "002b6e9e",
        null,
        "string"
      ]
    ],
    [
      "00bc3344",
      "WRITE",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc32a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc327c.md#insn-00bc32a0) · [`00bc32a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc327c.md#insn-00bc32a8) · [`00bc328c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc327c.md#insn-00bc328c)
- 新版 [`00bc333c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3318.md#insn-00bc333c) · [`00bc3344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3318.md#insn-00bc3344) · [`00bc3328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3318.md#insn-00bc3328)

~~~diff
- 00bc32a0 ["INT_ADD", "register:40f0:8", ["const:bc32a0:8", "const:4:8"]]
- 00bc32a0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc333c ["INT_ADD", "register:40f0:8", ["const:bc333c:8", "const:4:8"]]
+ 00bc333c ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc32a0 bytes 1c5f0294
+ 00bc333c bytes 295f0294
- 00bc32a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
- 00bc32a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc3344 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
+ 00bc3344 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc32a8 bytes 602e03f9
+ 00bc3344 bytes 60ae03f9
- 00bc328c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
- 00bc328c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc3328 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
+ 00bc3328 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc328c bytes 682e43f9
+ 00bc3328 bytes 68ae43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf5e55decaae2cab587bf30e26e739e8"></a>

### [`00bc32bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc32bc.md) → [`00bc3358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3358.md) _ZN8firebase13remote_config8internal26jni_config_update_listener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc3388",
      "incomplete_value": true,
      "site": "00bc3388",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc32ec",
      "incomplete_value": true,
      "site": "00bc32ec",
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
            "const:658:8"
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
      "definition_site": "00bc336c",
      "incomplete_value": true,
      "site": "00bc336c",
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
      "definition_site": "00bc32d0",
      "incomplete_value": true,
      "site": "00bc32d0",
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
      "definition_site": "00bc3378",
      "incomplete_value": false,
      "site": "00bc3380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:e9e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc32dc",
      "incomplete_value": false,
      "site": "00bc32e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
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
      "00bc3368",
      "READ",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3378",
      "PARAM",
      [
        "storage",
        "002b6e5e",
        null,
        "string"
      ]
    ],
    [
      "00bc3388",
      "WRITE",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3368",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3378",
      "PARAM",
      [
        "storage",
        "002b6e9e",
        null,
        "string"
      ]
    ],
    [
      "00bc3388",
      "WRITE",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc32e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc32bc.md#insn-00bc32e4) · [`00bc32ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc32bc.md#insn-00bc32ec) · [`00bc32cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc32bc.md#insn-00bc32cc)
- 新版 [`00bc3380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3358.md#insn-00bc3380) · [`00bc3388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3358.md#insn-00bc3388) · [`00bc3368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3358.md#insn-00bc3368)

~~~diff
- 00bc32e4 ["INT_ADD", "register:40f0:8", ["const:bc32e4:8", "const:4:8"]]
- 00bc32e4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc3380 ["INT_ADD", "register:40f0:8", ["const:bc3380:8", "const:4:8"]]
+ 00bc3380 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc32e4 bytes 0b5f0294
+ 00bc3380 bytes 185f0294
- 00bc32ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
- 00bc32ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc3388 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
+ 00bc3388 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc32ec bytes 602e03f9
+ 00bc3388 bytes 60ae03f9
- 00bc32cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
- 00bc32cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc3368 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
+ 00bc3368 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc32cc bytes 682e43f9
+ 00bc3368 bytes 68ae43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cd1678c1802791e52c1d51ee650fdc5"></a>

### [`00bc3300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3300.md) → [`00bc339c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc339c.md) _ZN8firebase13remote_config8internal26jni_config_update_listener10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3330"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc33cc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc33b0",
      "incomplete_value": true,
      "site": "00bc33b0",
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
      "definition_site": "00bc3314",
      "incomplete_value": true,
      "site": "00bc3314",
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
      "00bc33ac",
      "READ",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc331c",
      "PARAM",
      [
        "storage",
        "002b6e5e",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bc3330",
      "WRITE",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc33ac",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc33b8",
      "PARAM",
      [
        "storage",
        "002b6e9e",
        null,
        "string"
      ]
    ],
    [
      "00bc33cc",
      "WRITE",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3300.md#insn-00bc3314) · [`00bc3328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3300.md#insn-00bc3328) · [`00bc3330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3300.md#insn-00bc3330)
- 新版 [`00bc33b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc339c.md#insn-00bc33b0) · [`00bc33c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc339c.md#insn-00bc33c4)

~~~diff
- 00bc3314 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc3314 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bc33b0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc33b0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc3314 bytes 080100b5
+ 00bc33b0 bytes 080100b5
- 00bc3328 ["INT_ADD", "register:40f0:8", ["const:bc3328:8", "const:4:8"]]
- 00bc3328 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc33c4 ["INT_ADD", "register:40f0:8", ["const:bc33c4:8", "const:4:8"]]
+ 00bc33c4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc3328 bytes fa5e0294
+ 00bc33c4 bytes 075f0294
- 00bc3330 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
- 00bc3330 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc3330 bytes 602e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dd04b058401aa526e2d162a919451d4"></a>

### [`00bc33bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc33bc.md) → [`00bc3458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3458.md) _ZN8firebase13remote_config8internal26jni_config_update_listener12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_value, call, call_count, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 46.43% / 新版 46.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc33bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc33c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc33c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc33bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc33c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc33c4",
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
      "00bc3458",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bc345c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc3460",
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

- 旧版 [`00bc33bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc33bc.md#insn-00bc33bc) · [`00bc33c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc33bc.md#insn-00bc33c0) · [`00bc33c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc33bc.md#insn-00bc33c4)

~~~diff
- 00bc33bc ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bc33bc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bc33bc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc33bc bytes f50f1df8
- 00bc33c0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc33c0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc33c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc33c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc33c0 bytes f44f01a9
- 00bc33c4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc33c4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc33c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bc33c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc33c4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcc5c39c8e6838aa97255aede80fe598"></a>

### [`00bc342c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc342c.md) → [`00bc34c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc34c8.md) _ZN8firebase13remote_config8internal26jni_config_update_listener14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
      "site": "00bc346c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc3508"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3448"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc3440",
      "READ",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc3448",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc350c"
      ]
    ],
    [
      "unmatched:00bc3450",
      "PARAM",
      [
        "storage",
        "002b6e5e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc34dc",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc34e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc350c"
      ]
    ],
    [
      "00bc34ec",
      "PARAM",
      [
        "storage",
        "002b6e9e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc342c.md#insn-00bc3448) · [`00bc3464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc342c.md#insn-00bc3464) · [`00bc346c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc342c.md#insn-00bc346c)
- 新版 [`00bc3500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc34c8.md#insn-00bc3500)

~~~diff
- 00bc3448 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc3448 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc3448 bytes 410100b5
- 00bc3464 ["INT_ADD", "register:40f0:8", ["const:bc3464:8", "const:4:8"]]
- 00bc3464 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc3500 ["INT_ADD", "register:40f0:8", ["const:bc3500:8", "const:4:8"]]
+ 00bc3500 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc3464 bytes ab5e0294
+ 00bc3500 bytes b85e0294
- 00bc346c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:658:8"]]
- 00bc346c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc346c bytes 802e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8739c3d1577ab2e35cf3662303274a3"></a>

### [`00bc34d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc34d8.md) → [`00bc3574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3574.md) _ZN8firebase13remote_config8internal26jni_config_update_listener13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bc34d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc34d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc34dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc34d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc34dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc34ec",
      "READ",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3574",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc3578",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc3588",
      "READ",
      [
        "storage",
        "01126758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc34d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc34d8.md#insn-00bc34d8) · [`00bc34dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc34d8.md#insn-00bc34dc) · [`00bc34f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc34d8.md#insn-00bc34f4)

~~~diff
- 00bc34d8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc34d8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc34d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bc34d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc34d8 bytes f44fbea9
- 00bc34dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc34dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc34dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bc34dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc34dc bytes fd7b01a9
- 00bc34f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc34f4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bc34f4 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d97f62cd75a8cc715febee8f1c379f03"></a>

### [`00bc3584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3584.md) → [`00bc3620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3620.md) _ZN8firebase13remote_config8internal13config_update19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc364c",
      "incomplete_value": true,
      "site": "00bc364c",
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
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc35b0",
      "incomplete_value": true,
      "site": "00bc35b0",
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
            "const:678:8"
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
      "definition_site": "00bc3634",
      "incomplete_value": true,
      "site": "00bc3634",
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
      "definition_site": "00bc3598",
      "incomplete_value": true,
      "site": "00bc3598",
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
      "definition_site": "00bc3640",
      "incomplete_value": false,
      "site": "00bc3644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc35a4",
      "incomplete_value": false,
      "site": "00bc35a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:dc:8"
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
      "00bc3630",
      "READ",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3640",
      "PARAM",
      [
        "storage",
        "002bc0dc",
        null,
        "string"
      ]
    ],
    [
      "00bc364c",
      "WRITE",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3630",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3640",
      "PARAM",
      [
        "storage",
        "002bc088",
        null,
        "string"
      ]
    ],
    [
      "00bc364c",
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc35a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3584.md#insn-00bc35a8) · [`00bc35b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3584.md#insn-00bc35b0) · [`00bc3594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3584.md#insn-00bc3594)
- 新版 [`00bc3644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3620.md#insn-00bc3644) · [`00bc364c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3620.md#insn-00bc364c) · [`00bc3630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3620.md#insn-00bc3630)

~~~diff
- 00bc35a8 ["INT_ADD", "register:40f0:8", ["const:bc35a8:8", "const:4:8"]]
- 00bc35a8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc3644 ["INT_ADD", "register:40f0:8", ["const:bc3644:8", "const:4:8"]]
+ 00bc3644 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc35a8 bytes 5a5e0294
+ 00bc3644 bytes 675e0294
- 00bc35b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:678:8"]]
- 00bc35b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc364c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
+ 00bc364c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc35b0 bytes 603e03f9
+ 00bc364c bytes 60be03f9
- 00bc3594 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:678:8"]]
- 00bc3594 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc3630 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
+ 00bc3630 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc3594 bytes 683e43f9
+ 00bc3630 bytes 68be43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a4c33cdc0ae12b52907eb9780fa50de"></a>

### [`00bc3604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3604.md) → [`00bc36a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc36a0.md) _ZN8firebase13remote_config8internal13config_update10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc36d0",
      "incomplete_value": true,
      "site": "00bc36d0",
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
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3634",
      "incomplete_value": true,
      "site": "00bc3634",
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
            "const:678:8"
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
      "definition_site": "00bc36b4",
      "incomplete_value": true,
      "site": "00bc36b4",
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
      "definition_site": "00bc3618",
      "incomplete_value": true,
      "site": "00bc3618",
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
      "definition_site": "00bc36c0",
      "incomplete_value": false,
      "site": "00bc36c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3624",
      "incomplete_value": false,
      "site": "00bc362c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:dc:8"
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
      "00bc36b0",
      "READ",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc36c0",
      "PARAM",
      [
        "storage",
        "002bc0dc",
        null,
        "string"
      ]
    ],
    [
      "00bc36d0",
      "WRITE",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc36b0",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc36c0",
      "PARAM",
      [
        "storage",
        "002bc088",
        null,
        "string"
      ]
    ],
    [
      "00bc36d0",
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc362c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3604.md#insn-00bc362c) · [`00bc3634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3604.md#insn-00bc3634) · [`00bc3614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3604.md#insn-00bc3614)
- 新版 [`00bc36c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc36a0.md#insn-00bc36c8) · [`00bc36d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc36a0.md#insn-00bc36d0) · [`00bc36b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc36a0.md#insn-00bc36b0)

~~~diff
- 00bc362c ["INT_ADD", "register:40f0:8", ["const:bc362c:8", "const:4:8"]]
- 00bc362c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc36c8 ["INT_ADD", "register:40f0:8", ["const:bc36c8:8", "const:4:8"]]
+ 00bc36c8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc362c bytes 395e0294
+ 00bc36c8 bytes 465e0294
- 00bc3634 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:678:8"]]
- 00bc3634 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc36d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
+ 00bc36d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc3634 bytes 603e03f9
+ 00bc36d0 bytes 60be03f9
- 00bc3614 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:678:8"]]
- 00bc3614 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc36b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
+ 00bc36b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc3614 bytes 683e43f9
+ 00bc36b0 bytes 68be43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-230778ea08b13432f965e5112da88622"></a>

### [`00bc3648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3648.md) → [`00bc36e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc36e4.md) _ZN8firebase13remote_config8internal13config_update10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc3714",
      "incomplete_value": true,
      "site": "00bc3714",
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
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3678",
      "incomplete_value": true,
      "site": "00bc3678",
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
            "const:678:8"
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
      "definition_site": "00bc36f8",
      "incomplete_value": true,
      "site": "00bc36f8",
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
      "definition_site": "00bc365c",
      "incomplete_value": true,
      "site": "00bc365c",
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
      "definition_site": "00bc3700",
      "incomplete_value": false,
      "site": "00bc370c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3664",
      "incomplete_value": false,
      "site": "00bc3670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:dc:8"
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
      "00bc36f4",
      "READ",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3700",
      "PARAM",
      [
        "storage",
        "002bc0dc",
        null,
        "string"
      ]
    ],
    [
      "00bc3714",
      "WRITE",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc36f4",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3700",
      "PARAM",
      [
        "storage",
        "002bc088",
        null,
        "string"
      ]
    ],
    [
      "00bc3714",
      "WRITE",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3648.md#insn-00bc3670) · [`00bc3678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3648.md#insn-00bc3678) · [`00bc3658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3648.md#insn-00bc3658)
- 新版 [`00bc370c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc36e4.md#insn-00bc370c) · [`00bc3714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc36e4.md#insn-00bc3714) · [`00bc36f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc36e4.md#insn-00bc36f4)

~~~diff
- 00bc3670 ["INT_ADD", "register:40f0:8", ["const:bc3670:8", "const:4:8"]]
- 00bc3670 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc370c ["INT_ADD", "register:40f0:8", ["const:bc370c:8", "const:4:8"]]
+ 00bc370c ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc3670 bytes 285e0294
+ 00bc370c bytes 355e0294
- 00bc3678 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:678:8"]]
- 00bc3678 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc3714 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
+ 00bc3714 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc3678 bytes 603e03f9
+ 00bc3714 bytes 60be03f9
- 00bc3658 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:678:8"]]
- 00bc3658 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc36f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
+ 00bc36f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc3658 bytes 683e43f9
+ 00bc36f4 bytes 68be43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23b390df2bad3a366b7db36c93d84b65"></a>

### [`00bc3774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3774.md) → [`00bc3810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3810.md) _ZN8firebase13remote_config8internal13config_update14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bc37b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc3850"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3790"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc3788",
      "READ",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc3790",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3854"
      ]
    ],
    [
      "unmatched:00bc3798",
      "PARAM",
      [
        "storage",
        "002bc0dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc3824",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc382c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3854"
      ]
    ],
    [
      "00bc3834",
      "PARAM",
      [
        "storage",
        "002bc088",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3774.md#insn-00bc3790) · [`00bc37ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3774.md#insn-00bc37ac) · [`00bc37b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3774.md#insn-00bc37b4)
- 新版 [`00bc3848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3810.md#insn-00bc3848)

~~~diff
- 00bc3790 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc3790 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc3790 bytes 410100b5
- 00bc37ac ["INT_ADD", "register:40f0:8", ["const:bc37ac:8", "const:4:8"]]
- 00bc37ac ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc3848 ["INT_ADD", "register:40f0:8", ["const:bc3848:8", "const:4:8"]]
+ 00bc3848 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc37ac bytes d95d0294
+ 00bc3848 bytes e65d0294
- 00bc37b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:678:8"]]
- 00bc37b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc37b4 bytes 803e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff7eec1f0c851d8cb10ffb25ad81489b"></a>

### [`00bc3820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3820.md) → [`00bc38bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc38bc.md) _ZN8firebase13remote_config8internal13config_update13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00bc3860"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc38fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc383c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc3834",
      "READ",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc383c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3900"
      ]
    ],
    [
      "unmatched:00bc3844",
      "PARAM",
      [
        "storage",
        "002bc0dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc38d0",
      "READ",
      [
        "storage",
        "01126778",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc38d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3900"
      ]
    ],
    [
      "00bc38e0",
      "PARAM",
      [
        "storage",
        "002bc088",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc383c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3820.md#insn-00bc383c) · [`00bc3858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3820.md#insn-00bc3858) · [`00bc3860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3820.md#insn-00bc3860)
- 新版 [`00bc38f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc38bc.md#insn-00bc38f4)

~~~diff
- 00bc383c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc383c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc383c bytes 410100b5
- 00bc3858 ["INT_ADD", "register:40f0:8", ["const:bc3858:8", "const:4:8"]]
- 00bc3858 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc38f4 ["INT_ADD", "register:40f0:8", ["const:bc38f4:8", "const:4:8"]]
+ 00bc38f4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc3858 bytes ae5d0294
+ 00bc38f4 bytes bb5d0294
- 00bc3860 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:678:8"]]
- 00bc3860 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc3860 bytes 803e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b62cf0df126273332a56e75b343dc8cf"></a>

### [`00bc38cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc38cc.md) → [`00bc3968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3968.md) _ZN8firebase13remote_config8internal35config_update_listener_registration19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8in

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

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
      "site": "00bc38f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc3994"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc397c",
      "incomplete_value": true,
      "site": "00bc397c",
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
      "definition_site": "00bc38e0",
      "incomplete_value": true,
      "site": "00bc38e0",
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
      "00bc3978",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc38ec",
      "PARAM",
      [
        "storage",
        "002a982f",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bc38f0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00bc3978",
      "READ",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3988",
      "PARAM",
      [
        "storage",
        "002a985e",
        null,
        "string"
      ]
    ],
    [
      "00bc398c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc38e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc38cc.md#insn-00bc38e0) · [`00bc38f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc38cc.md#insn-00bc38f0) · [`00bc38f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc38cc.md#insn-00bc38f8)
- 新版 [`00bc397c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3968.md#insn-00bc397c)

~~~diff
- 00bc38e0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bc38e0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bc397c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bc397c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc38e0 bytes e80000b5
+ 00bc397c bytes e80000b5
- 00bc38f0 ["INT_ADD", "register:40f0:8", ["const:bc38f0:8", "const:4:8"]]
- 00bc38f0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc38f0 bytes 885d0294
- 00bc38f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
- 00bc38f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc38f8 bytes 604e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ebd6b16fd65181f3c810678e23c0ef9"></a>

### [`00bc390c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc390c.md) → [`00bc39a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc39a8.md) _ZN8firebase13remote_config8internal35config_update_listener_registration19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8in

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc39d4",
      "incomplete_value": true,
      "site": "00bc39d4",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3938",
      "incomplete_value": true,
      "site": "00bc3938",
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
            "const:698:8"
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
      "definition_site": "00bc39bc",
      "incomplete_value": true,
      "site": "00bc39bc",
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
      "definition_site": "00bc3920",
      "incomplete_value": true,
      "site": "00bc3920",
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
      "definition_site": "00bc39c4",
      "incomplete_value": false,
      "site": "00bc39cc",
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
            "const:85e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3928",
      "incomplete_value": false,
      "site": "00bc3930",
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
            "const:82f:8"
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
      "00bc39b8",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc39c4",
      "PARAM",
      [
        "storage",
        "002a982f",
        null,
        "string"
      ]
    ],
    [
      "00bc39d4",
      "WRITE",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc39b8",
      "READ",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc39c4",
      "PARAM",
      [
        "storage",
        "002a985e",
        null,
        "string"
      ]
    ],
    [
      "00bc39d4",
      "WRITE",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc390c.md#insn-00bc3930) · [`00bc3938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc390c.md#insn-00bc3938) · [`00bc391c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc390c.md#insn-00bc391c)
- 新版 [`00bc39cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc39a8.md#insn-00bc39cc) · [`00bc39d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc39a8.md#insn-00bc39d4) · [`00bc39b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc39a8.md#insn-00bc39b8)

~~~diff
- 00bc3930 ["INT_ADD", "register:40f0:8", ["const:bc3930:8", "const:4:8"]]
- 00bc3930 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc39cc ["INT_ADD", "register:40f0:8", ["const:bc39cc:8", "const:4:8"]]
+ 00bc39cc ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc3930 bytes 785d0294
+ 00bc39cc bytes 855d0294
- 00bc3938 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
- 00bc3938 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc39d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
+ 00bc39d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc3938 bytes 604e03f9
+ 00bc39d4 bytes 60ce03f9
- 00bc391c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
- 00bc391c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc39b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
+ 00bc39b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc391c bytes 684e43f9
+ 00bc39b8 bytes 68ce43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cecbff426946c618e6913dfdb8443642"></a>

### [`00bc394c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc394c.md) → [`00bc39e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc39e8.md) _ZN8firebase13remote_config8internal35config_update_listener_registration10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc3a18",
      "incomplete_value": true,
      "site": "00bc3a18",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc397c",
      "incomplete_value": true,
      "site": "00bc397c",
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
            "const:698:8"
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
      "definition_site": "00bc39fc",
      "incomplete_value": true,
      "site": "00bc39fc",
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
      "definition_site": "00bc3960",
      "incomplete_value": true,
      "site": "00bc3960",
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
      "definition_site": "00bc3a08",
      "incomplete_value": false,
      "site": "00bc3a10",
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
            "const:85e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc396c",
      "incomplete_value": false,
      "site": "00bc3974",
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
            "const:82f:8"
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
      "00bc39f8",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3a08",
      "PARAM",
      [
        "storage",
        "002a982f",
        null,
        "string"
      ]
    ],
    [
      "00bc3a18",
      "WRITE",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc39f8",
      "READ",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3a08",
      "PARAM",
      [
        "storage",
        "002a985e",
        null,
        "string"
      ]
    ],
    [
      "00bc3a18",
      "WRITE",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc394c.md#insn-00bc3974) · [`00bc397c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc394c.md#insn-00bc397c) · [`00bc395c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc394c.md#insn-00bc395c)
- 新版 [`00bc3a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc39e8.md#insn-00bc3a10) · [`00bc3a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc39e8.md#insn-00bc3a18) · [`00bc39f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc39e8.md#insn-00bc39f8)

~~~diff
- 00bc3974 ["INT_ADD", "register:40f0:8", ["const:bc3974:8", "const:4:8"]]
- 00bc3974 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc3a10 ["INT_ADD", "register:40f0:8", ["const:bc3a10:8", "const:4:8"]]
+ 00bc3a10 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc3974 bytes 675d0294
+ 00bc3a10 bytes 745d0294
- 00bc397c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
- 00bc397c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc3a18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
+ 00bc3a18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc397c bytes 604e03f9
+ 00bc3a18 bytes 60ce03f9
- 00bc395c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
- 00bc395c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc39f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
+ 00bc39f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc395c bytes 684e43f9
+ 00bc39f8 bytes 68ce43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-143ee4055ea4599a46e71703bb364931"></a>

### [`00bc3990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3990.md) → [`00bc3a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3a2c.md) _ZN8firebase13remote_config8internal35config_update_listener_registration10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00bc3a5c",
      "incomplete_value": true,
      "site": "00bc3a5c",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc39c0",
      "incomplete_value": true,
      "site": "00bc39c0",
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
            "const:698:8"
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
      "definition_site": "00bc3a40",
      "incomplete_value": true,
      "site": "00bc3a40",
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
      "definition_site": "00bc39a4",
      "incomplete_value": true,
      "site": "00bc39a4",
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
      "definition_site": "00bc3a48",
      "incomplete_value": false,
      "site": "00bc3a54",
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
            "const:85e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc39ac",
      "incomplete_value": false,
      "site": "00bc39b8",
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
            "const:82f:8"
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
      "00bc3a3c",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3a48",
      "PARAM",
      [
        "storage",
        "002a982f",
        null,
        "string"
      ]
    ],
    [
      "00bc3a5c",
      "WRITE",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc3a3c",
      "READ",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3a48",
      "PARAM",
      [
        "storage",
        "002a985e",
        null,
        "string"
      ]
    ],
    [
      "00bc3a5c",
      "WRITE",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc39b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3990.md#insn-00bc39b8) · [`00bc39c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3990.md#insn-00bc39c0) · [`00bc39a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3990.md#insn-00bc39a0)
- 新版 [`00bc3a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3a2c.md#insn-00bc3a54) · [`00bc3a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3a2c.md#insn-00bc3a5c) · [`00bc3a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3a2c.md#insn-00bc3a3c)

~~~diff
- 00bc39b8 ["INT_ADD", "register:40f0:8", ["const:bc39b8:8", "const:4:8"]]
- 00bc39b8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc3a54 ["INT_ADD", "register:40f0:8", ["const:bc3a54:8", "const:4:8"]]
+ 00bc3a54 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc39b8 bytes 565d0294
+ 00bc3a54 bytes 635d0294
- 00bc39c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
- 00bc39c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc3a5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
+ 00bc3a5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc39c0 bytes 604e03f9
+ 00bc3a5c bytes 60ce03f9
- 00bc39a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
- 00bc39a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bc3a3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
+ 00bc3a3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bc39a0 bytes 684e43f9
+ 00bc3a3c bytes 68ce43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8187cd202cad5026f15926dc6cd1c60"></a>

### [`00bc3a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3a4c.md) → [`00bc3ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3ae8.md) _ZN8firebase13remote_config8internal35config_update_listener_registration12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "site": "00bc3a88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3aa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc3b24"
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
      "00bc3afc",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3b08",
      "READ",
      [
        "storage",
        "011266a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc3b10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bc3a8c"
      ]
    ]
  ],
  "added": [
    [
      "00bc3afc",
      "READ",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3b08",
      "READ",
      [
        "storage",
        "011267a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc3b10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3b28"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3a4c.md#insn-00bc3a64) · [`00bc3a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3a4c.md#insn-00bc3a88) · [`00bc3a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3a4c.md#insn-00bc3a90)
- 新版 [`00bc3b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3ae8.md#insn-00bc3b00)

~~~diff
- 00bc3a64 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc3a64 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bc3b00 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bc3b00 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bc3a64 bytes 410200b4
+ 00bc3b00 bytes 410200b4
- 00bc3a88 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc3a88 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc3a88 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6a0:8"]]
- 00bc3a88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc3a88 bytes bf821a39
- 00bc3a90 ["INT_ADD", "register:40f0:8", ["const:bc3a90:8", "const:4:8"]]
- 00bc3a90 ["CALL", null, ["callee:00c5b030:8"]]
- 00bc3a90 bytes 345d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8878d5c8f5c2587b8bb4369ca645a884"></a>

### [`00bc3abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3abc.md) → [`00bc3b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3b58.md) _ZN8firebase13remote_config8internal35config_update_listener_registration14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

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
      "site": "00bc3afc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc3b98"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3ad8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc3ad0",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc3ad8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3b9c"
      ]
    ],
    [
      "unmatched:00bc3ae0",
      "PARAM",
      [
        "storage",
        "002a982f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc3b6c",
      "READ",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3b74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3b9c"
      ]
    ],
    [
      "00bc3b7c",
      "PARAM",
      [
        "storage",
        "002a985e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3abc.md#insn-00bc3ad8) · [`00bc3af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3abc.md#insn-00bc3af4) · [`00bc3afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3abc.md#insn-00bc3afc)
- 新版 [`00bc3b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3b58.md#insn-00bc3b90)

~~~diff
- 00bc3ad8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc3ad8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bc3ad8 bytes 410100b5
- 00bc3af4 ["INT_ADD", "register:40f0:8", ["const:bc3af4:8", "const:4:8"]]
- 00bc3af4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc3b90 ["INT_ADD", "register:40f0:8", ["const:bc3b90:8", "const:4:8"]]
+ 00bc3b90 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc3af4 bytes 075d0294
+ 00bc3b90 bytes 145d0294
- 00bc3afc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:698:8"]]
- 00bc3afc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc3afc bytes 804e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c72a6587195d29424418e8685ad1f7b"></a>

### [`00bc3b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3b2c.md) → [`00bc3bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3bc8.md) _ZN8firebase13remote_config8internal35config_update_listener_registration11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00bc3be4",
      "incomplete_value": false,
      "site": "00bc3be8",
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
            "const:30b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3b48",
      "incomplete_value": false,
      "site": "00bc3b4c",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc3bf4",
      "incomplete_value": true,
      "site": "00bc3c00",
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
      "definition_site": "00bc3b58",
      "incomplete_value": true,
      "site": "00bc3b64",
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
      "00bc3be4",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bc3bf4",
      "DATA",
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
      "00bc3be4",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bc3bf4",
      "DATA",
      [
        "storage",
        "011267a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3b2c.md#insn-00bc3b4c) · [`00bc3b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3b2c.md#insn-00bc3b48) · [`00bc3b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3b2c.md#insn-00bc3b54)
- 新版 [`00bc3be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3bc8.md#insn-00bc3be8) · [`00bc3be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3bc8.md#insn-00bc3be4) · [`00bc3bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3bc8.md#insn-00bc3bf0)

~~~diff
- 00bc3b4c ["INT_ADD", "register:40f0:8", ["const:bc3b4c:8", "const:4:8"]]
- 00bc3b4c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bc3be8 ["INT_ADD", "register:40f0:8", ["const:bc3be8:8", "const:4:8"]]
+ 00bc3be8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bc3b4c bytes 2d5d0294
+ 00bc3be8 bytes 3a5d0294
- 00bc3b48 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00bc3b48 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc3b48 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc3b48 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc3be4 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bc3be4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc3be4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc3be4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc3b48 bytes 009c0d91
+ 00bc3be4 bytes 002c0c91
- 00bc3b54 ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 00bc3b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc3b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc3b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc3bf0 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 00bc3bf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc3bf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc3bf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc3b54 bytes 08a11a91
+ 00bc3bf0 bytes 08a11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd868b5ab9e2658559b77425ebd7074a"></a>

### [`00bc3b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3b68.md) → [`00bc3c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3c04.md) _ZN8firebase13remote_config8internal35config_update_listener_registration13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bc3ba8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc3c44"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc3b84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc3b7c",
      "READ",
      [
        "storage",
        "01126698",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bc3b84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3c48"
      ]
    ],
    [
      "unmatched:00bc3b8c",
      "PARAM",
      [
        "storage",
        "002a982f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc3c18",
      "READ",
      [
        "storage",
        "01126798",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc3c20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc3c48"
      ]
    ],
    [
      "00bc3c28",
      "PARAM",
      [
        "storage",
        "002a985e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3b68.md#insn-00bc3b84) · [`00bc3ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3b68.md#insn-00bc3ba0) · [`00bc3ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3b68.md#insn-00bc3ba8)
- 新版 [`00bc3c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3c04.md#insn-00bc3c3c)

~~~diff
- 00bc3b84 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bc3b84 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bc3b84 bytes 410100b5
- 00bc3ba0 ["INT_ADD", "register:40f0:8", ["const:bc3ba0:8", "const:4:8"]]
- 00bc3ba0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bc3c3c ["INT_ADD", "register:40f0:8", ["const:bc3c3c:8", "const:4:8"]]
+ 00bc3c3c ["CALL", null, ["callee:00c5afe0:8"]]
- 00bc3ba0 bytes dc5c0294
+ 00bc3c3c bytes e95c0294
- 00bc3ba8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:698:8"]]
- 00bc3ba8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc3ba8 bytes 804e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9708efc8d9750291208d9273372698f"></a>

### [`00bc3bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3bd8.md) → [`00bc3c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3c74.md) _ZN8firebase13remote_config8internal35config_update_listener_registration10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00bc3c90",
      "incomplete_value": false,
      "site": "00bc3c94",
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
            "const:54d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3bf4",
      "incomplete_value": false,
      "site": "00bc3bf8",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bc3ca0",
      "incomplete_value": true,
      "site": "00bc3cac",
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
      "definition_site": "00bc3c04",
      "incomplete_value": true,
      "site": "00bc3c10",
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
      "00bc3c90",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bc3ca0",
      "DATA",
      [
        "storage",
        "011266b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc3c90",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bc3ca0",
      "DATA",
      [
        "storage",
        "011267b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3bd8.md#insn-00bc3bf8) · [`00bc3bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3bd8.md#insn-00bc3bf4) · [`00bc3c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3bd8.md#insn-00bc3c00)
- 新版 [`00bc3c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3c74.md#insn-00bc3c94) · [`00bc3c90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3c74.md#insn-00bc3c90) · [`00bc3c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3c74.md#insn-00bc3c9c)

~~~diff
- 00bc3bf8 ["INT_ADD", "register:40f0:8", ["const:bc3bf8:8", "const:4:8"]]
- 00bc3bf8 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bc3c94 ["INT_ADD", "register:40f0:8", ["const:bc3c94:8", "const:4:8"]]
+ 00bc3c94 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bc3bf8 bytes 025d0294
+ 00bc3c94 bytes 0f5d0294
- 00bc3bf4 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00bc3bf4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc3bf4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc3bf4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc3c90 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bc3c90 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc3c90 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc3c90 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc3bf4 bytes 00781491
+ 00bc3c90 bytes 00341591
- 00bc3c00 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 00bc3c00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc3c00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc3c00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc3c9c ["COPY", "tmp:0:8", ["const:7b0:8"]]
+ 00bc3c9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc3c9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc3c9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc3c00 bytes 08c11a91
+ 00bc3c9c bytes 08c11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e57cff20593209d673dce08feeda4f6"></a>

### [`00bc3c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3c1c.md) → [`00bc3cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3cb8.md) _ZN8firebase13remote_config8internal20RemoteConfigInternalC1ERKNS_3AppE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d870.md) · 呼出先 22件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5d940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d940.md) · 呼出先 22件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 44.21% / 新版 44.21%

CFGの説明率　旧版 26.62% / 新版 26.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 31件, `unresolved_branch_alignment` 29件, `unresolved_call_alignment` 37件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 25件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 6件, `store_condition` 1件, `store_destination` 5件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc3d40",
      "incomplete_value": true,
      "site": "00bc3d40",
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
                "const:a48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3ca4",
      "incomplete_value": true,
      "site": "00bc3ca4",
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
                "const:978:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc3d40",
      "incomplete_value": true,
      "site": "00bc3d40",
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
            "const:4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3ca4",
      "incomplete_value": true,
      "site": "00bc3ca4",
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
            "const:4:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc3e44",
      "incomplete_value": true,
      "site": "00bc3e5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3da8",
      "incomplete_value": true,
      "site": "00bc3dc0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc3d20",
      "READ",
      [
        "storage",
        "00c9b978",
        null,
        "pointer"
      ]
    ],
    [
      "00bc3d40",
      "DATA",
      [
        "storage",
        "011266b8",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ],
    [
      "00bc3d40",
      "DATA",
      [
        "storage",
        "011266bc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc3d20",
      "READ",
      [
        "storage",
        "00c9ba48",
        null,
        "pointer"
      ]
    ],
    [
      "00bc3d40",
      "DATA",
      [
        "storage",
        "011267b8",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ],
    [
      "00bc3d40",
      "DATA",
      [
        "storage",
        "011267bc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc3e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3c1c.md#insn-00bc3e24) · [`00bc3e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3c1c.md#insn-00bc3e38) · [`00bc3e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc3/00bc3c1c.md#insn-00bc3e94)
- 新版 [`00bc3ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3cb8.md#insn-00bc3ec0) · [`00bc3ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3cb8.md#insn-00bc3ed4) · [`00bc3f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc3/00bc3cb8.md#insn-00bc3f30)

~~~diff
- 00bc3e24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:658:8"]]
- 00bc3e24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
+ 00bc3ec0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:758:8"]]
+ 00bc3ec0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bc3e24 bytes 012d03f9
+ 00bc3ec0 bytes 01ad03f9
- 00bc3e38 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 00bc3e38 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00bc3e38 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00bc3e38 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00bc3ed4 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 00bc3ed4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00bc3ed4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00bc3ed4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00bc3e38 bytes 42801e91
+ 00bc3ed4 bytes 42c02191
- 00bc3e94 ["INT_ADD", "register:40f0:8", ["const:bc3e94:8", "const:4:8"]]
- 00bc3e94 ["CALL", null, ["callee:00c5b030:8"]]
+ 00bc3f30 ["INT_ADD", "register:40f0:8", ["const:bc3f30:8", "const:4:8"]]
+ 00bc3f30 ["CALL", null, ["callee:00c5b030:8"]]
- 00bc3e94 bytes 335c0294
+ 00bc3f30 bytes 405c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35881f0895ffeb234e63919b3a025378"></a>

### [`00bc4804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4804.md) → [`00bc48a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc48a0.md) _ZNSt6__ndk16vectorIN8firebase8internal12EmbeddedFileENS_9allocatorIS3_EEEC2ERKS6_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d970.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)
- 新版 呼出元 1件 [`00c5da40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da40.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 40.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_condition` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc484c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bc48e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00bc484c"
      ],
      [
        "FALL_THROUGH",
        "00bc48e8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bc48e4",
      "incomplete_value": true,
      "site": "00bc48fc",
      "value": [
        "INT_LESSEQUAL",
        "1",
        [
          [
            "INT_OR",
            "8",
            [
              "INT_AND",
              [
                "leaf",
                "const:aaa000000000000:8"
              ]
            ]
          ],
          [
            "INT_MULT",
            "8",
            [
              "INT_SRIGHT",
              "INT_OR"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc4848",
      "incomplete_value": true,
      "site": "00bc4860",
      "value": [
        "INT_LESSEQUAL",
        "1",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:40b0:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc484c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc494c"
      ]
    ]
  ],
  "added": [
    [
      "00bc48e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc494c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc484c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4804.md#insn-00bc484c) · [`00bc4840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4804.md#insn-00bc4840)
- 新版 [`00bc48e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc48a0.md#insn-00bc48e8)

~~~diff
- 00bc484c ["CBRANCH", null, ["local:b8:8", "register:102:1"]]
- 00bc484c bytes 22030054
+ 00bc48e8 ["CBRANCH", null, ["local:b8:8", "register:102:1"]]
+ 00bc48e8 bytes 22030054
- 00bc4840 ["INT_AND", "register:4040:8", ["register:4040:8", "const:ffffffffffff0000:8"]]
- 00bc4840 ["INT_OR", "register:4040:8", ["register:4040:8", "const:aaab:8"]]
- 00bc4840 bytes 685595f2
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-468b703d5ae592374eddf4d592a1e9d9"></a>

### [`00bc4b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4b3c.md) → [`00bc4bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4bd8.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal7CleanupEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d800.md) · 呼出先 7件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5afd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5afd0.md)
- 新版 呼出元 1件 [`00c5d8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d8d0.md) · 呼出先 7件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0a0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.36% / 新版 26.36%

CFGの説明率　旧版 6.41% / 新版 6.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件, `unresolved_branch_alignment` 18件, `unresolved_call_alignment` 28件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 19件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc4c0c",
      "incomplete_value": true,
      "site": "00bc4c0c",
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
                "const:a48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc4b70",
      "incomplete_value": true,
      "site": "00bc4b70",
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
                "const:978:8"
              ]
            ]
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
      "definition_site": "00bc4c0c",
      "incomplete_value": true,
      "site": "00bc4c0c",
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
            "const:4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc4b70",
      "incomplete_value": true,
      "site": "00bc4b70",
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
            "const:4:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc4bf0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc4bf8",
      "READ",
      [
        "storage",
        "00c9b978",
        null,
        "pointer"
      ]
    ],
    [
      "00bc4c08",
      "PARAM",
      [
        "storage",
        "011266bc",
        null,
        null
      ]
    ],
    [
      "00bc4c0c",
      "DATA",
      [
        "storage",
        "011266b8",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00bc4bf8",
      "READ",
      [
        "storage",
        "00c9ba48",
        null,
        "pointer"
      ]
    ],
    [
      "00bc4c08",
      "PARAM",
      [
        "storage",
        "011267bc",
        null,
        null
      ]
    ],
    [
      "00bc4c0c",
      "DATA",
      [
        "storage",
        "011267b8",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4b3c.md#insn-00bc4b74) · [`00bc4bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4b3c.md#insn-00bc4bc0) · [`00bc4bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4b3c.md#insn-00bc4bf0)
- 新版 [`00bc4c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4bd8.md#insn-00bc4c10) · [`00bc4c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4bd8.md#insn-00bc4c5c)

~~~diff
- 00bc4b74 ["INT_ADD", "register:40f0:8", ["const:bc4b74:8", "const:4:8"]]
- 00bc4b74 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bc4c10 ["INT_ADD", "register:40f0:8", ["const:bc4c10:8", "const:4:8"]]
+ 00bc4c10 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bc4b74 bytes a3570294
+ 00bc4c10 bytes b0570294
- 00bc4bc0 ["INT_ADD", "register:40f0:8", ["const:bc4bc0:8", "const:4:8"]]
- 00bc4bc0 ["CALL", null, ["callee:00c5b150:8"]]
+ 00bc4c5c ["INT_ADD", "register:40f0:8", ["const:bc4c5c:8", "const:4:8"]]
+ 00bc4c5c ["CALL", null, ["callee:00c5b150:8"]]
- 00bc4bc0 bytes 30590294
+ 00bc4c5c bytes 3d590294
- 00bc4bf0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bc4bf0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bc4bf0 ["INT_ADD", "tmp:2:8", ["register:40b0:8", "const:660:8"]]
- 00bc4bf0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bc4bf0 bytes df821939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-154c31e216f087c4bbc4699dd9c40a40"></a>

### [`00bc4f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4f2c.md) → [`00bc4fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4fc8.md) _ZN8firebase13remote_config8internal25EnsureInitializedCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc56d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc56d4.md) · 呼出先 6件 [`00bc505c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc505c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)
- 新版 呼出元 1件 [`00bc5770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5770.md) · 呼出先 6件 [`00bc50f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc50f8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.92% / 新版 85.92%

CFGの説明率　旧版 69.57% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc4f90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc4f94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc502c"
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
      "unmatched:00bc4f84",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5aed0"
      ]
    ],
    [
      "unmatched:00bc4f88",
      "READ",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc4f8c",
      "READ",
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
      "00bc5020",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5aed0"
      ]
    ],
    [
      "00bc5024",
      "READ",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "00bc5028",
      "READ",
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

- 旧版 [`00bc4f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4f2c.md#insn-00bc4f84) · [`00bc4f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4f2c.md#insn-00bc4f90) · [`00bc4f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4f2c.md#insn-00bc4f94)

~~~diff
- 00bc4f84 ["INT_ADD", "register:40f0:8", ["const:bc4f84:8", "const:4:8"]]
- 00bc4f84 ["CALL", null, ["callee:00c5aed0:8"]]
- 00bc4f84 bytes 9f570294
- 00bc4f90 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00bc4f90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00bc4f90 bytes e00f803d
- 00bc4f94 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00bc4f94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bc4f94 bytes e82300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dfe614bd9ff50cb0996b1aed35e2b67"></a>

### [`00bc505c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc505c.md) → [`00bc50f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc50f8.md) FUN_00bc50f8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bc4f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4f2c.md) [`00bc9174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9174.md) · 呼出先 4件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`0058f59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f59c.md) [`00c5ade0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ade0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 2件 [`00bc4fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4fc8.md) [`00bc9210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9210.md) · 呼出先 4件 [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`0058f5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f5dc.md) [`00c5aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aeb0.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.67% / 新版 83.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc5114",
      "incomplete_value": true,
      "site": "00bc5124",
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
                "const:668:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5078",
      "incomplete_value": true,
      "site": "00bc5088",
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
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc5130",
      "incomplete_value": true,
      "site": "00bc513c",
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
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5094",
      "incomplete_value": true,
      "site": "00bc50a0",
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
                "const:578:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc5194",
      "incomplete_value": false,
      "site": "00bc5198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:c81:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc50f8",
      "incomplete_value": false,
      "site": "00bc50fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:c41:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc5114",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc5130",
      "READ",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc5150",
      "READ",
      [
        "storage",
        "01126580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc5114",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc5130",
      "READ",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc5150",
      "READ",
      [
        "storage",
        "01126680",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc505c.md#insn-00bc5088) · [`00bc50a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc505c.md#insn-00bc50a0) · [`00bc50fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc505c.md#insn-00bc50fc)
- 新版 [`00bc5124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc50f8.md#insn-00bc5124) · [`00bc513c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc50f8.md#insn-00bc513c) · [`00bc5198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc50f8.md#insn-00bc5198)

~~~diff
- 00bc5088 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc5088 ["INT_ADD", "register:40f0:8", ["const:bc5088:8", "const:4:8"]]
- 00bc5088 ["CALLIND", null, ["register:0:8"]]
+ 00bc5124 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc5124 ["INT_ADD", "register:40f0:8", ["const:bc5124:8", "const:4:8"]]
+ 00bc5124 ["CALLIND", null, ["register:0:8"]]
- 00bc5088 bytes 00013fd6
+ 00bc5124 bytes 00013fd6
- 00bc50a0 ["INT_ADD", "register:40f0:8", ["const:bc50a0:8", "const:4:8"]]
- 00bc50a0 ["CALL", null, ["callee:0058f5dc:8"]]
+ 00bc513c ["INT_ADD", "register:40f0:8", ["const:bc513c:8", "const:4:8"]]
+ 00bc513c ["CALL", null, ["callee:0058f5dc:8"]]
- 00bc50a0 bytes 3f29e797
+ 00bc513c bytes 2829e797
- 00bc50fc ["INT_ADD", "register:40f0:8", ["const:bc50fc:8", "const:4:8"]]
- 00bc50fc ["CALL", null, ["callee:00c5aeb0:8"]]
+ 00bc5198 ["INT_ADD", "register:40f0:8", ["const:bc5198:8", "const:4:8"]]
+ 00bc5198 ["CALL", null, ["callee:00c5aeb0:8"]]
- 00bc50fc bytes 39570294
+ 00bc5198 bytes 46570294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db4c99f51bc9002b9006621c5b594f89"></a>

### [`00bc53d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc53d8.md) → [`00bc5474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5474.md) _ZN8firebase13remote_config8internal19SetDefaultsCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bc6380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6380.md) [`00bc6618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6618.md) [`00bc6d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc6/00bc6d2c.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5d8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d8c0.md)
- 新版 呼出元 3件 [`00bc641c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc641c.md) [`00bc66b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc66b4.md) [`00bc6dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc6dc8.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5d990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d990.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.47% / 新版 92.47%

CFGの説明率　旧版 55.26% / 新版 52.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc5474"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc5484"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bc5510"
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
      "unmatched:00bc5474",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc556c"
      ]
    ],
    [
      "unmatched:00bc5484",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc5558"
      ]
    ]
  ],
  "added": [
    [
      "00bc5510",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc556c"
      ]
    ],
    [
      "00bc5520",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc5558"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc53d8.md#insn-00bc5474) · [`00bc5484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc53d8.md#insn-00bc5484) · [`00bc54ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc53d8.md#insn-00bc54ac)
- 新版 [`00bc5548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5474.md#insn-00bc5548)

~~~diff
- 00bc5474 ["INT_EQUAL", "tmp:0:1", ["register:40c8:8", "const:0:8"]]
- 00bc5474 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00bc5474 bytes f90200b4
- 00bc5484 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00bc5484 bytes c0010054
- 00bc54ac ["INT_ADD", "register:40f0:8", ["const:bc54ac:8", "const:4:8"]]
- 00bc54ac ["CALL", null, ["callee:00c57f80:8"]]
+ 00bc5548 ["INT_ADD", "register:40f0:8", ["const:bc5548:8", "const:4:8"]]
+ 00bc5548 ["CALL", null, ["callee:00c57f80:8"]]
- 00bc54ac bytes 814a0294
+ 00bc5548 bytes 8e4a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a0c4f24df16a3b96c598ca40e134658"></a>

### [`00bc56d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc56d4.md) → [`00bc5770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5770.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal17EnsureInitializedEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d740.md) · 呼出先 15件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bc4f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc4f2c.md) [`00bc9c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9c14.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c5d810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d810.md) · 呼出先 15件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bc4fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4fc8.md) [`00bc9cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9cb0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.19% / 新版 99.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc57b4",
      "incomplete_value": true,
      "site": "00bc57c8",
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
                "const:a58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5718",
      "incomplete_value": true,
      "site": "00bc572c",
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
                "const:988:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc57f0",
      "incomplete_value": true,
      "site": "00bc57f8",
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
                "const:590:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5754",
      "incomplete_value": true,
      "site": "00bc575c",
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
                "const:490:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc581c",
      "incomplete_value": false,
      "site": "00bc5830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:e2c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5780",
      "incomplete_value": false,
      "site": "00bc5794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:dec:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc57b4",
      "READ",
      [
        "storage",
        "00c9b988",
        null,
        "pointer"
      ]
    ],
    [
      "00bc57b4",
      "PARAM",
      [
        "storage",
        "00bc9c14",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_13remote_config10ConfigInfoEEEvPv",
        null
      ]
    ],
    [
      "00bc57f0",
      "READ",
      [
        "storage",
        "01126490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc57b4",
      "READ",
      [
        "storage",
        "00c9ba58",
        null,
        "pointer"
      ]
    ],
    [
      "00bc57b4",
      "PARAM",
      [
        "storage",
        "00bc9cb0",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_13remote_config10ConfigInfoEEEvPv",
        null
      ]
    ],
    [
      "00bc57f0",
      "READ",
      [
        "storage",
        "01126590",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc572c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc56d4.md#insn-00bc572c) · [`00bc575c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc56d4.md#insn-00bc575c) · [`00bc5794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc5/00bc56d4.md#insn-00bc5794)
- 新版 [`00bc57c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5770.md#insn-00bc57c8) · [`00bc57f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5770.md#insn-00bc57f8) · [`00bc5830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5770.md#insn-00bc5830)

~~~diff
- 00bc572c ["INT_ADD", "register:40f0:8", ["const:bc572c:8", "const:4:8"]]
- 00bc572c ["CALL", null, ["callee:00c5af10:8"]]
+ 00bc57c8 ["INT_ADD", "register:40f0:8", ["const:bc57c8:8", "const:4:8"]]
+ 00bc57c8 ["CALL", null, ["callee:00c5af10:8"]]
- 00bc572c bytes c5550294
+ 00bc57c8 bytes d2550294
- 00bc575c ["INT_ADD", "register:40f0:8", ["const:bc575c:8", "const:4:8"]]
- 00bc575c ["CALL", null, ["callee:00497874:8"]]
+ 00bc57f8 ["INT_ADD", "register:40f0:8", ["const:bc57f8:8", "const:4:8"]]
+ 00bc57f8 ["CALL", null, ["callee:00497874:8"]]
- 00bc575c bytes 3648e397
+ 00bc57f8 bytes 1f48e397
- 00bc5794 ["INT_ADD", "register:40f0:8", ["const:bc5794:8", "const:4:8"]]
- 00bc5794 ["CALL", null, ["callee:00c5d9c0:8"]]
+ 00bc5830 ["INT_ADD", "register:40f0:8", ["const:bc5830:8", "const:4:8"]]
+ 00bc5830 ["CALL", null, ["callee:00c5d9c0:8"]]
- 00bc5794 bytes 57600294
+ 00bc5830 bytes 64600294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

