# v16.0.2 → v16.0.3 · 命令位置の検査未完了 (5)

[一覧の目次](README.md)

<a id="compare-aa5718c86692bc837b66436d9fcc6884"></a>

### [`006a3a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a3/006a3a10.md) → [`006a3dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a3/006a3dc0.md) FUN_006a3dc0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "006a3a1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a3a1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006a3dcc"
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
      "unmatched:006a3a1c",
      "DATA",
      [
        "storage",
        "00c75a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006a3dcc",
      "DATA",
      [
        "storage",
        "00c76a20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a3a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a3/006a3a10.md#insn-006a3a1c) · [`006a3a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a3/006a3a10.md#insn-006a3a20)
- 新版 [`006a3dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a3/006a3dc0.md#insn-006a3dcc)

~~~diff
- 006a3a1c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 006a3a1c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 006a3a1c ["COPY", "tmp:2:8", ["register:4008:8"]]
- 006a3a1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006a3a1c bytes 292000a9
- 006a3a20 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006a3a20 ["RETURN", null, ["register:0:8"]]
- 006a3a20 bytes c0035fd6
+ 006a3dcc ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 006a3dcc ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 006a3dcc ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 006a3dcc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 006a3dcc bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e6e0ff7d65a90b7a662a4ff9c4b4afb"></a>

### [`006a4dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a4/006a4dc8.md) → [`006a5178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a5/006a5178.md) FUN_006a5178

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 2件 [`00480bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480bd0.md) [`00480c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480c28.md)
- 新版 呼出元 1件 [`00a2c310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2c/00a2c310.md) · 呼出先 2件 [`00480ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480ef0.md) [`00480f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480f48.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 56.00% / 新版 53.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006a4e74"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006a4ee0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "006a5224"
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
      "unmatched:006a4e74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a521c"
      ]
    ],
    [
      "unmatched:006a4ee0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a5280"
      ]
    ],
    [
      "unmatched:006a4ee4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "006a51c8"
      ]
    ]
  ],
  "added": [
    [
      "006a5224",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a521c"
      ]
    ],
    [
      "006a5290",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a5280"
      ]
    ],
    [
      "006a5294",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "006a51c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a4e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a4/006a4dc8.md#insn-006a4e74) · [`006a4ee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a4/006a4dc8.md#insn-006a4ee0)
- 新版 [`006a5224`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a5/006a5178.md#insn-006a5224)

~~~diff
- 006a4e74 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 006a4e74 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 006a4e74 bytes c9ffffb5
- 006a4ee0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006a4ee0 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 006a4ee0 bytes 81ffff54
+ 006a5224 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 006a5224 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 006a5224 bytes c9ffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bd359eb1b999e153ddd64c6e6f90606"></a>

### [`006a5308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a5/006a5308.md) → [`006a56b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a5/006a56b8.md) FUN_006a56b8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) [`0090cca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090c/0090cca8.md) [`0090dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090d/0090dd50.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 3件 [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) [`0090dc54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0090d/0090dc54.md) [`0090ecfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0090e/0090ecfc.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 79.31% / 新版 85.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a531c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a531c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006a56cc"
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
      "unmatched:006a531c",
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
      "006a56cc",
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

- 旧版 [`006a531c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a5/006a5308.md#insn-006a531c) · [`006a530c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a5/006a5308.md#insn-006a530c)
- 新版 [`006a56cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a5/006a56b8.md#insn-006a56cc) · [`006a56bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a5/006a56b8.md#insn-006a56bc)

~~~diff
- 006a531c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 006a531c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 006a531c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 006a531c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006a531c bytes f44f03a9
+ 006a56cc ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 006a56cc ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 006a56cc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
+ 006a56cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 006a56cc bytes f44f03a9
- 006a530c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 006a530c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 006a56bc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 006a56bc ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 006a530c bytes e80300b4
+ 006a56bc bytes e80300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1371a51258f951dc6380622bb8e27bc"></a>

### [`006a5410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a5/006a5410.md) → [`006a57c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a5/006a57c0.md) FUN_006a57c0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) [`0090cca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090c/0090cca8.md) [`0090dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090d/0090dd50.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 3件 [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) [`0090dc54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0090d/0090dc54.md) [`0090ecfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0090e/0090ecfc.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 79.31% / 新版 82.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a54d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a54dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006a5888"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`006a54d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a5/006a5410.md#insn-006a54d8) · [`006a54dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a5/006a5410.md#insn-006a54dc)
- 新版 [`006a5888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a5/006a57c0.md#insn-006a5888)

~~~diff
- 006a54d8 ["INT_ADD", "register:4048:8", ["register:4048:8", "const:38:8"]]
- 006a54d8 ["STORE", null, ["const:1b1:8", "register:4048:8", "register:5000:16"]]
- 006a54d8 bytes 208d833c
- 006a54dc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:30:8"]]
- 006a54dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 006a54dc bytes 091800f9
+ 006a5888 ["INT_ADD", "register:4048:8", ["register:4048:8", "const:38:8"]]
+ 006a5888 ["STORE", null, ["const:1b1:8", "register:4048:8", "register:5000:16"]]
+ 006a5888 bytes 208d833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6532b30584db4ad433570376c986ff1"></a>

### [`006a5528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a5/006a5528.md) → [`006a58d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a5/006a58d8.md) FUN_006a58d8

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009d3b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d3/009d3b48.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`009d4af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d4/009d4af4.md) · 呼出先 3件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.57% / 新版 98.57%

CFGの説明率　旧版 66.10% / 新版 65.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006a5590"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006a56a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "006a5940"
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
      "unmatched:006a5590",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a59a0"
      ]
    ],
    [
      "unmatched:006a56a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a5a3c"
      ]
    ]
  ],
  "added": [
    [
      "006a5940",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a59a0"
      ]
    ],
    [
      "006a5a54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a5a3c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a5590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a5/006a5528.md#insn-006a5590) · [`006a56a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a5/006a5528.md#insn-006a56a4)
- 新版 [`006a5940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a5/006a58d8.md#insn-006a5940)

~~~diff
- 006a5590 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 006a5590 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 006a5590 bytes 080300b4
- 006a56a4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006a56a4 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 006a56a4 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 006a56a4 ["CBRANCH", null, ["local:b28:8", "tmp:2:1"]]
- 006a56a4 bytes 4cffff54
+ 006a5940 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 006a5940 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
+ 006a5940 bytes 080300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4f586bc1e90685217330211ae2531c4"></a>

### [`006a61e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a61e4.md) → [`006a6594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a6/006a6594.md) FUN_006a6594

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`006a5758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a5/006a5758.md) [`006a61e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a61e4.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 3件 [`006a61e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a61e4.md) [`006a6234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6234.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`006a5b08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a5/006a5b08.md) [`006a6594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a6/006a6594.md) [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) · 呼出先 3件 [`006a6594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a6/006a6594.md) [`006a65e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a6/006a65e4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006a65b0",
      "incomplete_value": true,
      "site": "006a65b4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4008:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006a6200",
      "incomplete_value": true,
      "site": "006a6204",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "006a6218",
      "incomplete_value": true,
      "site": "006a621c",
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
            "const:28:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "006a6214",
      "incomplete_value": true,
      "site": "006a621c",
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`006a6204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a61e4.md#insn-006a6204) · [`006a621c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a61e4.md#insn-006a621c) · [`006a6200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a61e4.md#insn-006a6200)
- 新版 [`006a65b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a6/006a6594.md#insn-006a65b4) · [`006a65cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a6/006a6594.md#insn-006a65cc)

~~~diff
- 006a6204 ["INT_ADD", "register:40f0:8", ["const:6a6204:8", "const:4:8"]]
- 006a6204 ["CALL", null, ["local:b0:8"]]
+ 006a65b4 ["INT_ADD", "register:40f0:8", ["const:6a65b4:8", "const:4:8"]]
+ 006a65b4 ["CALL", null, ["local:b0:8"]]
- 006a6204 bytes f8ffff97
+ 006a65b4 bytes f8ffff97
- 006a621c ["INT_ADD", "register:40f0:8", ["const:6a621c:8", "const:4:8"]]
- 006a621c ["CALL", null, ["callee:006a65e4:8"]]
+ 006a65cc ["INT_ADD", "register:40f0:8", ["const:6a65cc:8", "const:4:8"]]
+ 006a65cc ["CALL", null, ["callee:006a65e4:8"]]
- 006a621c bytes 06000094
+ 006a65cc bytes 06000094
- 006a6200 ["COPY", "register:4008:8", ["register:4040:8"]]
- 006a6200 bytes e10308aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f35c290cd85d397af10e110398985ad0"></a>

### [`006a6e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6e5c.md) → [`006a720c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a7/006a720c.md) FUN_006a720c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006a7518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a7/006a7518.md) · 呼出先 4件 [`008116c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/008116c8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b2fa54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2fa54.md) [`00b3bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf30.md)
- 新版 呼出元 1件 [`006a78c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a7/006a78c8.md) · 呼出先 4件 [`0081262c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/0081262c.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00b30a48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b30/00b30a48.md) [`00b3cf24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cf24.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.54% / 新版 91.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006a7350",
      "value": [
        "leaf",
        "ram:81262c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006a6fa0",
      "value": [
        "leaf",
        "ram:8116c8:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006a7360",
      "value": [
        "leaf",
        "ram:81262c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006a6fb0",
      "value": [
        "leaf",
        "ram:8116c8:8"
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006a7374",
      "value": [
        "leaf",
        "ram:81262c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006a6fc4",
      "value": [
        "leaf",
        "ram:8116c8:8"
      ]
    },
    "ordinal": 10,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006a7350",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008116c8"
      ]
    ],
    [
      "006a7360",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008116c8"
      ]
    ],
    [
      "006a7374",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008116c8"
      ]
    ]
  ],
  "added": [
    [
      "006a7350",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081262c"
      ]
    ],
    [
      "006a7360",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081262c"
      ]
    ],
    [
      "006a7374",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081262c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a6fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6e5c.md#insn-006a6fa0) · [`006a6fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6e5c.md#insn-006a6fb0) · [`006a6fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6e5c.md#insn-006a6fc4)
- 新版 [`006a7350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a7/006a720c.md#insn-006a7350) · [`006a7360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a7/006a720c.md#insn-006a7360) · [`006a7374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a7/006a720c.md#insn-006a7374)

~~~diff
- 006a6fa0 ["INT_ADD", "register:40f0:8", ["const:6a6fa0:8", "const:4:8"]]
- 006a6fa0 ["CALL", null, ["ram:8116c8:8"]]
+ 006a7350 ["INT_ADD", "register:40f0:8", ["const:6a7350:8", "const:4:8"]]
+ 006a7350 ["CALL", null, ["ram:81262c:8"]]
- 006a6fa0 bytes caa90594
+ 006a7350 bytes b7ac0594
- 006a6fb0 ["INT_ADD", "register:40f0:8", ["const:6a6fb0:8", "const:4:8"]]
- 006a6fb0 ["CALL", null, ["ram:8116c8:8"]]
+ 006a7360 ["INT_ADD", "register:40f0:8", ["const:6a7360:8", "const:4:8"]]
+ 006a7360 ["CALL", null, ["ram:81262c:8"]]
- 006a6fb0 bytes c6a90594
+ 006a7360 bytes b3ac0594
- 006a6fc4 ["INT_ADD", "register:40f0:8", ["const:6a6fc4:8", "const:4:8"]]
- 006a6fc4 ["CALL", null, ["ram:8116c8:8"]]
+ 006a7374 ["INT_ADD", "register:40f0:8", ["const:6a7374:8", "const:4:8"]]
+ 006a7374 ["CALL", null, ["ram:81262c:8"]]
- 006a6fc4 bytes c1a90594
+ 006a7374 bytes aeac0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f81baf71cf0473ef30f79e8469b16160"></a>

### [`006a7064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a7/006a7064.md) → [`006a7414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a7/006a7414.md) FUN_006a7414

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006afd4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006af/006afd4c.md) · 呼出先 11件 [`005cc9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc9e0.md) [`00664800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664800.md) [`0071c4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c4b8.md) [`0075b97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075b97c.md) [`00811630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/00811630.md)
- 新版 呼出元 1件 [`006b00fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b0/006b00fc.md) · 呼出先 11件 [`005ccd90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cc/005ccd90.md) [`00664bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664bb0.md) [`0071c868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c868.md) [`0075bd2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075b/0075bd2c.md) [`00812594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00812/00812594.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 12件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006a7510",
      "value": [
        "leaf",
        "ram:985ae8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006a7160",
      "value": [
        "leaf",
        "ram:984b3c:8"
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006a7524",
      "value": [
        "leaf",
        "ram:812594:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006a7174",
      "value": [
        "leaf",
        "ram:811630:8"
      ]
    },
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006a7538",
      "value": [
        "leaf",
        "ram:812594:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006a7188",
      "value": [
        "leaf",
        "ram:811630:8"
      ]
    },
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006a74c4",
      "DATA",
      [
        "storage",
        "003b5258",
        null,
        "byte[83]"
      ]
    ],
    [
      "006a7510",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00984b3c"
      ]
    ],
    [
      "006a7524",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00811630"
      ]
    ]
  ],
  "added": [
    [
      "006a74c4",
      "DATA",
      [
        "storage",
        "003b5258",
        null,
        "byte[67]"
      ]
    ],
    [
      "006a7510",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00985ae8"
      ]
    ],
    [
      "006a7524",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00812594"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a7160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a7/006a7064.md#insn-006a7160) · [`006a7174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a7/006a7064.md#insn-006a7174) · [`006a7188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a7/006a7064.md#insn-006a7188)
- 新版 [`006a7510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a7/006a7414.md#insn-006a7510) · [`006a7524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a7/006a7414.md#insn-006a7524) · [`006a7538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a7/006a7414.md#insn-006a7538)

~~~diff
- 006a7160 ["INT_ADD", "register:40f0:8", ["const:6a7160:8", "const:4:8"]]
- 006a7160 ["CALL", null, ["ram:984b3c:8"]]
+ 006a7510 ["INT_ADD", "register:40f0:8", ["const:6a7510:8", "const:4:8"]]
+ 006a7510 ["CALL", null, ["ram:985ae8:8"]]
- 006a7160 bytes 77760b94
+ 006a7510 bytes 76790b94
- 006a7174 ["INT_ADD", "register:40f0:8", ["const:6a7174:8", "const:4:8"]]
- 006a7174 ["CALL", null, ["ram:811630:8"]]
+ 006a7524 ["INT_ADD", "register:40f0:8", ["const:6a7524:8", "const:4:8"]]
+ 006a7524 ["CALL", null, ["ram:812594:8"]]
- 006a7174 bytes 2fa90594
+ 006a7524 bytes 1cac0594
- 006a7188 ["INT_ADD", "register:40f0:8", ["const:6a7188:8", "const:4:8"]]
- 006a7188 ["CALL", null, ["ram:811630:8"]]
+ 006a7538 ["INT_ADD", "register:40f0:8", ["const:6a7538:8", "const:4:8"]]
+ 006a7538 ["CALL", null, ["ram:812594:8"]]
- 006a7188 bytes 2aa90594
+ 006a7538 bytes 17ac0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2a6d60f4dafaba82d45dabc141dde92"></a>

### [`006b2bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b2bb4.md) → [`006b2f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b2/006b2f64.md) FUN_006b2f64

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006b3bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b3bfc.md) · 呼出先 24件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`0046da24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046da24.md) [`0046da88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046da88.md) [`0046ee44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ee44.md)
- 新版 呼出元 1件 [`006b3fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3fac.md) · 呼出先 24件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`0046dd44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046dd44.md) [`0046dda8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046dda8.md) [`0046f164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f164.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.62% / 新版 91.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 43件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006b3430",
      "value": [
        "leaf",
        "ram:6dee9c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006b3080",
      "value": [
        "leaf",
        "ram:6deaec:8"
      ]
    },
    "ordinal": 75,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006b3440",
      "value": [
        "leaf",
        "ram:6dee9c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006b3090",
      "value": [
        "leaf",
        "ram:6deaec:8"
      ]
    },
    "ordinal": 76,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006b3450",
      "value": [
        "leaf",
        "ram:6dee9c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006b30a0",
      "value": [
        "leaf",
        "ram:6deaec:8"
      ]
    },
    "ordinal": 77,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006b3430",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006deaec"
      ]
    ],
    [
      "006b3440",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006deaec"
      ]
    ],
    [
      "006b3450",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006deaec"
      ]
    ]
  ],
  "added": [
    [
      "006b3430",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006dee9c"
      ]
    ],
    [
      "006b3440",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006dee9c"
      ]
    ],
    [
      "006b3450",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006dee9c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b2cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b2bb4.md#insn-006b2cf0) · [`006b2d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b2bb4.md#insn-006b2d00) · [`006b2d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b2bb4.md#insn-006b2d10)
- 新版 [`006b30a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b2/006b2f64.md#insn-006b30a0) · [`006b30b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b2/006b2f64.md#insn-006b30b0) · [`006b30c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b2/006b2f64.md#insn-006b30c0)

~~~diff
- 006b2cf0 ["INT_ADD", "register:40f0:8", ["const:6b2cf0:8", "const:4:8"]]
- 006b2cf0 ["CALL", null, ["callee:008524fc:8"]]
+ 006b30a0 ["INT_ADD", "register:40f0:8", ["const:6b30a0:8", "const:4:8"]]
+ 006b30a0 ["CALL", null, ["callee:008524fc:8"]]
- 006b2cf0 bytes 187a0694
+ 006b30a0 bytes 177d0694
- 006b2d00 ["INT_ADD", "register:40f0:8", ["const:6b2d00:8", "const:4:8"]]
- 006b2d00 ["CALL", null, ["callee:008524fc:8"]]
+ 006b30b0 ["INT_ADD", "register:40f0:8", ["const:6b30b0:8", "const:4:8"]]
+ 006b30b0 ["CALL", null, ["callee:008524fc:8"]]
- 006b2d00 bytes 147a0694
+ 006b30b0 bytes 137d0694
- 006b2d10 ["INT_ADD", "register:40f0:8", ["const:6b2d10:8", "const:4:8"]]
- 006b2d10 ["CALL", null, ["callee:0085c2b8:8"]]
+ 006b30c0 ["INT_ADD", "register:40f0:8", ["const:6b30c0:8", "const:4:8"]]
+ 006b30c0 ["CALL", null, ["callee:0085c2b8:8"]]
- 006b2d10 bytes 7fa10694
+ 006b30c0 bytes 7ea40694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a51063ff8f952fb69116b8f060d2e51"></a>

### [`006eeadc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ee/006eeadc.md) → [`006eee8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ee/006eee8c.md) FUN_006eee8c

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006eed04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ee/006eed04.md) · 呼出先 4件 [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`006e4440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4440.md) [`006e4b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e4/006e4b1c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 1件 [`006ef0b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ef/006ef0b4.md) · 呼出先 4件 [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`006e47f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e47f0.md) [`006e4ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006e4/006e4ecc.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.75% / 新版 92.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006eeec4",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006eeb14",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006eeed8",
      "value": [
        "leaf",
        "ram:6e4ecc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006eeb28",
      "value": [
        "leaf",
        "ram:6e4b1c:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006eeee0",
      "value": [
        "leaf",
        "ram:6e47f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006eeb30",
      "value": [
        "leaf",
        "ram:6e4440:8"
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
      "006eeec4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ],
    [
      "006eeed8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4b1c"
      ]
    ],
    [
      "006eeee0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4440"
      ]
    ]
  ],
  "added": [
    [
      "006eeec4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ],
    [
      "006eeed8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ecc"
      ]
    ],
    [
      "006eeee0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e47f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006eeb14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ee/006eeadc.md#insn-006eeb14) · [`006eeb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ee/006eeadc.md#insn-006eeb28) · [`006eeb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ee/006eeadc.md#insn-006eeb30)
- 新版 [`006eeec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ee/006eee8c.md#insn-006eeec4) · [`006eeed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ee/006eee8c.md#insn-006eeed8) · [`006eeee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ee/006eee8c.md#insn-006eeee0)

~~~diff
- 006eeb14 ["INT_ADD", "register:40f0:8", ["const:6eeb14:8", "const:4:8"]]
- 006eeb14 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006eeec4 ["INT_ADD", "register:40f0:8", ["const:6eeec4:8", "const:4:8"]]
+ 006eeec4 ["CALL", null, ["ram:6e4ecc:8"]]
- 006eeb14 bytes 02d8ff97
+ 006eeec4 bytes 02d8ff97
- 006eeb28 ["INT_ADD", "register:40f0:8", ["const:6eeb28:8", "const:4:8"]]
- 006eeb28 ["CALL", null, ["ram:6e4b1c:8"]]
+ 006eeed8 ["INT_ADD", "register:40f0:8", ["const:6eeed8:8", "const:4:8"]]
+ 006eeed8 ["CALL", null, ["ram:6e4ecc:8"]]
- 006eeb28 bytes fdd7ff97
+ 006eeed8 bytes fdd7ff97
- 006eeb30 ["INT_ADD", "register:40f0:8", ["const:6eeb30:8", "const:4:8"]]
- 006eeb30 ["CALL", null, ["ram:6e4440:8"]]
+ 006eeee0 ["INT_ADD", "register:40f0:8", ["const:6eeee0:8", "const:4:8"]]
+ 006eeee0 ["CALL", null, ["ram:6e47f0:8"]]
- 006eeb30 bytes 44d6ff97
+ 006eeee0 bytes 44d6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ab211c6dbec993d890a98adad38d484"></a>

### [`0071e3ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e3ec.md) → [`0071e79c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071e/0071e79c.md) FUN_0071e79c

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0071d254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071d/0071d254.md) [`00921b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00921/00921b38.md) [`0097da08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0097d/0097da08.md) · 呼出先 10件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`006972e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006972e8.md) [`00b3befc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3befc.md) [`00b3bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf30.md) [`00b3bf74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf74.md)
- 新版 呼出元 3件 [`0071d604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071d/0071d604.md) [`00922ae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00922/00922ae4.md) [`0097e9b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0097e/0097e9b4.md) · 呼出先 10件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00697698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697698.md) [`00b3cef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cef0.md) [`00b3cf24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cf24.md) [`00b3cf68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cf68.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.26% / 新版 94.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0071e84c",
      "DATA",
      [
        "storage",
        "00746567",
        null,
        null
      ]
    ],
    [
      "0071e864",
      "PARAM",
      [
        "storage",
        "002a4604",
        null,
        "string"
      ]
    ],
    [
      "0071e864",
      "PARAM",
      [
        "storage",
        "002a3446",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0071e864",
      "PARAM",
      [
        "storage",
        "002a46cf",
        null,
        "string"
      ]
    ],
    [
      "0071e864",
      "PARAM",
      [
        "storage",
        "002a3511",
        null,
        "string"
      ]
    ],
    [
      "0071e864",
      "PARAM",
      [
        "storage",
        "002c031a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e3ec.md#insn-0071e454) · [`0071e45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e3ec.md#insn-0071e45c) · [`0071e474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e3ec.md#insn-0071e474)
- 新版 [`0071e804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071e/0071e79c.md#insn-0071e804) · [`0071e80c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071e/0071e79c.md#insn-0071e80c) · [`0071e824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071e/0071e79c.md#insn-0071e824)

~~~diff
- 0071e454 ["INT_ADD", "register:40f0:8", ["const:71e454:8", "const:4:8"]]
- 0071e454 ["CALL", null, ["callee:00b3cf68:8"]]
+ 0071e804 ["INT_ADD", "register:40f0:8", ["const:71e804:8", "const:4:8"]]
+ 0071e804 ["CALL", null, ["callee:00b3cf68:8"]]
- 0071e454 bytes c8761094
+ 0071e804 bytes d9791094
- 0071e45c ["INT_ADD", "register:40f0:8", ["const:71e45c:8", "const:4:8"]]
- 0071e45c ["CALL", null, ["callee:00b3cf24:8"]]
+ 0071e80c ["INT_ADD", "register:40f0:8", ["const:71e80c:8", "const:4:8"]]
+ 0071e80c ["CALL", null, ["callee:00b3cf24:8"]]
- 0071e45c bytes b5761094
+ 0071e80c bytes c6791094
- 0071e474 ["INT_ADD", "register:40f0:8", ["const:71e474:8", "const:4:8"]]
- 0071e474 ["CALL", null, ["callee:00b3cef0:8"]]
+ 0071e824 ["INT_ADD", "register:40f0:8", ["const:71e824:8", "const:4:8"]]
+ 0071e824 ["CALL", null, ["callee:00b3cef0:8"]]
- 0071e474 bytes a2761094
+ 0071e824 bytes b3791094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d198e6aa41ee9c1394525ac95612af4"></a>

### [`0071e618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e618.md) → [`0071e9c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071e/0071e9c8.md) FUN_0071e9c8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0071d254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071d/0071d254.md) · 呼出先 9件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`006972e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006972e8.md) [`00b3bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf30.md) [`00b3bfbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bfbc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`0071d604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071d/0071d604.md) · 呼出先 9件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00697698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00697/00697698.md) [`00b3cf24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cf24.md) [`00b3cfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cfb0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0071ea98",
      "PARAM",
      [
        "storage",
        "002a4604",
        null,
        "string"
      ]
    ],
    [
      "0071ea98",
      "PARAM",
      [
        "storage",
        "002a3446",
        null,
        "string"
      ]
    ],
    [
      "0071ea98",
      "PARAM",
      [
        "storage",
        "002c02d0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0071ea98",
      "PARAM",
      [
        "storage",
        "002a46cf",
        null,
        "string"
      ]
    ],
    [
      "0071ea98",
      "PARAM",
      [
        "storage",
        "002a3511",
        null,
        "string"
      ]
    ],
    [
      "0071ea98",
      "PARAM",
      [
        "storage",
        "002c031a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e618.md#insn-0071e688) · [`0071e6a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e618.md#insn-0071e6a4) · [`0071e6b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e618.md#insn-0071e6b8)
- 新版 [`0071ea38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071e/0071e9c8.md#insn-0071ea38) · [`0071ea54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071e/0071e9c8.md#insn-0071ea54) · [`0071ea68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071e/0071e9c8.md#insn-0071ea68)

~~~diff
- 0071e688 ["INT_ADD", "register:40f0:8", ["const:71e688:8", "const:4:8"]]
- 0071e688 ["CALL", null, ["callee:00b3cf24:8"]]
+ 0071ea38 ["INT_ADD", "register:40f0:8", ["const:71ea38:8", "const:4:8"]]
+ 0071ea38 ["CALL", null, ["callee:00b3cf24:8"]]
- 0071e688 bytes 2a761094
+ 0071ea38 bytes 3b791094
- 0071e6a4 ["INT_ADD", "register:40f0:8", ["const:71e6a4:8", "const:4:8"]]
- 0071e6a4 ["CALL", null, ["callee:00b3cfb0:8"]]
+ 0071ea54 ["INT_ADD", "register:40f0:8", ["const:71ea54:8", "const:4:8"]]
+ 0071ea54 ["CALL", null, ["callee:00b3cfb0:8"]]
- 0071e6a4 bytes 46761094
+ 0071ea54 bytes 57791094
- 0071e6b8 ["COPY", "tmp:0:8", ["const:604:8"]]
- 0071e6b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0071e6b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0071e6b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0071ea68 ["COPY", "tmp:0:8", ["const:6cf:8"]]
+ 0071ea68 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0071ea68 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0071ea68 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0071e6b8 bytes 4a111891
+ 0071ea68 bytes 4a3d1b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ff9eb8f36c9dbad22faf65ded29d2c0"></a>

### [`00766e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00766/00766e68.md) → [`00767244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00767/00767244.md) FUN_00767244

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`007662b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00766/007662b4.md) [`007671a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/007671a0.md) [`00769d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769d30.md) · 呼出先 8件 [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00550c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c68.md) [`00550d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550d6c.md) [`00597efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597efc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 3件 [`00766690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00766/00766690.md) [`0076757c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00767/0076757c.md) [`0076a10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a10c.md) · 呼出先 8件 [`0043df04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043d/0043df04.md) [`00550f88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00550/00550f88.md) [`0055108c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00551/0055108c.md) [`0059821c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/0059821c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 84.00% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00766e84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00767260"
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
      "unmatched:00766e84",
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
      "00767260",
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

- 旧版 [`00766e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00766/00766e68.md#insn-00766e84) · [`00766e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00766/00766e68.md#insn-00766e88)
- 新版 [`00767260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00767/00767244.md#insn-00767260)

~~~diff
- 00766e84 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00766e84 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00766e84 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00766e84 bytes a8831ff8
+ 00767260 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00767260 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
+ 00767260 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00767260 bytes a8831ff8
- 00766e88 ["INT_SUB", "register:4040:8", ["register:40e8:8", "const:20:8"]]
- 00766e88 bytes a88300d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c90e71238976278329ce087b22919b18"></a>

### [`0077c0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c0b0.md) → [`0077c48c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077c48c.md) FUN_0077c48c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00682364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682364.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00682714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00682/00682714.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 57.89% / 新版 57.89%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077c0cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077c108"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0077c4a8"
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
      "unmatched:0077c0cc",
      "DATA",
      [
        "storage",
        "00c78400",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0077c0d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077c4d8"
      ]
    ],
    [
      "unmatched:0077c0dc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c54d90"
      ]
    ]
  ],
  "added": [
    [
      "0077c4a8",
      "DATA",
      [
        "storage",
        "00c793d0",
        null,
        "pointer"
      ]
    ],
    [
      "0077c4ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077c4d8"
      ]
    ],
    [
      "0077c4b8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c54d90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077c0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c0b0.md#insn-0077c0cc) · [`0077c0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c0b0.md#insn-0077c0d0) · [`0077c0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c0b0.md#insn-0077c0dc)

~~~diff
- 0077c0cc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0077c0cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0077c0cc bytes 080000f9
- 0077c0d0 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 0077c0d0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0077c0d0 bytes 740100b4
- 0077c0dc ["INT_ADD", "register:40f0:8", ["const:77c0dc:8", "const:4:8"]]
- 0077c0dc ["CALL", null, ["callee:00c54d90:8"]]
- 0077c0dc bytes 315f1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0794ce8c49cc193f20ccab5ac883ba7d"></a>

### [`0077c148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c148.md) → [`0077c524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077c524.md) FUN_0077c524

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00682364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682364.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00682714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00682/00682714.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077c164"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077c1a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0077c540"
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
      "unmatched:0077c164",
      "DATA",
      [
        "storage",
        "00c78400",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0077c178",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077c570"
      ]
    ],
    [
      "unmatched:0077c1a0",
      "DATA",
      [
        "storage",
        "00c748e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0077c540",
      "DATA",
      [
        "storage",
        "00c793d0",
        null,
        "pointer"
      ]
    ],
    [
      "0077c554",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0077c570"
      ]
    ],
    [
      "0077c57c",
      "DATA",
      [
        "storage",
        "00c758b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077c164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c148.md#insn-0077c164) · [`0077c178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c148.md#insn-0077c178) · [`0077c1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c148.md#insn-0077c1a0)

~~~diff
- 0077c164 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0077c164 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0077c164 bytes 080000f9
- 0077c178 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0077c178 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 0077c178 bytes e00000b5
- 0077c1a0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0077c1a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0077c1a0 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee3e75eebe8e43d05a74c7f04e9b5d54"></a>

### [`0077c848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c848.md) → [`0077cc24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cc24.md) FUN_0077cc24

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 41.67% / 新版 41.67%

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
      "site": "0077c848"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077c848"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077c84c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0077c848",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077c84c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077c860",
      "DATA",
      [
        "storage",
        "00c78420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0077cc24",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0077cc28",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0077cc3c",
      "DATA",
      [
        "storage",
        "00c793f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077c848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c848.md#insn-0077c848) · [`0077c84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c848.md#insn-0077c84c) · [`0077c860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c848.md#insn-0077c860)

~~~diff
- 0077c848 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0077c848 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0077c848 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0077c848 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0077c848 bytes fd7bbea9
- 0077c84c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0077c84c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0077c84c bytes f30b00f9
- 0077c860 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0077c860 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0077c860 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8f893faf367054994d5ce48ce715813"></a>

### [`0077c878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c878.md) → [`0077cc54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cc54.md) FUN_0077cc54

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f00.md) [`00c59170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59170.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077c878"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077c878"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0077c87c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0077c878",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0077c87c",
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
      "0077cc54",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0077cc58",
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

- 旧版 [`0077c878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c878.md#insn-0077c878) · [`0077c87c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0077c/0077c878.md#insn-0077c87c)
- 新版 [`0077cc54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0077c/0077cc54.md#insn-0077cc54)

~~~diff
- 0077c878 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0077c878 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0077c878 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0077c878 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0077c878 bytes fd7bbea9
- 0077c87c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0077c87c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0077c87c bytes f30b00f9
+ 0077cc54 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0077cc54 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0077cc54 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 0077cc54 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0077cc54 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49687da4fc8e31efe6e0c033244ab59f"></a>

### [`00782af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00782/00782af0.md) → [`00782ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00782/00782ecc.md) FUN_00782ecc

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00782af8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00782ed4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00782afc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00782af8",
      "DATA",
      [
        "storage",
        "00c787c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00782ed4",
      "DATA",
      [
        "storage",
        "00c79790",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00782af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00782/00782af0.md#insn-00782af8) · [`00782afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00782/00782af0.md#insn-00782afc)
- 新版 [`00782ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00782/00782ecc.md#insn-00782ed4)

~~~diff
- 00782af8 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00782af8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00782af8 bytes 280000f9
- 00782afc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00782afc ["RETURN", null, ["register:0:8"]]
- 00782afc bytes c0035fd6
+ 00782ed4 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00782ed4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00782ed4 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9934ec3fb369cbfaaca51abb22d31a53"></a>

### [`00782b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00782/00782b08.md) → [`00782ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00782/00782ee4.md) FUN_00782ee4

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 60.00% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00782b2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00782f08"
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
      "unmatched:00782b2c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00782f08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00782b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00782/00782b08.md#insn-00782b2c) · [`00782b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00782/00782b08.md#insn-00782b10)
- 新版 [`00782f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00782/00782ee4.md#insn-00782f08) · [`00782eec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00782/00782ee4.md#insn-00782eec)

~~~diff
- 00782b2c ["INT_ADD", "register:40f0:8", ["const:782b2c:8", "const:4:8"]]
- 00782b2c ["CALL", null, ["ram:47ad34:8"]]
- 00782b2c bytes 82e0f397
+ 00782f08 ["INT_ADD", "register:40f0:8", ["const:782f08:8", "const:4:8"]]
+ 00782f08 ["CALL", null, ["ram:47b054:8"]]
+ 00782f08 bytes 53e0f397
- 00782b10 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00782b10 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00782eec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00782eec ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00782b10 bytes e1010054
+ 00782eec bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-974d1989cd54b4187be4c39fd0d23566"></a>

### [`00782f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00782/00782f44.md) → [`00783320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00783/00783320.md) FUN_00783320

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

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
      "site": "00782f68"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00783344"
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
      "unmatched:00782f68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00783344",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00782f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00782/00782f44.md#insn-00782f68) · [`00782f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00782/00782f44.md#insn-00782f4c)
- 新版 [`00783344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00783/00783320.md#insn-00783344) · [`00783328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00783/00783320.md#insn-00783328)

~~~diff
- 00782f68 ["INT_ADD", "register:40f0:8", ["const:782f68:8", "const:4:8"]]
- 00782f68 ["CALL", null, ["ram:47ad34:8"]]
- 00782f68 bytes 73dff397
+ 00783344 ["INT_ADD", "register:40f0:8", ["const:783344:8", "const:4:8"]]
+ 00783344 ["CALL", null, ["ram:47b054:8"]]
+ 00783344 bytes 44dff397
- 00782f4c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00782f4c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00783328 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00783328 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00782f4c bytes e1010054
+ 00783328 bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-232038fab0f80771b340884e1958b8bd"></a>

### [`00783060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783060.md) → [`0078343c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00783/0078343c.md) FUN_0078343c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "site": "00783078"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00783454"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00783080"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00783078",
      "DATA",
      [
        "storage",
        "00c78b70",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0078307c",
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
      "00783454",
      "DATA",
      [
        "storage",
        "00c79b40",
        null,
        "undefined *"
      ]
    ],
    [
      "00783458",
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

- 旧版 [`00783078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783060.md#insn-00783078) · [`00783080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783060.md#insn-00783080)
- 新版 [`00783454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00783/0078343c.md#insn-00783454)

~~~diff
- 00783078 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00783078 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00783078 bytes 080000f9
- 00783080 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00783080 ["RETURN", null, ["register:0:8"]]
- 00783080 bytes c0035fd6
+ 00783454 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00783454 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00783454 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfdb29266ee58114238cc677d150f2c9"></a>

### [`00783130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783130.md) → [`0078350c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00783/0078350c.md) FUN_0078350c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "site": "00783130"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00783130"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00783148"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00783130",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078313c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58f30"
      ]
    ],
    [
      "unmatched:00783148",
      "DATA",
      [
        "storage",
        "00c78bf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078350c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00783518",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58f30"
      ]
    ],
    [
      "00783524",
      "DATA",
      [
        "storage",
        "00c79bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00783130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783130.md#insn-00783130) · [`0078313c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783130.md#insn-0078313c) · [`00783148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783130.md#insn-00783148)

~~~diff
- 00783130 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00783130 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00783130 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00783130 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00783130 bytes fd7bbfa9
- 0078313c ["INT_ADD", "register:40f0:8", ["const:78313c:8", "const:4:8"]]
- 0078313c ["CALL", null, ["callee:00c58f30:8"]]
- 0078313c bytes 89531394
- 00783148 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00783148 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00783148 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-026b19ac2051f0e917b5d84986ec8eb6"></a>

### [`00783420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783420.md) → [`007837fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00783/007837fc.md) FUN_007837fc

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "site": "00783438"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00783814"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00783440"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00783438",
      "DATA",
      [
        "storage",
        "00c78d70",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0078343c",
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
      "00783814",
      "DATA",
      [
        "storage",
        "00c79d40",
        null,
        "undefined *"
      ]
    ],
    [
      "00783818",
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

- 旧版 [`00783438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783420.md#insn-00783438) · [`00783440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783420.md#insn-00783440)
- 新版 [`00783814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00783/007837fc.md#insn-00783814)

~~~diff
- 00783438 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00783438 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00783438 bytes 080000f9
- 00783440 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00783440 ["RETURN", null, ["register:0:8"]]
- 00783440 bytes c0035fd6
+ 00783814 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00783814 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00783814 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5347132c52ce5b61f86843fe7b7edb1"></a>

### [`007836a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/007836a4.md) → [`00783a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00783/00783a80.md) FUN_00783a80

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md) [`00a1b6a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a1b/00a1b6a4.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.97% / 新版 68.97%

CFGの説明率　旧版 12.50% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007836a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007836a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007836a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007836a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:007836a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:007836c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00783a80",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00783a84",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00783aa4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007836a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/007836a4.md#insn-007836a4) · [`007836a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/007836a4.md#insn-007836a8) · [`007836c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/007836a4.md#insn-007836c8)

~~~diff
- 007836a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 007836a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 007836a4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 007836a4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 007836a4 bytes fd7bbea9
- 007836a8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 007836a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 007836a8 bytes f30b00f9
- 007836c8 ["INT_ADD", "register:40f0:8", ["const:7836c8:8", "const:4:8"]]
- 007836c8 ["CALL", null, ["ram:47ad34:8"]]
- 007836c8 bytes 9bddf397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1427b9705beadf65412a90e7f602f319"></a>

### [`00783744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783744.md) → [`00783b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00783/00783b20.md) FUN_00783b20

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "site": "0078375c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00783b38"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00783764"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0078375c",
      "DATA",
      [
        "storage",
        "00c78ef0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00783760",
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
      "00783b38",
      "DATA",
      [
        "storage",
        "00c79ec0",
        null,
        "undefined *"
      ]
    ],
    [
      "00783b3c",
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

- 旧版 [`0078375c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783744.md#insn-0078375c) · [`00783764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783744.md#insn-00783764)
- 新版 [`00783b38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00783/00783b20.md#insn-00783b38)

~~~diff
- 0078375c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0078375c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0078375c bytes 080000f9
- 00783764 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00783764 ["RETURN", null, ["register:0:8"]]
- 00783764 bytes c0035fd6
+ 00783b38 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00783b38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00783b38 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16ab77560944e804341f13ef7b29f32a"></a>

### [`00783780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783780.md) → [`00783b5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00783/00783b5c.md) FUN_00783b5c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0078379c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00783b78"
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
      "unmatched:0078379c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00783b78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078379c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783780.md#insn-0078379c) · [`00783788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783780.md#insn-00783788)
- 新版 [`00783b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00783/00783b5c.md#insn-00783b78) · [`00783b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00783/00783b5c.md#insn-00783b64)

~~~diff
- 0078379c ["INT_ADD", "register:40f0:8", ["const:78379c:8", "const:4:8"]]
- 0078379c ["CALL", null, ["ram:47ad34:8"]]
- 0078379c bytes 66ddf397
+ 00783b78 ["INT_ADD", "register:40f0:8", ["const:783b78:8", "const:4:8"]]
+ 00783b78 ["CALL", null, ["ram:47b054:8"]]
+ 00783b78 bytes 37ddf397
- 00783788 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00783788 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00783b64 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00783b64 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00783788 bytes a1010054
+ 00783b64 bytes a1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-692b327953ee489e20c6f36c50f0b0ed"></a>

### [`00784444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00784/00784444.md) → [`00784820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00784/00784820.md) FUN_00784820

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 37.50% / 新版 37.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00784444"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00784444"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00784448"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00784444",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00784448",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078446c",
      "DATA",
      [
        "storage",
        "00c79070",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00784820",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00784824",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00784848",
      "DATA",
      [
        "storage",
        "00c7a040",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00784444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00784/00784444.md#insn-00784444) · [`00784448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00784/00784444.md#insn-00784448) · [`0078446c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00784/00784444.md#insn-0078446c)

~~~diff
- 00784444 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00784444 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00784444 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00784444 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00784444 bytes fd7bbea9
- 00784448 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00784448 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00784448 bytes f30b00f9
- 0078446c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0078446c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0078446c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1744e02178c41d9653ecdb2e3544b56c"></a>

### [`00784cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00784/00784cb0.md) → [`0078508c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00785/0078508c.md) FUN_0078508c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00784cd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00784cdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00784ce0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00784cd8",
      "DATA",
      [
        "storage",
        "00c790e0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00784ce4",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00784ce8",
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
      "007850b4",
      "DATA",
      [
        "storage",
        "00c7a0b0",
        null,
        "undefined *"
      ]
    ],
    [
      "007850c0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "007850c4",
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

- 旧版 [`00784cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00784/00784cb0.md#insn-00784cd8) · [`00784cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00784/00784cb0.md#insn-00784cdc) · [`00784ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00784/00784cb0.md#insn-00784ce0)

~~~diff
- 00784cd8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00784cd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00784cd8 bytes 080000f9
- 00784cdc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00784cdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00784cdc bytes 0080803c
- 00784ce0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:18:8"]]
- 00784ce0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00784ce0 bytes 090c00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e848ef36b4beb459b4384d9b2c647beb"></a>

### [`00785184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00785/00785184.md) → [`00785560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00785/00785560.md) FUN_00785560

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "site": "007851a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007851a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00785584"
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
      "unmatched:007851a8",
      "DATA",
      [
        "storage",
        "00c79160",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:007851ac",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:007851b0",
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
      "00785584",
      "DATA",
      [
        "storage",
        "00c7a130",
        null,
        "undefined *"
      ]
    ],
    [
      "00785588",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0078558c",
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

- 旧版 [`007851a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00785/00785184.md#insn-007851a8) · [`007851b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00785/00785184.md#insn-007851b4)
- 新版 [`00785584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00785/00785560.md#insn-00785584)

~~~diff
- 007851a8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 007851a8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 007851a8 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 007851a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 007851a8 bytes 082400a9
- 007851b4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 007851b4 ["RETURN", null, ["register:0:8"]]
- 007851b4 bytes c0035fd6
+ 00785584 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00785584 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00785584 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00785584 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00785584 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64a6f95787fe6916c77a025ad8b2f70a"></a>

### [`007854e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00785/007854e4.md) → [`007858c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00785/007858c0.md) FUN_007858c0

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "site": "007854fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "007858d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00785504"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007854fc",
      "DATA",
      [
        "storage",
        "00c79270",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00785500",
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
      "007858d8",
      "DATA",
      [
        "storage",
        "00c7a240",
        null,
        "undefined *"
      ]
    ],
    [
      "007858dc",
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

- 旧版 [`007854fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00785/007854e4.md#insn-007854fc) · [`00785504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00785/007854e4.md#insn-00785504)
- 新版 [`007858d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00785/007858c0.md#insn-007858d8)

~~~diff
- 007854fc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 007854fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 007854fc bytes 080000f9
- 00785504 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00785504 ["RETURN", null, ["register:0:8"]]
- 00785504 bytes c0035fd6
+ 007858d8 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 007858d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 007858d8 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52019d17ab0563771fa48f6c8b94b323"></a>

### [`00785594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00785/00785594.md) → [`00785970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00785/00785970.md) FUN_00785970

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "site": "007855ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00785988"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "007855b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007855ac",
      "DATA",
      [
        "storage",
        "00c792f0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:007855b0",
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
      "00785988",
      "DATA",
      [
        "storage",
        "00c7a2c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0078598c",
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

- 旧版 [`007855ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00785/00785594.md#insn-007855ac) · [`007855b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00785/00785594.md#insn-007855b4)
- 新版 [`00785988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00785/00785970.md#insn-00785988)

~~~diff
- 007855ac ["COPY", "tmp:0:8", ["register:4000:8"]]
- 007855ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 007855ac bytes 080000f9
- 007855b4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 007855b4 ["RETURN", null, ["register:0:8"]]
- 007855b4 bytes c0035fd6
+ 00785988 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00785988 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00785988 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48d4c6e54b88583d001b93864cf5956a"></a>

### [`00785910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00785/00785910.md) → [`00785cec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00785/00785cec.md) FUN_00785cec

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00785934"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00785934"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00785d10"
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
      "unmatched:00785934",
      "DATA",
      [
        "storage",
        "00c79470",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00785938",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078593c",
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
      "00785d10",
      "DATA",
      [
        "storage",
        "00c7a440",
        null,
        "undefined *"
      ]
    ],
    [
      "00785d14",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00785d18",
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

- 旧版 [`00785934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00785/00785910.md#insn-00785934) · [`00785940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00785/00785910.md#insn-00785940)
- 新版 [`00785d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00785/00785cec.md#insn-00785d10)

~~~diff
- 00785934 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00785934 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00785934 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00785934 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00785934 bytes 082400a9
- 00785940 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00785940 ["RETURN", null, ["register:0:8"]]
- 00785940 bytes c0035fd6
+ 00785d10 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00785d10 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00785d10 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00785d10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00785d10 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b10762f907d23b608a9bd20256b94e45"></a>

### [`00786068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00786/00786068.md) → [`00786444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00786/00786444.md) FUN_00786444

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00764b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764b24.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00764f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764f00.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 36.36% / 新版 36.36%

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
      "site": "00786088"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078608c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00786464"
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
      "unmatched:00786074",
      "READ",
      [
        "storage",
        "002c4120",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00786450",
      "READ",
      [
        "storage",
        "002c4170",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00786088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00786/00786068.md#insn-00786088) · [`0078608c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00786/00786068.md#insn-0078608c) · [`00786090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00786/00786068.md#insn-00786090)

~~~diff
- 00786088 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:98:8"]]
- 00786088 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00786088 bytes 094c00f9
- 0078608c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:88:8"]]
- 0078608c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:8"]]
- 0078608c bytes 004400fd
- 00786090 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00786090 ["RETURN", null, ["register:0:8"]]
- 00786090 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7be32501bb74cf9083e0b312a77da342"></a>

### [`007874d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/007874d8.md) → [`007878b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00787/007878b4.md) FUN_007878b4

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007861a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00786/007861a4.md) [`00787854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787854.md) · 呼出先 4件 [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md) [`00a46944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46944.md) [`00a46c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46c0c.md)
- 新版 呼出元 2件 [`00786580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00786/00786580.md) [`00787c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00787/00787c30.md) · 呼出先 4件 [`008b7ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ea8.md) [`008b89cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b89cc.md) [`00a47938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47938.md) [`00a47c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47c00.md)

変更の種類 constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.11% / 新版 92.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007874e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007874e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "007878bc"
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
      "unmatched:007874e0",
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
      "007878bc",
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

- 旧版 [`007874e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/007874d8.md#insn-007874e0) · [`0078750c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/007874d8.md#insn-0078750c)
- 新版 [`007878bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00787/007878b4.md#insn-007878bc)

~~~diff
- 007874e0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 007874e0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 007874e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 007874e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 007874e0 bytes f44f02a9
- 0078750c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0078750c ["COPY", "tmp:1:4", ["register:4058:4"]]
- 0078750c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 0078750c ["COPY", "tmp:1:4", ["register:4050:4"]]
- 0078750c bytes 73118a1a
+ 007878bc ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 007878bc ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 007878bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
+ 007878bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 007878bc bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ead8c1bbdfd1ec98ea1795a5f009a534"></a>

### [`00787570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787570.md) → [`0078794c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00787/0078794c.md) FUN_0078794c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007861a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00786/007861a4.md) [`00787854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787854.md) · 呼出先 11件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`008003d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/008003d0.md) [`00802688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802688.md) [`00806220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00806/00806220.md) [`008062fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00806/008062fc.md)
- 新版 呼出元 2件 [`00786580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00786/00786580.md) [`00787c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00787/00787c30.md) · 呼出先 11件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00801334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00801/00801334.md) [`008035ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/008035ec.md) [`00807184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00807/00807184.md) [`00807260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00807/00807260.md)

変更の種類 call, call_argument_candidate, call_count, call_target, constant, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.28% / 新版 93.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0078759c",
      "incomplete_value": true,
      "site": "007875a8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4010:4"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "007875ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007879d8",
      "value": [
        "leaf",
        "ram:807184:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007875fc",
      "value": [
        "leaf",
        "ram:806220:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007875ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0080715c"
      ]
    ],
    [
      "007879d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00806220"
      ]
    ],
    [
      "00787aa0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008062fc"
      ]
    ]
  ],
  "added": [
    [
      "007879c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008080c0"
      ]
    ],
    [
      "007879d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00807184"
      ]
    ],
    [
      "00787aa0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00807260"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007875a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787570.md#insn-007875a8) · [`007875ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787570.md#insn-007875ec) · [`007875fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787570.md#insn-007875fc)
- 新版 [`00787984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00787/0078794c.md#insn-00787984) · [`007879d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00787/0078794c.md#insn-007879d8)

~~~diff
- 007875a8 ["INT_ADD", "register:40f0:8", ["const:7875a8:8", "const:4:8"]]
- 007875a8 ["CALL", null, ["callee:00801334:8"]]
+ 00787984 ["INT_ADD", "register:40f0:8", ["const:787984:8", "const:4:8"]]
+ 00787984 ["CALL", null, ["callee:00801334:8"]]
- 007875a8 bytes 8ae30194
+ 00787984 bytes 6ce60194
- 007875ec ["INT_ADD", "register:40f0:8", ["const:7875ec:8", "const:4:8"]]
- 007875ec ["CALL", null, ["ram:80715c:8"]]
- 007875ec bytes dcfe0194
- 007875fc ["INT_ADD", "register:40f0:8", ["const:7875fc:8", "const:4:8"]]
- 007875fc ["CALL", null, ["ram:806220:8"]]
+ 007879d8 ["INT_ADD", "register:40f0:8", ["const:7879d8:8", "const:4:8"]]
+ 007879d8 ["CALL", null, ["ram:807184:8"]]
- 007875fc bytes 09fb0194
+ 007879d8 bytes ebfd0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e674428a66678f39ca3d0a33869b7bd"></a>

### [`00787790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787790.md) → [`00787b6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00787/00787b6c.md) FUN_00787b6c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 2件 [`008b79a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b79a0.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)
- 新版 呼出元 1件 [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) · 呼出先 2件 [`008b894c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b894c.md) [`008b89cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b89cc.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 53.06% / 新版 53.06%

CFGの説明率　旧版 18.18% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "007877e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00787804"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00787bbc"
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
      "unmatched:007877ac",
      "READ",
      [
        "storage",
        "00ca3fdc",
        null,
        "undefined4"
      ]
    ],
    [
      "00787b98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:007877cc"
      ]
    ],
    [
      "unmatched:007877c8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b894c"
      ]
    ]
  ],
  "added": [
    [
      "00787b88",
      "READ",
      [
        "storage",
        "00ca4fac",
        null,
        "undefined4"
      ]
    ],
    [
      "00787b98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00787ba8"
      ]
    ],
    [
      "00787ba4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b894c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007877c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787790.md#insn-007877c8) · [`007877dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787790.md#insn-007877dc) · [`007877e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787790.md#insn-007877e0)

~~~diff
- 007877c8 ["INT_ADD", "register:40f0:8", ["const:7877c8:8", "const:4:8"]]
- 007877c8 ["CALL", null, ["callee:008b894c:8"]]
- 007877c8 bytes 76c00494
- 007877dc ["INT_ADD", "register:40f0:8", ["const:7877dc:8", "const:4:8"]]
- 007877dc ["CALL", null, ["callee:008b89cc:8"]]
- 007877dc bytes 91c00494
- 007877e0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 007877e0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 007877e0 bytes 800000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-846a03ce43f0520cbc6c236a69143094"></a>

### [`00787a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787a40.md) → [`00787e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00787/00787e1c.md) FUN_00787e1c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`00787b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787b78.md) [`0078858c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/0078858c.md) · 呼出先 3件 [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b6f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f98.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md)
- 新版 呼出元 3件 [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) [`00787f54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00787/00787f54.md) [`00788968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00788/00788968.md) · 呼出先 3件 [`008b7f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f1c.md) [`008b7f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f44.md) [`008b89cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b89cc.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 29.49% / 新版 29.49%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00787ab0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00787af0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00787b30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00787a5c",
      "READ",
      [
        "storage",
        "00ca3fdc",
        null,
        "undefined4"
      ]
    ],
    [
      "00787e4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00787a9c"
      ]
    ],
    [
      "unmatched:00787a7c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b89cc"
      ]
    ]
  ],
  "added": [
    [
      "00787e38",
      "READ",
      [
        "storage",
        "00ca4fac",
        null,
        "undefined4"
      ]
    ],
    [
      "00787e4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00787e78"
      ]
    ],
    [
      "00787e58",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b89cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00787a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787a40.md#insn-00787a7c) · [`00787a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787a40.md#insn-00787a84) · [`00787a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787a40.md#insn-00787a90)

~~~diff
- 00787a7c ["INT_ADD", "register:40f0:8", ["const:787a7c:8", "const:4:8"]]
- 00787a7c ["CALL", null, ["callee:008b89cc:8"]]
- 00787a7c bytes e9bf0494
- 00787a84 ["INT_ADD", "register:40f0:8", ["const:787a84:8", "const:4:8"]]
- 00787a84 ["CALL", null, ["callee:008b7f44:8"]]
- 00787a84 bytes 45bd0494
- 00787a90 ["INT_ADD", "register:40f0:8", ["const:787a90:8", "const:4:8"]]
- 00787a90 ["CALL", null, ["callee:008b89cc:8"]]
- 00787a90 bytes e4bf0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2fed5d239bfc5599e404807b51ba54e"></a>

### [`00787f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787f5c.md) → [`00788338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00788/00788338.md) FUN_00788338

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00787e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787e0c.md) · 呼出先 3件 [`00467b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b30.md) [`00468c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468c1c.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md)
- 新版 呼出元 1件 [`007881e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00788/007881e8.md) · 呼出先 3件 [`00467e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e50.md) [`00468f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468f3c.md) [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md)

変更の種類 call_argument_candidate, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.53% / 新版 97.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00788020",
      "incomplete_value": true,
      "site": "00788028",
      "value": [
        "live",
        "register:40a0:8"
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
      "definition_site": "00788024",
      "incomplete_value": false,
      "site": "00788028",
      "value": [
        "leaf",
        "const:1:8"
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00788420",
      "incomplete_value": true,
      "site": "00788440",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00788028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787f5c.md#insn-00788028) · [`00788064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787f5c.md#insn-00788064) · [`0078800c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00787/00787f5c.md#insn-0078800c)
- 新版 [`00788404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00788/00788338.md#insn-00788404) · [`00788440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00788/00788338.md#insn-00788440) · [`007883e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00788/00788338.md#insn-007883e8)

~~~diff
- 00788028 ["INT_ADD", "register:40f0:8", ["const:788028:8", "const:4:8"]]
- 00788028 ["CALL", null, ["callee:00467e50:8"]]
+ 00788404 ["INT_ADD", "register:40f0:8", ["const:788404:8", "const:4:8"]]
+ 00788404 ["CALL", null, ["callee:00467e50:8"]]
- 00788028 bytes c27ef397
+ 00788404 bytes 937ef397
- 00788064 ["INT_ADD", "register:40f0:8", ["const:788064:8", "const:4:8"]]
- 00788064 ["CALL", null, ["callee:00469f64:8"]]
+ 00788440 ["INT_ADD", "register:40f0:8", ["const:788440:8", "const:4:8"]]
+ 00788440 ["CALL", null, ["callee:00469f64:8"]]
- 00788064 bytes f886f397
+ 00788440 bytes c986f397
- 0078800c ["INT_ADD", "register:40f0:8", ["const:78800c:8", "const:4:8"]]
- 0078800c ["CALL", null, ["callee:00469f64:8"]]
+ 007883e8 ["INT_ADD", "register:40f0:8", ["const:7883e8:8", "const:4:8"]]
+ 007883e8 ["CALL", null, ["callee:00469f64:8"]]
- 0078800c bytes 0e87f397
+ 007883e8 bytes df86f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d515e0620f5a4696aa342424d3bffcc"></a>

### [`007880b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/007880b8.md) → [`00788494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00788/00788494.md) FUN_00788494

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00764b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764b24.md) · 呼出先 2件 [`0057bee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00764f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764f00.md) · 呼出先 2件 [`0057c208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c208.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.20% / 新版 90.20%

CFGの説明率　旧版 44.44% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00788114"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "007884f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0078813c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00788114",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078813c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00788528"
      ]
    ],
    [
      "unmatched:00788120",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "007884f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00788518",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00788528"
      ]
    ],
    [
      "007884fc",
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

- 旧版 [`00788114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/007880b8.md#insn-00788114) · [`00788120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/007880b8.md#insn-00788120) · [`0078813c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/007880b8.md#insn-0078813c)

~~~diff
- 00788114 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00788114 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00788114 bytes e81300f9
- 00788120 ["COPY", "register:0:8", ["register:4040:8"]]
- 00788120 ["INT_ADD", "register:40f0:8", ["const:788120:8", "const:4:8"]]
- 00788120 ["CALLIND", null, ["register:0:8"]]
- 00788120 bytes 00013fd6
- 0078813c ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 0078813c bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5851accd5387e5f86598d3b35fcbeaff"></a>

### [`00788254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/00788254.md) → [`00788630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00788/00788630.md) FUN_00788630

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "site": "00788278"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00788278"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00788654"
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
      "unmatched:00788278",
      "DATA",
      [
        "storage",
        "00c79580",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0078827c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00788280",
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
      "00788654",
      "DATA",
      [
        "storage",
        "00c7a550",
        null,
        "undefined *"
      ]
    ],
    [
      "00788658",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0078865c",
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

- 旧版 [`00788278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/00788254.md#insn-00788278) · [`00788284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/00788254.md#insn-00788284)
- 新版 [`00788654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00788/00788630.md#insn-00788654)

~~~diff
- 00788278 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00788278 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00788278 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00788278 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00788278 bytes 082400a9
- 00788284 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00788284 ["RETURN", null, ["register:0:8"]]
- 00788284 bytes c0035fd6
+ 00788654 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00788654 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00788654 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00788654 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00788654 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51db1033e943c3fe40a56e5bd916dab7"></a>

### [`0078880c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/0078880c.md) → [`00788be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00788/00788be8.md) FUN_00788be8

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00788184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/00788184.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00788560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00788/00788560.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.26% / 新版 93.26%

CFGの説明率　旧版 52.94% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00788878"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "007888a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "007888ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00788878",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:007888a8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:007888ec",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00788c54",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00788c84",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00788cc8",
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

- 旧版 [`00788878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/0078880c.md#insn-00788878) · [`007888a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/0078880c.md#insn-007888a8) · [`007888ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00788/0078880c.md#insn-007888ec)

~~~diff
- 00788878 ["COPY", "register:0:8", ["register:4040:8"]]
- 00788878 ["INT_ADD", "register:40f0:8", ["const:788878:8", "const:4:8"]]
- 00788878 ["CALLIND", null, ["register:0:8"]]
- 00788878 bytes 00013fd6
- 007888a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007888a8 ["INT_ADD", "register:40f0:8", ["const:7888a8:8", "const:4:8"]]
- 007888a8 ["CALLIND", null, ["register:0:8"]]
- 007888a8 bytes 00013fd6
- 007888ec ["COPY", "register:0:8", ["register:4040:8"]]
- 007888ec ["INT_ADD", "register:40f0:8", ["const:7888ec:8", "const:4:8"]]
- 007888ec ["CALLIND", null, ["register:0:8"]]
- 007888ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-449501892bc65fff13dfb31bd001d7a7"></a>

### [`0078dbb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dbb4.md) → [`0078df90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078d/0078df90.md) FUN_0078df90

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0078de24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078de24.md) [`0078deac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078deac.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 2件 [`0078e200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e200.md) [`0078e288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e288.md) · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 61.76% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078dbb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078dbb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078dbb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0078dbb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078dbb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078dbd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078dfd0"
      ]
    ]
  ],
  "added": [
    [
      "0078df90",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0078df94",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0078dfb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078dfd0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078dbb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dbb4.md#insn-0078dbb4) · [`0078dbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dbb4.md#insn-0078dbb8) · [`0078dbd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dbb4.md#insn-0078dbd8)

~~~diff
- 0078dbb4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0078dbb4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0078dbb4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0078dbb4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0078dbb4 bytes fd7bbea9
- 0078dbb8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0078dbb8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0078dbb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0078dbb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0078dbb8 bytes f44f01a9
- 0078dbd8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0078dbd8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 0078dbd8 bytes e00000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f92f4a3898714c993a85b65bf0bfbe4c"></a>

### [`0078dd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dd04.md) → [`0078e0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e0e0.md) FUN_0078e0e0

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`0078de24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078de24.md) [`0078deac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078deac.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00846924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846924.md) [`00846ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846ffc.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 10件 [`0078e200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e200.md) [`0078e288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e288.md) [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) [`008478d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/008478d0.md) [`00847fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00847/00847fa8.md) · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 81.48% / 新版 81.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0078ddec"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "0078e1c8"
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
      "unmatched:0078ddec",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0078e1c8",
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

- 旧版 [`0078ddec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dd04.md#insn-0078ddec) · [`0078dd24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dd04.md#insn-0078dd24)
- 新版 [`0078e1c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e0e0.md#insn-0078e1c8) · [`0078e100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e0e0.md#insn-0078e100)

~~~diff
- 0078ddec ["COPY", "register:0:8", ["register:4040:8"]]
- 0078ddec ["INT_ADD", "register:40f0:8", ["const:78ddec:8", "const:4:8"]]
- 0078ddec ["CALLIND", null, ["register:0:8"]]
- 0078ddec bytes 00013fd6
+ 0078e1c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0078e1c8 ["INT_ADD", "register:40f0:8", ["const:78e1c8:8", "const:4:8"]]
+ 0078e1c8 ["CALLIND", null, ["register:0:8"]]
+ 0078e1c8 bytes 00013fd6
- 0078dd24 ["INT_ADD", "register:40f0:8", ["const:78dd24:8", "const:4:8"]]
- 0078dd24 ["CALL", null, ["callee:00c54d90:8"]]
+ 0078e100 ["INT_ADD", "register:40f0:8", ["const:78e100:8", "const:4:8"]]
+ 0078e100 ["CALL", null, ["callee:00c54d90:8"]]
- 0078dd24 bytes 1f181394
+ 0078e100 bytes 241b1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0a449bdc3caffd9bfb065d4c1ac9dac"></a>

### [`0078de24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078de24.md) → [`0078e200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e200.md) FUN_0078e200

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) [`0046f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f01c.md) [`00682364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682364.md) [`0078dbb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dbb4.md) [`0078dd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078dd04.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0046ec04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ec04.md) [`0046f33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f33c.md) [`00682714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00682/00682714.md) [`0078df90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078d/0078df90.md) [`0078e0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e0e0.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.41% / 新版 79.41%

CFGの説明率　旧版 16.67% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078de3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078de6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0078e218"
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
      "unmatched:0078de3c",
      "DATA",
      [
        "storage",
        "00c79718",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0078de6c",
      "DATA",
      [
        "storage",
        "00c748e0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0078de70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078e278"
      ]
    ]
  ],
  "added": [
    [
      "0078e218",
      "DATA",
      [
        "storage",
        "00c7a6e8",
        null,
        "pointer"
      ]
    ],
    [
      "0078e248",
      "DATA",
      [
        "storage",
        "00c758b0",
        null,
        "pointer"
      ]
    ],
    [
      "0078e24c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078e278"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078de3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078de24.md#insn-0078de3c) · [`0078de6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078de24.md#insn-0078de6c) · [`0078de70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078de24.md#insn-0078de70)

~~~diff
- 0078de3c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0078de3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0078de3c bytes 080000f9
- 0078de6c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0078de6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0078de6c bytes 680200f9
- 0078de70 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 0078de70 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0078de70 bytes 740100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-838bddbb2841bda2f66c65bf0278e22f"></a>

### [`0078df40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078df40.md) → [`0078e31c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e31c.md) FUN_0078e31c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "site": "0078df64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078df64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0078e340"
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
      "unmatched:0078df64",
      "DATA",
      [
        "storage",
        "00c79738",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0078df68",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078df6c",
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
      "0078e340",
      "DATA",
      [
        "storage",
        "00c7a708",
        null,
        "undefined *"
      ]
    ],
    [
      "0078e344",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0078e348",
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

- 旧版 [`0078df64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078df40.md#insn-0078df64) · [`0078df70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078df40.md#insn-0078df70)
- 新版 [`0078e340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e31c.md#insn-0078e340)

~~~diff
- 0078df64 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0078df64 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0078df64 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0078df64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0078df64 bytes 082400a9
- 0078df70 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0078df70 ["RETURN", null, ["register:0:8"]]
- 0078df70 bytes c0035fd6
+ 0078e340 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0078e340 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 0078e340 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 0078e340 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0078e340 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e0dc2bed588589632256f46f5f02437"></a>

### [`0078e2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e2bc.md) → [`0078e698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e698.md) FUN_0078e698

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "0078e2c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078e2c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0078e6a4"
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
      "unmatched:0078e2c8",
      "DATA",
      [
        "storage",
        "00c797b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078e6a4",
      "DATA",
      [
        "storage",
        "00c7a788",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e2c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e2bc.md#insn-0078e2c8) · [`0078e2cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e2bc.md#insn-0078e2cc)
- 新版 [`0078e6a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e698.md#insn-0078e6a4)

~~~diff
- 0078e2c8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0078e2c8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0078e2c8 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 0078e2c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0078e2c8 bytes 292000a9
- 0078e2cc ["COPY", "register:0:8", ["register:40f0:8"]]
- 0078e2cc ["RETURN", null, ["register:0:8"]]
- 0078e2cc bytes c0035fd6
+ 0078e6a4 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0078e6a4 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 0078e6a4 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 0078e6a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0078e6a4 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-231af4460c7ae214b39bc9baf4a7812e"></a>

### [`0078e4dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e4dc.md) → [`0078e8b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e8b8.md) FUN_0078e8b8

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "0078e4e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078e4e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0078e8c4"
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
      "unmatched:0078e4e8",
      "DATA",
      [
        "storage",
        "00c79838",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078e8c4",
      "DATA",
      [
        "storage",
        "00c7a808",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e4dc.md#insn-0078e4e8) · [`0078e4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e4dc.md#insn-0078e4ec)
- 新版 [`0078e8c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e8b8.md#insn-0078e8c4)

~~~diff
- 0078e4e8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0078e4e8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0078e4e8 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 0078e4e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0078e4e8 bytes 292000a9
- 0078e4ec ["COPY", "register:0:8", ["register:40f0:8"]]
- 0078e4ec ["RETURN", null, ["register:0:8"]]
- 0078e4ec bytes c0035fd6
+ 0078e8c4 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0078e8c4 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 0078e8c4 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 0078e8c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0078e8c4 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea4b8e8cb5d6b97879743fc978706ea6"></a>

### [`0078e568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e568.md) → [`0078e944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e944.md) FUN_0078e944

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

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
      "site": "0078e58c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078e590"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0078e968"
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
      "unmatched:0078e58c",
      "DATA",
      [
        "storage",
        "00c798b8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0078e594",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078e598",
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
      "0078e968",
      "DATA",
      [
        "storage",
        "00c7a888",
        null,
        "undefined *"
      ]
    ],
    [
      "0078e970",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0078e974",
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

- 旧版 [`0078e58c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e568.md#insn-0078e58c) · [`0078e590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e568.md#insn-0078e590) · [`0078e59c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e568.md#insn-0078e59c)

~~~diff
- 0078e58c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0078e58c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0078e58c bytes 080000f9
- 0078e590 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 0078e590 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0078e590 bytes 0080803c
- 0078e59c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0078e59c ["RETURN", null, ["register:0:8"]]
- 0078e59c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2df1b48b7c09db0c2a4aa3f6576fec67"></a>

### [`0078e5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e5f0.md) → [`0078e9cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e9cc.md) FUN_0078e9cc

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "0078e614"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078e614"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0078e9f0"
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
      "unmatched:0078e614",
      "DATA",
      [
        "storage",
        "00c79938",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0078e618",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078e61c",
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
      "0078e9f0",
      "DATA",
      [
        "storage",
        "00c7a908",
        null,
        "undefined *"
      ]
    ],
    [
      "0078e9f4",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0078e9f8",
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

- 旧版 [`0078e614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e5f0.md#insn-0078e614) · [`0078e620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e5f0.md#insn-0078e620)
- 新版 [`0078e9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078e9cc.md#insn-0078e9f0)

~~~diff
- 0078e614 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0078e614 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0078e614 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0078e614 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0078e614 bytes 082400a9
- 0078e620 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0078e620 ["RETURN", null, ["register:0:8"]]
- 0078e620 bytes c0035fd6
+ 0078e9f0 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0078e9f0 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 0078e9f0 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 0078e9f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0078e9f0 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c4a6a65dee5123614dd03b7e527bbcf"></a>

### [`0078e6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e6e0.md) → [`0078eabc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078eabc.md) FUN_0078eabc

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "0078e6ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078e6ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0078eac8"
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
      "unmatched:0078e6ec",
      "DATA",
      [
        "storage",
        "00c799b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078eac8",
      "DATA",
      [
        "storage",
        "00c7a988",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e6ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e6e0.md#insn-0078e6ec) · [`0078e6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e6e0.md#insn-0078e6f0)
- 新版 [`0078eac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078eabc.md#insn-0078eac8)

~~~diff
- 0078e6ec ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0078e6ec ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0078e6ec ["COPY", "tmp:2:8", ["register:4008:8"]]
- 0078e6ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0078e6ec bytes 292000a9
- 0078e6f0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0078e6f0 ["RETURN", null, ["register:0:8"]]
- 0078e6f0 bytes c0035fd6
+ 0078eac8 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0078eac8 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 0078eac8 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 0078eac8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0078eac8 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29048c32d00b01e57aef3f0d5f3ef399"></a>

### [`0078e83c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e83c.md) → [`0078ec18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078ec18.md) FUN_0078ec18

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "site": "0078e860"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078e860"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0078ec3c"
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
      "unmatched:0078e860",
      "DATA",
      [
        "storage",
        "00c79a28",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0078e864",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078e868",
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
      "0078ec3c",
      "DATA",
      [
        "storage",
        "00c7a9f8",
        null,
        "undefined *"
      ]
    ],
    [
      "0078ec40",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0078ec44",
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

- 旧版 [`0078e860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e83c.md#insn-0078e860) · [`0078e86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e83c.md#insn-0078e86c)
- 新版 [`0078ec3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078ec18.md#insn-0078ec3c)

~~~diff
- 0078e860 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0078e860 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0078e860 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0078e860 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0078e860 bytes 082400a9
- 0078e86c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0078e86c ["RETURN", null, ["register:0:8"]]
- 0078e86c bytes c0035fd6
+ 0078ec3c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0078ec3c ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 0078ec3c ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 0078ec3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0078ec3c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d221236614d1c220cf71cbab0383aac0"></a>

### [`0078e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e91c.md) → [`0078ecf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078ecf8.md) FUN_0078ecf8

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "site": "0078e940"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0078ed1c"
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
      "unmatched:0078e940",
      "DATA",
      [
        "storage",
        "00c79ab8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078ed1c",
      "DATA",
      [
        "storage",
        "00c7aa88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e91c.md#insn-0078e940) · [`0078e930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e91c.md#insn-0078e930)
- 新版 [`0078ed1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078ecf8.md#insn-0078ed1c) · [`0078ed0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078ecf8.md#insn-0078ed0c)

~~~diff
- 0078e940 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0078e940 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0078e940 bytes 080000f9
+ 0078ed1c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 0078ed1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0078ed1c bytes 080000f9
- 0078e930 ["INT_ADD", "register:40f0:8", ["const:78e930:8", "const:4:8"]]
- 0078e930 ["CALL", null, ["callee:00c58f30:8"]]
+ 0078ed0c ["INT_ADD", "register:40f0:8", ["const:78ed0c:8", "const:4:8"]]
+ 0078ed0c ["CALL", null, ["callee:00c58f30:8"]]
- 0078e930 bytes 8c251394
+ 0078ed0c bytes 89281394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a6dff66571f10685def27f1ccd912ac"></a>

### [`0078e954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e954.md) → [`0078ed30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078ed30.md) FUN_0078ed30

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "0078e95c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078e964"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0078ed38"
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
      "unmatched:0078e95c",
      "DATA",
      [
        "storage",
        "00c79ab8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078ed38",
      "DATA",
      [
        "storage",
        "00c7aa88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e954.md#insn-0078e95c) · [`0078e964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e954.md#insn-0078e964) · [`0078e968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078e954.md#insn-0078e968)

~~~diff
- 0078e95c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 0078e95c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0078e95c bytes 280000f9
- 0078e964 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 0078e964 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0078e964 bytes 2080803c
- 0078e968 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0078e968 ["RETURN", null, ["register:0:8"]]
- 0078e968 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d618c89d940623e97bb18a63a1aeab7e"></a>

### [`0078eb68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078eb68.md) → [`0078ef44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078e/0078ef44.md) FUN_0078ef44

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

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
      "site": "0078eb70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078eb78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0078ef4c"
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
      "unmatched:0078eb70",
      "DATA",
      [
        "storage",
        "00c79b38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078ef4c",
      "DATA",
      [
        "storage",
        "00c7ab08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078eb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078eb68.md#insn-0078eb70) · [`0078eb78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078eb68.md#insn-0078eb78) · [`0078eb7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078eb68.md#insn-0078eb7c)

~~~diff
- 0078eb70 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 0078eb70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0078eb70 bytes 280000f9
- 0078eb78 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 0078eb78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0078eb78 bytes 2080803c
- 0078eb7c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0078eb7c ["RETURN", null, ["register:0:8"]]
- 0078eb7c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-606a105db8a712f9632c02cd1e0a4121"></a>

### [`0078ed94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078ed94.md) → [`0078f170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078f170.md) FUN_0078f170

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`0085bbc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085bbc8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0085cb74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085cb74.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0078f188",
      "incomplete_value": true,
      "site": "0078f190",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": {
      "definition_site": "0078edac",
      "incomplete_value": true,
      "site": "0078edb4",
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:8:8"
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
    "new": null,
    "old": {
      "definition_site": "0078eda4",
      "incomplete_value": false,
      "site": "0078edb4",
      "value": [
        "leaf",
        "const:5:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0078edb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078ed94.md#insn-0078edb4) · [`0078edac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078ed94.md#insn-0078edac) · [`0078edb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078ed94.md#insn-0078edb0)
- 新版 [`0078f190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078f170.md#insn-0078f190)

~~~diff
- 0078edb4 ["INT_ADD", "register:40f0:8", ["const:78edb4:8", "const:4:8"]]
- 0078edb4 ["CALL", null, ["callee:0085cb74:8"]]
+ 0078f190 ["INT_ADD", "register:40f0:8", ["const:78f190:8", "const:4:8"]]
+ 0078f190 ["CALL", null, ["callee:0085cb74:8"]]
- 0078edb4 bytes 85330394
+ 0078f190 bytes 79360394
- 0078edac ["COPY", "register:4000:8", ["register:4098:8"]]
- 0078edac bytes e00313aa
- 0078edb0 ["COPY", "tmp:0:8", ["const:f54:8"]]
- 0078edb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078edb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078edb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078edb0 bytes 14513d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0059d9a4b265cbe6295b4f4401cd1872"></a>

### [`0078f1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f1fc.md) → [`0078f5d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078f5d8.md) FUN_0078f5d8

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00847c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00847/00847c7c.md) [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 5件 [`005c1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1c30.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) [`00848c28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00848/00848c28.md) [`00852508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852508.md) · 呼出先 5件 [`005c1fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1fe0.md) [`00676e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676e50.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 59.56% / 新版 59.56%

CFGの説明率　旧版 34.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 15件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078f39c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0078f814"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0078f29c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0078f668",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0078f2a0"
      ]
    ],
    [
      "unmatched:0078f290",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "0078f640"
      ]
    ],
    [
      "unmatched:0078f29c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078f63c"
      ]
    ]
  ],
  "added": [
    [
      "0078f668",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078f67c"
      ]
    ],
    [
      "0078f66c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "0078f640"
      ]
    ],
    [
      "0078f678",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078f63c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078f29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f1fc.md#insn-0078f29c) · [`0078f2a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f1fc.md#insn-0078f2a4) · [`0078f2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f1fc.md#insn-0078f2b4)

~~~diff
- 0078f29c ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 0078f29c bytes 20feff54
- 0078f2a4 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 0078f2a4 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 0078f2a4 bytes 94ffffb4
- 0078f2b4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0078f2b4 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 0078f2b4 bytes 00ffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-157d6567120257eb546945707f560d8f"></a>

### [`0078f6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f6c0.md) → [`0078fa9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078fa9c.md) FUN_0078fa9c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 3件 [`00480b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480b78.md) [`00480c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480c28.md) [`004810d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/004810d8.md)
- 新版 呼出元 1件 [`00a2c310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2c/00a2c310.md) · 呼出先 3件 [`00480e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480e98.md) [`00480f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480f48.md) [`004813f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/004813f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 71.43% / 新版 76.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0078f6f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0078fad4"
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
      "unmatched:0078f6f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078faf8"
      ]
    ]
  ],
  "added": [
    [
      "0078fad4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078faf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078f6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f6c0.md#insn-0078f6f8) · [`0078f6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f6c0.md#insn-0078f6e8)
- 新版 [`0078fad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078fa9c.md#insn-0078fad4) · [`0078fac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078fa9c.md#insn-0078fac4)

~~~diff
- 0078f6f8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0078f6f8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 0078f6f8 bytes 21010054
+ 0078fad4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0078fad4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 0078fad4 bytes 21010054
- 0078f6e8 ["INT_ADD", "register:40f0:8", ["const:78f6e8:8", "const:4:8"]]
- 0078f6e8 ["CALL", null, ["callee:00480e98:8"]]
+ 0078fac4 ["INT_ADD", "register:40f0:8", ["const:78fac4:8", "const:4:8"]]
+ 0078fac4 ["CALL", null, ["callee:00480e98:8"]]
- 0078f6e8 bytes 24c5f397
+ 0078fac4 bytes f5c4f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a357669f7173753bc5d28eb33ac35b3"></a>

### [`0078fccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fccc.md) → [`007900a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00790/007900a8.md) FUN_007900a8

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0078fc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fc04.md) [`007906b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/007906b4.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`0078ffe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078ffe0.md) [`00790a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00790/00790a90.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.53% / 新版 85.53%

CFGの説明率　旧版 63.16% / 新版 63.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078fccc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078fccc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078fcd0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0078fccc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078fcd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078fcd4",
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
      "007900a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "007900ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "007900b0",
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

- 旧版 [`0078fccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fccc.md#insn-0078fccc) · [`0078fcd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fccc.md#insn-0078fcd0) · [`0078fcd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fccc.md#insn-0078fcd4)

~~~diff
- 0078fccc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0078fccc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0078fccc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 0078fccc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0078fccc bytes fd7bbba9
- 0078fcd0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0078fcd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 0078fcd0 bytes f90b00f9
- 0078fcd4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0078fcd4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0078fcd4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0078fcd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0078fcd4 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0949f16c498aef0490cf50bff321dc49"></a>

### [`00794198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794198.md) → [`00794574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794574.md) FUN_00794574

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 1件 [`008b79a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b79a0.md)
- 新版 呼出元 1件 [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) · 呼出先 1件 [`008b894c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b894c.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

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
      "site": "00794198"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00794198"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079419c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00794198",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079419c",
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
      "00794574",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00794578",
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

- 旧版 [`00794198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794198.md#insn-00794198) · [`0079419c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794198.md#insn-0079419c)
- 新版 [`00794574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794574.md#insn-00794574)

~~~diff
- 00794198 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00794198 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00794198 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00794198 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00794198 bytes fd7bbea9
- 0079419c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0079419c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0079419c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0079419c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079419c bytes f44f01a9
+ 00794574 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00794574 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00794574 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00794574 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00794574 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83edc669e0b54217f94a9a0221a61acd"></a>

### [`00794c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794c80.md) → [`0079505c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/0079505c.md) FUN_0079505c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00792a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792a20.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00794da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794da4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00792dfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00792/00792dfc.md) · 呼出先 4件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00795180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795180.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.26% / 新版 97.26%

CFGの説明率　旧版 64.00% / 新版 64.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00794d84"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00795160"
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
      "unmatched:00794d84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079517c"
      ]
    ]
  ],
  "added": [
    [
      "00795160",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079517c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00794d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794c80.md#insn-00794d84) · [`00794ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794c80.md#insn-00794ca8)
- 新版 [`00795160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/0079505c.md#insn-00795160) · [`00795084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/0079505c.md#insn-00795084)

~~~diff
- 00794d84 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00794d84 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00794d84 bytes e1000054
+ 00795160 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00795160 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
+ 00795160 bytes e1000054
- 00794ca8 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
+ 00795084 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00794ca8 bytes 80060054
+ 00795084 bytes 80060054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8f39980fa2f78b7dd207a2b3a6e24e1"></a>

### [`007951d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007951d4.md) → [`007955b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/007955b0.md) FUN_007955b0

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079025c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/0079025c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00790638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00790/00790638.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 57.14% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00795210"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "007955ec"
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
      "unmatched:00795210",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "007955ec",
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

- 旧版 [`00795210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007951d4.md#insn-00795210) · [`007951f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007951d4.md#insn-007951f4)
- 新版 [`007955ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/007955b0.md#insn-007955ec) · [`007955d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/007955b0.md#insn-007955d0)

~~~diff
- 00795210 ["COPY", "register:0:8", ["register:4040:8"]]
- 00795210 ["INT_ADD", "register:40f0:8", ["const:795210:8", "const:4:8"]]
- 00795210 ["CALLIND", null, ["register:0:8"]]
- 00795210 bytes 00013fd6
+ 007955ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 007955ec ["INT_ADD", "register:40f0:8", ["const:7955ec:8", "const:4:8"]]
+ 007955ec ["CALLIND", null, ["register:0:8"]]
+ 007955ec bytes 00013fd6
- 007951f4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 007951f4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 007955d0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 007955d0 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 007951f4 bytes 000100b4
+ 007955d0 bytes 000100b4
~~~


<a id="compare-ade972c9600e75399f84c9a351f574e0"></a>

### [`007954ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007954ac.md) → [`00795888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795888.md) FUN_00795888

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007952b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007952b0.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0079568c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/0079568c.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.75% / 新版 88.75%

CFGの説明率　旧版 25.93% / 新版 28.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007954bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007954bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00795898"
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
      "unmatched:007954bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:007954e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00795978"
      ]
    ],
    [
      "unmatched:0079553c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00795978"
      ]
    ]
  ],
  "added": [
    [
      "00795898",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "007958bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00795978"
      ]
    ],
    [
      "00795918",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00795978"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007954bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007954ac.md#insn-007954bc) · [`007954e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007954ac.md#insn-007954e0) · [`0079553c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007954ac.md#insn-0079553c)

~~~diff
- 007954bc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 007954bc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 007954bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 007954bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 007954bc bytes f44f04a9
- 007954e0 ["CBRANCH", null, ["local:b19:8", "register:101:1"]]
- 007954e0 bytes e0050054
- 0079553c ["CBRANCH", null, ["local:b19:8", "register:101:1"]]
- 0079553c bytes 00030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-937182a6527360da9a2a718625821316"></a>

### [`0079a898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a898.md) → [`0079ac74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079a/0079ac74.md) FUN_0079ac74

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0088c178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md) [`00a8a488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8a/00a8a488.md) · 呼出先 6件 [`0079a9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a9e8.md) [`0079d8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d8b4.md) [`0079d8b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d8b8.md) [`0079d93c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d93c.md) [`0079d940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d940.md)
- 新版 呼出元 2件 [`0088d124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d124.md) [`00a8b47c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a8b/00a8b47c.md) · 呼出先 6件 [`0079adc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079a/0079adc4.md) [`0079dc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dc90.md) [`0079dc94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dc94.md) [`0079dd18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dd18.md) [`0079dd1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dd1c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 73.58% / 新版 73.58%

CFGの説明率　旧版 72.22% / 新版 76.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079a8b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079a8c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079a8c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079a8b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079a8c0",
      "DATA",
      [
        "storage",
        "00c79e38",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0079a8c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0079ac90",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "0079ac9c",
      "DATA",
      [
        "storage",
        "00c7ae08",
        null,
        "undefined *"
      ]
    ],
    [
      "0079ac9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079a8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a898.md#insn-0079a8b4) · [`0079a8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a898.md#insn-0079a8c0) · [`0079a8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a898.md#insn-0079a8c8)

~~~diff
- 0079a8b4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0079a8b4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0079a8b4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0079a8b4 bytes a8831ff8
- 0079a8c0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0079a8c0 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 0079a8c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0079a8c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079a8c0 bytes e80303a9
- 0079a8c8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 0079a8c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0079a8c8 bytes e82b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2356a588fc6cf74ea50938fa24bfd35a"></a>

### [`0079afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079afe0.md) → [`0079b3bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079b3bc.md) FUN_0079b3bc

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079d8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d8bc.md) · 呼出先 4件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0079b168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b168.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0079dc98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dc98.md) · 呼出先 4件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0079b544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079b544.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.59% / 新版 90.59%

CFGの説明率　旧版 50.00% / 新版 47.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079affc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0079b3d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079b060"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079affc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079b0b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079b4bc"
      ]
    ],
    [
      "unmatched:0079b104",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079b540"
      ]
    ]
  ],
  "added": [
    [
      "0079b3d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0079b48c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079b4bc"
      ]
    ],
    [
      "0079b4e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079b540"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079affc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079afe0.md#insn-0079affc) · [`0079b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079afe0.md#insn-0079b060) · [`0079b0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079afe0.md#insn-0079b0b0)

~~~diff
- 0079affc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0079affc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0079affc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0079affc bytes a8831ff8
- 0079b060 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 0079b060 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0079b060 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 0079b060 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 0079b060 bytes 29b18a9a
- 0079b0b0 ["CBRANCH", null, ["local:b20:8", "register:101:1"]]
- 0079b0b0 bytes 80010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccd5abe0897e6d52dd268e7ce7d2527b"></a>

### [`0079bd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079bd14.md) → [`0079c0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079c0f0.md) FUN_0079c0f0

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079ba1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079ba1c.md) · 呼出先 6件 [`0079be60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079be60.md) [`0079dce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dce0.md) [`0079dce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dce4.md) [`0079dd64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dd64.md) [`0079dd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dd68.md)
- 新版 呼出元 1件 [`0079bdf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079bdf8.md) · 呼出先 6件 [`0079c23c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079c23c.md) [`0079e0bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e0bc.md) [`0079e0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e0c0.md) [`0079e140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e140.md) [`0079e144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e144.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 50.00% / 新版 47.37%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079bd30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079bd3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079bd3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079bd30",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079bd3c",
      "DATA",
      [
        "storage",
        "00c7a0c8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0079bd3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0079c10c",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "0079c118",
      "DATA",
      [
        "storage",
        "00c7b098",
        null,
        "undefined *"
      ]
    ],
    [
      "0079c118",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079bd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079bd14.md#insn-0079bd30) · [`0079bd3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079bd14.md#insn-0079bd3c) · [`0079bd44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079bd14.md#insn-0079bd44)

~~~diff
- 0079bd30 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0079bd30 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0079bd30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0079bd30 bytes a8831ff8
- 0079bd3c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0079bd3c ["COPY", "tmp:1:8", ["register:4000:8"]]
- 0079bd3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0079bd3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079bd3c bytes e80303a9
- 0079bd44 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 0079bd44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0079bd44 bytes e82b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-706199cf5c9449fd1922b0dd38234b77"></a>

### [`0079c8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c8c4.md) → [`0079cca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079cca0.md) FUN_0079cca0

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079be60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079be60.md) · 呼出先 5件 [`0054079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054079c.md) [`005a140c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a140c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0079c23c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079c23c.md) · 呼出先 5件 [`00540abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540abc.md) [`005a172c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a1/005a172c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.21% / 新版 98.21%

CFGの説明率　旧版 53.33% / 新版 53.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079c958"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0079cd34"
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
      "unmatched:0079c958",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079cd4c"
      ]
    ]
  ],
  "added": [
    [
      "0079cd34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079cd4c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079c958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c8c4.md#insn-0079c958) · [`0079c8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c8c4.md#insn-0079c8f0)
- 新版 [`0079cd34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079cca0.md#insn-0079cd34) · [`0079cccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079cca0.md#insn-0079cccc)

~~~diff
- 0079c958 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 0079c958 bytes c0000054
+ 0079cd34 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
+ 0079cd34 bytes c0000054
- 0079c8f0 ["INT_ADD", "register:40f0:8", ["const:79c8f0:8", "const:4:8"]]
- 0079c8f0 ["CALL", null, ["callee:00c58f30:8"]]
+ 0079cccc ["INT_ADD", "register:40f0:8", ["const:79cccc:8", "const:4:8"]]
+ 0079cccc ["CALL", null, ["callee:00c58f30:8"]]
- 0079c8f0 bytes 9ced1294
+ 0079cccc bytes 99f01294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3982be68a430b9f025bdac2b798a10ef"></a>

### [`0079d8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d8a0.md) → [`0079dc7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dc7c.md) FUN_0079dc7c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "0079d8ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079d8ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0079dc88"
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
      "unmatched:0079d8ac",
      "DATA",
      [
        "storage",
        "00c79e38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079dc88",
      "DATA",
      [
        "storage",
        "00c7ae08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d8a0.md#insn-0079d8ac) · [`0079d8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d8a0.md#insn-0079d8b0)
- 新版 [`0079dc88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dc7c.md#insn-0079dc88)

~~~diff
- 0079d8ac ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0079d8ac ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0079d8ac ["COPY", "tmp:2:8", ["register:4008:8"]]
- 0079d8ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079d8ac bytes 292000a9
- 0079d8b0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0079d8b0 ["RETURN", null, ["register:0:8"]]
- 0079d8b0 bytes c0035fd6
+ 0079dc88 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0079dc88 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 0079dc88 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 0079dc88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0079dc88 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7af0c7d71cf60a4e6a5b11e8799a6ef6"></a>

### [`0079d944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d944.md) → [`0079dd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dd20.md) FUN_0079dd20

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 92.86% / 新版 86.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079d9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d944.md#insn-0079d9a4) · [`0079d9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d944.md#insn-0079d9b4) · [`0079d9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d944.md#insn-0079d9b8)
- 新版 [`0079dd80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dd20.md#insn-0079dd80) · [`0079dd94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dd20.md#insn-0079dd94)

~~~diff
- 0079d9a4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0079d9a4 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 0079dd80 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 0079dd80 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 0079d9a4 bytes a00000b4
+ 0079dd80 bytes a00000b4
- 0079d9b4 ["COPY", "register:0:8", ["register:4008:8"]]
- 0079d9b4 ["BRANCHIND", null, ["register:0:8"]]
- 0079d9b4 bytes 20001fd6
- 0079d9b8 ["INT_ADD", "register:40f0:8", ["const:79d9b8:8", "const:4:8"]]
- 0079d9b8 ["CALL", null, ["callee:0045a0d4:8"]]
+ 0079dd94 ["INT_ADD", "register:40f0:8", ["const:79dd94:8", "const:4:8"]]
+ 0079dd94 ["CALL", null, ["callee:0045a0d4:8"]]
- 0079d9b8 bytes fff0f297
+ 0079dd94 bytes d0f0f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f8ae6bfc32e22b52d5999871eb02733"></a>

### [`0079dbd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dbd4.md) → [`0079dfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dfb0.md) FUN_0079dfb0

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "0079dbe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079dbe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0079dfbc"
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
      "unmatched:0079dbe0",
      "DATA",
      [
        "storage",
        "00c7a048",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079dfbc",
      "DATA",
      [
        "storage",
        "00c7b018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079dbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dbd4.md#insn-0079dbe0) · [`0079dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dbd4.md#insn-0079dbe4)
- 新版 [`0079dfbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dfb0.md#insn-0079dfbc)

~~~diff
- 0079dbe0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0079dbe0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0079dbe0 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 0079dbe0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079dbe0 bytes 292000a9
- 0079dbe4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0079dbe4 ["RETURN", null, ["register:0:8"]]
- 0079dbe4 bytes c0035fd6
+ 0079dfbc ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0079dfbc ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 0079dfbc ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 0079dfbc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0079dfbc bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38c3ce1d3c836f867df6bd8b6a046037"></a>

### [`0079dc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dc98.md) → [`0079e074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e074.md) FUN_0079e074

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "0079dcbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079dcbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0079e098"
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
      "unmatched:0079dcbc",
      "DATA",
      [
        "storage",
        "00c7a0c8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0079dcc0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079dcc4",
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
      "0079e098",
      "DATA",
      [
        "storage",
        "00c7b098",
        null,
        "undefined *"
      ]
    ],
    [
      "0079e09c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0079e0a0",
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

- 旧版 [`0079dcbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dc98.md#insn-0079dcbc) · [`0079dcc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dc98.md#insn-0079dcc8)
- 新版 [`0079e098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e074.md#insn-0079e098)

~~~diff
- 0079dcbc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0079dcbc ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0079dcbc ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0079dcbc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079dcbc bytes 082400a9
- 0079dcc8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0079dcc8 ["RETURN", null, ["register:0:8"]]
- 0079dcc8 bytes c0035fd6
+ 0079e098 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0079e098 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 0079e098 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 0079e098 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0079e098 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42b797219ac866826c463a1192d43d35"></a>

### [`0079df84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079df84.md) → [`0079e360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e360.md) FUN_0079e360

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

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
      "site": "0079df84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079df84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079df88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079df84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079df88",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079dfac",
      "DATA",
      [
        "storage",
        "00c7a1d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e360",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0079e364",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0079e388",
      "DATA",
      [
        "storage",
        "00c7b1a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079df84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079df84.md#insn-0079df84) · [`0079df88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079df84.md#insn-0079df88) · [`0079dfac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079df84.md#insn-0079dfac)

~~~diff
- 0079df84 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0079df84 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0079df84 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0079df84 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0079df84 bytes fd7bbea9
- 0079df88 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0079df88 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0079df88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0079df88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079df88 bytes f44f01a9
- 0079dfac ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0079dfac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0079dfac bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-867a6e155492e37bc71a81c005d50f2e"></a>

### [`0079e590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e590.md) → [`0079e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e96c.md) FUN_0079e96c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.57% / 新版 69.57%

CFGの説明率　旧版 35.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e590"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e590"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e594"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079e590",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079e594",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0079e990",
      "DATA",
      [
        "storage",
        "00c7a258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e96c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0079e970",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0079e990",
      "DATA",
      [
        "storage",
        "00c7b228",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e590.md#insn-0079e590) · [`0079e594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e590.md#insn-0079e594) · [`0079e5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e590.md#insn-0079e5d8)

~~~diff
- 0079e590 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0079e590 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0079e590 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0079e590 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0079e590 bytes fd7bbea9
- 0079e594 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0079e594 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0079e594 bytes f30b00f9
- 0079e5d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079e5d8 ["INT_ADD", "register:40f0:8", ["const:79e5d8:8", "const:4:8"]]
- 0079e5d8 ["CALLIND", null, ["register:0:8"]]
- 0079e5d8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2440c66b1b3bfe3cd69841cb3999f2a"></a>

### [`0079e720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e720.md) → [`0079eafc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079eafc.md) FUN_0079eafc

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079be60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079be60.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0079c23c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079c23c.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 55.56% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e73c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0079eb18"
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
      "unmatched:0079e73c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079eb28"
      ]
    ]
  ],
  "added": [
    [
      "0079eb18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079eb28"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e73c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e720.md#insn-0079e73c) · [`0079e734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e720.md#insn-0079e734)
- 新版 [`0079eb18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079eafc.md#insn-0079eb18)

~~~diff
- 0079e73c ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 0079e73c bytes 80000054
+ 0079eb18 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 0079eb18 bytes 80000054
- 0079e734 ["COPY", "tmp:0:8", ["const:10:8"]]
- 0079e734 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0079e734 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0079e734 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0079e734 bytes 69420091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0a0d8dfad1612dfd29c39700ea3031e"></a>

### [`0079e7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e7b8.md) → [`0079eb94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079eb94.md) FUN_0079eb94

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079a9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a9e8.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`0079adc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079a/0079adc4.md) · 呼出先 7件 [`00598230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598230.md) [`005b772c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b772c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.42% / 新版 84.42%

CFGの説明率　旧版 52.94% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e7bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e7bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e7c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079e7bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079e7c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079e7c4",
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
      "0079eb98",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0079eb9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0079eba0",
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

- 旧版 [`0079e7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e7b8.md#insn-0079e7bc) · [`0079e7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e7b8.md#insn-0079e7c0) · [`0079e7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e7b8.md#insn-0079e7c4)

~~~diff
- 0079e7bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0079e7bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0079e7bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0079e7bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079e7bc bytes fd7b01a9
- 0079e7c0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0079e7c0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0079e7c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0079e7c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079e7c0 bytes f85f02a9
- 0079e7c4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0079e7c4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0079e7c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0079e7c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079e7c4 bytes f65703a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2147b048fd3c8fd057cdd1b975fa788a"></a>

### [`0079e930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e930.md) → [`0079ed0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079ed0c.md) FUN_0079ed0c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 86.11% / 新版 86.11%

CFGの説明率　旧版 64.29% / 新版 64.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e958"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0079ed34"
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
      "unmatched:0079e958",
      "DATA",
      [
        "storage",
        "00c7a2d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079ed34",
      "DATA",
      [
        "storage",
        "00c7b2a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e930.md#insn-0079e958) · [`0079e944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e930.md#insn-0079e944)
- 新版 [`0079ed34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079ed0c.md#insn-0079ed34) · [`0079ed20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079ed0c.md#insn-0079ed20)

~~~diff
- 0079e958 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0079e958 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0079e958 bytes 680200f9
+ 0079ed34 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 0079ed34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0079ed34 bytes 680200f9
- 0079e944 ["COPY", "register:4040:8", ["const:c7a000:8"]]
+ 0079ed20 ["COPY", "register:4040:8", ["const:c7b000:8"]]
- 0079e944 bytes e8260090
+ 0079ed20 bytes e82600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e5d10e8f154512c3a8da62347626bdd"></a>

### [`0079ea4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ea4c.md) → [`0079ee28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079ee28.md) FUN_0079ee28

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.60% / 新版 76.60%

CFGの説明率　旧版 11.76% / 新版 11.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079ea4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079ea4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079ea50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079ea4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079ea50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079ea54",
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
      "0079ee28",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0079ee2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0079ee30",
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

- 旧版 [`0079ea4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ea4c.md#insn-0079ea4c) · [`0079ea50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ea4c.md#insn-0079ea50) · [`0079ea54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ea4c.md#insn-0079ea54)

~~~diff
- 0079ea4c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0079ea4c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0079ea4c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 0079ea4c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0079ea4c bytes fd7bbda9
- 0079ea50 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0079ea50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0079ea50 bytes f50b00f9
- 0079ea54 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0079ea54 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0079ea54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0079ea54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079ea54 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dba7403a2e993cbaf422146082c8a982"></a>

### [`0079ece4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ece4.md) → [`0079f0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f0c0.md) FUN_0079f0c0

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079a9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a9e8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0079adc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079a/0079adc4.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 33.33% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079ed04"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0079f0e0"
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
      "unmatched:0079ed04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079f0f0"
      ]
    ]
  ],
  "added": [
    [
      "0079f0e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079f0f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079ed04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ece4.md#insn-0079ed04) · [`0079ecf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ece4.md#insn-0079ecf8)
- 新版 [`0079f0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f0c0.md#insn-0079f0e0)

~~~diff
- 0079ed04 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 0079ed04 bytes 80000054
+ 0079f0e0 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 0079f0e0 bytes 80000054
- 0079ecf8 ["COPY", "tmp:0:8", ["const:40:8"]]
- 0079ecf8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0079ecf8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0079ecf8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0079ecf8 bytes 69020191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89257632c386c1f01572af9e3d76b827"></a>

### [`0079eee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079eee0.md) → [`0079f2bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f2bc.md) FUN_0079f2bc

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 25.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079eef8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0079f2d4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079eefc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079eef8",
      "DATA",
      [
        "storage",
        "00c7a358",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0079eefc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079f2e8"
      ]
    ]
  ],
  "added": [
    [
      "0079f2d4",
      "DATA",
      [
        "storage",
        "00c7b328",
        null,
        "undefined *"
      ]
    ],
    [
      "0079f2d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079f2e8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079eef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079eee0.md#insn-0079eef8) · [`0079eefc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079eee0.md#insn-0079eefc)
- 新版 [`0079f2d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f2bc.md#insn-0079f2d4)

~~~diff
- 0079eef8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0079eef8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 0079eef8 bytes 0a0100f9
- 0079eefc ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 0079eefc bytes 80000054
+ 0079f2d4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0079f2d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 0079f2d4 bytes 0a0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3ab2e4d907a748f2b2cc03e99d403fa"></a>

### [`0079ef24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ef24.md) → [`0079f300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f300.md) FUN_0079f300

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.91% / 新版 73.91%

CFGの説明率　旧版 25.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079ef48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0079f324"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079ef4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079ef48",
      "DATA",
      [
        "storage",
        "00c7a358",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0079ef4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079f338"
      ]
    ],
    [
      "unmatched:0079ef6c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0079f324",
      "DATA",
      [
        "storage",
        "00c7b328",
        null,
        "undefined *"
      ]
    ],
    [
      "0079f328",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079f338"
      ]
    ],
    [
      "0079f348",
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

- 旧版 [`0079ef48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ef24.md#insn-0079ef48) · [`0079ef4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ef24.md#insn-0079ef4c) · [`0079ef6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ef24.md#insn-0079ef6c)

~~~diff
- 0079ef48 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0079ef48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0079ef48 bytes 680200f9
- 0079ef4c ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 0079ef4c bytes 80000054
- 0079ef6c ["COPY", "register:0:8", ["register:4040:8"]]
- 0079ef6c ["INT_ADD", "register:40f0:8", ["const:79ef6c:8", "const:4:8"]]
- 0079ef6c ["CALLIND", null, ["register:0:8"]]
- 0079ef6c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79d0597387f685e04050ad7217dd283c"></a>

### [`0079f008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f008.md) → [`0079f3e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f3e4.md) FUN_0079f3e4

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 12.50% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f024"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0079f400"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f05c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079f024",
      "DATA",
      [
        "storage",
        "00c7a358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079f400",
      "DATA",
      [
        "storage",
        "00c7b328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f008.md#insn-0079f024) · [`0079f05c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f008.md#insn-0079f05c)
- 新版 [`0079f400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f3e4.md#insn-0079f400)

~~~diff
- 0079f024 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0079f024 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 0079f024 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 0079f024 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0079f024 bytes 290401f8
- 0079f05c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0079f05c ["RETURN", null, ["register:0:8"]]
- 0079f05c bytes c0035fd6
+ 0079f400 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0079f400 ["COPY", "tmp:1:8", ["register:4008:8"]]
+ 0079f400 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
+ 0079f400 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 0079f400 bytes 290401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7189e4073096722c649a265f816e71e8"></a>

### [`0079f0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f0b4.md) → [`0079f490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f490.md) FUN_0079f490

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079a9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a9e8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0079adc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079a/0079adc4.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 10.00% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f0d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0079f4ac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f0f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079f0d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079f4bc"
      ]
    ],
    [
      "unmatched:0079f0f0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0079f4ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079f4bc"
      ]
    ],
    [
      "0079f4cc",
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

- 旧版 [`0079f0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f0b4.md#insn-0079f0d0) · [`0079f0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f0b4.md#insn-0079f0f0)
- 新版 [`0079f4ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f490.md#insn-0079f4ac)

~~~diff
- 0079f0d0 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 0079f0d0 bytes 80000054
- 0079f0f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079f0f0 ["INT_ADD", "register:40f0:8", ["const:79f0f0:8", "const:4:8"]]
- 0079f0f0 ["CALLIND", null, ["register:0:8"]]
- 0079f0f0 bytes 00013fd6
+ 0079f4ac ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 0079f4ac bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d02242c61aa42e86c1fb5556e38b3aba"></a>

### [`0079f2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f2c4.md) → [`0079f6a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f6a0.md) FUN_0079f6a0

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 71.43% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f2ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0079f6c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f2f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079f2ec",
      "DATA",
      [
        "storage",
        "00c7a3d8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0079f2f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079f6dc"
      ]
    ]
  ],
  "added": [
    [
      "0079f6c8",
      "DATA",
      [
        "storage",
        "00c7b3a8",
        null,
        "undefined *"
      ]
    ],
    [
      "0079f6cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079f6dc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f2c4.md#insn-0079f2ec) · [`0079f2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f2c4.md#insn-0079f2f0)
- 新版 [`0079f6c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f6a0.md#insn-0079f6c8)

~~~diff
- 0079f2ec ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0079f2ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0079f2ec bytes 680200f9
- 0079f2f0 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 0079f2f0 bytes 80000054
+ 0079f6c8 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 0079f6c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0079f6c8 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe618d0414637a38881a3e31ca4eead3"></a>

### [`0079f354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f354.md) → [`0079f730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f730.md) FUN_0079f730

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.86% / 新版 82.86%

CFGの説明率　旧版 33.33% / 新版 31.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f37c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0079f758"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f380"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079f37c",
      "DATA",
      [
        "storage",
        "00c7a3d8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0079f380",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079f76c"
      ]
    ]
  ],
  "added": [
    [
      "0079f758",
      "DATA",
      [
        "storage",
        "00c7b3a8",
        null,
        "undefined *"
      ]
    ],
    [
      "0079f75c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079f76c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f354.md#insn-0079f37c) · [`0079f380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f354.md#insn-0079f380)
- 新版 [`0079f758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f730.md#insn-0079f758)

~~~diff
- 0079f37c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0079f37c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0079f37c bytes 680200f9
- 0079f380 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 0079f380 bytes 80000054
+ 0079f758 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 0079f758 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0079f758 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48171563ad29b8b22f5f0291f6144fe9"></a>

### [`0079f678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f678.md) → [`0079fa54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079fa54.md) FUN_0079fa54

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079b424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b424.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0079b800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079b800.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 62.50% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f698"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0079fa74"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f6e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079f698",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079fa84"
      ]
    ],
    [
      "unmatched:0079f6e4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0079fa74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079fa84"
      ]
    ],
    [
      "0079fac0",
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

- 旧版 [`0079f698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f678.md#insn-0079f698) · [`0079f6e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f678.md#insn-0079f6e4)
- 新版 [`0079fa74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079fa54.md#insn-0079fa74)

~~~diff
- 0079f698 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 0079f698 bytes 80000054
- 0079f6e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079f6e4 ["INT_ADD", "register:40f0:8", ["const:79f6e4:8", "const:4:8"]]
- 0079f6e4 ["CALLIND", null, ["register:0:8"]]
- 0079f6e4 bytes 00013fd6
+ 0079fa74 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 0079fa74 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-187a749a4cfebc51582530f717aec41f"></a>

### [`0079f6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f6f8.md) → [`0079fad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079fad4.md) FUN_0079fad4

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 98.39% / 新版 98.39%

CFGの説明率　旧版 54.17% / 新版 54.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f74c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "0079fb28"
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
      "0079fb18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079fb58"
      ]
    ],
    [
      "0079fb34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079fb58"
      ]
    ],
    [
      "0079fb44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079fbb4"
      ]
    ]
  ],
  "added": [
    [
      "0079fb18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079fbb4"
      ]
    ],
    [
      "0079fb34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079fbb4"
      ]
    ],
    [
      "0079fb44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079fb58"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f74c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f6f8.md#insn-0079f74c) · [`0079f730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f6f8.md#insn-0079f730)
- 新版 [`0079fb28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079fad4.md#insn-0079fb28) · [`0079fb0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079fad4.md#insn-0079fb0c)

~~~diff
- 0079f74c ["COPY", "register:0:8", ["register:4040:8"]]
- 0079f74c ["INT_ADD", "register:40f0:8", ["const:79f74c:8", "const:4:8"]]
- 0079f74c ["CALLIND", null, ["register:0:8"]]
- 0079f74c bytes 00013fd6
+ 0079fb28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079fb28 ["INT_ADD", "register:40f0:8", ["const:79fb28:8", "const:4:8"]]
+ 0079fb28 ["CALLIND", null, ["register:0:8"]]
+ 0079fb28 bytes 00013fd6
- 0079f730 ["INT_ADD", "register:40f0:8", ["const:79f730:8", "const:4:8"]]
- 0079f730 ["CALL", null, ["callee:00c54d60:8"]]
+ 0079fb0c ["INT_ADD", "register:40f0:8", ["const:79fb0c:8", "const:4:8"]]
+ 0079fb0c ["CALL", null, ["callee:00c54d60:8"]]
- 0079f730 bytes 90d11294
+ 0079fb0c bytes 95d41294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59dfcacfd4a41bdbeca3de09e7f86bf0"></a>

### [`0079f88c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f88c.md) → [`0079fc68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079fc68.md) FUN_0079fc68

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 52.94% / 新版 52.94%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f8a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0079fc80"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f8a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079f8a4",
      "DATA",
      [
        "storage",
        "00c7a458",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0079f8a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079fc94"
      ]
    ]
  ],
  "added": [
    [
      "0079fc80",
      "DATA",
      [
        "storage",
        "00c7b428",
        null,
        "undefined *"
      ]
    ],
    [
      "0079fc84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079fc94"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f8a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f88c.md#insn-0079f8a4) · [`0079f8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f88c.md#insn-0079f8a8)
- 新版 [`0079fc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079fc68.md#insn-0079fc80)

~~~diff
- 0079f8a4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0079f8a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 0079f8a4 bytes 0a0100f9
- 0079f8a8 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 0079f8a8 bytes 80000054
+ 0079fc80 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0079fc80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 0079fc80 bytes 0a0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc48ac05c61e989187bee231262488cd"></a>

### [`0079f8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f8d0.md) → [`0079fcac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079fcac.md) FUN_0079fcac

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 52.17% / 新版 52.17%

CFGの説明率　旧版 62.50% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f8d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f8d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f8d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079f8d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079f8d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079f8f4",
      "DATA",
      [
        "storage",
        "00c7a458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079fcac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0079fcb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0079fcd0",
      "DATA",
      [
        "storage",
        "00c7b428",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079f8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f8d0.md#insn-0079f8d0) · [`0079f8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f8d0.md#insn-0079f8d4) · [`0079f8f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f8d0.md#insn-0079f8f4)

~~~diff
- 0079f8d0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0079f8d0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0079f8d0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0079f8d0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0079f8d0 bytes fd7bbea9
- 0079f8d4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0079f8d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0079f8d4 bytes f30b00f9
- 0079f8f4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 0079f8f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0079f8f4 bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b110a956b4e1a823780f1b94f81e069"></a>

### [`0079fa60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fa60.md) → [`0079fe3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079fe3c.md) FUN_0079fe3c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079b424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b424.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0079b800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079b800.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 55.00% / 新版 55.00%

CFGの説明率　旧版 12.50% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079fa60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079fa60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079fa64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079fa60",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079fa64",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079fa7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079fe68"
      ]
    ]
  ],
  "added": [
    [
      "0079fe3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0079fe40",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0079fe58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079fe68"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079fa60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fa60.md#insn-0079fa60) · [`0079fa64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fa60.md#insn-0079fa64) · [`0079fa7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fa60.md#insn-0079fa7c)

~~~diff
- 0079fa60 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0079fa60 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0079fa60 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0079fa60 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0079fa60 bytes fd7bbea9
- 0079fa64 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0079fa64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0079fa64 bytes f30b00f9
- 0079fa7c ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 0079fa7c bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3618a22ef4fb0230b4d17cbca03e1e98"></a>

### [`0079fab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fab0.md) → [`0079fe8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079fe8c.md) FUN_0079fe8c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079fac4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079fac4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0079fea0"
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
      "unmatched:0079fab4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0079fac4"
      ]
    ],
    [
      "unmatched:0079fac4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079facc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0045a0d4"
      ]
    ]
  ],
  "added": [
    [
      "0079fe90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079fea0"
      ]
    ],
    [
      "0079fea0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0079fea8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0045a0d4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079fab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fab0.md#insn-0079fab4) · [`0079fac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fab0.md#insn-0079fac4) · [`0079facc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fab0.md#insn-0079facc)

~~~diff
- 0079fab4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0079fab4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0079fab4 bytes 800000b4
- 0079fac4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0079fac4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0079fac4 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 0079fac4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0079fac4 bytes fd7bbfa9
- 0079facc ["INT_ADD", "register:40f0:8", ["const:79facc:8", "const:4:8"]]
- 0079facc ["CALL", null, ["callee:0045a0d4:8"]]
- 0079facc bytes bae8f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5c97d7bf4c9a0a7e6211c7e09beedf9"></a>

### [`007ac738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac738.md) → [`007acb5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007ac/007acb5c.md) FUN_007acb5c

採用 · 移動量 `+0x424` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007ac418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac418.md) · 呼出先 6件 [`007ad37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad37c.md) [`007aec94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aec94.md) [`007aec98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aec98.md) [`007aed18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed18.md) [`007aed1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed1c.md)
- 新版 呼出元 1件 [`007ac83c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007ac/007ac83c.md) · 呼出先 6件 [`007ad7a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007ad/007ad7a0.md) [`007af478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af478.md) [`007af47c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af47c.md) [`007af4fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af4fc.md) [`007af500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af500.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.85% / 新版 78.85%

CFGの説明率　旧版 45.00% / 新版 40.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007ac760"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007ac760"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007ac768"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007ac760",
      "DATA",
      [
        "storage",
        "00c7a668",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:007ac760",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:007ac768",
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
      "007acb84",
      "DATA",
      [
        "storage",
        "00c7b638",
        null,
        "undefined *"
      ]
    ],
    [
      "007acb84",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "007acb8c",
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

- 旧版 [`007ac760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac738.md#insn-007ac760) · [`007ac768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac738.md#insn-007ac768) · [`007ac774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac738.md#insn-007ac774)

~~~diff
- 007ac760 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 007ac760 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 007ac760 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 007ac760 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 007ac760 bytes e80303a9
- 007ac768 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 007ac768 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 007ac768 bytes e82b00f9
- 007ac774 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 007ac774 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 007ac774 ["COPY", "tmp:2:8", ["register:8:8"]]
- 007ac774 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 007ac774 bytes e80300a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f245f9a7de3acf6d1402510aed82856"></a>

### [`007ae85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae85c.md) → [`007af040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af040.md) FUN_007af040

採用 · 移動量 `+0x7e4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "site": "007ae880"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007ae880"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "007af064"
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
      "unmatched:007ae880",
      "DATA",
      [
        "storage",
        "00c7a568",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:007ae884",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:007ae888",
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
      "007af064",
      "DATA",
      [
        "storage",
        "00c7b538",
        null,
        "undefined *"
      ]
    ],
    [
      "007af068",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "007af06c",
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

- 旧版 [`007ae880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae85c.md#insn-007ae880) · [`007ae88c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae85c.md#insn-007ae88c)
- 新版 [`007af064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af040.md#insn-007af064)

~~~diff
- 007ae880 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 007ae880 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 007ae880 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 007ae880 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 007ae880 bytes 082400a9
- 007ae88c ["COPY", "register:0:8", ["register:40f0:8"]]
- 007ae88c ["RETURN", null, ["register:0:8"]]
- 007ae88c bytes c0035fd6
+ 007af064 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 007af064 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 007af064 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 007af064 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 007af064 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4324feadb60ec81e40006f62dc77848"></a>

### [`007ae8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae8ac.md) → [`007af090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af090.md) FUN_007af090

採用 · 移動量 `+0x7e4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`00493914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493914.md) [`007ae9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae9e8.md) [`007ae9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae9ec.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`00493c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493c34.md) [`007af1cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af1cc.md) [`007af1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af1d0.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 27.27% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007ae8d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007ae8dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "007af0bc"
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
      "unmatched:007ae8c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "unmatched:007ae8d8",
      "DATA",
      [
        "storage",
        "00c7a5e8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:007ae8d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "007af0ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048d058"
      ]
    ],
    [
      "007af0bc",
      "DATA",
      [
        "storage",
        "00c7b5b8",
        null,
        "undefined *"
      ]
    ],
    [
      "007af0bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ae8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae8ac.md#insn-007ae8c8) · [`007ae8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae8ac.md#insn-007ae8d8) · [`007ae8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae8ac.md#insn-007ae8dc)

~~~diff
- 007ae8c8 ["INT_ADD", "register:40f0:8", ["const:7ae8c8:8", "const:4:8"]]
- 007ae8c8 ["CALL", null, ["ram:48cd38:8"]]
- 007ae8c8 bytes 1c79f397
- 007ae8d8 ["COPY", "tmp:0:8", ["register:8:8"]]
- 007ae8d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 007ae8d8 bytes e80300f9
- 007ae8dc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 007ae8dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 007ae8dc bytes f31300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f836a480a1a349e4e2923c046e35ce8"></a>

### [`007ae9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae9b4.md) → [`007af198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af198.md) FUN_007af198

採用 · 移動量 `+0x7e4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "site": "007ae9cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "007af1b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "007ae9d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007ae9cc",
      "DATA",
      [
        "storage",
        "00c7a5e8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:007ae9d0",
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
      "007af1b0",
      "DATA",
      [
        "storage",
        "00c7b5b8",
        null,
        "undefined *"
      ]
    ],
    [
      "007af1b4",
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

- 旧版 [`007ae9cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae9b4.md#insn-007ae9cc) · [`007ae9d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007ae9b4.md#insn-007ae9d4)
- 新版 [`007af1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af198.md#insn-007af1b0)

~~~diff
- 007ae9cc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 007ae9cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 007ae9cc bytes 080000f9
- 007ae9d4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 007ae9d4 ["RETURN", null, ["register:0:8"]]
- 007ae9d4 bytes c0035fd6
+ 007af1b0 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 007af1b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 007af1b0 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5743ba121afa8630bafec05c9065b7e4"></a>

### [`007aec4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aec4c.md) → [`007af430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af430.md) FUN_007af430

採用 · 移動量 `+0x7e4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "site": "007aec70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007aec70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "007af454"
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
      "unmatched:007aec70",
      "DATA",
      [
        "storage",
        "00c7a668",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:007aec74",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:007aec78",
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
      "007af454",
      "DATA",
      [
        "storage",
        "00c7b638",
        null,
        "undefined *"
      ]
    ],
    [
      "007af458",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "007af45c",
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

- 旧版 [`007aec70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aec4c.md#insn-007aec70) · [`007aec7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aec4c.md#insn-007aec7c)
- 新版 [`007af454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af430.md#insn-007af454)

~~~diff
- 007aec70 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 007aec70 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 007aec70 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 007aec70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 007aec70 bytes 082400a9
- 007aec7c ["COPY", "register:0:8", ["register:40f0:8"]]
- 007aec7c ["RETURN", null, ["register:0:8"]]
- 007aec7c bytes c0035fd6
+ 007af454 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 007af454 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 007af454 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 007af454 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 007af454 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39d9392cff6b288af42c73e1177e45ec"></a>

### [`007aecd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aecd0.md) → [`007af4b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af4b4.md) FUN_007af4b4

採用 · 移動量 `+0x7e4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "site": "007aecf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007aecf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "007af4d8"
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
      "unmatched:007aecf4",
      "DATA",
      [
        "storage",
        "00c7a6e8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:007aecf8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:007aecfc",
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
      "007af4d8",
      "DATA",
      [
        "storage",
        "00c7b6b8",
        null,
        "undefined *"
      ]
    ],
    [
      "007af4dc",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "007af4e0",
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

- 旧版 [`007aecf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aecd0.md#insn-007aecf4) · [`007aed00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aecd0.md#insn-007aed00)
- 新版 [`007af4d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af4b4.md#insn-007af4d8)

~~~diff
- 007aecf4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 007aecf4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 007aecf4 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 007aecf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 007aecf4 bytes 082400a9
- 007aed00 ["COPY", "register:0:8", ["register:40f0:8"]]
- 007aed00 ["RETURN", null, ["register:0:8"]]
- 007aed00 bytes c0035fd6
+ 007af4d8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 007af4d8 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 007af4d8 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 007af4d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 007af4d8 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-977c1b31eb027ceaae382d8beea32e21"></a>

### [`007aed78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed78.md) → [`007af55c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af55c.md) FUN_007af55c

採用 · 移動量 `+0x7e4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "007aed80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "007af564"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "007aed84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007aed80",
      "DATA",
      [
        "storage",
        "00c7a768",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af564",
      "DATA",
      [
        "storage",
        "00c7b738",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aed80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed78.md#insn-007aed80) · [`007aed84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed78.md#insn-007aed84)
- 新版 [`007af564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af55c.md#insn-007af564)

~~~diff
- 007aed80 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 007aed80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 007aed80 bytes 280000f9
- 007aed84 ["COPY", "register:0:8", ["register:40f0:8"]]
- 007aed84 ["RETURN", null, ["register:0:8"]]
- 007aed84 bytes c0035fd6
+ 007af564 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 007af564 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 007af564 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a96d9da3a975c8e665f25d7a57c38ada"></a>

### [`007aee50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aee50.md) → [`007af634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af634.md) FUN_007af634

採用 · 移動量 `+0x7e4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

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
      "site": "007aee5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "007af640"
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
      "unmatched:007aee5c",
      "DATA",
      [
        "storage",
        "00c7a7e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af640",
      "DATA",
      [
        "storage",
        "00c7b7b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aee5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aee50.md#insn-007aee5c) · [`007aee50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aee50.md#insn-007aee50)
- 新版 [`007af640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af634.md#insn-007af640)

~~~diff
- 007aee5c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 007aee5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 007aee5c bytes 090000f9
+ 007af640 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 007af640 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 007af640 bytes 090000f9
- 007aee50 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 007aee50 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 007aee50 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 007aee50 bytes 08204039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5f5ba86b15dbd2a18643e5c8cf266c8"></a>

### [`007aef24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aef24.md) → [`007af708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af708.md) FUN_007af708

採用 · 移動量 `+0x7e4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

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
      "site": "007aef2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "007af710"
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
      "unmatched:007aef2c",
      "DATA",
      [
        "storage",
        "00c7a7e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af710",
      "DATA",
      [
        "storage",
        "00c7b7b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aef2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aef24.md#insn-007aef2c) · [`007aef24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aef24.md#insn-007aef24)
- 新版 [`007af710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af708.md#insn-007af710)

~~~diff
- 007aef2c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 007aef2c ["COPY", "tmp:1:8", ["register:4008:8"]]
- 007aef2c ["INT_ADD", "register:4008:8", ["register:4008:8", "const:8:8"]]
- 007aef2c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 007aef2c bytes 288400f8
+ 007af710 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 007af710 ["COPY", "tmp:1:8", ["register:4008:8"]]
+ 007af710 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:8:8"]]
+ 007af710 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 007af710 bytes 288400f8
- 007aef24 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 007aef24 bytes 68260090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acb753b354eb90ae70bfa0b095de3020"></a>

### [`007aefa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aefa8.md) → [`007af78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af78c.md) FUN_007af78c

採用 · 移動量 `+0x7e4` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`00492f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492f68.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`00493288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493288.md)

変更の種類 call, call_count, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "007aefb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "007af79c"
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
      "unmatched:007aefb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ],
  "added": [
    [
      "007af79c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048d058"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aefb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aefa8.md#insn-007aefb8)
- 新版 [`007af79c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007af78c.md#insn-007af79c)

~~~diff
- 007aefb8 ["INT_ADD", "register:40f0:8", ["const:7aefb8:8", "const:4:8"]]
- 007aefb8 ["CALL", null, ["ram:48cd38:8"]]
- 007aefb8 bytes 6077f397
+ 007af79c ["INT_ADD", "register:40f0:8", ["const:7af79c:8", "const:4:8"]]
+ 007af79c ["CALL", null, ["ram:48d058:8"]]
+ 007af79c bytes 2f76f397
~~~


<a id="compare-0dab21116eee2f327fd007effeb9230f"></a>

### [`007af344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af344.md) → [`007afd68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007afd68.md) FUN_007afd68

採用 · 移動量 `+0xa24` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 78.26% / 新版 78.26%

CFGの説明率　旧版 55.56% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007af368"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "007afd8c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "007af36c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007af368",
      "DATA",
      [
        "storage",
        "00c7a968",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:007af36c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007afda0"
      ]
    ]
  ],
  "added": [
    [
      "007afd8c",
      "DATA",
      [
        "storage",
        "00c7b938",
        null,
        "undefined *"
      ]
    ],
    [
      "007afd90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007afda0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af344.md#insn-007af368) · [`007af36c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af344.md#insn-007af36c)
- 新版 [`007afd8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007af/007afd68.md#insn-007afd8c)

~~~diff
- 007af368 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 007af368 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 007af368 bytes 680200f9
- 007af36c ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 007af36c bytes 80000054
+ 007afd8c ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 007afd8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 007afd8c bytes 680200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

